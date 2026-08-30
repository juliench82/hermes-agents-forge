# HERMES Agents Forge

## ⚠️ Important: Forge Extensions

The interview → team design → profile provisioning flow described in this project is **not** part of core HERMES Agent.
It is implemented as a **skill pack** that extends HERMES with:
- Pre-interview wizard (external to HERMES)
- Dynamic profile provisioning (via runtime/ Python modules)
- Isolated bot-mode profiles (using HERMES Bot Mode as foundation)

For official HERMES documentation, see: https://hermes-agent.nousresearch.com/docs

---

## Our Product Goal

A customer visits our site, clicks "Read agent instructions", and points their HERMES agent to:
https://hermes-agents-forge.vercel.app/llms.txt

From there, any HERMES agent (any LLM, any reasoning level) must:
1. Interview the user
2. Design a custom team of agents
3. Provision isolated bot-mode profiles that collaborate on workflows

## How It Works

### Step 1: Read HERMES.md / Trust Forge Skill

The user's HERMES agent reads this file and the forge skill at:
https://hermes-agents-forge.vercel.app/skills/forge/SKILL.md

### Step 2: Interview User

The forge skill conducts an interview to understand:
- User's goals and workflows
- Required specialist roles
- Collaboration patterns
- Tool and API needs

### Step 3: Propose Team

Based on interview responses, the forge skill proposes:
- Team composition (specialist bot-mode profiles)
- Role definitions and responsibilities
- Collaboration workflows
- Integration points

### Step 4: User Confirmation

User reviews and confirms the proposed team design.

### Step 5: Provision Isolated Bot-Mode Profiles

The runtime provisions:
- Isolated bot-mode profiles per specialist role
- Shared context and memory across team
- Tool integrations and API access
- Collaboration channels and routines

## Default: Use My Real Browser Profile

All provisioning defaults to "Use My Real Browser Profile" — the user's existing browser session and credentials are used unless they explicitly opt for isolated profiles.

## Architecture

See PRODUCT.md for detailed architecture and runtime/ for implementation.
