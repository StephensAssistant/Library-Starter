---
id: SKILL-0095
type: skill
title: Analytical SQL Transformation Authoring
status: current
created: 2026-09-20
updated: 2026-10-21
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047]
tags: [data-modelling, sql]
trigger_phrases: ["write analytical SQL", "author a warehouse transformation", "create deterministic transformation SQL"]
---

# SKILL-0095 — Analytical SQL Transformation Authoring

## Purpose

Author set-based analytical SQL that implements an already-defined grain and business rule safely.

## When to use

Use for: write analytical SQL; author a warehouse transformation; create deterministic transformation SQL.

## Method

1. Confirm source/target schemas, dialect, grain, keys and expected outputs.
2. Use explicit columns, types, timezones and deterministic ordering where needed.
3. Define incremental boundaries and idempotent behaviour.
4. Preserve consumer aliases and contracts.
5. Attach focused validation queries for material populations and measures.

## Benchmark case

Write a Snowflake transformation from supplied schemas that preserves output aliases, handles timezone explicitly and can rerun without duplication.

## Anti-patterns

- Inventing tables or columns.
- Using SELECT star in a governed contract.
- Mixing model design uncertainty into executable SQL.

## Stop

Stop with implementable SQL and validation evidence requirements.

## Verified Snowflake recovery authoring lessons — 4 October 2026

Verify the following with a bounded owner-authorised test and record the results:

- A RESULTSET consumed by a FOR loop was reused in a second FOR loop: the first made seven iterations and the second made zero. Use one pass or obtain a fresh RESULTSET. Before reporting PREPARED, verify expected processed populations and capture cardinality; an empty capture is not success merely because no exception occurred. The single-pass repair staged 557,059 expected roots.
- Inventory accepted permanent recovery tables/views and historical routes before assessing missing IDs. Omitting CUSTOMER_METAFIELD_RECOVERY overstated a gap as 4,524,770; including the accepted route reduced it to 2,560. Historical ID presence and latest consumer visibility are different evidence contracts.
- When a child source lacks a shop-ID column, verify scope through its parent ID against an explicitly shop-scoped parent population, report unresolved owner scope, and stop publication of unscoped records. Do not use missing CREATEDAT as an ID-assessment blocker.
- Preserve complete compound GID suffixes. InventoryLevel identities include inventory_item_id query components; do not strip them down to a shared numeric level/location component.
- Preserve native snapshots before transforming split typed values. The accepted metafield conversion selects exactly one non-null VALUE/VALUE__ST/VALUE__IT/VALUE__VA channel, converts verified integers to strings and JSON objects to JSON text, preserves JSON nulls/absent fields, and leaves unknown source types un-imputed. Never cast a JSON null into the literal string "null" as a business value.
- Before publishing Transactions, prepare complete source-backed parent Order snapshots with all related Transactions/Refunds. Validate source-to-mapped identity/uniqueness, all contracted business fields, timestamps, and exact related-array membership. A nonempty mapped table or presence of target IDs alone cannot validate a partial replay.
- Append recovery snapshots with deterministic receipts and explicit provenance; verify actual target payload/receipt equality before atomic commit. Keep full history/latest-value/nested-field/consumer parity and operation acceptance separate from historical ID retention.

Authority boundary: these techniques do not grant production changes, source edits, resets, truncations, grants, scheduling or cleanup. Reuse accepted evidence and run only checks material to a new change or diagnosed failure.


## Verified absent-key historical enrichment — 4 October 2026 evening

Trigger: a retained source has historical fields omitted by a replacement capture, and existing RAW VARIANT records should be enriched without replacing snapshots.

1. Enumerate every accepted current/history/permanent recovery receiver before declaring a source ID absent. Customer current-only comparison reported 2,005,785 absent IDs; corrected union found every assessed ID/version and verified 2,542,374 physical updates per field. A failed receipt-format join is also not a data gap.
2. Define the historical date field and cutoff explicitly. Match stable ID and source version, and for nested entities also match their ID and reject a different known nested version. Do not overlay older values onto a newer retained snapshot.
3. Freeze/deduplicate source ID/version values and block conflicting values at that same grain. Preserve native Boolean/VARIANT/object/array values and explicit JSON null. ANY_VALUE is safe only after same-grain value conflicts are rejected; it is not a rule for picking a preferred source version.
4. Fill absent keys only when that is the authorised contract. Existing non-null, JSON-null and empty-array keys are preserved; zero candidates proves only no eligible absent keys, not existing-value parity. An absent source property differs from an explicit source null or a missing optional nested entity; record these separately before considering an API gap.
5. Preserve every other payload value and all operating metadata. For nested insertion, validate the entire original record by removing the inserted child key and provenance marker and reconstructing the old parent object. Do not weaken this into ID/count-only acceptance.
6. Stage candidates once, publish with exact old-payload and metadata guards in one transaction, and perform one consolidated value/preservation verification before commit. Record physical affected rows separately from distinct staged records; six duplicate physical copies were all verified in Customer receipts and did not authorise duplicate deletion.
7. For bulk children, bind the source parent version using the captured loader/publication contract. Stitch receipt ID_KEY is numeric although payload IDs are GIDs. The initial Checkout title script used full GIDs in receipt comparisons and falsely reported all 17,727 children unbound; correcting all repeated scans to the numeric suffix produced zero bound-target/version gaps. Preserve compound identities in other domains; this numeric-suffix rule is specific to the evidenced receipt contract.
8. Clean unique session-temporary source/scope/stage objects on success/error without creating permanent test machinery. Preserve original error and transaction status. Cancellation does not prove rollback or undo committed work; check the stopped run's actual state before asserting completion.

Representative evidence: five Customer fields each 2,542,374 verified updates; Variant measurement 299,771; seven media properties each 465; corrected Checkout title/components 17,727 bound versions with no eligible absent keys. All accepted publication receipts returned zero conflicts/preservation violations and no source calls/watermark/schedule/permanent changes. These facts are scoped enrichment evidence, not full replacement parity.

Authority boundary: no source API recovery, schema redesign, duplicate cleanup, task changes, ownership changes or decommissioning is authorised by this technique. Existing acceptance evidence should not be rerun without a material change/failure.



## Worked Snowflake wrapper/snapshot constraints —15October2026


- Outer and embedded CTEs both named ORDERS_AS_LOADED caused invalid Recursive CTE. Renaming only the wrapper/consumer resolved compilation and final6-component Qlik reconciliation passed.
- SET name = literal || UUID_STRING() returned Unsupported feature assignment from non-constant source expression in the actual worksheet. Fixed session temporary names without SET/UUID generation executed. Do not generalise this to all Snowflake scripting variable mechanisms.
- Unchanged sales expressions do not prove identical selected rows under tied QUALIFY ordering. Capture one baseline for preservation testing, retain the selector risk separately, and never declare a failed aggregate comparison passed.
- Preserve aliases, signed values, NULL semantics, exact additions, zero-denominator fallback and date scope. Unknown VAT values remain NULL, not invented.

No grants, permanent diagnostic objects, source mutation, deployment or candidate action are authorised by these examples.



## Verified same-view scope patch and source capture — 21 October 2026


- An unexpected current view structure or mismatched definition guard is a stop with no mutation, not a reason to remove the guard. Obtain the actual GET_DDL/schema and make the next patch from that deployed input.
- Keep source-preserving wrappers bounded and explicit. This patch checked the original 35-column contract, retained its deployed body, appended two scoped-output fields, rechecked the captured definition and used COPY GRANTS under the verified owner. The resulting 37-column guard correctly makes reapplying the historical transition invalid.
- Separate aggregate steps when source-column names clash with summary aliases; do not put non-grouped opening/closing source values into an aggregate projection. Preserve the complete nested SELECT rather than cutting at a first SELECT token, which caused the earlier EOF failure.
- Archive both the actual applied transition and a complete source definition. A full source assembled from a supplied pre-change GET_DDL and that patch must be labelled reconstructed, not an exact-byte post-change export; compare retained parsed SELECTs and do not invent a deployed DDL hash.

The special source-preserving use of an existing output star here is not permission for unknown-schema SELECT star in new governed transformations. This scoped example adds no core-method, trigger, grant, runtime or merge authority.
