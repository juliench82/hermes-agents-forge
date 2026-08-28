# Forge Skill — HERMES Agents

## Purpose

This skill is the trusted entry point for the HERMES Forge onboarding flow. It enables any HERMES agent to:

1. Interview the user about what they want to automate.
2. Design a custom team of specialized agent profiles.
3. Provision isolated bot-mode profiles that collaborate on workflows.

## Trust boundary

When a user's HERMES agent trusts this skill, it authorizes the following actions **only within this repo**:

- Read:
  - `HERMES.md`
  - `site/llms.txt`
  - `runtime/onboarding_wizard.py`
  - `runtime/dynamic_profiles.py`
  - `runtime/live_provisioner.py`
  - `onboarding/workflows/**`
  - `profiles/**` (for inspection, not manual edit)

- Execute:
  - `python -m runtime.onboarding_wizard`
  - `python -m runtime.onboarding_wizard --refine`
  - `hermes profile create <name> --description "<role>"`
  - `hermes profile list`

- Create/modify:
  - Profiles under `profiles/` (bot-mode, isolated).
  - `~/.hermes/profiles/<name>/SOUL.md` per profile.
  - Workflows under `onboarding/workflows/`.

This skill **does not** allow:

- Direct edits to `profiles/**` by users or other agents (use the wizard or Hermes CLI).
- Arbitrary code execution outside the defined entry points.
- Changes to skill definitions or trust boundaries.

## Onboarding contract

When invoked as the onboarding skill, this module must:

### 1. Interview

Ask these questions one at a time. Wait for each answer before asking the next.

1. **What would you like to automate or build with HERMES?** (e.g., "triage GitHub issues", "generate weekly reports")
2. **What tools or APIs does this workflow need?** (GitHub, Slack, email, DBs, VPS, etc.)
3. **How many isolated bot profiles do you want?** (3 for simple single-domain, 5 for multi-stage, 7 for strict separation)
4. **What are your constraints?** (budget, latency, human-in-the-loop points)
5. **What does success look like?** (e.g., "90% of issues triaged in <5 min")

If Python is available, the agent can delegate to:
`python -m runtime.onboarding_wizard`

### 2. Design

Based on the interview, propose a minimal team as a table:

| Profile | Role | Responsibility | Allowed actions | Handoffs |

- Roles (e.g., Intake, Specialist, QA, Orchestrator).
- Responsibilities per role.
- Handoffs between roles.
- Present the design and ask for confirmation or adjustments.

### 3. Provision

Upon confirmation, create each profile:

**Path A — Python runtime:**
- `runtime/dynamic_profiles.py` creates N isolated bot-mode profiles under `profiles/`.
- `runtime/live_provisioner.py` wires profiles into a sample workflow under `onboarding/workflows/`.

**Path B — Hermes CLI (no Python required):**
- For each profile:
  - `hermes profile create <name> --description "<role>"`
  - Write `~/.hermes/profiles/<name>/SOUL.md` with: role, in-scope product, out-of-scope, handoffs.
- Create a workflow file under `onboarding/workflows/` that exercises the team.

Ensure each profile:
- Has a unique identity and credential scope.
- Is limited to actions allowed by this skill.
- Communicates via explicit handoffs, not shared mutable state.

### 4. Validate

- Run: `hermes profile list`
- Report: profiles created, SOUL.md files written, workflow file created, anything failed.
- Then stop.

### 5. Iterate

- Support `--refine` to:
  - Re-run a shortened interview.
  - Adjust roles and responsibilities.
  - Re-provision affected profiles and workflows.

## Security & isolation

- Profiles are isolated by:
  - Separate identity and credential scopes.
  - Skill-enforced action boundaries.
  - Explicit handoffs instead of shared state.

- This skill enforces:
  - What actions profiles can take.
  - Where they can write (paths, APIs, channels).
  - When human confirmation is required.

## Implementation notes

- The interview logic lives in `runtime/onboarding_wizard.py`.
- Profile creation and configuration live in `runtime/dynamic_profiles.py`.
- Workflow wiring lives in `runtime/live_provisioner.py`.
- This `SKILL.md` defines the **policy** and **contract**, not the implementation details.
- Legacy runtime modules (Buzz, Obsidian, duplicate audit, unused installer paths) have been removed.

Any HERMES agent that trusts this skill should be able to run the full funnel:

Interview → Team Design → N Isolated Bot-Mode Profiles → Sample Workflow.