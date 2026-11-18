---
id: SKILL-0116
type: skill
title: Deterministic Extraction Caching
status: current
created: 2026-09-20
updated: 2026-10-17
links: []
tags: [ai, caching, extraction]
trigger_phrases: ["cache extraction", "incremental corpus processing", "content hash cache"]
---

# SKILL-0116 — Deterministic Extraction Caching

## Purpose

Cache deterministic corpus extraction safely and recompute only content affected by a verified change.

## Intent routing contract

Activate only for cache extraction, incremental corpus processing, content hash cache or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Key cached output by SHA-256 of source content plus extraction-policy version.
2. Treat corrupt, incomplete or version-mismatched entries as misses.
3. Reuse unchanged feature vectors across path moves when content identity is proven.
4. Recompute changed and deleted records plus reverse-affected neighbours.
5. Periodically compare incremental output with a fresh full run.
6. Invalidate the cache when source content or extraction policy changes.

## Anti-patterns

- Keying cache only by path.
- Reusing output after policy changes.
- Assuming incremental equivalence without periodic proof.

## Benchmark case

After one record changes, a passing run recomputes that record and affected neighbours, reuses unchanged hashes and matches a scheduled full rebuild.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop cache reuse when identity, policy version or equivalence evidence is unavailable.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.

## Dependency completeness and reuse limits — 17 October 2026

Include every behaviour-changing input in the key: exact source bytes, extraction rules/policy, parser/tool/schema versions, configuration and declared dependency outputs. Record those identities and the successful output digest; an unregistered file read or external dependency makes equivalence unproved. Invalidate the reverse-dependent set when an input changes; include deletion and path-dependent semantics rather than assuming every move is harmless. Use a miss when validity cannot be established.

This Skill owns deterministic extraction caching only. It does not make live permissions, current branch refs, expiring evidence, changing external state or nondeterministic judgements cacheable. Workflow evidence reuse follows its separate governing freshness/check contract; mandatory fresh checks still execute. A periodic full comparison needs its own authorised schedule or explicit execution request; this method creates no schedule.

Cases: same source with a new parser version -> miss; changed dependency with unchanged main file -> invalidate dependents; unchanged path-independent bytes moved -> reuse only with identity and semantic proof. Source: [Bazel Skyframe](https://bazel.build/reference/skyframe), inspected 17 October 2026. Dependency-aware evidence reuse is an engineering adaptation, not a guarantee for external state.
