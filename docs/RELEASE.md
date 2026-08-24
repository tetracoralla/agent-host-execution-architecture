# Source release checklist

This repository publishes architecture documentation. It does not publish a
package, binary, hosted service, provider catalog, or Agent shell integration.

1. Run `python3 scripts/check_repository.py`.
2. Verify every linked public core repository and provider example from its
   public HTTPS URL.
3. Run the public-release auditor with owner `tetracoralla`, author `openAdam`,
   and license `Apache-2.0`.
4. Push through the protected branch workflow and wait for CI and CodeQL.
5. Inspect code-scanning, dependency, and secret-scanning alerts.
6. Re-clone the public repository and rerun its checker.
7. Create a tag or GitHub Release only after separate owner authorization.
