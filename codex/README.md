# Codex Skill Bootstrap System

> Agent-directed onboarding for autonomous Codex skill teams

## Overview

This system adapts the Hermes Agents Forge methodology for **OpenAI Codex**. Instead of Claude's ZIP-based skill upload, Codex skills are delivered as **markdown instruction files** that can be installed in `~/.codex/skills/` or bundled per-project.

## Core Concept

The bootstrap process mirrors both the Claude and Forge approaches:

1. **Interview** — The agent (Codex itself or you) interviews about goals, tools, complexity, and constraints
2. **Design** — A team of Codex skills is proposed (personas, capabilities, dependencies)
3. **Confirmation** — You review and approve the proposal
4. **Generation** — Each skill's instruction file and configuration are created
5. **Installation** — Skills are placed in Codex's expected directory structure
6. **Verification** — Skills are validated against Codex format
7. **Handoff** — Instructions for using the skills

## Prerequisites

- Codex CLI installed: `npm install -g @openai/codex`
- Basic understanding of Codex custom instructions

## Getting Started

1. Open a terminal with Codex available
2. Run the interview script:
   ```bash
   cd codex/builders
   python3 interview.py
   ```
3. Follow the prompts to design your skill team
4. Review the generated proposal
5. Confirm to generate the skill files

## Structure

- `BOOTSTRAP.md` — Complete operating manual (agent instructions)
- `templates/` — Skill templates (personas, role schemas)
- `skills/` — Generated skill instruction files
- `builders/` — Tools to generate and validate skills
- `docs/` — Documentation and guides

## Isolation

This system is completely separate from Hermes and Claude:
- No impact on `~/.hermes/` configuration
- No impact on `~/.claude/` or Claude Desktop
- All files contained within the `codex/` directory in this repo

## Pre-Built Skills

The following skills are pre-built and ready for installation:

1. `market-scout.clmd` — Conducts market analysis and competitive research
2. `idea-challenger.clmd` — Challenges assumptions and validates ideas
3. `decision-bot.clmd` — Facilitates structured decision-making
4. `product-manager.clmd` — Creates product specifications and roadmaps
5. `product-architect.clmd` — Designs technical architecture
6. `mvp-builder.clmd` — Builds minimum viable products
7. `quality-guardian.clmd` — Validates quality through systematic testing

## Key Differences from Claude

| Aspect | Claude Skills | Codex Skills |
|--------|---------------|--------------|
| Format | ZIP with SKILL.md | `.clmd` markdown files |
| Location | Claude Desktop UI upload | `~/.codex/skills/` or per-project |
| Invocation | `/skill-name` | Direct invocation or slash commands |
| Packaging | ZIP archive | Markdown file |

## For Codex (Agent Instructions)

When Codex encounters this folder, it should follow `BOOTSTRAP.md` to:

1. Interview the user about their workflow needs
2. Propose a team of skills with distinct personas
3. Generate `.clmd` files with proper frontmatter
4. Validate each skill against the Codex format
5. Provide installation instructions