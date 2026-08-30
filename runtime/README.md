# Runtime

Python modules for HERMES-Agents-Forge profile provisioning, isolation, and onboarding.

## Context

This runtime is designed for use with **HERMES Agent's browser automation** capabilities.
When a HERMES agent browses `site/llms.txt`, it executes the forge workflow which calls these runtime modules to provision profiles.

HERMES browser automation docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/browser

## Modules

- `onboarding_wizard.py`: Interview flow and user input collection
- `profile_provisioner.py`: Create and configure bot-mode profiles
- `dynamic_profiles.py`: Dynamic profile generation based on interview
- `isolation.py`: Profile isolation and context boundaries
- `hermes_kernel.py`: Core HERMES integration logic
- `skill_resolution.py`: Skill loading and execution
- [and more...]

## HERMES Integration

To use these runtime modules with HERMES:

### Option 1: MCP Server (Recommended)

1. Expose runtime as MCP server
2. Configure HERMES to call MCP for profile provisioning
3. Forge skill calls MCP endpoints during `/forge` workflow

### Option 2: Direct Python API

1. Install as Python package: `pip install -e .`
2. Import modules directly in skill execution context
3. Call provisioning APIs from forge skill

### Option 3: Standalone Wizard

Run onboarding wizard standalone:
```bash
python runtime/onboarding_wizard.py
```

This generates HERMES config files for manual import.

## Browser Automation Integration

When HERMES agent browses `site/llms.txt`:
1. Agent reads agent-directed instructions
2. Agent loads forge skill
3. Agent runs `/forge` workflow
4. Runtime modules provision profiles using HERMES browser tools
5. Default: "Use My Real Browser Profile" for user's existing session

## Setup

```bash
pip install -r requirements.txt
python -m runtime.smoke_tests
```

## Testing

```bash
python -m runtime.live_acceptance
python -m runtime.evidence_skill_verification
```
