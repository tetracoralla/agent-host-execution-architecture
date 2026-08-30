# Repository map

## Public architecture core

| Repository | Responsibility | Source relationship |
| --- | --- | --- |
| [agent-host-execution-architecture](https://github.com/tetracoralla/agent-host-execution-architecture) | Public model, terminology, adoption and claim boundaries | Documentation only |
| [capability-contracts](https://github.com/tetracoralla/capability-contracts) | Capability Semantic ABI, Profiles, Provider Manifests and conformance tooling | Independent standards repository |
| [procedure-contracts](https://github.com/tetracoralla/procedure-contracts) | Procedure Profiles, implementation manifests and conformance tooling | Independent standards repository |
| [direct-execution-runtime](https://github.com/tetracoralla/direct-execution-runtime) | Bounded host execution for already-closed structured calls | Independent runtime repository |

## Optional distribution and management

| Repository | Responsibility | Source relationship |
| --- | --- | --- |
| [agent-host-suite](https://github.com/tetracoralla/agent-host-suite) | Version-bound installation, supported host adapters, Direct Runtime service management, doctor/update/rollback/uninstall, and opt-in observability | Independent adopter; not required by the standards |

The Suite currently targets macOS with Codex and Claude adapters. Other Agent
shells may consume the same Provider, Capability, Procedure, and Direct Runtime
contracts through their own supported extension points without installing it.

## Public provider examples

| Product | Role in current public examples |
| --- | --- |
| [File Vitals](https://github.com/tetracoralla/file-vitals) | File-envelope Capability provider |
| [BatchTicket](https://github.com/tetracoralla/BatchTicket) | Structured-data Capability provider |
| [Migratory Time](https://github.com/tetracoralla/migratory-time) | Time-zone Capability and direct-host pilot |
| [Math Anchor](https://github.com/tetracoralla/math-anchor) | Typed mathematics MCP and direct-host pilot |

These are separate products, not folders inside this repository. Their public
names remain their product identities; descriptive role labels explain what
they contribute to the architecture.

Other openAdam tools may adopt parts of the architecture without becoming part
of this public core. Development-only pilots are not silently presented as
public dependencies.

## Adjacent planes

Observation, evaluation, and context-surface tools are adjacent to the core.
They may supply current observations, measurements, checks, or assessments,
but they are not required to execute a Capability or Procedure and are not
published here as authority over provider value, retirement, or routing.
