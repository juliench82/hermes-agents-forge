# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `PRODUCT.md` — product goal, current state, gaps, and next steps (customer journey: webpage → llms.txt → interview → bot-mode profiles → workflows)

### Changed
- `site/llms.txt` synced with post-PR-69 onboarding flow (added `hermes skills trust` step, updated referenced files)
- `README.md` rewritten to align with PR-#69 bootstrap/compiler model
- `BOOTSTRAP.md` rewritten as bootstrap manifest specification

### Planned (see PRODUCT.md)
- Rewrite `site/llms.txt` to be the product (interview → design → provision flow)
- Update `HERMES.md` to match (remove compiler-only flow as primary entry)
- Update `skills/forge/SKILL.md` to implement the interview and profile creation
- Inventory `runtime/` and delete leftovers (Buzz, Obsidian, duplicate audit, unused installer paths)
- Prove the funnel once (site button → `/llms.txt` → clone/trust → interview → N isolated profiles in bot mode → one sample workflow)

## [Unreleased] — PR #69 and cleanup

### Added
- `LICENSE` (MIT), `.gitignore`, `pyproject.toml` for proper Python packaging
- `AGENTS.md` for cross-tool agent instructions
- `CONTRIBUTING.md` and `CHANGELOG.md` for contributor guidance
- `Dockerfile` for isolated runtime testing
- `site/public/.well-known/skills/index.json` for skill discovery

### Changed
- `catalog/connectors/` primitives aligned with Hermes MCP server definitions
- `catalog/triggers/cron/` aligned with native `cronjob` tool
- `shared/safety-*.md` docs reference Hermes 8-layer security model
- `onboarding/` docs include `hermes skills trust` and `hermes setup --portal` steps
- `HERMES.md` updated with skills trust guidance
- `site/llms.txt` synced with post-PR-69 onboarding flow (added `hermes skills trust` step, updated referenced files to `HERMES.md`/`AGENTS.md`/`skills/forge/SKILL.md`/`bootstrap.manifest.json`)
- `README.md` rewritten to align with PR-#69 bootstrap/compiler model (Quick Start, Key Docs table, Architecture diagram, Conventions)

### Removed
- `site/index_new.html`, `site/script_new.js`, `site/styles_new.css` (stale website redesign duplicates)
- `site/public/SKILL.md`, `site/public/install.sh`, `site/public/start.md`, `site/public/llms.txt` (orphaned duplicates; discovery now points to GitHub or `site/llms.txt`)
- `site/README.md` (orphaned)
- `onboarding-loop.yaml`, `team-designer.yaml` (orphaned repository-root skills; superseded by `skills/forge/SKILL.md` and compiler/bootstrap flow)

### Fixed
- `site/public/install.sh` synced with root `install.sh` (before removal)
- `site/public/llms.txt` synced with `site/llms.txt` (before removal)

## [0.1.0] — 2026-08-22

### Added
- Initial release of Hermes Agents Forge
- Bootstrap manifest system for multi-profile team provisioning
- Compiler for discovering and activating bootstrap manifests
- Runtime for profile provisioning, skill resolution, and policy enforcement
- Catalog of versioned primitives (roles, connectors, triggers, memory, policies)
- Onboarding system with templates, workflows, and fixtures
- Skills/forge SKILL.md for agent capabilities
- Website with llms.txt for LLM discoverability
- CI/CD workflows for validation
- Comprehensive test suite (43 test files)

[Unreleased]: https://github.com/juliench82/hermes-agents-forge/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/juliench82/hermes-agents-forge/releases/tag/v0.1.0
