---
id: SKILL-0087
type: skill
title: Software Security Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [testing, security]
trigger_phrases: ["design security tests", "choose SAST DAST or fuzzing", "test permissions and misuse"]
---

# SKILL-0087 — Software Security Test Design

## Purpose

Select security checks that target the actual exposure introduced or changed by software.

## When to use

Use for: design security tests; choose SAST DAST or fuzzing; test permissions and misuse.

## Method

1. Map assets, trust boundaries, identities, inputs and permissions affected.
2. Identify realistic abuse and failure cases.
3. Choose dependency scanning, SAST, DAST, fuzzing, role tests or misuse cases that discriminate those risks.
4. Define safe execution constraints and evidence.
5. State residual exposure that automated checks cannot prove.

## Benchmark case

For a writeback endpoint, test unauthorised roles, tampered identifiers, invalid payloads and audit behaviour instead of treating a generic scanner as sufficient.

Boundary design case: a useful abuse test would reach a production identity or target outside the authorised scope. Keep it as an unexecuted scoped requirement and identify the missing authority or safe test environment; do not infer permission from the need for security evidence.

## Anti-patterns

- Treating a scanner pass as application security proof.
- Testing outside authorised scope.
- Ignoring permission-boundary behaviour.

## Stop

Stop with scoped cases, required authority and residual risk.
