---
id: SKILL-0045
type: skill
title: TypeSafe System One Primitive Selection
status: current
created: 2026-09-19
updated: 2026-10-24
owner: Library owner

trigger_phrases: ["choose TypeSafe primitive", "Choice Noul or Score", "typed AI judgement type", "System One primitive"]
links: []
tags: [skill, ai-engineering, typesafe, system-one, structured-decisions]
---

# TypeSafe System One Primitive Selection

Decide whether a bounded semantic judgement needs TypeSafe System One and, if so, select Choice, Noul or Score.

## Intent-routing contract

Use only for primitive selection. Typed-question design, request orchestration, probability policy, evaluation and production security are separate actions. Keep deterministic rules, calculations, permissions and execution in code.

## When to use

Use when software needs programmable common sense and deterministic code cannot reliably choose among defined options, assess whether a condition holds or place an item on ordered described levels.

## Current documentation preflight

Before designing or changing the integration, read the current TypeSafe documentation index, relevant primitive page, selected API or SDK page, confidence guidance and closest cookbook. Stop if current documentation is unavailable; do not freeze API signatures from this record.

## Method

1. Start from user-visible behaviour and isolate the smallest semantic judgement.
2. Reject TypeSafe when an exact rule, calculation, lookup or deterministic transformation decides the result.
3. Select Choice for one defined option, Noul for the probability that a condition holds, and Score for position among ordered independently described levels.
4. State the chosen primitive, bounded output and why deterministic code is insufficient.

## Benchmark case

A supplier reason must map to one defined charge category: Choice is selected because the output is one candidate, while rates and writes remain deterministic.

## Anti-patterns

- Using TypeSafe where a rule determines the answer
- Choosing a primitive before defining the answer meaning
- Treating primitive selection as permission to execute an action

## Provenance and security review

- Upstream: https://github.com/typesafe-ai/skills
- Admitted revision: 65a39f393687675ce170e6094757de20370365b9
- Reviewed paths: skills/typesafe-ai/SKILL.md (blob 0109513f9656917dc93cbc5ecddfca465a53ce66) and skills/typesafe-ai/LICENSE (blob 8c73b41b89d9a76ddf0fdb0edfaafdda800d36e8)
- Licence: MIT, Copyright 2026 TypeSafe AI
- Review date: 2026-09-19
- Findings: the admitted folder contains only Markdown guidance and the licence; no scripts, dependencies, hooks, MCP configuration, encoded payloads, credential access or executable content were present.
- Accepted risks: live documentation and service contracts may change; model outputs remain probabilistic; production use introduces external-service availability, cost and data-governance considerations.
- Update rule: reassess provenance, changed files, permissions and executable content before admitting a later revision.
- Removal path: delete this record and remove the locally installed typesafe-ai skill or application dependency; revoke any TypeSafe credentials separately if they were later created.

## Authoritative sources

- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/concepts/system-one
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one
- https://docs.typesafe.ai/primitives
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/api
- https://docs.typesafe.ai/sdk/python
- https://docs.typesafe.ai/sdk/javascript

## Stop

Stop when the semantic need, primitive and deterministic boundary are explicit.

## Contextual links

- `SKILL-0154` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0155` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0156` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0157` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0158` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 5 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
