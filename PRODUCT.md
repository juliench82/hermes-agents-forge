# PRODUCT.md — Hermes-Agents-Forge Product Requirements

## v0.5.3

A customer visits our site, clicks "Read agent instructions", and points their HERMES agent to:
`https://hermes-agents-forge.vercel.app/llms.txt`

From there, any HERMES agent (any LLM, any reasoning level) must:
1. Interview the user
2. Design a custom team of agents (3/5/7 by complexity)
3. Get one explicit approval for the full plan
4. Provision isolated bot-mode profiles — each with a rich persona and real skills
5. Verify with receipts and hand off with team rituals

## Core Flow

```
read llms.txt / verify forge skill version
  ↓
interview user
  ↓
propose team + personas + skills plan
  ↓
ONE approval for everything
  ↓
provision: profiles + rich SOUL.md + real skills (three-tier engine: builtins → generative → Hub gaps)
  ↓
verify with receipts → TEAM.md → rituals handoff
```

## The Persona Engine

Personas are generated, never enumerated:
- Universal schema (catalog/roles/soul-schema.md): 10 sections, same for
  every role — depth comes from structure.
- Grounded content: the user's quoted interview answers + the knowledge of
  the role's skills (all tiers count).
- Depth rules enforced by self-review — anything that could apply to any
  role unchanged gets rewritten.
- Golden examples in catalog/roles/examples/ calibrate the quality bar —
  they do not limit coverage.

## The Skills Engine

Three tiers, in order — stop when the role's needs are covered:
- Tier 1 — Builtins (~57 per profile): verify coverage, never duplicate.
- Tier 2 — Generative: the agent authors a bespoke skill for roles nothing
  covers, via skill_manage create, grounded in the interview answers —
  the persona engine's logic applied to capabilities.
- Tier 3 — Hub: genuine gaps only — search → inspect → install.
- Every role's skill needs are covered or explicitly reported as gaps —
  never silence.

## Experience Requirements

1. Zero-config onboarding — one URL is the whole entry point
2. Single approval gate — one yes, then autonomous execution to completion
3. Any HERMES agent works — any LLM follows the flow; small local models
   may collapse mid-run (Run 8: 12B) — flagship-class models are the bar
   for a full autonomous run
4. Any role works — no fixed catalog of personas
5. "Use My Real Browser Profile" is the default browser mode

## Success Criteria

- [x] Any HERMES agent can load the flow from llms.txt (verified on a 12B
      local model: full interview → Package 7 → confirmation → provisioning,
      zero nudges, after hardening commit 5d3dd01)
- [ ] Personas meet schema depth rules for ANY role — including roles with
      no template (test: social media manager)
- [ ] Every role's skill needs are covered by enabled builtins, a generated
      skill, or an explicit gap report
- [ ] Zero mid-flow confirmations after the single approval
- [ ] Skill installs pass the built-in security scan — never --force past
      a verdict
- [ ] Receipts: profile list + skill inventory + per-profile smoke test + TEAM.md
- [ ] Rituals: group chat / shared inbox / kickoff proposed in handoff
- [x] Interrupt recovery — a mid-provisioning model collapse is recoverable
      via the resume rule without redoing work (Run 4)
- [x] Clean-install flow — interview, package tier, exact gate question,
      batched provisioning, schema-grounded persona (Run 8, through 4b)
- [ ] Phase-exit receipts — a stalled run is auditable at its failure
      point, not only in a final report (v0.5.1)

## Test Log

- Run 1 (12B, no thinking): interview ✓, proposal ✓, stalled 4/7, language
  drift, false "done" — led to checklist/batching/resume rules.
- Run 2 (12B, thinking, pre-hardening): full proposal ✓, 7/7 profiles after
  2 nudges, hallucinated skill names, no verification — led to skills rules.
- Run 3 (12B, thinking, post-hardening 5d3dd01): 5/5 profiles, zero nudges,
  graceful skill skip, error recovery, handoff ✓.
- Run 4 (12B, thinking, v0.3.0 build): mid-provisioning model collapse
  (repetition loop) → clean recovery via the resume rule; 7/7 profiles +
  personas; 0 Hub skills landed (GitHub API rate limits, largely burned on
  duplicates) while 57 builtins cover most needs; final report falsely
  declared "complete" — led to v0.3.4 receipts rules and v0.3.5
  builtins-first.
- Run 5 (v0.4.0 build): four-tier engine ran; handoff still stopped at
  group rooms + a cron digest — runs 1–5 converged on the missing work
  engine (led to v0.5.0 Kanban wiring).
- Run 6 (v0.4.0-line build): autonomy drift — install confirmation prompts
  and a checklist kept only in memory — drove v0.4.1 (--yes on installs)
  and v0.4.2 (todo-tool anti-drift gate).
- Run 7 (v0.5.0, stale environment): hijacked by a pre-v0.3 local forge
  skill left in ~/.hermes/skills — 4-member team, thin personas, zero
  skill installs, no board; nothing in the flow detected version skew
  (led to the v0.5.1 skill handshake).
- Run 8 (v0.5.0, clean install, 12B local model): best flow adherence yet —
  5/5 interview questions, Package 7, exact gate question, batched 4a,
  schema-grounded persona with quoted answers; then model degeneration
  mid-4b (channel-token loops, 72.7s stall, off-task drift) — profiles
  left all-builtin, no skill installs, no receipts past 4b. The manual is
  validated; model class is the remaining variable (flagship retest =
  Run 9).
- Run 9 (next): v0.5.3 build on a flagship-class model (HERMES
  subscription) — success bar: full autonomous run through Step 6 board
  wiring, phase-exit receipts at every transition, manual version quoted
  in the first reply, context-hygiene applied before provisioning.

## References

- Official Skills docs (URL installs, skill_manage, security scanning):
  https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Official docs: https://hermes-agent.nousresearch.com/docs/
