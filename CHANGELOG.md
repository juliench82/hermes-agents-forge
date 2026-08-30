# Changelog

## [2026-08-30] — HERMES Alignment Update (Agent-Directed)

### Changes
- Rewrote `site/llms.txt` as agent-directed instructions (for HERMES agents browsing the page)
- Updated `HERMES.md` to address HERMES agents directly, with step-by-step workflow
- Updated `skills/forge/SKILL.md` with agent-executed workflow instructions
- Updated `PRODUCT.md` to describe agent-directed flow and package tiers (3/5/7)
- Updated `runtime/README.md` with browser automation context
- Added package tier documentation (3/5/7 agents based on task complexity)
- Clarified "Use My Real Browser Profile" as default provisioning option

### Why
- Product is designed for HERMES agents with browser automation to read `site/llms.txt` and execute workflow
- Docs were previously user-facing (manual installation steps) instead of agent-directed
- Needed to align with HERMES browser automation + real-profile browsing capabilities
- Added package tiers to match interview-driven complexity assessment

### Impact on User Flow
- User visits site, clicks "Read agent instructions"
- User's HERMES agent (with browser tools) browses to `site/llms.txt`
- Agent reads instructions, loads forge skill, runs `/forge`
- Agent interviews user, determines package tier (3/5/7), proposes team
- User confirms, agent provisions profiles via runtime
- Default: "Use My Real Browser Profile" for seamless auth

---

