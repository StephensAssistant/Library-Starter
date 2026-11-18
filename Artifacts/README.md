# Artifacts — `ART`

A file that is itself the deliverable: a script, spreadsheet, document, deck, configuration, dataset, or other reusable output. Each Artifact consists of the raw native-format file and a Markdown companion record filed together and linked to every relevant source record.

Plain text documentation uses `.md`. Native content keeps its real extension—for example, SQL uses `.sql`, Python uses `.py`, JSON uses `.json`, and equivalent formats follow the same rule.

A short code snippet used only for a quick yes/no check may remain inline in its source Markdown record. Any genuine reusable or runnable script must become its own Artifact file and be linked bidirectionally to that source.

Filenames: `ART-<NNNN>-<slug>.<ext>` for the native file, with a matching Markdown companion record.

Create the companion from `_TEMPLATE.md` using `_HOW-TO-CREATE.md`.

## Before changing this folder

- Confirm the item is a reusable deliverable, not a short one-off snippet.
- Reserve the required consecutive `ART` IDs; ensure the native file and Markdown companion are both present in the final staged candidate.
- Validate the companion's `stored_at` path and every reciprocal link to the source records.
