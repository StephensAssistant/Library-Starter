---
id: SKILL-0188
type: skill
title: Library Mutation Authority Boundary
status: current
created: 2026-09-20
updated: 2026-11-07
owner: Library owner

trigger_phrases: ["library write authority", "staging versus merge authority", "pause writes for merge"]
links: [FLOW-0001, FLOW-0002, PLAY-0037, PLAY-0046, PLAY-0056, PLAY-0059, PLAY-0069]
tags: [skill, library-mechanics, authority, git]
---

# Library Mutation Authority Boundary

Determines whether the current instruction authorises staging or merge action.

## When to use

Use before any Library mutation or when requested action changes from staging to merge.

## Method

1. Check the current chat's explicit Library-editing grant, private working-copy context and writable roots before declaring write access unavailable. Current evidence overrides an earlier session's limitation.
2. Establish the applicable source-write authority: explicit current-conversation scope or an applicable confirmed standing capture instruction. Verify target/access; neither historic access nor a scheduled run grants unrelated writes.
3. An update/save/stage request authorises only its named source write to `staging` and any mechanical commit. “Done” or “check” is not an independent mutation grant. PLAY-0059 needs its own requested/approved route; PLAY-0056, candidate validation and its required Actions use AGENTS.md Library rule6: approved daily schedule, named standalone one-off exception, or an explicit request to run an already-approved workflow that actually declares PLAY-0056. For the workflow route verify the original entry request, exact approved/admitted graph and component call, permitted effects, resolved scope, live actor/access and shared remaining bounds. Inherit that recorded grant without asking again per Playbook. Source-only FLOW-0001, a policy/source-edit request, links, dependencies read as context, approval or a score do not authorise PLAY-0056. Preserve the parent provenance and verified own-preparation advances; resolve then freeze the candidate boundary at PLAY-0056 entry. Apply PLAY-0056 Bounded repair continuation for cumulative candidate-repair accounting under AGENTS.md Library rule 6. Undeclared effects, missing access, cancellation, integrity movement or exhausted limits stop; no budget reset, automatic restart or new batch. Merge, main writes, sends, deployment and new schedules retain their separate gates.
4. Invoke PLAY-0055 only under explicit current-conversation merge authority or an enabled the Library owner-approved schedule specifically naming it, for its resolved single-use batch. Validation or a source write is not merge authority.
5. Pause further staging writes once merge is authorised until merge completes.
6. Stop at the authorised source/readback or separately authorised workflow boundary. AGENTS.md Library rule 6 distinguishes a recoverable failed validation attempt from a terminal invocation stop and owns the candidate-repair ceiling. Preserve scope/base, capture learning and obtain required independent review before retrying. Completion, terminal stop, cancellation or schedule disablement ends authority; never reuse it for another batch.

## Benchmark case

“Update the Library” permits staging but not PR readiness or merge.

## Anti-patterns

- Carrying write authority from an earlier conversation
- Carrying a read-only conclusion forward after the current chat grants Library editing
- Treating commit as merge authority
- Continuing staged edits during an authorised merge

## Stop

Stop at the boundary of the authority actually granted.



## Continuing source-repair authority — 16 October 2026

When the Library owner requests a defined source repair, establish its outcome, scope and permitted effects once; reuse that current grant through investigation, component correction, testing, non-author review and guarded source save. Check actual access and continuing scope before effects, but do not ask for the same permission at each step. Keep its authority source in the work owner. A failed target FLOW or named single-use invocation does not by itself revoke this separate source request; neither does the source request revive a terminated FLOW/Commit/Merge invocation.

If staging moves, stop and discard the stale write/proposal under SKILL-0185. A still-specific source request may support wholly fresh source preparation after fresh main/head/all-target reads, proof of non-overlap/unchanged target bytes and guidance, new construction from the current parent/base tree, independent required verification and guarded publication. Never refresh an old proposal's expected head, adopt concurrent content into authored changes, reuse stale PASS evidence or bypass an actual conflict. If the live source grant no longer covers the outcome/effects, report the exact missing scope; do not infer a standing grant.


## Supported trigger is not new authority

Under a current admitted workflow-entry grant that actually declares PLAY-0056, selecting an existing supported trigger for that same declared effect does not require a repeated component exception. Verify its actual callable capability, actor/access, correct input/boundary and remaining scope first. A `[daily-commit]` message does not itself confer authority: use PLAY-0056's substantive-source/boundary checks; never add it to a source-only child or source-repair publication to launch Actions. A separately admitted post-child validation-request control commit may use the exact narrow PLAY-0056/AGENTS transport route; it is an operational effect under the current workflow entry, not source-save authority. Missing tool is not proved permission denial. External recovery may investigate within existing authority but cannot revive a terminal invocation, reset budgets or convert source construction into candidate execution.


## Connected GitHub source preference — 4 November 2026

When the Library owner explicitly directs GitHub or the connected GitHub repository for Library work, use the authorised GitHub connector against `the configured Library repository` on `staging` as the source and write surface. A dirty, missing or divergent local checkout is then irrelevant to that connector route and must not block or replace it. Still verify the repository, branch, current target bytes and staging head through GitHub immediately before writing, preserve concurrent changes with the expected-head guard, and stop on connector access failure or target movement. Do not inspect or repair a local checkout unless the Library owner separately requests local-checkout work.
