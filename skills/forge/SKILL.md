---
name: forge
description: Provision a team of HERMES bots based on user requirements
tags: [multi-agent, bot-mode, provisioning]
---

# Forge Skill

## When to Use

Use when a user wants to:
- Create a team of specialist HERMES bots
- Automate multi-agent workflows
- Enable bot-to-bot collaboration

## Procedure

### Step 1: Interview

Ask the user the interview questions from `site/llms.txt` Phase 1.

### Step 2: Proposal

Present the team summary from `site/llms.txt` Phase 2. Wait for explicit "yes" or "proceed".

### Step 3: Provision

For each confirmed bot:

1. **Create profile**:
   ```bash
   hermes profile create <name> --description "<role>"
   ```

2. **Configure**:
   Write to `~/.hermes/profiles/<name>/config.yaml`:
   ```yaml
   agent:
     bot_mode_protocol: true
   browser:
     use_real_profile: true
   model:
     default: <selected-model>
   toolsets:
     - hermes-cli
     - browser
     - terminal  # if requested
   ```

3. **Install skills**:
   ```bash
   hermes -p <name> skills install official/<category>/<skill>
   ```

4. **Inject teammate roster**:
   Add to the profile's Bot Chat system prompt:
   ```
   Teammates:
   - @researcher: Gathers evidence from web, docs, GitHub
   - @coder: Implements features, runs tests, deploys
   - @reviewer: Security audits, challenges assumptions
   
   You can message them with @mentions or the message_agent tool.
   ```

### Step 4: Completion

Present:
```
✅ Team provisioned:
- @researcher (hermes -p researcher chat)
- @coder (hermes -p coder chat)
- @reviewer (hermes -p reviewer chat)

Next steps:
1. Start a group chat: Create → New Group Chat → select all three bots
2. Assign a task: "@researcher gather market data, @coder review the repo"
3. Set routines: Each bot can run scheduled tasks (hermes -p <name> cron list)
```

## Security Notes

- Each bot runs in an isolated profile (`~/.hermes/profiles/<name>/`)
- Real browser profile means the agent acts with your logins — only enable for trusted workflows
- Bot-to-bot messaging uses the `message_agent` tool, available only in canonical Bot Chat sessions
