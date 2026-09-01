# Changelog

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
