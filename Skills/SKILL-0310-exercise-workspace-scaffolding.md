---
id: SKILL-0310
type: skill
title: Exercise Workspace Scaffolding
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["scaffold a coding exercise workspace", "create exercise solution pairs"]
---

# Exercise Workspace Scaffolding

Create consistent educational exercise/solution workspaces using the project’s actual toolchain and learning objective.

## When to use and intent routing contract

Activate for scaffold a coding exercise workspace, create exercise solution pairs or equivalent intent. Exclude solve all exercises automatically, install an unavailable private scaffolding CLI. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Inspect package scripts, module conventions, naming, test runner and an existing exercise. Confirm the learner objective, starting knowledge and success behaviour; avoid introducing a new toolchain by default.
2. Create paired exercise and solution locations with stable names, runnable entry points and a small focused task. Keep the starting exercise incomplete only at the intended learning seam; make the solution readable and explicit.
3. Separate learner instructions, hints, tests and instructor solution. Avoid revealing the solution in the default exercise view. Use the existing scaffold mechanism or direct file creation rather than assuming the author’s private CLI exists.
4. Verify imports, scripts and tests in the solution; verify the exercise fails or remains incomplete for the intended reason while infrastructure works. Keep dependency changes and exercise scope within authority.

## Anti-patterns

- An exercise blocked by unrelated setup failure, or a solution hidden in the starter comments.
- Installing private/unknown tooling solely because upstream uses it.

## Benchmark cases

- Positive: Create a TypeScript parsing exercise and working solution under the repository’s current test scripts.
- Negative/boundary: Do not generate a multi-module course when one exercise was requested.

## Stop

Stop with a reproducible start command, intended task and verified solution. Delegate teaching pace and assessment to the learning owner.


## Source adaptation — 2026-10-10

[scaffold-exercises](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/scaffold-exercises/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0311` — `shared_method` — Connects exercise workspace scaffolding with pre-commit gates for reusable quality-controlled workspaces.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
