---
id: SKILL-0211
type: skill
title: OpenFlow Source-to-Load Parity Validation
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["validate OpenFlow load", "OpenFlow parity", "OpenFlow row reconciliation"]
---

# OpenFlow Source-to-Load Parity Validation

Reusable capability for proving that an OpenFlow load represents the authoritative source.

## When to use

Use only when the requested action is proving that an OpenFlow load represents the authoritative source. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Compare counts, distinct IDs, date coverage, null and duplicate IDs, parent-child integrity and representative measures; distinguish legitimate zero rows from missing extraction.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Decision and evidence details

Define the source/target population, aligned extraction cutoff, parent/child grain, identity and agreed acceptance/tolerance before comparison. Retain counts and unmatched/duplicate ID populations for each layer, not only totals. Classify timing, unavailable extraction and actual data differences separately.

Boundary design case: the target has zero rows but the source request failed. Report missing extraction rather than legitimate zero activity. A verified empty source window may reconcile to an empty target; unavailable source evidence cannot. Return the earliest evidenced mismatch and affected acceptance condition without rewriting source facts to force equality.

## Benchmark case

Orders roots, children, IDs and date coverage reconcile across the API and Snowflake target.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0032` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
