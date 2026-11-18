---
id: SKILL-0049
type: skill
title: Snowflake Application Writeback
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0054, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0271]
tags: [skill, snowflake, application, writeback]
trigger_phrases: [snowflake application writeback, streamlit writeback, snowflake governed writeback]
---

# Snowflake Application Writeback

Implement governed Snowflake writes initiated by Streamlit, Sigma or another application.

## When to use

Use when an application creates, edits or deletes governed source rows inside Snowflake.

## Method

1. Define the application event, target grain, business key, actor and authority.
2. Use a controlled procedure, transaction or equivalent governed write boundary.
3. Preserve created/modified actor and timestamps; use soft deletion when history or auditability requires it.
4. Enforce validation and duplicate rules before mutation.
5. Test create, edit, delete, duplicate prevention, permission denial and rollback/error behaviour; reconcile downstream refreshes.

## Benchmark case

A Streamlit form updates a charge rate. A passing application rejects overlapping invalid periods, records the actor and time, commits atomically and refreshes the governed consumer result once.

Failure design case: the application times out after submitting an edit. Treat the commit state as uncertain and inspect the target key, audit values and transaction evidence before retrying; neither the timeout nor a success toast proves whether the governed write persisted.

## Anti-patterns

- Treating writeback as an ungoverned shortcut.
- Allowing direct table mutation without validation or audit evidence.
- Testing only the happy-path SQL statement.
- Guessing application or service-role privileges.

## Stop

Stop after authorised, auditable and tested write behaviour is evidenced, or the precise authority, key, validation or recovery gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0049--SKILL-0266 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0049--SKILL-0267 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0049--SKILL-0268 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0049--SKILL-0269 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0049--SKILL-0270 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0049--SKILL-0271 | related_to | undirected | user_confirmed | supports
