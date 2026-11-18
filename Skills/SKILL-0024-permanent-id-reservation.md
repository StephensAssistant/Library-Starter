---
id: SKILL-0024
type: skill
title: Permanent ID reservation
status: current
created: 2026-09-05
updated: 2026-10-19
owner: Library owner
trigger_phrases: [reserve an id, reserve ids, next id, id reservation]
links: [FLOW-0001, FLOW-0002, PLAY-0046, PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, ids, serialisation]
---

# Permanent ID reservation

Getting a permanent ID without guessing, colliding, or breaking contiguity.

**Used by:** `PLAY-0056` (commit), `PLAY-0049` (plan start) — and any task that creates a governed record.

## The rules

- IDs are permanent, sequential, and never guessed, reused, or silently renumbered
- **Never hand-edit `.github/id-reservations.json`**
- New IDs must be **contiguous from the current maximum + 1**
- Reserve each required prefix through the serialized workflow; related prefixes may be reserved separately
- Every reservation required by the candidate must be consumed before merge — orphan reservations are rejected

## Step 1 — Find the current maximum

Before reserving, inspect the current target folder (or `Chats/` for CHAT), reservation receipts and deletion/tombstone evidence. A folder listing alone omits allocated but not yet consumed IDs. The allocator, not this diagnostic inspection, selects the next ID under its serialized current-state contract.

`check_ids.py` requires contiguity in the final candidate, accounting for retained history and consumed receipts. For a given prefix, if 41 is the highest used or reserved number and no other current allocation exists, the next allocation starts at 42. A gap or orphan receipt fails the merge gate.

Catching this before reserving costs one listing. Catching it at merge costs a full restart.

## Step 2 — Reserve

### Preferred: the workflow

Run `Reserve permanent IDs`. Put the **bare** form in the `requests` input — the workflow adds the header itself:

```
TICK 1
ART 2, TICK 1, CHAT 1
```

Ignore the legacy `prefix` and `count` inputs; they are superseded and ignored whenever `requests` is set.

### Fallback: a GitHub Issue

When workflow dispatch is unavailable, create an Issue whose title includes the header **explicitly**:

```
[ID-RESERVE] TICK
[ID-RESERVE] ART 2
[ID-RESERVE] TICK 1, CHAT 1
```

### Format rules

Enforced by `parse_id_reservation_request.py`:

- Read current `.github/type-prefixes.json`; it is the authoritative prefix list. Verify the executed reservation workflow checks out `staging` before parsing a newly registered prefix.
- Prefix must be known: `PROJ KNOW PERS DEC TICK ART PLAY SKILL HAT CHAT FLOW`
- Count optional, defaults to 1, range 1–50
- Comma-separated for multiple prefixes
- **No duplicate prefixes** — `TICK 1, TICK 1` is rejected; use `TICK 2`
- Total across all prefixes must not exceed 50

The requester must have write permission. The workflow validates it, allocates under a global concurrency lock, commits the receipt to `staging`, comments the IDs, and closes the issue.

## Step 3 — Wait

Never proceed on a guessed ID.

The allocator retries up to five times if `staging` moves during allocation. If it exhausts all five, it fails — wait and retry rather than working around it.

## Step 4 — Consume it

A reservation may sit unconsumed on `staging` temporarily, but the main PR gate **rejects orphans**. Every reservation required by the final staged candidate must be consumed before merge.

## Reservation requests

A single request may reserve a Ticket, an Artifact pair, and a Chat entry together when they are known:

```
[ID-RESERVE] TICK 1, ART 2, CHAT 1
```

Reserve IDs when their need is known. Separate serialized requests are permitted; all resulting receipts required by the final candidate must be consumed before merge.

## Artifacts need two

One ID for the native file, one for the markdown companion — **consecutive**.

## Chats

Chat IDs are globally sequential like every other type, but live inside daily files rather than getting their own file. `check_chat_ids.py` validates sequence, uniqueness, and receipt consumption separately from the per-file check.

## Deleted IDs

A deleted ID is never reused. `check_ids.py` adds tombstoned IDs to the existing set, so contiguity accounting still works — the next ID follows the deleted one, it does not fill the gap.

## Anti-patterns

- Inferring the next ID from the folder listing and using it directly
- Bypassing the serialized workflow because another required prefix was discovered later
- Hand-editing the reservation ledger when the workflow is slow
- Reserving before checking the current maximum
- Assuming a returned ID is contiguous without verifying
- Leaving a reservation unconsumed across a merge

## Failure recovery

**Five retries exhausted:** `staging` is being written too fast. Wait, then retry.

**Duplicate prefix rejected:** combine them into a single count.

**Returned ID appears non-contiguous:** stop the dependent filing and compare the allocator receipt, current records, unconsumed reservations and tombstones. Preserve the returned permanent IDs; do not discard the receipt or reserve again to conceal a gap. Route an allocator/ledger defect to the authorised owner for evidenced recovery; reserve further IDs only for a confirmed distinct need after the inconsistency is resolved.

**Neither workflow nor issue route available:** stop and tell the Library owner. Do not guess.

## Benchmark case

Given a confirmed need for three new Skills, verify the current maximum, submit one serialized `SKILL 3` reservation request, wait for the allocator receipt, and use only the three returned contiguous IDs.

## Stop

Stop after the allocator returns and records the exact reserved IDs. If allocation fails, is non-contiguous or unavailable, stop without guessing or editing the reservation ledger.





## Connector result versus allocation — 19 October 2026

An interactive issue form or awaiting_user_submission result is not a created issue or allocator receipt. Preserve that distinction; no permanent ID exists until the serial allocator returns and records it. Check for an existing request before a separately authorised retry through another available normal connector, and do not submit an older draft after a real issue has been created. A submitted issue and an allocator receipt are distinct verified results. Neither grants permission to bypass a denial, infer an ID or edit the reservation ledger.
