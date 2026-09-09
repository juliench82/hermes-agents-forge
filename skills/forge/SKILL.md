---
name: forge
description: Interview users, design custom agent teams, and provision isolated bot-mode profiles with rich personas and real skills
version: 1.11.0
metadata:
  hermes:
    tags: [onboarding, team-design, bot-mode]
    category: productivity
---

# Forge Skill — Custom Agent Team Provisioning

## When to Use
Use this skill when:
- A user visits the Hermes-Agents-Forge site and clicks "Read agent instructions"
- The user points their HERMES agent to `https://hermes-agents-forge.vercel.app/llms.txt`
- You need to interview the user, design a custom team, and provision isolated bot-mode profiles

## Procedure

### Step 1: Interview the User
Ask one at a time:
1. What workflows do you want to automate?
2. Which tools, sites, and accounts are involved?
3. What does a good result look like? (quality bar, review requirements)
4. How complex is your work? (one project or several? how many moving parts?)
5. Is there anything you do NOT want automated?

Keep the user's exact words — the personas will quote them.

### Step 2: Design the Team
Select the package tier:
- **Package 3** — basic: 3 specialists; single-domain, simple workflows.
- **Package 5** — intermediate: 5 specialists; multi-domain, needs analysis and review.
- **Package 7** — complex: 7 specialists; multi-project, coordination-heavy.

The team is exactly 3, 5, or 7 specialists — never 4 or 6.

Pick the smallest package that covers the user's needs. Specialists are
generated from the user's answers — never from a fixed list. Any role the
user needs (social media manager, grant writer, QA engineer) is designed
the same way.

### Step 3: Single Approval Gate
Present the complete plan: tier, specialists (name, role, tools, browser
mode — default "Use My Real Browser Profile"), collaboration, and what
provisioning will do (profiles + rich personas + real skills + main-profile
tuning + verification + board wiring).

Ask exactly: "Shall I provision this team as isolated bot-mode profiles?"

One yes authorizes everything. After it, run autonomously to completion —
no mid-flow confirmations. Deliver a final report.

### Step 4: Provision
Print a checklist of all confirmed agents first; mark each done as you go.

**4-0 — Externalize the checklist:** before the first `profile create`,
call the `todo` tool with one item per specialist plus one verification
item, using the approved names exactly. Mark items complete as you finish
them; call `todo` with no parameters between specialists and before
claiming done. The list — not memory — is the source of truth for what
remains.

**4-0a — Tune profile 0 (the main profile):** the main profile is the team
coordinator — a team next to a stock, untuned main profile is not fully
provisioned. Back up `~/.hermes/SOUL.md` to `SOUL.md.backup-forge` first,
then rewrite it as the coordinator (board operations, dispatch, receipts —
never implementation). Apply context hygiene to the main profile:
`hermes config set compression.enabled true`, `hermes config set
compression.threshold 0.50` (official default — never lower without
evidence), `hermes config set moa.enabled false` (one model per turn on
the coordinator — MOA multiplies token spend), and fix
`delegation.fanout: user_turn` if present. Set
`browser.use_real_profile true` per approved policy and still tell the
user to confirm the Desktop setting. Workers get the same treatment:
compression on, MOA off, inexpensive model unless pinned. A rejected
config key is recorded in TEAM.md and skipped loudly — never silently.

**4a — Profiles (batched, one terminal round):**
- `hermes profile create <name> --description "<role>"` (variant: `--clone`)
- Model pin only if requested: `hermes -p <name> config set model.default <model>`
- Write the `--description` line carefully: role + specialty in one line.
  Bot Mode injects every profile's title and description into each
  teammate's roster — that one line is how bots decide who to message.
- Apply the 4-0a worker settings to each new profile: compression on,
  MOA off, cheap model unless pinned.

**4b — Rich personas (every profile):**
Fetch catalog/roles/soul-schema.md from the repo (fallback skeleton:
Identity, Mission, Operating Principles, Working Style, Capabilities &
Tools, Collaboration Protocol, Boundaries, Escalation, Success Metrics).
Ground each persona in the user's quoted answers plus the knowledge of the
role's skills — all tiers count. Every section filled — minimum 2
sentences or 3 bullets. Self-review: rewrite anything that could apply to
any role unchanged. Write via write_file: `~/.hermes/profiles/<name>/SOUL.md`.

Phase exit: paste one line per profile — name and SOUL.md path written.

**4c — Real skills, three tiers in order:**
- Tier 1, builtins: `hermes -p <name> skills list` — a covering builtin
  satisfies the need; never duplicate an enabled builtin.
- Tier 2, generative: for uncovered roles, author a bespoke skill with
  `skill_manage` create — house format, description under 60 characters,
  grounded in the interview answers.
- Tier 3, Hub gaps only: `hermes skills search <term>` → `inspect` →
  `hermes -p <name> skills install <skill> --yes`. Never invent names.

Phase exit: paste one profile's FULL `skills list` output before
verification — the table plus the counts line (e.g. "2 hub-installed,
57 builtin, 1 local — 60 enabled, 0 disabled"). The counts line IS the
receipt; a rounded claim is an assertion.

If interrupted: `hermes profile list`, compare with the checklist, provision
only what is missing. Never re-create an existing profile.

## Verification (with receipts)

1. `hermes profile list` AND `todo` (no parameters) — count against the
   approved plan; zero open items; the roster must match the approved
   names exactly; partial is not success, provision what is missing.
2. `hermes -p <name> skills list` — paste the FULL output including the
   counts line; record the inventory per profile: builtins covering the
   role, generated skills, gaps.
3. `hermes -p <name> chat` — one smoke test per profile, answering in role.
4. Profile 0 receipts: `hermes config get compression` and
   `hermes config get moa.enabled` pasted verbatim; the coordinator
   SOUL.md path; the backup at ~/.hermes/SOUL.md.backup-forge confirmed.
5. Write TEAM.md: plan, profiles, skills (found/not found — with counts
   lines), main-profile tuning applied or skipped with reason, browser
   mode, verification results, everything skipped or failed.
6. Rituals (Bot Mode): create a group chat for the team — rooms hold 2–6
   Bots, so a 7-member team gets two rooms (e.g. build + review). Bots
   reach each other with @mentions in rooms and `message_agent` DMs;
   @user in a room pings the user. Optionally attach a routine
   (`hermes cron`) — e.g. a weekly status digest to the group chat. New
   profiles share the main profile's credential pool by default, matching
   the real-browser mode. If Bot Mode is unavailable, suggest one small
   first task instead.
7. Paste verbatim receipts into the final report — the actual output of
   `hermes profile list`, each profile's `skills list` with counts line,
   main-profile config receipts, and kanban receipts. "Verified"
   without output is not verification.
8. The final report must match the checklist: every item checked, or
   listed as SKIPPED with a reason (not found, rate limit, failed scan).
   Never declare the team "complete" or "ready" while an item is unchecked.
9. Phase-exit receipts: after personas, paste the SOUL.md files written;
   after skills, paste one profile's skills list — a stalled run must be
   auditable at its failure point, not only in a final report that never
   arrives.

## Wire the Board (Kanban — the work engine)

After verification: `hermes gateway status` → `hermes gateway start` if
not running (the dispatcher lives in the gateway). `hermes kanban init`
(idempotent; optional named board: `hermes kanban boards create <slug>
--name "<Team>" --switch`). Seed first cards: `hermes kanban create
"<title>" --assignee <approved-name> --body "<goal, context, decisions,
acceptance criteria>"`. Decide before fan-out — workers cannot see
sibling cards; stamp every decision into every body that depends on it.
"Keep going until done" cards: `--goal` with explicit acceptance criteria.
Per-card: `--skill <name>` (installed on the assignee), `--model <model>`
for quality-sensitive cards. Review loop: implementers call
`kanban_request_review`, reviewers call `kanban_request_changes`. Receipts:
verbatim `hermes kanban list` / `hermes kanban stats` into the final
report; board name, card IDs, and Desktop plugin state (on/off) into
TEAM.md.

Kanban Desktop: the dashboard's Kanban tab is a bundled plugin, OFF by
default — the CLI board and the Desktop view are two surfaces. The CLI
board, gateway, and dispatcher work without it. If the plugin is off,
record the state and put the one-line instruction in the final report
("Settings → Plugins → Kanban → enable"); never block the handoff on
the toggle, and never claim the board is "wired" without stating
whether the Desktop plugin is on or off.

## Pitfalls

- **Never point two agents at the same profile** — each gets its own `~/.hermes/profiles/<name>/`
- **Never trust a local forge skill of unknown version** — if its frontmatter is not 1.11.0, re-fetch skills/forge/SKILL.md from the repo and follow that copy
- **Never propose 4 or 6 specialists** — the package is exactly 3, 5, or 7
- **Never leave the default SOUL.md stock after provisioning a team** — the main profile is the coordinator; back it up first, then rewrite it
- **Never enable MOA on the coordinator** — reference models plus aggregator on every user turn multiplies token spend; one model per turn
- **Never claim a skills inventory without quoting the counts line verbatim** — "59 builtins + 1 generated" is a rounded assertion, not a receipt
- **Never claim Kanban is "wired" without stating the Desktop plugin state** — the CLI board and the Desktop tab are separate surfaces
- **Never search the Hub for a capability an enabled builtin already provides** — check the profile's skills list first
- **Never invent skill names** — search first; a rejected name means stop, not retry
- **Never --force past a security verdict** — dangerous means skip and report
- **Never write thin personas** — the schema's depth rules are the floor, not the ceiling
- **Never write a throwaway `--description`** — every teammate's roster reads it to decide who to message
- **Never break the single approval gate** — no mid-flow confirmations after the yes
- **Never claim done without receipts** — paste actual `profile list` / `skills list` / `config get` output; assertions are not verification
- **Never claim done from memory** — show the `todo` list (zero open items) and `hermes profile list` (roster matches approved names) first
- **Never declare complete with unchecked items** — skipped steps are reported as skipped, never absorbed into "complete"
- **Never create cards for assignee names that aren't on the roster** — the dispatcher silently fails on unknown assignees and auto-blocks the card after two spawn failures
- **Never let the coordinator profile do implementation work** — pair the board with a coordinator restricted to board operations (kanban, gateway, memory toolsets)
- **Never write a vague goal-mode body** — the judge reads title + body as acceptance criteria; vague goals block, sharp goals finish
- **Never silently skip a failed config key** — record the key and reason in TEAM.md; a recorded skip is valid, a silent skip is not
- **Bot Mode is a desktop UI feature** — programmatic provisioning uses `hermes profile create`
- **"Use My Real Browser Profile" is not an official HERMES feature** — it is a user preference, honored whenever a bot browses

## References

- Persona schema: catalog/roles/soul-schema.md — examples: catalog/roles/examples/
- Skills manifest: catalog/skills.json
- Official HERMES Bot Mode: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- Official HERMES Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Official HERMES Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Official HERMES Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Official HERMES Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- SOUL.md guide: https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes
