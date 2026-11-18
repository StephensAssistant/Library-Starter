---
id: SKILL-0240
type: skill
title: ADF Checkpoint Governance
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["advance ADF watermark", "reset ADF checkpoint", "ADF checkpoint"]
---

# ADF Checkpoint Governance

Reusable capability for governing when an ADF watermark or checkpoint may advance.

## When to use

Use only when the requested action is governing when an ADF watermark or checkpoint may advance. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Define the durable success boundary and update checkpoint only after it; preserve evidence for resets and recovery. Bind each proposed advancement to its run identity, prior checkpoint, bounded source population and committed sink evidence.
3. Define ownership of checkpoint advancement across overlapping runs and a guarded state transition that rejects a stale prior checkpoint. Where sink commit and checkpoint update are separate, specify replay-safe reconciliation for failure between them. Treat an unknown commit outcome as unresolved until durable sink evidence is checked; do not advance or blindly rerun.
4. Require explicit authorised scope and before/after evidence for a reset; preserve the prior position and prove no gap or unintended replay beyond that scope. Verify failure before sink commit, failure after sink commit before advancement, competing advancement and repeat recovery against expected target/checkpoint state; hand unresolved state to the pipeline owner.
5. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
6. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

The watermark advances after sink merge completion, not after source extraction.

Boundary design case: A second run has already advanced the checkpoint. Reject a stale prior-position update and reconcile the run/sink evidence; do not overwrite the newer position or reset state to make the retry succeed.

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
