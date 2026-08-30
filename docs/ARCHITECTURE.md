# Architecture

## End-to-end flow

The architecture has two valid entry routes.

### Natural-language route

1. The Agent shell receives intent and current context.
2. The harness helps the Agent identify an applicable Capability, Procedure,
   provider tool, or ordinary reasoning path.
3. The Agent resolves ambiguity and produces typed input.
4. The host validates the selected current contract and binding.
5. The host executes the provider call under current limits.
6. The provider returns its typed result or stable error.
7. The Agent resumes only when interpretation, judgment, presentation, or a new
   authorization decision remains.

### Already-structured route

When the caller already has valid typed input and a pinned operation identity,
steps 1–3 are unnecessary. An application, automation, CLI, or library can go
directly to host validation and execution. Zero Agent calls is the intended
budget for this execution stage.

## Semantic selection

A Capability owns one independently reusable operation meaning. It defines the
canonical input, output, caller-visible behavior, and stable errors without
depending on a particular transport or provider command.

A current provider binds the complete resolved Capability Profile with one
digest. Operation annotations are checked projections of Profile semantics,
not an independent source of safety truth. Schema equality alone is therefore
insufficient when behavior, stable errors, lifecycle, or effects change.

A Procedure owns a settled repeated method. It references versioned Capability
requirements, their order and dependencies, machine-evaluable optional-stage
conditions, and falsifiable completion branches. The implementation binds the
complete resolved Procedure Profile. It does not ask the Agent to reconstruct
the stage graph on every invocation.

## Evolution discipline

The architecture freezes identities, not implementation progress. Four
versions evolve independently:

- document format version describes how a contract file is encoded;
- Capability or Procedure semantic version describes caller-visible meaning;
- provider version describes one product implementation and release;
- adapter or host protocol version describes one carrier envelope.

Once a Capability or Procedure `id@version` is cataloged or consumed, its
schemas, stable errors, effect meaning, causal graph, and completion semantics
are immutable. A reviewer can and should identify a better design, but a
meaning-changing correction becomes a new semantic version with explicit
provider, Procedure, and host migration. Changing only a schema-format string
is not such a migration.

Provider algorithms and the host runtime may continue to improve connection
reuse, scheduling, concurrency, cancellation, recovery, resource bounds, and
performance under the same semantic version only when the complete selected
contract remains behaviorally conserved. This gives reviewers room to optimize
the system without letting a review silently redefine what existing consumers
already pinned.

Not every tool needs either standard. A provider-native typed operation remains
valid when no portable Capability or settled Procedure has been demonstrated.

## Provider execution

The provider remains the product. It owns its domain core, richer result,
runtime limits, adapters, packaging, release, and human surface. A canonical
Capability adapter may project the richer product result into a narrower
portable result; it must not mutate an existing Capability version when the
product grows.

The host execution layer reacquires current binding facts before execution. It
checks the selected identity, version, complete Profile digest, schema digests,
semantics-derived annotations, conditional graph/completion where applicable,
and input. It then owns admission, session/process reuse,
deadlines, cancellation, recovery, correlation, partial failure, and complete
response bounds. Provider domain results and errors remain provider-owned.

If one live carrier tool contains several explicitly discriminated operations,
the host may project the selected branch, prune unreachable local schema
definitions, compile only that branch, and cache it under the current provider
binding. It must keep the tool name, operation identity, input/output contract,
stable errors, provider version, and contract digest visible. Raw access to the
wide projected tool is then rejected at that host boundary. This optimization
happens after selection; it does not dynamically shrink the initial catalog of
an Agent shell that has no such extension point.

Provider-native MCP remains a valid fallback when no portable Profile exists.
In that route, an operator allowlist and live annotations are host policy inputs,
not Capability conformance or proof that the provider cannot cause effects.

## Agent re-entry

Execution returns to an Agent only when at least one of these is true:

- the intent or selected operation is still ambiguous;
- result interpretation requires contextual judgment;
- a new authorization or business decision is required;
- the current contract cannot represent the request honestly;
- presentation must be adapted for the human conversation.

A transport failure, provider error, or large catalog does not by itself
justify asking a model to invent an alternative result.

## Observation and assessment

Operational measurements and evaluations are adjacent to execution, not part
of the portable result by default. A current run may produce observations such
as selected route, calls, latency, bytes, retries, process count, and resource
growth. A deterministic predicate over explicit inputs is a check. A reviewer
or model mapping current facts to criteria is an assessment.

Only an enforced host boundary that consumes predefined checks and actually
blocks or permits one named action is a gate. A generated report, trace, or
self-authored record does not become authority over the action it describes.

## Side effects and authority

Capability and Procedure semantics do not grant host authority. Credentials,
permissions, endpoint health, filesystem grants, and approval state are current
facts owned by the host and external systems. The initial Direct Execution
Runtime is intentionally read-only. Extending it to side effects requires a
real consumer and a separate effect and authorization contract; it is not an
implicit consequence of this architecture.
