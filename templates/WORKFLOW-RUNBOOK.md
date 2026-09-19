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

1. Confirm the trigger and approved scope (one customer-created card or message).
2. Read the source-of-truth inputs.
3. Create the intake card; the chain self-advances: each stage completes its work, attaches evidence, and **creates the next stage's card** (`hermes kanban create --parent <card> --assignee <next>`) — the dispatcher daemon picks it up on the next tick.
4. At each approval gate and the final handoff, the producing stage creates a **decision card** for the decision bot carrying the typed decision contract; nothing proceeds past it without a recorded `decision_response`.
5. Apply the decision-bot routing: `promote` → next stage proceeds; `request-changes` → back to the producing stage with conditions; `block` → stop and escalate to the customer.
6. Attach evidence to every handoff (artifact path, command output, citation, timestamp).
7. Reconcile the final output against acceptance criteria.
8. Deliver the approved report or result (decision-gated).

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

## Tool policy

Use Hermes builtin file tools for every Forge-managed artifact — this runbook, the workflow contract, policy, trial plan, receipts, and Kanban card-body source content. Use the Hermes CLI only for Hermes runtime operations and verbatim receipts.

Do not use `cat`, `head`, `tail`, `echo`, shell substitution, heredocs, `sed`, `awk`, `grep`, `rg`, `find`, Python direct-file operations, or temporary-file content transport to read, compose, search, patch, or write Forge-managed artifacts.

If a required builtin file tool is unavailable, stop and record SKIPPED with the exact unavailable tool and reason. Do not substitute shell or generic code execution for an append-only or safety-relevant artifact.

A Kanban card body must be composed as a controlled literal or retrieved using a builtin file read. It must be included verbatim in the handoff receipt. Do not pass card bodies through temporary files or shell command substitution.

## Change log

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1 | `[date]` | Initial runbook | `[human]` |
