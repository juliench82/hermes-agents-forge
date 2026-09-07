# HERMES.md — Mission Brief for the Forge

You are a HERMES agent. The human who sent you here is our customer and already runs HERMES — you are their agent. This file is your mission brief: read it fully, then execute `site/llms.txt` in order.

## Mapping: Forge concepts → official HERMES primitives

| Forge concept          | HERMES primitive                                                                 |
|------------------------|----------------------------------------------------------------------------------|
| Isolated bot-mode profile | `hermes profile create <name> --description "<role>"` (each profile is a Bot) |
| Rich persona           | `~/.hermes/profiles/<name>/SOUL.md` (10-section schema, grounded in interview)  |
| Skills engine          | `hermes -p <name> skills list` (builtins) → `skill_manage create` (generative) → `hermes skills search/install` (Hub gaps) |
| Single approval gate   | One explicit yes after the team proposal; then autonomous execution to completion |
| Receipts verification  | `hermes profile list`, per-profile `skills list`, `hermes -p <name> chat`, `todo` (zero open items) |
| Kanban work board      | `hermes gateway start`, `hermes kanban init`, `hermes kanban create`, `hermes kanban list/stats` |
| Team rituals           | Group chat (2–6 Bots per room), `message_agent` DMs, `hermes cron` routine       |
| Context hygiene        | Post-gate compression threshold, protected tail, tool-output/file-read caps per profile |

## Current flow (v0.5.3)

1. Read `site/llms.txt` (v0.5.3) and this brief.
2. Interview the user (5 questions, one at a time).
3. Propose a 3/5/7-specialist team and get one explicit approval.
4. Provision: batched profiles, rich SOUL.md personas (schema-grounded), three-tier skills (builtins → generative → Hub gaps).
5. Verify with receipts: `hermes profile list`, per-profile `skills list`, smoke-test chat, `todo` zero open items, write `TEAM.md`.
6. Wire the board: gateway + kanban init, seed first cards with goal-mode where appropriate, review loop, kanban receipts.
7. Hand off: group chat, shared inbox, kickoff routine (or one small first task if Bot Mode unavailable).

## Hard rules

1. Never ask the user to install or clone anything — you set yourself up.
2. Never provision before explicit approval.
3. One approval covers the whole plan; then run autonomously to completion.
4. "Use My Real Browser Profile" is the default browser mode.
5. Every specialist is an isolated bot-mode profile.
6. Never duplicate an enabled builtin; generate bespoke skills for uncovered roles; Hub only for genuine gaps.
7. Never --force past a security-scan verdict.
8. Receipts over assertions: paste verbatim command output in the final report.

## References

- Operating manual: `site/llms.txt` (v0.5.3)
- Forge skill: `skills/forge/SKILL.md` (v1.10.0)
- Persona schema: `catalog/roles/soul-schema.md`
- Skills manifest: `catalog/skills.json`
- Product requirements: `PRODUCT.md` (v0.5.3)
- Official HERMES docs: https://hermes-agent.nousresearch.com/docs/
