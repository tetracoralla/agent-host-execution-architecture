# Skill-to-Capability authoring and lowering

`Skill-to-Capability` is the compatibility name for an optional
bring-your-own-Agent authoring flow. The user's chosen Agent may turn an
explicit, owner-controlled Skill corpus into a proposal for a smaller set of
executable and guidance artifacts. Natural-language meaning is not uniquely
recoverable, so the platform does not supply or certify the semantic author:
deterministic tools only expose exact authoring contracts, validate submitted
artifacts, and materialize one explicitly supported lowering target.

## Current flow

```text
owned Skill directory or exact local Git checkout
  -> Skill Mining Lab source observation and candidate facts
  -> user's chosen Agent authors classification and refinement proposals
  -> Skill Refinery plan/candidate validation
  -> generated private typed Tool Provider + thin Skill
  -> optional later Capability binding only when semantics genuinely match
  -> verified sealed agent-tool archive
  -> Agent Host preview/import/activation
  -> isolated Codex discovery and real typed call
  -> drift detection, remove and rollback
```

The current local cross-repository vertical executes the deterministic part of
this chain with a temporary Host state and temporary Codex home. It starts from
one synthetic Skill through the packaged Skill Mining intake, uses fixed
Agent-authored fixture plans, builds a real Provider, imports and activates the
sealed archive, calls its valid and invalid inputs, observes source drift as
stale, removes it, rolls back, verifies the restored call, and purges the
temporary installation. It also validates a two-run cold-Agent evaluation
input while executing zero model runs. This establishes the mechanical carrier
chain, not the quality or autonomy of an authoring Agent.

## What each layer owns

- Skill Mining Lab performs bounded read-only source observation. Its local
  checkout route accepts one exact Git worktree and contained Skill root,
  records revision/status/tree digests before and after, rejects change during
  scanning, and emits a public origin only when it is credential-free HTTPS.
- The user's chosen Agent classifies fragments as unresolved guidance,
  deterministic Capability candidates, settled Procedure candidates, Host
  policy, or exclusions. This is its assessment, not a platform extraction
  claim. Different Agents may produce different structurally valid proposals.
- Skill Refinery validates the explicit plan, builds only supported templates,
  verifies the archive, and leaves unsupported semantics visible rather than
  generating guessed code.
- Agent Host admits the sealed package through existing private-component
  preview/import/activation/rollback mechanics. It does not accept source
  checkouts or caller-supplied runtime commands.
- Agent Tool Evals can compare a cold Agent with and without the generated tool
  using explicit Host-managed runtime roots. Validation itself performs no
  model call; actual model runs remain a separate, cost-bearing evaluation.

## Thin output rule

Keep in the Skill only what still changes an Agent's judgment: applicability,
ambiguity, input preservation, interpretation, stopping and presentation.
Move stable parsing, calculation, conversion, validation and bounded API
mechanics into Provider code. Move only a genuinely settled multi-stage method
into a Procedure. Put permission, installation, credentials, mandatory calls
and completion blocking in the Host or owning external system.

The output is not required to define a public Capability Profile immediately.
A private typed Provider can enter one Host first. Promote common meaning only
after a second caller/provider path demonstrates that the semantics, rather
than just the JSON shape, should be portable.

## Privacy and claim boundary

The source scanner and deterministic build do not require a model credential
or network. The semantic planning Agent still sees the supplied Skill content
inside its current execution environment; the owner chooses that Agent,
harness, privacy boundary, and any external model service. Agent Host does not
mediate or broaden that authorization.

An Agent-authored plan is a proposal. A successful validation means its shape,
citations, digests, exact links, and supported lowering inputs agree; it does
not mean that the Agent understood the Skill, chose the right abstraction,
preserved task quality, or produced the best thin Skill.

The current vertical proves one supported template and carrier chain. It does
not prove automatic compilation of arbitrary Skills, semantic correctness or
quality of an Agent-authored plan, natural routing in every Agent shell,
production distribution, or universal token savings. Those are separate
evaluation, installed-runtime and owner-acceptance lanes.

## Optional effect-preservation assessment

Effect preservation is a user goal, not a default platform property. When
the owner asks for it, compare the original Skill route with the refined route
under the same task knowledge, Agent, harness and budget. Treat the result as
conditional on the evaluated models, attempts, tasks and graders.

A weak Agent result is not an upper bound on a stronger Agent or on sustained
expert-human practice. Conversely, one strong Agent success does not establish
field reliability. Escalate assessment in proportion to the decision:

1. deterministic checks for source, pack and runtime facts;
2. repeated runs across the weakest and strongest intended Agent classes for
   routing and attainable task quality;
3. independent external outcomes or expert review for consequential semantic
   equivalence;
4. sustained dogfood for workflows whose real value depends on context learned
   over days or weeks.

No Agent-generated report can promote itself across these levels. Report the
highest level actually observed and keep stronger capability, human practice,
long-horizon effects and ecological coverage explicitly untested. When the
owner does not request effect equivalence, these comparisons do not block a
private tool build.
