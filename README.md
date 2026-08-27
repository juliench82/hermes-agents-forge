# HERMES Agents — Forge

A customer goes to the webpage, clicks **"read agent instructions"**, and points their HERMES agent to:

https://hermes-agents-forge.vercel.app/llms.txt

From there, any HERMES agent (any LLM, any thinking level) should:

1. **Interview** the user about what they want to automate.
2. **Design** a custom team of specialized agent profiles.
3. **Provision** isolated bot-mode profiles that collaborate on workflows.

## Quick start

1. **Clone** this repo.
2. **Read** the product spec: [`HERMES.md`](./HERMES.md).
3. **Trust** the Forge skill: [`skills/forge/SKILL.md`](./skills/forge/SKILL.md).
4. **Run** the onboarding wizard:

   ```bash
   python -m runtime.onboarding_wizard
   ```

   This will:
   - Ask what you want to automate (domains, tools, constraints).
   - Propose a minimal team (roles, responsibilities, handoffs).
   - On confirmation, provision isolated bot-mode profiles under `profiles/`.
   - Create a sample workflow under `onboarding/workflows/`.

5. **Inspect** your team:
   - Profiles: `profiles/`
   - Workflow: `onboarding/workflows/`
   - Skill boundary: `skills/forge/SKILL.md`

To refine your team later:

```bash
python -m runtime.onboarding_wizard --refine
```

## Architecture

- **`site/llms.txt`** — Public entry point for HERMES agents.
- **`HERMES.md`** — Product spec and onboarding flow.
- **`skills/forge/SKILL.md`** — Trusted skill that implements interview + provisioning.
- **`runtime/`** — Onboarding engine:
  - `onboarding_wizard.py` — Interview + team design.
  - `dynamic_profiles.py` — Profile creation/configuration.
  - `live_provisioner.py` — Workflow wiring.
- **`compiler/`** — Backend utility for manifest generation (not the user-facing entry point).
- **`profiles/`** — Managed by the wizard; do not edit manually.

## Security & isolation

- Each profile is isolated:
  - Separate identity and credentials.
  - Scoped actions via the Forge skill.
  - Explicit handoffs instead of shared state.

- The Forge skill enforces:
  - What actions profiles can take.
  - Where they can write (paths, APIs, channels).
  - When human confirmation is required.

## Changelog

See [`CHANGELOG.md`](./CHANGELOG.md).
