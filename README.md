# Agent-Host Execution Architecture

Agent-Host Execution Architecture is an open architecture for moving settled,
typed work out of repeated model turns and into bounded host execution without
replacing the Agent shell.

The central separation is:

> Agents decide. Contracts define meaning. Hosts execute closed work.

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

## Public core

- [Capability Semantic ABI](https://github.com/tetracoralla/capability-contracts)
  defines canonical input, output, behavior, and stable errors for reusable
  operations.
- [Procedure Contracts](https://github.com/tetracoralla/procedure-contracts)
  compose versioned Capability requirements into a settled method with explicit
  completion semantics.
- [Direct Execution Runtime](https://github.com/tetracoralla/direct-execution-runtime)
  validates current bindings and executes eligible structured calls through a
  library, CLI, or local current-user service.

Provider products remain independent repositories. They keep their own richer
product contracts, source, releases, transports, limits, and human surfaces.
This repository contains no provider source and is not a monorepo.

See [Repository map](docs/REPOSITORIES.md) for the current public set.

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
  Runtime v0.1 admits only read-only, non-destructive, idempotent, closed-world
  operations.

## Start here

1. Read [Architecture](docs/ARCHITECTURE.md) for the end-to-end flow.
2. Read [Layers](docs/LAYERS.md) to separate Agent runtime, shell, harness,
   contracts, providers, and host execution.
3. Use [Adoption](docs/ADOPTION.md) to add only the layers a real task needs.
4. Read [Claims and verification](docs/CLAIMS_AND_VERIFICATION.md) before making
   a correctness, portability, performance, or value claim.
5. Read [Related work](docs/PRIOR_ART.md) for overlap and non-overlap with MCP,
   MCP infrastructure, workflow specifications, and durable orchestration.

## Current status

The architecture is experimental. Its public repositories, schemas, runners,
and local provider pilots are executable on the maintainer's current macOS
environment. That is enough for a public reference implementation and local
dogfood; it is not a universal device, shell, production-load, or same-domain
substitution claim.

## License

Licensed under the Apache License, Version 2.0. See `LICENSE` and `NOTICE`.
