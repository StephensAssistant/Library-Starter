---
id: PLAY-0071
type: playbook
title: Mandatory Two-Layer Library Link Review
status: current
created: 2026-10-24
updated: 2026-11-15
trigger_phrases: [review library links, review unlinked records, complete link review, create contextual links, find related subjects]
links: [PLAY-0075, SKILL-0025, SKILL-0114, SKILL-0176, SKILL-0177, SKILL-0182]
tags: [playbook, library-mechanics, links, relationships]
---

# Mandatory Two-Layer Library Link Review

## Trigger

Run automatically before saving a new governed Library record, after a material change that can alter its relationships, when a governed record has `links: []`, or when an explicit link-review status is pending. No separate user request is required.

## Method

1. Search the complete current Library using the record ID, title, names, organisations, systems, source references, explicit IDs, tags and distinctive subject terms. Include generated relationship candidates only as hypotheses.
2. Complete the confirmed layer first. Open every plausible canonical record and classify each candidate from direct evidence as confirmed, rejected or unresolved. Similarity, co-occurrence, graph proximity and transitive connections are not confirmation.
3. Apply exactly one confirmed result:
   - `links_created`: add every directly supported relationship to both live endpoints in the same candidate, record required relationship evidence, and verify the mirrored edit changed nothing unrelated.
   - `no_supported_links`: leave the link set unchanged and record the searches performed, candidates inspected, rejection or unresolved reason, and an explicit statement that no new supported relationship was found; verify any existing confirmed links rather than describing them as absent.
4. Only after the confirmed result is complete, assess the secondary contextual layer. Select the strongest useful overlaps in subject, business context, system, method, analogous problem or reusable precedent. A contextual candidate needs a concise retrieval benefit and must not contradict either record; it does not need direct relationship evidence.
5. Apply exactly one contextual result:
   - `contextual_links_created`: add a reciprocal bullet to each endpoint's `## Contextual links` section using ``- `<ID>` — `<basis>` — <why this may help future work>.`` Allowed bases are `shared_subject`, `shared_context`, `shared_system`, `shared_method`, `analogous_problem` and `reusable_precedent`. Keep only useful candidates and never copy them into frontmatter `links` or the confirmed ledger.
   - `no_contextual_links`: leave contextual sections unchanged and record the subject/context search and why no candidate offered a useful retrieval path.
6. Record a dated `## Link review` section in the reviewed record with both results, searches, confirmed links, contextual links, rejected or unresolved candidates and the basis for each conclusion. Where the record type has link-review frontmatter, update it consistently only after both layers are complete.
7. Parse the complete frontmatter, verify every confirmed link and contextual pointer has a live reciprocal endpoint, confirm the two stores remain separate, and stop when both selected results are complete.

An incomplete search, unavailable endpoint, malformed record, missing confirmed evidence or missing contextual rationale is not a negative result. Preserve the review as incomplete and follow the applicable blocker route without inventing either kind of relationship.

## Benchmark case

Given a new record with `links: []`, the AI first searches for direct evidence. Direct evidence confirming a Project relationship produces reciprocal frontmatter links and `links_created`; no direct support produces `no_supported_links`. It then separately assesses contextual usefulness: a shared system and analogous problem may produce reciprocal `## Contextual links` bullets and `contextual_links_created`, while no useful retrieval path produces `no_contextual_links`. A failed or partial layer produces no result for that layer.

## Stop

Stop only after one confirmed result and one contextual result are recorded. Contextual links must remain visibly advisory and separate from the confirmed graph.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`; the existing reciprocal Skill links remain supported and no new confirmed relationship was found.
- Contextual result: `no_contextual_links`; every useful current candidate is already represented by a confirmed link, so a duplicate advisory pointer would add no retrieval value.

## Cleanup integration — 15 November 2026

PLAY-0075 is the chat-scoped Cleanup caller approved for creation by the Library owner. Its operation preserves the agreed fresh AGENTS read → source preparation → final-candidate validation → scratch deletion order. This association grants no execution authority; changed workflow dependencies require fresh qualification before invocation.

RELATIONSHIP-EVIDENCE: PLAY-0071--PLAY-0075 | related_to | undirected | user_confirmed | supports
