---
id: SKILL-0208
type: skill
title: OpenFlow Pagination and Cursor Design
status: current
created: 2026-09-20
updated: 2026-10-24
links: []
tags: [skill, action-specific, openflow, pagination, cursor]
trigger_phrases: ["OpenFlow pagination", "OpenFlow cursor", "page OpenFlow source"]
---

# OpenFlow Pagination and Cursor Design

Design deterministic page traversal and cursor progression for one OpenFlow source.

## When to use

Use when an OpenFlow source returns bounded pages and the flow must traverse every source record exactly once per traversal. Route persisted checkpoints, watermarks, replay overlap and restart safety to SKILL-0282.

## Intent-routing contract

This Skill owns page ordering, cursor input/output and traversal termination. It does not own checkpoint persistence, incremental watermark policy or adjacent implementation and deployment work.

## Method

1. Confirm the source’s authoritative pagination mechanism and maximum page size.
2. Select a stable, deterministic ordering key with an explicit tie-breaker.
3. Define the initial request, returned cursor, next-page request and terminal response.
4. Keep the cursor opaque unless the source contract explicitly defines its structure.
5. Detect missing, repeated or non-advancing cursors and stop rather than loop or skip.
6. Define duplicate handling only for page-boundary behaviour inside one traversal.
7. Establish the source-backed consistency boundary for the traversal: snapshot/version, fixed population or an evidenced reconciliation strategy. Do not claim exactly-once completeness from ordering alone when the source can change during traversal. Preserve observed source changes as exceptions and hand unresolved restart/replay needs to SKILL-0282.
8. Bound traversal requests and elapsed time from the source contract; test first, middle, final, empty, exact-page-size and interrupted-page responses without advancing past an unconfirmed page.

## Evidence expected

Retain the source contract, ordering keys, cursor trace, page counts, terminal condition and any duplicate or ordering exception.

## Benchmark case

An Orders flow follows opaque next-page cursors across equal timestamps using a stable ID tie-breaker, terminates on the documented final response and visits every expected row once.

## Anti-patterns

- Constructing an opaque cursor from assumptions
- Paginating without stable ordering or a tie-breaker
- Treating a repeated cursor as successful completion
- Mixing persisted watermark policy into page traversal

## Stop

Stop when first-to-final traversal is reproducible without gaps or loops, or when cursor progression, ordering or termination remains ambiguous.


## Contextual links

- `SKILL-0032` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
