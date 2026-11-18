# Tickets — TICK

One canonical record owns outcome, acceptance, status, evidence and next action. Search before creating; reserve a new ID only for a distinct subject. Use the current frontmatter schema.

Create from `_TEMPLATE.md` using `_HOW-TO-CREATE.md`. Close with `_HOW-TO-CLOSE.md`.

Small work uses an inline `## Work plan` checklist. Substantial work may use one linked Planning companion. Preserve existing plans and their parent pointers; do not create one just to resume a small item.

Read the record and relevant relationships, and use [[PLAY-0021]] for focused wider Library reuse checks before creating or resuming work. Save authorised source changes to `staging` through the mechanical source-save transaction and verify exact source readback while preserving concurrent work. This does not authorise Commit Ready, PLAY-0056, candidate validation, Actions or merge; AGENTS.md owns their separate authority. Chat provenance is optional when useful, not a required extra record. Preserve existing Chat history and outbound links.

## Intake and work phase

[[PLAY-0021]] owns the shared intake method and phase progression. Keep a small inline section recording the evidenced existing/new/unknown target, Library reuse with fit and limits (or a scoped checked no-match), current phase, observable evidence needed for the next phase and the outstanding next decision (`none` is valid). Use the phases `requirements`, `discovery`, `approach`, `delivery`, `verification` and `acceptance/closure`. Gather only enough facts for the next useful prototype, test or implementation step, reuse settled answers and resume only affected phases when evidence changes.

Phase records the present work, not lifecycle status or `work_state`; do not derive either field from a phase change. A small Ticket may compress the section into a few lines. No extra plan, mock prototype or checklist interview is required when it adds no value. A Ticket's phase is independent of any parent Project's phase. Add or refresh this section when creating or meaningfully resuming the record; do not mass-migrate historical records.

## Last internal-customer contact

Use `last_customer_contact_date: "YYYY-MM-DD"` for the latest confirmed outbound update sent or posted to the internal customer about this Ticket. The field is an optional, backwards-compatible metadata extension permitted by SKILL-0023; include it in every new record and keep it on every active/blocked record. Use `""` when no dated customer contact is evidenced, the date is unknown, or no internal customer applies. A blank value is not proof that no communication occurred.

the Library owner reviews and sends/posts communications. Update the date only after his confirmation or explicit sent-message evidence; use the actual contact date in Europe/London, never the review date. Record the audience, channel/reference, concise message summary and evidence source in `## Customer communication log`. Preserve historical entries and acceptance state. Supplier messages, dependency-team requests, incoming replies, meetings without evidenced customer-update delivery, drafts, record edits and last-worked dates do not reset it.

For multiple customers/external references, keep a dated log per audience/matter. The scalar date is the latest confirmed contact on the record; it must not suppress an older uncontacted audience. Do not copy a parent Project's date to child Tickets, or vice versa, without evidence that the same communication covered that matter and audience.

PLAY-0066 reads this field and its evidence log to identify updates due at seven calendar days, with missing/uncertain dates listed separately for confirmation. Include customer-facing active/blocked backlog work when the Library owner requests the full active portfolio. Personal and Library-tooling work receives the field but is not a customer reminder unless an internal customer is explicitly recorded. Leave status, priority, work state, next action and last meaningful movement unchanged by contact-date maintenance alone. Normal source writes target `staging`; this maintenance does not authorise Commit Ready, Commit, candidate validation or Merge.
