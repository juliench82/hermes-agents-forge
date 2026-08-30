# Changelog

## [2026-08-30] — HERMES Alignment Update

### Changes
- Updated site/llms.txt to clarify this is a HERMES skill pack, not core HERMES
- Added disclaimer to HERMES.md noting forge extensions beyond core HERMES
- Updated skills/forge/SKILL.md with usage instructions for HERMES CLI
- Added runtime/README.md section on HERMES integration options (MCP or direct API)
- Updated PRODUCT.md with architecture notes clarifying runtime extensions

### Why
- Product goal described interview → team → provision flow not supported by core HERMES
- Users following "point HERMES agent to llms.txt" would not trigger intended flow
- Needed to align docs with what HERMES actually supports vs our extensions

### Impact on User Flow
- Users now install HERMES first, then opt-in to forge skill
- `/forge` command in HERMES CLI starts team design workflow
- Runtime modules provision profiles via MCP or direct Python API
- "Use My Real Browser Profile" remains default option in onboarding wizard

---

