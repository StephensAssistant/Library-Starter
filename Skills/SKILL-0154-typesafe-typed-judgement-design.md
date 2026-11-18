---
id: SKILL-0154
type: skill
title: TypeSafe Typed-Judgement Design
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["design TypeSafe question", "define System One judgement", "write typed AI criteria"]
links: []
tags: [skill, action-specific]
---

# TypeSafe Typed-Judgement Design

Design one narrow TypeSafe System One judgement with explicit state, instructions, criteria and output options.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after a semantic judgement and primitive have been selected.

## Current documentation preflight

Before this action, read the current TypeSafe documentation index, relevant primitive page, selected API or SDK page, confidence guidance and closest cookbook. Stop if current documentation is unavailable; do not freeze API signatures from this record.

## Method

1. Supply only relevant state as clearly named fields.
2. Put the judgement in instructions and define every valid answer in criteria.
3. Give each question complete meaning; question IDs are not model context.
4. Ask one coherent judgement per question and include a no-match outcome when candidates may be incomplete.

## Decision and evidence details

Deliver the proposed primitive, named input state, complete question/instructions, allowed outputs and criteria together. Check that a reader can decide what each option means without relying on an ID or omitted context.

Boundary design case: a supplier description fits none of the supplied categories. The question must permit the explicit no-match result. If required state is missing, obtain or report that gap instead of designing criteria that assume it.

## Benchmark case

A supplier reason is matched against complete category definitions with an explicit no-match outcome.

## Anti-patterns

- Mixing independently useful judgements
- Omitting a valid candidate
- Using irrelevant state as implicit context

## Authoritative sources

- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/concepts/system-one
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one
- https://docs.typesafe.ai/primitives
- https://docs.typesafe.ai/confidence

## Stop

Stop when the question has one bounded meaning and every allowed result is explicit.

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
