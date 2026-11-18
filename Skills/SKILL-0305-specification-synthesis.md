---
id: SKILL-0305
type: skill
title: Specification Synthesis
status: current
created: 2026-10-10
updated: 2026-11-01
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["synthesise an implementation specification", "turn decisions into a build spec"]
---

# Specification Synthesis

Convert established decisions and evidence into an implementation-ready behavioural contract without duplicating the project’s canonical source of truth.

## When to use and intent routing contract

Activate for synthesise an implementation specification, turn decisions into a build spec or equivalent intent. Exclude unresolved product decision, implementation already requested without need for new spec. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Locate the agreed goal, domain model, constraints, repository conventions and outstanding decisions. Distinguish confirmed requirements from proposals; carry unresolved choices explicitly rather than selecting them silently.
2. State observable behaviour, inputs/outputs, invariants, failure cases, compatibility, security and non-goals. Specify acceptance examples with independent expected results and evidence sources.
3. Describe architecture boundaries and integration points only as far as necessary to constrain behaviour. Identify migration sequencing, rollback needs and risky assumptions; avoid line-by-line coding instructions.
4. Check the specification against actual code and stakeholder decisions. Save or update the existing canonical specification when authorised; give planning a stable reference and mark what still prevents implementation.

## Anti-patterns

- Treating a brainstorm as approved scope.
- A spec that repeats a ticket while leaving error handling and acceptance undefined.

## Benchmark cases

- Positive: Convert an agreed import flow into success, duplicate-input and malformed-file acceptance cases.
- Negative/boundary: Keep an undecided data-retention period as a business question rather than inventing a default.

## Stop

Stop with a traceable contract and open questions, or hand off an already authorised complete spec. Do not publish, implement or send it merely because synthesis is complete.


## Source adaptation — 2026-10-10

[to-spec](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0297` — `shared_method` — Connects diagram design with specification synthesis so future specifications can pair precise prose with explanatory visuals.
- `SKILL-0304` — `shared_method` — Connects domain-language design with specification synthesis so future requirements preserve consistent concepts.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 2 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.


## Addy Osmani method extension — 2026-11-01

Before synthesising a specification, check whether the accepted request contains independently testable capabilities. Map each capability to its observable outcome, inputs/outputs, boundary, dependencies and acceptance examples; retain shared invariants explicitly. Use this map to separate specification units where the acceptance or authority boundary differs, then hand sequencing to the existing planning owners. A capability map does not approve unresolved product choices, create extra scope or require a new file for each capability. Reuse settled decisions and the existing canonical specification.

Source: [spec-driven-development](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/spec-driven-development/SKILL.md), revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/spec-driven-development/SKILL.md`; licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`. Adapted method only; source text grants no additional authority, runtime installation, workflow invocation or operational acceptance.
