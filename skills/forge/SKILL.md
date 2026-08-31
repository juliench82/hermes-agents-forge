---
name: forge
description: Interview users, design custom agent teams, and provision isolated bot-mode profiles
version: 1.0.0
metadata:
  hermes:
    tags: [onboarding, team-design, bot-mode]
    category: productivity
---

# Forge Skill — Custom Agent Team Provisioning

## When to Use

Use this skill when:
- A user visits the Hermes-Agents-Forge site and clicks "Read agent instructions"
- The user points their HERMES agent to `https://hermes-agents-forge.vercel.app/llms.txt`
- You need to interview the user, design a custom team, and provision isolated bot-mode profiles

## Procedure

### Step 1: Interview the User

Ask the user:
1. What workflows do you want to automate? (e.g., research, coding, content creation, customer support)
2. How many specialized agents do you need? (1–5 recommended for starters)
3. What models should each agent use? (default: inherit from your main profile)
4. Should agents share credentials or have isolated API keys? (default: shared)

### Step 2: Design the Team

Based on the interview, propose a team structure:
- **Agent 1**: `<name>` — `<role>` (e.g., "Researcher — reads docs, writes summaries")
- **Agent 2**: `<name>` — `<role>` (e.g., "Coder — implements features, writes tests")
- Include model pins, skills, and SOUL.md for each

### Step 3: Get User Confirmation

Present the team proposal and ask for explicit confirmation:
> "Shall I provision these agents as isolated bot-mode profiles? This will create separate Hermes profiles under `~/.hermes/profiles/<name>/."

Wait for user approval before proceeding.

### Step 4: Provision Isolated Bot-Mode Profiles

For each confirmed agent:
1. Run: `hermes profile create <name> --description "<role>"`
2. Optionally clone skills: `hermes profile create <name> --clone` (shares config, fresh memory)
3. Configure model pin (if requested): `hermes -p <name> config set model.default <model>`
4. Write SOUL.md: `echo "<persona>" > ~/.hermes/profiles/<name>/SOUL.md`
5. Install relevant skills: `hermes -p <name> skills install <skill>`

### Step 5: Default to "Use My Real Browser Profile"

**Important**: Before provisioning, ask:
> "Do you want to use your real browser profile for web automation, or create isolated browser profiles for each agent?"

- **Default**: "Use My Real Browser Profile" (user's existing browser session)
- If user wants isolation: create separate browser profiles per agent (advanced setup)

## Verification

After provisioning:
1. Run `hermes profile list` — confirm all new profiles appear
2. Run `hermes -p <name> chat` — confirm each agent responds with its role
3. Confirm Bot Mode roster shows all new agents (if using Hermes Desktop)

## Pitfalls

- **Never point two agents at the same profile** — each must have its own `~/.hermes/profiles/<name>/`
- **Bot Mode is a desktop UI feature** — programmatic provisioning uses `hermes profile create`, not a Bot Mode API
- **"Use My Real Browser Profile" is not an official HERMES feature** — document it as a user preference for browser automation, not a HERMES primitive

## References

- Official HERMES Bot Mode docs: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- Official HERMES Profiles docs: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Official HERMES Skills docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Official HERMES SOUL.md docs: https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes
