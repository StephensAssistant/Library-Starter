---
id: SKILL-0176
type: skill
title: Relationship Evidence Recording
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["record relationship evidence", "relationship direction evidence", "relationship provenance"]
links: []
tags: [skill, library-mechanics, relationships, evidence]
---

# Relationship Evidence Recording

Records permanent evidence for a relationship’s type, direction or provenance.

## When to use

Use only when a relationship needs more than a reciprocal navigation link.

## Method

1. Confirm both endpoints exist and the relationship is evidenced.
2. Pin an exact Git blob SHA and a resolvable anchor at the canonical path.
3. Add the matching `RELATIONSHIP-EVIDENCE:` declaration to the source record.
4. Append a unique ledger entry; never rewrite history except a qualifying later contradiction resolution.
5. Interpret direction literally against the ledger’s canonical sorted endpoints.

## Decision and evidence details

Before appending, inspect existing entry identifiers and the exact declaration/anchor so an interrupted prior attempt is not duplicated. Read back the authorised source and ledger changes and compare endpoint order, literal direction and pinned provenance. An uncertain append outcome requires state inspection before retry.

Boundary design case: both endpoints exist but no resolvable source anchor supports direction. Leave that direction unresolved; endpoint validity alone does not justify a directed evidence entry.

## Benchmark case

Given an evidenced directed dependency, records a pinned source declaration and ledger entry without reversing the edge or editing prior evidence.

## Anti-patterns

- Using generated output as evidence
- Adding evidence merely to admit a navigation link
- Reusing evidence IDs or sequence numbers

## Stop

Stop when the append-only entry and source declaration agree, or when provenance/direction is unresolved.
