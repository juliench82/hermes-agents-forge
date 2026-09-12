# Workflow Runbook

> Operational instructions created by Workflow Builder. Keep this document synchronized with the approved workflow contract and policy.

## Operating summary

- **Workflow:** `[name]`
- **Owner:** `[human/team]`
- **Current status:** `DESIGNED | TRIAL-PASSED | OPERATIONAL | PAUSED`
- **Start condition:** `[trigger]`
- **Success condition:** `[observable result]`
- **Pause/rollback:** `[procedure]`

## Standard execution

1. Confirm the trigger and approved scope.
2. Read the source-of-truth inputs.
3. Execute stages in the contract order.
4. Attach evidence to every handoff.
5. Stop at the configured approval gate.
6. Reconcile the final output against acceptance criteria.
7. Deliver the approved report or result.

## Handoff checklist

Every handoff includes:

- Task and acceptance criteria.
- Source references.
- Completed work and evidence.
- Open risks, blockers, and approvals.
- Exact next action for the receiving role.

## Exceptions and recovery

### `[Exception]`

- **Detection:** `[signal]`
- **Immediate action:** `[safe action]`
- **Owner:** `[profile or human]`
- **Escalation target:** `[target]`
- **Retry rule:** `[rule]`
- **Evidence required:** `[artifact]`
- **Stop condition:** `[condition]`

## Monitoring

- **Status surface:** `[board, room, dashboard, or report]`
- **Required alerts:** `[alerts]`
- **Review cadence:** `[cadence]`
- **Metrics:** `[metrics]`

## Human takeover

A human takes over when an approval is denied, source data conflicts, a permission boundary is reached, retries are exhausted, or the workflow cannot satisfy an acceptance criterion. The workflow must preserve the current state, evidence, and next safe action.

## Change log

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1 | `[date]` | Initial runbook | `[human]` |
