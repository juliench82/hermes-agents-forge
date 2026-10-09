# Changelog

## [2026-10-09] — v0.8.0: Token-minimization defaults during onboarding

- Step 4.1 provisions token-minimization defaults for the coordinator profile: threshold 0.75
  (effective floor for models below 512K context; 0.50 is silently ignored on those models),
  target_ratio 0.15, protect_last_n 12, proactive_prune_tokens 48000 on large-window models,
  idle_compact_after_seconds 1800, reasoning_effort medium by default with a supervised-trial gate
  before ever lowering to low, display verbosity off (show_reasoning, turn_summary,
  show_commentary, interim_assistant_messages, spinner_token_flow → false).
- Reasoning effort stays at medium by default — never low until a supervised trial verifies the
  customer's resolved free model follows the manual faithfully at low; raise if any Step 4 stage
  stalls or fabricates a receipt.
- Warning: `agent.text_verbosity` is a Responses/Codex-transport-only key — do not set it on
  `chat_completions` profiles, where it is a dead end.
- Model-provider models below 512K context are floored at threshold 0.75 (raise-only) — set 0.75
  explicitly rather than 0.50, which is silently ignored on those models.

## [2026-10-05] — v0.7.9: Measure cost, never gate on a balance header

- `hermes/llms.txt` and `site/llms.txt` (v0.7.9, commit 5340102): ship Kanban as `defaultEnabled: true` during Team Setup (Desktop bot-pool capacity switch flip), and add Story 3 — parent-chained six-card kanban pipeline with `request-review`/`request-changes` retry — as the final step after profile creation.
- A Forge team was verified on a model priced at `0.0000000000`, and six live smoke tests were
  still recorded `SKIPPED` because a `⚠ You've used $X of your $Y cap` banner was read as a
  per-run budget. It is not one: `agent/credits_tracker.py:200` reports an account-level
  subscription balance from response headers, and per-run cost never enters that number.
- New **Step 1b — Cost verification before gating any live run**: read the price cache, quote the
  runtime's own `is_free_tier_model()`, measure a run with `hermes -z … --usage-file`, and treat a
  credit notice as a missing measurement rather than a budget. A free model suppresses only
  `credits.depleted`, so the usage gauge still fires and proves nothing about the run in hand.
- Smoke-test receipts now require the per-run measured cost per profile, and a `SKIPPED` receipt
  citing a credit or quota notice is explicitly not acceptable.
- The model default now reads "cheapest tier that meets the capability bar", resolved from the
  installed provider's catalog and price cache — **no free model is hardcoded in this manual**, and
  the customer's configured default is never changed without team-design approval. A free SKU
  differs per provider and per build, and a `stealth/` preview can change or vanish.
- New hard rule covering both: never gate or skip work on a credit notice, never hardcode a free
  model.

## [2026-10-05] — v0.7.8: Link drop starts the flow

- Sharing the Forge URL is now itself the request to run the manual. A bare paste of
  `hermes-agents-forge.vercel.app/llms.txt` starts Team Setup at the interview — the agent no
  longer asks what to do with the link or waits for a "read and follow" phrase.
- The team-design approval gate is unchanged and still required exactly once.
- Hermes READMEs now teach the bare URL as the entry point, with `@url:` documented as the
  fallback for agents that do not fetch bare links.
- Workflow Builder remains a separate, explicitly-triggered phase.

## [2026-09-07] — v0.5.2: Context hygiene

- Adds post-gate context-hygiene configuration, per-profile settings, and Kanban Desktop activation guidance.
