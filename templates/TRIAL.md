# Workflow Trial

> This report belongs to Workflow Builder. Team Setup must not use it to claim a workflow is operational.

## Trial identity

- **Workflow:** `[name]`
- **Team record:** `~/.hermes/TEAM.md`
- **Trial ID:** `[identifier]`
- **Date:** `[date]`
- **Human approver:** `[name]`
- **Outcome:** `planned | passed | failed | needs-changes`

## Scope and safety

- **Test data/sandbox:** `[scope]`
- **Production access:** `disabled | limited | approved`
- **Dry-run:** `yes | no`
- **Rollback/pause procedure:** `[procedure]`

## Mission

- **Task:** `[one real workflow task]`
- **Acceptance criteria:**
  - `[criterion]`
  - The chain **self-advances without a coordinator nudge** (each stage creates the next stage's card; dispatcher timestamps show pickup without manual intervention).
  - At least one **decision gate is exercised with a typed `decision_response`** (choice answer + routing + conditions + timestamp), and routing moved the chain (`promote`) or returned it (`request-changes`).
  - No approval bypass: no stage completed without a decision record where the contract required one.
- **Roles involved:** `[approved profiles]` + `decision-bot`
- **Final integrator:** `[profile]`

## Evidence log

| Step | Owner | Input/source | Output/artifact | Handoff/approval | Result |
|---|---|---|---|---|---|
| 1 | `[profile]` | `[reference]` | `[artifact]` | `[handoff]` | `pass / fail` |
| … | `[producing profile]` | `[artifact]` | `decision card + decision_request` | `decision-bot → promote / request-changes / block` | `pass / fail` |

## Trial review

- **Ownership was clear:** `yes | no`
- **Required context was passed:** `yes | no`
- **Duplicate work occurred:** `no | yes — describe`
- **Blockers and exceptions were visible:** `yes | no`
- **Approval gates were preserved:** `yes | no`
- **Final output met acceptance criteria:** `yes | no`
- **Retries/errors:** `[count and details]`
- **Cost and duration:** `[usage, elapsed time]`

## Corrective actions

- `[contract, policy, skill, permission, handoff, or roster change]`

## Sign-off

- **Human decision:** `approve | reject | revise`
- **Activation approved:** `yes | no`
- **Decision date:** `[date]`
- **Next review:** `[date or trigger]`
