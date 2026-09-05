# Agent-Host Execution Architecture

Agent-Host Execution Architecture is an open architecture for moving settled,
typed work out of repeated model turns and into bounded host execution without
replacing the Agent shell.

The central separation is:

> Agents decide. Contracts define meaning. Hosts execute closed work.

The practical rule is equally small: use the main Agent for unresolved intent
and judgment; put deterministic or mechanically checkable work in provider
code; describe reusable meaning with typed contracts; and let the host execute
already-closed calls without another model relay. A small model may implement a
provider when judgment remains, but it does not become the Capability identity.

```text
Natural-language intent                         Already structured input
          |                                               |
          v                                               |
  Agent shell + harness                                   |
  intent, ambiguity, judgment                             |
          |                                               |
          +-------------- typed selection ----------------+
                                 |
                                 v
                  Capability or Procedure contract
                                 |
                                 v
                  current provider binding + schema
                                 |
                                 v
                  bounded host execution runtime
                                 |
                                 v
                    typed provider result or error
```

An Agent shell still owns conversation, intent, unresolved judgment, and final
presentation. A harness supplies durable routing and product-specific guidance.
The semantic contracts define portable operation or method meaning. The host
runtime validates current bindings, reuses eligible provider sessions, applies
limits, and executes the already-closed call without another model decision.
When a provider carrier advertises many typed operations, a capable host may
project the already-selected operation into one smaller contract for validation
and execution. The projection preserves operation identity, version, input,
output, and error meaning; it is not an opaque universal invoke tool and does
not claim to rewrite an unmodified Agent shell's initial tool catalog.

## Public core

- [Capability Semantic ABI](https://github.com/tetracoralla/capability-contracts)
  defines canonical input, output, behavior, and stable errors for reusable
  operations.
- [Procedure Contracts](https://github.com/tetracoralla/procedure-contracts)
  compose versioned Capability requirements into a settled method with explicit
  completion semantics.
- [Direct Execution Runtime](https://github.com/tetracoralla/agent-host-suite/tree/main/packages/direct-execution-runtime)
  is a versioned Agent Host package that validates current bindings and
  executes eligible structured calls through a library, CLI, or local
  current-user service.

Independently useful provider products remain separately releasable. They keep
their own richer product contracts, source, releases, transports, limits, and
human surfaces. Host-owned providers and standards fixtures may share their
owning source workspace while preserving typed package and failure boundaries.
A Provider Instance binds one such product to an installed root or remote
endpoint, account/credential reference, permissions, and current health. The
Host manages Instance facts; the Capability does not. This documentation
repository contains no provider or Host runtime source.

[Agent Host Suite](https://github.com/tetracoralla/agent-host-suite) is the
optional local distribution and management product for current hosts. It binds
compatible releases, installs through supported shell extension points, runs
the private Direct Runtime service, and offers update, rollback, doctor,
uninstall, and opt-in observability. It is an adopter of the architecture, not
a required standards runtime.

See [Repository map](docs/REPOSITORIES.md) for the current public set.

See [Development direction](docs/DEVELOPMENT_DIRECTION.md) for the current
value hypothesis, executable substitution experiment, and decisions that
require real consumer evidence before further expansion.

## What this architecture is not

- not a replacement or fork of Codex, Claude Code, or another Agent shell;
- not a patch to an Agent runtime that an application update can overwrite;
- not an MCP replacement, gateway, server registry, or model-facing generic
  `invoke(provider, operation, opaqueInput)` tool;
- not a workflow DSL, planner, memory system, Agent graph, credential vault, or
  operating-system sandbox;
- not a claim that every Agent will route correctly or that every provider is
  substitutable;
- not an authorization layer for side effects. The current Direct Execution
  Runtime admits only read-only, non-destructive, idempotent, closed-world
  operations.

## Start here

1. Read [Architecture](docs/ARCHITECTURE.md) for the end-to-end flow.
2. Read [Layers](docs/LAYERS.md) to separate Agent runtime, shell, harness,
   contracts, providers, and host execution.
3. Use [Adoption](docs/ADOPTION.md) to add only the layers a real task needs.
4. Read [Claims and verification](docs/CLAIMS_AND_VERIFICATION.md) before making
   a correctness, portability, performance, or value claim.
5. Use the [Interoperability map](docs/INTEROPERABILITY.md) to place MCP, A2A,
   OASF, Agent SDKs, workflow engines, and small models without collapsing their
   responsibilities.
6. Run the [public Math Anchor demo](https://github.com/tetracoralla/agent-host-suite/blob/main/packages/direct-execution-runtime/docs/PUBLIC_DEMO.md)
   for a real zero-model execution-stage walkthrough.
7. Read [Related work](docs/PRIOR_ART.md) for current overlap and non-overlap.
8. Read [Compatibility contract set](docs/COMPATIBILITY.md) before treating one
   combination of repository revisions as a release coordinate.
9. Read [Provider forms](docs/PROVIDER_FORMS.md) for local-program, system/API,
   bounded model-inference, and Agent-runner implementations without confusing
   Product, Instance, Tool, or Skill.
10. Read [Skill-to-Capability authoring and lowering](docs/SKILL_TO_CAPABILITY.md)
    for the optional bring-your-own-Agent private-Skill production path.

## Current status

The architecture is experimental. Its public repositories, schemas, runners,
and local provider pilots are executable on the maintainer's current macOS
environment. That is enough for a public reference implementation and local
dogfood; it is not a universal device, shell, production-load, or same-domain
substitution claim.

## License

Licensed under the Apache License, Version 2.0. See `LICENSE` and `NOTICE`.
