# Provider forms

A Provider is an implementation of typed meaning, not necessarily a local
deterministic executable. The architecture keeps its outer objects stable while
allowing four implementation forms: local code, a remote system/API, bounded
model inference, or an Agent runner.

## The objects

| Object | Durable identity | Current facts |
| --- | --- | --- |
| Capability Profile | Capability id, semantic version, operations and schemas | Provider-neutral |
| Provider Product | Provider id and product version | Code/service release, adapters, limits and support boundary |
| Provider Instance | One installed/configured realization | Product version, local root or endpoint, account/credential reference, grants and health |
| Tool | Host/Agent callable carrier | MCP, CLI, HTTP, library or application action |
| Skill | Guidance for unresolved selection and use | Applicability, ambiguity, interpretation and presentation |
| Procedure | Settled multi-stage method | Versioned Capability requirements, order and completion |

A Provider Product may implement several Capabilities. Several independent
Provider Products may implement one Capability. A Procedure composes
Capabilities; Providers do not combine to “form” a Capability.

## Local program Provider

The Product packages a deterministic program, mature library, rules engine, or
standards database. The Instance fixes the installed product root, version,
permissions and current health. Its canonical adapter may share the product's
MCP/CLI core but retains exact typed results and stable errors.

This is the most mature current form in the reference implementation.

## System/API Provider

The Product may live behind a remote system API. A local bridge still exposes
the exact selected Capability adapter to the Host. Its Instance fixes one
endpoint, closed operation allowlist, timeout, response bound, and credential
reference. The endpoint and token are deployment facts, never Capability
fields.

The current development `Capability HTTP Bridge` implements this carrier. It
requires HTTPS outside numeric loopback, follows no redirects, performs no
automatic retries, bounds request/response/time, preserves exact semantic
result/errors, and turns connectivity/protocol failure into Host transport
failure rather than a fabricated domain error. Its macOS bearer-token route
references Keychain service/account; no token enters a Skill, Manifest,
argument, environment variable, work order, source file, or diagnostic.

The Direct Runtime pilot has executed one typed Capability across an observed
loopback HTTP boundary with zero model calls and per-call process cleanup. That
is a carrier observation, not production endpoint, credential, privacy,
installed-Host, or semantic-conformance acceptance.

## Model-backed inference Provider

A model-backed Provider may be as small as one typed inference node. The
Provider Product owns the mapping from typed input to bounded context and from
model output to the declared result. It does not need tools, memory, a planning
loop, or autonomous stopping merely because a model performs the operation.
The Instance fixes the actual model/runtime, credential reference, grants,
configured context inputs, per-call limits and current health.

This is analogous to a model node in a visual workflow: the caller or Procedure
decides what context reaches the node, and the node returns one typed result.
Provider- or Instance-level context tuning is allowed. If a change alters the
caller-visible meaning, stable errors, or interpretation of the result, the
binding/version and relevant evaluation must change; quality-only tuning need
not create a new Capability identity.

The outer Capability declares stochasticity, uncertainty/provenance that
changes caller use, limits and stable failure meaning when applicable. A
product needs an independent oracle only when it claims measured quality,
equivalence or substitution—not merely to exist as a model-backed Provider.

## Agent-runner Provider

Use the heavier form only when the implementation actually performs an
Agent-style run. Its Product then owns the subordinate model, harness, allowed
tools, run policy, context construction, turn/tool budgets, cancellation,
termination and result adapter. Its Instance fixes actual model/service access,
credentials, permissions, configured resources and health.

The calling Agent receives one typed result. A package that only supplies a
Skill and asks that same Agent to reason through the work is guidance, not an
independently installable Provider implementation; that guidance route remains
valid when unresolved judgment belongs with the main Agent. A package that
embeds an API key is invalid Instance design; a real Host or credential system
owns the secret reference.

There is no current live model-backed reference Provider in the public core.
Creating one requires a concrete repeated operation, privacy and spending
authority, a typed context/result boundary, and honest variability/limit
semantics. Tool loops and product-owned termination policy are required only
for an Agent runner. Model-backed evaluation is required for the quality claim
being made; it is not a universal admission gate. The architecture intentionally
does not invent a generic “ask a model/Agent” Capability merely to demonstrate
either form.

## Host responsibility

The Host manages Provider Instances and their Capability bindings. It may
project provider-specific Tools or Skills into each Agent shell's supported
extension format. It must keep these states distinct:

- declared Product/Manifest;
- installed package/root;
- configured endpoint/account and credential reference;
- current permissions and endpoint health;
- schema-valid successful call;
- Agent-shell discovery and natural routing.

One state cannot stand in for the next. In particular, a local adapter process
does not prove that its implementation performs no network egress; a real
remote Instance needs explicit network/privacy authorization outside the
Capability semantic claim.
