# Repository map

## Public architecture core

| Repository | Responsibility | Source relationship |
| --- | --- | --- |
| [agent-host-execution-architecture](https://github.com/tetracoralla/agent-host-execution-architecture) | Public model, terminology, adoption and claim boundaries | Documentation only |
| [capability-contracts](https://github.com/tetracoralla/capability-contracts) | Capability Semantic ABI, Profiles, Provider Manifests and conformance tooling | Independent standards repository |
| [procedure-contracts](https://github.com/tetracoralla/procedure-contracts) | Procedure Profiles, implementation manifests and conformance tooling | Independent standards repository |
| [Agent Host Direct Execution Runtime package](https://github.com/tetracoralla/agent-host-suite/tree/main/packages/direct-execution-runtime) | Bounded host execution for already-closed structured calls | Versioned internal package with its own CLI, library, schemas, process and error boundary |

## Optional distribution and management

| Repository | Responsibility | Source relationship |
| --- | --- | --- |
| [agent-host-suite](https://github.com/tetracoralla/agent-host-suite) | Version-bound installation, Host-owned Direct Runtime source and service management, supported host adapters, doctor/update/rollback/uninstall, and opt-in observability | Independent adopter; not required by the standards |

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

These are independently useful products, not fixtures manufactured merely to
demonstrate repository separation. Their public names remain their product
identities; descriptive role labels explain what they contribute to the
architecture.

Other openAdam tools may adopt parts of the architecture without becoming part
of this public core. Development-only pilots are not silently presented as
public dependencies.

## Current development extensions

The maintainer workspace also contains not-yet-public development modules for
Skill mining, Skill refinement, and the bounded HTTP Capability bridge. They
exercise optional ecosystem-production and remote Provider paths, but neither a
typed boundary nor a pilot makes them independent products. Their long-term
source ownership is Agent Host or private labs unless real external consumption
establishes otherwise.

## Adjacent planes

Observation, evaluation, and context-surface tools are adjacent to the core.
They may supply current observations, measurements, checks, or assessments,
but they are not required to execute a Capability or Procedure and are not
published here as authority over provider value, retirement, or routing.
