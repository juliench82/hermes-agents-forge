# Workflow Builder Kickoff

> This is a control-plane onboarding card. It starts workflow discovery; it does not execute a customer workflow.

## Card identity and idempotency

- **Title:** `Start Workflow Builder — define first workflow`
- **Type:** `onboarding/control-plane`
- **Assignee:** main coordinator/profile 0 only
- **Expected initial status:** `READY`
- **Idempotency key:** `workflow-builder-kickoff:v1`
- **Duplicate rule:** There must be at most one non-closed card with this idempotency key. If one exists, update/reuse it; do not create another.

## Preconditions

- `TEAM STATUS` must equal `PROVISIONED`.
- `WORKFLOW STATUS` must equal `NONE`.
- `WORKFLOW HANDOFF` must not already be `COMPLETE` or `CANCELLED`.
- Read `~/.hermes/TEAM.md`, `TEAM-CONTRACT.md`, and `TEAM-POLICY.md`.
- Confirm the roster, team receipts, and coordinator profile are complete.

## Objective

Interview the customer and propose exactly one first workflow for the existing team.

## Required output

Create drafts only:

- `WORKFLOW-CONTRACT.md`.
- `WORKFLOW-POLICY.md`.
- `WORKFLOW-RUNBOOK.md`.
- `TRIAL.md`.
- A handoff receipt containing the card ID, coordinator profile, current state, artifact paths, and next approval required.

The drafts must define the trigger, outcome, stages, owners, inputs, outputs, handoffs, source of truth, acceptance criteria, exception paths, approval gates, runtime controls, safe test scope, and status transitions.

## Forbidden before workflow-design approval

- Do not create workflow execution cards.
- Do not connect live systems or credentials.
- Do not change permissions.
- Do not create or enable routines.
- Do not start a trial.
- Do not send, publish, merge, deploy, pay, delete, or modify external state.

## Stop condition

Present the complete workflow design to the customer and request explicit approval. Record the approval receipt before provisioning workflow execution.

## Acceptance criteria

- Exactly one active kickoff card exists for this team.
- The card remains assigned to the main coordinator/profile 0.
- The card uses the idempotency key above.
- Team status and workflow status preconditions are recorded.
- Discovery artifacts are drafts only.
- No workflow execution asset or external action was created.
- Handoff receipt is written before the card is considered complete.

## State transitions

```text
READY → DESIGNING → DESIGNED
```

The card remains assigned to the main coordinator/profile 0 throughout discovery. Specialist profiles are not assigned until the workflow-design approval exists.
