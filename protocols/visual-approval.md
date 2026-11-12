# Visual approval

Use this for every non-trivial change: prompts, automations, dashboards, database writes, site or app edits. The user should see what you plan, mark each item themselves, and never have to guess what you did.

## Steps

1. Document first. Change nothing yet.
2. Build a review page as an Artifact, with the `db` and `user` capabilities so picks are saved. Load the `artifact-design` and `artifact-capabilities` skills before writing it. The page has:
   - one card per change
   - the old and the new side by side
   - the reason in plain words
   - a pick per card (accept / alternative / keep the original / my own wording) and a note box
   - your suggested pick marked as suggested, and an "accept all suggestions" button
3. Explain in chat what the page contains, in a few lines. Then stop and wait.
4. Read the picks back with the Artifact tool (`read_db`, list the collection). Copy them into the project folder and record them in the project notes.
5. Build only from the picks.
   - A note always beats the radio choice.
   - If you must keep something against a pick (for a technical reason), show it as its own card with the reason. Never do it silently.
   - Anything new you find mid-build goes back on a page before you apply it.
6. Dry run first, with a full diff, in a sandbox or copy if one exists. Then apply. Then watch the first real runs end to end in the destination system, not just the new step's output.
7. Report results in a before and after table. Keep the page URLs in the project notes so the user can reopen them.

## Fallback

If the Artifact tool or its saved picks are not available:

- Write a local HTML review page with the same cards and open it for the user.
- The user types their picks and notes in chat.
- Everything else stays the same: build only from the picks, show any exception as its own card.

## Rules

- No hidden work. If it is not on a card, do not do it.
- The user's words are the approval. Your suggestion is not.
