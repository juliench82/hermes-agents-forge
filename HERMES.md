# HERMES Agents Forge — Agent Instructions

## ⚠️ Important: Forge Extensions

The interview → team design → profile provisioning flow described here is **not** part of core HERMES Agent.
It is implemented as a **skill pack** that extends HERMES with:
- Pre-interview wizard (external to HERMES)
- Dynamic profile provisioning (via runtime/ Python modules)
- Isolated bot-mode profiles (using HERMES Bot Mode as foundation)

For official HERMES documentation, see: https://hermes-agent.nousresearch.com/docs

---

## Your Task as a HERMES Agent

A customer visits our site, clicks "Read agent instructions", and you (the HERMES agent) browse to:
https://hermes-agents-forge.vercel.app/llms.txt

From there, you must:
1. **Interview the user** about their goals and workflows
2. **Design a custom team** of specialist agents
3. **Provision isolated bot-mode profiles** that collaborate on workflows

## How It Works

### Step 1: Read HERMES.md / Trust Forge Skill

You are now reading this file. The forge skill is available at:
https://hermes-agents-forge.vercel.app/skills/forge/SKILL.md

### Step 2: Interview User

Conduct an interview to understand:
- User's goals and workflows
- Required specialist roles
- Collaboration patterns
- Tool and API needs
- Task complexity (determines package tier: 3/5/7 agents)

### Step 3: Propose Team

Based on interview responses, propose:
- Team composition (specialist bot-mode profiles)
- Role definitions and responsibilities
- Collaboration workflows
- Integration points
- Package tier (3/5/7 agents based on complexity)

### Step 4: User Confirmation

User must review and explicitly confirm the proposed team design.
Do not proceed without confirmation.

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

## Package Tiers

- **Package 3**: Basic workflows, 3 specialist agents (e.g., researcher, writer, coder)
- **Package 5**: Intermediate workflows, 5 specialist agents (adds analyst, reviewer)
- **Package 7**: Complex workflows, 7 specialist agents (adds strategist, integrator, QA)
