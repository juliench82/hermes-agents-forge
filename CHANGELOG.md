# Changelog

## [2026-09-07] — v0.5.3: Generation-only skills engine

### Changed
- Removed all "Forge library" references from site/llms.txt, skills/forge/SKILL.md, PRODUCT.md; skills engine is now builtins → generate → Hub only; no pre-authored skills stored in the repo.
- catalog/skills.json: removed forge_library tier and forge_skills map; manifest now three tiers (builtins, generative, hub).
- Restored skills/forge/SKILL.md to full v1.10.0 content (frontmatter + Procedure/Pitfalls/Verification) after incomplete v0.5.3 push (db7dffa) that only updated llms.txt.
- Restored PRODUCT.md to full v0.5.3 content (Core Flow, persona/skills engine, Experience Requirements, Success Criteria, Test Log).

## [2026-09-07] — v0.5.2: Context hygiene

### Changed
- Adds post-gate context-hygiene configuration, per-profile settings, and Kanban Desktop activation guidance.
