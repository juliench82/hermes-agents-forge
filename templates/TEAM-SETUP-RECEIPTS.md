# Team Setup Receipts

> Reusable receipt templates for Team Setup reconciliation. Generated
> during Forge provisioning; replace bracketed values with the verbatim
> receipt content captured from the live Hermes environment.

## Generated-skill reconciliation receipt

Required after any generated local skill is created or written. A generated
skill is considered installed only when the exact fresh inventory shows its
identifier once and the count deltas match. Creation-operation success alone
is never a receipt.

```text
Profile: <target profile>
Pre-write: <N> hub-installed, <N> builtin, <N> local — <N> enabled
Action: created|wrote generated skill <exact generated skill identifier>
Post-write: <N> hub-installed, <N> builtin, <N> local — <N> enabled
Expected delta: +<N> local / +<N> total
Actual delta: +<N> local / +<N> total
Reconciliation: PASS|FAIL
```

Reconciliation procedure:

1. Capture the target profile's pre-write enabled-skill receipt.
2. Create or write the skill.
3. Reload or re-query the target profile's skill registry.
4. Run `hermes -p <profile> skills list --enabled-only`.
5. Verify that the exact generated skill identifier appears exactly once.
6. Verify the local-skill and total-enabled count deltas equal the expected change.
7. Record the pre-write count, action, post-write count, expected delta,
   actual delta, and reconciliation result.
8. If the registry does not reconcile, mark Team Setup incomplete and stop.

## Configuration-key classification record

Required for every changed setting. Classify before writing and record the
classification in the receipts.

```text
Config key: <key>
Classification: Registry-supported | Runtime-supported / CLI-unregistered | Unsupported or stale | Existing non-schema key
Evidence: <standard CLI receipt | source/runtime evidence reference | exact SKIPPED reason>
Write method: standard CLI | --force (approved) | not written
Post-write verification: <`config get` receipt | effective runtime value receipt | SKIPPED>
```

Known registry-drift keys:

- `agent.reasoning_effort` — runtime-supported/CLI-unregistered only if the
  installed runtime source and resolver demonstrate it; a forced write
  requires a post-write effective runtime receipt.
- `skills.disabled` — runtime-supported/CLI-unregistered only if the active
  skill loader reads it; verify the actual enabled skill inventory after the
  change.
- `delegation.fanout` — never modified merely because it exists in YAML;
  modify only if both the current schema and runtime reader confirm it,
  otherwise record `SKIPPED`.
- `moa.enabled` — never used as evidence that MoA is active or inactive
  unless the installed version's runtime actually uses it; verify the active
  supported MoA selector/preset state instead.

## Completion condition

Every generated-skill write reconciles; every changed configuration key is
classified with evidence; any mismatch marks Team Setup incomplete and stops.