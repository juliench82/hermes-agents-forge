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

- Create/modify:
  - Profiles under `profiles/` (bot-mode, isolated, managed by the wizard).
  - Workflows under `onboarding/workflows/`.
  - Minimal metadata files needed to wire profiles into workflows.

This skill **does not** allow:

- Direct edits to `profiles/**` by users or other agents.
- Arbitrary code execution outside the defined entry points.
- Changes to skill definitions or trust boundaries.

## Onboarding contract

When invoked as the onboarding skill, this module must:

1. **Interview**
   - Call `runtime/onboarding_wizard.py` to run the interview.
   - Collect:
     - Target domains (e.g., support, content, ops).
     - Tools/APIs in scope (GitHub, Slack, email, DBs, etc.).
     - Constraints (budget, latency, human-in-the-loop points).
     - Success criteria ("what good looks like").

2. **Design**
   - Use the interview output to propose a minimal team:
     - Roles (e.g., Intake, Specialist, QA, Orchestrator).
     - Responsibilities per role.
     - Handoffs between roles.
   - Present the design to the user and ask for confirmation or adjustments.

3. **Provision**
   - Upon confirmation:
     - Use `runtime/dynamic_profiles.py` to create N isolated bot-mode profiles under `profiles/`.
     - Use `runtime/live_provisioner.py` to:
       - Wire profiles into a sample workflow under `onboarding/workflows/`.
       - Configure triggers, queues, and escalation paths.
   - Ensure each profile:
     - Has a unique identity and credential scope.
     - Is limited to actions allowed by this skill.
     - Communicates via explicit handoffs, not shared mutable state.

4. **Iterate**
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

Any HERMES agent that trusts this skill should be able to run the full funnel:

Interview → Team Design → N Isolated Bot-Mode Profiles → Sample Workflow.