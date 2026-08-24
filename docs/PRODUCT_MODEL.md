# Product model

## User and task

The direct user is a provider author, Agent-host author, automation developer,
or standards maintainer who needs to decide which layer should own repeated
work and how to execute settled structured work without another model relay.

This repository is a documentation and navigation product. Its task is to make
the public architecture understandable, falsifiable, adoptable in parts, and
correctly linked to the executable repositories that own each contract.

## Stable public object

The stable public object is the layered architecture, not an Agent shell,
protocol, provider catalog, workflow graph, or universal runtime API.

The architecture connects four independently useful objects:

1. a versioned Capability semantic contract;
2. a versioned Procedure method contract when a stable multi-stage method
   exists;
3. an independent provider product implementing those semantics;
4. a host execution layer for already selected and structured work.

Agent shells and harnesses are clients of the architecture. MCP, CLI, HTTP,
libraries, and local services are carriers. None of them becomes the semantic
identity of a Capability or Procedure.

## Repository boundary

This repository owns:

- the public layer model and terminology;
- the adoption sequence and claim boundaries;
- the map of independent public repositories;
- related-work comparison at the architectural level.

It does not own executable schemas or implementation code. Normative changes
belong in Capability Semantic ABI, Procedure Contracts, Direct Execution
Runtime, or the concrete provider repository that can test them.

## Current release boundary

The initial public release is source and documentation under Apache-2.0. It
does not publish a package, binary, tag, hosted service, registry, or Agent
shell integration. The linked core repositories have independent histories,
security settings, CI, releases, and acceptance boundaries.
