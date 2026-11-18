---
id: SKILL-0200
type: skill
title: Failed-Candidate Learning Receipt
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["failed candidate receipt", "candidate repair learning", "failed predecessor analysis"]
links: []
tags: [skill, library-mechanics, learning, repair]
---

# Failed-Candidate Learning Receipt

Records the required learning analysis after a failed consolidated candidate run.

## When to use

Use when the immediate prior staging head has a failed candidate run and a changed-input repair commit is prepared.

## Method

1. Record each required field exactly once: event, reusable pattern, cause, prevention, disposition and reference.
2. Make pattern, cause and prevention specific to observable evidence.
3. Use `captured` only when the referenced canonical owner/path changes in the authored diff.
4. Use a specific `n/a` only for infrastructure-only or insufficient-evidence failures.
5. Do not omit analysis merely because the next run may pass.

## Decision and evidence details

Bind the receipt to the exact failed run/head, diagnosed evidence and prepared repair diff. Preserve infrastructure uncertainty separately from an authored defect; a later passing run does not establish the earlier cause. Inspect the current receipt contract for exact syntax before writing.

Boundary design case: failure logs are unavailable. Use the permitted specific insufficient-evidence disposition and gap; do not invent a parsing cause or claim a preventive rule was captured without an owner change.

## Benchmark case

A malformed frontmatter failure records the parsing cause and a bounded prevention control in the repair commit.

## Anti-patterns

- Generic failure wording
- Captured with an unchanged reference
- Skipping the receipt after an input repair

## Stop

Stop when the repair commit contains one valid complete receipt.
