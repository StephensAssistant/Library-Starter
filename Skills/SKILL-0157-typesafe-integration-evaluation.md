---
id: SKILL-0157
type: skill
title: TypeSafe Integration Evaluation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["test TypeSafe integration", "evaluate Jev model", "benchmark System One"]
links: []
tags: [skill, action-specific]
---

# TypeSafe Integration Evaluation

Evaluate a TypeSafe System One integration on representative domain cases and operational measures.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use before production adoption or after material model, question or policy changes.

## Current documentation preflight

Before this action, read the current TypeSafe documentation index, relevant primitive page, selected API or SDK page, confidence guidance and closest cookbook. Stop if current documentation is unavailable; do not freeze API signatures from this record.

## Method

1. Test positive, negative, ambiguous and changed-state cases.
2. Separate missing evidence, model error, code error and service failure.
3. Measure target-domain quality, latency, token use and cost.
4. Retest policy thresholds and escalation outcomes against observed distributions.

## Decision and evidence details

Before testing, record the intended bounded use and its owner-agreed quality, latency and cost acceptance predicates. If those criteria are missing, contradictory or unevaluable, report measured results with a criteria gap and withhold adoption support; do not invent thresholds. Retain the integration/model/question/policy versions, domain case inputs, independently expected outcomes and per-case actual responses. State the measured population and available usage/cost evidence; unavailable measurements remain unknown. Distinguish correctness of typed output from correctness of the application's escalation/action branch.

Boundary design case: all clear matches succeed but ambiguous cases bypass manual review. Record the policy failure separately; aggregate match accuracy cannot establish the intended bounded production use.

## Benchmark case

Historical supplier descriptions include clear matches, ambiguous cases and unseen wording; results are scored separately from code and service failures.

## Anti-patterns

- Testing only happy paths
- Combining model and code failures
- Claiming general accuracy from demonstrations

## Authoritative sources

- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/api

## Stop

Stop when quality and operational evidence support the intended bounded use or expose a named blocker.

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
