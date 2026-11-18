---
id: SKILL-0184
type: skill
title: Full-File Rewrite Integrity
status: current
created: 2026-09-20
updated: 2026-10-16
owner: Library owner

trigger_phrases: ["whole file rewrite", "verify full file edit", "transcription risk"]
links: [PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, editing, verification]
---

# Full-File Rewrite Integrity

Prevents unrelated transcription changes during whole-file updates.

## When to use

Use whenever a tool replaces a complete file to make a bounded edit.

## Method

1. Read the current file immediately before the edit.
2. Preserve every unrelated byte or line verbatim.
3. Write with the current SHA guard.
4. Read back and compare the result to the pre-edit version.
5. Accept only the intended differences.

## Benchmark case

Changing one due date while accidentally altering tags fails, even when the new tags seem reasonable.

## Anti-patterns

- Retyping unrelated fields from memory
- Combining opportunistic cleanup
- Treating successful write as proof

## Stop

Stop only after readback proves the bounded intended diff.

