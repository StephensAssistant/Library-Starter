---
id: SKILL-0179
type: skill
title: Raw Artifact Reciprocal-Link Resolution
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["link raw artifact", "artifact companion reciprocity", "stored_at relationship"]
links: []
tags: [skill, library-mechanics, links, artifacts]
---

# Raw Artifact Reciprocal-Link Resolution

Routes a raw Artifact’s reciprocal relationship to its Markdown companion.

## When to use

Use when a governed link targets a raw Artifact ID backed by a `stored_at` companion.

## Method

1. Resolve the raw Artifact’s Markdown companion through `stored_at`.
2. Validate both the raw Artifact and companion.
3. Place the reciprocal edge on the companion, not the binary/raw file.
4. Verify the originating record and companion form the required reciprocal pair.

## Decision and evidence details

Retain the raw Artifact ID, exact stored_at resolution and verified Markdown companion identity. Read back both the originating record and companion after authorised edits, checking that the reciprocal edge is on the resolved companion and the raw content is unchanged.

Boundary design case: stored_at is absent, ambiguous or resolves to an unrelated file. Stop the reciprocal write and report that mapping gap; a filename resemblance is not a substitute.

## Benchmark case

A Project links to a raw CSV Artifact; the reciprocal Project link is written to that Artifact’s Markdown companion.

## Anti-patterns

- Editing a raw binary to carry frontmatter
- Mirroring onto an unrelated companion by filename guess

## Stop

Stop when `stored_at` resolves uniquely and the companion owns the reciprocal edge.
