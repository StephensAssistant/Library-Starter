---
id: SKILL-0303
type: skill
title: Architecture Friction Survey
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["survey codebase architecture friction", "find deep module opportunities"]
---

# Architecture Friction Survey

Discover and rank evidenced module-boundary improvements before selecting a bounded architecture change.

## When to use and intent routing contract

Activate for survey codebase architecture friction, find deep module opportunities or equivalent intent. Exclude one reproducible bug only, unrequested architecture rewrite. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Survey representative entry points, call sites, tests and repository conventions read-only. Follow dependencies rather than ranking files by size. Record exact paths and examples of repeated caller burden.
2. For each candidate, describe the responsibility split, leaked knowledge, proposed deeper boundary, affected callers, dependency/testability trade-off and compatibility risk. Separate observed evidence from inferred maintenance cost.
3. Compare alternative boundaries, including doing nothing. Rank by caller simplification, cohesion, migration size and evidence strength; do not invent numeric benefits without measurements.
4. Produce a concise candidate report with diagrams only where topology helps. Select a bounded candidate under the current task authority and hand it to the design/implementation owners; broader changes remain proposals.

## Anti-patterns

- Treating every dependency as harmful or promising cost savings without evidence.
- Automatically opening issues, refactoring all candidates or generating an unsolicited web report.

## Benchmark cases

- Positive: Repeated parsing and retry logic across three callers yields a documented boundary candidate with caller examples.
- Negative/boundary: A request to fix one assertion failure does not trigger a repository-wide rewrite.

## Stop

Stop at an evidence-backed ranked shortlist and clear scope. If source access is incomplete, mark missing evidence instead of declaring architecture defects.


## Source adaptation — 2026-10-10

[improve-codebase-architecture](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/improve-codebase-architecture/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0302` — `reusable_precedent` — Connects deep module design with architecture-friction discovery so future refactoring can move from diagnosis to structure.
- `SKILL-0304` — `shared_method` — Connects architecture-friction analysis with domain-language design for future boundary and naming work.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 2 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
