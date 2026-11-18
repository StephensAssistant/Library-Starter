---
id: SKILL-0155
type: skill
title: TypeSafe Request Orchestration
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["batch TypeSafe questions", "orchestrate System One requests", "chain typed judgements"]
links: []
tags: [skill, action-specific]
---

# TypeSafe Request Orchestration

Group or sequence TypeSafe System One judgements according to their evidence dependencies.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when an integration has multiple already-designed typed judgements.

## Current documentation preflight

Before this action, read the current TypeSafe documentation index, relevant primitive page, selected API or SDK page, confidence guidance and closest cookbook. Stop if current documentation is unavailable; do not freeze API signatures from this record.

## Method

1. Map which questions are independent and which require an earlier result.
2. Submit independent questions over the same state together.
3. Create a later request only when an earlier result is required to fetch evidence or construct its state.
4. Preserve each raw response and dependency boundary for diagnosis.

## Decision and evidence details

Deliver the dependency graph with each request's state source, grouped independent questions and the result required before a dependent request can be constructed. Preserve raw responses with the state/version used.

Boundary design case: the first judgement is unavailable or invalid and its result selects the next candidate set. Hold that dependent request and report the prerequisite gap; do not fetch an assumed candidate set or treat a missing response as a category choice.

## Benchmark case

Independent routing and risk questions are batched, while a follow-up match waits for the first result to load its candidate set.

## Anti-patterns

- Sequential calls for independent questions
- Batching a question before its required evidence exists
- Using question IDs as hidden context

## Authoritative sources

- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one
- https://docs.typesafe.ai/api
- https://docs.typesafe.ai/sdk/python
- https://docs.typesafe.ai/sdk/javascript

## Stop

Stop when request grouping mirrors actual evidence dependencies.

## Contextual links

- `SKILL-0045` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
