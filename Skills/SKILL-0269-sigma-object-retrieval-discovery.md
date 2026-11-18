---
id: SKILL-0269
type: skill
title: Sigma Object Retrieval and Discovery
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050]
tags: [skill, sigma, automation, discovery]
trigger_phrases: [find sigma object id, retrieve sigma object, inspect sigma object schema]
---

# Sigma Object Retrieval and Discovery

Resolve and retrieve an existing Sigma object and its current machine-readable contract.

## Intent-routing contract

Activate only when an existing Sigma object, identifier or schema must be discovered or retrieved. Mutation, export and mechanism selection are separate Skills.

## When to use

Use before automation that requires an exact workbook, page, element, dataset or other supported Sigma object.

## Method

1. Verify the current authorised Sigma retrieval surface and authentication context.
2. Search or list with evidenced workspace, object-type and naming constraints.
3. Resolve the exact object ID; never infer it from a display name alone.
4. Retrieve the current representation and record its object type, schema, parent context and concurrency metadata where available.
5. Return ambiguity or missing access as an explicit gap rather than selecting a near match.

## Benchmark case

Two workbooks share a similar title. A passing application uses workspace and object metadata to identify the intended workbook, retrieves its exact ID and schema and leaves the other object untouched.

Boundary design case: Listing returns a workbook name and ID but the current object representation is inaccessible. Return identity evidence with the schema/access gap; do not invent fields or treat list metadata as its complete contract.

## Anti-patterns

- Inventing identifiers or schemas.
- Selecting the first fuzzy name match.
- Treating list metadata as the full object representation.
- Mutating or exporting during discovery.

## Stop

Stop with the exact retrieved object contract, or the precise identity, access or capability gap.
