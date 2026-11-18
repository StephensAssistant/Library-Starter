---
id: SKILL-0025
type: skill
title: Reciprocal Frontmatter Link Management
status: current
created: 2026-09-05
updated: 2026-10-31
owner: Library owner

trigger_phrases: [reciprocal links, link both sides, repair direct link]
links: [PLAY-0056, PLAY-0059, PLAY-0071]
tags: [skill, library-mechanics, links, relationships]
---

# Reciprocal Frontmatter Link Management

Creates or repairs factual bidirectional navigation links between governed records.

## When to use

Use when adding or repairing a direct relationship in frontmatter. Use the separate relationship-evidence Skill only when type, direction or provenance must be permanently recorded.

## Method

1. Verify both endpoints exist and are live.
2. Require direct evidence; topic similarity alone is not a relationship.
3. Add the target ID to the source `links` list and the source ID to the target list in the same final candidate.
4. Format each list as IDs only, with no trailing prose.
5. Parse the complete frontmatter after every `links` edit. Confirm `links` is a list at both endpoints and the reciprocal IDs appear in the parsed collections; a visible ID inside malformed YAML is not a valid link.
6. Read each endpoint immediately before writing and use its current SHA.
7. Read back both files and confirm only the intended link bookkeeping changed.
8. Route Chats, raw Artifacts, legacy pending links and healer runs to their focused Skills.

## Benchmark case

For a confirmed relationship, verify both endpoints contain reciprocal links and every unrelated field remains unchanged.

Missing-input design case: both records exist but the only support is a shared tag. Leave both link lists unchanged and report the missing direct relationship evidence; reciprocal syntax would not turn an inferred candidate into a factual relationship.

## Anti-patterns

- Adding only one side
- Linking by shared title or tag
- Guessing a target ID
- Appending prose to a links list
- Using an inferred candidate as authority

## Stop

Stop when both live endpoints carry the factual reciprocal edge, or when evidence or endpoint identity is unresolved.

