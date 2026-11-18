---
id: SKILL-0308
type: skill
title: Dangerous Git Command Guardrails
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["guard dangerous git commands", "review git execution safety controls"]
---

# Dangerous Git Command Guardrails

Design and verify execution controls for destructive Git operations without treating a text-pattern hook as a complete permission system.

## When to use and intent routing contract

Activate for guard dangerous git commands, review git execution safety controls or equivalent intent. Exclude ordinary read-only git inspection, assume a regex is a security boundary. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Identify protected repositories/branches and authorised operations. Inspect the actual runner and hook API. Distinguish read-only commands from reset/clean/checkout deletion, forced pushes and history rewriting; safety depends on flags, paths and repository context.
2. Place enforcement at the execution boundary with parsed argv and repository-aware policy where available. Require the governing authority for destructive operations. A shell-string regex is defence in depth only; fail closed when the command cannot be classified.
3. Test representative allowed reads and forbidden operations plus aliases, shell chaining, subshells, alternate flag forms, wrapper executables, git -C, environment variables and indirect scripts. Do not execute destructive test cases against real work.
4. Inspect existing configuration, make the smallest authorised change, and test policy activation in an isolated disposable fixture. Confirm configuration errors and missing hooks do not silently allow protected actions; document residual bypasses.

## Anti-patterns

- Installing the upstream shell regex as a guaranteed security barrier.
- Executing a dangerous command to prove it is dangerous, overwriting existing hooks, or granting forced-push authority.

## Benchmark cases

- Positive: Allow status/diff and deny a protected-branch force push in a disposable fixture.
- Negative/boundary: A shell wrapper or alias around reset must remain subject to the execution policy; a regex match alone is insufficient.

## Stop

Stop when the actual enforcement boundary, allowed/denied evidence and residual limitations are explicit. If policy cannot inspect an indirect command, deny or require the governing authority; do not claim comprehensive protection.


## Source adaptation — 2026-10-10

[git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/git-guardrails-claude-code/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0299` — `shared_context` — Connects engineering harness design with dangerous Git command guardrails for safer repository automation.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
