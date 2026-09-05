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

The architecture connects five independently useful objects:

1. a versioned Capability semantic contract;
2. a versioned Procedure method contract when a stable multi-stage method
   exists;
3. an independent Provider Product implementing those semantics;
4. a configured Provider Instance on one host or account;
5. a host execution layer for already selected and structured work.

An optional distribution suite may install and manage concrete host adapters,
providers, and the direct runtime for a supported device. It consumes the
architecture but does not become the semantic standard or a prerequisite for
independent implementations.

Agent shells and harnesses are clients of the architecture. MCP, CLI, HTTP,
libraries, and local services are carriers. None of them becomes the semantic
identity of a Capability or Procedure.

A Skill remains guidance rather than executable semantic authority. In the
optional refinement flow, the user's chosen Agent reads the authorized Skill
material and authors a semantic proposal. Deterministic tools can validate
that proposal's structure and source bindings, lower one explicitly supported
contract into Provider code, and leave unresolved ambiguity or routing
knowledge in a thinner Skill. A settled multi-stage method may separately
become a Procedure.

The architecture neither supplies nor grades that authoring Agent. It does not
promise extraction quality, a uniquely correct partition, or effect
preservation unless the owner separately requests and defines a bounded
assessment. The flow is an optional ecosystem-production path, not a
prerequisite for using the architecture or an automatic natural-language
compiler.

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

This repository's initial public release is source and documentation under
Apache-2.0. It does not itself publish a package, binary, hosted service,
registry, or Agent shell integration. Linked core, provider, and optional Suite
repositories have independent histories, security settings, CI, releases, and
acceptance boundaries.
