# Hermes Agents Forge — Product Requirements

## Product definition

Hermes Agents Forge is a Hermes-native product that provisions **governed, isolated specialist teams that run as a persistent autonomous work force**. A customer points Hermes at the canonical `site/llms.txt` instructions; the agent interviews the customer once (defaults first, one question for non-default cases), designs the smallest useful team, provisions it with real profiles and skills, optimizes it, verifies it with receipts, and hands it off as a self-driving work force that reports to a single **decision bot** and a stable coordinator.

The product is intentionally model-agnostic and role-agnostic. It must generate team roles, personas, skills, boundaries, and handoffs dynamically from the customer's requirements rather than forcing a fixed industry catalog or a pre-stored persona library.

The product has two deliberately separated phases:

1. **Team Setup** creates and verifies the team, including the decision bot.
2. **Workflow Builder** applies that team to one declared workflow as an autonomous, self-advancing chain.

The split changes only the stopping point of the original Forge flow. It must not reduce the quality of team design, provisioning, optimization, skill resolution, persona generation, governance, or receipts.

## Customer entry and promise

Customers should not need to clone this repository or manually assemble profiles. They provide Hermes with the canonical LLM instructions, and Forge guides the setup flow from there.

The customer promise is:

> First, Forge builds your governed AI team — a work force that picks up your repos and ideas and runs them itself. Its only checkpoints are the coordinator (routing) and the decision bot (approvals). Nothing is automated until the workflow design is approved, the supervised trial passes, and activation is explicitly approved.

## Operating model — the autonomous work force

A provisioned team behaves like a small 9-to-5 company, not a prompt queue:

- **Manual request in, decision out.** The customer starts work with one manual request: a card (repos + ideas + goal) or a message to the coordinator. After that, the chain runs itself.
- **Workers own the pipeline.** Each stage's completion contract includes *creating the next stage's card* (`hermes kanban create --parent <this card> --assignee <next profile>` with artifact paths and acceptance criteria attached). The coordinator does not bottleneck card creation after intake.
- **The dispatcher is the engine.** `hermes kanban daemon` (60-second ticks) picks up assigned cards automatically; workers are spawned, work, create the next card, and the chain advances with no human in between.
- **The decision bot is the only approval layer.** Every approval gate and the final handoff produce a decision card assigned to the decision bot. Nothing proceeds past it without a recorded decision. Workers never approve each other; the coordinator never substitutes its judgment for a decision.
- **9-to-5 pulse (optional, post-trial).** A cron hygiene job on the coordinator can sweep intake, run dispatch, and surface stalled cards on a schedule. It is never enabled before the supervised trial passes and activation is approved.

### Decision bot

Every team receives exactly one **decision bot** — a dedicated profile **outside** the specialist package count (like the coordinator). Its contract:

- Receives decision cards (kanban `review` state) containing a **typed decision request** (see Decision contract).
- Resolves the request against the configured decision source and records the typed response verbatim.
- Routes the outcome: `promote` (proceed), `request-changes` (revise), or `block` (stop), with conditions.
- Never invents approvals. If no decision source is reachable, it escalates to the customer.

**Decision sources, in order of preference:**

| Source | Mode | When |
|---|---|---|
| Human (customer) | The decision bot renders the typed questions as a short plain-language form in chat; the customer answers; answers are mapped back into the contract | Default, always available |
| Jev (TypeSafe AI "System One" model — a **model**, never a skill) | The same typed decision request is sent as a Jev API call (`state` + typed `choice` / `score` / `noul` questions); typed answers return in 70–500 ms with calibrated probabilities | When Hermes exposes Jev as a provider/model. Not yet available through Nous Portal at time of writing; this build's provider cache lists `jev-1.13-free` under the keyless `opencode-free` lane, and the TypeSafe AI API/SDK is the direct alternative. Until then the human source is active |

The decision request is **identical in both modes** — the human path is a rendering of the same schema. That is what makes Jev a drop-in decision source: the work force already emits structured, typed handoffs; it never writes prose and asks Jev to parse it.

### Decision contract (canonical schema, v1)

Stored on every decision card and appended verbatim to the team/workflow record:

```yaml
decision_request:
  schema_version: "1"
  decision_id: <uuid or card id>
  workflow_id: <workflow-id>
  stage: <producing stage>
  state:                    # the "program state" the decision source evaluates
    artifacts: [<paths>]
    evidence: [<command-output references / citations>]
    acceptance_results: {<criterion>: pass|fail|not-testable}
    guardian_verdict: PASS|PASS_WITH_CONDITIONS|FAIL   # when applicable
    approval_gates_triggered: [<gate names>]
    risk_summary: <plain-language risk summary>
  questions:                # typed; mirrors the Jev API exactly
    final_verdict:
      type: choice
      instructions: "How should this handoff proceed?"
      options: [promote, revise, reject, escalate]
    approved_as_is:
      type: noul
      instructions: "The recommended decision should be accepted as-is"
    confidence:
      type: score
      instructions: "Rate confidence in the recommendation"
      labels: [low, medium, high]

decision_response:
  schema_version: "1"
  decision_id: <same>
  decision_source: human | jev
  answers:
    final_verdict: {type: choice, choice: promote, probabilities: {...}, confidence: <0..1>}
    approved_as_is: {type: noul, noul: <0..1>}
    confidence: {type: score, score: <value>, legend: {...}, confidence: <0..1>}
  conditions: [<free-text / typed conditions>]
  routing: promote | request-changes | block
  approver: <customer or jev>
  timestamp: <ISO-8601>
```

Jev primitives (TypeSafe AI, launched 2026-09-15): **choice** — pick from a fixed option set, returns the winning key + probability per option + confidence; **score** — rate against ordered labels, returns a continuous score + distribution + confidence; **noul** — a yes/no question, returns the probability of "yes" (the caller picks the threshold).

## Phase 1 — Team Setup

Team Setup asks for broad capability and governance inputs, **defaults first**:

1. Present the default team and governance model in plain language (one short summary).
2. Ask one simple question: **"Is there any specific non-default case for you?"**
   - No → proceed with the defaults.
   - Yes → capture the specific case(s) and adapt only those dimensions.

Customers are non-technical; the default must be a good experience, and the one question is the escape hatch. Design and governing personas are still grounded in the customer's own words when provided.

It does not ask for a business-process trigger, production schedule, workflow-specific source of truth, workflow acceptance criteria, or live test data.

### Team package sizing

Exactly one specialist package:

- **3 specialists:** focused single-domain work with limited coordination.
- **5 specialists:** multi-stage work requiring analysis, implementation, review, and reconciliation.
- **7 specialists:** complex multi-domain or coordination-heavy work.

The coordinator and the decision bot are separate from the package count. Every team gets exactly one coordinator and one decision bot. Four- and six-specialist packages are not used because they create ambiguous sizing and unnecessary coordination overhead.

### Team Setup outputs

After one explicit approval, Team Setup provisions:

- Isolated Hermes profiles with stable names and unambiguous descriptions: the specialists, the coordinator, and the decision bot.
- Rich schema-grounded `SOUL.md` personas grounded in the customer's own words.
- Team-wide contracts, data/tool boundaries, approval gates, and operating policy — with the decision bot as the sole approval layer.
- Builtin skills first, generated skills for genuine capability gaps, and inspected/security-scanned external skills only where required.
- Model, compression, reasoning, browser, MOA, concurrency, and cost optimization supported by the installed Hermes version.
- Smoke tests for role identity, boundaries, and assigned capabilities — including a decision-contract smoke test on the decision bot.
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
decision_bot_profile: <decision bot>
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

- Interviews the user about **one** concrete trigger-to-outcome workflow (defaults first; one non-default question).
- Redefines the workflow as the autonomous chain: intake → worker-self-advancing stages → decision-bot gates → final decision → routing.
- Defines workflow-specific inputs, outputs, sources of truth, handoffs, acceptance criteria, exceptions, and status transitions.
- Documents worker card-creation permissions, the decision contract, and the decision routing map (which verdicts `promote` / `request-changes` / `block` which cards).
- Creates `WORKFLOW-CONTRACT.md`, `WORKFLOW-POLICY.md`, `WORKFLOW-RUNBOOK.md`, and `TRIAL.md`.
- Uses workflow-specific IDs and idempotency keys; later workflows do not reuse the first-workflow key.
- Stores workflow artifacts and receipts under `~/.hermes/workflows/<workflow-id>/` while `TEAM.md` remains the team-level index.
- Creates execution assets (cards, integrations, routines, delivery targets) only after explicit workflow-design approval.
- Runs a supervised trial that must prove the chain **self-advances without a coordinator nudge** and that the decision gate is exercised with a typed decision record.
- Requires explicit human activation approval before `OPERATIONAL`.

Before workflow-design approval, Workflow Builder may only validate the handoff, claim it safely, interview the user, and create drafts. It may not create execution cards, credentials, permission changes, routines, trials, or external actions.

## Governance and trust

- One explicit approval is required before Team Setup provisioning.
- Workflow-design approval is required before workflow execution assets.
- **The decision bot is the only approval layer; workers never approve each other, and the decision bot never invents approvals.**
- External and irreversible actions remain approval-gated.
- The coordinator owns discovery, receipts, routing, and reconciliation; specialists execute approved stages and self-advance the pipeline by creating the next stage's card; the decision bot owns approvals.
- Skills are inspected and security-scanned; dangerous verdicts are never forced.
- Unsupported configuration keys, unavailable integrations, provider failures, and skipped capabilities are reported explicitly.
- Receipts are preferred over assertions.
- A workflow is not operational until supervised trial evidence and explicit activation approval exist.
- The 9-to-5 pulse (cron) is never enabled before trial-passed and activation approval.

## Coordination surfaces

Team Setup provisions the coordinator/control-plane surface, the decision bot, and a non-executable handoff. Workflow Builder owns workflow-specific Kanban execution cards, routines, integrations, delivery targets, and trial evidence. The control-plane kickoff must never be treated as ordinary customer-work execution, and the decision bot is the only approved consumer of decision cards.

## Status vocabulary

- **Team provisioned:** Profiles (specialists + coordinator + decision bot), personas, skills, optimization, contracts, policy, and setup receipts are complete.
- **Workflow handoff ready:** One coordinator-owned first-workflow discovery handoff exists as an enforced control-plane card or a local-only `~/.hermes/TEAM.md` receipt; `dispatcher_enforcement` is `VERIFIED` or `UNSUPPORTED`; no workflow execution exists. The semantic handoff state is never confused with a physical Kanban status.
- **Workflow designing:** The coordinator is interviewing the user and drafting workflow artifacts.
- **Workflow designed:** A workflow contract and policy are approved; execution has not yet passed trial.
- **Workflow trial-passed:** Controlled execution met acceptance criteria — including self-advancement without coordinator nudges and a typed decision-gate record — and preserved approval boundaries.
- **Workflow operational:** Human activation approval exists and the approved runtime is active.

## Verification principle

Every setup and workflow state transition requires evidence. Never treat profile or skill creation as proof that a workflow works. Never claim completion without verbatim receipts, and never claim runtime readiness without testing the installed Hermes environment — including a live dispatcher tick and a real decision-contract exchange.

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