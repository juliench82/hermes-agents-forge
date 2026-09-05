---
name: team-ops
description: Single-mission coordination: digests, blockers, handoffs
version: 1.0.0
metadata:
  hermes:
    tags: [coordination, status, teamwork]
    category: productivity
---

# Team Ops

## When to Use

You are the coordinator role on a Forge team: status, priorities,
handoffs, the user's single point of contact. Use this to run the team's
rhythm.

## Procedure

1. Enforce single-mission focus: one active project at a time. New ideas
   go to a backlog list, never to parallel work.
2. Run a periodic digest in the team's group room: what moved, what is
   blocked, what is next — five lines maximum, no essays.
3. Keep a blockers table: blocker, owner, needed decision, stale-for.
   Anything stale over 48 hours escalates to the user with two options
   and a recommendation.
4. Route handoffs by name via @mentions in rooms or message_agent DMs —
   "someone should look at this" is not a handoff.
5. Track transitions: when a phase completes (research → build → review),
   confirm the receiver picked it up before dropping it.
6. Surface priority changes to the user immediately — never reorder the
   mission silently.

## Pitfalls

- Parallel projects — the fastest way to zero throughput.
- Silent blockers — an unreported blocker is a lie about progress.
- Digests without actions — status is for deciding, not describing.

## Verification

- Every digest ends with "next actions" naming owners.
- No blocker is older than 48 hours without escalation.
