# Playbooks — `PLAY`

A reusable procedure combining Skills to achieve one defined outcome, with an explicit trigger, necessary checks and an exit. Workflows in `Workflows/` orchestrate Playbooks and nested Workflows across outcomes, decisions and handoffs. Hats own or review actions at any layer. Existing Playbooks remain authoritative until explicitly reviewed; this distinction does not automatically migrate or renumber them.

Filenames: `PLAY-<NNNN>-<slug>.md`

Added 2026-08-14, per the Library owner's explicit sign-off (the ninth type, per the old Library's §1a rule that a new folder is never created unilaterally).

Create from `_TEMPLATE.md` using `_HOW-TO-CREATE.md`.

Keep explanations, reference material and standards in Knowledge. If an existing Knowledge record owns a recurring executable procedure, create a Playbook only where that distinction is justified. Supersede the source after the replacement validates and its live links migrate. Verify a generated discovery index before retiring its predecessor. Ask the owner for material thresholds, timing, approvers and escalation routes as needed. The owner makes live decisions and authorises external effects.

## Before changing this folder

- Create a Playbook only for a distinct reusable procedure with a real trigger and exit; keep one-off procedures in their work record.
- For a new record, reserve the `PLAY` ID, satisfy base frontmatter, use `current` or `superseded` status, and add evidence-backed reciprocal links.
- Add its intent-routing contract and benchmark case before candidate validation.

## Supporting Skills and workflow admission

For workflow use, every Playbook must have the correct, complete supporting Skills for its actual requirements, including indirect Playbook calls. Name existing SKILL IDs and preserve confirmed reciprocal canonical associations. Verify input/output compatibility, prerequisites, material branches, failure/recovery and observable success against actual Skill contracts. Follow Workflows/README.md for requirement coverage and independent approval evidence. Missing or incomplete support is a blocking gap: search/reuse first; amend the same owner or create a distinct governed capability, then test affected callers and re-review. No material ambiguity may be silently filled by the operator or AI. This is a requirement for workflow admission, not a claim that every existing Playbook has already been assessed.
