---
id: SKILL-0035
type: skill
title: dbt Model Materialisation Selection
status: current
created: 2026-09-16
updated: 2026-10-31
links: []
tags: [skill, dbt, materialisation]
trigger_phrases: ["dbt materialization", "dbt view or table", "dbt ephemeral model", "choose dbt model type"]
---

# dbt Model Materialisation Selection

Reusable capability for selecting the materialisation for one dbt model.

## When to use

Use only when the requested action is selecting the materialisation for one dbt model. Use the independent action-specific Skills for adjacent validation, recovery, testing, performance, rehearsal or delivery work.

## Intent-routing contract

This Skill owns this one action from authoritative inputs to its evidenced result. It does not absorb adjacent jobs merely because they use the same platform or subject.

## Method

1. Confirm authoritative inputs, scope and success condition.
2. State model grain, key, freshness, reuse and workload; compare view, table, incremental and ephemeral behavior; document the selected materialisation and reassessment condition.
3. Preserve evidence, assumptions, result and any unresolved material gap.


### Application checks

Use the supplied model and workload contract to record what each candidate would recompute, persist or inline, and how that meets freshness and reuse. Evaluate incremental only against verified key and update behaviour; do not supply an imagined incremental predicate. Return the selected materialisation, rejected alternatives with the deciding evidence, and the condition that would reopen the choice. Unknown workload or update semantics remain an explicit selection gap.

## Evidence expected

Retain the inputs, checks, chosen result, source/date context and any condition that requires reassessment.

## Benchmark case

A frequently reused transformation moves from view to table only after its workload and freshness contract justify persistence.

Missing-input design case: reuse is known but required freshness and incremental update semantics are not. Record which alternatives remain unevaluable and the missing contracts; do not select incremental merely because the source is large or treat selection as a deployment.

## Anti-patterns

- Expanding this Skill into another action because the subject is similar.
- Treating tool success or polished output as verified evidence.
- Proceeding through an unresolved material input or authority gap.

## Stop

Stop when the authoritative input or success condition is unknown. Route the next distinct action to its own Skill.

## Contextual links

- `SKILL-0228` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0229` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0230` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0231` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0232` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0233` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0234` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0235` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0236` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0237` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 10 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
