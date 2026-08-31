# PRODUCT.md — Hermes-Agents-Forge Product Requirements

## Product Goal

A customer visits our site, clicks "Read agent instructions", and points their HERMES agent to:
`https://hermes-agents-forge.vercel.app/llms.txt`

From there, any HERMES agent (any LLM, any reasoning level) must:
1. Interview the user
2. Design a custom team of agents
3. Provision isolated bot-mode profiles that collaborate on workflows
4. Default to "Use My Real Browser Profile"

## Core Flow

```
read HERMES.md / trust forge skill
  ↓
interview user
  ↓
propose team
  ↓
get confirmation
  ↓
provision isolated bot-mode profiles
```

## Implementation Mapping (Official HERMES)

| Product Goal | HERMES Primitive | Implementation |
|--------------|------------------|----------------|
| Interview user | `/forge` skill Procedure | `runtime/onboarding_wizard.py` |
| Design team | Skill output (markdown proposal) | `runtime/dynamic_profiles.py` |
| Get confirmation | HERMES `skills.write_approval` pattern | `runtime/confirmation.py` |
| Provision profiles | `hermes profile create <name>` | `runtime/profile_provisioner.py` |
| Isolated bot-mode | Separate profiles under `~/.hermes/profiles/` | `runtime/isolation.py` |
| "Use My Real Browser Profile" | User preference (not HERMES primitive) | Interview question in skill |

## User Experience Requirements

1. **Zero-config onboarding**: User only needs to point their HERMES agent to the llms.txt URL
2. **Any HERMES agent works**: The skill must be compatible with any LLM, any reasoning level
3. **Explicit confirmation**: User must approve the team design before provisioning
4. **Isolated profiles**: Each agent gets its own `~/.hermes/profiles/<name>/` directory
5. **Default shared browser**: "Use My Real Browser Profile" is the default option

## Technical Requirements

1. **Valid HERMES skill**: `skills/forge/SKILL.md` must have YAML frontmatter and standard sections
2. **Official CLI usage**: All profile operations via `hermes profile` commands
3. **Progressive disclosure**: Skill loads on-demand, not in initial context
4. **Verification steps**: Agent confirms profiles exist and respond correctly

## Success Criteria

- [ ] Any HERMES agent can load `/forge` skill from llms.txt
- [ ] Skill executes full interview → design → confirm → provision flow
- [ ] Profiles created via official `hermes profile create` CLI
- [ ] "Use My Real Browser Profile" asked as default before provisioning
- [ ] User can see new agents in `hermes profile list` and Bot Mode roster
