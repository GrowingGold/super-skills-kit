# Skill review checklist (merged)

Built from skill-reviewer (evaluation checklist, PR template), skill-creator (progressive disclosure, evals, lack of surprise),
superpowers:writing-skills (description rules, pressure tests), writing-for-agents (pruning, ladder) and the user's intake log.
Use it for: reviewing any skill, the security pass of a library intake, and the self-check of a super-skill.
Sections A-G in order; H only when sending changes to someone else's repo. Done when every box is ticked or has a written finding.

## A. Security and fit (third-party skills, before anything else)
- [ ] List every file. Flag `scripts/`, hooks (`hooks.json`, settings snippets), commands, binaries, `package.json` install steps.
- [ ] Read each script and hook. Flag: network calls, telemetry or analytics, background workers (`nohup`, launch agents, loops), installers
      (`npx -y`, `curl | bash`, `pip install` at run time), hooks that fire on every tool call or log tool input/output to disk.
- [ ] Paid API or account needed (Exa, Firecrawl, fal, DashScope, Composio/Rube, X API...)? Note it: use asks the user first.
- [ ] Runtime it assumes (OpenClaw, Open Design `$OD_BIN`, dmux, babysitter, an in-app tool set) is installed here? If not, it does not run.
- [ ] English original, not a translated stub or placeholder (the `docs/ja-JP` trap); real instructions, not an auto-generated outline.
- [ ] Not a duplicate or mirror of a library skill or a built-in (`anthropic-skills:*`, `superpowers:*`). Check the catalog.
- [ ] License present or noted; commit pinned in the source comment.
- [ ] "Lack of surprise": nothing in it would surprise the user if described in one sentence [skill-creator].
- Verdict line: **add** / **add with library note** (what is disabled or needs asking) / **do not add** + one-line reason for the intake log.

## B. Frontmatter
- [ ] `name`: lowercase letters, digits, hyphens, max 64 chars; unique in the library (else `ecc-` prefix). "anthropic"/"claude" are reserved for claude.ai / API uploads.
- [ ] `description`: present, max 1024 chars, no `<` or `>`, one line or a valid YAML scalar (no bare `: ` or ` #` in a plain scalar), third person.
- [ ] Extra fields valid for where it runs (`disable-model-invocation`, `allowed-tools`, `argument-hint`, `model`; super-skills: `members`).
      The upload spec allows only `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility`.
- [ ] Run the frontmatter check from SKILL.md (Core rules: Frontmatter check): `quick_validate.py` when PyYAML exists, else the ruby one-liner.

## C. Description (the pointer)
- [ ] Says what it does, then when: concrete situations, file types, words users type [skill-creator, skill-reviewer].
- [ ] No workflow summary (Claude would follow the summary and skip the body) [writing-skills].
- [ ] Every branch the body handles has a trigger; synonyms of one branch collapsed unless it is a library skill scored by the router [writing-for-agents].
- [ ] Leading word first. Pushy enough that near-miss prompts still fire it ("even when X is not named").

## D. Body
- [ ] Imperative voice; explains why instead of ALL-CAPS MUSTs.
- [ ] Steps end on checkable completion criteria; a copyable checklist for multi-step work.
- [ ] Information ladder: every-branch material inline, branch-only material disclosed behind a pointer saying when to open it.
- [ ] Concept + rules + caveats co-located; no duplicated meaning; nothing restated from `--help` or config; no no-op sentences.
- [ ] Positive targets; any ban paired with its positive and reason.
- [ ] Examples for output formats.
- [ ] Under 500 lines (super-skills: hard cap 550).
- [ ] No stale facts: model ids, tool names, CLI flags, prices checked against the source (old-model prompts: `claude-api` `prompt-audit`).

## E. Resources
- [ ] References one level deep, self-explanatory names, loaded on demand, no duplication with SKILL.md; over 300 lines -> table of contents.
- [ ] Scripts: shebang, specific exception types, helpful error messages, recovery path, no hardcoded secrets.
- [ ] Assets are used in output, not loaded into context.

## F. Privacy (skills meant for sharing)
- [ ] No absolute user paths, personal or company names, phone numbers, IDs, keys or tokens. (personal skills may use `~` paths.)

## G. Behavior test
- [ ] Baseline: the target task without the skill; note the failures the skill should fix.
- [ ] With skill: same task; the failures are gone and nothing new broke.
- [ ] Trigger check: 3-5 prompts that should fire it, 2-3 near-misses that should not.
- [ ] Rule-enforcing skill: 2-3 pressure scenarios (time pressure, "just this once") and the rationalizations closed [writing-skills].
- [ ] Measured eval needed? Use the `anthropic-skills:skill-creator` loop; API-calling scripts ask the user first.

## Report template
```
Skill: <name>   Source: <repo @ commit or path>   Verdict: add | add with note | do not add
| Area | Status | Finding (file:line) | Fix |
| Security/fit | | | |
| Frontmatter | | | |
| Description | | | |
| Body | | | |
| Resources | | | |
| Privacy | | | |
| Behavior | | | |
Library note (if added): what is disabled, what needs the user's OK, paid APIs.
```

## H. Changes to someone else's repo (additive only) [skill-reviewer]
- Fork + feature branch; only with the user's OK to open a PR.
- Never delete files, remove features, rename components or change the primary language; add alongside instead
  ("added README.en.md, Chinese kept as default"; "added marketplace.json, metadata.json kept").
- PR body sections: Summary; What this PR does; **What this PR does NOT change**; Detailed changes (before / after / rationale);
  Files changed table; Test plan; References. End with the attribution line the session gives.
- Tone: describe benefits ("improved description for better discovery"), never "fixed the incorrect...".
- Self-check: no files deleted, no functionality removed, original language kept, author's design respected, every change explained.
