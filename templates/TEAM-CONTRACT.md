# Team Contract

> Generated during Forge provisioning. Replace bracketed values with the approved team design.

## Team

- **Project:** `[project name]`
- **Coordinator:** `[profile name]`
- **Contract version:** `1`
- **Status:** `proposed | provisioned | trial-passed | operational`

## Operating agreement

The coordinator routes work, records decisions, collects receipts, and reconciles outputs. It does not implement worker-owned tasks. Each worker owns only the responsibilities listed below and must hand off the named artifact to the next role.

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

## Handoff protocol

Every handoff must include:

1. The task and acceptance criteria.
2. The source-of-truth references used.
3. The work completed and evidence produced.
4. Open risks, blockers, and required approvals.
5. The exact next action requested from the receiving role.

The receiving role acknowledges ownership, rejects incomplete context explicitly, and returns the artifact or a blocker—not a duplicate implementation.

## Change log

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1 | `[date]` | Initial contract | `[human]` |
