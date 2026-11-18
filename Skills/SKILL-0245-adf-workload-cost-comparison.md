---
id: SKILL-0245
type: skill
title: ADF Workload Cost Comparison
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["ADF full versus incremental cost", "ADF pipeline cost", "integration runtime cost"]
---

# ADF Workload Cost Comparison

Reusable capability for comparing ADF movement strategies using representative workload cost.

## When to use

Use only when the requested action is comparing ADF movement strategies using representative workload cost. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the full/delta candidates, equivalent source population, freshness/recovery requirements, representative period, runtime settings and authoritative charging basis.
2. Measure full and delta runtimes, integration-runtime use, activity volume and operational complexity; avoid fixed saving claims.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return measured runtime, integration-runtime use, activity volume and operational-effort comparison with assumptions and exclusions; do not claim a saving from an incomplete or differently scoped workload.

## Benchmark case

Incremental loading is retained only when measured total effort and cost beat a reliable full load.

Boundary design case: A delta pilot excludes backfill/recovery effort while the full-load baseline includes it. Disclose the mismatch and withhold a total-cost saving claim until comparable evidence exists.

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
