# Hermes Agents Forge

Hermes Agents Forge helps customers build a governed AI team first, then apply that team to one workflow at a time.

## Start here

A customer points Hermes to the canonical instructions:

`https://hermes-agents-forge.vercel.app/llms.txt`

Forge then conducts the setup interview and provisions the team from the customer’s requirements—no repository clone or manual installation is required for the Forge flow.

## Team Setup first

After one explicit approval, Forge provisions:

- The smallest useful coordinator-plus-worker team, selected from broad capability needs rather than a fixed industry catalog.
- Isolated Hermes profiles with rich role personas.
- Verified builtin, generated, or approved external skills.
- Model, compression, reasoning, concurrency, and cost optimization.
- Team-wide contracts, tool boundaries, approval policy, and auditable receipts.
- A durable `~/.hermes/TEAM.md` team record.

Team Setup does not create a live business workflow, connect workflow integrations, schedule routines, or run a trial.

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

If the card already exists, Forge reuses it. If duplicates exist or the dispatcher cannot enforce the metadata, it stops or queues the handoff locally rather than creating executable work. This is an automatic handoff, not automatic automation.

## Workflow Builder

The coordinator claims the card with a receipt, moves it to `DESIGNING`, asks the workflow interview questions, and drafts one workflow contract, policy, runbook, and trial plan. It then stops for workflow-design approval.

Only after approval can Workflow Builder create execution cards, connect integrations, change workflow permissions, schedule routines, or run a supervised trial. Workflow-specific artifacts live under `~/.hermes/workflows/<workflow-id>/`.

## Validation

Use `ACCEPTANCE.md` for the fresh-install acceptance plan. Distinguish specification readiness from runtime readiness; do not claim production readiness without evidence.

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

## Trust and safety

- One approval is required before team provisioning.
- Workflow-design approval is required before workflow execution assets.
- External and irreversible actions remain approval-gated.
- Skills are inspected and security-scanned; dangerous verdicts are never forced.
- Receipts are preferred over assertions.
- A workflow is not operational until supervised trial evidence and explicit activation approval exist.

Canonical instructions: `site/llms.txt`.
