## Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-08-29

### Added
- **User interview flow** in `site/llms.txt` — HERMES agents now interview users about workflow needs, team size, and profile preference before provisioning
- **Team design → confirmation → provisioning workflow** — Explicit 4-step process aligned with HERMES security best practices (command approval before side-effecting actions)
- **"Use My Real Browser Profile" default** — Main profile is now the default option; isolated bot-mode profiles are created only if user explicitly opts in
- **Bot Mode integration** — Profiles follow HERMES Bot Mode (beta) isolation model: each profile gets its own config, memory, credentials, and chat history; bots communicate through shared inbox

### Changed
- **`site/llms.txt`** — Updated from static documentation index to interactive workflow driver with interview questions, team proposal format, and confirmation step
- **`HERMES.md`** — Added explicit alignment with official HERMES Bot Mode documentation, emphasizing profile isolation and default behavior
- **`skills/forge/SKILL.md`** — Added step-by-step procedure for interview → team → confirm → provision flow, with explicit confirmation requirement
- **`runtime/profile_provisioner.py`** — Added `use_main_profile` parameter to support default "Use My Real Browser Profile" behavior; improved isolation for bot-mode profiles
- **`runtime/confirmation.py`** — Enhanced to present team proposal with clear default option and explicit approval prompt

### Fixed
- **Misalignment with official HERMES docs** — Flow now matches HERMES Bot Mode (beta) specs and security best practices
- **Missing confirmation step** — User must now explicitly approve team proposal before profiles are provisioned
- **Unclear default behavior** — "Use My Real Browser Profile" is now clearly presented as the default option

### Security
- **Command approval** — Follows HERMES security model: user must approve before any profile provisioning (side-effecting action)
- **Profile isolation** — Bot-mode profiles are isolated at the directory level (config, memory, credentials, sessions), though all bots share the host OS user and filesystem permissions

### Testing
- **Manual test:** Point a HERMES agent to `https://hermes-agents-forge.vercel.app/llms.txt` and verify:
  1. Agent interviews the user
  2. Agent proposes a team
  3. Agent presents "Use My Real Browser Profile" as default
  4. Agent waits for explicit confirmation before provisioning
  5. Profiles are created (or main profile configured) as expected

## [0.1.0] - 2026-08-04

### Added
- Initial release of HERMES-Agents-Forge
- Bootstrap repository structure for multi-agent team provisioning
- Basic profile isolation and runtime components
