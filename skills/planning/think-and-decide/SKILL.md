---
name: think-and-decide
description: Pressure-test ideas, plans and decisions before anything is built or changed. Use for "grill me", "grill this plan", "stress-test", "poke holes", "think this through", "deep think", "should we", "go/no-go", "ship now or wait", "tradeoff", "which option", "second opinion", "devil's advocate", "council", "postmortem", "architecture review", "challenge my assumptions", "is this worth building", "validate the idea", "product brief", "prioritize features", "ICE", "time-to-value", "onboarding audit", "what do we call this", "glossary", "ADR", "domain model", "prototype this", "does this logic feel right", "show me UI variants", "teach me", "help me learn". Routes to design-tree grilling rounds, a 10-stage think loop, a four-voice council, product diagnostics, domain modeling (glossary + ADRs), throwaway logic/UI prototypes or a multi-session learning workspace, and ends with decisions the user can mark on a review page.
members: [grill-me, grill-with-docs, think, council, product-lens, domain-modeling, prototype, teach]
---

# Think and Decide

One place for every "should we / is this right / what exactly do we mean" moment. It merges eight skills into one method:
frame the real question, separate evidence from opinion, map the decision tree, challenge it at the depth the stakes deserve,
let a throwaway prototype settle what argument can't, and hand the user decisions they can mark. Load this file first; open a member
file only when a route says so. `superpowers:brainstorming` stays the front door for brand-new wants; this skill takes over
once there is a plan, idea or decision to pressure-test.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| New idea, vague want, the why is not clear yet | Discover | Skill `superpowers:brainstorming` (one open question per message, play-back, written design). Return here once something exists to test. |
| "Grill me", "stress-test this plan", a plan or design exists | Grill | Workflow steps 1-8, design-tree rounds (Core rules). Source text: Matt Pocock's public `grilling` skill (`members/grill-me/` is only a stub pointing there). |
| Grill and write the decisions down as we go (repo with its own vocabulary) | Grill with docs | Grill mode plus Domain-mode side effects. `members/domain-modeling/SKILL.md`, `members/domain-modeling/GLOSSARY-FORMAT.md`, `members/domain-modeling/ADR-FORMAT.md` |
| Consequential or ambiguous reasoning, tradeoff, postmortem, architecture review | Think | Full workflow at the depth step 0 picks; output shape in `references/decision-formats.md`. `members/think/SKILL.md` |
| Go/no-go, several credible paths, the user wants dissent, anchoring risk | Council | Four voices, three fresh subagents (costs 3 agent runs: say so first). `members/council/SKILL.md` |
| "Is this worth building", pick between features, launch sanity check, idea to brief | Product | Diagnostic, founder review, journey audit or ICE. `members/product-lens/SKILL.md` |
| Terms are fuzzy or clash, "what do we call this", glossary, ADR | Domain | Challenge terms, invent scenarios, check code, write lazily. `members/domain-modeling/SKILL.md` |
| "Does this state model / logic feel right?" | Prototype: logic | One self-contained HTML file over a pure module. `members/prototype/LOGIC.md` |
| "What should this look like?", "show me options" | Prototype: UI | 3 (max 5) structurally different variants behind `?variant=`. `members/prototype/UI.md` |
| "Teach me X" over several sessions | Teach | Learning workspace. `members/teach/SKILL.md` + `members/teach/*-FORMAT.md` |
| One-off "explain X", "what is X" | Learn | Skill `anthropic-skills:learn` |
| Decision made, next step is building | Hand off | Record it (step 9), then the `plan-and-execute` super-skill or `superpowers:writing-plans` |
| Trivial, reversible lookup or typo | None | Just answer. Skip the loop. |

## Unified workflow

### 0. Size the depth before anything else [think]
Depth follows stakes, irreversibility, uncertainty and novelty. Over-thinking a reversible call wastes the user's money; under-thinking an
irreversible one is how live systems break.

| Signal | Depth |
|---|---|
| Reversible in minutes, low stakes | Answer with one line of evidence. |
| Moderate stakes, reversible | Think-lite: evidence frame (step 2) + strongest counterargument (step 6) + Decision / Evidence / Risks. |
| Hard to reverse; money, customers or a live system; or the user asked for rigor | Full loop, all steps; grilling rounds or a council; decision cards to the user (step 8). |

Loop back whenever a later step exposes a missing observation or a misunderstood requirement [think].

### 1. Extract the real question [council, product-lens, think: LISTEN]
Write one sentence: what we are deciding, which constraints matter, what counts as success. For product questions add who it is for
(a specific person, not "users"), the pain (how often, how bad, what they do today) and why now [product-lens]. If the question itself
is vague, ask one clarifying question before anything else [council]. Ask only questions whose answers could change the outcome [think].

### 2. Build the evidence frame and fetch facts yourself [think, grilling]
Sort everything into **Observed** (directly supported by an input, test or measurement), **Inferred** (state the bridge), **Unknown**
(missing evidence that could flip the decision) and **Preference** (a choice, not a fact) [think]. Say what you inspected in full versus
sampled [think: OBSERVE].

Finding facts is your job; decisions are the user's [grilling]. If a fact lives in the filesystem, a database, an API or logs, look it up
(a lookup subagent is fine; Haiku for pure lookups). Don't block on it: only the questions downstream of that fact wait; ask the rest now.
Never fabricate a quote, locator, test result, consensus or confidence number [think].

### 3. Check yourself before hearing others [think: OBSERVE internal, council step 3]
Name the one or two biases most likely here: anchoring, ownership, novelty, familiarity, urgency, sunk cost, confirmation, a desired
verdict. Then write your own position (recommendation, its three strongest reasons, its main risk) before reading council voices,
prototype results or the user's stated preference, so the synthesis can't simply mirror them [council].

### 4. Map the design tree [grilling]
List the decisions; under each, the decisions that hang off it. The **frontier** is every decision whose prerequisites are settled:
the questions you can ask now without guessing answers you haven't heard. The tree is the progress bar: you are done when the frontier
is empty and no branch was silently assumed.

### 5. Reason the frontier down [think: THINK, CONNECT]
For each frontier decision: invariants, alternatives (think wide privately, drop the weak ones), tradeoffs and failure modes; failure
behavior is part of the spec. **Lateral:** the same structure in an adjacent component or domain; use an analogy only with its mapped
similarities and limits stated. **System:** upstream inputs, downstream consumers, ownership, state boundaries, interfaces, recovery
paths; check whether a locally sound choice breaks something elsewhere. In the user's ops this is the game-out list: every workflow, node
that reads `$json`, DB trigger, dashboard, daily check, and the other companies' copies. Prefer the smallest reversible test that
could disprove the leading option [think].

### 6. Challenge at the strength step 0 chose
Use one or more:
- **Language** [domain-modeling]: call out a term that conflicts with `GLOSSARY.md` ("your glossary says cancellation is X, you mean Y?");
  propose one canonical word for fuzzy or overloaded ones ("account: Customer or User?"); invent edge-case scenarios that force precise
  boundaries; check whether the code agrees with what is being claimed and surface contradictions.
- **Product** [product-lens]: 10-star version, MVP that proves the thesis, anti-goal, the metric that shows it works (not vibes);
  ICE when there are many options.
- **Counterargument** [think: ACCEPT]: the strongest reasonable case against your preferred answer; unfavorable findings stated plainly;
  agreement is not correctness.
- **Human side** [think: FEEL]: cognitive load, trust and error recovery for the user, their team, the customer. Intuition is a signal to
  investigate, never evidence.
- **Council** [council]: at full depth with several credible paths. Three fresh subagents get only the question and compact context
  (that isolation is the anti-anchoring mechanism), one strict role each, under 300 words; synthesize with the guardrails in Core rules.

### 7. Let a prototype settle what paper can't [prototype]
When the argument is about how logic behaves or how something looks, stop debating and build a throwaway that answers one question.
- **Logic:** one HTML file, no framework or server. A pure module (reducer, state machine, pure functions or a class, whichever fits
  the question) plus a thin page in domain language: the question at the top, a readable current-state panel re-rendered after every
  click, free-play buttons, and guided walkthrough tabs (happy path, tricky edge case, an attempt at something that should be illegal),
  each starting from a known state. For the user, publish it as a private Artifact (load `artifact-design` first) so they can click it anywhere.
- **UI:** variants on the existing page (preferred) behind `?variant=`, keeping real data fetching; a floating switcher with arrows and
  arrow keys (ignored inside inputs), hidden in production builds. Variants must disagree on structure, not color.

"Wait, that shouldn't be possible" is a bug in the idea, which is the point. Fold the validated decision back into steps 5-8.

### 8. Put the decisions to the user [grilling + visual approval protocol]
Ask the whole frontier in one round: numbered, each with your recommended answer, worded so "yes" accepts it. A question that depends
on another still open in this round waits for the next one. Recompute the frontier after every round. Formats in
`references/decision-formats.md`.

Where the round goes:
- Three questions or fewer and nothing touches a live system: in chat.
- More than that, or any decision changes an agent, prompt, n8n workflow, dashboard or data: a review page, one card per decision (what it
  is, old vs new side by side, the reason in plain words, a pick of accept / alternative / original / my own wording, plus a note box)
  saved to the page's store. Read the picks back and build only from them; a note beats the radio. Load `artifact-capabilities` for the
  `db` + `user` capabilities.

Don't act until the user confirms a shared understanding [grilling].

### 9. Record only what earns it [think, domain-modeling, council]
- **Decision record:** Decision / Evidence / Counterargument and risks / Verification / Growth loop [think].
- **ADR** only when all three hold: hard to reverse, surprising without context, the result of a real tradeoff [domain-modeling].
  One paragraph is enough. Repo: `docs/adr/NNNN-slug.md`. Ops project: the project doc or worklog.
- **Glossary:** update inline the moment a term resolves, never batched [domain-modeling].
- **Lesson** that should change future behavior: a short note in the project memory (Why / How to apply), not a "save" skill.
  Persist only when it changes something real [council].

### 10. Close the loop [think: GROW + verification discipline]
Before calling it done: test the highest-risk claim or say why it stays untested; look for disconfirming evidence; match verification
effort to blast radius; list the commands, sources and artifacts actually used; separate "this check passed" from the broader
correctness it doesn't prove; give confidence in words with reasons. Name the feedback signal that should reopen the decision and when
to revisit. Then hand off to `plan-and-execute`.

## Core rules and checklists

### Grilling rounds [grilling]
- Rounds over one-by-one: ask the full frontier, each question with a recommendation, then wait.
- "Yes" must accept your recommendation; multiple choices go inside the question body.
- A running fact lookup is an unsettled prerequisite: hold only its downstream questions.
- Never ask the user for a fact you can look up; always put the decision to the user.
- Done = empty frontier + the user confirms shared understanding.

### The ten stages, one line each [think]
1 OBSERVE external: read the real inputs, state, failures, prior work. 2 OBSERVE internal: biases, recalibrate confidence.
3 LISTEN: intent, success condition, unstated stakes, dissent, edge cases. 4 THINK: invariants, alternatives, tradeoffs, failure modes.
5 CONNECT lateral: same structure elsewhere, analogy with limits. 6 CONNECT system: upstream, downstream, ownership, recovery.
7 FEEL: load, trust, accessibility, recovery experience. 8 ACCEPT: constraints, contradictions, strongest counterargument.
9 CREATE: the smallest useful artifact (recommendation, record, experiment, draft, handoff), assumptions marked; no state changes.
10 GROW: feedback signal, revisit condition, reusable lesson. Use them as a loop of attention, not a transcript.

### Council [council]
- Use for: multiple credible paths, explicit tradeoffs, requests for dissent, anchoring risk, go/no-go. Not for: code review
  (`code-review` skill), implementation planning (`plan-and-execute`), factual questions or obvious tasks (just do them).
- Voices: **Architect** (you: correctness, maintainability, long-term effects), **Skeptic** (challenge the framing, simplest credible
  alternative), **Pragmatist** (shipping speed, user impact, operational reality), **Critic** (edge cases, downside, failure modes).
- Each voice returns Position (1-2 sentences), Reasoning (3 bullets), Risk, Surprise (one thing the others may miss).
- Synthesis guardrails: never dismiss a voice without saying why; say so if a voice changed your recommendation; always show the
  strongest dissent; two voices against your initial position is a real signal; raw positions stay visible before the verdict.
- Verdict: Consensus / Strongest dissent / Premise check (did the Skeptic challenge the question?) / Recommendation. Phone-scannable.
- One round by default. A second round gets a focused question; keep the Skeptic as clean of prior context as possible.
- Anti-patterns: feeding voices the whole transcript, hiding disagreement, persisting every verdict.

### Product lens [product-lens]
- **Diagnostic (7 questions):** who exactly; the pain quantified; why now; 10-star version; MVP; anti-goal; the metric. Output a short
  brief with answers, risks and go/no-go. If "go", the next lane is a plan, not more founder theater.
- **Founder review:** infer what the project is trying to be (README, CLAUDE.md, package.json, recent commits; for a store or site, the
  live pages and product list); score product-market-fit signals 0-10 (usage trajectory, retention, revenue signals, moat); name the one
  thing that would 10x it and the work that doesn't matter.
- **Journey audit:** go through as a brand-new user, log every friction point, time each step, compare with a competitor, score
  time-to-value (time to first win), recommend the top 3 fixes.
- **ICE:** (impact 1-5 x confidence 1-5) / effort 1-5; rank; then apply constraints (runway, team, dependencies); output a ranked list
  with rationale. Every recommendation ends in a specific next step.

### Domain modeling [domain-modeling]
- Glossary entries: bold term, 1-2 sentences on what it IS (not what it does), `_Avoid_:` aliases; be opinionated; only terms specific to
  this project (no general programming concepts); no implementation details; group under subheadings when clusters appear.
- Multiple contexts: a root `GLOSSARY-MAP.md` lists each context, where it lives and how contexts relate; infer the context, ask if unclear.
- ADRs that qualify: architectural shape, integration patterns between contexts, technology with real lock-in, boundary and scope
  decisions (the explicit no's too), deliberate deviations from the obvious path, constraints invisible in code, non-obvious rejected
  alternatives. Optional sections (Status, Considered Options, Consequences) only when they add value.
- Create files lazily; number by scanning for the highest existing number + 1.

### Prototype rules [prototype]
0. Pick the branch from the question ("does it feel right?" = logic, "what should it look like?" = UI); getting it wrong wastes the
   whole prototype. If it is ambiguous and the user is away, default by the surrounding code (backend module = logic, page or component = UI)
   and state the assumption at the top.
1. Throwaway from day one and named so (e.g. `prototype` in the path), placed next to what it explores.
2. Trivial to run: one command, or a file the user double-clicks / an Artifact link.
3. No persistence unless persistence is the question; then a scratch DB or file named "PROTOTYPE, wipe me". Never a live system.
4. Skip polish: no tests, no error handling beyond runnable, no abstractions, no "what if later".
5. Surface the full relevant state after every action or variant switch.
6. Capture the verdict and the question it settled; fold the validated logic into real code (rewritten properly, with tests).
- Logic: keep the module pure (no DOM, no handlers reaching in) so it lifts into the codebase; restrained styling, one accent color.
- UI: default 3 variants, cap 5; a shared header is fine, a shared layout defeats the point; read-only or stubbed mutations;
  the useful feedback is "header from B with sidebar from C".

### Teach [teach]
- No lesson before a mission: if `MISSION.md` is empty, interview for the concrete real-world goal first (one mission per workspace).
- Knowledge comes from curated high-trust sources in `RESOURCES.md` (annotated, pruned, gaps listed), not parametric memory; cite in lessons.
- A lesson is one short self-contained HTML file (`lessons/0001-slug.html`): one tangible win inside the zone of proximal development,
  a primary source to read or watch, links to other lessons and reference docs, a reminder to ask follow-ups. Reuse `assets/` components
  and a shared stylesheet. Open it for the user (`open <file>`) or publish it as a private Artifact so they can read it on their phone.
- Aim for storage strength over fluency: retrieval practice, spacing, interleaving (skills only). Difficulty is the enemy while acquiring
  knowledge and the tool while building skill. Tight, ideally automatic feedback loops.
- Quiz answers: same word count (and length) for every option; vary the correct position; no formatting clues.
- Learning records (`learning-records/0001-slug.md`) only for demonstrated understanding, disclosed prior knowledge, corrected
  misconceptions, or a mission shift; supersede, don't delete. Coverage is not learning.
- Wisdom comes from communities: suggest high-reputation ones unless the learner opted out (record that in `RESOURCES.md`).

## When members disagree

| Between | Issue | Rule |
|---|---|---|
| superpowers:brainstorming vs grilling | One open question per message vs the whole frontier per round with recommendations | Phase decides: discovering what the user wants = brainstorming; testing a plan that exists = grilling rounds (fewer turns, cheaper for the user). |
| think vs domain-modeling / grill-with-docs / prototype | Think is read-only; the others write files | Think and Council modes never write. Glossary/ADR writes only in Domain or Grill-with-docs mode, inside the repo or project folder in play. Prototypes write only marked throwaway files. No mode touches a live system. |
| council vs the user's cost rules | Three subagents per use vs "no subagents for simple tasks, Haiku for lookups" | Council only at full depth; announce "3 agent runs" first; voices run on the default model (reasoning, not lookup). Below full depth, use an in-context counterargument and say it is weaker against anchoring. |
| think vs product-lens | "No decorative percentages" vs 0-10 PMF scores and ICE numbers | Numbers are allowed as ranking inputs with one line of evidence each; confidence is always stated in words. |
| prototype vs the user's git rule | Commit the prototype to a throwaway branch vs commit/push only when the user asks | Keep prototypes in the scratchpad, a marked prototype path, or a private Artifact; offer the throwaway-branch capture and do it only on their yes. |
| grilling vs "operate autonomously" | Wait for confirmation vs don't ask permission | Lookups, reading, drafting, prototypes: autonomous. Decisions that change what gets built or a live system: the user's, asked in rounds. |
| council vs grilling | Ask one clarifying question vs ask the whole frontier | Council's single question frames the question itself, before anything else; grilling rounds start once it is framed. |
| domain-modeling vs ops work | ADRs in `docs/adr/` vs ops work with no repo | Repo: `docs/adr/`. Ops: the decision goes in the project doc or worklog. |
| teach vs anthropic-skills:learn | Stateful multi-session workspace vs in-chat explanation | One question = learn. "I want to get good at X" over weeks = teach workspace in a folder the user names. |
| product-lens founder review vs the user's brands | Reads README/package.json vs stores and sites | For a store or site, read the live pages, catalog and (read-only) analytics; same scoring. |

## Combine with
- `superpowers:brainstorming` (always on): discovery before this skill; its builder check is the same cold read as step 10.
- `anthropic-skills:learn`: quick explanations instead of a Teach workspace.
- `superpowers:writing-plans` or the `plan-and-execute` super-skill: right after the decision is recorded.
- `artifact-design` and `artifact-capabilities` skills: before building a review page or an Artifact prototype.
- `deep-research` skill / `research-hub` super-skill: when the evidence frame needs outside sources (paid search APIs ask first).
- Specialist prompts (pass the file as the Agent prompt plus the question; good council voices or second opinions):
  - `~/.claude/skill-library/agents/voltagent/10-research-analysis/first-principles-thinking.md`: rebuild from fundamentals; a strong Skeptic.
  - `~/.claude/skill-library/agents/voltagent/08-business-product/assumption-mapping.md`: riskiest assumptions before a go/no-go.
  - `~/.claude/skill-library/agents/voltagent/10-research-analysis/project-idea-validator.md`: blunt idea teardown with competitor check.
  - `~/.claude/skill-library/agents/voltagent/08-business-product/product-manager.md`: prioritization and roadmap second opinion.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/architect-reviewer.md`: Architect voice for system-design calls.
  - `~/.claude/skill-library/agents/voltagent/08-business-product/ux-researcher.md`: journey audits and the FEEL stage.

## House rules (the user)
- Every decision that changes something goes on a review page: one card per change, old vs new, plain reason, pick + note; build only
  from their picks; anything kept against a pick gets its own card.
- Slow and correct: never recommend an apply until each protocol box has evidence in chat: the proven problem, exact diff, blast radius,
  sandbox result, tested undo.
- One decision or fix at a time, carried through to verification on real traffic before starting the next.
- the user-facing options are 2-3 plain steps and yes/no questions with your recommendation; detail lives in the document, not the question.
- Paid APIs and anything that sends, publishes, posts, buys or calls a live system ask the user first; prototypes and councils never touch
  live systems.
- Say what a council or research fan-out will cost before launching it; Haiku only for pure lookups.

## Members

| Member | Best at | Path |
|---|---|---|
| grill-me | Entry point for a relentless plan interview; the method itself lives in `grilling` (design tree, frontier rounds, recommended answers) | `members/grill-me/SKILL.md` (stub) + Matt Pocock's public `grilling` skill |
| grill-with-docs | Grilling that writes GLOSSARY.md and ADRs as decisions land | `members/grill-with-docs/SKILL.md` (stub: grilling + domain-modeling) |
| think | Depth scaling, evidence frame, bias check, 10-stage loop, verification discipline, decision output shape | `members/think/SKILL.md` |
| council | Anti-anchoring four-voice council with fresh subagents and synthesis guardrails | `members/council/SKILL.md` |
| product-lens | Product diagnostic questions, PMF scoring, time-to-value journey audit, ICE ranking | `members/product-lens/SKILL.md` |
| domain-modeling | Challenging terms against a glossary, edge-case scenarios, glossary and ADR formats with a strict ADR test | `members/domain-modeling/SKILL.md`, `GLOSSARY-FORMAT.md`, `ADR-FORMAT.md` |
| prototype | Throwaway prototypes that answer one question: clickable logic demos and switchable UI variants | `members/prototype/SKILL.md`, `LOGIC.md`, `UI.md` |
| teach | Multi-session learning workspace: mission, trusted resources, short HTML lessons, learning records, retrieval and spacing | `members/teach/SKILL.md`, `MISSION-FORMAT.md`, `RESOURCES-FORMAT.md`, `LEARNING-RECORD-FORMAT.md`, `GLOSSARY-FORMAT.md` |

If a member folder is missing (not installed), work from this file alone.
