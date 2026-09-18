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
| Workflow kickoff | One coordinator-owned Kanban control-plane card (enforced) or one local-only `~/.hermes/TEAM.md` handoff receipt |
| Workflow artifacts | `WORKFLOW-CONTRACT.md`, `WORKFLOW-POLICY.md`, `WORKFLOW-RUNBOOK.md`, `TRIAL.md` |
| Approval records | Exact action, target, payload/change, approver, decision, timestamp |
| Context/cost hygiene | Hermes compression, model, reasoning, concurrency, and MOA settings supported by the installed version |

## Stage 1 — Team Setup

Run `skills/forge/SKILL.md` only. Interview the user about broad capability, required specialist roles/tools, constraints, autonomy, communication, approval posture, and forbidden access/actions. Obtain one explicit approval, provision and optimize isolated profiles, generate rich personas and verified team-capability skills, write team contracts/policy, and collect receipts.

Do not create a customer workflow during Stage 1. Do not create workflow execution cards, live integrations, schedules, routines, or trials.

When Team Setup receipts pass:

1. Resolve and record the stable coordinator profile identity.
2. Search `~/.hermes/TEAM.md` and the active Kanban board for `workflow-builder-kickoff:first-workflow:v1`.
3. Reuse exactly one active matching handoff; never create a duplicate.
4. Record the two distinct handoff concepts: `handoff_state` (semantic, e.g. `READY_FOR_WORKFLOW_BUILDER`) and `board_state` (physical Kanban state, or `null`), with `delivery_mode` (`LOCAL_RECORD` | `ENFORCED_CONTROL_PLANE_CARD`) and `dispatcher_enforcement` (`VERIFIED` | `UNSUPPORTED`).
5. A Kanban kickoff card may be created only when the installed dispatcher can enforce routing only to the exact stable coordinator, no specialist spawn, no customer-work tool execution, and control-plane-only state transitions. Native assignee support and idempotency support alone are insufficient.
6. If any enforcement requirement is unavailable, do not create a Kanban kickoff card; append one local-only handoff receipt to `~/.hermes/TEAM.md` and record `WORKFLOW HANDOFF: READY — LOCAL ONLY` with `DISPATCHER ENFORCEMENT: UNSUPPORTED`.
7. Record the handoff receipt.

Record:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

## Stage 2 — Workflow Builder

Run `skills/workflow-builder/SKILL.md` only after the team record and coordinator handoff are verified. Validate metadata, uniqueness, and stable coordinator identity; claim the handoff with a receipt and move it to `DESIGNING` only when beginning the workflow interview.

Draft the workflow contract, policy, runbook, and trial plan. Stop for explicit workflow-design approval. No execution cards, credentials, permission changes, routines, trials, or external actions may occur before that receipt.

After approval, provision only the approved workflow execution and later require supervised trial evidence plus explicit human activation before `OPERATIONAL`.

## Hard rules

- Never ask the user to install or clone anything merely to run Forge.
- Never provision before explicit team approval.
- Never duplicate profiles or enabled builtin skills.
- Never invent skills, tools, models, integrations, or configuration keys.
- Never force past a dangerous security verdict.
- Never claim verification without verbatim receipts.
- Never let the coordinator implement worker-owned tasks.
- Never let specialists own workflow discovery or approval.
- Never execute external or irreversible actions without the applicable approval gate.
- Never treat the kickoff card as ordinary customer-work execution.
- Never treat a general "unblock card" action as authorization for workflow discovery or execution.
- Never create a kickoff card when dispatcher enforcement is unverified; use the local-only handoff record instead.

## References

- Canonical manual: `site/llms.txt`
- Product requirements: `PRODUCT.md`
- Team Setup: `skills/forge/SKILL.md`
- Workflow Builder: `skills/workflow-builder/SKILL.md`
- Team contract: `templates/TEAM-CONTRACT.md`
- Team policy: `templates/TEAM-POLICY.md`
- Workflow kickoff: `templates/WORKFLOW-KICKOFF.md`
- Persona schema: `catalog/roles/soul-schema.md`
- Skills manifest: `catalog/skills.json`
- Official HERMES docs: https://hermes-agent.nousresearch.com/docs/
