# runtime/

This directory is the **onboarding engine** for HERMES Agents — Forge.

## Entry point

```bash
python -m runtime.onboarding_wizard
```

## Modules

- `onboarding_wizard.py` — Interview + team design orchestration.
- `dynamic_profiles.py` — Profile creation and configuration.
- `live_provisioner.py` — Wiring profiles into workflows.
- `__init__.py` — Package marker.

## Usage

1. User runs `python -m runtime.onboarding_wizard`.
2. Wizard interviews the user, proposes a team, and (on confirmation) provisions isolated bot-mode profiles.
3. Profiles are created under `profiles/`; a sample workflow is created under `onboarding/workflows/`.

## Notes

- Do not manually edit files under `profiles/`; use `--refine` to adjust teams.
- The `compiler/` directory is a backend utility for manifest generation, not part of the user-facing flow.