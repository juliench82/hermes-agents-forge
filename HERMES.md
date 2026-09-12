# Hermes Agents Forge — Bootstrap Instructions

Point Hermes at this repository or its `site/llms.txt` instructions. Follow the two-stage lifecycle exactly.

## Stage 1: Team Setup

Run `skills/forge/SKILL.md` only. Interview the user about broad capability, required specialist roles/tools, constraints, autonomy, and forbidden access/actions. Obtain approval, provision and optimize isolated profiles, generate rich personas and verified team-capability skills, write team contracts/policy, and collect receipts.

Do not create a customer workflow during Stage 1. Do not create workflow execution cards, live integrations, schedules, routines, or trials.

When team receipts pass:

1. Read `~/.hermes/TEAM.md` and check for `workflow-builder-kickoff:v1`.
2. If an active kickoff card already exists, reuse it; never create a duplicate.
3. Otherwise queue exactly one coordinator-owned control-plane card titled `Start Workflow Builder — define first workflow` in `READY` status with that idempotency key.
4. Record the card ID and a handoff receipt in `~/.hermes/TEAM.md`.

Record:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

## Stage 2: Workflow Builder

Run `skills/workflow-builder/SKILL.md` from the coordinator kickoff card. Verify the team record, kickoff idempotency key, card uniqueness, and handoff receipt before starting discovery. Keep the card assigned to the main coordinator/profile 0 and move it to `DESIGNING` only when the coordinator begins the workflow interview.

Draft the workflow contract, workflow policy, runbook, and trial plan. Record a handoff receipt and stop for explicit workflow-design approval. No execution cards, credentials, permission changes, routines, trials, or external actions may occur before that receipt.

After approval, provision only the approved workflow execution and later require supervised trial evidence plus explicit human activation approval before `OPERATIONAL`.
