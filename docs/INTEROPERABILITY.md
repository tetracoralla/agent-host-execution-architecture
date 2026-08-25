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
| Capability JSONL execution | Implemented for current Provider Manifest bindings. |
| Procedure JSONL execution | Implemented for current Procedure Profile and implementation-manifest bindings. |
| A2A or OASF discovery export | Mapping guidance only; no packaged adapter is currently claimed. |
| OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, or NVIDIA Agent Intelligence Toolkit binding | Architectural fit only; no packaged framework adapter is currently claimed. |

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

### A2A and OASF

A2A `AgentSkill` and OASF skill/domain records are useful discovery
descriptions. A future discovery adapter should link an exact Capability or
Procedure id, version, and contract digest instead of copying the full contract
or treating descriptive tags as conformance. Provider endpoint, authentication,
availability, and cost remain current provider or host facts.

### Agent and workflow frameworks

OpenAI Programmatic Tool Calling, Google ADK workflows, Microsoft Agent
Framework workflows, NVIDIA Agent Intelligence Toolkit workflows, Temporal,
and similar systems may own orchestration. They can call a provider directly,
implement a Procedure, or hand already-selected typed work to Direct Execution
Runtime. Their workflow or function identity does not replace the portable
Capability or Procedure identity.

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
