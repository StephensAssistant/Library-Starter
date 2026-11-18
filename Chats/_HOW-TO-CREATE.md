# How to create a Chat entry

GitHub-only format: create the canonical item in this repository on `staging`, using this folder's current `README.md`, `_TEMPLATE.md` and schema where applicable; do not substitute ChatGPT Library, Google Drive or another external document.
Apply [AGENTS.md — Minimum necessary action control](../AGENTS.md#minimum-necessary-action-control) before executing this procedure. Its action boundary, evidence reuse and stop rules govern every step below.

## 1. Identify the daily file and reservation

Use today's `Chats/YYYY-MM-DD.md` and the current entry format in `Chats/README.md`. Search for an existing entry for the same logical checkpoint before adding another. Reserve a CHAT ID through SKILL-0024 only when a new entry is required, and read the committed reservation receipt. The allocator owns sequence/uniqueness: do not scan all daily files to calculate the maximum separately.

## 2. Assemble provenance

Append the reserved heading, tags, concise evidence-backed body, outbound `Links` and separator using the README format. Do not add frontmatter or reciprocal links. Name the literal ID of every materially changed Ticket/Project this entry documents before the final staged candidate is validated or merged. Do not duplicate or reuse a permanent ID.

## 3. Save, verify and stop

Ensure this entry and the record/plan changes it documents are all present in the final PLAY-0056 candidate. That procedure owns validation, generated views and staging confirmation. Read back the saved entry and stop. No PR or merge is authorised.
