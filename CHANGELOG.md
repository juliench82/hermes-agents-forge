## [Unreleased]

### Changed

- **site/llms.txt**: Replaced compiler-only instructions with the full interview → design → provision flow. Added explicit 5-question interview script, team design table, dual provisioning paths (Python runtime + Hermes CLI fallback), and native HERMES collaboration wiring (group chats, `message_agent`, Routines via `hermes cron`, Kanban via `hermes kanban init`).
- **HERMES.md**: Rewrote to describe the conversational onboarding funnel (interview, team design, profile provisioning, collaboration wiring). Added explicit interview questions, Hermes CLI fallback path, browser-based authentication (no API keys needed), and native HERMES collaboration primitives.
- **skills/forge/SKILL.md**: Updated to define the Forge skill as the trusted onboarding entry point. Added explicit interview questions, team design table format, Hermes CLI provisioning commands (`hermes profile create --clone`, `hermes cron add`, `hermes kanban init`), and collaboration wiring section.

### Added

- Clear product contract: any HERMES agent (any LLM, any thinking level) can point to `/llms.txt`, trust the Forge skill, and get a custom team of isolated profiles plus a sample workflow.
- Dual provisioning paths: Python runtime (`python -m runtime.onboarding_wizard`) for full automation, Hermes CLI (`hermes profile create`) for agents without Python.
- `hermes profile create --clone` option to inherit credentials and config from the main profile.
- Browser-based authentication: with `browser.backend: browser-use`, profiles authenticate via the user's existing browser logins — no API keys needed.
- Native HERMES collaboration primitives: group chats with `@mentions`, `message_agent` for direct handoffs, Routines via `hermes cron`, Kanban via `hermes kanban init` for high-autonomy teams.
- Support for `python -m runtime.onboarding_wizard --refine` to iteratively adjust teams after initial provisioning.
- Explicit 5-question interview script in llms.txt, HERMES.md, and SKILL.md.

### Removed

- Deleted legacy runtime modules: `buzz_integration.py`, `buzz_setup.py`, `obsidian_integration.py`, `obsidian_setup.py` (Buzz/Obsidian leftovers).
- Deleted duplicate audit modules: `audit_log.py`, `audit_logger.py`.
- Deleted unused installer paths: `installer_entrypoint.py`, `installation_runner.py`, `adaptive_installer.py`, `installation_state.py`, `installation_store.py`.
- Deprecated `compiler/` as the user-facing entry point; it is now a backend utility for manifest generation.

### Fixed

- Resolved contradiction between "do not create profiles/" and the product goal of creating isolated agent profiles. Profiles under `profiles/` are now explicitly managed by the onboarding wizard or Hermes CLI.
- Aligned terminology with official HERMES docs: "bot-mode profiles" → "isolated agent profiles (Bots)" throughout. A Bot is a Hermes profile with its own config, memory, skills, and credentials.
- Replaced vague "workflow hooks (triggers, queues, channels)" with actual HERMES primitives: Routines (`hermes cron`), group chats, `message_agent`, and Kanban.
- Fixed typo in HERMES.md ("avatar/metdata" → "avatar/metadata").
- Corrected CHANGELOG entry that claimed runtime cleanup was done; now reflects actual file deletions.

## 0.2.0 - 2026-08-20

### Added

- Initial release of the Forge skill system
- Compiler-based team provisioning
- Basic profile isolation

### Changed

- Updated documentation for v0.2.0 release