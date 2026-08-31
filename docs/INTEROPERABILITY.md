# Interoperability map

This architecture is a semantic and execution layer between existing Agent
products, protocols, discovery systems, workflow frameworks, and provider
products. It does not ask those systems to adopt one shared runtime.

## Four different questions

| Question | Typical owner | This architecture's relationship |
| --- | --- | --- |
| How is a tool discovered and called? | MCP or a framework's function-tool API | Carrier. The provider may expose the same operation through MCP, CLI, HTTP, or a library. |
| What does this operation or settled method mean? | Capability or Procedure contract | Semantic narrow waist: versioned canonical inputs, outputs, behavior, stable errors, stages, and completion. |
| Which Agent or provider advertises an ability? | A2A Agent Cards, OASF records, catalogs | Discovery metadata may point to a contract identity; it does not establish conformance by description alone. |
| How is selected work scheduled and executed? | Agent SDK, workflow engine, application host, or Direct Execution Runtime | Execution binding. The host validates the current provider and invokes already-structured work under its own limits. |

Keeping these questions separate allows each ecosystem to keep its own
transport, discovery, orchestration, deployment, and product choices.

## Current integration status

| Surface | Current status |
| --- | --- |
| MCP provider execution | Implemented in Direct Execution Runtime through live stdio schema acquisition, pinned provider identity, persistent sessions, and bounded execution. |
| Selected MCP operation projection | Implemented in Direct Execution Runtime for explicitly declared discriminated tools; only the selected branch is compiled and raw wide-tool bypass is rejected. This is post-selection host behavior, not dynamic mutation of an Agent shell catalog. |
| Capability JSONL execution | Implemented for Capability Profile v0.3 plus Provider Manifest v0.3 complete semantic bindings. |
| Procedure JSONL execution | Implemented for closed-world Procedure Profile v0.5 plus implementation-manifest v0.5, including conditional completion validation. |
| Remote HTTPS Capability Provider | Development implementation and Direct Runtime loopback pilot through a local bounded JSONL bridge; no production endpoint, public package, credential or installed-Host claim. |
| Private Skill refinement | Development cross-repository vertical from bounded local source observation through generated Provider/thin Skill, sealed Host import, isolated Codex discovery, call, drift and rollback; semantic planning remains Agent-authored. |
| A2A or OASF discovery export | Mapping guidance only; no packaged adapter is currently claimed. |
| OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, or NVIDIA NeMo Agent Toolkit binding | Architectural fit only; no packaged framework adapter is currently claimed. |

The [public Math Anchor demo](https://github.com/tetracoralla/direct-execution-runtime/blob/main/docs/PUBLIC_DEMO.md)
is the shortest current executable integration. It uses a real MCP provider and
keeps provider errors distinct from host validation errors without involving a
model in the execution stage.

## Adapter rules

### MCP

MCP defines callable tools with input schemas and optional output schemas. A
Capability adapter may project those schemas into a provider-neutral contract,
but matching JSON shapes do not by themselves establish matching units,
ordering, ambiguity behavior, side effects, or stable errors. Conformance must
run through the real provider boundary.

Direct provider-native MCP execution additionally requires a closed operator
allowlist and safe live annotations. Those inputs can veto a call but do not
promote a raw MCP tool into a Capability or verify its external effects.
For an explicitly declared multi-operation tool, the host may additionally
project one selected branch and validate native batch items against their own
branches. Batch is used only when the provider declares native support; the
host does not silently coalesce calls or change ordering and failure semantics.

### A2A and OASF

A2A `AgentSkill` and OASF skill/domain records are useful discovery
descriptions. A future discovery adapter should link an exact Capability or
Procedure id, version, and contract digest instead of copying the full contract
or treating descriptive tags as conformance. Provider endpoint, authentication,
availability, and cost remain current provider or host facts.

### Agent and workflow frameworks

OpenAI Tool Search and Programmatic Tool Calling, Google ADK workflows,
Microsoft Agent Framework workflows, NVIDIA NeMo Agent Toolkit workflows,
Temporal, and similar systems may own discovery or orchestration. They can call
a provider directly, implement a Procedure, or hand already-selected typed work
to Direct Execution Runtime. Their tool, workflow, or function identity does
not replace the portable Capability or Procedure identity.

### Small models

A small model is one possible provider implementation when code, a standard
engine, or a database cannot produce the result alone. The contract must still
declare caller-visible input, output, uncertainty, bounds, and stable errors.
The model name, prompt, temperature, deployment, and latency belong to the
provider binding or diagnostics, not to the Capability identity.

## Adoption rule

Add a concrete adapter only when a current consumer needs it and can exercise
it through the real boundary. Until then, keep the relationship as documented
mapping rather than publishing empty compatibility packages or badges.
