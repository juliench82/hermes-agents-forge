---
name: forge
description: Interview users, design custom agent teams, and provision isolated bot-mode profiles with rich personas and real skills
version: 1.4.0
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

Pick the smallest package that covers the user's needs. Specialists are
generated from the user's answers — never from a fixed list. Any role the
user needs (social media manager, grant writer, QA engineer) is designed
the same way.

### Step 3: Single Approval Gate
Present the complete plan: tier, specialists (name, role, tools, browser
mode — default "Use My Real Browser Profile"), collaboration, and what
provisioning will do (profiles + rich personas + real skills + verification).

Ask exactly: "Shall I provision this team as isolated bot-mode profiles?"

One yes authorizes everything. After it, run autonomously to completion —
no mid-flow confirmations. Deliver a final report.

### Step 4: Provision
Print a checklist of all confirmed agents first; mark each done as you go.

**4a — Profiles (batched, one terminal round):**
- `hermes profile create <name> --description "<role>"` (variant: `--clone`)
- Model pin only if requested: `hermes -p <name> config set model.default <model>`
- Write the `--description` line carefully: role + specialty in one line.
  Bot Mode injects every profile's title and description into each
  teammate's roster — that one line is how bots decide who to message.

**4b — Rich personas (every profile):**
Fetch catalog/roles/soul-schema.md from the repo (fallback skeleton:
Identity, Mission, Operating Principles, Working Style, Capabilities &
Tools, Collaboration Protocol, Boundaries, Escalation, Success Metrics).
Ground each persona in the user's quoted answers plus the knowledge of the
role's skills — builtins count. Every section filled — minimum 2 sentences
or 3 bullets. Self-review: rewrite anything that could apply to any role
unchanged. Write via write_file: `~/.hermes/profiles/<name>/SOUL.md`.

**4c — Real skills (every profile):**
Builtins first: every profile ships ~57 builtin skills already enabled
(test-driven-development, systematic-debugging, github,
codebase-inspection, computer-use, google-workspace…). Start with
`hermes -p <name> skills list` — a builtin that covers the role's need
satisfies it; never install a duplicate of an enabled builtin. Then, for
genuine gaps only, follow catalog/skills.json: `hermes skills search
<term>` → `hermes skills inspect <skill>` → `hermes -p <name> skills
install <skill>`. Never invent names. Skills from outside the official
Hub must pass NVIDIA SkillSpector (https://github.com/nvidia/skillspector)
first — on any risk finding, skip and report. Record builtins covering
the role, Hub skills installed, and genuine gaps per profile.

If interrupted: `hermes profile list`, compare with the checklist, provision
only what is missing. Never re-create an existing profile.

## Verification (with receipts)

1. `hermes profile list` — count against the approved plan; partial is not
   success, provision what is missing.
2. `hermes -p <name> skills list` — record the inventory per profile:
   builtins covering the role, Hub skills installed, genuine gaps.
3. `hermes -p <name> chat` — one smoke test per profile, answering in role.
4. Write TEAM.md: plan, profiles, skills (found/not found), browser mode,
   verification results, everything skipped or failed.
5. Rituals (Bot Mode): create a group chat for the team — rooms hold 2–6
   Bots, so a 7-member team gets two rooms (e.g. build + review). Bots
   reach each other with @mentions in rooms and `message_agent` DMs;
   @user in a room pings the user. Optionally attach a routine
   (`hermes cron`) — e.g. a weekly status digest to the group chat. New
   profiles share the main profile's credential pool by default, matching
   the real-browser mode. If Bot Mode is unavailable, suggest one small
   first task instead.
6. Paste verbatim receipts into the final report — the actual output of
   `hermes profile list` and each profile's `skills list`. "Verified"
   without output is not verification.
7. The final report must match the checklist: every item checked, or
   listed as SKIPPED with a reason (not found, rate limit, failed scan).
   Never declare the team "complete" or "ready" while an item is unchecked.

## Pitfalls

- **Never point two agents at the same profile** — each gets its own `~/.hermes/profiles/<name>/`
- **Never search the Hub for a capability an enabled builtin already provides** — check the profile's skills list first
- **Never invent skill names** — search first; a rejected name means stop, not retry
- **Never install third-party skills without the SkillSpector scan**
- **Never write thin personas** — the schema's depth rules are the floor, not the ceiling
- **Never write a throwaway `--description`** — every teammate's roster reads it to decide who to message
- **Never break the single approval gate** — no mid-flow confirmations after the yes
- **Never claim done without receipts** — paste actual `profile list` / `skills list` output; assertions are not verification
- **Never declare complete with unchecked items** — skipped steps are reported as skipped, never absorbed into "complete"
- **Bot Mode is a desktop UI feature** — programmatic provisioning uses `hermes profile create`
- **"Use My Real Browser Profile" is not an official HERMES feature** — it is a user preference, honored whenever a bot browses

## References

- Persona schema: catalog/roles/soul-schema.md — examples: catalog/roles/examples/
- Skills manifest: catalog/skills.json
- Official HERMES Bot Mode: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- Official HERMES Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Official HERMES Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- SOUL.md guide: https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes
- SkillSpector: https://github.com/nvidia/skillspector
