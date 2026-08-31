# Layers and terms

| Layer | Owns | Does not own |
| --- | --- | --- |
| Agent runtime | Model turns, tool-call loop, conversation state, cancellation and host integration supplied by the Agent product | Portable domain semantics or provider correctness |
| Agent shell | The concrete user-facing Agent product or command environment | This architecture's standards |
| Harness | Durable instructions, installed skills/plugins, routing hints, provider configuration and repo-local guidance | Domain algorithms or settled Procedure stages |
| Capability Semantic ABI | Portable meaning of one reusable typed operation | Provider commands, deployment, credentials or UI |
| Procedure Contracts | Portable meaning of one settled multi-stage method and completion condition | A new workflow DSL, planner or generic approval model |
| Provider Product | Domain core, richer product contract, adapters, packaging, limits and human surface | One host/account's endpoint, credentials or live health |
| Provider Instance | One installed/configured realization: exact product version, local root or endpoint, account/credential reference, grants and current health | Portable Capability meaning or Provider source |
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
this independent repository or its provider contracts. Its operation-level
projection can reduce post-selection validation and execution surface, but it
cannot alter the initial catalog of a shell that does not expose a dynamic tool
registration hook.

Agent Host Suite is an optional installer and manager around these layers. It
uses supported shell extension points and owns its installed files, service,
profiles, updates, rollback, and opt-in observations. It is neither the Agent
runtime nor the semantic standard, and another host may implement the same
contracts without installing it.

## Tool versus Capability versus Procedure

- A **Tool** is a callable carrier exposed to a host or Agent.
- A **Capability** is the versioned semantic meaning of one reusable operation.
- A **Procedure** is the versioned semantic meaning of a settled method that
  composes Capability requirements.
- A **Provider Product** is independently versioned code or service that
  implements those semantics.
- A **Provider Instance** is that product installed or configured for one host,
  endpoint, account, credential reference, and permission set.
- A **Skill** carries unresolved knowledge, routing, policy, and presentation
  guidance. It should not duplicate stable algorithms or Procedure stages.

One object can have several carriers. MCP, CLI, library, HTTP, and application
actions may all expose the same provider core without becoming separate
Capabilities.
