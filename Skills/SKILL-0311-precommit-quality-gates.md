---
id: SKILL-0311
type: skill
title: Pre-commit Quality Gate Design
status: current
created: 2026-10-10
updated: 2026-11-01
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["set up precommit quality gates", "review precommit checks"]
---

# Pre-commit Quality Gate Design

Add fast, scoped pre-commit checks while preserving existing hooks, package conventions and independent CI enforcement.

## When to use and intent routing contract

Activate for set up precommit quality gates, review precommit checks or equivalent intent. Exclude commit or publish automatically, replace required CI with local hooks. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Inspect package manager, workspace layout, existing hook ownership and required CI checks. Determine which checks are fast enough for local feedback and which must remain full CI gates.
2. Choose existing supported tooling before adding dependencies. Scope formatting/lint checks to staged files safely, handle filenames with spaces and avoid unintended working-tree changes. Keep type-checking at the appropriate project boundary.
3. Merge configuration rather than overwrite it. Define failure messages, recovery and installation steps; a bypassable local hook is a convenience gate, never proof that protected-branch requirements passed.
4. In an isolated fixture, demonstrate a valid change passes, a deliberately invalid staged change fails for the expected reason, and the corrected change passes. Verify partial staging is not silently expanded. Run only checks authorised for the task.

## Anti-patterns

- Auto-committing after hook setup, staging unrelated changes, or reformatting the whole repository.
- Presenting a developer hook as tamper-proof enforcement.

## Benchmark cases

- Positive: Preserve the existing hook and add staged lint feedback with a failing and corrected example.
- Negative/boundary: A green local hook cannot substitute for an unrun required CI check.

## Stop

Stop at verified configuration and usable recovery instructions. Commit/push actions need their existing task authority; hook setup alone supplies none.


## Source adaptation — 2026-10-10

[setup-pre-commit](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/setup-pre-commit/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0299` — `shared_method` — Connects engineering harness design with pre-commit quality gates for future automated verification work.
- `SKILL-0310` — `shared_method` — Connects exercise workspace scaffolding with pre-commit gates for reusable quality-controlled workspaces.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 2 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.


## Addy Osmani method extension — 2026-11-01

When designing checks for an agreed quality bar, inspect changes to the bar itself as well as product code: new suppressions, skipped or deleted tests, removed assertions, unfinished stubs, lowered thresholds, changed measurement populations and new exclusions or exceptions. Compare both added and removed content in the actual candidate, including new files; a missing baseline or failed checker is unavailable evidence, not a clean result. Patterns are review signals, not proof of intent or complete enforcement. Distinguish a legitimate relocated test or equivalent assertion from an unexplained loss of coverage, and require evidence for that distinction.

Keep thresholds, measurement definitions and any permitted exceptions in their existing canonical contract. Define exception scope, reason, owner, review/expiry condition and required authority there; do not silently weaken an agreed constraint to obtain green checks. When no numerical target is agreed, a measured baseline can support a proposed no-regression ratchet, with direction and measurement noise stated explicitly; do not invent a target or promote the proposal to accepted policy. Verify representative clean, weakened-bar and checker-failure cases in an authorised isolated fixture before claiming enforcement. Existing local hooks remain bypassable and cannot substitute for independent CI; no upstream guard script, new constraints file, dependency or hook is installed by this method extension.

Source: [constraint-driven-development](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/constraint-driven-development/SKILL.md), revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/constraint-driven-development/SKILL.md`; licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`. Adapted method only; source text grants no additional authority, runtime installation, workflow invocation or operational acceptance.
