# Review contract

Review current linked repositories and public GitHub state; do not accept this
repository's own prose as proof that executable layers conform. This contract
records durable architecture boundaries and minimum coverage, not a fixed
reasoning script or completion runway.

Before applying the named checks, reconstruct the current repository map,
layer ownership, compatibility document family, executable consumers, and
public claims. Perform and report at least one independent discovery route
derived from that model rather than from this file, test names, prior findings,
or the changed-file list. Completing every item below cannot by itself end the
review.

## Development regression

Run `python3 scripts/check_repository.py` for repository-local invariants. Its
result must explicitly say whether adjacent contract digests were verified or
unavailable. In the complete `tools-dev` workspace, run
`python3 scripts/check_repository.py --require-sibling-contracts`; this strict
mode fails when any named adjacent contract file is absent instead of silently
skipping drift detection. Reacquire every public repository URL and verify that
responsibility statements still match its current README and product model.
Check internal links, legal identity, workflow pinning, and the absence of
personal paths, generated reports, local configuration, and copied provider
source.

## Architecture integrity

Check that:

1. Agent runtime, shell, harness, semantic contracts, provider product, direct
   host runtime, host authority, and assessment plane remain distinct.
2. Capability owns reusable typed operation meaning; Procedure owns settled
   method and completion; neither owns provider deployment or Agent planning.
3. Direct execution begins only after typed selection and current binding/input
   validation. Operation projection preserves exact identity, version,
   input/output, errors, and digest; raw wide-tool bypass is rejected. No
   model-facing generic opaque invoke tool or dynamic-shell claim is proposed.
4. Provider source and public product names remain in their independent
   repositories.
5. Observations, measurements, checks, assessments, gates, and proofs are not
   collapsed into an unqualified evidence claim.
6. Related work is described from current primary sources without novelty or
   universal superiority claims.
7. The interoperability map distinguishes implemented carriers from mapping
   guidance and does not turn discovery metadata or framework fit into a
   compatibility or conformance claim.
8. Capability and Procedure implementation manifests bind their complete
   resolved Profiles; annotations, optional-stage conditions, and completion
   branches cannot drift independently of that binding.
9. A cataloged or consumed Capability/Procedure `id@version` is not rewritten
   in place. Meaning-changing review findings create a new semantic version;
   implementation-only optimization demonstrates behavioral conservation.
10. `compatibility/experimental-contract-set.v0.2.json` exactly names the
   current document family. `draft-unbound` is never described as immutable;
   `published-bound` requires exact repository revisions and a release tag.
11. Agent Host Suite remains an optional distribution adopter, not a required
    standards runtime, provider source repository, or patched Agent shell.

## Executable lanes

This repository cannot close the executable lanes by itself. Review them in
their owners:

- Capability and provider conformance in Capability Semantic ABI and current
  provider repositories;
- Procedure result, composition, and stage-binding conformance in Procedure
  Contracts and current implementations;
- direct runtime safety, load, cancellation, recovery, packaging, and current
  pilots in Direct Execution Runtime;
- installed Agent routing and human product flows in the actual Agent shell and
  provider products.

## Reporting

Report public/legal closure, documentation regression, linked executable
regression, installed-host behavior, performance/load/economics, and owner
business acceptance separately. End with PASS, FAIL, or BLOCKED for each
applicable lane and name any stale link or cross-repository drift.
