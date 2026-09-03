# Changelog

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

---
