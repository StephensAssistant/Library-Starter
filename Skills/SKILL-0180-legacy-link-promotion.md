---
id: SKILL-0180
type: skill
title: Legacy Link Promotion
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["resolve migrated link", "promote legacy id", "migrated_links_pending"]
links: []
tags: [skill, library-mechanics, links, migration]
---

# Legacy Link Promotion

Promotes a legacy pending link only when a live target or approved override exists.

## When to use

Use when `migrated_links_pending` may contain an old ID that now resolves.

## Method

1. Check whether the old ID is live or explicitly mapped in `.github/migration-link-overrides.json`.
2. Let the healer promote qualifying entries and remove the field only when empty.
3. Leave unresolved entries pending.
4. Treat changes limited to links, updated and pending migration links as relationship bookkeeping.

## Decision and evidence details

Retain the pending IDs, live-target or approved-override evidence and healer result. Compare the final links and remaining pending entries against that evidence; an empty pending field is removed only when no unresolved entry remains.

Boundary design case: a similar current title suggests a replacement but no live ID or approved override resolves it. Preserve the pending entry and report the mapping gap; do not hand-edit it away to reduce debt.

## Benchmark case

Use an approved override to promote a legacy link to its verified record. Preserve unresolved neighbouring links.

## Anti-patterns

- Hand-editing the pending list
- Inventing a mapping to clear debt
- Deleting unresolved entries

## Stop

Stop when qualifying entries are promoted and every unresolved ID remains pending.
