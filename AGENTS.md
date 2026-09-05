# Agent-Host Execution Architecture repository guidance

Read `docs/PRODUCT_MODEL.md`, `docs/ARCHITECTURE.md`, and
`docs/REVIEW_CONTRACT.md` before changing this repository.

A review reconstructs the current repository map and executable consumers,
then applies the contract as minimum coverage plus an independent discovery
route. The contract is not a completion script.

This repository owns the public architectural narrative and repository map. It
does not own external provider source, Capability or Procedure schemas, Host
runtime code, Agent shell code, deployment, or a generic workflow language.

- Preserve typed package, protocol, version, and failure boundaries. Do not
  require a separate repository when a Host-owned implementation has no
  verified independent consumer; it may live as an internal Agent Host package.
- Keep independently useful external provider products separately releasable.
  A Plugin, conformance suite, or provider identity alone does not establish
  that product boundary.
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
