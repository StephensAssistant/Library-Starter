---
id: SKILL-0284
type: skill
title: ADF Retry-policy Design
status: current
created: 2026-09-20
updated: 2026-10-24
links: []
tags: [skill, action-specific, adf, retry-policy]
trigger_phrases: ["design ADF retry policy", "choose ADF retry behavior", "ADF retry settings"]
---

# ADF Retry-policy Design

Design bounded recovery behaviour for an already classified Azure Data Factory failure.

## When to use

Use after the failure class, operational impact and idempotency boundary are evidenced. Failure classification, pipeline implementation and retry execution are separate actions.

## Intent-routing contract

This Skill owns retry-policy design only. It does not classify the original failure, apply settings, execute a rerun or approve production change.

## Method

1. Confirm the evidenced failure class, activity semantics, idempotency, side effects, dependencies and recovery objective.
2. Permit automatic retry only for transient classes with a safe replay contract.
3. Define retry count, delay or backoff, timeout, terminal condition and escalation path from current platform capability.
4. Define duplicate-prevention, partial-write and downstream-consistency safeguards before retrying mutating work.
5. Route authorization, missing-file, schema-drift, validation and other deterministic failures to correction or authority resolution rather than generic retry.
6. Record the proposed policy, evidence, exceptions and required approval before implementation.

## Evidence expected

Retain the classified failure, activity contract, retry parameters, replay safeguards, terminal behaviour, approval requirement and source/date context.

## Benchmark case

A transient source timeout on an idempotent read receives a bounded delayed retry policy, while a permission denial receives no automatic retry and is routed for authority resolution.

## Anti-patterns

- Retrying every failure class.
- Designing retry without proving idempotency.
- Omitting terminal and escalation behaviour.
- Applying or executing the policy during design.

## Stop

Stop with a bounded evidence-backed retry policy, or the precise classification, idempotency, side-effect, capability or authority gap.

## Contextual links

- `SKILL-0036` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
