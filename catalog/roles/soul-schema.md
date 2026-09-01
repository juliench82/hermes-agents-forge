# SOUL.md Schema — Universal Persona Skeleton (Forge)

Every provisioned profile gets a SOUL.md written against this schema.
The schema is role-agnostic: a social media manager and a QA engineer use
the same sections. Depth comes from grounding, never from templates.

## Required sections (all of them, in this order)

1. `# <Role Name>` — the role, named in this team's context
2. `## Identity` — who this agent is; one solid paragraph
3. `## Mission` — what it exists to accomplish; must quote the user's own words
4. `## Operating Principles` — 5–7 numbered rules that govern its decisions
5. `## Working Style` — how it communicates, reports, formats output
6. `## Capabilities & Tools` — concrete tools/platforms/accounts and how each is used
7. `## Collaboration Protocol` — handoffs with NAMED teammates, group chats, routines. Name how teammates are reached: @mentions in group rooms, direct `message_agent` DMs. The profile's own one-line description is what every teammate sees in its roster — write it as a pitch.
8. `## Boundaries` — what it never does
9. `## Escalation` — when and how it escalates to the user or teammates
10. `## Success Metrics` — how it knows it did well; measurable where possible

## Grounding sources (use all three)

1. The user's interview answers — their goals, quality bar, tools,
   constraints. Quote their own words.
2. The role's installed skills — `hermes skills search <domain>` then
   `hermes skills inspect <candidate>`: the skill's own knowledge grounds
   the persona's principles and metrics.
3. The official SOUL.md guide:
   https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes

## Depth rules — verify before writing the file

1. Every section is filled. No placeholders, no "TBD".
2. Minimum 2 sentences or 3 bullets per section.
3. The user's own words appear at least once (Mission or Principles).
4. Tools are named concretely (GitHub, X, Gmail) — never just "the browser".
5. At least one handoff names a specific teammate profile.
6. Self-review pass — ask: "Could this text apply to any role unchanged?"
   If yes, rewrite it with role-specific detail.

## Examples

`catalog/roles/examples/` — a system architect and a social media manager,
both built on this schema, to calibrate expected depth.
