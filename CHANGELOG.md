# Changelog

## [2026-10-05] — v0.7.9: Measure cost, never gate on a balance header

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
