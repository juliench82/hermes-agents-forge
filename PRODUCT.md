# Product Goal

A customer visits our site, clicks "Read agent instructions", and their HERMES agent (with browser automation enabled) browses to:
https://hermes-agents-forge.vercel.app/llms.txt

From there, any HERMES agent (any LLM, any reasoning level) must:
1. **Interview the user** about their goals and workflows
2. **Design a custom team** of specialist agents (3/5/7 based on complexity)
3. **Provision isolated bot-mode profiles** that collaborate on workflows

## Agent-Directed Flow

This product is designed for **HERMES agents with browser automation** to read and execute.

When a HERMES agent browses `site/llms.txt`, it should:
- Recognize these are instructions for itself
- Load the forge skill
- Execute `/forge` workflow
- Interview the user, propose team, provision profiles

## Package Tiers

Based on interview responses about task complexity, propose one of:

- **Package 3** (Basic): 3 specialist agents
  - Typical roles: researcher, writer, coder
  - For: simple workflows, single-project focus

- **Package 5** (Intermediate): 5 specialist agents
  - Typical roles: researcher, writer, coder, analyst, reviewer
  - For: multi-project workflows, quality assurance needs

- **Package 7** (Complex): 7 specialist agents
  - Typical roles: researcher, writer, coder, analyst, reviewer, strategist, integrator, QA
  - For: complex workflows, team coordination, enterprise needs

## Architecture Notes

This product extends HERMES Agent with:
- External onboarding wizard (runtime/onboarding_wizard.py)
- Dynamic profile provisioning (runtime/profile_provisioner.py)
- Isolated bot-mode profiles (runtime/isolation.py + HERMES Bot Mode)

Core HERMES provides:
- CLI and gateway infrastructure
- Bot Mode for named specialist agents
- Skills system for reusable workflows
- Browser automation with real-profile browsing

The integration between our runtime and HERMES is via:
- MCP server (recommended)
- Direct Python API (alternative)

## User Flow

1. User visits site, clicks "Read agent instructions"
2. User's HERMES agent (with browser tools) browses to `site/llms.txt`
3. HERMES agent reads instructions, loads forge skill
4. Agent runs `/forge` and conducts interview
5. Agent determines package tier (3/5/7) based on complexity
6. Agent proposes team design
7. User confirms team design
8. Runtime provisions isolated bot-mode profiles
9. User now has team of specialist Bots in HERMES

## Default: Use My Real Browser Profile

All provisioning defaults to "Use My Real Browser Profile" — the user's existing browser session and credentials are used unless they explicitly opt for isolated profiles.
