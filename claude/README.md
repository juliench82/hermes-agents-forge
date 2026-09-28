# Claude Skill Bootstrap System

> Agent-directed onboarding for autonomous Claude Chat skill teams

## Overview

This system adapts the Hermes Agents Forge methodology for **Claude Desktop Chat** (not Claude Code). Instead of provisioning Hermes profiles with SOUL.md personas, it generates SKILL.md files that package Claude skills as ZIP files for upload through the Claude Desktop UI.

## Core Concept

The bootstrap process mirrors Forge's flow:

1. **Interview** — The agent interviews you about your goals, tools, complexity, and constraints
2. **Design** — A team of Claude skills is proposed (personas, capabilities, dependencies)
3. **Confirmation** — You review and approve the proposal
4. **Generation** — Each skill's SKILL.md and supporting files are created
5. **Packaging** — Skills are built into ZIP files ready for upload
6. **Verification** — Skills are validated against the Claude skill format
7. **Handoff** — Instructions for uploading and activating skills

## Prerequisites

- Claude Desktop app with skills capability enabled
- No additional software required (skills are uploaded as ZIP files)

## Getting Started

1. Open Claude Desktop
2. Start a conversation with a coding-capable model
3. Send: `"Read and follow the bootstrap instructions at BOOTSTRAP.md"`

## Structure

- `BOOTSTRAP.md` — Complete operating manual (agent instructions)
- `templates/` — Skill templates (personas, role schemas, hooks)
- `skills/` — Generated skill packages ready for upload
- `builders/` — Tools to validate and package skills
- `docs/` — Documentation and guides
- `assets/` — Icons and images for skills

## Isolation

This system is completely separate from Hermes:
- No impact on `~/.hermes/` configuration
- No impact on existing Forge workflows
- All files contained within the `claude/` directory in this repo

## Pre-Built Skills

The following skills are pre-built and ready for upload:

1. **market-scout** — Conducts market research and competitive analysis
2. **idea-challenger** — Challenges assumptions and validates ideas before implementation
3. **product-manager** — Creates product specifications, roadmaps, and requirements
4. **product-architect** — Designs technical architecture and system patterns
5. **decision-bot** — Formal decision-making and evaluation framework
6. **mvp-builder** — Builds minimum viable products through structured iteration
7. **quality-guardian** — Validates quality, creates test plans, catches regressions