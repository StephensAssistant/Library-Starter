---
id: SKILL-0182
type: skill
title: Link Mirror Rewrite Verification
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["verify mirrored link rewrite", "whole file link edit", "reciprocal endpoint rewrite"]
links: []
tags: [skill, library-mechanics, links, verification]
---

# Link Mirror Rewrite Verification

Verifies a whole-file reciprocal-link edit changed nothing unrelated.

## When to use

Use when a write tool requires rewriting the complete reciprocal endpoint file.

## Method

1. Read the current endpoint immediately before editing.
2. Copy every unrelated line verbatim; alter only `links` and, when appropriate, `updated`.
3. Write using the current file SHA.
4. Read back and compare against the pre-edit content.
5. Reject the edit if any unrelated field or prose changed.

## Decision and evidence details

Retain the pre-edit identity/content, intended link delta and exact readback diff. If readback contains unrelated changes, report the actual saved state and stop acceptance. Any repair must preserve current concurrent work and stay within authority; a rejected comparison does not itself authorise overwriting the endpoint.

Boundary design case: the link is correct but unrelated prose changed during the rewrite. Keep verification failed until the bounded intended diff is proven.

## Benchmark case

A reciprocal update may change only the authorised link list and update date. Any change to trigger phrases fails verification.

## Anti-patterns

- Reconstructing frontmatter from memory
- Accepting a harmless-looking unrelated change
- Skipping readback

## Stop

Stop only when the intended minimal diff is proven.
