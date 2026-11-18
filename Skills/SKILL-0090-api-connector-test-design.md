---
id: SKILL-0090
type: skill
title: API and Connector Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [testing, api-connector]
trigger_phrases: ["design API tests", "test connector pagination", "test API checkpoint recovery"]
---

# SKILL-0090 — API and Connector Test Design

## Purpose

Design tests for API or managed-connector extraction contracts, state and recovery.

## When to use

Use for: design API tests; test connector pagination; test API checkpoint recovery.

## Method

1. Verify authorised scope and representative object coverage.
2. Test pagination, cursors, checkpoints or high watermarks at boundaries.
3. Test retries, rate/error handling, partial failures and resume.
4. Prove idempotent replay/MERGE and schema-evolution behaviour.
5. Reconcile source responses with landed population.

## Benchmark case

Inject a partial page failure, resume from the saved cursor and prove no gaps or duplicates across the loaded result.

Boundary design case: a replay completes but duplicate stable IDs appear across page boundaries. Expect a failed recovery case even if every response succeeded; retain the cursor/page and landed-key evidence rather than accepting the connector status as completeness or idempotency proof.

## Anti-patterns

- Treating connector success with zero rows as healthy.
- Ignoring partial failure.
- Testing one page only.

## Stop

Stop with source-to-load and recovery cases plus expected evidence.
