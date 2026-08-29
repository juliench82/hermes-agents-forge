# Forge Skill — Team Provisioning

## Name
forge

## Description
Provisions isolated bot-mode profiles for HERMES agents after user interview and confirmation.

## Procedure

### Step 1: Review Interview Responses
Read the user's answers to:
- What workflows do you want to automate?
- How many specialized agents (1-5)?
- Preference: main profile or isolated bots?

### Step 2: Generate Team Proposal
Create a proposal with:
- 1-5 bot roles (e.g., "Researcher", "Coder", "Reviewer")
- For each role:
  - Suggested model (can differ per bot)
  - Required skills
  - Memory isolation level

### Step 3: Present for Confirmation
Show the user:
```
Proposed Team:
- Bot 1: [Role] — Model: [X] — Skills: [Y]
- Bot 2: [Role] — Model: [X] — Skills: [Y]
...

Default: "Use My Real Browser Profile" (no isolation)
Option: Create isolated bot-mode profiles

Do you approve this team? (yes/no)
```

**Wait for explicit "yes" or "approve" before proceeding.**

### Step 4: Provision Profiles
If user confirms:
- If "Use My Real Browser Profile": configure the main profile with the team's skills
- If isolated bots: create profiles under `~/.hermes/profiles/forge-{role}/`
  - Each profile gets its own: config, memory, credentials, chat history
  - Set up shared inbox for bot-to-bot communication
  - Configure cron jobs if needed

### Step 5: Verify
Run `hermes profile list` to confirm profiles exist.
Test each bot with a simple command.

## References
- `site/llms.txt` — Interview questions and workflow
- `runtime/profile_provisioner.py` — Profile creation logic
- `runtime/isolation.py` — Isolation verification
