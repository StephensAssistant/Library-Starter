---
id: SKILL-0218
type: skill
title: Snowflake Streamlit Governed Deletion Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, snowflake, streamlit, deletion]
trigger_phrases: ["Streamlit soft delete", "Streamlit hard delete", "governed deletion"]
---

# Snowflake Streamlit Governed Deletion Design

Design safe deletion behaviour for records managed through a Snowflake Streamlit application.

## When to use

Use when deciding or specifying how an application removes, hides, retains or restores governed records. Trusted audit-metadata design is a separate Skill.

## Intent-routing contract

This Skill owns deletion mode, lifecycle, visibility, dependency and recovery behaviour. It does not own audit-field trust, adjacent architecture, implementation, approval or deployment.

## Method

1. Confirm the authoritative record, business purpose, retention obligations, dependencies and deletion authority.
2. Choose hard or soft deletion explicitly from evidence; defaulting to either without retention and recovery analysis is not a decision.
3. For soft deletion, define active/deleted states, filtering rules, restore behaviour and when permanent purge is permitted.
4. For hard deletion, prove no required history, dependency, legal retention or recovery path is lost.
5. Define consistent application reads, downstream processing, uniqueness rules and customer visibility for deleted records.
6. Require a trusted deletion event record through the audit-metadata capability; do not make audit fields user-editable.
7. Test delete, repeat-delete, restore where applicable, dependent-record and downstream-read behaviour.

## Evidence expected

Retain the deletion decision, authority, dependencies, retention basis, state transitions, tests, unresolved gaps and source/date context.

## Benchmark case

Removing a supplier mapping soft-deletes it, excludes it from active reads and downstream processing, retains historical evidence, supports an authorised restore and prevents a repeated delete from corrupting state.

Boundary design case: Retention obligations are unresolved for a requested hard delete. Stop that deletion decision and identify the missing authority/evidence; hiding the row or switching silently to soft delete does not resolve it.

## Anti-patterns

- Hard-deleting because it is simpler.
- Soft-deleting without filtering downstream consumers.
- Allowing deletion when dependent records or retention rules are unresolved.
- Treating a hidden UI row as deletion evidence.

## Stop

Stop when deletion authority, retention obligations, dependencies, recovery requirement or downstream behaviour is unknown. Do not claim completion without evidence of the designed lifecycle.

## Contextual links

- `SKILL-0033` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
