<!-- super-skills-kit:start -->
## Super-skills kit

Full protocol files: `~/.claude/super-skills-kit/protocols/`.

### Entry optimizer (every user message)
Tier the message (reply / task / build / spec / epic). Work out the goal, deliverable, standing rules, done check and real gaps (max 3 questions). Never add scope the user did not give. Big or vague specs get the EARS pass. Build tier: run `superpowers:brainstorming` first if that plugin is installed; otherwise ask your questions one at a time and get a written OK on the design before building.
Reply line 1: `Optimized: <task, max 20 words> · Skills: <super-skill (mode)> + ... or none`
Full text: `entry-optimizer.md`.

### Skill loading
A hook suggests up to 5 super-skills per message. Load every one that clearly applies (usually 1-3), one per area, by reading its SKILL.md. Open members only through the mode table. Name super-skill paths in helper-agent briefs. A skill never overrides my rules. Full text: `skill-loading.md`. Index: `~/.claude/skill-library/SUPER-SKILLS.md`.

### Token diet
Helper agents on Sonnet, lookups on Haiku, Opus only for hard judgment with a one-line reason. Max 3-4 build agents with short briefs and step budgets. One phase per session; end with `docs/HANDOFF-<date>.md`. Replies of 1-3 sentences. Grep first, read with offset/limit, no re-reads, batch and parallelize tool calls. Full text: `token-diet.md`.

### Visual approval
For any non-trivial change, make an Artifact review page first (db + user capabilities): one card per change, old and new side by side, reason, a pick and a note. Explain in chat, wait, read the picks back, build only from them. Full text: `visual-approval.md`.

### Change protocol
Before any change to something live: prove the problem with real data, game out the fix system-wide, adjust and repeat, present on the review page (evidence, impact, risks, undo), then watch the first real runs. Full text: `change-protocol.md`.

### Ask first
Ask before anything outward-facing or paid (send, call, publish, buy, invite). Never print secrets.
<!-- super-skills-kit:end -->
