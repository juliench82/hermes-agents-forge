# Forge Skill — Agent Instructions

## ⚠️ Important

This skill extends HERMES Agent with team design and profile provisioning capabilities.
It requires the runtime/ Python modules to be available.

## Your Task

You are a HERMES agent that has loaded this skill. Execute the following workflow:

1. **Start the forge workflow**: Run `/forge` to begin team design
2. **Interview the user**: Ask about goals, workflows, task complexity
3. **Determine package tier**: Assess if user needs 3/5/7 specialist agents
4. **Propose team**: Present specialist roles, responsibilities, collaboration patterns
5. **Wait for confirmation**: Do not proceed without explicit user confirmation
6. **Provision profiles**: Call runtime modules to create bot-mode profiles
7. **Default to real browser profile**: Use user's existing browser session unless they opt out

## Skill Definition

[... rest of existing SKILL.md content ...]

## Runtime Integration

Profile provisioning requires runtime/ Python modules. See:
- runtime/README.md for setup and integration options
- runtime/profile_provisioner.py for profile creation
- runtime/dynamic_profiles.py for dynamic team generation
- runtime/isolation.py for profile isolation

## Package Tiers

- **Package 3**: 3 agents (researcher, writer, coder) — basic workflows
- **Package 5**: 5 agents (adds analyst, reviewer) — intermediate workflows
- **Package 7**: 7 agents (adds strategist, integrator, QA) — complex workflows
