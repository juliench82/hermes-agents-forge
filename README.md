# Hermes-Agents-Forge

A customer visits our site, clicks "Read agent instructions", and points their HERMES agent to:
`https://hermes-agents-forge.vercel.app/llms.txt`

From there, any HERMES agent (any LLM, any reasoning level) interviews the user, designs a custom team of 3/5/7 specialists, gets one explicit approval, then provisions governed, isolated specialist teams that prove themselves on a real workflow—with explicit roles, tool boundaries, approval policy, and auditable receipts.

## What you get

- **Custom team design** — 3 (basic), 5 (intermediate), or 7 (complex) specialists generated from your workflows, not a fixed catalog.
- **Rich personas** — every profile gets a 10-section SOUL.md persona grounded in your quoted answers and real skill knowledge.
- **Real skills** — three-tier engine: builtins first, then bespoke generated skills for uncovered roles, Hub only for genuine gaps.
- **Receipts, not assertions** — final report includes verbatim `hermes profile list`, per-profile `skills list`, smoke-test chat output, and kanban receipts.
- **Kanban work board** — after verification, your team gets a durable board: cards seeded, review loop wired, progress observable in `hermes kanban watch` or the dashboard.
- **Team rituals** — group chat (2–6 Bots per room), `message_agent` DMs, optional weekly digest routine.

## Trust & safety

- You never install anything — your HERMES agent sets itself up from one URL.
- One approval gate — after your yes, the agent runs autonomously to completion.
- Security scanning — every skill install (generated or Hub) is scanned; dangerous verdicts are skipped and reported.
- Context hygiene — post-gate compression and output caps tuned per profile for token-efficient runs.
- Interrupt recovery — if the agent stalls mid-provisioning, it resumes from the `todo` checklist and `hermes profile list`, provisioning only what's missing.

## How it works (at a glance)

1. **Interview** — 5 questions about your workflows, tools, quality bar, complexity, and boundaries.
2. **Proposal** — package tier, specialist roster (name, role, tools, browser mode), collaboration plan, and what provisioning will do.
3. **Approval** — one explicit yes covers team, personas, skills, browser mode, and board wiring.
4. **Provisioning** — batched profile creation, SOUL.md personas, three-tier skills, phase-exit receipts.
5. **Verification** — `hermes profile list`, per-profile `skills list`, smoke-test chat, `todo` zero open items, `TEAM.md` written.
6. **Board wiring** — gateway + kanban init, first cards seeded (goal-mode where appropriate), review loop, kanban receipts.
7. **Handoff** — group chat, shared inbox, kickoff routine (or one small first task if Bot Mode unavailable).

## Team sizes

- **Package 3** — basic: 3 specialists; single-domain, simple workflows.
- **Package 5** — intermediate: 5 specialists; multi-domain, needs analysis and review.
- **Package 7** — complex: 7 specialists; multi-project, coordination-heavy.

The team is exactly 3, 5, or 7 specialists — never 4 or 6.

## Get started

Point your HERMES agent to:
`https://hermes-agents-forge.vercel.app/llms.txt`

The agent will read the operating manual, interview you, and guide you through the rest.

## References

- Operating manual: https://hermes-agents-forge.vercel.app/llms.txt
- Official HERMES docs: https://hermes-agent.nousresearch.com/docs/
