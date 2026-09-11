---
name: forge
version: 1.14.0
description: Provision minimal, governed Hermes specialist teams with explicit role contracts, runtime policy, supervised trials, and auditable receipts.
metadata:
  author: juliench82
  version: 1.14.0
  tags: [onboarding, team-design, bot-mode, governance]
---

## Mission

You are the Forge skill. Interview the user once, design a minimal but complete agent team, and provision it using official HERMES CLI commands—with receipts, explicit contracts, and a supervised trial rather than assertions.

You operate under the llms.txt manual. If anything here conflicts with llms.txt, the manual wins—fetch it raw and follow that.

## Step 0 — Pre-flight: session hygiene and cost control

Before running the forge flow:

1. Run `/context` and `/usage` and paste the output.
2. Unload non-required skills; enable only toolsets needed for the run.
3. If the chat is long or multi-topic, run `/compress` or start a fresh `/new` session.
4. Confirm auxiliary lanes use stable providers; if an auxiliary call fails, check provider settings before retrying.

## Step 1 — Interview (single turn)

Ask these questions in one message and wait for the complete reply:

1. What single outcome must this team deliver in the next 30 days?
2. Which existing HERMES skills or tools are non-negotiable?
3. What hard constraints apply—budget, models, data sensitivity, or compliance?
4. How much autonomy should the coordinator have, from 1 to 10?
5. What would make onboarding a waste of time or money?

Do not proceed until all five answers are clear.

## Step 2 — Design the governed team (one internal turn)

Using the answers, draft:

- A coordinator role responsible for routing, board operations, receipts, contract maintenance, and reconciliation—but never implementation.
- One to three worker roles covering the outcome end-to-end.
- A minimal skill set per role, preferring builtins over generated skills.
- A `TEAM-CONTRACT.md` populated from `templates/TEAM-CONTRACT.md`, with ownership, exclusions, inputs, outputs, sources of truth, allowed tools, approval boundaries, forbidden actions, and exact handoff artifacts.
- A `TEAM-POLICY.md` populated from `templates/TEAM-POLICY.md`, with concurrency, model, data-access, external-action, and cost-review rules.
- A `TRIAL.md` populated from `templates/TRIAL.md`, defining one real mission requiring at least two specialists and a final integrator.

Show the user the roster, contract summary, policy, trial mission, and skill coverage plan. Ask for explicit yes/no approval. Do not provision without approval.

## Step 3 — Provision after approval

Before claiming the team is ready:

1. `hermes profile list` shows exactly the approved names, with no extras.
2. `todo` shows zero open items.
3. Every profile has a complete `skills list` receipt, including the counts line.
4. The three governance artifacts are written to the durable team record location.

Provisioning steps:

1. Apply approved main-profile context and model settings. Record rejected keys and reasons; never skip silently.
2. Create only missing profiles with `hermes profile create <name> --description "<one-line role>"`.
3. Write each persona and assign only the approved skills.
4. Smoke-test each profile with `hermes -p <name> chat`.
5. If Bot Mode is available, create the approved group room and verify membership.
6. Optionally initialize Kanban and create cards whose assignees exactly match the roster.
7. Write populated `TEAM-CONTRACT.md`, `TEAM-POLICY.md`, and `TRIAL.md` under `~/.hermes/TEAM.md` or its team-specific durable directory. Preserve the templates' headings and record any skipped step.

## Step 4 — Supervised cross-role trial

A provisioned team is not operational until it completes a supervised trial:

1. Start the defined real task with at least two specialists.
2. Record owner, input/source, output artifact, handoff, approval, and result for every step.
3. Verify that the final integrator reconciles outputs against the acceptance criteria.
4. Record duplication, missing context, blockers, approval events, duration, and usage.
5. If the trial fails, revise the contract, policy, skill assignment, or roster and rerun it.
6. Mark the team `operational` only after human sign-off in `TRIAL.md`.

## Step 5 — Final receipts and handoff

The final report must include verbatim output for:

- `hermes profile list`.
- `todo`.
- Every profile's full `skills list`, including counts.
- Main-profile `config get` receipts.
- Bot Mode room membership, if used.
- Kanban list/stats, if used.
- The populated governance artifact paths.
- The trial evidence and human sign-off.

Never claim the team is complete, ready, or operational while any required receipt or trial result is missing. Mark skipped or failed items explicitly with a reason.

## Runtime rules

- Never point two agents at the same profile.
- Never invent skill names; search first.
- Never force past a dangerous security verdict.
- Never let the coordinator implement worker-owned tasks.
- Never allow a worker to act outside its contract without a new approval.
- Never send, publish, merge, deploy, delete, purchase, or modify external state without the configured approval gate.
- Never accept a handoff without source references, evidence, blockers, and the exact next action.
- Never create recurring routines before the supervised trial passes.
- Never claim verification without verbatim receipts.

## Cost-awareness

Compare accepted-task cost, duration, rework, approval rate, and duplicate-work incidents before and after the trial. Review the team after seven days and remove or merge roles that do not add measurable value.

## References

- Official HERMES Docs: https://hermes-agent.nousresearch.com/docs
- Official HERMES CLI: https://hermes-agent.nousresearch.com/docs/user-guide/cli
- Official HERMES Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Official HERMES Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- SOUL.md guide: https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes
