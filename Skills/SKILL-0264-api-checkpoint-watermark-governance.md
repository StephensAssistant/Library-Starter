---
id: SKILL-0264
type: skill
title: API Checkpoint and Watermark Governance
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0054, SKILL-0056, SKILL-0057, SKILL-0058]
tags: [skill, api, checkpoint, watermark, incremental-extraction]
trigger_phrases: ["govern an API extraction checkpoint", "choose an incremental API watermark", "advance an extraction high watermark"]
---

# SKILL-0264 — API Checkpoint and Watermark Governance

## Purpose

Define, persist and advance an authoritative API extraction checkpoint without creating gaps or silently skipping late changes.

## When to use

Use when an incremental extract needs durable continuation across runs. Do not use for page traversal inside one run or for validating the extracted population.

## Method

1. Identify the source field or token, its ordering guarantees, timezone, precision, mutability and delete semantics.
2. Prove whether the candidate is monotonic and sufficiently unique; add a stable tie-breaker when timestamps can repeat.
3. Define inclusive/exclusive boundaries, overlap or lookback policy and late-arrival handling.
4. Read the last committed checkpoint before extraction but do not advance it during unconfirmed work.
5. Persist a new checkpoint only after the covered population is durably stored and its completion evidence passes. Prevent a concurrent or stale run from overwriting the authoritative checkpoint using the verified persistence mechanism; reconcile any conflict or ambiguous update before retry. Never treat a failed checkpoint write as proof that the stored value is unchanged.
6. Retain run, old-value, new-value, covered window and recovery evidence.
7. On failure, establish the last committed checkpoint from durable evidence before replay. Reuse that confirmed position and the evidenced idempotent replay contract; an ambiguous checkpoint write must first be reconciled.

## Benchmark case

Several records share the same second-level `updated_at` value and one arrives late. A passing design uses timestamp plus stable ID, an evidenced lookback, and advances the checkpoint only after the full window is stored, preventing both gaps and duplicates.

Boundary design case: Checkpoint persistence times out after the sink committed. Read the stored checkpoint and durable sink evidence before replay; do not assume the prior value survived merely because the call failed.

## Anti-patterns

- Manufacturing a watermark from ingestion time.
- Assuming a mutable or non-monotonic field is safe.
- Advancing state before durable completion.
- Using an exclusive timestamp boundary without a tie-breaker.
- Ignoring deletes or late-arriving changes.

## Stop

Stop when checkpoint semantics, persistence, advancement and replay are proven, or when monotonicity, precision, tie-breaking, deletes or late-arrival behaviour remain unresolved.

