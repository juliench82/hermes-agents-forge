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

The agent asks these questions one at a time:

1. **What would you like to automate or build with HERMES?** (e.g., "triage GitHub issues", "generate weekly reports")
2. **What tools or APIs does this workflow need?** (GitHub, Slack, email, DBs, VPS, etc.)
3. **How many isolated bot profiles do you want?** (3 for simple single-domain, 5 for multi-stage, 7 for strict separation)
4. **What are your constraints?** (budget, latency, human-in-the-loop points)
5. **What does success look like?** (e.g., "90% of issues triaged in <5 min", "daily report by 9am")

If Python is available, the agent can also run:

```bash
python -m runtime.onboarding_wizard
```

The wizard collects the same information programmatically.

### 3. Team design

Based on the interview, the agent:

- Proposes a minimal team (e.g., intake triage, specialist, QA, orchestrator).
- Presents each role's:
  - Responsibilities.
  - Allowed actions (via the Forge skill).
  - Handoffs to other roles.
- Asks the user for confirmation or adjustments.

### 4. Profile provisioning

Once confirmed, the agent provisions the team. Two paths:

**Path A — Python runtime (preferred):**

- Uses `runtime/dynamic_profiles.py` + `runtime/live_provisioner.py` to:
  - Create N isolated bot-mode profiles under `profiles/`.
  - Configure each profile's:
    - Identity (name, role, avatar/metadata).
    - Allowed actions (via skill policies).
    - Workflow hooks (triggers, queues, channels).
- Creates one sample workflow under `onboarding/workflows/` that:
  - Exercises the team end-to-end.
  - Demonstrates handoffs and escalation paths.

**Path B — Hermes CLI (fallback, no Python required):**

- For each profile:
  - `hermes profile create <name> --description "<role>"`
  - Write `~/.hermes/profiles/<name>/SOUL.md` with: role, in-scope product, out-of-scope, handoffs.
- Create a workflow file under `onboarding/workflows/` that exercises the team.

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
  - Legacy modules (Buzz, Obsidian, duplicate audit, unused installer paths) have been removed.

- **compiler/**
  - Used internally as a backend to generate manifests from a design.
  - Not the user-facing entry point.

- **skills/forge/**
  - `SKILL.md` — defines the trusted capability boundary for interview + provisioning.

- **profiles/**
  - Managed by the wizard/provisioner or Hermes CLI.
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