# Changelog

> **Maintenance policy:** Update this changelog on every meaningful
> repository change (commit, PR, merge, hotfix, migration, or restore) with
> date, version/commit context, what changed, and why.

## [Unreleased]

### v0.7.0 — 2026-09-19
- feat: redefine the team as an **autonomous work force** with a mandatory **decision bot** (`site/llms.txt` v0.7.0, Forge Team Setup v1.25.0, Workflow Builder v1.6.0).
- Added the autonomous work-force operating model: the customer's manual request (one card or one message) starts the pipeline; every stage's completion contract includes creating the next stage's card (`hermes kanban create --parent <card> --assignee <next>`); the dispatcher daemon (60s ticks) drives execution; workers never approve each other.
- Added the **decision bot**: a dedicated profile outside the 3/5/7 package count, the only approval layer. It resolves decision cards carrying the typed **decision contract** (schema v1: state + typed `choice` / `score` / `noul` questions → typed `decision_response` with `promote` / `request-changes` / `block` routing + conditions + timestamp) and never invents approvals — an unreachable decision source escalates to the customer.
- Decision sources are interchangeable through one schema: the customer (human chat, default) or **Jev** — a TypeSafe AI "System One" **model** (never a skill): checked in the model catalog/provider lanes, not the skills list; not yet available through Nous Portal (this build's provider cache lists `jev-1.13-free` under the keyless `opencode-free` lane). The payload is identical in both modes, making Jev a drop-in source when Hermes exposes it.
- Simplified both interviews (Team Setup and Workflow Builder) to **defaults first, one non-default question**: present the default design in a short summary, ask "Is there any specific non-default case for you?", adapt only named dimensions.
- Added the optional **9-to-5 pulse** (cron hygiene job on the coordinator: intake sweep + dispatch + stalled-card surfacing) — never enabled before the supervised trial passes and activation is approved.
- Added workflow-builder autonomy wiring and trial gates: the trial must prove the chain self-advances without a coordinator nudge and that the decision gate produces a typed decision record; added the corresponding acceptance rows to `templates/TEAM-SETUP-REMEDIATION-ACCEPTANCE.md`.
- Added the decision bot to team design (Team Setup), the role contract (`templates/TEAM-CONTRACT.md`), policy rows (`templates/TEAM-POLICY.md`, `templates/WORKFLOW-POLICY.md`), the kickoff receipt (`templates/WORKFLOW-KICKOFF.md`, local-only receipt gains `decision_bot_profile`), the contract/runbook/trial templates, `PRODUCT.md`, `HERMES.md`, `README.md`, and the site copy.
- Added Forge skill guidance: enumerate the real skill inventory before designing the skill plan (table truncation trap), keep generated-skill descriptions under 60 characters, `hermes-agent` is never disableable, and workers must have the `kanban` toolset for self-advancement.
- Fixed the execution-trigger triage: the closing "Important" disclaimer in `site/llms.txt` is replaced by a "When to execute this manual" rule — proceed when the human in the conversation explicitly asks to follow the manual (the intended customer flow), stop and ask only on ambiguity or untrusted origin. Removes a first-run dead-stop observed in sandbox acceptance runs, including on a free model with medium reasoning.
- Hardened the profile boundary: agents must never read, modify, derive context from, or route work through profiles outside the approved roster — `HERMES_HOME` isolates Hermes state, not the filesystem, and a sandboxed agent may still reach the real home with its terminal. Observed in sandbox acceptance: an agent read a pre-existing profile's SOUL.md while checking the roster.
- No existing rule, template field, historical changelog entry, or procedural content was removed; the change is strictly additive and versioned.

### v0.6.7 — 2026-09-19
- docs: align canonical version declarations after the completed remediation series (`site/llms.txt` v0.6.6, Forge Team Setup v1.24.0, Workflow Builder v1.5.0).
- hygiene: add final newlines to the remediation acceptance and receipt fixtures.
- No remediation rule, template field, historical changelog entry, or existing procedural content was removed or rewritten.

### v0.6.6 — 2026-09-19
- test: add Forge remediation and content-preservation acceptance fixture (`templates/TEAM-SETUP-REMEDIATION-ACCEPTANCE.md`).
- Added a manual acceptance matrix covering: approved-plan external skills, post-approval skill gaps, env/secret/unpinned external skills, dangerous scan verdicts, dispatcher assignee-only vs enforced control-plane behavior, generated-skill registry deltas, skills-count mismatch, runtime-read/CLI-unregistered config keys, unknown YAML keys, Forge-managed artifact tool policy, modified repository file preservation, and CHANGELOG append-only updates.
- Added the File Preservation Report template (pre/post SHAs, additions, deletions, deletion explanations) and its completion condition; a file rebuilt from partial, inferred, cached, or older content fails acceptance.

### v0.6.5 — 2026-09-19
- docs: enforce builtin file-tool use for Forge-managed artifacts (`site/llms.txt`, `skills/forge/SKILL.md`, `skills/workflow-builder/SKILL.md`, `templates/WORKFLOW-RUNBOOK.md`).
- Added the Forge-managed artifact tool policy: builtin file tools only for SOUL.md, generated SKILL.md files, TEAM.md, TEAM-CONTRACT.md, TEAM-POLICY.md, Workflow Builder draft artifacts, Kanban card-body source content, and receipt files; the Hermes CLI only for profile management, supported configuration operations, skill registry inspection, Kanban state operations, authentication operations, and smoke-test execution.
- Prohibited content manipulation of Forge-managed artifacts through `cat`, `head`, `tail`, `echo`, shell substitution, heredocs, `sed`, `awk`, `grep`, `rg`, `find`, Python direct-file operations, or temporary-file content transport; a missing builtin file tool stops the flow and records `SKIPPED` rather than falling back to shell or generic code.
- Added the Kanban body rule (card bodies composed as controlled literals or builtin file reads, included verbatim in the handoff receipt) and the required TOOL POLICY COMPLIANCE verification receipt.

### v0.6.4 — 2026-09-19
- fix: reconcile generated skills and runtime configuration receipts (`site/llms.txt`, `skills/forge/SKILL.md`, `templates/TEAM-POLICY.md`, `templates/TEAM-SETUP-RECEIPTS.md`).
- Added a generated-skill reconciliation rule: after any generated local skill is created or written, capture the pre-write receipt, reload/re-query the registry, run `hermes -p <profile> skills list --enabled-only`, verify the exact identifier appears once, verify the local and total count deltas, and record pre/post counts with expected vs actual delta; a mismatch marks Team Setup incomplete and stops the flow.
- A generated skill is considered installed only when the exact fresh inventory reconciles; creation-operation success alone is never a receipt. Added the required reconciliation receipt example.
- Added a configuration-key classification rule for every changed setting: Registry-supported (standard CLI write + `config get` receipt), Runtime-supported / CLI-unregistered (source/runtime evidence, `--force` only when approved, post-write effective-value receipt), Unsupported or stale (`SKIPPED` with the exact reason), and Existing non-schema key (never proof of active configuration).
- Applied the classification to the known registry-drift keys `agent.reasoning_effort`, `skills.disabled`, `delegation.fanout`, and `moa.enabled`; stale YAML keys are never evidence of runtime behavior.

### v0.6.3 — 2026-09-19
- fix: keep unenforceable workflow handoffs local and non-executable (`site/llms.txt`, `skills/forge/SKILL.md`, `skills/workflow-builder/SKILL.md`, `templates/WORKFLOW-KICKOFF.md`, `HERMES.md`, `PRODUCT.md`).
- Defined two distinct handoff concepts everywhere they appear: `handoff_state` (semantic, e.g. `READY_FOR_WORKFLOW_BUILDER`) and `board_state` (physical Kanban state, or `null`), plus `delivery_mode` (`LOCAL_RECORD` | `ENFORCED_CONTROL_PLANE_CARD`) and `dispatcher_enforcement` (`VERIFIED` | `UNSUPPORTED`).
- A Kanban kickoff card may be created only when the installed dispatcher enforces routing to the exact stable coordinator, no specialist spawn, no customer-work tool execution, and control-plane-only state transitions; native assignee and idempotency support alone are insufficient.
- When any enforcement requirement is unavailable, no Kanban kickoff card is created; one local-only handoff receipt is appended to `~/.hermes/TEAM.md` with `WORKFLOW HANDOFF: READY — LOCAL ONLY` and `DISPATCHER ENFORCEMENT: UNSUPPORTED`.
- Workflow Builder now accepts `LOCAL_RECORD` or `ENFORCED_CONTROL_PLANE_CARD`; the local record requires an explicit founder instruction before the workflow interview, and no general "unblock card" action authorizes discovery or execution.
- The generic `status: READY` metadata field is no longer used where it would conflict with the actual physical board state.

### v0.6.2 — 2026-09-18
- feat: require approval for unplanned external skill installs (forge skill v1.21.0; manual v0.6.2).
- Added an "Approved Skill Plan" requirement to the design/proposal before Team Setup approval. Each planned capability resolution now records target profile, capability gap, resolution type (builtin / generated / hub-external), exact identifier for any Hub/external skill, source/repository, expected or actual scan verdict, and approval state.
- Replaced the broad Hub rule with an explicit approval amendment gate: a Hub or external skill may be installed only when its exact identifier, target profile, capability gap, and scan verdict were included in the approved skill plan. New gaps after approval require a stop-before-installation step, an explicit skill-plan amendment approval, and a recorded amendment receipt before installation. Official origin does not itself authorize an installation.
- Explicit amendment approval is now required when a scan surfaces any meaningful finding (environment access, secret access, network credential access, shell/system command execution, unpinned dependency or package installation, or any dangerous verdict).
- Added a skill approval-policy table to `templates/TEAM-POLICY.md` and a verification receipt requirement that each Hub/external skill record includes exact identifier, source, target profile, capability gap, scan verdict and findings, approval or amendment receipt reference, and installed / skipped / rejected state.
- All existing content is preserved; the change is strictly additive and records scan findings and rollback/removal information.

### v0.6.1 — 2026-09-13
- docs: made builtin tool usage explicit in `site/llms.txt` and `skills/forge/SKILL.md` (forge skill v1.20.0; manual v0.6.1).
- Added a "Builtin tool usage" section to both files mapping each flow step to the Hermes builtin tools that implement it: `todo`, `read_file`, `write_file`, `patch`, `search_files`, `skills_list`, `skill_view`, `skill_manage`, `memory`, `session_search`, `clarify`, `delegate_task`, `execute_code`, and the `kanban` toolset.
- Grounded tool names in the official Built-in Tools Reference (https://hermes-agent.nousresearch.com/docs/reference/tools-reference) and added that link to the manual's Source files.
- Documented the SKIPPED-with-reason rule for unavailable tools (availability varies by platform, credentials, and enabled toolsets).
- No procedural content was changed or removed; the additions are strictly additive on top of the v0.6.0 two-stage content.

### v0.6.0 — 2026-09-13
- feat: split onboarding into two explicit phases: Team Setup and Workflow Builder
- docs: restore complete historical changelog entries (v0.3.0 through v0.5.6)
- Added explicit two-stage lifecycle with coordinator handoff receipt
- Added workflow-specific contracts, policies, runbooks, and trial plans
- Preserved team governance artifacts while separating workflow execution

## [2026-09-10] — v0.5.6: TEAM.md fixed home, changelog history restored, typo fix

### Added
- Standing maintenance policy at the top of CHANGELOG.md: update on every
  meaningful repository change with date, version/commit context, what
  changed, and why.

### Changed
- `site/llms.txt` — v0.5.5 (forge skill v1.12.0): changed the durable
  record destination to ~/.hermes/TEAM.md (fixed path under the HERMES
  home directory, never the shell CWD which could be Downloads, Desktop,
  or any unrelated project folder); added explicit hard rule "Never derive
  Forge's durable output path from the shell CWD"; removed stray word
  "class" before the main-profile config receipt command in Step 5; final
  report must state the full path ~/.hermes/TEAM.md.
- `skills/forge/SKILL.md` — v1.12.0: mirrored the durable-record location
  change to ~/.hermes/TEAM.md; added two new pitfalls ("Never write
  TEAM.md to the shell CWD" and "Never derive Forge's durable output path
  from the shell CWD").
- `CHANGELOG.md` — restored the full historical body for v0.3.0 through
  v0.5.1 exactly as provided; preserved all v0.5.2, v0.5.3, and v0.5.4
  entries unchanged.

### Why

The v0.5.4 flow wrote TEAM.md to the shell CWD, which could be Downloads,
Desktop, or any unrelated project directory — not a durable home under
HERMES install. The v0.5.5 fix moves the durable record to
~/.hermes/TEAM.md, a fixed path that survives CWD changes and is
co-located with the profiles and skills. The changelog history for v0.3.0
through v0.5.1 was incomplete in v0.5.4; this patch restores it exactly.
The stray word "class" before the main-profile config receipt command in
Step 5 was a typo introduced in v0.5.4.

## [2026-09-09] — v0.5.4: Profile 0 tuning, Kanban Desktop state, verbatim config receipts

### Added
- `site/llms.txt` — new Step 4-0a "Tune profile 0": the main profile is
  the team coordinator in every run. Back up the default SOUL.md, rewrite
  it as a schema-grounded coordinator (board ops, dispatch, receipts —
  never implementation), apply context hygiene to the main profile
  (compression enabled, threshold 0.50 official default, MOA off — one
  model per turn on the coordinator), fix delegation.fanout user_turn,
  set browser.use_real_profile per approved policy. Workers get the same
  treatment with inexpensive models. Rejected config keys are recorded in
  TEAM.md and skipped loudly.
- Kanban Desktop state: the dashboard Kanban tab is a bundled plugin, off
  by default — CLI board and Desktop view are two surfaces. The flow now
  records the plugin state in TEAM.md and the final report, includes the
  one-line enable instruction, and never blocks the handoff on the toggle.
- Receipts hardened: main-profile `hermes config get compression` and
  `moa.enabled` pasted verbatim; per-profile skills receipts must include
  the FULL table with the counts line (e.g. "2 hub-installed, 57 builtin,
  1 local — 60 enabled"); a rounded claim is an assertion, not a receipt.
- `skills/forge/SKILL.md` — v1.11.0: mirrors 4-0a, the Desktop plugin
  rule, and the counts-line receipt rule; six new pitfalls (never leave the
  default SOUL.md stock, never enable MOA on the coordinator, never claim
  a skills inventory without the counts line, never claim Kanban wired
  without the Desktop state, never let the coordinator implement,
  never silently skip a failed config key).

### Why

Run 9 post-mortem (DeepSeek v4 Flash): the flow ran end-to-end with
phase-exit receipts, but verification against the live machine found
three gaps the manual never covered. (1) The main profile was left stock —
generic "warm, playful" SOUL.md, MOA enabled with two reference models
plus a Pro aggregator, no compression block — the opposite of a cheap
orchestrator; the official Kanban cost guidance says coordinator strong /
workers cheap, and profile 0 was never tuned. (2) Kanban Desktop is a
plugin off by default — the run claimed "board wired" while the user had
to find and flip a Settings toggle manually; the docs treated CLI board
and Desktop tab as one surface. (3) The final report rounded the skills
inventory ("59 builtins + 1 generated") while the live table read "2
hub-installed, 57 builtin, 1 local" — verbatim tables were required for
profile list and skills list, but nothing demanded the counts line, and a
summary without the table slipped through. v0.5.4 makes profile 0 a
first-class provisioning step, splits the Kanban receipt into CLI board
vs Desktop plugin state, and closes the receipts gap.

## [2026-09-07] — v0.5.3: Generation-only skills engine

### Changed
- `site/llms.txt` — Step 4c is now generation-only: builtins verify →
  generative skills via skill_manage create for uncovered roles → Hub for
  genuine gaps only; the forge_library tier is retired; the skills engine
  generates capabilities on demand using the same persona-engine logic.
- `skills/forge/SKILL.md` — v1.10.0: mirrors the generation-only flow;
  new pitfall (never search the Hub for a capability an enabled builtin
  already provides — check the profile's skills list first).
- `catalog/skills.json` — forge_library tier removed; manifest is now
  search-term hints + vetted third-party packs only; policy updated to
  generation-only.
- `PRODUCT.md` — Skills Engine simplified to generation-only; success
  criteria updated; Run 5 success bar defined (flagship model, full
  autonomous run to board wiring).

### Why

Run 5 (v0.5.2 build, flagship model) validated the four-tier engine
end-to-end — but the forge_library tier (pre-authored role skills) added
repo complexity without changing run quality: the generative tier already
produced role-specific methodology grounded in the interview and schema.
Retiring the library simplifies the product: the skills engine's job is
now verifying builtin coverage and generating the rest — no separate
library to maintain, no category flags to discover, no tap to manage.

## [2026-09-07] — v0.5.2: Context hygiene (post-gate config tuning, per-profile settings, Kanban desktop note)

### Added
- `site/llms.txt` — new Step 4-0a "Tune profile 0": the main profile is
  the team coordinator in every run. Back up the default SOUL.md, rewrite
  it as a schema-grounded coordinator (board ops, dispatch, receipts —
  never implementation), apply context hygiene to the main profile
  (compression enabled, threshold 0.50 official default, MOA off — one
  model per turn on the coordinator), fix delegation.fanout user_turn,
  set browser.use_real_profile per approved policy. Workers get the same
  treatment with inexpensive models. Rejected config keys are recorded in
  TEAM.md and skipped loudly.
- Kanban Desktop state: the dashboard Kanban tab is a bundled plugin, off
  by default — CLI board and Desktop view are two surfaces. The flow now
  records the plugin state in TEAM.md and the final report, includes the
  one-line enable instruction, and never blocks the handoff on the toggle.
- Receipts hardened: main-profile `hermes config get compression` and
  `moa.enabled` pasted verbatim; per-profile skills receipts must include
  the FULL table with the counts line (e.g. "2 hub-installed, 57 builtin,
  1 local — 60 enabled"); a rounded claim is an assertion, not a receipt.
- `skills/forge/SKILL.md` — v1.9.0: mirrors 4-0a, the Desktop plugin
  rule, and the counts-line receipt rule; six new pitfalls (never leave the
  default SOUL.md stock, never enable MOA on the coordinator, never claim
  a skills inventory without the counts line, never claim Kanban wired
  without the Desktop state, never let the coordinator implement,
  never silently skip a failed config key).

### Why

Run 9 post-mortem (DeepSeek v4 Flash): the flow ran end-to-end with
phase-exit receipts, but verification against the live machine found
three gaps the manual never covered. (1) The main profile was left stock —
generic "warm, playful" SOUL.md, MOA enabled with two reference models
plus a Pro aggregator, no compression block — the opposite of a cheap
orchestrator; the official Kanban cost guidance says coordinator strong /
workers cheap, and profile 0 was never tuned. (2) Kanban Desktop is a
plugin off by default — the run claimed "board wired" while the user had
to find and flip a Settings toggle manually; the docs treated CLI board
and Desktop tab as one surface. (3) The final report rounded the skills
inventory ("59 builtins + 1 generated") while the live table read "2
hub-installed, 57 builtin, 1 local" — verbatim tables were required for
profile list and skills list, but nothing demanded the counts line, and a
summary without the table slipped through. v0.5.2 makes profile 0 a
first-class provisioning step, splits the Kanban receipt into CLI board
vs Desktop plugin state, and closes the receipts gap.

## [2026-09-07] — v0.5.1: Self-verifying runs — version stamp, skill handshake, phase-exit receipts

### Added
- `site/llms.txt` — Version line at the top; the agent states the version
  in its first reply, proving which manual a run followed. Version
  handshake for the forge skill: a locally installed skill must match the
  version this manual names, or it is re-fetched from the repo; on any
  conflict the manual wins. Package rule hardened: exactly 3, 5, or 7
  specialists — never 4 or 6. Phase-exit receipts: after 4b paste the
  SOUL.md files written, after 4c paste one profile's skills list — a
  stalled run is auditable at its failure point, not only in a final
  report that never arrives.
- `skills/forge/SKILL.md` — v1.8.0: mirrors the handshake and phase-exit
  receipts; two new pitfalls (never trust a local skill of unknown
  version; never propose 4 or 6 specialists).
- `PRODUCT.md` — Runs 5–8 recorded in the Test Log; model-class note
  (small local models follow the flow but risk mid-run collapse — Run 8);
  Run 9 success bar defined (flagship model, full autonomous run to board
  wiring).

### Why

Run 7 was hijacked by a pre-v0.3 local forge skill left in ~/.hermes/skills
from an earlier session — nothing in the flow detected version skew, and
the run executed a dead flow while the manual said "TRUST IT". Run 8
(clean install) validated the flow itself — interview, Package 7, the
exact gate question, batched provisioning, a schema-grounded persona with
quoted answers — but the model degenerated mid-4b (channel-token loops,
72.7s stall, off-task drift), and nothing after the first persona had a
receipt. v0.5.1 makes runs self-verifying: the version is quotable, the
skill's age is checkable, and every phase transition leaves evidence
even if the run dies.

## [2026-09-06] — v0.5.0: Kanban team-wiring — the board is the work engine

### Added
- `site/llms.txt` — new Step 6 "Wire the team onto a board": gateway
  check/start, `hermes kanban init`, optional named board per project,
  first-card seeding with `hermes kanban create` (approved assignee names,
  decision-stamped card bodies for fan-out, goal-mode cards with explicit
  acceptance criteria, per-card `--skill`/`--model` pins, cost-strategy
  note), the review loop via `kanban_request_review` /
  `kanban_request_changes`, kanban receipts (`hermes kanban list`,
  `hermes kanban stats`) in the final report, board name + card IDs in
  TEAM.md, and the dashboard/watch handoff.
- New failure path: gateway cannot start → create cards anyway; they
  dispatch on the next gateway tick; never block the handoff on the board.
- `skills/forge/SKILL.md` — v1.7.0: mirrors the board wiring; three new
  pitfalls (never assign cards to non-roster names, never let the
  coordinator implement, never write vague goal bodies); Kanban docs link
  in References.

### Changed
- `site/llms.txt` — Step 3 approval-gate bullet now states the board
  wiring happens after approval: the single yes covers team, personas,
  skills, browser mode, and the board.

### Why

Runs 1–5 converged on the same gap: Forge provisions a team, but the
collaboration handoff stopped at group rooms and a cron digest. The
official Kanban system is the platform's native work engine — a durable
board, a dispatcher that spawns each assignee as its own worker process,
review states, and goal-mode looping — and it was never wired in. v0.5
closes the loop between the team Forge provisions and the engine HERMES
already ships: after handoff, work runs on the board, not in prompts.

### Impact on user flow

Customers now get a working team, not a roster: cards are on the board,
the dispatcher is running, the QA-review loop and "iterate until done"
are native kanban states, and progress is observable in `hermes kanban
watch` or the dashboard.

## [2026-09-05] — v0.4.0: The Forge skills library + four-tier skills engine

### Added
- `skills/library/` — 8 custom skills authored for Forge team roles:
  prd-author, blueprint, mvp-builder, qa-gate, ship-it, source-dig,
  feed-craft, team-ops. Official SKILL.md format (When to Use / Procedure /
  Pitfalls / Verification), MIT, installable onto any profile via direct
  URL with automatic security scanning.
- `skills.sh.json` — repo-root groupings file: the repo can be added as a
  skills tap (`hermes skills tap add juliench82/hermes-agents-forge`).

### Changed
- `site/llms.txt` — Step 4c is now a four-tier engine: builtins verify →
  Forge library install (direct URL + `--category`) → generative skills
  via skill_manage create for uncovered roles → Hub for genuine gaps.
  Security gate now rides Hermes's built-in install scanner (quarantine →
  scan → verdict → confirm); never --force past a verdict.
- `skills/forge/SKILL.md` — v1.5.0: mirrors the four tiers; new pitfall
  (never --force past a security verdict); SkillSpector-specific gate
  retired in favor of the built-in scanner (SkillEvaluator remains an
  optional advisory layer).
- `catalog/skills.json` — new forge_skills map (role → skill → category),
  forge_library + generative policies, security_gate updated.
- `PRODUCT.md` — Skills Engine rebuilt as four tiers; success criteria
  updated; Run 5 success bar defined.

### Why

Run 4 showed 0 hub installs landed; and relying on builtins alone would
make every Forge team identical to what any user gets from plain
`hermes profile create`. The Forge library gives every profile
role-specific methodology we author, version, and security-scan — the
product's differentiation. The generative tier covers roles we never
imagined: the persona engine's logic applied to capabilities. Mechanism
verified end-to-end on a real profile (direct-URL install → quarantine →
scan → SAFE verdict → confirm → per-profile install path, including
`--category` flag discovery).

## [2026-09-03] — v0.3.5: Builtins-first skills engine

### Changed
- `site/llms.txt` — Step 4c is now "Cover real skills": start with
  `hermes -p <name> skills list`; a builtin that covers the role's need
  satisfies it — Hub searches are for genuine gaps only, and installing a
  duplicate of an enabled builtin is forbidden. 4b persona grounding now
  includes builtin skill knowledge.
- `skills/forge/SKILL.md` — v1.4.0: same rule in 4c; new pitfall — never
  search the Hub for a capability an enabled builtin already provides.
- `catalog/skills.json` — policy gains `builtin_first`; closing rule updated
  to check enabled builtins before runtime Hub searches.
- `PRODUCT.md` — Skills Engine and success criteria updated to
  builtins-first; Run 4 recorded in the Test Log; interrupt-recovery
  success criterion checked.

### Why

Run 4 receipts: all 7 profiles show `0 hub-installed, 57 builtin` — every
Hub install attempt failed (GitHub API rate limits, largely burned on
skills duplicating builtins), yet the final report claimed verified skill
installation. Meanwhile the builtin library (test-driven-development,
systematic-debugging, github, codebase-inspection, computer-use,
google-workspace…) already covers most of the manifest's domains. The
skills engine's real job is verifying builtin coverage and filling genuine
gaps — not performing redundant installs.

## [2026-09-03] — v0.3.4: Verbatim receipts + honest final reports

### Changed
- `site/llms.txt` — Step 5 now requires the final report to paste verbatim
  command output (`hermes profile list`, per-profile `skills list`);
  asserting "verified" without output is not verification. The report must
  match the checklist — every item checked, or listed as skipped with a
  reason (not found, rate limit, failed scan). Never declare the team
  "complete" while an item is unchecked. New failure path: rate-limited or
  transiently failed skill installs are marked skipped and reported.
- `skills/forge/SKILL.md` — v1.3.0: same two rules added to Verification;
  two new pitfalls (no done-without-receipts, no
  complete-with-unchecked-items).

### Why

Run 4 (12B local model, v0.3.0 build) recovered cleanly from a
mid-provisioning model collapse via the resume rule — but its final report
declared "the technical setup is complete" while its own checklist showed
two skill installations unchecked (GitHub API rate limits), and it asserted
verification results without showing any command output. Assertions are
not receipts.

## [2026-09-02] — v0.3.3: HERMES.md aligned with the v0.3 flow

### Changed
- `HERMES.md` rewritten for the current product: single approval gate,
  persona engine (10-section SOUL.md schema), skills engine (search →
  inspect → install, SkillSpector-gated), receipts verification, and Bot
  Mode rituals (group rooms, message_agent, routines).
- Browser-mode contradiction fixed: real-browser is the unasked default,
  isolated only on explicit opt-out. The old text had the skill asking the
  user first — contradicting llms.txt hard rule 5.
- Primitive mapping table kept and extended with a team-collaboration row.

## [2026-09-01] — v0.3.2: v0.1 architecture purge

### Removed
- `compiler/` (14 files), `runtime/` (32), `onboarding/` (18), `shared/` (13),
  `schemas/` (7), `scripts/` (6), `examples/` (1) — the complete v0.1
  TenantSpec system: team compiler, provisioning engine, policy contracts,
  artifact schemas, and the installer (which violated the current hard rule
  "never ask the user to install anything").
- `catalog/` v0.1 primitives: `connectors/`, `memory/`, `policies/`,
  `triggers/`, `roles/executor/`, `roles/supervisor/`, `README.md`, `index.json`
  (the versioned-primitive index the dead compiler resolved against).
- `pyproject.toml` — packaged only the purged folders; the product is no
  longer Python software.
- `bootstrap.manifest.json` — the v0.1 machine-readable entrypoint.

### Added
- `LICENSE` (MIT) — restored from history (c46f1e4).

### Why

The v0.2 rewrite moved all logic into agent-followed markdown
(llms.txt + SKILL.md). The Python system was referenced by nothing in the
live flow, and dead architecture sitting next to the live manual risked
weak models following the wrong path. The repo now contains exactly the
load-bearing files: HERMES.md, PRODUCT.md, README.md, site/,
skills/forge/SKILL.md, catalog/roles/soul-schema.md + examples,
catalog/skills.json.

### Recovery points (git history)
- v0.1 catalog primitives + TenantSpec validator: fb0bb09
- compiler (planner, catalog, CLI): a7c643d
- hygiene files (LICENSE, Dockerfile, tests, pyproject): c46f1e4

## [2026-09-01] — v0.3.1: Bot Mode alignment + new README

### Added
- `README.md` — customer-facing introduction: what the Forge does, what
  you get, team sizes, trust & safety. No jargon.
- Bot Mode mechanics across the flow: group chats (2–6 Bots per room; a
  7-member team gets two rooms), @mentions, `message_agent` DMs, routines
  via `hermes cron`, shared credential pool by default.

### Changed
- `site/llms.txt` — Step 4a now instructs careful `--description` writing
  (Bot Mode injects title + description into every teammate's roster);
  Step 5 rituals now set up the real collaboration layer instead of just
  proposing it.
- `catalog/roles/soul-schema.md` — Collaboration Protocol section now
  names the reach mechanics (@mentions, `message_agent` DMs) and the
  roster-visible description.
- `skills/forge/SKILL.md` — v1.2.0, mirrors the same; new pitfall on the
  `--description` line.

### Why

Hermes v2026.8.31 turned Bot Mode into the platform's native multi-agent
layer: profiles are Bots with built-in bot-to-bot messaging, group rooms,
and routines, sharing the main profile's credential pool by default. The
Forge's funnel maps 1:1 onto those primitives — this patch makes the
handoff create the real collaboration layer, not just suggest one.

## [2026-09-01] — v0.3.0: The Supercharged Forge (persona engine + skills engine)

### Added
- `catalog/roles/soul-schema.md` — universal 10-section SOUL.md schema with
  grounding sources and depth rules; role-agnostic by design.
- `catalog/roles/examples/` — golden-sample personas (system-architect,
  social-media-manager) to calibrate depth, not to limit coverage.
- `catalog/skills.json` — skills manifest: per-domain search terms, vetted
  third-party packs (superpowers), and the SkillSpector security-gate policy.
- Single approval gate: one yes authorizes profiles + personas + skills;
  zero mid-flow confirmations afterwards.
- Receipts verification: `hermes profile list` count, per-profile skill
  inventory, per-profile chat smoke test, durable TEAM.md record.
- Team rituals in handoff: group chat, shared inbox, kickoff routine (Bot Mode).

### Changed
- `site/llms.txt` — Step 4 split into 4a profiles (batched) / 4b persona
  engine (schema-driven, grounded in interview quotes + skill knowledge) /
  4c skills engine (search → inspect → install, SkillSpector-gated).
- `skills/forge/SKILL.md` — v1.1.0, mirrors the same protocol; pitfalls
  updated (no thin personas, no invented names, no unscanned installs,
  no broken approval gate).
- `PRODUCT.md` — success criteria raised to the new bar; test log added.

### Why

Post-test review (runs 1–3) showed the product provisioned thin personas
(3-line SOUL.md) and installed no skills — quality lived in the model's
imagination instead of in the repo. The persona engine moves depth into
a universal schema + grounding sources; the skills engine moves
capability into the HERMES Skills Hub with a real security gate; the
single approval gate removes confirmation fatigue.

### Impact on user flow

Customers now get: one approval → a team of isolated profiles, each with a
rich, grounded persona and real installed skills, verified with receipts
and handed off with collaboration rituals — on any LLM, any reasoning
level, for any role they ask for.
