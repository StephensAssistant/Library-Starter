# Transcriptions — `TRAN`

Verbatim source records for meetings, calls, voice notes and other captured conversations. Transcriptions preserve what was said; Projects, Tickets, Decisions, Playbooks and Knowledge remain the canonical homes for interpreted outcomes.

Filenames: `TRAN-<NNNN>-YYYY-MM-DD-<slug>.md`

Create from `_TEMPLATE.md` using `_HOW-TO-CREATE.md`.

## Source-of-truth boundary

- Preserve the imported transcript verbatim. Do not silently correct, summarise or rewrite the source text.
- Put corrections, speaker-attribution changes and review notes in separate sections with dates and provenance.
- Use `transcript_status: raw`, `reviewed` or `verified`; this describes transcript review, not whether every statement in the meeting is true.
- Record the capture source and stable source reference. Keep an audio reference when one is available; do not copy secrets or unsupported sensitive material into the Library.
- Link derived decisions, actions and reusable knowledge reciprocally. A transcription is evidence, not the canonical owner of project state, ticket status, a playbook or a decision.
- Every new transcription starts with `link_review_status: pending`. Its immediate next processing step is a wider Library search for related People, Projects, Tickets, Decisions, Playbooks, Knowledge, Artifacts and earlier Transcriptions.
- Read each plausible canonical record before linking. Search matches are candidates, not confirmed relationships. Add reciprocal links only when the transcript and target record support the relationship; otherwise record the candidate as rejected or no-match in the link-review notes.
- Set `link_review_status: complete` and `link_reviewed_at` only after the search, candidate inspection, reciprocal-link updates and derived-record review are complete. A complete review may legitimately produce no links when that result is documented.
- Never reuse a `TRAN` ID. Reserve the next ID through the serialized allocator.

## Required AI processing order

1. Ingest and preserve the source transcript.
2. Search the complete current Library using participant names, organisations, systems, subjects, explicit IDs, decisions, actions and distinctive phrases from the transcript.
3. Open and inspect each plausible canonical record. Distinguish confirmed relationships from inferred candidates.
4. Add confirmed reciprocal links to both records. Do not add a link from resemblance or co-occurrence alone.
5. Extract decisions, actions, risks and reusable knowledge into their canonical owners, linking them back to the transcription when supported.
6. Complete the transcription's link-review notes, including searches performed, confirmed links, rejected candidates and an explicit no-match result where applicable.
7. Mark the link review complete only after the preceding steps are evidenced.

## Privacy and retention

Only file recordings that the Library owner is authorised to retain. Record participants as supplied, preserve any known notice or consent context in the notes, and keep unknowns explicit. Do not infer consent from the existence of a recording.
