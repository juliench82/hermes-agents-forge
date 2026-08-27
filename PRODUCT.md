# Hermes Agents Forge — Product Goal

## Intended Customer Journey

1. Customer goes to our webpage (`https://hermes-agents-forge.vercel.app`)
2. Clicks "read agent instructions"
3. Points their HERMES agent to `https://hermes-agents-forge.vercel.app/llms.txt`
4. HERMES agent (any LLM, any thinking level: LOW/MEDIUM/HIGH) interviews the user:
   - What do you want to automate?
   - What tools do you use? (GitHub, email, calendar, etc.)
   - What are your constraints? (budget, time, approval gates)
   - Where should we send you updates? (Telegram, Discord, Slack, email)
5. Agent designs a custom team of isolated bot-mode profiles
6. Agent provisions the profiles and starts collaboration
7. Team delivers workflows to automate the customer's pain points

## Current State (after PR #69 + cleanup)

### Entry Point
- `site/llms.txt` exists and is deployed to Vercel
- Points to `HERMES.md` + `hermes skills trust` + `pip install -e ".[dev]"` + `python -m compiler --manifest bootstrap.manifest.json`
- Warns "do not create profiles/" — conflicts with the goal of creating isolated bot-mode profiles

### Core Components
- `skills/forge/SKILL.md` — project-local forge skill (~9KB), requires `hermes skills trust`
- `compiler/` — `onboarding_prompt.py`, `first_interaction.py`, `team_compiler.py`, adapter tests for 6 fixed roles (architect, builder, orchestrator, product-strategist, quality-guardian, self-improver)
- `runtime/` — `onboarding_wizard.py`, `dynamic_profiles.py`, `live_provisioner.py`, `hermes_kernel.py`, plus leftovers (Buzz, Obsidian, duplicate audit)
- `onboarding/` — workflows/templates, but docs say "follow after compiler", not "ask the user what to automate"
- `catalog/` — connectors (imap-smtp, rest-api), triggers (cron), policies (8-layer security), roles
- `bootstrap.manifest.json` — declarative team spec (solo-founder-app-builder example)

### Hygiene (Done)
- LICENSE, `.gitignore`, `pyproject.toml`, `Dockerfile`
- README, HERMES, AGENTS, BOOTSTRAP, CHANGELOG, CONTRIBUTING rewritten
- Duplicate `site/public/{SKILL.md,install.sh,start.md,llms.txt}` removed
- Root YAML skills (`onboarding-loop.yaml`, `team-designer.yaml`) removed
- Adapter tests no longer depend on repo-root `profiles/` tree

## Known Gaps

1. **No interview loop**: `llms.txt` + `HERMES.md` do not tell the agent to interview the user. They only describe the compiler pipeline.
2. **No bot-mode provisioning**: Docs warn "do not create profiles/" but the goal is to create isolated bot-mode profiles.
3. **Two engines, no spine**: `skills/forge` (Hermes skill) vs `python -m compiler` (Python CLI). Both exist, but neither is the product entry point.
4. **Leftover runtime**: Buzz, Obsidian, duplicate audit, unused installer paths still in `runtime/`.
5. **Frozen team**: Adapter tests are for 6 fixed roles, not dynamic customer teams.
6. **Buzz optional**: Agreed Buzz should be optional, but not addressed in docs or code.

## Next Steps

1. **Rewrite `site/llms.txt`** to be the product:
   - After "read HERMES.md / trust forge skill", add: interview the user, propose a team, get confirmation, then provision isolated bot-mode profiles.
   - Remove "do not create profiles/" warning.
   - Add: "Run `hermes skills trust` to load the forge skill, then start the interview."

2. **Update `HERMES.md`** to match:
   - Remove compiler-only flow as the primary entry.
   - Add the interview → design → provision flow.
   - Keep `hermes skills trust` as a critical step.

3. **Update `skills/forge/SKILL.md`** to implement:
   - The interview questions (use case, tools, constraints, messengers).
   - Team design (propose 3–7 profiles based on answers).
   - Profile creation (`hermes profile create --bot-mode` for each).
   - Optional: call `python -m compiler` as a backend for advanced teams.

4. **Inventory `runtime/`** and delete files not called by the new flow:
   - Buzz (optional, quarantine or delete).
   - Obsidian (optional, quarantine or delete).
   - Duplicate audit (`audit_log.py` + `audit_logger.py`).
   - Unused installer paths.

5. **Prove the funnel once**:
   - Site button → `/llms.txt` → clone/trust → interview → N isolated profiles in bot mode → one sample workflow.
   - Test with LOW, MEDIUM, HIGH thinking models.

6. **Update `CHANGELOG.md`** with these changes.

## How to Continue (for New Conversations)

Start by reading:
1. `PRODUCT.md` (this file) — goal, current state, gaps, next steps
2. `CHANGELOG.md` — what changed in each PR
3. `site/llms.txt` — current entry point
4. `HERMES.md` — current Hermes-specific instructions
5. `skills/forge/SKILL.md` — forge skill
6. `runtime/` directory — inventory leftovers

Then propose exact changes to `site/llms.txt`, `HERMES.md`, and `skills/forge/SKILL.md` to close the gap.

## References

- PR #69: `chore: repo cleanup and Hermes-native alignment`
- Hermes docs: https://hermes-agent.nousresearch.com/docs/user-guide/
- Vercel site: https://hermes-agents-forge.vercel.app
- GitHub repo: https://github.com/juliench82/hermes-agents-forge
