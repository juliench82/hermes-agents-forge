# Team Contract

> Generated during Forge provisioning. Replace bracketed values with the approved team design.

## Team

- **Project:** `[project name]`
- **Coordinator:** `[profile name]`
- **Contract version:** `1`
- **Status:** `proposed | provisioned | trial-passed | operational`

## Operating agreement

The coordinator routes work, records decisions, collects receipts, and reconciles outputs. It does not implement worker-owned tasks. Each worker owns only the responsibilities listed below and must hand off the named artifact to the next role **by creating the next stage's card** (`hermes kanban create --parent <this card> --assignee <next profile>` + artifact + acceptance criteria) — the coordinator never bottlenecks card creation after intake. The decision bot is the only approval layer: every approval gate and the final handoff is a decision card it resolves and routes (`promote` / `request-changes` / `block`).

## Role contracts

### `[profile name]` — `[role]`

- **Owns:**
  - `[responsibility]`
- **Does not own:**
  - `[excluded responsibility]`
- **Inputs:**
  - `[input or event]`
- **Outputs:**
  - `[artifact, status, or decision]`
- **Source of truth:**
  - `[path, board, or system]`
- **Allowed tools and skills:**
  - `[tool or skill]`
- **Approval required before:**
  - `[external or irreversible action]`
- **Must never:**
  - `[forbidden action]`
- **Handoff to:** `[next profile]`
- **Handoff artifact:** `[path or message]`
- **Acceptance criteria:**
  - `[testable criterion]`

### `decision-bot` — `decision-bot`

- **Owns:** every approval gate and the final handoff. Resolves typed decision requests against the configured decision source (customer by default; Jev when Hermes exposes it and the customer approves), records typed decision responses verbatim, and routes `promote` / `request-changes` / `block` with conditions.
- **Does not own:** implementing work, designing, verifying, or inventing approvals.
- **Inputs:** decision cards (`review` state) carrying the decision contract (schema v1: `decision_request` with typed `choice` / `score` / `noul` questions).
- **Outputs:** typed `decision_response` (answers + probabilities/confidence + conditions + routing + approver + timestamp) recorded on the card and in the team/workflow record.
- **Source of truth:** the decision card body and `~/.hermes/TEAM.md`.
- **Allowed tools and skills:** file/read tools and the `kanban` toolset (claim decision cards, `promote`, `request-changes`).
- **Approval required before:** any external or irreversible effect of an approval (a `promote` that deploys, publishes, spends, or contacts third parties is still a customer decision).
- **Must never:** invent an approval when no decision source is reachable — escalate to the customer; approve its own or another worker's work outside a decision card.
- **Handoff to:** the receiving stage (on `promote`), the producing stage (on `request-changes`), or the customer (on `block` / escalation).
- **Acceptance criteria:** every decision card is resolved within the configured source's SLA, the typed response is recorded verbatim, and routing matches the decision.

## Handoff protocol

Every handoff must include:

1. The task and acceptance criteria.
2. The source-of-truth references used.
3. The work completed and evidence produced.
4. Open risks, blockers, and required approvals.
5. The exact next action requested from the receiving role.

The receiving role acknowledges ownership, rejects incomplete context explicitly, and returns the artifact or a blocker—not a duplicate implementation. Workers self-advance the pipeline by creating the next stage's card with the artifact and acceptance criteria attached; approval gates are decision cards, never inline asks.

## Change log

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1 | `[date]` | Initial contract | `[human]` |
