# Hermes Agents Forge

Hermes Agents Forge provisions a governed, isolated Hermes specialist team before it creates any customer workflow.

## Team Setup first

Forge interviews the customer, proposes the smallest useful team, and—after approval—provisions isolated profiles, rich personas, verified capabilities, model/cost optimization, team contracts, approval policy, and auditable receipts.

The main profile is recorded as a stable coordinator identity in `TEAM.md`. The coordinator owns routing, discovery, approvals, and receipts; it never performs worker implementation.

## First Workflow handoff

After setup verification, Forge queues exactly one non-executable control-plane card for the first workflow:

```text
Title: Start Workflow Builder — define first workflow
Assignee: <stable coordinator profile>
Status: READY
Key: workflow-builder-kickoff:first-workflow:v1
Kind: onboarding
Control plane: true
Execution allowed: false
```

If the card already exists, Forge reuses it. If duplicates exist, it stops and reports them. This is an automatic handoff, not automatic automation.

## Workflow Builder

The coordinator claims the card, records the handoff receipt, and moves it to `DESIGNING`. It drafts one workflow contract, policy, runbook, and trial plan, then stops for workflow-design approval.

Only after approval can Workflow Builder create execution cards, connect integrations, change workflow permissions, schedule routines, or run a supervised trial.

## State lifecycle

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
        ↓
WORKFLOW HANDOFF: DESIGNING
WORKFLOW STATUS: DESIGNING
        ↓
WORKFLOW STATUS: DESIGNED
        ↓
WORKFLOW STATUS: TRIAL-PASSED
        ↓
WORKFLOW STATUS: OPERATIONAL
```

## Safety principle

Team Setup builds capability. Workflow Builder applies it to one declared process. Every transition is receipt-backed, and external or irreversible actions remain approval-gated.

Canonical instructions: `site/llms.txt`.
