# HERMES.md — Hermes-Agents-Forge Integration Guide

## What is Hermes-Agents-Forge?

Hermes-Agents-Forge is a **skill-based onboarding system** for HERMES agents. It teaches any HERMES agent (via the `/forge` skill) how to:

1. Interview users about their automation needs
2. Design custom multi-agent teams
3. Provision isolated bot-mode profiles using official HERMES CLI

## How It Works (Official HERMES Primitives)

| Forge Concept | Official HERMES Primitive | CLI Command |
|---------------|--------------------------|-------------|
| "Bot-mode profile" | HERMES Profile | `hermes profile create <name>` |
| "Isolated agent" | Profile with own config, memory, skills | `hermes -p <name> chat` |
| "Team roster" | Bot Mode UI over profiles | Desktop Bots tab |
| "Agent persona" | SOUL.md | `~/.hermes/profiles/<name>/SOUL.md` |
| "Agent capabilities" | Skills | `hermes -p <name> skills install <skill>` |

## User Flow

1. User visits site → clicks "Read agent instructions"
2. User points HERMES agent to `https://hermes-agents-forge.vercel.app/llms.txt`
3. HERMES agent loads the `/forge` skill
4. Skill executes: interview → team design → confirmation → profile provisioning
5. Result: isolated profiles under `~/.hermes/profiles/<name>/`

## Default: "Use My Real Browser Profile"

Before provisioning, the skill asks:
> "Do you want to use your real browser profile for web automation, or create isolated browser profiles for each agent?"

**Default**: "Use My Real Browser Profile" — agents share the user's existing browser session for web automation tasks.

This is a **user preference**, not an official HERMES feature. Document it clearly in the skill's interview step.

## Official HERMES Documentation

The official HERMES documentation is available at:
- Main docs: https://hermes-agent.nousresearch.com/docs/
- Full documentation bundle: https://hermes-agent.nousresearch.com/docs/assets/files/llms-full-f963828d9e90cf8f351ea9497445e567.txt

Key sections referenced by this project:
- Bot Mode: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- SOUL.md: https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes
