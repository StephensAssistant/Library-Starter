---
id: SKILL-0026
type: skill
title: Final Candidate Scope Assembly
status: current
created: 2026-09-05
updated: 2026-10-31
owner: Library owner

trigger_phrases: [commit scope, final candidate completeness, what goes in this update]
links: [PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, commit, staging]
---

# Final Candidate Scope Assembly

Assembles related authored changes into one complete staged candidate.

## When to use

Use after an authorised Library update is defined and before candidate validation or merge.

## Method

1. Keep each author commit limited to related work; intermediate commits may be incomplete.
2. Require the final candidate to include all canonical source and mandatory companions.
3. Include the proportionate plan used under PLAY-0049/PLAY-0050: inline Work plan for small work, or the one linked companion for substantial sequencing/dependencies. Preserve existing used plan history and exact parent/backlink integrity.
4. Include both sides of every reciprocal link.
5. Include native and Markdown companions plus consumed IDs for new Artifacts. For a changed native with a hash claim, use the checker-recognised `Artifact SHA-256 of the raw stored UTF-8 bytes:` label once for its current raw-byte hash. Retain older values under clearly historical labels that do not match the current-hash pattern. Run `check_artifact_companion_hashes` from the current `.github/scripts/run_changed_validation.py` against the actual source/companion bytes before claiming byte agreement; documentary matching alone is insufficient.
6. Include consumed reservations, intent routing and benchmark cases for new Skills or Playbooks.
7. Exclude workflow-owned generated views and unrelated opportunistic fixes.
8. Use concise commit messages that state what changed and why.
9. Route branch verification, concurrency, rewrites, reconciliation, staged verification and authority checks to their focused Skills.

## Benchmark case

A new Skill candidate contains its source file, consumed reservation, precise intent-routing entry and benchmark, without unrelated cleanup or hand-edited generated indexes.

Boundary design case: the new Skill source exists but its reservation consumption or required routing companion is missing. Return an incomplete candidate with the exact missing item; do not describe source save as candidate readiness or start validation under assembly authority.

## Anti-patterns

- Treating an intermediate commit as the complete candidate
- Bundling unrelated fixes
- Receipt-only commits
- Hand-authoring workflow-owned generated views

## Stop

Stop when the final authored candidate is complete for its declared scope and ready for governed reconciliation.


