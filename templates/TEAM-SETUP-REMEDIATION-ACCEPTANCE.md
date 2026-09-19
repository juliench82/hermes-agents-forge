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
