---
id: SKILL-0233
type: skill
title: dbt Warehouse Performance Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt Snowflake performance", "slow dbt model", "profile dbt SQL"]
---

# dbt Warehouse Performance Diagnosis

Reusable capability for diagnosing warehouse performance of generated dbt SQL.

## When to use

Use only when the requested action is diagnosing warehouse performance of generated dbt SQL. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the model and compiled SQL revision, actual query/run identity, representative data and warehouse/workload conditions, and accepted performance baseline.
2. Profile compiled SQL, scans, joins and warehouse workload; separate lineage/orchestration choices from execution performance.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return profile evidence for the dominant execution constraint, a bounded proposed correction and actual comparative checks where authorised; disclose unmeasured improvement.

## Benchmark case

A slow model is improved from its Snowflake query profile, not by replacing ref() with source().

Boundary design case: A slow run has no matching query profile. Report the missing execution evidence and avoid substituting an orchestration/ref-source change for an unproved SQL-performance cause.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0035` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
