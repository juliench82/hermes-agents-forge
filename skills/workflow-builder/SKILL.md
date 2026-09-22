---
name: workflow-builder
version: 1.6.6
description: Design, test, and activate a workflow as an autonomous self-advancing chain with a decision-bot approval layer, using an existing provisioned Hermes team.
metadata:
  author: juliench82
  version: 1.6.6
  tags: [workflow, orchestration, kickoff, trial, activation, idempotency, control-plane, governance, decision-bot, autonomy]
---

## Mission

You are Workflow Builder. Apply an existing provisioned Hermes team to one declared workflow as an **autonomous, self-advancing chain**: the customer's manual request starts the pipeline, each stage's completion contract includes creating the next stage's card, the dispatcher daemon drives execution, and every approval gate plus the final handoff is a **decision card** resolved by the decision bot. The coordinator owns discovery and receipts; specialists execute approved stages and self-advance the pipeline; the decision bot owns all approvals. Do not create profiles or redesign the team unless a documented capability gap is approved.

## Workflow scope

- The initial automatic kickoff uses `workflow-builder-kickoff:first-workflow:v1` and can create only the first workflow.
- Later workflows must use their own workflow identifier and idempotency key, for example `workflow:<workflow-slug>:v1`.
- Never reuse the first-workflow key for a later workflow.

## Entry gate

Before discovery:

- **Version handshake (do this first):** compare the copy of this skill you are about to follow against the canonical `skills/workflow-builder/SKILL.md`@`main` (frontmatter version; fetch from `@main` when the local copy is missing, stale, or unverifiable). A cache (`~/.hermes/forge-source/`) or a copy left by another session is stale-by-default and never authoritative. Record the verdict — local vs canonical version, source followed — in the receipts.

1. Confirm `~/.hermes/TEAM.md` exists and contains `TEAM STATUS: PROVISIONED`.
2. Resolve the stable `COORDINATOR PROFILE` from `TEAM.md` and the `DECISION BOT PROFILE`.
3. Confirm the first-workflow kickoff key or an explicit later-workflow invocation.
4. Confirm the delivery mode:
   - `ENFORCED_CONTROL_PLANE_CARD` with `dispatcher_enforcement: VERIFIED` — confirm exactly one non-closed matching kickoff card exists and is assigned to the stable coordinator profile.
   - `LOCAL_RECORD` with `dispatcher_enforcement: UNSUPPORTED` — confirm the local-only handoff receipt carrying `workflow-builder-kickoff:first-workflow:v1` exists in `~/.hermes/TEAM.md` and that an explicit founder instruction to start Workflow Builder was received. Without that instruction, do not begin the workflow interview.
5. Confirm team roster (specialists + coordinator + decision bot), skills, contracts, policy, and handoff receipt.
6. If missing or duplicated, stop and report; never guess.

## Control-plane card contract

The first-workflow kickoff card must contain:

```yaml
kind: onboarding
control_plane: true
execution_allowed: false
idempotency_key: workflow-builder-kickoff:first-workflow:v1
assignee: <stable coordinator profile name>
handoff_state: READY_FOR_WORKFLOW_BUILDER
delivery_mode: ENFORCED_CONTROL_PLANE_CARD
dispatcher_enforcement: VERIFIED
board_state: <actual Kanban state>
```

The `handoff_state` is the semantic handoff state; `board_state` is the physical Kanban state. Never use one for the other, and never describe a card as ready when its actual board state is something else.

The dispatcher must route this card only to the exact coordinator and must not spawn a specialist or execute customer-work tools. If the dispatcher cannot enforce the metadata, the card must remain unclaimed and the handoff must be queued locally. A kickoff card may be created only when the installed dispatcher can enforce routing only to the exact stable coordinator, no specialist spawn, no customer-work tool execution, and control-plane-only state transitions. Native assignee support and idempotency support alone are insufficient.

## Delivery modes

Workflow Builder must accept either delivery mode:

- `LOCAL_RECORD`, or
- `ENFORCED_CONTROL_PLANE_CARD`.

For a `LOCAL_RECORD`, require an explicit founder instruction to start Workflow Builder before it asks the workflow interview.

For an enforced Kanban card, require:

1. validated stable coordinator identity;
2. validated team record;
3. validated idempotency key;
4. claim receipt;
5. valid state transition to `DESIGNING`.

Never let a general "unblock card" action itself become authorization to perform workflow discovery or execution.

## Tool policy for Forge-managed artifacts

Use Hermes builtin file tools for every Forge-managed artifact:

- SOUL.md
- generated SKILL.md files
- TEAM.md
- TEAM-CONTRACT.md
- TEAM-POLICY.md
- Workflow Builder draft artifacts
- Kanban card-body source content
- receipt files

Use Hermes CLI only for Hermes runtime operations and verbatim receipts:

- profile management
- supported configuration operations
- skill registry inspection
- Kanban state operations
- authentication operations
- smoke-test execution

Prohibit content manipulation through shell and generic code execution:

```md
Do not use `cat`, `head`, `tail`, `echo`, shell substitution, heredocs,
`sed`, `awk`, `grep`, `rg`, `find`, Python direct-file operations, or
temporary-file content transport to read, compose, search, patch, or
write Forge-managed artifacts.
```

Allow a narrow exception only when a builtin file tool is unavailable:

```md
If a required builtin file tool is unavailable, stop and record SKIPPED
with the exact unavailable tool and reason. Do not substitute shell or
generic code execution for an append-only or safety-relevant artifact.
```

Kanban body rule:

```md
A Kanban card body must be composed as a controlled literal or retrieved
using a builtin file read. It must be included verbatim in the handoff
receipt. Do not pass card bodies through temporary files or shell command
substitution.
```

Verification receipt:

```text
TOOL POLICY COMPLIANCE
- Forge-managed artifact file operations: builtin tool only | PASS/FAIL
- CLI use: runtime operations and receipts only | PASS/FAIL
- Shell/generic-code artifact-content operations: none | list deviations
- Temporary content files for artifacts: none | list deviations
```

## Explicit workflow interview

Apply the **Interview rule** (defaults first, one non-default question). Present the default workflow design in one short plain-language summary, then ask **"Is there any specific non-default case for you?"** The default design covers:

1. **Team:** the existing provisioned team (coordinator + all specialists + decision bot).
2. **Trigger and outcome:** the customer starts one manual request (a card with repos + ideas + goal, or a message to the coordinator); success is defined by the workflow's approval-gated outcome (e.g. a verified runnable artifact or a decision-ready recommendation).
3. **Goal shape — must be elicited before designing stages:** ask what the customer is starting from — **(a) a new idea to build, (b) an existing project to improve/complete to a working state, or (c) both.** The stage chain must be designed around the actual goal shape, never assumed:
   - New idea → challenge → evidence → (re-challenge) → build.
   - **Existing project** → runs an **audit-and-fix loop**, not a single named slice. Existence is the trigger, never a kill reason. The chain: independent audit (`quality-guardian`: full-clone, run the real build/tests, probe the money paths, produce a prioritized findings report Critical/Major/Minor/hygiene with command/line receipts) → remediation design (`product-architect`: an ordered series of branches/commits, critical-first, each PR-sized with its own acceptance criteria) → **fix loop** (the builder fixes one batch via branch → PR → CI → merge; the verifier re-checks each landed fix; loop to the next batch) → report. **Default stop line:** fix all Critical + Major findings autonomously, then report and ask the customer before tackling Minor/hygiene; the customer can raise or lower it any time. Every fix is a proper branch→PR→merge, never a direct-to-main push.
   - Where the customer's goals span both, encode a lane split in the contract (commercial/new-idea vs personal/existing-project) rather than forcing one shape.
4. **Inputs/outputs:** customer-provided repos/ideas as inputs; artifacts under `~/.hermes/workflows/<workflow-id>/` as outputs; `~/.hermes/TEAM.md` and the `default` board as source of truth.
5. **Stages:** the approved specialist chain from Team Setup; each stage owns its next-stage card creation; every approval gate and the final handoff is a decision card for the decision bot. Stage order follows the goal shape (new-idea vs existing-project), not a one-size template.
6. **Approvals:** the decision bot is the only approval layer; spend, publishing, deploys, credentials, legal/financial actions, and anything external or irreversible are always customer-approved (`promote`/`block` routing).
7. **Runtime:** no schedule; one workflow instance at a time; 2h per-stage timeout; 2 retries then escalate; the 9-to-5 pulse (cron) starts disabled.
8. **Trial scope:** dry-run with synthetic data; the trial must prove self-advancement without a coordinator nudge and one typed decision-gate record.
9. **Metrics/acceptance:** every stage produces its named artifact with a receipt; the chain self-advances; no deliverable reaches the customer without a typed decision record; zero approval-gate breaches and zero personal-data incidents.

Do not provision a team or silently broaden permissions. If a required capability is missing, document the gap and stop for approval rather than changing the team implicitly.

## Claim and recovery protocol

Claiming the kickoff card is a two-phase operation:

1. Validate metadata, team preconditions, uniqueness, and coordinator identity.
2. Atomically write the claim receipt and transition `READY → DESIGNING`.
3. If either write fails, do not continue. Re-read the card and receipt:
   - If both show the new state and receipt, resume.
   - If neither changed, retry once with the same key.
   - If they disagree, mark `WORKFLOW HANDOFF: CLAIM-RECOVERY-REQUIRED` and stop.

The receipt must include card ID, key, prior/new state, coordinator, timestamp, and team record path.

## Workflow design and approval

After a successful claim and interview, set:

```text
WORKFLOW HANDOFF: DESIGNING
WORKFLOW STATUS: DESIGNING
```

Create drafts only:

- `WORKFLOW-CONTRACT.md`.
- `WORKFLOW-POLICY.md`.
- `WORKFLOW-RUNBOOK.md`.
- `TRIAL.md`.

The contract must define trigger, outcome, stages, owners, inputs, outputs, handoffs, **the worker card-creation rules (which profile creates the next card, with what --parent link and artifact)**, the decision-gate map (which gates produce decision cards for the decision bot), the decision contract, source of truth, acceptance criteria, exceptions, approvals, runtime controls, and status transitions. The workflow policy must be at least as restrictive as the team policy.

**Reconcile inside, escalate only what is the customer's call.** The contract must include an internal-reconciliation rule: technical specification/behavior tensions (e.g. an acceptance criterion that conflicts with the intent or a mandate) resolve inside the team — the owner of the produced artifact (the verifier) routes the question to the owning role (e.g. the architect) for interpretation and adopts that answer unless clearly wrong. No specialist escalates a technical specification question to the customer by default. The customer is the escalation target only for (a) scope/budget/trade-off decisions, (b) external or irreversible actions, or (c) a genuine deadlock after the owning role has been consulted. This keeps the pipeline autonomous for non-technical users: design decisions stay in the team, and only truly customer-owned decisions surface.

**Founder surface (human interface protocol).** The contract must define how the customer experiences the pipeline, because the board is a bot-to-bot system of record and is not the customer's primary interface. Every gate and every stage end emits ONE short digest to the customer's channel (chat, or a configured messaging platform like Discord/Telegram served by the gateway), fixed format:

```
DONE      <one line: stage + artifact, no details>
VERDICT   <one line: bot conclusion — PASS / KILLED / needs decision>
WAITING ON YOU  <the single decision + exact reply verbs, e.g. "reply: approve | hold">
```

Rules that must be encoded:
1. **One profile talks to the customer: the coordinator only.** Workers never message the customer directly; their output lands on cards and the coordinator digests it.
2. **One digest per gate.** No walls of text or card dumps; details stay on the card.
3. **Reply verbs are explicit.** Every "WAITING ON YOU" names the exact acceptable replies (`approve` / `hold` / `name a slice` / `accept` / `refresh`).
4. **Gate-card existence rule.** A routing promise ("promote → founder gate R3") is not complete until the gate card EXISTS (created, assigned, `blocked`/`ready`). The coordinator creates gate cards from routing output in the same action; never assume a later stage will create its own gate. Observed live: an R3 push gate was never created after a promote, so a founder's approval comment landed on a dead `done` card.
5. **Customer replies are transcribed, never executed blind.** The coordinator reads the customer's reply (chat or messaging platform) and records it verbatim on the gate card for the decision bot; the decision bot resolves; the coordinator or worker executes only what the typed `decision_response` routes.
6. The kanban remains the only source of truth; the channel is a shorthand human interface, never a second record.

**External delivery method (mandatory).** The contract must require that any push to a remote follows the `github-pr-workflow` skill: cut a feature branch off the latest `origin/main` (zero-drift check first), commit, push the **branch**, open a PR, wait for CI green, then merge (squash) and delete the branch. **Never push directly to `main`/`master`.** A customer "push" approval authorizes the change, not a bypass of the branch→PR→merge method; a direct push requires an explicit recorded exception. Observed live: a verified build was pushed straight to `main` because the contract said only "approval required before pushing" without mandating the method.

### Decision contract

Every decision card carries the typed decision contract from `site/llms.txt` (schema v1): a `decision_request` (state + typed `choice`/`score`/`noul` questions) and, once resolved, a typed `decision_response` with routing (`promote` | `request-changes` | `block`), conditions, approver, and timestamp. The decision source is the customer by default; Jev (TypeSafe AI "System One" model) is a drop-in source when Hermes exposes it and the customer approves the switch — the payload is identical in both modes. The decision-bot profile must keep the bundled `sdlc-review` skill **enabled**: the dispatcher's review lane auto-attaches it to `review`-state cards, and disabling it crashes the spawn with `Unknown skill(s): sdlc-review` (observed live in trial 1).

The decision bot's protocol on each decision card:

1. Read the card and the `decision_request`.
2. Resolve: human source → render the questions as a short plain-language form to the customer; Jev source → submit the same payload to the Jev API/model lane.
3. Record the `decision_response` verbatim on the card (and in the team/workflow record).
4. Apply routing: `promote` → the next stage proceeds or the handoff completes; `request-changes` → the producing stage receives the conditions; `block` → stop and escalate.
5. If no decision source is reachable, escalate to the customer — **never invent an approval**.
6. **Never auto-dispatch a human-source card.** Human-source decision cards are created dispatcher-exempt (`blocked`), and resolution happens in the customer's live channel; a headless dispatcher spawn of a human gate is a process failure, not a valid resolution path.

Record an approval receipt containing workflow ID/version, exact artifact paths, profiles/tools, integration and credential scope, allowed external actions and approvals, test scope, runtime limits, schedule, approver, decision, and timestamp.

Before that receipt, do not create execution cards, connect credentials, change permissions, create routines, start a trial, or perform external actions. After approval, set `WORKFLOW STATUS: DESIGNED` and provision only approved execution assets.

## Autonomy wiring after approval

1. Create the intake card for the first run (or document that the customer's manual request creates it).
2. Confirm each worker's SOUL.md/contract includes the next-stage card-creation rule.
3. Confirm the decision bot is the assigned `review`-state consumer for decision cards, and that the dispatcher is running (verify with `hermes kanban diagnostics` / `hermes kanban dispatch` — the `daemon` subcommand is deprecated; the dispatcher runs in the gateway).
4. Keep the 9-to-5 pulse (cron) **disabled** until the trial passes.

## Supervised trial and activation

Use safe data, sandbox, dry-run, or limited scope. Record stage evidence, handoffs, approvals, blockers, retries, exceptions, duration, usage, and acceptance results.

The trial must additionally prove, with receipts:

1. **Self-advancement:** the chain advances from intake through the stages **without a coordinator nudge** — each stage creates the next stage's card and the dispatcher daemon picks it up (record card parent/child links and timestamps).
2. **Decision gate:** at least one decision card is resolved with a typed `decision_response` (choice answer + routing + conditions + timestamp), and routing actually moved the chain (`promote`) or returned it with conditions (`request-changes`).
3. **No approval bypass:** no stage completed without a decision record where the contract required one.
4. **No headless human-gate resolution:** every human-source decision card was resolved in the customer's live channel with a typed `decision_response`; **no** human-source gate was auto-spawned headlessly by the dispatcher. An auto-spawned human gate fails the trial.

Set `WORKFLOW STATUS: TRIAL-PASSED` only when every acceptance criterion passes. Set `WORKFLOW STATUS: OPERATIONAL` only after explicit human activation approval. On activation, the optional 9-to-5 pulse (a cron hygiene job: intake sweep + `hermes kanban dispatch` + stalled-card surfacing) may be enabled.

## Receipts and runtime rules

Report team status, stable coordinator, decision bot, card metadata, idempotency key, state transitions, handoff/claim receipt, workflow artifacts, approval receipt, execution assets, decision records, trial evidence, activation approval, and skipped/failed items verbatim.

Store workflow-specific artifacts and receipts under `~/.hermes/workflows/<workflow-id>/` and keep `TEAM.md` as the team-level index and status record.

Never allow a specialist to own discovery or workflow-design approval. Never allow workers to approve each other. Never let the decision bot invent an approval. Never reuse an idempotency key for a different workflow. Never act externally without the applicable approval gate.