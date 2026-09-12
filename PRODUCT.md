# Hermes Agents Forge

## Product definition

Hermes Agents Forge provisions governed, isolated specialist teams. It creates profiles, personas, tools, skills, optimization, approval boundaries, and auditable receipts before applying the team to any customer workflow.

## Two-stage lifecycle

### Phase 1 — Team Setup

Team Setup interviews for broad capability, specialist requirements, constraints, autonomy, data boundaries, and approval posture. It provisions the smallest useful coordinator-plus-worker team, rich personas, verified capabilities, supported optimization, team contracts, team policy, and receipts.

After setup verification, it creates exactly one first-workflow control-plane handoff with key `workflow-builder-kickoff:first-workflow:v1`, unless that active handoff already exists. The handoff is assigned to the stable coordinator profile and is non-executable:

```yaml
kind: onboarding
control_plane: true
execution_allowed: false
workflow_scope: first-workflow-only
idempotency_key: workflow-builder-kickoff:first-workflow:v1
assignee: <stable coordinator>
status: READY
```

This is an automatic handoff, not automatic automation.

Team Setup ends with:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

No workflow execution cards, live integrations, routines, schedules, trials, or external actions are allowed in Phase 1.

### Phase 2 — Workflow Builder

The stable coordinator verifies the handoff and claims the kickoff card. It records the handoff receipt, then transitions:

```text
WORKFLOW HANDOFF: READY → DESIGNING
WORKFLOW STATUS: NONE → DESIGNING
```

It interviews the customer and creates drafts for one workflow. It must obtain explicit workflow-design approval before provisioning execution assets. After approval:

```text
WORKFLOW STATUS: DESIGNING → DESIGNED → TRIAL-PASSED → OPERATIONAL
```

The first automatic handoff is limited to the first workflow. Later workflows use separate workflow IDs and idempotency keys, for example `workflow:<workflow-slug>:v1`.

## Roles

- **Coordinator:** control-plane routing, discovery, approvals, contracts, receipts, and reconciliation; never worker implementation.
- **Specialists:** execute approved workflow stages only; never own workflow discovery or workflow-design approval.

## Customer promise

> First, Forge builds your governed AI team. Then it hands the team to the coordinator for workflow discovery. Nothing is automated until the workflow design is approved, trial evidence passes, and activation is explicitly approved.

## Verification principle

Every setup and workflow state transition requires evidence. Never treat profile or skill creation as proof that a workflow works. Never claim operational status without trial evidence and human activation approval.
