---
id: SKILL-0158
type: skill
title: TypeSafe Production Data Security
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["secure TypeSafe integration", "TypeSafe credentials", "Jev production data review"]
links: []
tags: [skill, action-specific]
---

# TypeSafe Production Data Security

Assess and enforce data, credential and authority boundaries for a production TypeSafe integration.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use before production data is sent or consequential application behaviour is enabled.

## Current documentation preflight

Before this action, read the current TypeSafe documentation index, relevant primitive page, selected API or SDK page, confidence guidance and closest cookbook. Stop if current documentation is unavailable; do not freeze API signatures from this record.

## Method

1. Keep credentials server-side and out of prompts, clients and records.
2. Classify data sensitivity and verify authority to send it to the external service.
3. Check current documentation for data handling, API and service constraints.
4. Limit model authority to semantic output; keep permissions and execution in authorised code.
5. Stop on unresolved provenance, security or data-governance findings.

## Decision and evidence details

Record which fields leave the system, their sensitivity/provenance, receiving service, current handling evidence and applicable sending authority. Retain credential location and permission/execution boundaries without copying secrets into the review. Unresolved handling or authority blocks the affected send.

Boundary design case: the classifier works with synthetic descriptions but authority for production fields is absent. Keep the production integration blocked at that boundary; synthetic success does not approve sending the real dataset.

## Benchmark case

A production classifier sends only authorised supplier-description fields from a server component and cannot execute the resulting recommendation.

## Anti-patterns

- Client-side credentials
- Sending sensitive state without authority
- Treating typed output as execution permission

## Authoritative sources

- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/api
- https://docs.typesafe.ai/sdk/python
- https://docs.typesafe.ai/sdk/javascript

## Stop

Stop when credentials, data authority, service handling and execution boundaries are evidenced.

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
