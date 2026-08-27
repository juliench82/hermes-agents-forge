## [Unreleased]

### Changed

- **site/llms.txt**: Replaced compiler-only instructions with the full interview → design → provision flow. Users now run `python -m runtime.onboarding_wizard` instead of `python -m compiler --manifest ...`.
- **HERMES.md**: Rewrote to describe the conversational onboarding funnel (interview, team design, profile provisioning) instead of a static manifest-based flow.
- **skills/forge/SKILL.md**: Updated to define the Forge skill as the trusted onboarding entry point, with explicit permissions to interview users, propose teams, and provision isolated bot-mode profiles.

### Added

- Clear product contract: any HERMES agent can point to `/llms.txt`, trust the Forge skill, and get a custom team of isolated profiles plus a sample workflow.
- Support for `python -m runtime.onboarding_wizard --refine` to iteratively adjust teams after initial provisioning.

### Removed / Deprecated

- Deprecated `compiler/` as the user-facing entry point; it is now a backend utility for manifest generation.
- Marked legacy runtime modules (Buzz, Obsidian, duplicate audit, unused installer paths) for quarantine/deletion in a follow-up PR.

### Fixed

- Resolved contradiction between "do not create profiles/" and the product goal of creating isolated bot-mode profiles. Profiles under `profiles/` are now explicitly managed by the onboarding wizard.

## 0.2.0 - 2026-08-20

### Added

- Initial release of the Forge skill system
- Compiler-based team provisioning
- Basic profile isolation

### Changed

- Updated documentation for v0.2.0 release