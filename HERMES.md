# Hermes Agents Forge — Bootstrap Instructions

You are a HERMES agent. The human who points you here is the customer. Read this brief, then follow `site/llms.txt` as the canonical operating manual.

## Product boundary

Hermes Agents Forge has two deliberately separate stages:

1. **Team Setup** provisions the governed, isolated team.
2. **Workflow Builder** applies that existing team to one concrete workflow.

Team Setup must finish before Workflow Builder begins. A successful Team Setup does not prove that any customer workflow works.

## Mapping: Forge concepts → Hermes primitives

| Forge concept | Hermes primitive |
|---|---|
| Coordinator profile | Main/default Hermes profile; record its stable name in `TEAM.md` |
| Isolated specialist | `hermes profile create <name> --description "<role>"` |
| Rich persona | `~/.hermes/profiles/<name>/SOUL.md` |
| Skills engine | `hermes -p <name> skills list` → generated skills → inspected Hub gaps |
| Team receipts | Profile list, full skills lists, config, smoke tests, and `TEAM.md` |
| Team contract/policy | `TEAM-CONTRACT.md` and `TEAM-POLICY.md` |
| Workflow kickoff | One coordinator-owned Kanban control-plane card |
| Workflow artifacts | `WORKFLOW-CONTRACT.md`, `WORKFLOW-POLICY.md`, `WORKFLOW-RUNBOOK.md`, `TRIAL.md` |
| Approval records | Exact action, target, payload/change, approver, decision, timestamp |
| Context/cost hygiene | Hermes compression, model, reasoning, concurrency, and MOA settings supported by the installed version |

## Stage 1: Team Setup

Run `skills/forge/SKILL.md` only. Interview the user about broad capability, required specialist roles/tools, constraints, autonomy, and forbidden access/actions. Obtain approval, provision and optimize isolated profiles, generate rich personas and verified team-capability skills, write team contracts/policy, and collect receipts.

Do not create a customer workflow during Stage 1. Do not create workflow execution cards, live integrations, schedules, routines, or trials.

When team receipts pass:

1. Resolve and record the stable coordinator profile identity.
2. Read `~/.hermes/TEAM.md` and search for the **first-workflow** idempotency key `workflow-builder-kickoff:first-workflow:v1`.
3. If an active first-workflow kickoff card already exists, reuse it; never create a duplicate.
4. Otherwise queue exactly one coordinator-owned control-plane card in `READY` status with the metadata defined by `templates/WORKFLOW-KICKOFF.md`.
5. Record the card ID and a handoff receipt in `~/.hermes/TEAM.md`.

Record:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

## Stage 2: Workflow Builder

Run `skills/workflow-builder/SKILL.md` from the coordinator kickoff card. Verify the team record, stable coordinator identity, kickoff metadata, card uniqueness, and handoff receipt before starting discovery. Keep the card assigned to the coordinator and move it to `DESIGNING` only when the coordinator begins the workflow interview.

Draft the workflow contract, workflow policy, runbook, and trial plan. Record a handoff receipt and stop for explicit workflow-design approval. No execution cards, credentials, permission changes, routines, trials, or external actions may occur before that receipt.

After approval, provision only the approved workflow execution and later require supervised trial evidence plus explicit human activation approval before `OPERATIONAL`.

## Acceptance

Use `ACCEPTANCE.md` to validate the final branch on a fresh Hermes installation or isolated runtime. Do not claim runtime readiness without evidence for Team Setup quality, handoff safety/idempotency, negative separation checks, and Workflow Builder entry checks.
