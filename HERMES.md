# HERMES.md — Hermes-Agents-Forge Integration Guide

## What is Hermes-Agents-Forge?

Hermes-Agents-Forge is an **agent-followed onboarding system** for HERMES.
One URL is the entire entry point:

`https://hermes-agents-forge.vercel.app/llms.txt`

Any HERMES agent that reads it — any LLM, any reasoning level — learns to:

1. Interview the user about their workflows, tools, and quality bar
2. Design a custom team of specialists (3, 5, or 7 by complexity)
3. Get ONE explicit approval for the complete plan
4. Provision the team via the official HERMES CLI: isolated profiles,
   rich SOUL.md personas, real installed skills
5. Verify with receipts and hand off with team rituals

No installation, no cloning, no configuration. The agent is the installer.

## Forge Concepts → Official HERMES Primitives

| Forge Concept | Official HERMES Primitive | CLI Command |
|---------------|--------------------------|-------------|
| "Bot-mode profile" | HERMES Profile | `hermes profile create <name> --description "<role>"` |
| "Isolated agent" | Profile with own config, memory, skills | `hermes -p <name> chat` |
| "Agent persona" | SOUL.md | `~/.hermes/profiles/<name>/SOUL.md` |
| "Agent capabilities" | Skills from the official Skills Hub | `hermes -p <name> skills install <skill>` |
| "Team roster" | Bot Mode over profiles (on by default in Desktop) | Bots tab |
| "Team collaboration" | Group rooms (2–6 Bots), `message_agent` DMs, routines | Bot Mode; `hermes cron list` |

## The Flow (what the agent executes)

1. Read, in order: `site/llms.txt` → this file → `skills/forge/SKILL.md` →
   `catalog/roles/soul-schema.md` → `catalog/skills.json`
2. Interview the user — one question at a time, keeping their exact words
3. Propose the team (names, roles, tools, browser mode) and ask exactly:
   "Shall I provision this team as isolated bot-mode profiles?"
4. After one explicit yes: create the profiles, write each persona against
   the 10-section SOUL.md schema, and install real skills —
   `hermes skills search` → `inspect` → `install`; third-party skills must
   pass the NVIDIA SkillSpector scan first
5. Verify with receipts: `hermes profile list` count, per-profile
   `skills list`, one `chat` smoke test per profile, and a durable TEAM.md
   record
6. Hand off with rituals: a group room for the team, `message_agent` DMs
   between specialists, an optional kickoff routine

One approval covers the whole plan. After the yes, the agent runs
autonomously to completion.

## Default: "Use My Real Browser Profile"

Real-browser mode is the **unasked default** for every provisioned bot. The
skill does not ask — isolated browser profiles are created only when the
user explicitly opts out. New profiles share the main profile's credential
pool by default, consistent with this.

"Use My Real Browser Profile" is a **user preference**, not an official
HERMES feature. Record the mode in TEAM.md and honor it whenever a bot
browses.

## Official HERMES Documentation

- Main docs: https://hermes-agent.nousresearch.com/docs/
- Bot Mode: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- SOUL.md guide: https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes
