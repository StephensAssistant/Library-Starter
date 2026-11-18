---
id: SKILL-0048
type: skill
title: Deterministic Paginated API Extraction
status: current
created: 2026-09-20
updated: 2026-10-04
owner: Library owner

links: [PLAY-0006, PLAY-0018, PLAY-0025, SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0053, SKILL-0054, SKILL-0055, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0266, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0270, SKILL-0271]
tags: [skill, api, graphql, pagination, extraction]
trigger_phrases: ["implement paginated API extraction", "extract every GraphQL page", "follow API cursors deterministically"]
---

# SKILL-0048 — Deterministic Paginated API Extraction

## Purpose

Extract a complete API or GraphQL population by following a deterministic page, cursor or continuation contract.

## When to use

Use when a synchronous API exposes a result over multiple pages and complete traversal is the required action. Use the separate bulk-operation, checkpoint-governance and extraction-validation Skills for those jobs.

## Method

1. Verify the endpoint and version, authorised scope, authoritative objects, grain and stable source identifiers.
2. Establish the initial request, page size, ordering and exact next-page or cursor semantics.
3. Follow only source-issued continuation state until the documented terminal condition is reached.
4. Record page/cursor evidence and extraction timestamps separately from ingestion timestamps.
5. Handle retryable transport failures without advancing past an unconfirmed page.
6. Make page replay idempotent so a retry cannot duplicate or omit stable source IDs.
7. Return the extracted population and traversal receipt for independent validation.

## Benchmark case

A GraphQL connection returns three pages with `hasNextPage` and `endCursor`. A passing application requests each cursor once, stops only when `hasNextPage=false`, safely replays a failed second page and produces no duplicate stable IDs.

## Anti-patterns

- Assuming the first page is complete.
- Inventing or incrementing a cursor not issued by the source.
- Advancing continuation state before page persistence succeeds.
- Treating HTTP success as proof of population completeness.
- Embedding credentials in code or Library records.

## Stop

Stop when every page is traversed to the source-defined terminal condition with replay-safe evidence, or when endpoint scope, ordering, stable identity or continuation semantics remain unresolved.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0048--SKILL-0266 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0048--SKILL-0267 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0048--SKILL-0268 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0048--SKILL-0269 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0048--SKILL-0270 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0048--SKILL-0271 | related_to | undirected | user_confirmed | supports

## Verified nested-connection technique — 4 October 2026

Trigger: an outer GraphQL connection returns nodes without their own Node ID, while each node owns separately paginated child connections. Root-only pagination does not extract the children completely. the applicable canonical record Shopify API 2026-07 locationsForMove supplied the representative case.

1. Capture each outer edge cursor and the cursor immediately preceding that edge. Use the preceding cursor with outer first:1 to reselect exactly that node while continuing its child lists; validate its stable domain identity (here location.id) and non-child header on every reselection.
2. Track available and unavailable child cursors/completion independently. When querying both lists together, ignore results from a child that already completed; do not append its first page again when its continuation input becomes null.
3. Require valid hasNextPage and a source-issued advancing cursor. Reject empty nonterminal pages, repeated cursors, duplicate outer identities and missing/duplicate child IDs. Follow every outer page and every child page to terminal state.
4. Reconcile returned Count metadata only when precision is EXACT. Report exact checks performed and nonexact/missing metadata separately; never emit an unconditional reconciliation flag for checks that were skipped.
5. Compare the parent ID/version throughout and at a final read, record traversal receipts and persist only the completed evidence. An unchanged parent timestamp does not independently prove an atomic snapshot or child-only change detection.
6. Bound elapsed time, requests and retries. For operating use, keep resumable cursor/version state durable and preserve it on retry; a successful DEV probe is not an installed production delta route.

Verify with representative fixtures and retain reproducible evidence in the owner’s Library.

Verify with representative fixtures and retain reproducible evidence in the owner’s Library.

Additional anti-patterns: treating a nullable cursor as text "None"; reselecting a different outer node during child continuation; reporting unperformed count checks as successful; inferring full production readiness from an empty pilot.
