---
id: SKILL-0177
type: skill
title: Contextual Relationship Candidate Management
status: current
created: 2026-09-20
updated: 2026-10-24
owner: Library owner

trigger_phrases: ["inferred relationship candidate interpretation", "interpret relationship candidate", "inferred link score", "relationship hypothesis", "contextual relationship candidate management", "create contextual link", "create contextual links", "find related subjects"]
links: []
tags: [skill, library-mechanics, relationships, inference]
---

# Contextual Relationship Candidate Management

Interprets inferred relationship candidates and records useful reciprocal contextual discovery pointers without granting them authority.

## When to use

Use when consulting `.github/relationship-candidates.json` or assessing subject and context overlap during the secondary layer of PLAY-0071.

## Method

1. Treat each candidate as a hypothesis only and complete the confirmed-link review first.
2. Check direct evidence and surface any contradiction. If direct evidence exists, route the candidate to confirmed-link handling instead of contextual storage.
3. Assess whether the overlap in subject, context, system, method, analogous problem or reusable precedent creates a concrete future retrieval benefit.
4. For a useful candidate, add reciprocal bullets to both live endpoints under `## Contextual links` using ``- `<ID>` — `<basis>` — <why this may help future work>.``
5. Never add the candidate to frontmatter `links`, the confirmed relationship ledger or association closure, and never use it for status, causality, identity, dependency or action authority.
6. Reject weak keyword coincidence, generic tags, contradictions, duplicates and transitive-only proximity. Do not infer A-to-C from A-to-B and B-to-C.
7. Read back both endpoints and verify the contextual pointers are reciprocal, separately labelled and rationale-bearing.

## Benchmark case

Two Projects share a Snowflake migration subject and reusable reconciliation approach without a direct factual relationship. Reciprocal `reusable_precedent` contextual pointers are recorded with the retrieval benefit, while frontmatter `links` remain unchanged.

## Anti-patterns

- Promoting a contextual pointer or score into authority
- Ignoring contradictory direct evidence
- Inferring A→C from A→B and B→C
- Adding a one-sided or rationale-free contextual pointer

## Stop

Stop after each candidate is classified as confirmed elsewhere, contextually linked, rejected or unresolved, and any contextual link is reciprocal and visibly advisory.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`; existing reciprocal relationships remain supported and no new confirmed relationship was found.
- Contextual result: `no_contextual_links`; the useful candidate-management relationships are already confirmed, and no separate advisory pointer would improve retrieval.
