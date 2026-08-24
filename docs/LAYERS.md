# Layers and terms

| Layer | Owns | Does not own |
| --- | --- | --- |
| Agent runtime | Model turns, tool-call loop, conversation state, cancellation and host integration supplied by the Agent product | Portable domain semantics or provider correctness |
| Agent shell | The concrete user-facing Agent product or command environment | This architecture's standards |
| Harness | Durable instructions, installed skills/plugins, routing hints, provider configuration and repo-local guidance | Domain algorithms or settled Procedure stages |
| Capability Semantic ABI | Portable meaning of one reusable typed operation | Provider commands, deployment, credentials or UI |
| Procedure Contracts | Portable meaning of one settled multi-stage method and completion condition | A new workflow DSL, planner or generic approval model |
| Provider product | Domain core, richer product contract, adapters, packaging, limits and human surface | Cross-provider semantic ownership by itself |
| Direct Execution Runtime | Current binding validation, bounded admission, session reuse, deadlines, cancellation, recovery and result delivery | Natural-language intent, provider marketplace or domain meaning |
| Host and external systems | Installation, filesystem/network grants, credentials, permissions, endpoint health and real authorization | Portable semantic claims |
| Observer/evaluation plane | Current observations, measurements, deterministic checks and assessments | Self-certification or execution authority |

## Runtime versus harness

The Agent runtime is executable machinery inside an Agent product. It controls
the model/tool loop and usually updates with that product. This architecture
does not require patching it.

The harness is configuration around the runtime: repository guidance, Skills,
plugin manifests, provider bindings, schemas, and routing rules. Durable local
policy belongs in owned files and repositories, not in update-managed plugin
caches or patched application internals.

Direct Execution Runtime is a second runtime with a narrower responsibility. It
does not converse or reason. It runs only after a host, Agent, automation, or
person has selected a typed operation. Updating an Agent shell does not replace
this independent repository or its provider contracts.

## Tool versus Capability versus Procedure

- A **Tool** is a callable carrier exposed to a host or Agent.
- A **Capability** is the versioned semantic meaning of one reusable operation.
- A **Procedure** is the versioned semantic meaning of a settled method that
  composes Capability requirements.
- A **Provider** is a product that implements those semantics.
- A **Skill** carries unresolved knowledge, routing, policy, and presentation
  guidance. It should not duplicate stable algorithms or Procedure stages.

One object can have several carriers. MCP, CLI, library, HTTP, and application
actions may all expose the same provider core without becoming separate
Capabilities.
