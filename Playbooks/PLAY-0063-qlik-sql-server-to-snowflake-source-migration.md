---
id: PLAY-0063
type: playbook
title: Qlik SQL Server-to-Snowflake Source Migration
status: current
created: 2026-09-20
updated: 2026-10-16
owner: the Library owner
links: [PLAY-0022]
tags: [playbook, qlik-sense, sql-server, snowflake, source-migration, fix-forward]
---

# Qlik SQL Server-to-Snowflake Source Migration

## Trigger

A Qlik app must stop querying SQL Server and use Snowflake while retaining the existing Qlik front end, data model and load-script transformations.

## Intent routing

Use for requests to convert, migrate or replace a Qlik app's SQL Server source with Snowflake without redesigning the app. Do not use for a Qlik-to-Sigma rebuild or for introducing fact/dimension, Semantic View or golden dynamic-table layers; those belong to the later reporting-platform route.

Inherit the shared access, grants, ownership, testing, promotion authority and seven-calendar-day hypercare controls from [[PLAY-0022]]. This Playbook owns only the source-only Qlik procedure.

## Method

1. Inventory the active SQL Server connections and queries, their Qlik field contract, filters, joins, rolling windows, null behaviour, transformations, QVD outputs and front-end consumers. Exclude only proved dead or out-of-scope code.
2. Select one unresolved source, filter, join, key, grain, formula or aggregation as the active domino. State the observation that would confirm or reject it, then use the smallest stable sample or aggregate check that can decide it. Compare only the columns necessary for that check.
3. Verify the result before expanding scope. Recompute downstream work from the evidence, discard invalidated hypotheses and skip questions or tests the result has made irrelevant. Do not run a broad multi-branch comparator, redesign several stages or ask several future decisions when the active domino can collapse them.
4. For the next surviving dependency, identify the verified equivalent existing Snowflake object and exact columns. Treat physical location, the Qlik connection's authorised execution route and a successful runtime query as separate evidence; never accept name similarity as a mapping. Repeat steps 2–4 one domino at a time.
5. If a required source is missing or its access route is unverified, record the precise blocker and affected app section. Do not invent a substitute or redesign the front end; continue with the next ready app where possible.
6. Duplicate the backstage app for development and leave production untouched until promotion.
7. Change only the connection and embedded source queries required to read Snowflake. Preserve existing Qlik transformations, associations, field names, expressions, outputs and front-end behaviour. Use preceding-load aliases where connector output casing would otherwise break the existing Qlik contract.
8. Apply and verify the required system access, current and future Snowflake grants and established Snowflake ownership rules before declaring the source runnable.
9. At an aligned reload cutoff, reconcile row counts, business keys, agreed metrics and representative records; prove a successful reload and complete sheet-by-sheet front-end regression.
10. Hand the validated development app to a BI Analyst for an independent final behavioural check. Customer UAT is optional unless explicitly required. Repair only evidenced exceptions.
11. After BI Analyst approval and verified production-promotion authority, recheck the exact development/production app identities and validated revision before the authorised publisher replaces production with the validated development app. Changed source or target invalidates the affected acceptance; preserve it and revalidate before promotion. Leave the preceding backstage app in the backstage space and add `(Archived)` to its name as historical evidence only.
12. Run seven calendar days of fix-forward hypercare. the Library owner owns technical monitoring and remediation; the BI Analyst checks report behaviour. Never return the app to SQL Server.

## Benchmark case

Use the owner’s verified migration record and reconcile replacement sources, consumer contracts and representative report outputs.

## Stop

Stop successfully after BI Analyst acceptance, production promotion and seven calendar days of hypercare with no unresolved or unverified material defect. Stop as blocked when a required Snowflake source, execution route, access grant, ownership rule or parity result is missing; name the exact evidence required and do not alter the front end to bypass it.
