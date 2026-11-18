---
id: SKILL-0185
type: skill
title: Concurrent Staging Write Guard
status: current
created: 2026-09-20
updated: 2026-10-16
owner: Library owner

trigger_phrases: ["staging head changed", "concurrent library write", "fast forward staging"]
links: [PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, git, concurrency]
---

# Concurrent Staging Write Guard

Prevents one session from overwriting another staging update.

## When to use

Use immediately before each staging write in a shared working period.

## Method

1. Read the current staging head.
2. Compare it with the head used to prepare the change.
3. If the head or any target moved, preserve the concurrent work and stop this write; do not overwrite, reconcile or absorb it. Only an already-authorised PLAY-0059/PLAY-0056 run may apply its explicit bounded stabilisation or workflow-proven reconciliation exception.
4. Push only a fast-forward child of the verified head.
5. Never overwrite or force past another session’s work.

## Benchmark case

Staging advances after drafting a file; the editor preserves the advance and stops the stale write. An authorised Commit route may proceed only under its specific stabilisation exception.

## Anti-patterns

- Assuming the earlier SHA remains current
- Force-updating staging
- Discarding concurrent changes

## Stop

Stop when the write is based on the current head or when a conflict requires owner direction.



## Guarded object publication — 16 October 2026

For a multi-file source pack, a current head read alone is not an atomic lease. Verify the exact target bytes/blob SHAs against the inspected staging parent and preserve its base tree; construct the reviewed tree and one commit whose sole parent is that inspected head. Immediately re-read targets and both heads, then publish only to explicitly named staging with the same expected head and force=false. The expected-head and non-force checks must reject a moved/divergent branch; do not refresh the expected head and reuse an old proposal. Verify resulting parent/diff and every changed source by exact readback. An unavailable or unverified guarded primitive blocks publication; this method grants no new Commit-playbook, candidate or merge authority.

FLOW-0001 qualification exercised the connected expected-head primitive with a mismatched-head negative call (generic error, no branch movement), a correct-head no-op and then the actual reviewed three-file repair from cc28f2233790db952dbdddb3dc5378da9b473472 to0d8f7e189a225238696702fc644e86ddff97d2cf, force=false with the pinned expected parent; all three readbacks matched. The negative error did not name the lease cause, so its internal diagnosis remains limited. This evidence is scoped to that adapter/transaction, not proof every API provides a lease or every possible concurrent race was tested.

