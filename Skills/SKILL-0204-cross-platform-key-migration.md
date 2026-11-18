---
id: SKILL-0204
type: skill
title: Cross-Platform Key Migration
status: current
created: 2026-09-20
updated: 2026-10-24
trigger_phrases: ["migrate surrogate keys", "snowflake business key join", "cross platform key parity"]
links: []
tags: [skill, sql-server, snowflake, keys, migration]
---

# Cross-Platform Key Migration

Selects and validates compatible keys across legacy and Snowflake platforms.

## When to use

Use when joins currently depend on SQL Server-generated surrogate or composite keys.

## Method

1. Do not assume platform surrogate keys are portable.
2. Identify a validated business/natural key or Snowflake-owned conformed key.
3. Prove uniqueness, null behaviour and cardinality on both sides.
4. Measure unmatched and duplicate populations.
5. Document expected exceptions before replacing the join.

## Benchmark case

Legacy `Variant Key` values differ in Snowflake; use the validated natural variant identity after proving one-to-one cardinality.

## Anti-patterns

- Joining on same-named surrogate keys
- Ignoring duplicate populations
- Choosing a key without orphan analysis

## Stop

Stop when key compatibility and cardinality are proven or key design is unresolved.


## Verified case-comparison boundary — Killingworth, 13 October 2026

Check comparison semantics as well as key names before a cross-platform join. A case-sensitive Snowflake size match can reject a logical legacy key, e.g. King/KING and350ml/350ML. Prove all proposed matches and retain product-type constraints; do not add unrelated trimming or arbitrary fallback. When the dimension contributes only eligibility and no selected attribute, use an EXISTS semijoin with the evidenced case-insensitive comparison: it preserves each source fact and does not pick an ambiguous variant. When attributes are needed, separately prove normalized-key uniqueness before enrichment.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

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
