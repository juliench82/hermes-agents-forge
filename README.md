# Hermes Agents Forge

**Hermes-native bootstrap repository for provisioning isolated multi-profile agent teams.**

Point your Hermes agent at this repo and it can:

1. **Discover** bootstrap manifests (`bootstrap.manifest.json`) in the wild
2. **Compile** tenant specs into profile bundles with roles, connectors, triggers, and policies
3. **Provision** isolated Hermes profiles with dynamic skills, context files, and MCP integrations
4. **Onboard** users via guided workflows with acceptance criteria and audit trails

## Quick Start

```bash
# 1. Install Hermes (if not already)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 2. Fast setup (model + tool gateway in one OAuth)
hermes setup --portal

# 3. Trust project-local skills (required)
hermes skills trust

# 4. Install dependencies
pip install -e ".[dev]"

# 5. Run the bootstrap compiler
python -m compiler --manifest bootstrap.manifest.json
```

## Key Docs

| File | Purpose |
|------|---------|
| [`HERMES.md`](./HERMES.md) | Hermes-specific context (highest priority) |
| [`AGENTS.md`](./AGENTS.md) | Cross-tool agent instructions (Claude Code, Codex, Hermes) |
| [`BOOTSTRAP.md`](./BOOTSTRAP.md) | Bootstrap manifest specification |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | How to contribute |
| [`onboarding/START.md`](./onboarding/START.md) | Onboarding quick start |

## Architecture

```
├── bootstrap.manifest.json    # Declarative team spec
├── compiler/                  # Bootstrap discovery, team compilation, rendering
├── runtime/                   # Profile provisioning, skill resolution, policy enforcement
├── catalog/                   # Versioned primitives (roles, connectors, triggers, memory, policies)
├── onboarding/                # Templates, workflows, fixtures for user onboarding
├── shared/                    # Cross-cutting contracts (security, context, skill, workflow policies)
├── skills/forge/              # Project-local forge skill (SKILL.md)
└── site/                      # Public website with llms.txt for LLM discoverability
```

## Key Conventions

- **Manifests over code**: Team specs are declarative JSON/YAML, compiled by `compiler/`
- **Versioned primitives**: Catalog entries use semantic versioning (`1.0.0/primitive.yaml`)
- **Hermes-native alignment**: Connectors map to MCP servers, triggers to `cronjob`, delegation to `delegate_task`
- **Security by design**: All runtime operations reference Hermes's 8-layer security model (see `shared/safety-enforcement.md`)

## Testing

```bash
pytest tests/ -v --cov
```

## License

MIT — see [`LICENSE`](./LICENSE)
