---
id: SKILL-0282
type: skill
title: OpenFlow Checkpoint and Watermark Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific, openflow, checkpoint, watermark]
trigger_phrases: ["OpenFlow checkpoint", "OpenFlow watermark", "resume OpenFlow load"]
---

# OpenFlow Checkpoint and Watermark Design

Design replay-safe persisted checkpoints and watermark advancement for one OpenFlow source.

## When to use

Use when an OpenFlow flow must resume after interruption or load incrementally without gaps, including overlap, replay, duplicate and zero-row behaviour.

## Intent-routing contract

This Skill owns checkpoint state, watermark boundaries and replay safety. Route page traversal and cursor mechanics to SKILL-0208.

## Method

1. Define the source change field or durable position represented by the watermark.
2. Record the initial checkpoint, inclusive/exclusive boundary and timezone or ordering semantics.
3. Set an evidence-based overlap window and deterministic duplicate-handling rule.
4. Persist the next checkpoint only after the corresponding output is durably committed. Specify and verify a serialization or concurrency guard so a stale or overlapping run cannot overwrite the committed position.
5. Preserve the prior checkpoint when a page, transformation or destination write fails. On an ambiguous output commit or checkpoint update, reconcile actual durable output and stored checkpoint before retry; do not assume a failed call left either unchanged.
6. Define zero-row behaviour without advancing beyond an unverified source boundary.
7. Prove interruption replay, late-arriving data, repeated-run, stale concurrent update and ambiguous-commit outcomes.

## Evidence expected

Retain checkpoint values, boundary semantics, overlap, commit evidence, duplicate rule, replay test and unresolved source limitations.

## Benchmark case

An Orders flow fails after writing a page but before checkpoint advancement; rerunning from the prior watermark replays safely, deduplicates deterministically and skips no records.

Boundary design case: A zero-row response has no verified complete source boundary. Preserve the prior checkpoint and investigate the source evidence; an empty page alone cannot justify advancing the watermark.

## Anti-patterns

- Advancing the watermark before durable output
- Treating the latest observed timestamp as a complete boundary
- Using overlap without deterministic duplicate handling
- Moving the checkpoint after an unverified zero-row response

## Stop

Stop when replay and late-arrival tests prove no gaps with bounded duplicates, or when the source lacks a trustworthy checkpoint field or durable commit evidence.


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
