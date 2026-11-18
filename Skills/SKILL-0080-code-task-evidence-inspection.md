---
id: SKILL-0080
type: skill
title: Code Task Evidence Inspection
status: current
created: 2026-09-20
updated: 2026-10-31
links: [PLAY-0006, SKILL-0008]
tags: [coding, evidence-first]
trigger_phrases: ["inspect before coding", "analyse a code change request", "identify code assumptions"]
---

# SKILL-0080 — Code Task Evidence Inspection

## Purpose

Establish the known code, contracts, tests, failure evidence and material gaps before implementation.

## When to use

Use for: inspect before coding; analyse a code change request; identify code assumptions.

## Method

1. Read the current target and relevant callers, schemas, tests and logs.
2. Separate observed facts from inference.
3. Identify public and downstream contracts.
4. Name only assumptions that affect the next action.
5. Investigate discoverable facts first. When a remaining material human-owned decision changes the next action or makes it unsafe, use SKILL-0318 to ask the one highest-leverage decision-changing question. Keep dependent actions blocked until the answer and its consequences are verified, then reassess before asking another question. Group questions only when the Library owner explicitly requests a batch or the inputs are genuinely inseparable for the same immediate action.

## Benchmark case

Before altering an unfamiliar procedure, inspect its parameters, callers and failing evidence, then identify the smallest affected surface without inventing columns.

Boundary design case: a caller contradicts the proposed parameter assumption. Preserve the observed caller contract and locate the governing requirement before implementation; do not treat a plausible change request or a missing test as proof that the existing consumer is wrong.

## Anti-patterns

- Guessing unseen code or schemas.
- Asking for facts available in the repository.
- Blocking on immaterial unknowns.

## Stop

Stop with an evidence map, material assumptions and implementation boundary.
