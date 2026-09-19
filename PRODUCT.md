# Hermes Agents Forge — Product Requirements

## Product definition

Hermes Agents Forge is a Hermes-native bootstrap product for customers who want to create governed, isolated specialist teams from their own goals and capability needs. A customer points Hermes at the canonical `site/llms.txt` instructions; the agent interviews the customer, designs the smallest useful team, provisions it with real profiles and skills, optimizes it, and verifies the result with receipts.

The product is intentionally model-agnostic and role-agnostic. It must generate team roles, personas, skills, boundaries, and handoffs dynamically from the customer's requirements rather than forcing a fixed industry catalog or a pre-stored persona library.

The product has two deliberately separated phases:

1. **Team Setup** creates and verifies the team.
2. **Workflow Builder** applies that existing team to one declared workflow.

The split changes only the stopping point of the original Forge flow. It must not reduce the quality of team design, provisioning, optimization, skill resolution, persona generation, governance, or receipts.

## Customer entry and promise

Customers should not need to clone this repository or manually assemble profiles. They provide Hermes with the canonical LLM instructions, and Forge guides the setup flow from there.

The customer promise is:

> First, Forge builds your governed AI team. Then it hands that team to the coordinator for workflow discovery. Nothing is automated until the workflow design is approved, the supervised trial passes, and activation is explicitly approved.

## Phase 1 — Team Setup

Team Setup asks only for broad capability and governance inputs:

- Broad outcome or capability target.
- Required specialist capability domains, tools, and data sources.
- Model/provider and budget constraints.
- Privacy, data-sensitivity, and compliance boundaries.
- Autonomy, communication, and approval posture.
- Forbidden access, modifications, and actions.

It does not ask for a business-process trigger, production schedule, workflow-specific source of truth, workflow acceptance criteria, or live test data.

### Team package sizing

The team is generated dynamically using exactly one package:

- **3 specialists:** focused single-domain work with limited coordination.
- **5 specialists:** multi-stage work requiring analysis, implementation, review, and reconciliation.
- **7 specialists:** complex multi-domain or coordination-heavy work.

The coordinator is separate from the package count and owns routing, control-plane operations, contracts, receipts, memory, and reconciliation. It never implements worker-owned tasks. Four- and six-specialist packages are not used because they create ambiguous sizing and unnecessary coordination overhead.

### Team Setup outputs

After one explicit approval, Team Setup provisions:

- Isolated Hermes profiles with stable names and unambiguous descriptions.
- Rich schema-grounded `SOUL.md` personas grounded in the customer's own words.
- Team-wide contracts, data/tool boundaries, approval gates, and operating policy.
- Builtin skills first, generated skills for genuine capability gaps, and inspected/security-scanned external skills only where required.
- Model, compression, reasoning, browser, MOA, concurrency, and cost optimization supported by the installed Hermes version.
- Smoke tests for role identity, boundaries, and assigned capabilities.
- Verbatim profile, skill, configuration, and verification receipts.
- Durable append-only team records under `~/.hermes/TEAM.md`.

### Team Setup completion

Team Setup must not claim workflow success. It completes only after all setup receipts pass and creates/reuses one non-executable coordinator handoff for the first workflow — but only when the installed dispatcher can enforce routing only to the exact stable coordinator, no specialist spawn, no customer-work tool execution, and control-plane-only state transitions. Native assignee support and idempotency support alone are insufficient. If any enforcement requirement is unavailable, Team Setup records a local-only handoff in `~/.hermes/TEAM.md` and creates no Kanban card.

Enforced control-plane card (dispatcher enforcement verified):

```yaml
kind: onboarding
control_plane: true
execution_allowed: false
workflow_scope: first-workflow-only
idempotency_key: workflow-builder-kickoff:first-workflow:v1
assignee: <stable coordinator profile name>
handoff_state: READY_FOR_WORKFLOW_BUILDER
delivery_mode: ENFORCED_CONTROL_PLANE_CARD
dispatcher_enforcement: VERIFIED
board_state: <actual Kanban state>
```

Local-only handoff (dispatcher enforcement unsupported), appended to `~/.hermes/TEAM.md`:

```yaml
handoff_state: READY_FOR_WORKFLOW_BUILDER
delivery_mode: LOCAL_RECORD
dispatcher_enforcement: UNSUPPORTED
idempotency_key: workflow-builder-kickoff:first-workflow:v1
coordinator_profile: <stable coordinator>
team_record: ~/.hermes/TEAM.md
workflow_execution_allowed: false
next_required_action: explicit founder instruction to start Workflow Builder
timestamp: <ISO-8601>
```

The final Team Setup state is:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
DISPATCHER ENFORCEMENT: VERIFIED
```

or, for a local-only handoff:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY — LOCAL ONLY
WORKFLOW STATUS: NONE
DISPATCHER ENFORCEMENT: UNSUPPORTED
```

Team Setup never creates workflow execution cards, schedules, routines, live integrations, trials, or external workflow actions.

## Phase 2 — Workflow Builder

Workflow Builder starts only after Team Setup has produced a verified team record and valid coordinator handoff. It does not recreate the team or silently broaden its permissions.

### Workflow Builder responsibilities

Workflow Builder:

- Interviews the user about one concrete trigger-to-outcome workflow.
- Assigns approved specialists to workflow stages only after workflow-design approval.
- Defines workflow-specific inputs, outputs, sources of truth, handoffs, acceptance criteria, exceptions, and status transitions.
- Creates `WORKFLOW-CONTRACT.md`, `WORKFLOW-POLICY.md`, `WORKFLOW-RUNBOOK.md`, and `TRIAL.md`.
- Uses workflow-specific IDs and idempotency keys; later workflows do not reuse the first-workflow key.
- Stores workflow artifacts and receipts under `~/.hermes/workflows/<workflow-id>/` while `TEAM.md` remains the team-level index.
- Creates execution cards, integrations, routines, and delivery targets only after explicit workflow-design approval.
- Runs a supervised trial with safe data, sandbox, dry-run, or limited scope.
- Requires explicit human activation approval before `OPERATIONAL`.

Before workflow-design approval, Workflow Builder may only validate the handoff, claim it safely, interview the user, and create drafts. It may not create execution cards, credentials, permission changes, routines, trials, or external actions.

## Governance and trust

- One explicit approval is required before Team Setup provisioning.
- Workflow-design approval is required before workflow execution assets.
- External and irreversible actions remain approval-gated.
- The coordinator owns discovery, approval reconciliation, routing, and receipts; specialists execute approved stages only.
- Skills are inspected and security-scanned; dangerous verdicts are never forced.
- Unsupported configuration keys, unavailable integrations, provider failures, and skipped capabilities are reported explicitly.
- Receipts are preferred over assertions.
- A workflow is not operational until supervised trial evidence and explicit activation approval exist.

## Coordination surfaces

Team Setup may prepare the coordinator/control-plane surface and a non-executable handoff. Workflow Builder owns workflow-specific Kanban execution cards, routines, integrations, delivery targets, and trial evidence. The control-plane kickoff must never be treated as ordinary customer-work execution.

## Status vocabulary

- **Team provisioned:** Profiles, personas, skills, optimization, contracts, policy, and setup receipts are complete.
- **Workflow handoff ready:** One coordinator-owned first-workflow discovery handoff exists as an enforced control-plane card or a local-only `~/.hermes/TEAM.md` receipt; `dispatcher_enforcement` is `VERIFIED` or `UNSUPPORTED`; no workflow execution exists. The semantic handoff state is never confused with a physical Kanban status.
- **Workflow designing:** The coordinator is interviewing the user and drafting workflow artifacts.
- **Workflow designed:** A workflow contract and policy are approved; execution has not yet passed trial.
- **Workflow trial-passed:** Controlled execution met acceptance criteria and preserved approval boundaries.
- **Workflow operational:** Human activation approval exists and the approved runtime is active.

## Verification principle

Every setup and workflow state transition requires evidence. Never treat profile or skill creation as proof that a workflow works. Never claim completion without verbatim receipts, and never claim runtime readiness without testing the installed Hermes environment.

## Source files

- Canonical instructions: `site/llms.txt`
- Bootstrap brief: `HERMES.md`
- Team Setup: `skills/forge/SKILL.md`
- Workflow Builder: `skills/workflow-builder/SKILL.md`
- Persona schema: `catalog/roles/soul-schema.md`
- Skills manifest: `catalog/skills.json`
- Team contract: `templates/TEAM-CONTRACT.md`
- Team policy: `templates/TEAM-POLICY.md`
- Workflow kickoff: `templates/WORKFLOW-KICKOFF.md`
- Workflow contract/policy/runbook/trial: `templates/WORKFLOW-*.md`
- Official Hermes docs: https://hermes-agent.nousresearch.com/docs/
