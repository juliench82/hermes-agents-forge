# Changelog

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
- Removed all "Forge library" references from site/llms.txt, skills/forge/SKILL.md, PRODUCT.md; skills engine is now builtins → generate → Hub only; no pre-authored skills stored in the repo.
- catalog/skills.json: removed forge_library tier and forge_skills map; manifest now three tiers (builtins, generative, hub).
- Restored skills/forge/SKILL.md to full v1.10.0 content (frontmatter + Procedure/Pitfalls/Verification) after incomplete v0.5.3 push (db7dffa) that only updated llms.txt.
- Restored PRODUCT.md to full v0.5.3 content (Core Flow, persona/skills engine, Experience Requirements, Success Criteria, Test Log).

## [2026-09-07] — v0.5.2: Context hygiene

### Changed
- Adds post-gate context-hygiene configuration, per-profile settings, and Kanban Desktop activation guidance.
