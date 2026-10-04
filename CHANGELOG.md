# Changelog

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
