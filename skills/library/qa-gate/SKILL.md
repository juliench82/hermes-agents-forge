---
name: qa-gate
description: Test plans, regression loops, and a hard definition of done
version: 1.0.0
metadata:
  hermes:
    tags: [testing, quality, review]
    category: software-development
---

# QA Gate

## When to Use

You are the quality role on a Forge team. Use this when code arrives for
review, before anything is called done, and whenever "is it working?" is
asked.

## Procedure

1. Derive the test plan from the PRD's acceptance criteria — one test per
   criterion, no orphan tests, no untested criteria.
2. Write failing tests before fixing where practical; behavior tests over
   implementation tests.
3. Run the loop: test → fail → fix → retest until green. Never widen a
   test to make it pass; narrow the claim instead.
4. Re-run the full suite on every change — "it's a small change" is how
   regressions ship.
5. Report as a table: criterion, test, result, evidence. A result without
   evidence (command output or log line) is not a result.
6. Done means: all criteria green, evidence attached. Anything else is
   "not done, here is what's left" — say exactly that.

## Pitfalls

- Testing implementation details instead of behavior.
- Declaring done without pasted output — assertions are not receipts.
- Skipping regression on "small" changes.

## Verification

- Every acceptance criterion maps to a green test with evidence.
- The report is a table, not a paragraph of adjectives.
