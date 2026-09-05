# Adoption

Adopt the architecture from a real repeated task, not from a desire to fill
every layer.

## Optional: mine an existing Skill corpus

When the repeated task already lives in a private Skill or runbook, begin with
a bounded read-only observation. Let the user's chosen Agent author the
semantic proposal, then use deterministic tools only to validate its closed
shape and lower explicitly supported contracts. Keep ambiguity and judgment in
a thin Skill. The platform does not supply or grade the authoring Agent and
does not promise extraction quality or effect preservation. The current
development refinement route is described in `SKILL_TO_CAPABILITY.md`. Do not
upload a private corpus or turn an Agent assessment into generated code without
the owner's chosen privacy boundary.

## 1. Keep the provider independently useful

Start with one deterministic or bounded provider core and explicit typed
input/output. Keep its existing CLI, MCP, API, library, or human surface. The
provider should remain buildable and useful without the architecture repo.

## 2. Add a Capability only when meaning is reusable

Define a Capability Profile when multiple callers need the same operation
meaning independent of transport. Project the provider's richer result into a
canonical result and run conformance through the real adapter. One provider is
enough for an experimental provider-seeded Profile, not for substitution.

Configure a Provider Instance separately from the Profile: exact product
version, local root or endpoint, account/credential reference, grants and
health. These are Host facts and must not be promoted into portable semantics.

## 3. Add a Procedure only when the method is settled

Define a Procedure when a repeated task has meaningful stage order,
dependencies, stable errors, and a falsifiable completion condition. Reference
Capability identities; do not copy their schemas or build another workflow
language. Keep intent interpretation outside the Procedure.

## 4. Add direct host execution when work is already closed

Use the host runtime when structured calls are repeated, provider startup or
session cost matters, or callers need bounded concurrency, cancellation, and
correlation. Pin current bindings and validate the selected operation schema
before execution. If a provider-native carrier groups many discriminated
operations in one schema, project and cache only the already-selected branch;
preserve its exact identity and semantics, and keep the original wide carrier
unavailable through that projected route. Do not expose a generic opaque invoke
tool to the model.

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

## Small models belong behind a provider contract

Use a smaller model when the operation still needs bounded interpretation or
classification that deterministic code cannot supply. Keep the Capability
identity stable across implementation changes, and expose uncertainty, limits,
and stable failure semantics in the provider result. Model name, prompt,
temperature, hosting, and price remain provider binding or diagnostic facts.

Do not send settled deterministic work to a small model merely to make the
architecture look uniformly AI-based. The cheapest correct implementation may
be code, a mature library, a standards database, a rules engine, or a model.

## Add a second provider only for a real substitution need

One real provider can seed an experimental Profile. Add an independent second
provider when a current caller needs failover, vendor choice, independent
verification, or portable behavior across engines. Prefer a thin adapter over
an existing mature engine or provider; do not build a second complete product
only to obtain a higher conformance label.

Until the same Profile has current differential coverage across independent
providers, describe each provider's conformance separately and leave
substitution unestablished.

## Minimal adoption

A project may use only a provider-native typed tool and the harness rules. It
may add a Capability without a Procedure, or a Procedure backed by an existing
workflow runtime. It may use Direct Execution Runtime without modifying its
Agent shell. Partial adoption is expected.
