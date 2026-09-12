# Workflow Builder Kickoff

> Control-plane onboarding card only. It starts discovery; it cannot execute customer work.

## Machine-readable metadata

```yaml
kind: onboarding
control_plane: true
execution_allowed: false
workflow_scope: first-workflow-only
idempotency_key: workflow-builder-kickoff:first-workflow:v1
assignee: <stable coordinator profile name>
status: READY
```

## Dispatcher routing contract

The dispatcher must route cards with `control_plane: true` and `execution_allowed: false` only to the exact stable coordinator profile. It must not spawn a specialist, claim the card as customer work, execute tools on behalf of the card, or advance it past the approved control-plane state machine.

If the dispatcher cannot parse or enforce this metadata, it must leave the card unclaimed and record `DISPATCHER_UNSUPPORTED_CONTROL_PLANE_METADATA` in the handoff receipt. Forge must record the handoff as `READY — QUEUED LOCALLY` rather than creating an executable card.

## Card identity and idempotency

- **Title:** `Start Workflow Builder — define first workflow`
- **Type:** `onboarding/control-plane`
- **Assignee:** the exact `COORDINATOR PROFILE` recorded in `TEAM.md`
- **Expected initial status:** `READY`
- **Idempotency scope:** first workflow only
- **Idempotency key:** `workflow-builder-kickoff:first-workflow:v1`
- **Duplicate rule:** At most one non-closed card may use this key. Reuse it if present; stop on duplicates.

## Preconditions

- `TEAM STATUS` equals `PROVISIONED`.
- `WORKFLOW STATUS` equals `NONE`.
- `WORKFLOW HANDOFF` equals `READY`.
- `COORDINATOR PROFILE` is resolved and matches the assignee.
- Team receipts and policy paths are recorded.

## Objective

Interview the customer and propose exactly one first workflow for the existing team.

## Required output

Create drafts only:

- `WORKFLOW-CONTRACT.md`.
- `WORKFLOW-POLICY.md`.
- `WORKFLOW-RUNBOOK.md`.
- `TRIAL.md`.
- A handoff receipt containing card ID, key, metadata, coordinator, prior/new state, artifact paths, and next approval required.

## Claim and recovery protocol

Claiming the card is a two-phase operation:

1. Validate metadata, team preconditions, uniqueness, and coordinator identity.
2. Atomically write the claim receipt and transition `READY → DESIGNING`.
3. If either write fails, do not continue discovery. Re-read the card and receipt:
   - If both show the new state and receipt, resume.
   - If neither changed, retry once with the same idempotency key.
   - If they disagree, mark the handoff `CLAIM-RECOVERY-REQUIRED` and stop.

Receipt schema:

```yaml
receipt_type: workflow-handoff
workflow_scope: first-workflow-only
idempotency_key: workflow-builder-kickoff:first-workflow:v1
card_id: <card id>
prior_state: READY
new_state: DESIGNING
coordinator_profile: <stable profile name>
team_record: ~/.hermes/TEAM.md
artifact_paths: []
approval_required: workflow-design
timestamp: <ISO-8601 timestamp>
```

## Forbidden before workflow-design approval

- Execution cards.
- Live integrations or credentials.
- Permission changes.
- Routines or schedules.
- Trials.
- External or irreversible actions.

## Acceptance criteria

- Exactly one active first-workflow kickoff card exists.
- Machine-readable metadata is present and valid.
- The exact stable coordinator profile owns the card.
- The card is not executable by a workflow dispatcher.
- Discovery artifacts are drafts only.
- No workflow execution asset or external action was created.
- Handoff receipt is written before completion.

## State machines

Card state:

```text
READY → DESIGNING → DESIGNED
```

Team/workflow state:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY → DESIGNING
WORKFLOW STATUS: NONE → DESIGNING → DESIGNED → TRIAL-PASSED → OPERATIONAL
```

Later workflows use their own workflow ID and idempotency key. The first-workflow key must not be reused.
