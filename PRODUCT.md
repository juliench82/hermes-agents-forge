# Hermes Agents Forge

## Product definition

Hermes Agents Forge is a Hermes-native bootstrap system for creating governed, isolated specialist teams. It provisions profiles, personas, tools, skills, optimization, approval boundaries, and auditable receipts before any customer workflow is activated.

The product deliberately separates **Team Setup** from **Workflow Builder**. This prevents a promising team configuration from being judged by an unrelated or prematurely designed workflow, and it gives customers a clean checkpoint before live integrations, routines, and external actions are introduced.

## Lifecycle

### Phase 1 — Team Setup

Team Setup interviews the customer about broad outcomes, required capabilities, autonomy, constraints, data boundaries, and approval posture. It then designs and provisions the smallest useful team with isolated profiles, rich personas, verified skills, supported model/cost optimization, generic role contracts, and a team-wide policy.

Team Setup does not create workflow-specific cards, schedules, live integrations, production routines, or workflow trials. It finishes with:

```text
TEAM STATUS: PROVISIONED
WORKFLOW STATUS: NONE
```

This means the team itself is ready for workflow design; it does not mean a business process is operational.

### Phase 2 — Workflow Builder

Workflow Builder starts only after a verified team exists. It interviews the customer about one concrete workflow, defines its trigger, outcome, stages, handoffs, source of truth, permissions, approval gates, runtime controls, test scope, and success metrics.

It then creates the workflow contract, workflow policy, runbook, trial plan, and—only after approval—the workflow board/cards, integrations, routines, and controlled execution. A workflow becomes operational only after trial evidence and explicit human activation approval:

```text
TEAM STATUS: PROVISIONED
WORKFLOW STATUS: DESIGNED → TRIAL-PASSED → OPERATIONAL
```

## What Team Setup provides

- A coordinator profile that routes work, maintains receipts, and reconciles outputs without implementing worker tasks.
- One to three isolated workers with distinct, generated capability ownership.
- Rich schema-grounded personas based on the customer’s requirements.
- Builtin, generated, or approved external skills with provenance and verification receipts.
- Team-wide model, concurrency, data, tool, and approval policy.
- Compression and cost controls compatible with the installed Hermes version.
- Durable `TEAM.md`, `TEAM-CONTRACT.md`, and `TEAM-POLICY.md` records.
- Profile smoke tests and auditable completion evidence.

## What Workflow Builder provides

- One specific trigger-to-outcome workflow.
- Workflow-specific contracts, permissions, data boundaries, and acceptance criteria.
- A runbook covering execution, exceptions, monitoring, takeover, pause, and rollback.
- Safe test/sandbox or dry-run configuration.
- Workflow-specific Kanban cards, integrations, routines, and delivery targets.
- Supervised trial evidence and human activation sign-off.

## Customer promise

> First, Forge builds your governed AI team. Then, Workflow Builder connects that team to one process, tests it safely, and activates it only when the evidence supports doing so.

## Non-goals of Team Setup

Team Setup must not claim to have automated a customer workflow. It must not create live schedules, run production tasks, or report workflow success. Those belong to Workflow Builder.

## Status vocabulary

- **Team provisioned:** Profiles, skills, policies, optimization, and receipts are complete.
- **Workflow designed:** A specific workflow contract and policy are approved, but execution has not passed trial.
- **Workflow trial-passed:** Controlled execution met acceptance criteria and preserved approvals.
- **Workflow operational:** Human activation approval exists and the approved runtime is active.
