---
id: SKILL-0084
type: skill
title: Code Intent Documentation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0008]
tags: [coding, evidence-first]
trigger_phrases: ["document non-obvious code", "add useful code comments", "explain an implementation invariant"]
---

# SKILL-0084 — Code Intent Documentation

## Purpose

Add concise notation for non-obvious intent, invariants, business rules, workarounds and cross-system contracts.

## When to use

Use for: document non-obvious code; add useful code comments; explain an implementation invariant.

## Method

1. Identify knowledge a competent reader cannot infer from names and structure.
2. Document why the constraint exists, not what syntax does.
3. Follow repository conventions for headers and notation.
4. Remove or avoid redundant comments that can drift.
5. Keep external operational detail in its canonical runbook.

## Benchmark case

Add one comment explaining why a business-key join replaces a misleading surrogate-key match, without narrating every SQL clause.

Near-miss design case: the proposed comment merely repeats a clear assignment, while the claimed business reason is unverified. Omit the redundant narration and identify any decision-changing knowledge gap; do not add a persuasive but unsupported invariant that future maintainers may trust.

## Anti-patterns

- Commenting every line.
- Restating syntax.
- Moving runbook content into code.
- Documenting unsupported assumptions as facts.

## Stop

Stop when future maintainers can understand the non-obvious constraint without comment noise.
