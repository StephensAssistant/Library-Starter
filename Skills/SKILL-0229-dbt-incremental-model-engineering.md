---
id: SKILL-0229
type: skill
title: dbt Incremental Model Engineering
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt incremental model", "dbt unique_key", "dbt incremental merge"]
---

# dbt Incremental Model Engineering

Reusable capability for designing replay-safe dbt incremental models.

## When to use

Use only when the requested action is designing replay-safe dbt incremental models. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Define unique key, change boundary, overlap, late arrivals, deletes, deterministic deduplication and full-refresh behavior; prove repeated execution.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

A duplicate-row MERGE failure is fixed by restoring the real grain and deterministic source deduplication.

Boundary design case: A joined source changes while the primary timestamp stays fixed, but no reliable business-change signal is known. Name that coverage gap; do not manufacture one from audit churn or claim repeat-safe change coverage.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Joined-source change coverage — 2026-10-11

Use this technique when joined inputs change without advancing the primary model's selection timestamp.

1. Map each business dependency to affected target keys. Cover inserts, updates, relationship changes/removals, and applicable time-driven eligibility.
2. Prove a reliable source or staging business-change signal and extend the existing candidate selection with the smallest evidenced change. Event-date MAX and generated audit churn are not reliable correction signals.
3. Verify stage replacement/truncation behaviour before relying on change tracking. Do not substitute a broad per-field comparison or full refresh without evidence and the agreed scope.
4. Preserve target grain, surrogate keys, null/deduplication semantics, excluded merge columns, stored intake/creation state, and post-hooks.
5. Validate changed keys and unaffected rows. For historical repair, retain before/after keys and protected columns, require unambiguous source matches, and prove the next normal pipeline run preserves the correction.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

Representative checks: a joined-only update must select the affected key when the primary timestamp is unchanged; an unrelated key must retain protected state. A relationship removal or age-boundary change requires its own demonstrated signal. Zero present mismatches do not prove future change coverage.

Stop when selective change coverage and repeat execution are evidenced, or name the unresolved signal. Documentation capture does not authorise database repair, deployment, or clearing a security hold.

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
