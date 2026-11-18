---
id: SKILL-0058
type: skill
title: Sigma Guarded Object Mutation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265]
tags: [skill, sigma, automation, mutation]
trigger_phrases: [update sigma object, mutate sigma object safely, change sigma object by api]
---

# Sigma Guarded Object Mutation

Apply one authorised Sigma object mutation while preserving its current content and concurrency boundary.

## Intent-routing contract

Activate only for an approved programmatic update to an existing Sigma object. Object discovery, export and mechanism selection are separate Skills.

## When to use

Use after the exact Sigma object, intended change, mechanism, access and authority are verified.

## Method

1. Retrieve the current object representation, identifier, schema and concurrency token where supported.
2. Define the smallest authorised change and preserve every unrelated field.
3. Apply optimistic concurrency or the platform's full-content mutation safeguard.
4. Stop on stale state, schema drift, missing authority or an unsupported mutation.
5. Read back the object and verify the intended change and absence of unrelated mutation.

## Benchmark case

An approved workbook-object update uses its current ID and representation, changes only the named property and reads the object back to prove no unrelated field changed.

Failure design case: a mutation times out without a definitive response. Read the current object and compare the intended property and unrelated fields before any retry; preserve concurrent changes and report uncertain effects rather than reapplying a stale full-content representation.

## Anti-patterns

- Inventing object IDs, schemas or mutation support.
- Updating from a stale representation.
- Treating syntactic acceptance as behavioural verification.
- Combining discovery, export or mechanism selection with mutation.

## Stop

Stop after the authorised mutation is read back and verified, or at the precise stale-state, capability, access or authority gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0058--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0058--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0058--SKILL-0265 | related_to | undirected | user_confirmed | supports
