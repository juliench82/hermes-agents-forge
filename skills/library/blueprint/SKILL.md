---
name: blueprint
description: Design technical blueprints: stack, data model, repo layout
version: 1.0.0
metadata:
  hermes:
    tags: [architecture, planning, software]
    category: software-development
---

# Blueprint

## When to Use

You are an architect or technical lead on a Forge team and a requirements
doc or idea needs to become a buildable plan — before any code is written.

## Procedure

1. State the constraints first: budget ceiling (free-tier?), hosting
   limits, the user's own words for what "done" means. Constraints are
   inputs, not afterthoughts.
2. Pick the stack as a table: layer, choice, why, free-tier limit. Every
   row names the limit — a stack with unnamed limits is not a decision.
3. Define the data model: entities, relations, and the one query that
   must stay fast.
4. Define the repo layout and the CI/CD shape the developer will inherit.
5. Name the top three things that will break and the plan for each.
6. Write it as a one-page ADR (decision + alternatives + why) to
   docs/ARCHITECTURE.md and hand off to the developer by name.

## Pitfalls

- Over-architecting — if it fits one service and one database, it gets
  one service and one database.
- Paid-tier creep — any cost-bearing choice needs the user's explicit
  sign-off, in writing, before it enters the blueprint.
- Blueprints without failure modes — a plan that cannot name what breaks
  has not been thought through.

## Verification

- Every stack row names its free-tier limit or has user sign-off.
- The top-three failure modes each have a mitigation.
- The developer teammate is named in the handoff.
