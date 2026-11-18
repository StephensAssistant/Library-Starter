---
id: SKILL-0206
type: skill
title: Qlik Association and Key-Model Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-24
trigger_phrases: ["diagnose Qlik association gap", "trace unmatched Qlik composite key", "compare legacy replacement key populations"]
links: []
tags: [skill, qlik, snowflake, migration, diagnostics]
---

# Qlik Association and Key-Model Diagnosis

Prove whether available, populated Qlik fields fail to associate because of keys, joins, grain or unmatched populations.

## When to use

Use after SKILL-0175 has proven required source fields and aliases are present, but a Snowflake-backed Qlik output remains blank or null. Route expression evaluation to SKILL-0257 only after the association model is proven.

## Intent-routing contract

This Skill owns association, composite-key, join, grain and unmatched-population diagnosis. It does not own source-field mapping or expression semantics.

## Method

1. Confirm the required fields and aliases are present and populated.
2. Identify the tables, association fields, composite keys, join expectations and grain required by one affected output.
3. Compare legacy and replacement key construction, values, nulls, duplicates and unmatched populations.
4. Locate the earliest association or key-model divergence.
5. Repair only that proven boundary and revalidate the association population.
6. Hand off to SKILL-0257 only when required associations and source rows are proven.

## Benchmark case

A blank coverage measure has populated fields but an unmatched composite key; the key construction is corrected and association coverage is proven before expression evaluation.

## Anti-patterns

- Rechecking source aliases without evidence of a mapping failure.
- Rewriting the measure expression before associations are proven.
- Changing several keys or joins at once.

## Stop

Stop when the required association and key populations are proven or the earliest model divergence is evidenced; then route the next failed boundary explicitly.

## Contextual links

- `SKILL-0031` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
