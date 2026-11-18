---
id: SKILL-0046
type: skill
title: Snowflake Staged-File Ingestion
status: current
created: 2026-09-20
updated: 2026-10-14
owner: Library owner

links: [PLAY-0006, PLAY-0018, PLAY-0025, SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0053, SKILL-0054, SKILL-0055, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0266, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0270, SKILL-0271]
tags: [skill, snowflake, ingestion, staged-files]
trigger_phrases: [snowflake staged file ingestion, copy into snowflake, load file to raw]
---

# Snowflake Staged-File Ingestion

Implement replay-safe file ingestion from a governed Snowflake stage into RAW, STAGING and INGESTED responsibilities.

## When to use

Use when CSV, JSON, Excel or another file lands in an internal or external Snowflake stage.

## Method

1. Verify file authority, format, expected headers, delivery cadence, stage ownership and file identity.
2. Land source-faithful rows in RAW with `COPY INTO` and file/load metadata; do not change business meaning there.
3. Preserve auditable load history in STAGING where replay or investigation requires it.
4. Produce deterministic INGESTED state using proven grain, deduplication, update/delete rules and rerun-safe keys.
5. Reconcile file population, rows, distinct keys, timestamps, rejects and material totals before release.


## Read CSV headers without changing the pipeline format

For staged SELECT, reference a named file format with `FILE_FORMAT => 'database.schema.format_name'`. Inline TYPE/SKIP_HEADER definitions belong to other commands and are not supported by this SELECT grammar. Do not retry by replacing equals signs with arrows inside an inline format.

If the production format skips the header, create a separately named TEMPORARY FILE FORMAT with TYPE=CSV, SKIP_HEADER=0 and the evidenced delimiter/quote settings. Query METADATA$FILE_ROW_NUMBER=1 through that named format in the same session. Drop the temporary format after inspection; never alter the pipeline format to read a header.

Verify with representative fixtures and retain reproducible evidence in the owner’s Library.

Authority: https://docs.snowflake.com/en/user-guide/querying-stage and https://docs.snowflake.com/en/sql-reference/sql/create-file-format. This inspection creates no data table and must not invoke a loader.

Learning disposition: guidance-failed in the supplied inline SQL, bounded existing-owner repair. Expected outcome: named-format header inspection succeeds without changing normal ingestion. Rollback/rejection: remove this added method if the named-format grammar is disproved; do not weaken format isolation or cleanup.

## Inflated spreadsheet-export review

When a spreadsheet export carries a large used range, treat physical CSV rows and populated business rows as different populations.

1. Pin the exact staged filename, size/checksum and parsing contract before loading.
2. Parse into a newly created session-only review table; do not load the persistent RAW table first.
3. Reconcile the COPY result to populated source rows. Identify blank inflation only with an all-source-fields-blank predicate; never delete a row because one required field is blank.
4. Establish the source date and numeric formats from the populated values, then parse explicitly. A NULL parsed date can collapse distinct daily rows into false duplicate groups, so reject duplicate conclusions until parsing is proven.
5. Delete only the proven wholly blank rows from the temporary review table, rerun required-value, type, grain, duplicate, relationship and material-total checks, and retain both physical-row and populated-row counts.
6. Advance to persistent RAW/STAGING/INGESTED loading only after the populated scope passes. A successful COPY or a large loaded-row count is not business-population proof.
7. Drop or verify absence of the validation-only temporary object after its evidence is retained; preserve permanent stages and pipeline objects.

Verify with representative fixtures and retain reproducible evidence in the owner’s Library.

Representative cases:
- Positive: the all-fields-blank predicate removes only inflated empty rows, explicit date parsing preserves daily grain, and populated counts/totals reconcile.
- Negative: COPY succeeds but populated dates parse NULL; stop without deleting persistent data or treating grouped NULL dates as genuine duplicates.
- Boundary: a row with any populated source field is retained for validation even when other required fields are blank; only the all-fields-blank population is cleanup-eligible.

Learning disposition: existing-owner update. The staged-file ingestion owner was incomplete for verified spreadsheet used-range inflation and parse-induced false duplicates; no distinct Skill or new ID is needed.

## Benchmark case

A corrected supplier file is resubmitted. A passing application identifies the file version, reloads without duplicating governed rows, preserves prior load evidence and reconciles the replacement result.

## Anti-patterns

- Loading by column position when named headers are available.
- Treating a successful `COPY INTO` as proof of completeness.
- Removing load evidence needed for replay.
- Guessing missing-header mappings.

## Stop

Stop after a reconciled, replay-safe INGESTED result, or the precise file, schema, grain or ownership gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0046--SKILL-0266 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0046--SKILL-0267 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0046--SKILL-0268 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0046--SKILL-0269 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0046--SKILL-0270 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0046--SKILL-0271 | related_to | undirected | user_confirmed | supports
