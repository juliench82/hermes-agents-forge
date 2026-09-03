# PRODUCT.md — Hermes-Agents-Forge Product Requirements

## Product Goal

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
read llms.txt / trust forge skill
  ↓
interview user
  ↓
propose team + personas + skills plan
  ↓
ONE approval for everything
  ↓
provision: profiles + rich SOUL.md + real skills (SkillSpector-gated)
  ↓
verify with receipts → TEAM.md → rituals handoff
```

## The Persona Engine

Personas are generated, never enumerated:
- Universal schema (catalog/roles/soul-schema.md): 10 sections, same for
  every role — depth comes from structure.
- Grounded content: the user's quoted interview answers + the knowledge of
  the role's skills (builtins count).
- Depth rules enforced by self-review — anything that could apply to any
  role unchanged gets rewritten.
- Golden examples in catalog/roles/examples/ calibrate the quality bar —
  they do not limit coverage.

## The Skills Engine

- Builtins first: every profile ships ~57 builtin skills enabled by default —
  verify coverage with `hermes -p <name> skills list` before any Hub search.
- catalog/skills.json: per-domain search terms + vetted third-party packs.
- Runtime: `hermes skills search` → `inspect` → `install` — real names,
  genuine gaps only — never a duplicate of an enabled builtin.
- Security gate: skills from outside the official Hub must pass NVIDIA
  SkillSpector before install.
- Every role's skill needs are covered by builtins, Hub installs, or an
  explicit gap report — never silence.

## Experience Requirements

1. Zero-config onboarding — one URL is the whole entry point
2. Single approval gate — one yes, then autonomous execution to completion
3. Any HERMES agent works — any LLM, any reasoning level
4. Any role works — no fixed catalog of personas
5. "Use My Real Browser Profile" is the default browser mode

## Success Criteria

- [x] Any HERMES agent can load the flow from llms.txt (verified on a 12B
      local model: full interview → Package 7 → confirmation → provisioning,
      zero nudges, after hardening commit 5d3dd01)
- [ ] Personas meet schema depth rules for ANY role — including roles with
      no template (test: social media manager)
- [ ] Every role's skill needs are covered by enabled builtins or an
      explicit gap report
- [ ] Zero mid-flow confirmations after the single approval
- [ ] Third-party skills blocked unless SkillSpector-clean
- [ ] Receipts: profile list + skill inventory + per-profile smoke test + TEAM.md
- [ ] Rituals: group chat / shared inbox / kickoff proposed in handoff
- [x] Interrupt recovery — a mid-provisioning model collapse is recoverable
      via the resume rule without redoing work (Run 4)

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
- Run 5 (next): v0.3.4/5 build — success bar: verbatim receipts, builtins-
  first inventory, honest gaps, no false completion.

## References

- SkillSpector (NVIDIA): https://github.com/nvidia/skillspector
- Superpowers (obra, MIT): https://github.com/obra/superpowers
- HERMES Skills Hub: `hermes skills search` / `install` — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Official docs: https://hermes-agent.nousresearch.com/docs/
