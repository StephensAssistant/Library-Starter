---
id: SKILL-0007
type: skill
title: Minimal Code Change Implementation
status: current
created: 2026-08-22
updated: 2026-11-01
links: [SKILL-0008, SKILL-0085, SKILL-0086, SKILL-0087, SKILL-0088, SKILL-0089, SKILL-0090, SKILL-0091, SKILL-0092, SKILL-0093, SKILL-0094, SKILL-0278, SKILL-0279, SKILL-0280, SKILL-0281, PLAY-0015]
tags: [coding, implementation, surgical-change]
trigger_phrases: ["implement this code change", "make the smallest code change", "add this feature without refactoring", "apply this fix"]
source_skill: karpathy-coding
migrated_from: SKILL-0007-old-library
---

# SKILL-0007 — Minimal Code Change Implementation

## Purpose

Implement the smallest code change that satisfies an evidenced requirement while preserving adjacent behaviour and established style.

## When to use

Use after the target, contracts, expected outcome and relevant verification have been identified.

## Method

1. Translate the requirement into the smallest affected surface and observable success criterion.
2. Follow the existing local pattern when it safely satisfies the requirement.
3. Change only lines traceable to the outcome or a required correctness fix.
4. Preserve public contracts, schemas, aliases, ordering, filenames and downstream interfaces unless their change is explicit.
5. Remove only dead code directly orphaned by the change.
6. Run the selected focused verification and report evidence rather than successful execution alone.

## Benchmark case

Given a defect in one transformation, change the earliest correctable expression while retaining consumer aliases and unrelated structure, then prove the affected output and its nearest regression case.

Boundary design case: the smallest apparent fix would rename a consumer alias without authority. Preserve the interface and investigate a compatible fix; if none is evidenced, report that specific contract decision instead of silently enlarging the implementation scope.

## Anti-patterns

- Speculative frameworks or configuration.
- Drive-by refactoring.
- Changing consumer contracts unintentionally.
- Expanding scope because adjacent cleanup is attractive.
- Reporting “it ran” as proof it works.

## Stop

Stop when the minimal diff meets the observable criterion and relevant regression evidence, or when a material unresolved gap makes implementation unsafe.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0007 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0008 | related_to | undirected | authoritative_record | supports

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0278 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0279 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0280 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0281 | related_to | undirected | user_confirmed | supports



## Addy Osmani method extension — 2026-11-01

For explicitly requested behaviour-preserving simplification, the requested clarity improvement is the scoped outcome. Inspect the current behaviour and caller contracts first; prefer clearer names, guard clauses, reduced duplication and established local patterns only where they improve understanding. Preserve errors, ordering, side effects and public interfaces as well as return values. Make bounded changes and use focused checks against independently stated before/after behaviour. Fewer lines, a passing build or a cleaner appearance alone do not prove preservation. Unrelated cleanup and architectural rewrites remain outside scope; an evidenced behaviour change needs its own requirement and authority.

Source: [code-simplification](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/code-simplification/SKILL.md), revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/code-simplification/SKILL.md`; licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`. Adapted method only; source text grants no additional authority, runtime installation, workflow invocation or operational acceptance.
