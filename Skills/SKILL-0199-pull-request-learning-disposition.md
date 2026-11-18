---
id: SKILL-0199
type: skill
title: Pull-Request Learning Disposition
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["learning disposition", "capture sweep receipt", "already covered learning"]
links: [PLAY-0056]
tags: [skill, library-mechanics, learning, receipts]
---

# Pull-Request Learning Disposition

Records the canonical learning disposition for a staged candidate or PR.

## When to use

Use when a candidate requires `LEARNING-DISPOSITION`, `LEARNING-REF` and capture-sweep evidence.

## Method

1. Choose `captured` only when the canonical owner changed in the staged candidate.
2. Use `already-covered` for an effective existing owner, `task-local` for non-reusable learning, or `n/a` with a specific reason.
3. Provide the governed ID/path or specific reason in `LEARNING-REF`.
4. Set capture-sweep status and concrete evidence.
5. Preserve the exact receipt syntax expected by validation.

## Decision and evidence details

Inspect the current validation contract before forming the receipt; do not guess fields or enum syntax from examples. Compare each disposition/reference with the exact staged diff and effective existing owner, retaining the evidence for already-covered or task-local decisions.

Boundary design case: a useful rule is drafted in chat but absent from the staged owner. Do not mark captured. Record the truthful pending/disposition state using the governing syntax rather than claiming a source change.

## Benchmark case

A reusable rule already enforced by SKILL-0184 records `already-covered` with that ID; it does not claim captured.

## Anti-patterns

- Using captured without a staged owner change
- Vague n/a reasons
- Changing receipt syntax alone

## Stop

Stop when every receipt field is specific, valid and consistent with the staged diff.

