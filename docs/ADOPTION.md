# Adoption

Adopt the architecture from a real repeated task, not from a desire to fill
every layer.

## 1. Keep the provider independently useful

Start with one deterministic or bounded provider core and explicit typed
input/output. Keep its existing CLI, MCP, API, library, or human surface. The
provider should remain buildable and useful without the architecture repo.

## 2. Add a Capability only when meaning is reusable

Define a Capability Profile when multiple callers need the same operation
meaning independent of transport. Project the provider's richer result into a
canonical result and run conformance through the real adapter. One provider is
enough for an experimental provider-seeded Profile, not for substitution.

## 3. Add a Procedure only when the method is settled

Define a Procedure when a repeated task has meaningful stage order,
dependencies, stable errors, and a falsifiable completion condition. Reference
Capability identities; do not copy their schemas or build another workflow
language. Keep intent interpretation outside the Procedure.

## 4. Add direct host execution when work is already closed

Use the host runtime when structured calls are repeated, provider startup or
session cost matters, or callers need bounded concurrency, cancellation, and
correlation. Pin current bindings and validate the selected operation schema
before execution. Do not expose a generic opaque invoke tool to the model.

## 5. Teach each harness the cheapest correct route

Repository guidance and product Skills should explain when to select the
Procedure, standalone Capability, provider-native tool, or ordinary Agent
reasoning. They should not duplicate schemas or algorithms. Agent products may
route differently; use cold-session observations instead of assuming prose is
followed.

## 6. Verify lanes separately

At minimum report:

- public source and legal closure;
- repository development regression;
- Capability and Procedure conformance against current providers;
- installed-host availability and actual Agent routing;
- direct-host performance, load, cancellation and resource behavior;
- human product runtime when one exists;
- owner business and experience acceptance.

A green check in one lane does not close the others.

## Minimal adoption

A project may use only a provider-native typed tool and the harness rules. It
may add a Capability without a Procedure, or a Procedure backed by an existing
workflow runtime. It may use Direct Execution Runtime without modifying its
Agent shell. Partial adoption is expected.
