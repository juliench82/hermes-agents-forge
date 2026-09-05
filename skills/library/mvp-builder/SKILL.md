---
name: mvp-builder
description: Build the smallest demoable increment, then iterate to good
version: 1.0.0
metadata:
  hermes:
    tags: [development, mvp, iteration]
    category: software-development
---

# MVP Builder

## When to Use

You are a developer on a Forge team turning a blueprint into a working
increment. Use this whenever "build the app" is the task — the discipline
is slicing, not coding speed.

## Procedure

1. Define the demo scenario first: the exact 60-second walkthrough the
   user will perform. If you cannot demo it, you cannot ship it.
2. Slice one vertical path through the stack — UI click to database and
   back. No horizontal layers, no scaffolding for features that do not
   exist yet.
3. Implement thin: the happy path works end to end before any edge case.
4. Run it. Fix until the demo path is green with zero errors.
5. Iterate: one improvement per pass, re-run the demo path each time,
   stop at "good enough for the demo" — the user's words define that bar.
6. Commit with a message naming the demo scenario; hand off to QA.

## Pitfalls

- Gold-plating — polish on paths the demo never touches.
- Building horizontal layers first ("the whole API, then the whole UI").
- "Good enough" drift — without the user's quoted bar, you never stop.

## Verification

- The demo scenario runs end to end without errors.
- Every commit message names what it advanced.
- QA received the handoff with the demo path described.
