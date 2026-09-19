# Workflow Contract

> Created by Workflow Builder after Team Setup. Replace bracketed values with the approved workflow design.

## Identity and status

- **Workflow:** `[name]`
- **Team record:** `~/.hermes/TEAM.md`
- **Workflow version:** `1`
- **Status:** `DESIGNED | TRIAL-PASSED | OPERATIONAL | PAUSED | RETIRED`
- **Human owner:** `[name]`

## Trigger and outcome

- **Trigger:** `[event, schedule, or manual command — default: one customer-created card (repos + ideas + goal) or one message to the coordinator]`
- **Final outcome:** `[observable result — decision-gated]`
- **Success metric:** `[metric and target]`
- **Dry-run/sandbox scope:** `[scope]`
- **Autonomy contract:** every stage's completion contract includes creating the next stage's card (`hermes kanban create --parent <this card> --assignee <next profile>`, artifact + acceptance criteria attached); the dispatcher daemon drives execution; approval gates and the final handoff are **decision cards** for the decision bot using the decision contract (schema v1: typed `choice` / `score` / `noul` questions → typed `decision_response` with `promote` / `request-changes` / `block` routing).

## Decision gates

- **`[gate name]`** → decision card for `decision-bot` → `promote` / `request-changes` / `block` → `[next action]`
- **(list every approval gate and the final handoff here)**

## Source of truth and boundaries

- **Authoritative inputs:** `[files, systems, or queues]`
- **Expected outputs:** `[files, records, messages, or decisions]`
- **Allowed data boundary:** `[paths, systems, and data classes]`
- **Excluded data/actions:** `[explicit exclusions]`

## Stages and handoffs

### `[stage number]` — `[stage name]`

- **Owner:** `[approved profile]`
- **Inputs:** `[references]`
- **Work:** `[specific action]`
- **Output artifact:** `[path or record]`
- **Handoff to:** `[next profile or human]`
- **Acceptance criteria:**
  - `[testable criterion]`
- **Failure/escalation path:** `[action]`

## Approval boundaries

- **Approval required before:** `[external, irreversible, sensitive, or costly action]`
- **Approver:** `[human or approved role]`
- **Approval record:** `[where decision, target, payload, and timestamp are recorded]`

## Runtime controls

- **Concurrency:** `[maximum]`
- **Timeout:** `[duration]`
- **Retries:** `[count and backoff]`
- **Schedule:** `[if approved]`
- **Delivery target:** `[room, report, or system]`
- **Rollback/pause:** `[command or procedure]`

## Status transitions

`DESIGNED` → `TRIAL-PASSED` → `OPERATIONAL`

Any failed trial returns the workflow to `DESIGNED` or `PAUSED`. Retiring a workflow requires a recorded human decision.

## Change log

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1 | `[date]` | Initial workflow contract | `[human]` |
