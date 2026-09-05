# Compatibility contract set

The architecture publishes one machine-readable compatibility bill of
materials at
`compatibility/experimental-contract-set.v0.3.json`. It names the document and
protocol versions intended to work together and records SHA-256 bytes for each
schema source.

The v0.3 set resolves Direct Runtime schemas from their current owner,
`agent-host-suite/packages/direct-execution-runtime`, and refreshes the
Differential Suite schema digest. The former v0.2 draft remains historical;
it is not validated against today's working trees.

The Direct Runtime document family includes the explicit contract-selection
schema used for post-selection Capability, Procedure, or MCP-operation
projection. It does not standardize a model-facing provider catalog or opaque
invoke API.

The current file is deliberately `draft-unbound`: it coordinates the repaired
working trees, but it is not immutable because no repository revisions or
release tag have been created. This prevents prose, green tests, or matching
local files from being presented as a published compatibility release.

Promotion to an immutable contract set requires one separately authorized
release action:

1. run every repository's current checks and the cross-repository pilots;
2. commit each cleanly reviewed repository through its own protected workflow;
3. replace `draft-unbound` with a bound publication record containing every
   exact 40-character Git revision and the architecture release tag;
4. verify every schema digest from fresh clones of those revisions;
5. tag or publish only after owner authorization and hosted CI/security checks.

Changing any listed document format, protocol, or schema bytes creates a new
contract-set version. Provider releases and Capability/Procedure semantic
versions remain separately owned; the bill of materials does not certify
provider availability, substitution, performance, or business acceptance.

The current draft coordinates the Capability JSONL v0.1 envelope as schema
bytes, including its two exact compatible error forms: `{code,message}` and
`{code,message,retryable}`. The Capability Profile remains authoritative for
retryability.

It also coordinates `openadam.differential-suite.v0.1`. That document format
allows two distinct Provider Manifests to be compared over one bounded corpus;
including its schema bytes does not promote any Profile to L3 or certify a
test-only witness as a released substitute.

## Current semantic migrations

These coordinates describe the repaired local pilot set; they are not a
published compatibility certification:

| Identity | Preserved version | Active pilot version | Reason for a new semantic version |
| --- | --- | --- | --- |
| `org.openadam.raster.prepare` | `0.1.0` | `0.2.0` | output replacement is classified as destructive rather than ordinary write |
| `org.openadam.projective.transform` | `0.1.0` | `0.2.0` | raster publication receives the same corrected effect classification |
| `org.openadam.standard-expression.run` | `0.1.0` | `0.2.0` | carrier and provider-infrastructure failures are removed from the stable semantic error set |
| `org.openadam.brand-asset.prepare` | `0.1.0`, `0.2.0` | `0.3.0` | the closed-world Procedure declaration now conservatively aggregates every Capability stage |
| `org.openadam.structured-data.preflight` | `0.1.0`, `0.2.0` | `0.3.0` | the closed-world Procedure declaration now conservatively aggregates every Capability stage |
| `org.openadam.package-dependency.change-preflight` | `0.1.0` | `0.2.0` | the closed-world Procedure declaration now conservatively aggregates every Capability stage |

Old catalog entries remain readable at their old meaning. Active provider and
Procedure manifests move to the new versions explicitly; provider product
release versions do not change merely because their semantic binding changes.
