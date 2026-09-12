# Hermes Agents Forge

## Product definition

Hermes Agents Forge is a Hermes-native bootstrap system for creating governed, isolated specialist teams. It provisions profiles, personas, tools, skills, optimization, approval boundaries, and auditable receipts before any customer workflow is activated.

The product deliberately separates **Team Setup** from **Workflow Builder**. This prevents a promising team configuration from being judged by an unrelated or prematurely designed workflow, and it gives customers a clean checkpoint before live integrations, routines, and external actions are introduced.

## Lifecycle

### Phase 1 — Team Setup

Team Setup interviews the customer about broad outcomes, required capabilities, autonomy, constraints, data boundaries, and approval posture. It then designs and provisions the smallest useful team with isolated profiles, rich personas, verified skills, supported model/cost optimization, generic role contracts, and a team-wide policy.

After all setup receipts pass, Team Setup automatically queues exactly one coordinator-owned **Workflow Builder Kickoff** card in `READY` status. This is an automatic handoff, not automatic automation: the card starts workflow discovery but cannot execute a customer workflow.

Team Setup does not create workflow-specific execution cards, schedules, live integrations, production routines, or workflow trials. It finishes with:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

### Phase 2 — Workflow Builder

The main coordinator picks up the kickoff card and interviews the customer about one concrete workflow. It moves the card to `DESIGNING` and drafts the workflow contract, policy, runbook, and trial plan.

The coordinator must stop and obtain an explicit workflow-design approval receipt. Only then may Workflow Builder create execution cards, configure integrations, change workflow permissions, create routines, or start a trial:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY → DESIGNING
WORKFLOW STATUS: NONE → DESIGNED
```

A workflow becomes operational only after trial evidence and explicit human activation approval:

```text
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
- One coordinator-owned Workflow Builder Kickoff card in `READY` status.

## What Workflow Builder provides

- One specific trigger-to-outcome workflow.
- Workflow-specific contracts, permissions, data boundaries, and acceptance criteria.
- A runbook covering execution, exceptions, monitoring, takeover, pause, and rollback.
- Safe test/sandbox or dry-run configuration.
- Workflow-specific Kanban execution cards, integrations, routines, and delivery targets after approval.
- Supervised trial evidence and human activation sign-off.

## Customer promise

> First, Forge builds your governed AI team. Then, it automatically hands the team to the coordinator for workflow discovery. Nothing is automated until you approve the workflow design and its trial plan.

## Non-goals of Team Setup

Team Setup must not claim to have automated a customer workflow. It must not create live schedules, run production tasks, or report workflow success. Those belong to Workflow Builder after workflow-design approval.

## Status vocabulary

- **Team provisioned:** Profiles, skills, policies, optimization, and receipts are complete.
- **Workflow handoff ready:** One coordinator-owned discovery card is queued; no workflow execution exists.
- **Workflow designing:** The coordinator is gathering requirements and drafting workflow artifacts.
- **Workflow designed:** A specific workflow contract and policy are approved, but execution has not passed trial.
- **Workflow trial-passed:** Controlled execution met acceptance criteria and preserved approvals.
- **Workflow operational:** Human activation approval exists and the approved runtime is active.
