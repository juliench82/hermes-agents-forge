# HERMES-Agents-Forge

## What This Is
A HERMES-native bootstrap repository that enables **any HERMES agent** to:
1. Interview users about their workflow needs
2. Design custom teams of specialized bot-mode profiles
3. Provision isolated profiles after user confirmation
4. Default to "Use My Real Browser Profile" unless user opts for isolation

## How It Works

### For Users
1. Visit [hermes-agents-forge.vercel.app](https://hermes-agents-forge.vercel.app)
2. Click "Read agent instructions"
3. Point your HERMES agent to: `https://hermes-agents-forge.vercel.app/llms.txt`
4. Your agent will interview you, propose a team, and (after confirmation) provision profiles

### For HERMES Agents
When you read `site/llms.txt`, you should:
1. **Interview the user** using the questions in `llms.txt`
2. **Design a team** based on their responses
3. **Present the proposal** and wait for explicit confirmation
4. **Provision profiles** using the `forge` skill only after approval

## Bot Mode Integration
This project uses HERMES Bot Mode (beta), which provides:
- Isolated profile directories (config, memory, credentials, chat history)
- Different models per bot
- Shared inbox for bot-to-bot communication
- Cron job support for recurring tasks

**Important:** Bot Mode isolation is at the profile folder level. All bots share the host OS user and filesystem permissions.

## Default Behavior
**"Use My Real Browser Profile" is always the default option.**
Isolated bot-mode profiles are created only if the user explicitly opts in.

## Files
- `site/llms.txt` — AI agent instructions (start here)
- `skills/forge/SKILL.md` — Forge skill for team provisioning
- `runtime/` — Profile provisioning, isolation, and orchestration code
- `PRODUCT.md` — Product requirements and user stories
- `CHANGELOG.md` — Version history
