# Two-Stage Onboarding Acceptance

This contract validates the product split without creating or executing a customer-specific workflow.

## Test environment

Run on a fresh Hermes installation or isolated test profile with the branch's `site/llms.txt` as the canonical instructions. Record Hermes version, branch/commit, model/provider, enabled tools, and usage baseline.

## Phase 1 — Team Setup

Use a generic capability request, not a real business workflow. Do not provide a workflow trigger, schedule, live integration, production source-of-truth mapping, or business acceptance criteria.

Verify:

- [ ] One interview collects broad capability, required specialist capabilities/tools, constraints, autonomy/approval posture, and forbidden access/actions.
- [ ] Team size is exactly 3, 5, or 7 specialists; never 4 or 6.
- [ ] Roles are generated dynamically and have distinct ownership/non-ownership.
- [ ] Coordinator is created/tuned first and has a backed-up original `SOUL.md`.
- [ ] Workers have isolated profiles and rich schema-grounded personas.
- [ ] Supported compression, model, reasoning, browser, and MOA settings are applied or recorded as `SKIPPED` with reasons.
- [ ] Skills resolve builtin → generated → inspected/security-scanned external gaps, without duplicate builtins.
- [ ] Every profile has a complete skills receipt with the counts line.
- [ ] Every profile passes a role/boundary/capability smoke test without executing a business workflow.
- [ ] Team contract, policy, receipts, and zero-open-items checklist exist.
- [ ] `TEAM.md` records the stable coordinator and append-only setup receipts.

## Handoff

Verify after setup receipts pass:

- [ ] Exactly one first-workflow key is used: `workflow-builder-kickoff:first-workflow:v1`.
- [ ] Existing matching handoff is reused; no duplicate is created.
- [ ] Card metadata is present:

```yaml
kind: onboarding
control_plane: true
execution_allowed: false
workflow_scope: first-workflow-only
idempotency_key: workflow-builder-kickoff:first-workflow:v1
assignee: <stable coordinator profile name>
status: READY
```

- [ ] Dispatcher routes only to the coordinator and cannot spawn specialists or customer-work tools.
- [ ] If metadata is unsupported, no executable card is created and the handoff is recorded as `READY — QUEUED LOCALLY`.
- [ ] Handoff receipt records card/local-handoff ID, metadata, assignee, state, timestamp, and dispatcher support verdict.
- [ ] Final Phase 1 status is exactly:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

## Phase 2 — Workflow Builder entry

Do not execute a workflow. Verify only:

- [ ] Workflow Builder rejects missing/unverified team records.
- [ ] Workflow Builder rejects duplicate or malformed kickoff cards.
- [ ] Coordinator claim records a receipt and transitions `READY → DESIGNING`.
- [ ] Interrupted claim can be recovered or becomes `CLAIM-RECOVERY-REQUIRED` without continuing.
- [ ] The explicit workflow interview is present and asks eight workflow questions.
- [ ] Draft workflow artifacts are stored under `~/.hermes/workflows/<workflow-id>/`.
- [ ] No execution cards, integrations, credentials, routines, trials, or external actions occur before workflow-design approval.
- [ ] Later workflows use separate workflow IDs and idempotency keys.

## Negative assertions

The test fails if Team Setup:

- Asks workflow-specific questions.
- Creates a real business workflow.
- Creates a workflow execution card.
- Creates a cron/routine.
- Connects a live integration.
- Runs a workflow trial.
- Assigns a business-process task to a specialist.
- Performs an external or irreversible action.

## Release decision

Do not claim production-ready until every applicable checkbox has evidence. Record unavailable runtime capabilities as `SKIPPED` with a reason; distinguish specification pass from runtime pass.
