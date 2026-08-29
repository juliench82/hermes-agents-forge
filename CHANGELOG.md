# HERMES-Forge Changelog

## [2026-08-28] - Initial Forge Skill

### Added
- `skills/forge/SKILL.md` for multi-agent team provisioning
- `runtime/` directory with profile creation and configuration modules
- `site/llms.txt` as the primary product surface
- `HERMES.md` for core HERMES setup documentation

### Changed
- Initial repository structure from bootstrap template

## [2026-08-29] - HERMES Alignment Update

### Added
- `site/llms.txt` now drives the full 3-phase interview → team → provisioning flow
- `skills/forge/SKILL.md` with executable provisioning procedure including Bot Mode protocol injection
- `runtime/config_generator.py` now sets `agent.bot_mode_protocol: true` and `browser.use_real_profile: true` by default
- `runtime/onboarding_wizard.py` collects model preferences per bot during interview
- Teammate roster injection into each Bot Chat system prompt

### Changed
- Provisioned profiles now default to `browser.use_real_profile: true` (users get their logged-in browser sessions)
- All bots get `agent.bot_mode_protocol: true` for teammate messaging via `@mentions`
- Skills are scoped per bot role (researcher/coder/reviewer)
- User confirmation required before provisioning with explicit team proposal

### Fixed
- Bot Mode protocol now injected into provisioned Bot Chat sessions
- Profile isolation boundaries enforced (separate `.env`, `config.yaml`, memory per profile)
- Model pinning per bot supported during interview

### Security Notes
- Real browser profile means agent acts with your logins — only enable for trusted workflows
- Each bot runs in isolated profile (`~/.hermes/profiles/<name>/`)
- Bot-to-bot messaging uses `message_agent` tool, available only in canonical Bot Chat sessions

### Post-PR #74 Changes
- Integrated PR #74 changes into alignment flow
- Ensured llms.txt is the single source of truth for the product flow
