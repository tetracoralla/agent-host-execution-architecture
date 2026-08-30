from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryCheckerTests(unittest.TestCase):
    def isolated_copy(self) -> Path:
        temporary_directory = tempfile.mkdtemp(prefix="check-repository-test-")
        self.addCleanup(shutil.rmtree, temporary_directory, True)
        isolated_root = Path(temporary_directory) / ROOT.name
        shutil.copytree(
            ROOT,
            isolated_root,
            ignore=shutil.ignore_patterns(".git", ".verify", "build", "__pycache__"),
        )
        return isolated_root

    def run_checker(self, isolated_root: Path, *flags: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/check_repository.py", *flags],
            cwd=isolated_root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_missing_siblings_are_disclosed_locally_and_rejected_strictly(self) -> None:
        isolated_root = self.isolated_copy()
        command = [sys.executable, "scripts/check_repository.py"]

        local = self.run_checker(isolated_root)
        self.assertEqual(local.returncode, 0, local.stderr)
        self.assertIn("sibling digest verification incomplete", local.stdout)

        strict = self.run_checker(isolated_root, "--require-sibling-contracts")
        self.assertEqual(strict.returncode, 1, strict.stdout)
        self.assertIn("required sibling contract files are unavailable", strict.stderr)

    def test_tampered_sibling_document_fails_digest_verification(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set = json.loads(
            (isolated_root / "compatibility/experimental-contract-set.v0.2.json").read_text(encoding="utf-8")
        )
        repository = contract_set["repositories"][0]
        sibling_file = isolated_root.parent / repository["id"] / repository["documents"][0]["file"]
        sibling_file.parent.mkdir(parents=True, exist_ok=True)
        sibling_file.write_text('{"schemaVersion": "tampered"}\n', encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("digest drift", result.stderr)

    def test_personal_path_in_public_text_fails(self) -> None:
        isolated_root = self.isolated_copy()
        readme = isolated_root / "README.md"
        leaked_path = "/Users/" + "openadam" + "/Development/tools-dev"
        readme.write_text(
            readme.read_text(encoding="utf-8") + f"\nLocal checkout: {leaked_path}\n",
            encoding="utf-8",
        )

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("forbidden public text is present", result.stderr)

    def test_personal_path_in_contract_set_fails(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set_path = isolated_root / "compatibility/experimental-contract-set.v0.2.json"
        contract_set = json.loads(contract_set_path.read_text(encoding="utf-8"))
        contract_set["publication"]["description"] = "/".join(
            ("", "Users", "openadam", "Development", "private")
        )
        contract_set_path.write_text(json.dumps(contract_set, indent=2) + "\n", encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("forbidden public text is present", result.stderr)

    def test_document_mapping_drift_fails_without_siblings(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set_path = isolated_root / "compatibility/experimental-contract-set.v0.2.json"
        contract_set = json.loads(contract_set_path.read_text(encoding="utf-8"))
        contract_set["repositories"][0]["documents"][0]["file"] = "schemas/wrong.json"
        contract_set_path.write_text(json.dumps(contract_set, indent=2) + "\n", encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("document mapping drift", result.stderr)

    def test_protocol_drift_fails(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set_path = isolated_root / "compatibility/experimental-contract-set.v0.2.json"
        contract_set = json.loads(contract_set_path.read_text(encoding="utf-8"))
        contract_set["repositories"][0]["protocols"] = ["openadam.capability-jsonl.v9"]
        contract_set_path.write_text(json.dumps(contract_set, indent=2) + "\n", encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("protocol drift", result.stderr)

    def test_invalid_contract_set_json_fails_without_traceback(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set_path = isolated_root / "compatibility/experimental-contract-set.v0.2.json"
        contract_set_path.write_text("{\n", encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("invalid JSON", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_draft_contract_set_rejects_release_anchors(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set_path = isolated_root / "compatibility/experimental-contract-set.v0.2.json"
        contract_set = json.loads(contract_set_path.read_text(encoding="utf-8"))
        contract_set["repositories"][0]["revision"] = "a" * 40
        contract_set_path.write_text(json.dumps(contract_set, indent=2) + "\n", encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("must not carry release anchors", result.stderr)

    def test_published_bound_without_release_anchor_fails(self) -> None:
        isolated_root = self.isolated_copy()
        contract_set_path = isolated_root / "compatibility/experimental-contract-set.v0.2.json"
        contract_set = json.loads(contract_set_path.read_text(encoding="utf-8"))
        contract_set["publication"] = {"status": "published-bound"}
        contract_set_path.write_text(json.dumps(contract_set, indent=2) + "\n", encoding="utf-8")

        result = self.run_checker(isolated_root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("release tag", result.stderr)


if __name__ == "__main__":
    unittest.main()
