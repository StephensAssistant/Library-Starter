# Library Reference

`Reference/` stores authorised, read-only schema snapshots and data exports that help an AI understand source structures without pasting large files into chat.

## Rules

1. Upload only authorised, non-secret material. Customer-level, personal, credential, token, and private-key content is prohibited.
2. Use descriptive, versioned filenames such as `orders-schema-2026-08-30.csv`; do not overwrite an earlier snapshot.
3. Files are immutable after admission to `main`. Add a newer version instead of editing, renaming, moving, or deleting the earlier evidence.
4. Reference files are supporting evidence, not governed records or automatic sources of truth. Cite the relevant Project, Ticket, Knowledge, or Artifact when using them consequentially.
5. Automated intake analysis may read, hash, index, lint, and report on these files. It never reformats or alters them.

## Automated analysis

The consolidated reconciliation workflow publishes a downloadable JSON report and a compact run summary. Reports include exact duplicates, redacted security findings, suspicious-content indicators, routing suggestions, SQL dependencies, lint warnings, and byte/line chunk ranges for large files.

Suspicious-content screening is deterministic triage, not a replacement for endpoint antivirus. A security finding blocks validation; matched secret values are never printed.


## Before changing this folder

- Admit only authorised, non-secret evidence with a descriptive versioned filename.
- Never overwrite, rename, move, or delete a snapshot admitted to `main`; add a new version instead.
- Link consequential use back to the authoritative Project, Ticket, Knowledge, or Artifact.
