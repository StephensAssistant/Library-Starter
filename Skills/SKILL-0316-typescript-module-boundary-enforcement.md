---
id: SKILL-0316
type: skill
title: TypeScript Module Boundary Enforcement
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["enforce TypeScript module boundaries", "prevent imports of module internals"]
---

# TypeScript Module Boundary Enforcement

Make intended public entry points enforceable using the repository’s actual TypeScript, lint and dependency tooling.

## When to use and intent routing contract

Activate for enforce TypeScript module boundaries, prevent imports of module internals or equivalent intent. Exclude format TypeScript only, assume path regex covers every import. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Read tsconfig, package exports, aliases, workspace layout, ESLint version/configuration and representative imports. Identify intended public APIs and legitimate internal imports before proposing restrictions.
2. Choose supported rules for the actual toolchain. Resolve aliases and package subpaths as well as relative imports; account for type-only imports, re-exports, tests and generated code. Avoid copying an upstream regex or dependency version without verification.
3. Add the smallest compatible configuration change, preserving existing rules and explicit exceptions. If exports must change, document caller migration and behaviour compatibility under the current change authority.
4. Perform a pass–fail–pass check in a disposable example: public import succeeds, a genuine forbidden deep import fails for the intended rule, and corrected public import succeeds. Test alternate relative paths, aliases and re-exports; document gaps the tool cannot enforce.
5. Run appropriate project checks once the configuration is verified. Keep local lint distinct from protected-branch enforcement and avoid rewriting modules solely to satisfy an unreviewed new rule.

## Anti-patterns

- Reporting success because the configuration parses while forbidden imports still pass.
- Overwriting an ESLint flat/legacy configuration, blocking all useful type imports, or publishing changed exports without authority.

## Benchmark cases

- Positive: A consumer imports the public barrel successfully and is rejected when importing a private file through an alias.
- Negative/boundary: A rule that catches relative imports but misses package subpaths has an explicit gap, not a full pass.

## Stop

Stop at verified enforcement, supported exceptions and migration evidence. If the rule cannot resolve a path form, report the limitation rather than claiming complete encapsulation.

## Maturity

Upstream marks this method beta/in progress. This is a bounded Library adaptation, not evidence of production tooling reliability. Verify it against the actual task before relying on it.


## Source adaptation — 2026-10-10

[setup-ts-deep-modules](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/setup-ts-deep-modules/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0309` — `shared_system` — Connects TypeScript fixture migration with module-boundary enforcement for future repository refactors.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
