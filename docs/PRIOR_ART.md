# Related work and positioning

Last reviewed: 2026-08-25.

This architecture overlaps several active open-source categories. Publication
or popularity is a category signal, not a reason to claim that one layer owns
another. The comparisons below use each project's own public description.

| Project or standard | What it owns | Relationship to this architecture |
| --- | --- | --- |
| [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | A protocol and schemas for connecting AI applications to context, tools, and servers | MCP is one carrier. It does not become the semantic identity of a Capability or the settled method of a Procedure. |
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

## License note

Names and trademarks in this document belong to their respective owners. Links
are informational and do not imply endorsement or compatibility certification.
