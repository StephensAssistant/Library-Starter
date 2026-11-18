---
id: SKILL-0178
type: skill
title: Directional Chat Provenance Linking
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["link chat provenance", "chat outbound link", "daily chat relationship"]
links: []
tags: [skill, library-mechanics, links, chat]
---

# Directional Chat Provenance Linking

Adds outbound provenance links from a Chat without reciprocal mirroring.

## When to use

Use when a Chat discussed, relied on or produced another governed record.

## Method

1. Confirm the target endpoint and ID are valid.
2. Add the target only to the Chat’s outbound links.
3. Do not add the Chat back to the target.
4. Retain all syntax, endpoint and provenance checks; only reciprocity is waived.

## Decision and evidence details

Retain the Chat identity, target identity and evidence that the Chat discussed, relied on or produced the target. Read back the outbound link and verify the target received no reciprocal Chat edge.

Near-miss design case: a Project, rather than a Chat, links to another record. Do not apply this Chat-only reciprocity waiver. Missing target/provenance evidence blocks the affected Chat link even though mirroring is waived.

## Benchmark case

A dated Chat links to a Ticket it produced. The Ticket does not gain a reciprocal link to the Chat.

## Anti-patterns

- Mirroring a Chat link onto its target
- Waiving endpoint validation because the edge is directional

## Stop

Stop when the outbound Chat link is valid and the target remains unchanged.
