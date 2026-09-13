# Changelog

All notable changes to Hermes Agents Forge are documented here.

## Unreleased

### Product lifecycle

- Split onboarding into two explicit phases: Team Setup and Workflow Builder.
- Restored the full original Team Setup quality contract: dynamic 3/5/7 team sizing, coordinator-first tuning, isolated profiles, rich personas, tiered skill resolution, optimization, recovery, smoke tests, and receipt-first verification.
- Added an idempotent, non-executable coordinator handoff for the first workflow.
- Added workflow-scoped contracts, policies, runbooks, trials, approval gates, and activation states.
- Kept workflow-specific execution, integrations, routines, trials, and external actions out of Team Setup.
- Restored and expanded the canonical `site/llms.txt` operating manual.
- Added explicit release-readiness distinction between specification readiness and runtime acceptance.

### Governance

- Preserved team contracts and policy templates.
- Added control-plane metadata and dispatcher fallback behavior.
- Added claim/recovery receipts and duplicate-kickoff protection.
- Kept dangerous skill verdicts, unsupported settings, unavailable capabilities, and provider failures visible rather than silently absorbing them.
