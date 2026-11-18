# Create a Transcription record

1. Confirm the recording may be retained and the source material is available. Do not infer notice or consent.
2. Search for an existing transcription of the same recording. Update that record rather than creating a duplicate.
3. Reserve one `TRAN` ID through **Reserve permanent IDs** using `TRAN 1`. The first allocation is `TRAN-0001`; never guess or reuse it.
4. Copy `_TEMPLATE.md` to `TRAN-<NNNN>-YYYY-MM-DD-<slug>.md` and complete every required field.
5. Preserve the imported transcript verbatim. Put corrections and review notes outside the transcript section.
6. Leave `link_review_status: pending` during ingestion. The immediate next step is to search the complete current Library using participants, organisations, systems, subjects, explicit IDs, decisions, actions and distinctive phrases from the transcript.
7. Open every plausible canonical record before deciding whether the relationship is confirmed. A search match, shared participant or similar topic is not sufficient by itself.
8. Add confirmed reciprocal links to the transcription and each eligible target. Record rejected candidates and why they were not linked; if nothing qualifies, record an explicit no-match result.
9. Extract decisions, actions, risks and reusable knowledge into their canonical records, linking them back to the transcription when supported.
10. Complete the AI processing checklist and link-review notes. Only then set `link_review_status: complete` and `link_reviewed_at` to the review timestamp.
11. Save the authorised source change to `staging`. Candidate validation and merge remain separate actions requiring their own authority.

Stop after the source record, completed link review, derived-record updates and confirmed reciprocal links are staged. If link discovery is blocked, preserve `pending`, name the blocker and do not present the transcription as processed. Do not invent participants, decisions, owners, dates, consent, verification or relationships.
