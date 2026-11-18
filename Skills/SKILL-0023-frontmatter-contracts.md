---
id: SKILL-0023
type: skill
title: Frontmatter contracts by type
status: current
created: 2026-09-05
updated: 2026-10-24
owner: Library owner

trigger_phrases: [frontmatter, schema fields, operating fields, status enum]
links: [PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, frontmatter, schema]
---

# Frontmatter validation

Getting the metadata contract right, per type.

**Used by:** `PLAY-0056` (commit), `PLAY-0049` (plan start) — and any task that creates or amends a governed record.

## Authority

Use current owner-approved work-management rules for semantics and the schemas for syntax. For example, links may be a bracketed list of two valid destination record IDs.

## Base contract — every type

```yaml
---
id: <PREFIX>-<NNNN>
type: <project|ticket|knowledge|person|decision|artifact|playbook|skill|aihat|workflow>
title: <clear, specific, searchable>
status: <see enum>
created: YYYY-MM-DD
updated: YYYY-MM-DD
links: [ID1, ID2]
tags: [tag1, tag2]
---
```

All eight are required. `created` and `updated` are the same date on a new record.

**Chats are the exception** — no frontmatter at all. Tags and links fold into the entry body.

### Fields beyond the base eight

The schema specifies a **required** set, not an exhaustive one. Extra fields are tolerated, and several records carry them: `verification_state`, `verified_on`, `review_on`, `migrated_from`, `owner`.

**`protocol:`** is a Drive-era PROTOCOL-TOKEN field. Records migrated from the old Library still carry it. It is **legacy — do not add it to new records** and do not treat its absence as a defect.

## Status enums

| Type | Valid values |
|---|---|
| Project, Ticket | `active`, `blocked`, `done`, `archived` |
| Knowledge, Artifact, Playbook, Skill, AIHat, Workflow, Transcription | `current`, `superseded` |
| Decision | `decided`, `superseded` |
| Person | `current`, `archived` |

There is no `backlog` **status**. `backlog` is a `work_state`.

## Operating fields — Project and Ticket

Required when `status` is `active`, `blocked`, or `done`:

`owner` `external_ref` `priority` `effort` `estimate_minutes` `work_class` `work_state` `due` `next_action` `waiting_on` `review_on` `sprint` `depends_on` `started` `completed` `evidence`

Because a new Project or Ticket is `status: active`, **these are required from creation** — not added later.

`work_state` enum: `backlog` `ready` `doing` `review` `waiting` `done`

### What each means

| Field | Semantics |
|---|---|
| `priority` | Importance, not current activity. Never fabricated from age or inconvenience. |
| `effort` / `estimate_minutes` | Evidence-based. Unknown stays unknown until scoped. |
| `work_class` | Workload-balancing category, not priority. Values including `support`, `incident`, `operations` exempt the item from WIP limits. |
| `due` | Only a confirmed commitment. Never invented, silently moved, or erased to clear an alert. |
| `next_action` | **One** observable executable action, beginning with a verb. Null only on done or archived. |
| `waiting_on` | The exact person, team, system, or deliverable. Required when `work_state: waiting`. |
| `review_on` | A deliberate review or chase date. Required when waiting. Default two working days after the block if none supplied. A passed date stays overdue until real evidence exists. |
| `sprint` | Committed planning week, never merely desirable work. |
| `depends_on` | Evidenced **Library** dependencies only. External ones go in `waiting_on`. |
| `started` | When execution actually began. |
| `completed` / `evidence` | Completion proof, never intention. |

**Unknown and unassessed are honest states.** They must stay visible for triage rather than being guessed away.

**`evidence` is legitimately empty on a new record.** Leave it empty. Never invent evidence to fill a field — an empty field is a fact, invented evidence is a lie.

### Optional internal-customer contact date

`last_customer_contact_date` is a permitted optional Project/Ticket extension: a quoted ISO calendar date (`"YYYY-MM-DD"`) or `""` for unknown/not applicable. New templates include it; the 2026-10-01 backfill adds it to active/blocked records without requiring a rewrite of closed historical records. The existing validator tolerates extra fields; it does not enforce this date's syntax or communication evidence.

It means the latest confirmed outbound update to the internal customer about this record. A dated Customer communication log supplies audience, channel/reference, message summary and source. Do not use supplier/dependency contact, an incoming reply, draft or record-edit date. Maintain per-audience dates for multiple customer matters; no unsupported parent/child inheritance. See Tickets/README.md, Projects/README.md and PLAY-0066 for maintenance and reminder behaviour.

## Type-specific extras

**Workflow:** use `Workflows/README.md`, its creation guide/template and workflow schema. `status: current` does not imply approval: `review_status` is draft, needs_review or approved. Workflow definitions have no work priority; priority belongs to their owning Ticket/Project.

**Artifact:** `stored_at` — a valid repo-relative path to the native file. It must resolve, and only one companion may claim a given target.

**Transcription:** `recorded_at`, `source`, `source_reference`, `participants`, `transcript_status`, `link_review_status` and `link_reviewed_at`. Transcript status is `raw`, `reviewed` or `verified`; it describes review of the transcript, not truth of every statement in the recording. Link review is `pending` or `complete`; complete requires an evidenced Library-wide candidate search and inspection, confirmed reciprocal-link updates, rejected-candidate or no-match notes, and the review timestamp.

**Playbook / Skill:** `trigger_phrases` in the frontmatter, plus a matching entry in `.github/intent-routing.json` and a benchmark case — both required companion files.

**Knowledge:** must be durable reusable learning. A new one needs `DURABLE-LEARNING: yes` (or its ID) in the merge PR body.

**AIHat:** must record scope, evidence, verdict, residual risk, owner, and hand-off in the body.

## Formatting traps


Prose on or after the links line gets parsed as a malformed ID and becomes a **permanent broken-link exception**. Nothing but IDs inside the brackets, nothing trailing after them.

**List fields use flow style,** not block style. The parser is line-based:

```yaml
links: [A, B, C]          # correct
links:                     # never parsed
  - A
  - B
```

Items must be comma-free, because the parser splits on commas before stripping quotes.

**The frontmatter `id` must exactly equal the filename ID.** These are validated separately, so both must be right.

## Validating

- `check_schema.py` — the frontmatter contract
- `check_ids.py` — ID sequence, uniqueness, folder prefix, frontmatter/filename match, `stored_at` resolution

Read `.github/frontmatter-rules/<type>.json` when uncertain. Do not infer a field and do not omit one.

## Anti-patterns

- Copying frontmatter from another record and forgetting to change the ID
- Using block-style YAML lists
- Inventing a `due` date because the field felt empty
- Setting `evidence` from intention
- Treating `unassessed` as low priority
- Leaving `next_action` empty on an active record
- Adding a new tag when a synonym already exists in `Catalog/TAG-INDEX.md`
- Working from another record's schema instead of reading the type's own

## Benchmark case

Given a proposed Skill record, validate its frontmatter against the Skill contract, reject an invalid status or missing required field, and return the smallest compliant correction without changing body content.

## Stop

Stop when the record's frontmatter conforms to the applicable type contract, or when the record type or required value cannot be resolved without owner input.


