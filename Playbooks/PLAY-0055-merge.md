---
id: PLAY-0055
type: playbook
title: Merge
status: current
created: 2026-09-01
updated: 2026-10-13
owner: the Library owner
trigger_phrases: ["run merge playbook", "merge staging to main", "run merge", "validate and merge"]
links: [PLAY-0006, PLAY-0029, PLAY-0041, PLAY-0044, PLAY-0046, PLAY-0047, PLAY-0056, PLAY-0059]
tags: [playbook, merge, staging, validation, github-actions, governance]
---

# Merge

## Purpose and authority

Enter only under AGENTS.md Library rules 6 and 9: the Library owner's explicit current-conversation merge instruction, or an enabled schedule he explicitly created or approved that specifically names PLAY-0055. Resolve the runtime staging batch when the run begins; authority ends after verified merge, failure or stop and cannot carry to another batch. Then merge one verified staging candidate through protected main. Never write to main directly. The authority is single-use for this staged batch.

## Capability routes

Use only evidence the active environment can mechanically read.

- A local Git worker may inspect live protection and perform the post-merge staging refresh with an expected-old-SHA lease.
- A browser assistant using the Library MCP may read branches, the draft PR, its combined status and check runs; mark the PR ready; invoke GitHub's native PR merge; and verify the merged PR and branch heads.
- If live ruleset inspection is unavailable, say so. Do not claim it was checked. Require the stored ruleset contract, successful exact-head `candidate-ready`, clean PR mergeability and the native protected merge endpoint. Never use a direct branch write to main or any bypass.
- If safe ref-level staging refresh is unavailable, the merge may complete but refresh is a reported reconciliation requirement. Do not imitate force-with-lease with a content rewrite or unconditional branch update.

## Method

1. Read current main, staging and the existing draft staging-to-main PR. Require its head to equal the reviewed candidate SHA, its base to equal current main and its exact-head `candidate-ready` status to be successful. Reuse unchanged valid evidence; do not repeat preparation.
2. Verify every protection signal exposed by the active route:
   - Local route: verify active protected PR, strict current-base required checks, squash only, no force pushes/deletion and no bypass actors.
   - Browser-MCP route: read the stored main-ruleset contract, PR head/base, combined status, check runs and mergeability. If the native merge endpoint reports a protection or policy block, stop; do not bypass it.
3. Update the existing draft PR with a concise description of behavior, verification and applicable independent review for the exact candidate SHA, then mark it ready. Do not open a second release PR.
4. Re-read the PR immediately before merge. Require unchanged head/base, successful `candidate-ready` and clean mergeability. Use GitHub's native squash merge. A changed head/base, conflict, pending/failed status or policy rejection blocks merge; reconcile only on staging.
5. Read the merged PR and current main to verify the squash result.
6. Refresh staging only with a ref operation that atomically requires its current head to equal the reviewed candidate:
   - Local route: `git push origin <verified-main-sha>:refs/heads/staging --force-with-lease=refs/heads/staging:<reviewed-candidate-sha>`.
   - Any route with an equivalent compare-and-swap ref tool may use it and must read back both heads.
   - Browser-MCP without such a tool must leave staging unchanged, report its exact head and the verified main SHA, and mark staging reconciliation required before the next staged write. This is not a failed merge and does not authorize an unsafe refresh.
7. Stop after verified merge and either verified refresh or the precise refresh limitation. Do not create a repair Ticket, recovery PR or rollback automatically.

## Acceptance

PASS requires explicit single-use merge authority, the exact candidate's successful `candidate-ready`, native squash merge, a merged-PR/main read-back and no direct main write. Report staging as either refreshed to verified main or preserved at its pre-merge head pending safe reconciliation. Never claim the second state is clean/refreshed.

The custom merge-command and main-guard recovery workflows are retired. These are the intended protection boundaries. The stored contract does not establish live enforcement; report the actual exposed protection and endpoint evidence and its limits. Expected-head reconciliation must reject concurrent staging movement.


<!-- RELATIONSHIP-EVIDENCE: PLAY-0029--PLAY-0055 | related_to | undirected | authoritative_record | governs explicit recovery merge -->
