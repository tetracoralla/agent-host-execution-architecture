# Source release checklist

This repository publishes architecture documentation. It does not publish a
package, binary, hosted service, provider catalog, or Agent shell integration.

1. From the complete adjacent multi-repository workspace, run
   `python3 scripts/check_repository.py --require-sibling-contracts`. The
   repository-local mode reports unavailable sibling checks but is not the
   release digest check.
2. Verify the compatibility contract set. It must remain `draft-unbound` until
   exact reviewed revisions exist in every executable repository.
3. Verify every linked public core repository and provider example from its
   public HTTPS URL.
4. Run the public-release auditor with owner `tetracoralla`, author `openAdam`,
   and license `Apache-2.0`.
5. Push through the protected branch workflow and wait for CI and CodeQL.
6. Inspect code-scanning, dependency, and secret-scanning alerts.
7. Re-clone every pinned revision, verify all contract-set schema digests, and
   rerun each repository checker.
8. Change the contract set to `published-bound`, pin all exact 40-character
   revisions and its release tag, then rerun the architecture checker.
9. Create the tag or GitHub Release only after separate owner authorization.
