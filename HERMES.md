# HERMES Agents — Forge

## Product goal

A customer visits the project page, clicks "read agent instructions", and points their HERMES agent to:

https://hermes-agents-forge.vercel.app/llms.txt

From there, any HERMES agent (any LLM, any thinking level) should:

1. Interview the user about what they want to automate.
2. Design a custom team of specialized agent profiles.
3. Provision isolated bot-mode profiles that collaborate on workflows.

## Entry point

The public entry point is:

- `site/llms.txt` — instructions for the user's HERMES agent.
- This file (`HERMES.md`) — product spec and flow description.
- `skills/forge/SKILL.md` — trusted skill that implements interview + provisioning.

## Onboarding flow

### 1. Read + trust

1. The user's agent reads `site/llms.txt`.
2. The agent reads this `HERMES.md` for context.
3. The agent trusts the Forge skill at `skills/forge/SKILL.md`.

This skill is authorized to:

- Ask structured questions about the user's workflows, tools, and constraints.
- Propose a team design (roles, responsibilities, handoffs).
- Create and configure isolated bot-mode profiles under `profiles/`.
- Wire those profiles into a sample workflow under `onboarding/workflows/`.

### 2. Interview

The agent runs:

```bash
python -m runtime.onboarding_wizard
```

`onboarding_wizard`:

- Asks what domains the user wants to automate (e.g., support, content, ops).
- Asks about tools/APIs in scope (GitHub, Slack, email, DBs, etc.).
- Captures constraints (budget, latency, human-in-the-loop points).
- Summarizes a target outcome ("what success looks like").

### 3. Team design

Based on the interview, the agent:

- Proposes a minimal team (e.g., intake triage, specialist, QA, orchestrator).
- Describes each role's:
  - Responsibilities.
  - Allowed actions (via the Forge skill).
  - Handoffs to other roles.
- Asks the user for confirmation or adjustments.

### 4. Profile provisioning

Once confirmed, the agent:

- Uses `runtime/dynamic_profiles.py` + `runtime/live_provisioner.py` to:
  - Create N isolated bot-mode profiles under `profiles/`.
  - Configure each profile's:
    - Identity (name, role, avatar/metdata).
    - Allowed actions (via skill policies).
    - Workflow hooks (triggers, queues, channels).
- Creates one sample workflow under `onboarding/workflows/` that:
  - Exercises the team end-to-end.
  - Demonstrates handoffs and escalation paths.

### 5. Iteration

To refine the team later:

```bash
python -m runtime.onboarding_wizard --refine
```

This re-runs a shortened interview and allows:

- Adding/removing roles.
- Adjusting responsibilities.
- Re-provisioning affected profiles.

## Architecture notes

- **runtime/**  
  - `onboarding_wizard.py` — interview + design orchestration.  
  - `dynamic_profiles.py` — profile creation and configuration.  
  - `live_provisioner.py` — wiring profiles into workflows.

- **compiler/**  
  - Used internally as a backend to generate manifests from a design.  
  - Not the user-facing entry point.

- **skills/forge/**  
  - `SKILL.md` — defines the trusted capability boundary for interview + provisioning.

- **profiles/**  
  - Managed by the wizard/provisioner.  
  - Do not manually edit; use `--refine` to adjust.

## Security & isolation

- Each profile is isolated:
  - Separate identity and credentials.
  - Scoped actions via the Forge skill.
  - Explicit handoffs instead of shared state.

- The Forge skill enforces:
  - What actions profiles can take.
  - Where they can write (paths, APIs, channels).
  - When human confirmation is required.

---

This spec defines the end-to-end funnel:

site button → `/llms.txt` → clone + trust → interview → team design → N isolated bot-mode profiles → one sample workflow.