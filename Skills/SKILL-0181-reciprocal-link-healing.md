---
id: SKILL-0181
type: skill
title: Reciprocal Link Healing
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["run link healer", "check reciprocal closure", "auto heal links"]
links: []
tags: [skill, library-mechanics, links, automation]
---

# Reciprocal Link Healing

Runs or checks deterministic reciprocal-link closure.

## When to use

Use when reconciling declared reciprocal edges with `auto_heal_links.py`.

## Method

1. Run write mode only in an authorised reconciliation context; use `--check` for read-only debt detection.
2. Allow closure to repeat until no additions remain.
3. Run a second check to confirm idempotence.
4. Do not expect the healer to create evidence, inferred signals or guessed mappings.

## Decision and evidence details

Retain the authorised mode, input source state, tool output and exact changed-file diff. Confirm the second check demonstrates no remaining additions and distinguish deterministic navigation closure from relationship-evidence creation.

Boundary design case: an endpoint cannot be resolved. Preserve the reported debt and route the mapping/evidence gap; do not invent the target or repeat write mode blindly. Read-only --check detects debt without authorising its repair.

## Benchmark case

A declared A→B edge produces B→A once; a second run produces no byte change.

## Anti-patterns

- Using the healer to invent relationships
- Treating a pending legacy ID as a defect to force closed
- Accepting a non-idempotent second run

## Stop

Stop at deterministic closure or on an unresolved endpoint/mapping that requires evidence.
