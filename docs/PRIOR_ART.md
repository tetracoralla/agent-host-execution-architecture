# Related work and positioning

Last reviewed: 2026-08-30.

This architecture overlaps several active open-source categories. Publication
or popularity is a category signal, not a reason to claim that one layer owns
another. The comparisons below use each project's own public description.

| Project or standard | What it owns | Relationship to this architecture |
| --- | --- | --- |
| [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | A protocol and schemas for connecting AI applications to context, tools, and servers | MCP is one carrier. It does not become the semantic identity of a Capability or the settled method of a Procedure. |
| [OpenAI Agents SDK Hosted Tool Search](https://openai.github.io/openai-agents-python/tools/#hosted-tool-search) | A supported Responses model can defer function tools, namespaces, or hosted MCP servers and load a smaller surface when needed | Strong overlap in reducing the initial model-facing catalog. It remains model-directed discovery inside an OpenAI Agent run; this architecture separately covers provider-neutral semantics and post-selection host validation/execution, and does not claim to retrofit deferred loading into an unmodified shell. |
| [OpenAI Agents SDK Programmatic Tool Calling](https://openai.github.io/openai-agents-python/tools/#programmatic-tool-calling) | A supported Responses model can generate JavaScript that coordinates eligible tools through loops, branching, parallel calls, and intermediate calculations without a model round trip for every tool call | Strong overlap in reducing repeated model relays. It is a model-generated, OpenAI-hosted orchestration mechanism; this architecture separately defines provider-neutral semantics and a host route for work that is already selected and structured. |
| [A2A Protocol](https://a2a-protocol.org/latest/specification/) | Agent-to-agent communication, Agent Cards, interfaces, tasks, and descriptive `AgentSkill` records | A2A may advertise or carry an Agent interaction. A descriptive skill record does not replace executable Capability or Procedure conformance. |
| [Open Agentic Schema Framework](https://github.com/agntcy/oasf) | Versioned records, taxonomies, metadata, and discovery for Agent identities, skills, domains, and relationships | OASF is a natural discovery layer. A record may link to exact contract identities, while portable operation meaning and real-boundary conformance remain separate. |
| [Google Agent Development Kit workflows](https://adk.dev/agents/workflow-agents/) | Predefined sequential, parallel, and loop execution patterns plus newer graph and dynamic workflow structures | ADK can implement orchestration or a Procedure binding. Its deterministic execution order does not by itself define provider-neutral stage or operation semantics. |
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) | Agent application abstractions, tools, middleware, telemetry, and workflows for well-defined steps | Its agent-versus-workflow guidance aligns with keeping functions and explicit workflows below open-ended Agent reasoning. Capability conformance and direct host binding remain distinct. |
| [NVIDIA NeMo Agent Toolkit](https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html) | Reusable functions, tools, agents, workflows, evaluation, profiling, observation, MCP, and A2A integrations | It can host provider or Procedure implementations. This architecture does not replace its workflow, evaluation, registry, authentication, or deployment surface. |
| [ToolHive](https://github.com/stacklok/toolhive) | Running, proxying, securing, observing, and managing MCP servers locally and on Kubernetes, with registry and gateway features | Strong overlap in provider lifecycle and MCP session infrastructure. This architecture does not supply containers, Kubernetes, a registry, or an enterprise gateway; its distinct focus is semantic and method contracts plus a narrow direct-host route. |
| [Microsoft MCP Gateway](https://github.com/microsoft/mcp-gateway) | A reverse proxy and management layer for scalable, session-aware MCP routing and lifecycle in Kubernetes | Complementary infrastructure. Direct Execution Runtime is a current-host execution layer, not a Kubernetes gateway. |
| [Open Workflow Specification](https://open-workflow-specification.org/) | A vendor-neutral DSL ecosystem for defining and executing workflows | Procedure Contracts do not introduce a workflow DSL. An OWS document can be an implementation binding behind a Procedure Profile. |
| [Temporal](https://docs.temporal.io/) | Durable, reliable workflow execution with persisted state, retries, and recovery | Temporal can implement a Procedure that needs durable orchestration. This architecture does not duplicate durable workflow state or replay. |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | Stateful Agent and workflow graphs, persistence, and Agent orchestration | LangGraph can own an Agent flow or Procedure implementation. Capability semantics and host binding validation remain separate concerns. |

## Positioning

The public contribution is the explicit composition of four boundaries:

1. provider-neutral operation semantics;
2. provider-neutral settled method semantics;
3. provider-owned implementations and transports;
4. host-owned bounded execution for already-closed work.

This is a testable architectural position, not a claim that no prior system has
implemented any individual boundary. The project should be compared through
real integrations: same task, current provider, fixed harness/model where an
Agent is involved, and separately measured direct-host execution.

See the [Interoperability map](INTEROPERABILITY.md) for current adapter status
and the rules for relating transport, discovery, semantic contracts, and
execution without presenting documented fit as implemented compatibility.

## License note

Names and trademarks in this document belong to their respective owners. Links
are informational and do not imply endorsement or compatibility certification.
