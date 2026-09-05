# Development direction

The next useful state is a small execution system whose value can be tested
against real alternatives. Repository count, contract count, successful startup,
and a larger Agent catalog are poor substitutes for that result.

The working hypothesis is that portable meaning helps when a consumer must
retain its behavior while implementations, deployment or transports change.
The corresponding Host value is reliable, bounded reuse of already-selected
work. These are distinct hypotheses: one can succeed while a particular
Provider product has little independent utility.

## Keep three decisions separate

| Decision | What should determine it |
| --- | --- |
| Use an existing Provider, generated code, an API or UI interaction for a task | Required result, current access, reliability, total task effort and observed cost |
| Share a Capability meaning across implementations | Repeated consumer need and executable agreement on input, output, behavior and stable errors |
| Keep a component as a separate product or repository | Independent users, useful ownership, release needs and maintenance burden |

The Agent or an explicitly designed caller owns task-level judgment. The
current Host resolver owns only finite exact matching against supplied local
bindings; it does not choose a winner or silently retry another Provider.
There is no reason to grow a natural-language router, marketplace or perpetual
planning service merely to complete these three decisions.

Provider value may come from authoritative state and permissions, maintained
domain data, exact semantics, repeated-work efficiency, specialist performance,
or a useful human surface. Each claim needs observations from the actual
product. A short wrapper can be valuable when it provides such a boundary; a
large tool can be unnecessary when it does not. Existing investment is not a
reason to retain an unused default integration.

## The executable next step

The first development slice uses the existing
`org.openadam.time-zone.convert@0.2.0` Profile. The standards repository owns a
bounded, reproducible generated corpus and UTC conservation properties. Agent
Host owns a maintainer experiment that resolves and projects exact bindings,
runs one unchanged consumer against Migratory Time and the Python `zoneinfo`
witness, and repeats the calls through its library and CLI/local-service
carriers. It checks ordered results, ambiguous/nonexistent times, declared
errors, current contract identity, and host-side input rejection. It records
cold/warm execution and payload observations separately.

The relevant source commands are:

- `capability-contracts`: `npm run check:time-zone-differential -- --generated`;
- `agent-host-suite/packages/direct-execution-runtime`:
  `npm run check:local-substitution`.

These commands exercise existing standards and Host boundaries. They add no
semantic version, Profile metadata taxonomy, Provider ranking, installation
policy or model-facing invocation surface. Their current corpus and consumer
can fail on mismatches instead of assuming that a shared schema means shared
behavior. Full run observations stay with the caller; this architecture
repository does not publish machine-local measurements.

The experiment remains a development observation: one domain, one consumer,
two Host carriers, and an independent engine witness. The witness is not a
released replacement product; both carriers share a runtime. Generated
coverage does not automatically promote a conformance level. Its interpreter,
database and source dependencies must remain explicit. An independent second
consumer or product should arise from a useful task, not be created solely to
fill a test matrix.

## What would justify further development

These are decision aids for the current investment choices, not admission rules
for every future requirement. A real task can justify revising the architecture
itself. Distinguish a current version's unsupported behavior, an intentional
product non-goal, and a caller promise that needs compatibility. Unpublished,
unbound drafts outside the catalog can change or disappear; existing layers,
repositories, and experiments can also be merged or retired when their useful
role no longer warrants their maintenance.

| Proposed investment | Observation that would justify it | If that observation is absent |
| --- | --- | --- |
| A broader shared Profile | A second consumer or implementation repeatedly needs the same meaning | Keep the contract experimental and local in scope |
| A released alternative Provider | A real consumer benefits from substituting deployment, engine, performance or access | Keep the witness as test infrastructure |
| A default Host integration | Repeated task use and an advantage after discovery, setup, execution and recovery costs | Keep it optional or outside the ordinary catalog |
| A settled Procedure | A recurring dependent method has stable completion and failure behavior | Keep composition with the caller |
| Automated route selection | A caller has an explicit objective, comparable observations, limits and failure policy | Retain explicit selection and visible uncertainty |

A task comparison must give its alternatives the same intended outcome and
check the result independently. Count setup, context/schema exposure, model
turns when actually used, elapsed time, recovery, and retained dependencies.
Measure repeated use separately from a one-off task. Unknown price, token use,
privacy or reliability stays unknown; a zero-model Host stage is not proof of
zero task cost. A latency comparison with a prewritten witness does not measure
the effort of having a model write and debug that code.

The product purpose is to move concrete repeated work from Agent reasoning into
reliable tools. Verify that an existing consumer can discover the operation,
supply its inputs, and use its result without manually repeating the algorithm.
Correctness, failure recovery, and calling overhead can be checked directly.
A further model comparison is optional work for a specific unresolved decision,
not a default next step or a prerequisite for useful delivery. Do not fabricate
a no-tool run or infer reasoning savings from deterministic conformance. Net
reasoning and token savings remain unknown until actually observed. There is
no standing authorization here for model spend, scheduled agents, external
publication, installation or product removal.

## Follow transport evolution without duplicating it

MCP already defines typed tool input/output and structured results. Its
2026-07-28 release also introduces cacheable list results and moves Tasks into
an extension. Those facilities belong to the transport ecosystem. See the
[current tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
and the [official release description](https://blog.modelcontextprotocol.io/posts/2026-07-28/).

The architectural inference is to keep shared domain meaning and tested
substitution narrow, while adopting transport facilities where they solve a
current need. This does not claim that the current Host has migrated to that
protocol version. Such a migration must check the installed SDK, supported
clients, cancellation, schema acquisition and service lifecycle together; a
new specification alone does not make working older bindings defective.

Vendor model announcements and benchmark tables can suggest new alternatives
to test. They do not establish that this system is obsolete, valuable or
compatible. Product decisions should use task evidence and current official
integration contracts rather than an inherited strategic conversation's
release dates, prices or benchmark claims.
