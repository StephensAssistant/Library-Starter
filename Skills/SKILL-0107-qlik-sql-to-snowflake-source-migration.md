---
id: SKILL-0107
type: skill
title: Qlik SQL-to-Snowflake Source Migration
status: current
created: 2026-09-20
updated: 2026-10-15
links: [SKILL-0175]
tags: [qlik, migration, snowflake]
trigger_phrases: ["repoint Qlik to Snowflake", "Qlik SQL Server migration", "Qlik source conversion", "Qlik Snowflake replacement", "Qlik Snowflake field casing"]
---

# SKILL-0107 — Qlik SQL-to-Snowflake Source Migration

## Purpose

Replace a Qlik app's SQL Server or legacy QVD source with Snowflake while preserving accepted front-end behaviour.

## Intent routing contract

Activate for repoint Qlik to Snowflake, Qlik SQL Server migration, Qlik source conversion, Qlik Snowflake replacement, Snowflake connector field-casing work or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Read the original working load section, source query, field aliases, joins, transformations, table order, execution control flow and consumer contract. For the initial SQL Server-to-Snowflake source-only route, work in a duplicated development app and leave production untouched until authorised promotion; retain the existing Qlik transformations without introducing the later Sigma reporting architecture.
2. Separate source replacement from business-logic redesign unless explicitly authorised. Preserve the original Qlik-facing table names, field names, aliases, QVD names, section order, filters, joins, aggregation and stop conditions unless evidence requires a scoped correction.
3. Treat the Snowflake-to-Qlik connector boundary as a mandatory two-stage contract:
   - Snowflake connector output identifiers arrive in Qlik as uppercase, including quoted mixed-case SQL aliases.
   - Give a SQL expression an alias when the expression, aggregation or source-name change requires a stable output name; SQL alias casing alone does not preserve the Qlik field contract.
   - Place a Qlik preceding `LOAD` immediately above every Snowflake `SQL SELECT`.
   - In that preceding `LOAD`, consume every returned connector field using its uppercase name and explicitly alias it to the exact retained Qlik-facing name, including spaces, punctuation, underscores, deliberate misspellings and case.
   - Apply the rule to direct columns and derived fields alike. Do not omit fields merely because their Snowflake SQL aliases visually match the required Qlik names.
4. Use the explicit pattern below:

   ```qlik
   TargetTable:
   LOAD
       [ORDERNUMBER] AS [OrderNumber],
       [LINE ADJUSTED AMOUNT] AS [Line Adjusted Amount],
       [PAYMENT GATWAY] AS [Payment Gatway];

   SQL
   SELECT
       ORDER_NUMBER AS "OrderNumber",
       SUM(LINE_AMOUNT) AS "Line Adjusted Amount",
       GATEWAY AS "Payment Gatway"
   FROM REPORTING_PROD.EXAMPLE
   GROUP BY ORDER_NUMBER, GATEWAY;
   ```

   The connector exposes `ORDERNUMBER`, `LINE ADJUSTED AMOUNT` and `PAYMENT GATWAY`; only the preceding `LOAD` restores the exact downstream field names.
5. Use proven portable business keys; do not carry SQL Server surrogate keys without cross-platform evidence.
6. Convert one logical section at a time. Once the required columns, joins, logic and connector-boundary mapping are established, install the like-for-like development replacement and use reload/front-end evidence to isolate specific residual defects; do not repeatedly reopen completed source-discovery chains or demand bulk result exports.
7. For a multi-section app, maintain a section ledger with one explicit status per section: `accepted`, `validated at stated layer`, `unvalidated` or `blocked`. Record each section's source/filter/join/key/grain/aggregation contract, evidence and cutoff, residual gap and next action. Freeze only independently accepted sections while diagnosing another section, unless requirements change or contrary evidence appears. Restart each unvalidated or blocked section from its retained contract; do not infer its cause from partial corrections or broaden the rewrite into healthy sections.
8. Reconcile rows, keys and agreed metrics at an aligned reload cutoff before acceptance. Prove a successful reload and complete sheet-by-sheet front-end regression, then obtain the BI Analyst's independent final validation before production promotion. Customer UAT is optional unless explicitly required.
9. Record any remaining legacy bridge as an unresolved migration dependency. Promotion and seven-calendar-day hypercare follow the governing source-only migration procedure; after promotion, fix forward and never return the app to SQL Server. The preceding backstage app is archived historical evidence, not a rollback source.

## Required pre-handoff checks

- Every active Snowflake `SQL SELECT` has a corresponding preceding Qlik `LOAD`.
- Every connector output referenced by the preceding `LOAD` uses the uppercase name Qlik will receive.
- Every preceding-load alias exactly matches the retained Qlik consumer field, including existing spelling errors such as `Payment Gatway`.
- Computed and aggregate SQL expressions have stable output aliases, and those aliases are mapped again at the Qlik boundary.
- Active section order, filters, joins, aggregations and `Exit Script;` behaviour match the confirmed source control flow.
- The replacement contains no unintended SQL Server, Stitch, archived-source or production-write dependency.
- For a multi-section app, the section ledger assigns `accepted`, `validated at stated layer`, `unvalidated` or `blocked`; records the source/filter/join/key/grain/aggregation contract, evidence/cutoff, residual gap and next action; and preserves independently accepted sections unless requirements change or contrary evidence appears.
- Local/static review is not runtime proof; record the development reload and front-end checks separately.

## Anti-patterns

- Relying on quoted mixed-case SQL aliases to preserve Qlik field case.
- Returning Snowflake SQL directly into the target Qlik table without a preceding `LOAD`.
- Mapping only derived fields while leaving direct columns dependent on connector casing.
- Changing source, business logic and visual behaviour together.
- Declaring migration complete while authoritative legacy dependencies remain.
- Changing QVD filenames or field contracts incidentally.
- Re-running broad value-discovery work after the required source columns, joins and transformations are already established.

## Failure recovery

If reload reports a missing field after a Snowflake section:

1. Inspect the exact preceding `LOAD` source name first.
2. Compare it with the uppercase connector output name, including spaces and punctuation.
3. Correct only the boundary mapping and rerun with changed input.
4. If the uppercase mapping is correct, then investigate SQL output presence, population and downstream association under SKILL-0175.
5. Never treat successful SQL execution or a large returned row set as proof that Qlik received the retained field contract.

## Benchmark case

For Shopify Order Breakdown, four Snowflake SQL sections returned millions of rows successfully, but the first replacement relied on quoted SQL aliases and omitted preceding loads. The corrected form maps all uppercase connector outputs through explicit preceding `LOAD` aliases before the existing Qlik model consumes them. SQL success proved source execution only; the corrected Qlik boundary remained subject to development reload and front-end verification.

## Output and evidence

Record inputs, direct evidence, resulting replacement, connector-boundary mapping, runtime result, residual uncertainty, owner and next action.

## Stop

Stop on unresolved grain, key portability, source availability, field contract or baseline. Do not promote while the development reload, front-end regression or required independent validation remains open.

## Change Log

- 2026-10-15: Added per-section state isolation after the 4 Way Sales Balancing checkpoint recorded healthy Store/Digital development results, upstream-only Gift Card publication parity with front-end sign-off absent, unvalidated D365NotInvoiced and materially unresolved/blocked NonExport. No unresolved cause is inferred.
- 2026-10-14: Strengthened the Snowflake-to-Qlik boundary contract after Shopify Order Breakdown exposed an application failure: quoted SQL aliases were incorrectly treated as case-preserving. Added mandatory uppercase preceding-load mappings, a representative pattern, pre-handoff checks, focused recovery and the rule to move to reload/front-end diagnosis once source discovery is settled.
- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
