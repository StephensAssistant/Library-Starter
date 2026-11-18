---
id: SKILL-0241
type: skill
title: ADF Rerun and Backfill Recovery
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["ADF backfill", "rerun ADF window", "missing ADF date"]
---

# ADF Rerun and Backfill Recovery

Reusable capability for recovering a deterministic ADF window without duplicates or gaps.

## When to use

Use only when the requested action is recovering a deterministic ADF window without duplicates or gaps. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact authorised window/cutoff, source population, sink key/partition, evidenced replay mechanism, prior committed checkpoint and overlapping-run status.
2. Make the requested window and cutoff explicit; pair replay with evidenced idempotent upsert or partition replacement; verify the source contained data. Establish whether another run can write the same window and prevent conflicting replay before changing the sink.
3. Reconcile the replayed keys, rows and agreed metrics at the aligned cutoff, including adjacent periods. Preserve the last committed checkpoint until durable replay and validation succeed; reconcile partial effects before any retry.
4. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
5. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return before/after window and adjacent-period reconciliation, checkpoint state and any partial/unknown effects; identify whether the replay or only its plan was verified.

## Benchmark case

One missing day is replayed exactly and reconciled without affecting adjacent periods.

Boundary design case: A partial replay may have written rows and another run can write the same window. Preserve state, reconcile effects and resolve the conflict before retry; do not assume a failed pipeline wrote nothing.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.


## Contextual links

- `SKILL-0036` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
