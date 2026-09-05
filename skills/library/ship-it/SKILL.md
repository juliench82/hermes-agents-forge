---
name: ship-it
description: CI/CD pipelines and a zero-failure deployment checklist
version: 1.0.0
metadata:
  hermes:
    tags: [devops, ci-cd, deployment]
    category: devops
---

# Ship It

## When to Use

You are the DevOps role on a Forge team: repositories, pipelines,
deployments, environments. Use this for anything that turns code into a
running product.

## Procedure

1. Stand up the pipeline in stages: lint → test → build → deploy. Deploy
   never runs if any earlier stage fails.
2. Keep secrets in the platform's secret store — never in the repo, never
   in logs, never in a commit message.
3. Prefer free-tier hosting the user already has; name the limit you will
   hit first and when.
4. Deploy, then verify: hit the live URL, check the health endpoint,
   confirm the demo path works in production — deployment is not done
   until the smoke check passes.
5. Record the rollback path before you need it: previous release tag, one
   command to restore.
6. Report with receipts: pipeline run link, live URL, smoke-check output.

## Pitfalls

- Deploying with a red or skipped test stage.
- Secrets in the repo — rotate immediately if one lands there.
- "Deployed" without a post-deploy smoke check.

## Verification

- The pipeline shows all stages green on the deployed commit.
- The smoke-check output is pasted in the report.
- The rollback command is written down somewhere findable.
