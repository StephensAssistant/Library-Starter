---
id: SKILL-0309
type: skill
title: TypeScript Test Fixture Migration
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["migrate test fixtures to shoehorn", "remove unsafe casts from test fixtures"]
---

# TypeScript Test Fixture Migration

Replace sprawling test-only type assertions with explicit, maintainable fixture construction while preserving behaviour and type feedback.

## When to use and intent routing contract

Activate for migrate test fixtures to shoehorn, remove unsafe casts from test fixtures or equivalent intent. Exclude production type assertions, suppress a real domain mismatch. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Inventory assertions in tests and understand which fields each scenario exercises. Distinguish deliberate incomplete fixtures from invalid production data or a broken domain type.
2. Inspect the package manager, existing fixture helpers and current official library documentation before changing dependencies. Use a test/development-only dependency if shoehorn is justified; otherwise retain or improve an existing typed builder.
3. Migrate a small representative fixture first. Specify behaviour-relevant fields explicitly, centralise safe defaults and avoid a generic casting escape hatch spreading into production. Never use fixture convenience to silence genuine mismatches.
4. Run relevant type checks and tests; confirm omitted/overridden fields retain the original scenario. Migrate remaining similar tests mechanically within scope and inspect the diff for assertions still masking an error.

## Anti-patterns

- Blindly copying an outdated package API, introducing runtime production casts, or removing checks until tests compile.
- Tests that succeed only because a mocked object no longer represents the scenario.

## Benchmark cases

- Positive: Replace a long partial customer assertion in a unit test with a test-only fixture exposing the fields the test uses.
- Negative/boundary: An as Customer cast in production is a correctness question, not a shoehorn migration target.

## Stop

Stop when fixture intent, type-check evidence and scenario behaviour are preserved. Escalate a domain inconsistency instead of casting it away.


## Source adaptation — 2026-10-10

[migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/migrate-to-shoehorn/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0316` — `shared_system` — Connects TypeScript fixture migration with module-boundary enforcement for future repository refactors.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
