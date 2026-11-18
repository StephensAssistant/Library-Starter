---
id: SKILL-0022
type: skill
title: Anchored editing — replace the part, never the whole
status: current
created: 2026-09-05
updated: 2026-10-13
owner: Library owner

trigger_phrases: [anchored edit, partial edit, replace the part, edit safely]
links: [FLOW-0002, PLAY-0046, PLAY-0056]
tags: [skill, library-mechanics, editing, concurrency]
---

# Anchored editing

Changing part of a file without damaging the rest.

**Used by:** `PLAY-0056` (commit), `PLAY-0037` (hygiene), `PLAY-0041` (learning repair), `PLAY-0050` (plan execution) — and any task that edits an existing record.

## The rule

Replace the part, never the whole.

A whole-file rewrite is permitted only when the Library owner explicitly asks for it, or when the change genuinely touches most of the file **and** you can evidence that identity, unrelated content, formatting, and links were preserved.

Review must reject an un-requested full rewrite and require granular edits unless the evidenced exception above applies. This is an instruction, not a claim that an automated validator enforces it.

## Method

### 1. Read the current file from the target branch

From the current `staging` head. Not from `main`. Not from an earlier read in this session — another write may have landed since.

Capture the file SHA. You need it for step 5.

### 2. Choose an anchor

Exact text from the current file, long enough to be unique.

Good anchors:
- A full line including its leading marker (`- `, `## `, `| `)
- A distinctive phrase plus the line before or after it
- A frontmatter key with its full value

Poor anchors:
- A bare word or short phrase
- Anything that looks like boilerplate
- A line that could plausibly appear twice

### 3. Verify uniqueness — and understand why

Count the occurrences. It must be exactly **one**.

**Zero matches:** the file is not what you thought. Re-read it. Do not proceed on assumption.

**Two or more:** widen the anchor with surrounding text until it is unique.

**Why this matters more than it looks:** some replace operations patch only the *first* match and report success. A non-unique anchor can therefore succeed silently while leaving later occurrences stale — producing drift that surfaces much later as an inexplicable inconsistency.

This has happened in this Library. A first-occurrence-only replace kept updating one copy of a duplicated document while the second stagnated, and nobody noticed for days.

### 4. Predict the size delta

Before writing, work out the expected change in file length.

This is not optional bookkeeping. It is what has actually caught concurrent edits and silent duplication here — including one case where two sessions were editing the same file and only the length check revealed it.

### 5. Check concurrency immediately before writing

Re-read the file. Compare the SHA to the one from step 1.

**Unchanged:** write.

**Changed:** the file moved under you. Preserve the concurrent work and stop this write under AGENTS.md. Report the changed target/head and the affected anchor; do not overwrite or absorb the concurrent change. A later authorised reconciliation must start from the then-current target and head.

**Never overwrite another session's work.** The earlier read and SHA no longer authorise this write.

### 6. Write, then verify

Replace only the anchored text. Leave IDs, links, formatting, and untargeted blocks untouched.

Then:
- **Read the file back.** A tool call succeeding is not evidence the file says what you intended.
- **Compare measured size to predicted.** A mismatch means something else changed — investigate before proceeding.
- **After a multi-anchor edit, scan for duplicated blocks.** A sequence of replaces can leave a sentence or section present twice if one anchor matched more broadly than intended.

## Halt conditions

Stop and tell the Library owner when:

- The anchor cannot be made unique
- The anchor is missing entirely
- The measured size does not match the prediction and you cannot account for the difference
- A concurrent change genuinely contradicts what was requested

**Halting is the correct outcome, not a failure.** Guessing which occurrence was meant is how files get damaged.

## Special cases

### Editing inside a Chat daily file

Chat entries share a file, and their `Tags:` and `Links:` lines look identical across entries.

Scope the anchor to the specific block: include the `### CHAT-<NNNN> — <summary>` heading, or enough surrounding content to be unique **within the whole file**, not just within the block you have in mind.

The `---` separator between entries belongs to neither entry. Do not consume it.

### Editing frontmatter

Include the key in the anchor: `status: active`, not `active`.

If several records are being changed, the same frontmatter line will appear in each — but you are editing one file at a time, so uniqueness is per-file.

### Never hand-edit generated output

`Catalog/BOARD.md`, folder `index.md` files, `Catalog/TAG-INDEX.md`, `Catalog/SESSION-PACK.md`, the graph HTML, `relationship-candidates.json`, and reciprocal-link output are all generated.

If one is wrong, the source record or the generator is wrong. Fix that and regenerate.

## Anti-patterns

- Falling back to a whole-file rewrite because the anchor was hard to find
- Skipping the uniqueness check because the tool did not complain
- Treating a successful tool call as proof of the intended result
- Re-reading before the write but not comparing the SHA
- Widening an anchor by adding text you have not verified is present
- Editing from memory of a file read earlier in the session

## Worked example

Changing a Ticket's work_state from `doing` to `waiting`:

1. Read `the affected Ticket` from `staging`, capture SHA `abc123...`
2. Anchor: `work_state: doing` — check the file, appears once ✓
3. Predicted delta: `doing` (5) → `waiting` (7) = +2 bytes. But `waiting_on` and `review_on` also need values, so recalculate across all three edits.
4. Re-read immediately before writing — SHA still `abc123...` ✓
5. Apply the three anchored replaces
6. Read back: `work_state: waiting` present once, `waiting_on` and `review_on` populated, measured delta matches ✓

If step 2 had found `work_state: doing` twice — impossible in frontmatter, but if the phrase appeared in the body too — the anchor would widen to include the surrounding frontmatter lines.

## Benchmark case

Given a long governed record with one uniquely identifiable paragraph to change, locate that exact anchor, replace only the intended paragraph, and verify the preceding and following content remains byte-for-byte unchanged.

## Stop

Stop when the requested anchored fragment is replaced and its surrounding content is verified unchanged. If the anchor is missing or non-unique, stop without writing and report the ambiguity.
