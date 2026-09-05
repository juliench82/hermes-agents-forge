---
name: prd-author
description: Turn a raw idea into a scoped, testable requirements doc
version: 1.0.0
metadata:
  hermes:
    tags: [product, requirements, planning]
    category: productivity
---

# PRD Author

## When to Use

You are an analyst or product role on a Forge team and the user (or a
teammate) hands you a raw idea, feature request, or business goal that
needs to become something buildable. Use this before any design or code.

## Procedure

1. Restate the idea in one sentence, quoting the user's own words where
   possible. If you cannot, ask one clarifying question — not five.
2. List the user stories: "As a <who>, I want <what>, so that <why>."
   Three to seven stories; more means the scope is too big.
3. Draw the scope fence: explicitly list what is OUT for this iteration.
   The fence is a deliverable, not an afterthought.
4. For each story, write acceptance criteria a test could check —
   concrete inputs, expected outputs, measurable thresholds.
5. List open questions and assumptions separately. Assumptions are
   decisions made without the user; flag each one for review.
6. Write the PRD to docs/PRD.md in the project repo: one-sentence idea,
   stories, scope fence, acceptance criteria, open questions, assumptions.
7. Hand off to the architect or developer teammate by name (group-room
   @mention or message_agent DM) with a one-line summary and the doc path.

## Pitfalls

- Vague acceptance criteria ("works well", "fast") — rewrite as numbers.
- Scope creep via "while we're here" additions — those go to the fence's
  out-list, not into this iteration.
- Silent assumptions — every assumption gets named and flagged.
- A PRD nobody can test — if QA cannot derive a test from a criterion,
  the criterion is not done.

## Verification

- Every story has at least one checkable acceptance criterion.
- The scope fence lists at least three things explicitly out.
- The handoff names the receiving teammate and the doc path.
