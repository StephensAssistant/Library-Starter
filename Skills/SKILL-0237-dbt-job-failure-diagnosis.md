---
id: SKILL-0237
type: skill
title: dbt Job Failure Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt job failed", "dbt run_results", "diagnose dbt job"]
---

# dbt Job Failure Diagnosis

Reusable capability for proving the root cause of a failed dbt job.

## When to use

Use only when the requested action is proving the root cause of a failed dbt job. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact failed run, project revision, invocation/environment, logs and run_results.json; ensure the artifacts belong to the same run before comparing recent changes and compiled SQL.
2. Collect run identity, logs and run_results.json; classify infrastructure, compile/code or data/test failure; inspect recent changes and compiled SQL.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the first evidenced failure boundary and classification, supporting/contradicting observations, residual hypotheses and next diagnostic action; distinguish a suspected cause from a proven one.

## Benchmark case

A failing production job is traced to a data contract breach without weakening its protective test.

Boundary design case: A failed production run is paired with run_results.json from another invocation. Report the artifact mismatch and collect matching evidence; do not diagnose from the unrelated successful result.

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
