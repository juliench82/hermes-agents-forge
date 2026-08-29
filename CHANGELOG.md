# Changelog

All notable changes to Hermes-Agents-Forge are documented in this file.

## [2026-08-29] — Alignment with Official HERMES Documentation

### Changed
- **skills/forge/SKILL.md**: Converted to valid HERMES skill format with YAML frontmatter (`name:`, `description:`, `version:`), standard sections (`When to Use`, `Procedure`, `Verification`, `Pitfalls`), and progressive disclosure pattern
- **site/llms.txt**: Restructured as LLM-readable index with explicit instructions for any HERMES agent to load and execute the `/forge` skill
- **HERMES.md**: Added mapping table between Forge concepts and official HERMES primitives (profiles, Bot Mode, SOUL.md, skills)
- **PRODUCT.md**: Added "Implementation Mapping" section linking product goals to HERMES CLI commands
- **runtime/profile_provisioner.py**: Updated profile provisioning to use official `hermes profile create` CLI instead of direct filesystem manipulation

### Added
- Explicit "Use My Real Browser Profile" interview question in skill Procedure (default option)
- References to official HERMES docs throughout (Bot Mode, Profiles, Skills, SOUL.md)
- Verification steps in skill (`hermes profile list`, `hermes -p <name> chat`, Bot Mode roster check)
- `list_profiles()` and `verify_profile()` helper functions in profile_provisioner.py

### Fixed
- SKILL.md now recognized by HERMES agents as valid skill (appears in `skills_list()`)
- User flow now executable by any HERMES agent via `/forge` skill
- Profile provisioning now compatible with standard HERMES installations (no custom APIs)

### Why These Changes Were Needed
- Original SKILL.md lacked YAML frontmatter — HERMES agents couldn't recognize it
- Bot Mode was described as a programmatic API, but it's officially a desktop UI feature over profiles
- "Use My Real Browser Profile" was underspecified — now documented as a user preference interview question
- site/llms.txt was not structured for LLM consumption — now follows llms.txt convention

### Impact on User Flow
- Users can now point **any** HERMES agent to `https://hermes-agents-forge.vercel.app/llms.txt`
- The agent will recognize `/forge` as a valid skill and execute the interview → design → confirm → provision flow
- All provisioning uses official HERMES CLI — works with standard installations
- "Use My Real Browser Profile" is now the explicit default, asked before provisioning

## [Previous versions]

See git history for earlier changes.
