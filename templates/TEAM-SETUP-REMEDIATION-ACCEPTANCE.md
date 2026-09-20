# Team Setup Remediation — Acceptance Fixture

> Manual acceptance cases for the Forge remediation work (workflow handoff
> safety, receipt reconciliation, tool policy, and content preservation).
> Execute each scenario against a fresh Team Setup run and record the
> actual result next to the required expected result.

## Acceptance cases

| Scenario | Required expected result |
|---|---|
| External skill identified in original approval plan | Install allowed only after actual scan outcome is recorded |
| New external skill gap after approval | Stop, present amendment payload, wait for explicit approval |
| External skill reports env/secret access or unpinned install | Stop for explicit founder decision |
| Dangerous scan verdict | Reject; never force |
| Dispatcher supports only assignee and idempotency | Local-only TEAM.md handoff; no Kanban kickoff card |
| Dispatcher enforces coordinator-only/non-execution state | Optional enforced control-plane card; exact state receipt |
| Generated coordinator skill | Post-write enabled inventory shows exact +1 local/+1 total delta |
| Skills count mismatch | Team Setup stays incomplete |
| Runtime-read/CLI-unregistered config key | Source/runtime proof + forced write + effective-value receipt |
| Unknown YAML key | SKIPPED; no forced write |
| Forge-managed artifact update | Builtin file tool used; no shell/generic-code content mutation |
| Modified repository documentation file | Full pre-edit content retrieved; no unapproved deletion |
| CHANGELOG.md update | New entry appended without altering historical entries |
| Worker creates next-stage card on completion | Next card exists with `--parent` link, artifact paths, and acceptance criteria; chain advances via dispatcher without coordinator action |
| Decision bot resolves a decision card (human source) | Typed `decision_response` recorded verbatim; routing applied (`promote` / `request-changes` / `block`) |
| Decision source unreachable | Decision bot escalates to the customer; **no approval is invented** |
| Jev present in the provider lane | Decision-contract payload is identical; Jev usable as a drop-in source only after customer approval |
| Decision-contract exchange composed by the provisioning agent (not the decision-bot profile) | Reject; the exchange must be resolved by the decision-bot profile itself |
| Placeholder/fake timestamp in a decision response | Reject; real capture timestamp required |
| Host-derived founder name in personas, contracts, or records | Reject; role label only ("the founder") — artifacts must be machine-independent |
| Worker config receipt shows top-level `moa.enabled` or a hand-edited profile `config.yaml` | Reject; must show `moa.presets.default.enabled` set via `hermes config set -p` and verified with `hermes config get` |
| `team_record` path in receipts differs from the resolved `$HERMES_HOME` | Reject; receipts must carry the resolved actual path |
| Human-source decision card created `ready` / auto-spawned headless by the dispatcher | Reject; must be dispatcher-exempt (`blocked`) and resolved in the customer's live channel |
| `sdlc-review` disabled on a profile that owns `review`-state cards | Reject; the dispatcher's review lane requires it — spawn crashes with `Unknown skill(s): sdlc-review` |
| Team larger than the desktop pool default with no pool-capacity receipt | Reject; `maxBackends`/`idleMs` must be recorded with the config receipts (or `SKIPPED` with reason for headless deploys) |

## File Preservation Report

| File | Pre-change SHA | Post-change SHA | Additions | Deletions | Deletion explanation |
|---|---|---|---:|---:|---|
| `[path]` | `[SHA]` | `[SHA]` | `[n]` | `[n]` | `none` |

Completion condition:

- Every modified existing file was read in full before editing.
- Every deletion is explicitly listed, justified, and separately approved.
- CHANGELOG.md was updated append-only.
- A file rebuilt from partial, inferred, cached, or older content fails acceptance.

## Note on scope

This fixture describes manual acceptance for the remediation branch. It
does not modify application code; this is a documentation/skills
repository.
