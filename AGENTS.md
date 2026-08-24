# Agent-Host Execution Architecture repository guidance

Read `docs/PRODUCT_MODEL.md`, `docs/ARCHITECTURE.md`, and
`docs/REVIEW_CONTRACT.md` before changing this repository.

This repository owns the public architectural narrative and repository map. It
does not own provider source, Capability or Procedure schemas, Direct Execution
Runtime code, Agent shell code, deployment, or a generic workflow language.

- Keep every linked implementation in its independent repository.
- Do not copy tool source or publish local configuration, credentials, paths,
  measurements, generated reports, or Agent traces here.
- Treat observations, measurements, deterministic checks, assessments, gates,
  and proofs as different concepts. Do not promote one into another by naming.
- Do not claim uniqueness, universal effectiveness, cross-provider
  substitution, production capacity, or compatibility with every Agent shell.
- Add a normative machine contract only in its owning executable repository,
  with a current consumer and regression coverage.
- Use Apache-2.0 and the public author identity `openAdam`.

Run `python3 scripts/check_repository.py` before proposing a change. Commit or
publish only with explicit owner authorization.
