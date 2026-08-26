# Bootstrap Manifest Specification

The **bootstrap manifest** (`bootstrap.manifest.json`) is the declarative team specification that drives the Hermes Agents Forge compiler.

## What It Is

A JSON file that defines:
- **Tenant identity** — name, description, isolation boundaries
- **Agent roster** — roles (architect, builder, orchestrator, etc.), skills, connectors, triggers
- **Delegation graph** — how work flows between agents
- **Security policies** — approval gates, secret handling, isolation rules
- **Onboarding workflows** — acceptance criteria, audit trails, handoff contracts

## Schema

Validated against [`schemas/bootstrap-manifest.v1.schema.json`](./schemas/bootstrap-manifest.v1.schema.json).

## Minimal Example

```json
{
  "$schema": "./schemas/bootstrap-manifest.v1.schema.json",
  "tenant": {
    "name": "solo-founder-app-builder",
    "description": "Single-founder app development team",
    "isolation": {
      "dataNamespace": "solo-founder"
    }
  },
  "agents": [
    {
      "id": "orchestrator",
      "role": "orchestrator",
      "isolation": {
        "dataNamespace": "solo-founder.orchestrator"
      },
      "skills": ["coordinate-task"],
      "connectors": ["github"],
      "triggers": ["cron"]
    },
    {
      "id": "builder",
      "role": "builder",
      "isolation": {
        "dataNamespace": "solo-founder.builder"
      },
      "skills": ["implement-feature"],
      "connectors": ["github"],
      "requiresApprovalFor": ["git.push"]
    }
  ],
  "delegation": [
    {"from": "orchestrator", "to": "builder", "condition": "task.type == 'implementation'"}
  ],
  "policies": {
    "approvalGates": ["git.push", "github.write"],
    "secretHandling": "hermes-vault"
  }
}
```

## How the Compiler Uses It

```bash
python -m compiler --manifest bootstrap.manifest.json
```

The compiler (`compiler/`):
1. **Validates** the manifest against the v1 schema
2. **Discovers** bootstrap manifests in the wild (for activation)
3. **Compiles** the tenant spec into profile bundles
4. **Renders** Hermes-compatible outputs:
   - `runtime.json` — agent definitions, skills, connectors, routing
   - `coordination.json` — delegation graph, handoff contracts, workflows
   - `manifest.json` — bundle metadata, security flags, fingerprint
   - Profile assets (`profiles/<role>/profile.yaml`, `skill.md`)

## Key Conventions

- **Manifests over code**: Team specs are declarative JSON, compiled by `compiler/`
- **Versioned primitives**: Catalog entries (`catalog/`) use semantic versioning (`1.0.0/primitive.yaml`)
- **Isolation namespaces**: Each agent gets a unique `dataNamespace` for session/memory boundaries
- **Explicit delegation**: Work handoffs are declared in the `delegation` array, not inferred
- **Security by design**: Approval gates, secret handling, and isolation rules are part of the manifest

## Related Docs

- [`HERMES.md`](./HERMES.md) — Hermes-specific context and Quick Start
- [`AGENTS.md`](./AGENTS.md) — Cross-tool agent instructions
- [`README.md`](./README.md) — Project overview and architecture
- [`schemas/bootstrap-manifest.v1.schema.json`](./schemas/bootstrap-manifest.v1.schema.json) — JSON Schema definition
- [`catalog/`](./catalog/) — Versioned primitives (roles, connectors, triggers, policies)
- [`compiler/`](./compiler/) — Bootstrap discovery, team compilation, rendering
