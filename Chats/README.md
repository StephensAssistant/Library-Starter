# Chats — `CHAT`

A distilled record of a conversation — what was asked, what was decided, what it touched. Not a full transcript.

**Storage exception, per 00-LIBRARY-RULES.md §4/§6**: unlike every other type, a Chat entry does not get its own file. Multiple entries live inside a shared **daily** file, `Chats/YYYY-MM-DD.md` — the GitHub-native replacement for the old Drive Library's monthly volumes, split by day instead of by size, since Git has no equivalent 1M-character ceiling to design around.

**Entry format**, one per heading, inside the day's file. Copy `_TEMPLATE.md` and follow `_HOW-TO-CREATE.md`:

```
### CHAT-<NNNN> — <one-line summary>

Tags: [tag1, tag2]

<body — what was asked, decided, done>

Links: [ID1, ID2]

---
```

- `CHAT-<NNNN>` is still a permanent, globally sequential ID — same numbering discipline as every other type, just not one file per ID.
- **Links are directional provenance, not reciprocal** — per §6, a Chat entry links out to everything it discussed, relied on, or produced, but nothing links back to the Chat. This is the one type `auto-heal-links` deliberately does not touch.
- Tags fold into the entry itself rather than YAML frontmatter, matching §4b's storage exception for this type.

## Before changing this folder

- Reserve the `CHAT` ID and add the entry to the correct daily file.
- Include its heading, tags, concise evidence-backed body, and directional provenance links.
- Do not add frontmatter or reciprocal links: Chats are the explicit exception.
- Create Chat provenance only when it adds useful conversation evidence; ordinary work updates do not require a new Chat. Preserve existing entries and outbound links.
