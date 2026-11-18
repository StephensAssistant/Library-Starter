---
id: SKILL-0183
type: skill
title: Staging Branch Target Verification
status: current
created: 2026-09-20
updated: 2026-10-16
owner: Library owner

trigger_phrases: ["verify staging branch", "branch safety before write", "never write main"]
links: [PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, git, branch-safety]
---

# Staging Branch Target Verification

Verifies the exact writable branch before a Library mutation.

## When to use

Use immediately before any authorised GitHub Library write.

## Method

1. List branches rather than trusting a default.
2. Require an explicit `staging` target; a missing or defaulted branch is a hard stop.
3. Never target `main`.
4. If staging is absent, create it from current main only with authorised update scope.
5. Confirm staging contains current main; reconcile ancestry before writing if behind.

## Benchmark case

A write request omits its branch: stop instead of allowing the tool to choose main.

## Anti-patterns

- Trusting a tool default
- Writing directly to main
- Ignoring stale staging ancestry

## Stop

Stop when explicit staging and valid ancestry are confirmed, or when reconciliation authority is missing.

