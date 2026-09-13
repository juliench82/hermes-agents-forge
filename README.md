A customer points Hermes to the canonical instructions at:

`https://hermes-agents-forge.vercel.app/llms.txt`

Forge then interviews the customer, designs a custom governed team, provisions isolated profiles and real skills, optimizes the installation, and verifies the result with receipts. No repository clone or manual profile assembly is required for the Forge flow.

## What you get

- **Custom team design** — 3, 5, or 7 specialists generated from broad capability needs, not a fixed industry catalog.
- **Rich personas** — every profile receives a schema-grounded `SOUL.md` based on the customer's actual requirements and words.
- **Real skills** — builtin skills first, bespoke generated skills for genuine gaps, and inspected/security-scanned external skills only where necessary.
- **Governance** — explicit ownership, tool boundaries, data boundaries, approval gates, cost/model policy, and escalation rules.
- **Receipts, not assertions** — profile, skill, configuration, smoke-test, handoff, and durable `TEAM.md` evidence.
- **Optimization** — compression/context hygiene, economical worker models, reasoning policy, browser policy, concurrency, and MOA settings supported by the installed Hermes version.
- **Coordination surface** — a coordinator-owned control-plane handoff; Workflow Builder owns workflow-specific execution boards, routines, integrations, and trials.

## Two-stage lifecycle

### Stage 1 — Team Setup

After one explicit team-provisioning approval, Forge:

1. Runs pre-flight and session-hygiene checks.
2. Designs the smallest complete 3/5/7 specialist team.
3. Tunes the coordinator and backs up the original persona.
4. Creates isolated workers with rich personas and focused skills.
5. Verifies full skill inventories, configuration, smoke tests, contracts, policy, and receipts.
6. Creates or reuses one non-executable coordinator handoff for the first workflow.

Team Setup finishes with:

```text
TEAM STATUS: PROVISIONED
WORKFLOW HANDOFF: READY
WORKFLOW STATUS: NONE
```

It does not ask workflow-specific questions or create workflow execution cards, schedules, routines, live integrations, trials, or external workflow actions.

### Stage 2 — Workflow Builder

The stable coordinator validates and claims the handoff, records the receipt, asks the workflow-specific interview, and drafts the workflow contract, policy, runbook, and trial plan.

Workflow Builder stops for explicit workflow-design approval. Only after approval may it create execution cards, connect integrations, change workflow permissions, create routines, or run a supervised trial. A workflow becomes operational only after trial evidence and explicit human activation approval.

## Team sizes

- **3 specialists:** focused, single-domain capability.
- **5 specialists:** multi-stage capability requiring analysis, execution, review, and reconciliation.
- **7 specialists:** complex, coordination-heavy capability across multiple domains.

The coordinator is separate from the package count. Four- and six-specialist packages are not used.

## Trust and safety

- One explicit approval gates Team Setup provisioning.
- A workflow-design approval gates all workflow execution assets.
- External and irreversible actions remain approval-gated.
- Skills are inspected and security-scanned; dangerous verdicts are never forced.
- Rejected settings, unavailable capabilities, and provider failures are reported explicitly.
- Interrupted setup resumes from receipts and provisions only missing assets.
- A workflow is not operational without supervised trial evidence and explicit human activation.

## References

- Canonical instructions: `site/llms.txt`
- Product requirements: `PRODUCT.md`
- Bootstrap brief: `HERMES.md`
- Team Setup: `skills/forge/SKILL.md`
- Workflow Builder: `skills/workflow-builder/SKILL.md`
- Official Hermes docs: https://hermes-agent.nousresearch.com/docs/
