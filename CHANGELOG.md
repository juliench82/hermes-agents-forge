## [Unreleased]

### Changed

- **site/llms.txt**: Replaced compiler-only instructions with the full interview → design → provision flow. Added explicit 5-question interview script, team design table, and dual provisioning paths (Python runtime + Hermes CLI fallback).
- **HERMES.md**: Rewrote to describe the conversational onboarding funnel (interview, team design, profile provisioning). Added explicit interview questions and Hermes CLI fallback path for agents without Python.
- **skills/forge/SKILL.md**: Updated to define the Forge skill as the trusted onboarding entry point. Added explicit interview questions, team design table format, and Hermes CLI provisioning commands.

### Added

- Clear product contract: any HERMES agent (any LLM, any thinking level) can point to `/llms.txt`, trust the Forge skill, and get a custom team of isolated profiles plus a sample workflow.
- Dual provisioning paths: Python runtime (`python -m runtime.onboarding_wizard`) for full automation, Hermes CLI (`hermes profile create`) for agents without Python.
- Support for `python -m runtime.onboarding_wizard --refine` to iteratively adjust teams after initial provisioning.
- Explicit 5-question interview script in llms.txt, HERMES.md, and SKILL.md.

### Removed

- Deleted legacy runtime modules: `buzz_integration.py`, `buzz_setup.py`, `obsidian_integration.py`, `obsidian_setup.py` (Buzz/Obsidian leftovers).
- Deleted duplicate audit modules: `audit_log.py`, `audit_logger.py`.
- Deleted unused installer paths: `installer_entrypoint.py`, `installation_runner.py`, `adaptive_installer.py`, `installation_state.py`, `installation_store.py`.
- Deprecated `compiler/` as the user-facing entry point; it is now a backend utility for manifest generation.

### Fixed

- Resolved contradiction between "do not create profiles/" and the product goal of creating isolated bot-mode profiles. Profiles under `profiles/` are now explicitly managed by the onboarding wizard or Hermes CLI.
- Fixed typo in HERMES.md ("avatar/metdata" → "avatar/metadata").
- Corrected CHANGELOG entry that claimed runtime cleanup was done; now reflects actual file deletions.

## 0.2.0 - 2026-08-20

### Added

- Initial release of the Forge skill system
- Compiler-based team provisioning
- Basic profile isolation

### Changed

- Updated documentation for v0.2.0 release