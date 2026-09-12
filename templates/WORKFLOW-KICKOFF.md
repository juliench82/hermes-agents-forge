# Workflow Builder Kickoff

> This is a control-plane onboarding card. It starts workflow discovery; it does not execute a customer workflow.

## Preconditions

- `TEAM STATUS` must equal `PROVISIONED`.
- Read `~/.hermes/TEAM.md`, `TEAM-CONTRACT.md`, and `TEAM-POLICY.md`.
- Confirm the roster and team receipts are complete.

## Objective

Interview the customer and propose exactly one first workflow for the existing team.

## Required output

Create drafts only:

- `WORKFLOW-CONTRACT.md`.
- `WORKFLOW-POLICY.md`.
- `WORKFLOW-RUNBOOK.md`.
- `TRIAL.md`.

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

## State transitions

```text
READY → DESIGNING → DESIGNED
```

The card remains assigned to the main coordinator/profile 0 throughout discovery. Specialist profiles are not assigned until the workflow-design approval exists.
