# HERMES Forge

**Agent-directed onboarding for autonomous HERMES teams**

Repo: https://github.com/juliench82/hermes-agents-forge  
Live instructions: https://hermes-agents-forge.vercel.app/llms.txt

---

## What HERMES Forge is

HERMES Forge is a self‑contained, agent‑directed onboarding system for HERMES. A customer with HERMES already installed visits the Forge site, clicks **Read agent instructions**, and their HERMES agent reads `llms.txt`. From there, the agent:

1. Interviews the user (5–6 questions).
2. Selects a package tier (3 / 5 / 7 specialists).
3. Proposes a team of bot‑mode profiles.
4. Waits for explicit confirmation.
5. Provisions isolated profiles with real skills and SOUL.md personas.
6. Verifies the team and hands off a first task.

This quickstart shows you exactly how to run that flow end‑to‑end and verify it worked.

---

## Prerequisites

- HERMES Desktop or CLI installed and working.
- A GitHub account (for code workflows).
- A browser (Chrome/Brave) for research and docs.
- Optional but recommended: Gmail and Google Docs access.

You do **not** need to clone any repo or run manual install scripts. The agent will fetch what it needs from `llms.txt`.

---

## Step 1 — Start the flow

In your HERMES session, use this exact prompt:

```text
Read and follow the agent instructions at https://hermes-agents-forge.vercel.app/llms.txt
```

If your HERMES agent supports browser automation, it may open the URL. If not, it should fetch the plain‑text file directly. Either way, the content it reads is the same operating manual.

**Success signal:** The agent begins an interview with you, one question at a time.

---

## Step 2 — The interview (5–6 questions)

The agent will ask about your goals, tools, quality bar, complexity, and constraints. Answer in plain language. Example answers for a solo founder who wants "idea → app":

1. **What should your agent team do for you?**  
   "Take a random business idea for an app and build it end‑to‑end: research, spec, code, test, deploy."

2. **Which tools, sites, and accounts are involved?**  
   "GitHub, browser for research, Gmail, Google Docs. I'm open to suggestions for project tracking and deployment."

3. **What's your quality bar before something is 'done'?**  
   "Code must run, pass basic tests, and be demonstrable. I want human‑readable summaries before any public release."

4. **How complex is your work? (single project or several? how many moving parts?)**  
   "One project at a time, but each project spans research, product, design, frontend, backend, QA, and release."

5. **Is there anything you do NOT want automated?**  
   "No — I want the team to iterate on code until it's reliably working and demo‑ready."

The agent uses your answers to pick a package tier.

---

## Step 3 — Package selection (3 / 5 / 7)

Forge defines three tiers:

- **Package 3 — Basic:** Single‑domain, simple workflows.
- **Package 5 — Intermediate:** Multi‑domain, needs analysis and review.
- **Package 7 — Complex:** Multi‑project, coordination‑heavy.

For "idea → app" with research, product, design, frontend, backend, QA, and release, the correct tier is **Package 7 (Complex)**.

**Success signal:** The agent explicitly states "Package 7 (Complex)" and lists 7 specialist roles.

---

## Step 4 — Team proposal

The agent must present a table or list with, for each specialist:

- Name (e.g., `market-researcher`, `product-manager`, `lead-architect`, `frontend-developer`, `backend-developer`, `qa-engineer`, `release-manager`).
- Role and responsibilities.
- Primary tools (browser, GitHub, terminal, docs).
- Browser mode: **"Use My Real Browser Profile"** presented as the default.

It must then ask:

> "Shall I provision this team as isolated bot‑mode profiles? This will create separate HERMES profiles under `~/.hermes/profiles/<name>/`."

**Do not confirm yet.** First, test the confirmation gate.

### Test the confirmation gate

Reply with a change request, for example:

> "Wait — swap the researcher for an editor focused on landing‑page copy."

The agent must:

- Adjust the proposal accordingly.
- Re‑present the updated team.
- Ask for confirmation again.

Only when you are happy with the proposal, reply:

> "Yes — provision this team as isolated bot‑mode profiles."

---

## Step 5 — Provisioning

After your explicit "yes", the agent must provision each profile using HERMES CLI commands of the form:

```bash
hermes profile create <name> --description "<role>"
hermes -p <name> config set model.default <model>
# Write SOUL.md to ~/.hermes/profiles/<name>/SOUL.md
hermes -p <name> skills install <skill> --yes
```

Key points:

- Each specialist gets its own isolated profile under `~/.hermes/profiles/`.
- `--yes` skips only the confirmation prompt; the security scanner still runs on every skill install.
- The agent should install skills in four tiers:
  1. **Builtins first** — `hermes -p <name> skills list` — never duplicate an enabled builtin.
  2. **Forge library** — direct URL installs from the repo's `skills/library/` (with `--category` and `--yes`).
  3. **Generative** — bespoke skills authored with `skill_manage` for uncovered roles.
  4. **Hub** — `hermes skills search` → `inspect` → `install <skill> --yes` for genuine gaps.

If the agent is interrupted mid‑provisioning, it must resume by:

1. Running `hermes profile list`.
2. Comparing to the proposed checklist.
3. Creating only the missing profiles.

---

## Step 6 — Verification

Before claiming "team ready", the agent must verify:

```bash
hermes profile list
```

and confirm that all proposed profiles exist. For each profile, it should optionally run:

```bash
hermes -p <name> doctor
hermes -p <name> skills list
```

**Success signals:**

- The number of profiles matches the package tier (e.g., 7 for Package 7).
- Each profile responds to `doctor` without errors.
- Skills are listed and match the four‑tier plan (no duplicates of builtins).

Only then should the agent say the team is ready and propose a first task.

---

## Troubleshooting top 5 failures

### 1. Browser CDP / remote debugging errors

Symptoms: `browser_exec` fails, "Allow remote debugging?" popup loops, or connection timeouts.

Fix:

- Quit Chrome fully (⌘Q, check Activity Monitor).
- Launch Chrome with debugging enabled:

  ```bash
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --remote-debugging-port=9222 \
    --user-data-dir="$HOME/.hermes/chrome-debug-profile" &
  ```

- In HERMES: `/browser connect ws://localhost:9222`  
  Or set `BROWSER_CDP_URL="http://localhost:9222"` in `~/.hermes/.env`.

Use browser automation only when needed; the Forge bootstrap itself does not require it.

---

### 2. Partial team creation

Symptoms: Agent claims "team ready" but `hermes profile list` shows fewer profiles than promised.

Fix:

- Run `hermes profile list`.
- Compare to the proposed checklist.
- Ask the agent to create only the missing profiles.
- Require `hermes profile list` again before accepting "done".

---

### 3. Skill install prompts breaking autonomy

Symptoms: Agent stops at "Confirm skill install? [y/N]" and waits.

Fix:

- Ensure the agent uses `--yes` on all `skills install` commands.
- For Forge library skills, the single approval to run the flow covers all installs; `--yes` skips only the prompt, not the security scan.

---

### 4. Model drift / language switching / hallucination

Symptoms: Agent switches languages, invents commands, or claims impossible actions.

Fix:

- Use a medium or high reasoning model if available.
- Keep the initial prompt minimal and unchanged:  
  `Read and follow the agent instructions at https://hermes-agents-forge.vercel.app/llms.txt`
- If drift occurs, restart with a fresh session and the same prompt.

---

### 5. False "done" claims

Symptoms: Agent says "team is ready" without running `hermes profile list` or verifying skills.

Fix:

- Require the agent to run and show `hermes profile list`.
- Require at least one `hermes -p <name> doctor` and `skills list` per profile.
- Do not accept "done" until verification commands are shown.

---

## Next steps

Once your team is verified:

1. Give it a concrete first project brief (one paragraph: idea, target users, must‑have features).
2. Let the team run through research → spec → code → test → deploy.
3. Observe how the QA loop forces iteration until the app is demo‑ready.

For deeper playbooks (interview scripts, role SOUL.md templates, skills engineering), see the paid HERMES Forge guides.

---

## Links

- Repo: https://github.com/juliench82/hermes-agents-forge
- Live instructions: https://hermes-agents-forge.vercel.app/llms.txt
- HERMES docs: https://hermes-agent.nousresearch.com/docs
