#!/usr/bin/env python3
"""Check narrow public invariants for the architecture documentation."""

from __future__ import annotations

import argparse
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
REQUIRED_CONTRACT_REPOSITORIES = {
    "capability-contracts": {
        "url": "https://github.com/tetracoralla/capability-contracts",
        "protocols": ["openadam.capability-jsonl.v0.1"],
        "documents": {
            "openadam.capability-profile.v0.3": "schemas/capability-profile.schema.v0.3.json",
            "openadam.provider-manifest.v0.3": "schemas/provider-manifest.schema.v0.3.json",
            "openadam.conformance-suite.v0.2": "schemas/conformance-suite.schema.v0.2.json",
            "openadam.capability-jsonl-envelope.v0.1": "schemas/capability-jsonl-envelope.schema.v0.1.json",
        },
    },
    "procedure-contracts": {
        "url": "https://github.com/tetracoralla/procedure-contracts",
        "protocols": ["openadam.procedure-jsonl.v0.2"],
        "documents": {
            "openadam.procedure-profile.v0.5": "schemas/procedure-profile.schema.v0.5.json",
            "openadam.procedure-implementation-manifest.v0.5": (
                "schemas/procedure-implementation-manifest.schema.v0.5.json"
            ),
            "openadam.procedure-conformance-suite.v0.4": (
                "schemas/procedure-conformance-suite.schema.v0.4.json"
            ),
            "openadam.procedure-composition-suite.v0.2": (
                "schemas/procedure-composition-suite.schema.v0.2.json"
            ),
        },
    },
    "direct-execution-runtime": {
        "url": "https://github.com/tetracoralla/direct-execution-runtime",
        "protocols": [
            "openadam.capability-jsonl.v0.1",
            "openadam.procedure-jsonl.v0.2",
        ],
        "documents": {
            "openadam.direct-provider-config.v0.2": "schemas/provider-config.schema.json",
            "openadam.direct-work-order.v0.1": "schemas/work-order.schema.json",
            "openadam.direct-contract-selection.v0.1": "schemas/contract-selection.schema.json",
        },
    },
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


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError(f"invalid JSON in {path.relative_to(ROOT)}: {error}") from error


def main(*, require_sibling_contracts: bool = False) -> int:
    files = inventory(ROOT)
    relative = {str(path.relative_to(ROOT)) for path in files}
    missing = sorted(REQUIRED - relative)
    if missing:
        raise RuntimeError(f"required public files are missing: {', '.join(missing)}")

    text_files = [
        path
        for path in files
        if path.suffix in {".json", ".md", ".py", ".yml"} or path.name == "NOTICE"
    ]
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
    contract_set = read_json(contract_set_path)
    if not isinstance(contract_set, dict):
        raise RuntimeError("compatibility contract set must be a JSON object")
    if contract_set.get("schemaVersion") != "openadam.architecture-contract-set.v0.1":
        raise RuntimeError("compatibility contract set has the wrong schemaVersion")
    publication = contract_set.get("publication")
    if not isinstance(publication, dict) or publication.get("status") not in {"draft-unbound", "published-bound"}:
        raise RuntimeError("compatibility contract set has an invalid publication status")
    repositories = contract_set.get("repositories")
    if not isinstance(repositories, list) or len(repositories) != len(REQUIRED_CONTRACT_REPOSITORIES):
        raise RuntimeError("compatibility contract set must name the three public executable repositories")
    repository_ids: set[str] = set()
    schema_versions: set[str] = set()
    missing_sibling_contracts: list[str] = []
    for repository in repositories:
        if not isinstance(repository, dict):
            raise RuntimeError("compatibility contract set repositories must be objects")
        repository_id = repository.get("id")
        if not isinstance(repository_id, str) or repository_id in repository_ids:
            raise RuntimeError("compatibility contract set has a missing or duplicate repository id")
        repository_ids.add(repository_id)
        expected_repository = REQUIRED_CONTRACT_REPOSITORIES.get(repository_id)
        if expected_repository is None or repository.get("url") != expected_repository["url"]:
            raise RuntimeError(f"compatibility contract set has an unknown repository URL: {repository_id}")
        if repository.get("protocols") != expected_repository["protocols"]:
            raise RuntimeError(f"compatibility contract set has protocol drift: {repository_id}")
        repository_documents = repository.get("documents")
        if not isinstance(repository_documents, list):
            raise RuntimeError(f"compatibility contract set documents must be an array: {repository_id}")
        observed_documents: dict[str, str] = {}
        for document in repository_documents:
            if not isinstance(document, dict):
                raise RuntimeError(f"compatibility contract set documents must be objects: {repository_id}")
            schema_version = document.get("schemaVersion")
            digest = document.get("fileSha256")
            document_file = document.get("file")
            if not isinstance(schema_version, str) or schema_version in schema_versions:
                raise RuntimeError("compatibility contract set has a missing or duplicate schema version")
            if not isinstance(digest, str) or re.fullmatch(r"[a-f0-9]{64}", digest) is None:
                raise RuntimeError(f"compatibility contract set has an invalid digest: {schema_version}")
            if not isinstance(document_file, str) or not document_file:
                raise RuntimeError(f"compatibility contract set has an invalid sibling file: {schema_version}")
            if expected_repository["documents"].get(schema_version) != document_file:
                raise RuntimeError(f"compatibility contract set has document mapping drift: {schema_version}")
            observed_documents[schema_version] = document_file
            sibling_root = (ROOT.parent / repository_id).resolve()
            sibling_file = (sibling_root / document_file).resolve()
            if not sibling_file.is_relative_to(sibling_root):
                raise RuntimeError(f"compatibility contract set sibling file escapes its repository: {schema_version}")
            if sibling_file.is_file():
                observed_digest = hashlib.sha256(sibling_file.read_bytes()).hexdigest()
                if observed_digest != digest:
                    raise RuntimeError(f"compatibility contract set digest drift: {schema_version}")
            else:
                missing_sibling_contracts.append(f"{repository_id}/{document_file}")
            schema_versions.add(schema_version)
        if observed_documents != expected_repository["documents"]:
            raise RuntimeError(f"compatibility contract set document family drift: {repository_id}")
    if repository_ids != set(REQUIRED_CONTRACT_REPOSITORIES):
        raise RuntimeError("compatibility contract set repository family drift")
    required_schema_versions = {
        schema_version
        for repository in REQUIRED_CONTRACT_REPOSITORIES.values()
        for schema_version in repository["documents"]
    }
    if schema_versions != required_schema_versions:
        raise RuntimeError("compatibility contract set does not exactly name the current document family")
    if require_sibling_contracts and missing_sibling_contracts:
        raise RuntimeError(
            "required sibling contract files are unavailable: "
            + ", ".join(sorted(missing_sibling_contracts))
        )
    if publication["status"] == "draft-unbound":
        if "releaseTag" in publication or any("revision" in repository for repository in repositories):
            raise RuntimeError("draft compatibility contract set must not carry release anchors")
    else:
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

    if missing_sibling_contracts:
        print(
            f"repository-local invariants passed for {len(files)} public files; "
            f"sibling digest verification incomplete for {len(missing_sibling_contracts)} files "
            "(rerun with --require-sibling-contracts in the complete workspace)"
        )
    else:
        print(f"repository and sibling digest invariants passed for {len(files)} public files")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-sibling-contracts",
        action="store_true",
        help="fail unless every compatibility document is present in its adjacent repository",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        arguments = parse_args()
        raise SystemExit(main(require_sibling_contracts=arguments.require_sibling_contracts))
    except RuntimeError as error:
        print(f"FAIL {error}", file=sys.stderr)
        raise SystemExit(1) from error
