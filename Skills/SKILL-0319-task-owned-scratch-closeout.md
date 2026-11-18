---
id: SKILL-0319
type: skill
title: Task-owned Scratch Close-out
status: current
created: 2026-10-16
updated: 2026-11-15
owner: Library owner

trigger_phrases: ["close out task scratch", "classify session residue", "verify scratch retention"]
links: [FLOW-0001, FLOW-0002, PLAY-0037, PLAY-0059, PLAY-0075]
tags: [skill, library-mechanics, cleanup]
---

# Task-owned Scratch Close-out

## When to use and intent routing contract

Close out exact files created or controlled by this AI in the active task. Use for close out task scratch, classify session residue or verify scratch retention. Exclude whole-machine cleanup, repository cleanup, canonical record deletion and another AI's workspace. This technique supports PLAY-0059's Scratch close-out and PLAY-0075 Cleanup. The admitted caller owns the sequence: Cleanup MUST defer all deletion until its final-candidate validation gate passes; source readback alone never releases that hold.

## Method

1. Inventory exact paths under the established task-owned scratch boundary. Prove ownership from this session's actions, not location or filename alone. Unknown ownership or inaccessible external-session material remains a named Gap.
2. Assign each file one disposition: file/verify/delete the duplicate; capture material evidence/verify/delete the diagnostic; retain temporarily; or delete. File only a relevant accepted reusable output through its current owner and governed source process. Test-only, failed, partial and superseded work is not accepted output. Preserve unique evidence required for unresolved verification even if a summary exists.
3. Before deleting a filed duplicate or diagnostic, verify the canonical source/evidence by exact readback. A promised write or tool-call success is insufficient. Retain an active working copy, unfinished input or sole unreproduced evidence with exact path, purpose, owner, next action and deletion trigger. 'Might be useful' is not a purpose.
4. For every proposed deletion, resolve its exact path; reject a symlink or path escaping the task-owned boundary. Confirm each resolved file is owned by this task and permitted by the recorded disposition. Prefer recoverable deletion when available. Never use broad recursive deletion, unresolved variables, mixed-ownership wildcards, home/repository roots or a shared folder. Delete only the verified exact files; a failed deletion retains the file and its evidence.
5. Read back the remaining inventory and compare it with intended removals/retentions. Report actual removed files, retained paths/purposes/triggers and blocked ownership/access/verification. A summary does not prove deletion. Do not broaden scope or delete another file to hide a failed check.

## Representative cases

- Positive: accepted reusable output plus successful canonical readback allows its redundant local copy to be removed after exact-path/ownership checks.
- Negative: a file belongs to another session or resolves through a symlink outside the boundary; retain it and name the Gap.
- Boundary: a diagnostic is the sole unreproduced evidence for pending validation; retain it with the validation outcome as deletion trigger even when a summary is filed.

## Anti-patterns

- Deleting because a summary exists, because a filename looks temporary or because another session has finished.
- Claiming capture, acceptance, cleanup or runtime protection from a planned action.

## Stop

Stop when every task-owned file has a verified disposition and remaining inventory matches, or report the precise blocked file and next action. This Skill grants no canonical deletion, source write, Commit, merge or wider maintenance authority.

## Provenance and verification limits


## Contextual links


## Cleanup integration — 15 November 2026

PLAY-0075 is the chat-scoped Cleanup caller approved for creation by the Library owner. Its operation preserves the agreed fresh AGENTS read → source preparation → final-candidate validation → scratch deletion order. This association grants no execution authority; changed workflow dependencies require fresh qualification before invocation.

RELATIONSHIP-EVIDENCE: PLAY-0075--SKILL-0319 | related_to | undirected | user_confirmed | supports
