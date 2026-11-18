---
id: SKILL-0057
type: skill
title: Sigma Writeback Engineering
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265]
tags: [skill, sigma]
trigger_phrases: [sigma writeback, sigma input table, sigma action]
---

# Sigma Writeback Engineering

Design and validate Sigma input tables, actions and governed writeback behaviour.

## When to use

Use when Sigma users will create or modify data, trigger actions, annotate, plan or approve.

## Method

1. Define target schema, grain, authority, validation and audit fields.
2. Verify the executing identity and required Snowflake privileges.
3. Make action scope and failure behaviour explicit.
4. Test create, edit, duplicate, permission denial and partial-failure cases.
5. Reconcile the persisted result and downstream consumer refresh.

## Benchmark case

A planning input writes one authorised row, rejects an invalid duplicate, records actor/time and exposes the confirmed result downstream.

Failure design case: an action reports an error after a possible write. Inspect the persisted business key and actor/time evidence before retrying, retain partial effects, and keep the consumer-refresh result separate; do not create a duplicate to obtain a reassuring UI response.

## Anti-patterns

- Inventing Sigma capabilities, identifiers, schemas or successful evidence.
- Duplicating governed logic without a measured reason.
- Treating a syntactically accepted change as verified behaviour.

## Stop

Stop after the named outcome is read back and verified, or the precise capability, access, source or evidence gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0057--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0057--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0057--SKILL-0265 | related_to | undirected | user_confirmed | supports
