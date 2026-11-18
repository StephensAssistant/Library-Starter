---
id: SKILL-0302
type: skill
title: Deep Module Design
status: current
created: 2026-10-10
updated: 2026-11-01
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["design a deep module", "reduce interface complexity"]
---

# Deep Module Design

Design a small caller-facing interface that hides substantial coherent implementation complexity. Compare module depth by responsibilities and caller effort, not line count.

## When to use and intent routing contract

Activate for design a deep module, reduce interface complexity or equivalent intent. Exclude cosmetic code formatting, rewrite an unrelated subsystem. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Read the actual callers, public contracts, failure modes and change history. Name the difficult knowledge currently duplicated or exposed; distinguish unavoidable domain complexity from accidental plumbing.
2. Sketch at least two genuinely different interfaces before choosing. For each, show a realistic caller example, invariants, lifecycle, errors, dependencies and what implementation knowledge remains hidden.
3. Choose the boundary that groups related knowledge and makes callers simpler without hiding policy choices callers must control. Keep unrelated responsibilities outside it. Prefer explicit domain operations to configurable wrappers around every internal function.
4. Plan compatible migration of callers and contract-level tests. Check that internals can change without caller edits and that failure behaviour remains observable. Implement only within the authorised change scope.

## Anti-patterns

- Equating depth with a large file, abstraction count or fewer exported symbols.
- A forwarding wrapper that preserves all incidental complexity, or a universal options object.

## Benchmark cases

- Positive: Two callers duplicate transaction/error plumbing; propose a narrow domain operation and compare it with the current low-level API.
- Negative/boundary: A formatting-only task does not authorise a new architecture; retain the existing public interface.

## Stop

Stop when alternative designs, caller examples, invariants and migration risks are reviewable. Hand off implementation to the coding owner; stop on an unresolved externally visible contract change.


## Source adaptation — 2026-10-10

[codebase-design](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0303` — `reusable_precedent` — Connects deep module design with architecture-friction discovery so future refactoring can move from diagnosis to structure.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.


## Addy Osmani method extension — 2026-11-01

For a proposed caller-facing boundary, include concrete valid and invalid request/response examples, error semantics, validation ownership and compatibility expectations in the competing designs. Distinguish input accepted from a caller from output guaranteed by the module; validate untrusted input at the relevant boundary. Where duplicate mutations are possible, specify operation identity, idempotency-key scope, changed-payload reuse, concurrent duplicate handling and failed or uncertain outcomes rather than claiming a key alone prevents duplication. Verify platform-specific REST, GraphQL, schema and persistence mechanisms against the actual implementation before adopting them. This adds contract-design questions; it does not turn module design into a complete endpoint implementation or authorise changing an existing consumer contract.

Source: [api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/api-and-interface-design/SKILL.md), revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/api-and-interface-design/SKILL.md`; licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`. Adapted method only; source text grants no additional authority, runtime installation, workflow invocation or operational acceptance.
