---
id: SKILL-0230
type: skill
title: dbt Compilation and Macro Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt compile error", "dbt macro failure", "dbt templating error"]
---

# dbt Compilation and Macro Diagnosis

Reusable capability for diagnosing dbt parsing, compilation and macro-expansion failures.

## When to use

Use only when the requested action is diagnosing dbt parsing, compilation and macro-expansion failures. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact project revision, dbt/adapter context, failing invocation, error text and relevant model/macro inputs; use the matching parsed graph and compiled output when available.
2. Inspect exact errors, parsed graph and compiled SQL; isolate quoting, ref and macro expansion before modifying model logic.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the failing parse/compile/expansion boundary, source-to-generated-SQL evidence and bounded correction or unresolved gap; keep downstream data correctness separate from compilation.

## Benchmark case

Malformed generated SQL is traced to a macro argument rather than guessed from the source template.

Boundary design case: Compilation fails before SQL is generated. Retain the exact error and available parse/macro evidence; do not invent compiled SQL or change unrelated transformation logic to obtain a clean run.

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
