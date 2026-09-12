# Hermes Agents Forge

Hermes Agents Forge provisions a governed, isolated Hermes specialist team before it creates any customer workflow.

## Two-stage lifecycle

### 1. Team Setup

Forge interviews the customer, proposes the smallest useful coordinator-plus-worker team, and—after approval—provisions:

- Isolated Hermes profiles.
- Rich role personas.
- Verified builtin, generated, or approved external skills.
- Model, compression, reasoning, concurrency, and cost optimization.
- Team-wide contracts, boundaries, and approval policy.
- Auditable receipts and a durable `~/.hermes/TEAM.md` record.

Team Setup does not create a live business workflow, connect workflow integrations, schedule routines, or run a trial.

After all setup receipts pass, Forge queues exactly one control-plane card:

```text
Start Workflow Builder — define first workflow
Assignee: main coordinator / profile 0
Status: READY
Type: onboarding/control-plane
```

This is an automatic handoff, not automatic automation. The card is a safe next step for workflow discovery; it is not permission to execute customer work.

### 2. Workflow Builder

The main coordinator claims the kickoff card, interviews the customer, and drafts one workflow contract, policy, runbook, and trial plan. It remains in discovery mode until the customer approves the workflow design.

Only after the approval receipt may Workflow Builder create execution cards, connect integrations, change workflow permissions, schedule routines, or start a supervised trial.

## Status lifecycle

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
        ↓
WORKFLOW HANDOFF: DESIGNING
        ↓
WORKFLOW STATUS: DESIGNED
        ↓
WORKFLOW STATUS: TRIAL-PASSED
        ↓
WORKFLOW STATUS: OPERATIONAL
```

## Safety principle

Team Setup builds capability. Workflow Builder applies capability to one declared process. The coordinator owns discovery; specialist profiles do not design or activate workflows. Every transition is receipt-backed, and external or irreversible actions remain approval-gated.

See `PRODUCT.md`, `site/llms.txt`, and the skills under `skills/forge/` and `skills/workflow-builder/` for the canonical operating instructions.
