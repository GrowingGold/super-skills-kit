# Token diet

Tokens cost money and context. Follow these defaults unless the user says otherwise.

## Models for helper agents

- Helper agents run on Sonnet by default. The kit sets `CLAUDE_CODE_SUBAGENT_MODEL=sonnet` for this.
- Searches and lookups pass `model: "haiku"`.
- Use Opus for an agent only for hard judgment: a design council, a tricky bug, a final review. Say why in one line.

## How many agents

- At most 3-4 build agents at a time.
- Give each a short brief and a step budget (for example "about 40 tool calls").
- Merge their work yourself. Do not send a finished agent back just to re-merge.
- No subagent for a simple task. Use the direct tool.
- Keep workflows small. No heavy multi-agent workflow for routine work.

## One phase per session

- At the end of a phase, write a handoff file: `<project>/docs/HANDOFF-<date>.md`.
- Put in it: open tasks and who owns them, the user's latest picks and notes, decisions made, file paths and commit ids, pending approvals.
- Save anything worth remembering to memory, then tell the user to start a new session.

## When the context is compacted

Keep: open tasks and owners, the user's latest picks and notes, decisions made, file paths and commit ids, pending approvals.

## Short replies

- 1-3 sentences unless the user asks for detail. No essays. No recap of what you just did. Do not paste code back.
- Use the Concise output style if it is available (`/output-style`).

## Targeted reads and tool calls

- Search first (grep, glob), then read only the part you need (offset and limit).
- Never read a whole 500-line file unless you truly need all of it.
- Do not re-read a file you already read.
- Batch related edits. Make independent tool calls in parallel. Go straight to code you already know. Skip narration.

## Optional: RTK

RTK is a command-line tool that shortens noisy shell output. It is optional. Install it only if the user chooses to. It is not part of this kit.

## Weekly note (optional)

If the user wants it, once a week give a short token note: the total, the top 3 token burners, and one fix.
