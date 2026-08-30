# Product Goal

A customer visits our site, clicks "Read agent instructions", and points their HERMES agent to:
https://hermes-agents-forge.vercel.app/llms.txt

From there, any HERMES agent (any LLM, any reasoning level) must:
1. Interview the user
2. Design a custom team of agents
3. Provision isolated bot-mode profiles that collaborate on workflows

## Architecture Notes

This product extends HERMES Agent with:
- External onboarding wizard (runtime/onboarding_wizard.py)
- Dynamic profile provisioning (runtime/profile_provisioner.py)
- Isolated bot-mode profiles (runtime/isolation.py + HERMES Bot Mode)

Core HERMES provides:
- CLI and gateway infrastructure
- Bot Mode for named specialist agents
- Skills system for reusable workflows

The integration between our runtime and HERMES is via:
- MCP server (recommended)
- Direct Python API (alternative)

## User Flow

1. User visits site, reads PRODUCT.md
2. User installs HERMES Agent per official docs
3. User clones hermes-agents-forge repo
4. User runs `hermes skills opt-in --sync` to install forge skill
5. User runs `/forge` in HERMES CLI
6. Forge skill conducts interview (via runtime modules)
7. User confirms team design
8. Runtime provisions isolated bot-mode profiles
9. User now has team of specialist Bots in HERMES

## Default: Use My Real Browser Profile

All provisioning defaults to "Use My Real Browser Profile" — the user's existing browser session and credentials are used unless they explicitly opt for isolated profiles.
