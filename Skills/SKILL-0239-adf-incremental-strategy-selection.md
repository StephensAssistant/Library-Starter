---
id: SKILL-0239
type: skill
title: ADF Incremental Strategy Selection
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["ADF incremental load", "ADF watermark strategy", "ADF CDC"]
---

# ADF Incremental Strategy Selection

Reusable capability for selecting an ADF delta mechanism from authoritative source behavior.

## When to use

Use only when the requested action is selecting an ADF delta mechanism from authoritative source behavior. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm source update/delete behaviour, available change fields/tokens or file metadata, ordering/freshness evidence and replay requirement before choosing the delta mechanism.
2. Choose watermark, CDC, fixed window, file metadata or full load based on update/delete semantics and replay needs.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the selected mechanism and its evidenced change/delete/replay coverage, rejected alternatives and unresolved source limitations; selection is not implementation proof.

## Benchmark case

A source without a trustworthy change field uses a controlled full load instead of a fragile watermark.

Boundary design case: A timestamp detects inserts but its response to updates and deletes is unknown. Do not declare a complete incremental strategy; investigate those semantics or retain the explicit coverage gap.

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
