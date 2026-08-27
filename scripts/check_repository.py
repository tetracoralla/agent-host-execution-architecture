#!/usr/bin/env python3
"""Check narrow public invariants for the architecture documentation."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".verify", "build", "__pycache__"}
REQUIRED = {
    ".github/dependabot.yml",
    ".github/workflows/ci.yml",
    ".github/workflows/codeql.yml",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE",
    "README.md",
    "SECURITY.md",
    "THIRD_PARTY_NOTICES.md",
    "compatibility/experimental-contract-set.v0.2.json",
    "docs/ADOPTION.md",
    "docs/ARCHITECTURE.md",
    "docs/CLAIMS_AND_VERIFICATION.md",
    "docs/COMPATIBILITY.md",
    "docs/INTEROPERABILITY.md",
    "docs/LAYERS.md",
    "docs/PRIOR_ART.md",
    "docs/PRODUCT_MODEL.md",
    "docs/RELEASE.md",
    "docs/REPOSITORIES.md",
    "docs/REVIEW_CONTRACT.md",
}
REQUIRED_REPOSITORIES = {
    "https://github.com/tetracoralla/capability-contracts",
    "https://github.com/tetracoralla/procedure-contracts",
    "https://github.com/tetracoralla/direct-execution-runtime",
}


def inventory(directory: Path) -> list[Path]:
    found: list[Path] = []
    for path in sorted(directory.iterdir()):
        if path.name in IGNORED:
            continue
        if path.is_symlink():
            raise RuntimeError(f"public tree must not contain symlinks: {path.relative_to(ROOT)}")
        if path.is_dir():
            found.extend(inventory(path))
        elif path.is_file():
            found.append(path)
    return found


def check_markdown_link(source: Path, target: str) -> None:
    if target.startswith(("http://", "https://", "#", "mailto:")):
        return
    path_text = target.split("#", maxsplit=1)[0]
    if not path_text:
        return
    resolved = (source.parent / path_text).resolve()
    if not resolved.is_relative_to(ROOT) or not resolved.exists():
        raise RuntimeError(f"broken or escaping Markdown link in {source.relative_to(ROOT)}: {target}")


def main() -> int:
    files = inventory(ROOT)
    relative = {str(path.relative_to(ROOT)) for path in files}
    missing = sorted(REQUIRED - relative)
    if missing:
        raise RuntimeError(f"required public files are missing: {', '.join(missing)}")

    text_files = [path for path in files if path.suffix in {".md", ".py", ".yml"} or path.name == "NOTICE"]
    documents: dict[Path, str] = {}
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        documents[path] = text
        if "\x00" in text or any(line.endswith((" ", "\t")) for line in text.splitlines()):
            raise RuntimeError(f"invalid text formatting: {path.relative_to(ROOT)}")

    public_text = "\n".join(documents.values())
    personal_path = "/".join(("", "Users", "openadam", "Development"))
    for forbidden in (
        personal_path,
        "file" + "://",
        "provides static " + "evidence",
        "correctness" + "Evidence",
        "opportunity" + "Evidence",
        "utility" + "Evidence",
    ):
        if forbidden in public_text:
            raise RuntimeError(f"forbidden public text is present: {forbidden}")
    for repository in REQUIRED_REPOSITORIES:
        if repository not in public_text:
            raise RuntimeError(f"public core repository link is absent: {repository}")
    if "Copyright 2026 openAdam" not in documents[ROOT / "NOTICE"]:
        raise RuntimeError("NOTICE must use the public openAdam identity")

    contract_set_path = ROOT / "compatibility/experimental-contract-set.v0.2.json"
    contract_set = json.loads(contract_set_path.read_text(encoding="utf-8"))
    if contract_set.get("schemaVersion") != "openadam.architecture-contract-set.v0.1":
        raise RuntimeError("compatibility contract set has the wrong schemaVersion")
    publication = contract_set.get("publication")
    if not isinstance(publication, dict) or publication.get("status") not in {"draft-unbound", "published-bound"}:
        raise RuntimeError("compatibility contract set has an invalid publication status")
    repositories = contract_set.get("repositories")
    if not isinstance(repositories, list) or len(repositories) != 3:
        raise RuntimeError("compatibility contract set must name the three public executable repositories")
    repository_ids: set[str] = set()
    schema_versions: set[str] = set()
    for repository in repositories:
        repository_id = repository.get("id")
        if not isinstance(repository_id, str) or repository_id in repository_ids:
            raise RuntimeError("compatibility contract set has a missing or duplicate repository id")
        repository_ids.add(repository_id)
        if repository.get("url") not in REQUIRED_REPOSITORIES:
            raise RuntimeError(f"compatibility contract set has an unknown repository URL: {repository_id}")
        for document in repository.get("documents", []):
            schema_version = document.get("schemaVersion")
            digest = document.get("fileSha256")
            if not isinstance(schema_version, str) or schema_version in schema_versions:
                raise RuntimeError("compatibility contract set has a missing or duplicate schema version")
            if not isinstance(digest, str) or re.fullmatch(r"[a-f0-9]{64}", digest) is None:
                raise RuntimeError(f"compatibility contract set has an invalid digest: {schema_version}")
            sibling_file = ROOT.parent / repository_id / document.get("file", "")
            if sibling_file.is_file():
                observed_digest = hashlib.sha256(sibling_file.read_bytes()).hexdigest()
                if observed_digest != digest:
                    raise RuntimeError(f"compatibility contract set digest drift: {schema_version}")
            schema_versions.add(schema_version)
    required_schema_versions = {
        "openadam.capability-profile.v0.3",
        "openadam.provider-manifest.v0.3",
        "openadam.conformance-suite.v0.2",
        "openadam.capability-jsonl-envelope.v0.1",
        "openadam.procedure-profile.v0.5",
        "openadam.procedure-implementation-manifest.v0.5",
        "openadam.procedure-conformance-suite.v0.4",
        "openadam.procedure-composition-suite.v0.2",
        "openadam.direct-provider-config.v0.2",
        "openadam.direct-work-order.v0.1",
        "openadam.direct-contract-selection.v0.1",
    }
    if schema_versions != required_schema_versions:
        raise RuntimeError("compatibility contract set does not exactly name the current document family")
    if publication["status"] == "published-bound":
        if re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", publication.get("releaseTag", "")) is None:
            raise RuntimeError("published compatibility contract set must name a release tag")
        for repository in repositories:
            if re.fullmatch(r"[a-f0-9]{40}", repository.get("revision", "")) is None:
                raise RuntimeError("published compatibility contract set must pin every repository revision")

    for path, text in documents.items():
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                check_markdown_link(path, target)

    workflow_text = "\n".join(
        text for path, text in documents.items() if ".github/workflows" in str(path)
    )
    for unsafe in ("pull_request_target", "permissions: write-all", "contents: write"):
        if unsafe in workflow_text:
            raise RuntimeError(f"unsafe workflow authority is present: {unsafe}")
    for reference in re.findall(r"\buses:\s+[^\s@]+@([^\s#]+)", workflow_text):
        if re.fullmatch(r"[a-f0-9]{40}", reference) is None:
            raise RuntimeError(f"workflow action is not pinned to a full commit: {reference}")

    print(f"repository invariants passed for {len(files)} public files")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"FAIL {error}", file=sys.stderr)
        raise SystemExit(1) from error
