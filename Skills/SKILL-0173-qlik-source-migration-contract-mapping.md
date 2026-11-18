---
id: SKILL-0173
type: skill
title: Qlik Source Migration Contract Mapping
status: current
created: 2026-09-20
updated: 2026-10-12
owner: Library owner

links: []
tags: [skill, qlik, migration, contracts]
trigger_phrases: [map qlik migration contract, replace qlik source contract, document qlik source replacement]
---

# Qlik Source Migration Contract Mapping

Map a legacy Qlik source section to a replacement while preserving required consumer contracts.

## When to use

Use for SQL Server-to-Snowflake, API replacement, QVD retirement or another Qlik source migration.

## Method

1. Identify required downstream outputs and contracts.
2. Map each output to a verified target field or transformation.
3. Preserve aliases, table names, variables and QVD/store contracts unless change is authorised.
4. Prove cross-platform key compatibility before reusing surrogate keys.
5. Use an explicit typed null only when its business effect is understood and accepted.
6. Distinguish a temporary legacy-authoritative bridge from native migration.
7. Assign retain, replace, bridge, null or remove disposition to each source section.

## Benchmark case

A Snowflake replacement lacks one legacy field. A passing application preserves the alias with an accepted typed null or records a gap rather than silently dropping it.

## Anti-patterns

- Reusing surrogate keys without proof.
- Calling a Snowflake-hosted legacy bridge native.
- Changing consumer contracts incidentally.

## Stop

Stop with an actionable disposition and mapped contract for every assessed section.

## Amount and invoice meaning before legacy replication — 12 October 2026

Trigger: migration evidence proves the legacy build inflates or drops business values. Preserve intended population/consumer contracts, not confirmed defects; obtain source-backed disposition before changing metric meaning. Record the original and corrected formula, representative source evidence and limits.

Do not infer unit-versus-line money from a column name. Trace the producer/raw field or verify an actual source order with quantity, unit amount and line total. Digital Analytics FEN12231418 shows quantity2 at80, total160; its field called LINE_GROSS_UNIT_PRICE is160. Multiplying again yields320. For a partial cancellation, proportional allocation requires an accepted original-quantity/line-value basis and explicit invalid-input policy; a full-cancellation screenshot does not verify every partial line.

Invoice presence, unique reference/date and fully invoiced quantity are separate claims. Keep facts at source grain; represent multiple references without selecting an arbitrary latest record or allocating sales through order/SKU alone. FEN10637650 has conflicting D365/source quantities, so multi-invoice is not automatically legitimate split fulfillment.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.
