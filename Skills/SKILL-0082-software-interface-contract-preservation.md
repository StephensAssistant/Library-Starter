---
id: SKILL-0082
type: skill
title: Software Interface Contract Preservation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0008]
tags: [coding, evidence-first]
trigger_phrases: ["preserve code interfaces", "check downstream contracts before refactoring", "protect data aliases and payloads"]
---

# SKILL-0082 — Software Interface Contract Preservation

## Purpose

Identify and preserve the interfaces that consumers rely on during a software change.

## When to use

Use for: preserve code interfaces; check downstream contracts before refactoring; protect data aliases and payloads.

## Method

1. Inventory public parameters, return behaviour, field aliases, schemas, filenames, payloads, ordering and side effects.
2. Trace affected consumers and compatibility expectations.
3. Mark each contract preserved, intentionally changed or unresolved.
4. Add focused contract verification to the change.

## Benchmark case

Before migrating a Qlik source, preserve expected aliases, QVD names and field types while changing only the data provider.

Boundary design case: a field rename is explicitly requested but one affected consumer is unreadable. Mark that consumer contract unresolved and limit the compatibility claim; do not infer preservation from compilation or silently drop the observed dependency to complete the map.

## Anti-patterns

- Equating technical validity with compatibility.
- Renaming outputs incidentally.
- Ignoring undocumented but observed consumers.

## Stop

Stop with a contract map and evidence that each affected interface is preserved or explicitly authorised to change.
