---
name: ux-lab
description: "Design reasoning and evaluation for any screen, flow or conversation: critique a rendered screen (visual hierarchy, composition, typography, colour, affordance, information density, brand consistency), heuristic evaluation, UX laws (Fitts, Hick, Miller, Jakob, Doherty, Tesler, Peak-End, serial position, Von Restorff, Zeigarnik, aesthetic-usability, Gestalt proximity, similarity, common region, closure, continuity, figure-ground), interaction patterns (forms, validation, navigation, search, errors, feedback, toasts, loading states, skeletons, gestures, micro-interactions, animation feel, state machines), conversational and voice UX for voice agents, SMS agents, chatbots and IVR, and usability research (test scenarios, first-click tests, user flows, wireframe specs and lo-fi SVG wireframes, prototype fidelity, concept selection). Use for 'critique this', 'design review', 'why is this confusing', 'users can't find X', 'wireframe/sketch this screen'. Building UI goes to ui-studio."
members: [aesthetic-usability, animation-principles, click-test-plan, concept-selection, conversational-ux, critique-affordance, critique-brand-consistency, critique-color, critique-composition, critique-information-density, critique-typography, critique-visual-hierarchy, doherty-threshold, error-handling-ux, fitts-law, form-design, gesture-patterns, heuristic-evaluation, hicks-law, interfaces-that-feel, jakobs-law, law-of-closure, law-of-common-region, law-of-continuity, law-of-figure-ground, law-of-proximity, law-of-similarity, loading-states, micro-interaction-spec, millers-law, navigation-patterns, parallel-concepts, peak-end-rule, prototype-strategy, search-ux, serial-position-effect, state-machine, teslers-law, test-scenario, user-flow-diagram, von-restorff-effect, wireframe-spec, zeigarnik-effect, design-critique, wireframe]
---

# UX Lab

One place for design reasoning and evaluation: 17 UX and Gestalt laws, 12 interaction-pattern skills, 7 screen-critique
lenses plus a product design critique pass, heuristic evaluation, conversational and voice UX, and usability research with
drawn lo-fi wireframes (46 members). The heart is a
critique-and-improve loop that uses the laws as reasons for findings, not as a checklist to recite. Load this file first,
pick a mode, and open a member (`members/<name>/SKILL.md`) only when a row or step points to it. ux-lab judges and
specifies; ui-studio builds. The merged critique checklists live in `references/critique-lenses.md`.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| "Critique this screen", a screenshot, URL or Figma frame, "what's wrong with this page", pre-launch screen review | **Screen critique** (default) | Unified workflow steps 1-9, all lenses A1-A7 plus B1, B5, B7 from `references/critique-lenses.md`. |
| "Why is this confusing", "can people tell what to do here", quick functional check | **Quick UX check** | Steps 1, 3, 4, 5, 7 with three lenses only: A1 hierarchy, A6 affordance, A7 density. End with one sentence: the biggest functional risk. |
| Review a whole flow or product area (checkout, signup, intake), no users available | **Heuristic evaluation** | Steps 1-9; the flow map in step 2 is mandatory; two walk-throughs; Nielsen coverage check (§C of the lenses file); `members/heuristic-evaluation/SKILL.md`. |
| Screen against brand files (DESIGN.md, brand guidelines, voice doc, tokens) | **Brand check** | Lens A5; `members/critique-brand-consistency/SKILL.md`. A missing file means that dimension is skipped, never invented. |
| "Which law explains this", "apply Fitts / Hick / ...", justify a layout decision | **Laws** | Law finder table (Core rules), then the law's member file. Cite a law as the cause of a finding, never as decoration. |
| Grouping reads wrong, too many borders or cards, eye jumps, unclear overlay or selected state | **Gestalt** | Lens A2 and the law finder rows Proximity to Figure-ground; `members/law-of-<name>/SKILL.md`. |
| Design or fix a form, validation, which input type | **Pattern: forms** | Design-a-pattern path + Forms checklist; `members/form-design/SKILL.md`. Which fields to cut for lead conversion: also conversion-lab (Form). |
| Navigation, menus, tabs, sidebars, labels, "users can't find X" | **Pattern: navigation** | Navigation table + lens B4; `members/navigation-patterns/SKILL.md`; prove the labels with a first-click test (Research path). |
| Search box, autocomplete, filters, zero results, search analytics | **Pattern: search** | Search checklist; `members/search-ux/SKILL.md`. |
| Error messages, failure states, recovery, permission errors | **Pattern: errors** | Lens B2; `members/error-handling-ux/SKILL.md`. |
| Toasts, confirmations, status badges, notifications, "did it work?" | **Pattern: feedback** | Feedback rules + lens B1; `members/feedback-patterns/SKILL.md`. |
| "Feels slow", spinners, skeletons, optimistic UI, latency budget | **Pattern: waiting** | Response ladder (Numbers); `members/doherty-threshold/SKILL.md`, `members/loading-states/SKILL.md`. Measuring and fixing real speed: react-next-pro or the performance-engineer agent. |
| Swipe, drag, long-press, pinch, pull-to-refresh | **Pattern: gestures** | Gesture rules; `members/gesture-patterns/SKILL.md`. iOS/Android standard gestures: mobile-app-studio (platform conventions). |
| Spec one interaction for engineering, or how one animation should feel | **Micro-interaction** | Spec template (Core rules); `members/micro-interaction-spec/SKILL.md`, `members/animation-principles/SKILL.md`. Motion tokens and code: ui-studio (Motion). |
| Component or flow with many states, "impossible states", async edge cases | **State machine** | Method (Core rules); `members/state-machine/SKILL.md`; draw it as Mermaid `stateDiagram-v2`. |
| "Works but feels cold, flat, robotic", celebration, endings, resume and re-engagement moments | **Emotion** | Lens B7; `members/interfaces-that-feel/SKILL.md`, `members/peak-end-rule/SKILL.md`, `members/zeigarnik-effect/SKILL.md`, `members/aesthetic-usability/SKILL.md`. |
| Voice agent, SMS agent, chatbot, IVR: turns, reprompts, confirmations, persona, transcript review | **Conversational** | Conversational path + House rules; `members/conversational-ux/SKILL.md`. Prompt mechanics: prompt-engineer agent. |
| Usability test tasks, "test it with users" | **Research: scenarios** | Research path; `members/test-scenario/SKILL.md`. |
| Findability, first-click, five-second impression, nav label test | **Research: click test** | Research path step 4; `members/click-test-plan/SKILL.md`. |
| Map how users move through a feature, its branches and error paths | **Flow map** | Step 2; `members/user-flow-diagram/SKILL.md`; render as a Mermaid flowchart (built-in `artifact-diagramming`). |
| Structure before visuals, annotated wireframe spec for engineering | **Wireframe spec** | `members/wireframe-spec/SKILL.md`; styling later in ui-studio. |
| "Wireframe / sketch this screen", lo-fi mockup, draft a layout, a page of all screens to click through | **Wireframe (drawn)** | Core rules: Lo-fi wireframes. `members/wireframe/SKILL.md`, primitives `members/wireframe/references/components.md`, worked examples `references/examples.md`, viewer `assets/site-template.html`. |
| "Should we prototype this, and how", fidelity choice | **Prototype strategy** | Research path step 3; `members/prototype-strategy/SKILL.md`. The throwaway build itself: think-and-decide (Prototype: UI or logic). |
| One direction on the table, "show me alternatives", "explore options" | **Explore** | `members/parallel-concepts/SKILL.md`, then Converge. |
| Several directions alive and one must win | **Converge** | `members/concept-selection/SKILL.md`; decision record; the user picks on a review page. |
| Build, restyle, polish, tokens, components | hand-off | ui-studio leads; ux-lab reviews the result with Screen critique. |
| WCAG audit, keyboard, screen readers | hand-off | web-a11y (critique flags contrast, targets and focus at screen level only). |
| A/B test, onboarding and activation, pricing page, CRO | hand-off | conversion-lab. |
| Charts, ops dashboards | hand-off | dashboard-studio. |

Super-skill paths: `~/.claude/skill-library/<area>/<name>/SKILL.md` (index `~/.claude/skill-library/SUPER-SKILLS.md`).

## Unified workflow: critique and improve

One loop for a screen, a flow or a conversation. Every critique runs steps 1-9; the Design-a-pattern, Conversational and
Research paths below reuse it. The laws enter at the step where they explain something, so each finding carries its cause.

### 1. Frame the job (write it down, five lines)
- **Who and in what state:** who arrives, from where, on what device, feeling what (anxious, rushed, celebrating,
  recovering from an error). Start from the felt state, not the task [interfaces-that-feel].
- **The one job** of this screen or flow and its success signal (purchase, booking, completed intake, setting found). On
  the user's stores the job is converting visitors into buyers (House rules).
- **Frequency and stakes:** frequent or high-stakes steps must stay conventional and fast; rare ones have latitude [jakobs-law].
- **Expertise:** novices need fewer simultaneous choices; experts chunk more and want shortcuts [millers-law, hicks-law].
- **Evidence on hand:** analytics, recordings, search logs, transcripts, support themes. With none, every finding is
  labelled "expert judgment" in step 5.
- **Missing the job?** If who the user is, their job here or what success looks like can't be inferred, ask before
  critiquing; without them a critique grades taste. Also note what comes right before and after this screen [design-critique].

### 2. Get the real thing and map the path
- **Render, don't read code.** Screenshot at 390 px and 1440 px (Playwright MCP, or the built-in `run` skill for a local app)
  and capture every state the job touches: default, hover and focus, empty, loading, error, success, disabled
  [critique-affordance, wireframe-spec]. A screen reviewed only in its happy state hides most of its problems.
- **Map the flow** for anything longer than one screen: entry, screens, decisions, system steps, end; happy path first,
  then error and exit paths; one flow per user goal; every arrow labelled with its trigger [user-flow-diagram].
- **Annotate the map with the flow-level laws.** Decisions per step [hicks-law]; what the user must remember from one step to
  the next [millers-law]; work pushed onto the user that the product could do [teslers-law]; where the peak and the end are
  [peak-end-rule]; where an interruption can happen and whether the user can resume exactly there [zeigarnik-effect]; which
  steps sit in the forgettable middle [serial-position-effect]. Single-screen critique never sees these.
- **Conversations:** the render is real transcripts or recordings plus the agent's flow and prompt; map turns instead of
  screens [conversational-ux].

### 3. First-glance read (a five-second test on yourself)
Before any checklist, write two or three lines on what a first-time user sees in five seconds: the entry point, what reads
as foreground, how the screen groups, and the one action it asks for [click-test-plan five-second test]. Blur or squint at
the screenshot: groups must be legible without the words [law-of-proximity], one element must dominate [von-restorff-effect],
foreground must separate from background [law-of-figure-ground]. Compare with the job from step 1; a mismatch here is
usually the top finding.

### 4. Run the lenses
Run the lenses the mode calls for from `references/critique-lenses.md`: visual A1-A7 (hierarchy, composition and Gestalt,
typography, colour, brand, affordance, density) and interaction B1-B7 (status and waiting, errors, forms, navigation,
conventions, motion, emotion). Walk the flow twice: as a first-time user, then as someone doing it for the tenth time
[heuristic-evaluation]. Measure instead of eyeballing whatever can be measured: contrast ratio, target size, type size,
step count, decisions per step, response time.

### 5. Write every finding the same way
Observation (neutral) -> Problem (what breaks for the user and why, with the law or heuristic as the cause) -> Fix (the
exact value, token, copy, placement or pattern) -> Severity 0-4 -> Evidence (crop, measured value, transcript line,
metric) -> Confidence (observed or expert judgment) -> Nielsen heuristic. Rate each lens pass / minor issue / major issue
[critique-*, heuristic-evaluation]. Template: lenses file §D.

### 6. Find root causes
Cluster the findings and ask which single cause produces several. A missing spacing scale shows up as proximity, rhythm
and alignment findings; no single primary action shows up in hierarchy, affordance and isolation; one screen serving
several goals shows up in density, choice count and hierarchy. Fix the cause once instead of patching each symptom. For
every simplification, ask where the removed complexity goes (support queue, error rate, a later step) [teslers-law].

### 7. Prioritize
P1 = severity 3-4 (blocks the task, hides a required action, fails a contrast or target minimum, breaks brand
compliance, or leaks conversion on the main path; fix before shipping); P2 = severity 2; P3 = severity 1. Inside a level,
order by task frequency times position on the main path, and tag effort S/M/L [critique-screen command, heuristic-evaluation].

### 8. Improve
- Give each P1 and P2 a concrete fix, then check it against the neighbouring laws before proposing it: a bigger CTA
  [fitts-law] must stay the only isolated element [von-restorff-effect]; hiding options [hicks-law] must not hide what
  frequent users need [teslers-law]; a new pattern must beat the convention it replaces [jakobs-law]; added motion must
  stay inside the response ladder [doherty-threshold].
- When a fix has real alternatives that change what the user does (sequence, unit of interaction, who decides, entry
  point, commitment point), draft 2-3 such options at matched fidelity [parallel-concepts] and choose against criteria
  written down before comparing them [concept-selection]. Options that differ only in looks are one option; a deliberately
  weak option is a strawman and corrupts the choice.
- Present the way the user approves: a review page with one card per change, current screenshot and proposed mock side by side,
  the reason in plain words, a pick and a note box (House rules; built-ins `artifact-design` and `artifact-capabilities`).
  Build only from their picks; the build goes to ui-studio, agent wording to the agent's own change path.

### 9. Verify
Re-render the changed screen in the same states, re-run the same lenses, and report before/after per finding (fixed,
partly, not). If the open question is behavioural (can people find it, do they finish), say so and plan the study
(Research path) or an A/B test (conversion-lab) instead of claiming success. Conversations: text-simulate the changed path,
then read the first real transcripts after the user applies the change.

**Report format:** (1) a one-paragraph verdict: what works, the biggest risk, the strongest and weakest lens; (2) the fix
list P1 -> P3 as Issue / Lens / Law or heuristic / Fix / Severity / Effort; (3) the lens rating table; (4) what needs a test
rather than an opinion; (5) strengths to keep: the things the next round must not change, which is signal, not flattery
[design-critique]. A critique recommends, it doesn't redesign or slip in new features, and it is feedback, not sign-off:
state approval only when asked [design-critique].

### Design-a-pattern path (new form, navigation, search, flow)
1. **Start from convention.** How do 3-5 comparable products and the platform do this? Name the convention before
   departing from it; a departure needs a stated reason and a test [jakobs-law].
2. **Decide who carries the complexity.** Ask only what only the user knows; formats, detection and defaults belong to the
   product [teslers-law].
3. **Cut simultaneous choices** by grouping, defaults and progressive disclosure, one decision per step in setup flows
   [hicks-law, millers-law].
4. **Model the states** (states, events, guards, impossible states, a way out of each) and map each state to a screen
   [state-machine].
5. **Per state, specify** feedback and waiting (response ladder), errors (prevent, detect, communicate, recover) and each
   micro-interaction (template) loading-states, error-handling-ux, micro-interaction-spec].
6. **Place and order:** targets [fitts-law], grouping [law-of-proximity and the Gestalt members], order (key value moments
   first or last, required-but-tedious steps in the middle, resolution last) [serial-position-effect], the peak and the end
   [peak-end-rule].
7. **Wireframe with annotations** (priorities, states, breakpoints) [wireframe-spec], drawn as lo-fi SVGs when the user needs
   to see the layout [wireframe], then run loop steps 3-9 on the wireframe before ui-studio styles it.

### Conversational path (voice agents, SMS agents, chat)
1. **Pick the medium honestly.** Conversation suits open, ambiguous or multi-step tasks; many required fields or parallel
   choices suit a form or a link [conversational-ux].
2. **Map turns:** system prompt, user response, acknowledgement plus next prompt. One thing per prompt; the expected kind of
   answer is clear; the question comes last, never buried mid-sentence.
3. **Unhappy path first.** Handle the four error types: no input (re-prompt shorter), no match (clarify, offer constrained
   choices), out of scope (acknowledge and redirect without pretending to understand), partial match (confirm what was
   understood, ask only for the missing piece). Reprompt ladder: 1 rephrase with a little more context, 2 constrained
   choices ("morning, afternoon or evening"), 3 a graceful exit. Every reprompt adds information; never repeat one.
4. **Confirm by stakes:** explicit for high-stakes or easily confused items (spelled names, date of birth, amounts,
   appointment day, time and time zone), implicit for low-stakes recoverable ones, none where misrecognition is rare.
5. **Write for the ear:** short sentences, active voice, no visual references ("click below"), acronyms spelled out on first
   use, at most three options in one turn, numbers read in chunks [conversational-ux, millers-law].
6. **Pace by the response ladder:** a silence over about 1 s before the agent answers is a wait the caller notices; before a
   slow lookup, acknowledge first, in varied words [doherty-threshold]. After a misunderstanding, leave a beat before the
   next prompt [interfaces-that-feel].
7. **Persona holds under failure:** same register when things break; the agent never claims to be human when sincerely asked.
8. **Exits:** the caller can always stop, restart or get help. On the user's SMS agent the exit is an apology plus the
   customer-service number from the prompt, never a hand-off (House rules).
9. **Peak and end of the call:** end on a clear next step (booked time, what happens next), never on an error or an
   administrative line [peak-end-rule].
10. **Read real transcripts.** The gap between expected and actual user phrasing is the design backlog [conversational-ux].
    Changes go through the agent platform's own change path, the review page and a text simulation; the user applies.

### Research path (questions people must answer)
1. **Write the decision first:** what will this study settle? A study that answers no question is a portfolio
   [parallel-concepts, prototype-strategy].
2. **Cheapest method that answers it:** heuristic evaluation (no users), first-click or five-second test (findability,
   first impression), task-based usability test (can they finish), A/B test on live traffic (which converts: conversion-lab).
3. **Prototype at the question's fidelity:** paper or low-fi for flow and IA; clickable mid-fi for navigation and interaction;
   high-fi or coded for visual design and micro-interactions; Wizard of Oz (real front end, faked back end) suits
   conversational agents; video for concept pitches. Prototype the riskiest assumption first, make it obviously a
   prototype, build to throw away [prototype-strategy]; the build itself goes to think-and-decide.
4. **Write the tasks:** realistic context, a goal not instructions, the participant's words, no UI terms that reveal the
   path, one goal per task, a warm-up first, easy to hard, more tasks than needed, a pilot run; success = completion, time,
   errors and wrong paths, assistance asks, difficulty 1-5; an observation guide for hesitation and comments
   [test-scenario]. Click tests: target areas fixed before testing, one task per screen, real content not lorem ipsum,
   20-50 participants, first-click success of 65 % or more means good findability, plus time to first click and confidence
   [click-test-plan].
5. **Who runs it:** Claude writes the plan and analyses results; people run the sessions. Simulated "AI users" are not
   evidence and are labelled expert judgment. Paid panels and tools ask the user first.
6. **Converge:** criteria fixed before comparing (each able to fail a concept), marked threshold or trade-off; evidence over
   volume; name what the winner costs; a split set is a priority question for the user, not a reason to average; never graft
   losers onto the winner; the incumbent is judged too; record per rejected concept what it tested, what it lost on, what
   would revive it [concept-selection].

## Core rules and checklists

### Law finder (symptom -> law -> fix)
| Symptom | Law | Fix direction | Member |
|---|---|---|---|
| Mis-taps, tiny or distant targets, CTA out of thumb reach | Fitts | Bigger and closer targets via padding; action on the thing it acts on; bottom on mobile, screen edges on desktop | fitts-law |
| Users stall on a screen full of options | Hick | Fewer simultaneous, more distinct choices; group, default, disclose progressively | hicks-law |
| Users forget options or info between steps; long flat lists | Miller | Chunk into about 4 meaningful groups; structure first, count second | millers-law |
| Users hunt for something the team calls obvious; novel pattern | Jakob | Follow the convention of 3-5 comparable products unless a stated reason and a test say otherwise | jakobs-law |
| Feels laggy, spinners flash, flow breaks | Doherty | Acknowledge within 100 ms, aim under 400 ms, response ladder, optimistic UI | doherty-threshold |
| Users do the system's work (formats, re-entry, decoding errors), or experts hunt for hidden settings | Tesler | Product absorbs extraneous complexity; smart defaults with the option still reachable | teslers-law |
| Flow works but is remembered badly; ends on an admin screen or an error | Peak-End | Design the peak and the end; make recovery the new peak | peak-end-rule |
| Important item ignored in the middle of a list or menu | Serial position | Critical items first or last; isolate a middle item that cannot move; repeat key items in a closing summary | serial-position-effect |
| One thing must stand out but doesn't, or everything is highlighted | Von Restorff | One isolated element per view, surrounded by consistent peers, coded by more than colour | von-restorff-effect |
| Multi-step tasks abandoned and never resumed | Zeigarnik | Autosave, show progress and the exact resume point, 1-2 open loops at most | zeigarnik-effect |
| Label floats between fields, groups misread | Proximity | Within-group space smaller than between-group space, from one scale | law-of-proximity |
| Grouping lost in a tight layout; the group must act as a unit | Common region | Weakest container that works: background, then border, then card; nest 2 levels at most | law-of-common-region |
| Same-role things look different, or different things look the same | Similarity | One visual vocabulary per role (tokens); unintended differences are bugs; redundant coding | law-of-similarity |
| Boxed-in, heavy look; borders everywhere | Closure | Remove borders until grouping breaks; single-edge rules; alignment implies the grid | law-of-closure |
| Eye jumps; sequence unclear; ragged edges | Continuity | One alignment axis; connecting lines for sequences; deliberate breaks for new sections | law-of-continuity |
| Overlay, modal, text on photo or active item ambiguous | Figure-ground | Scrim, surface stack in tokens, overlay behind text on images, unmistakable selected state | law-of-figure-ground |
| Works but tests as untrustworthy; rough error or empty screens | Aesthetic-usability | Consistency first; give error, empty and loading states equal care; polish never hides a usability problem | aesthetic-usability |

### Numbers that matter (merged)
- **Targets:** touch 44x44 pt (Apple) / 48x48 dp (Material), pointer 24x24 px minimum; hit area grows with padding, not icon size [fitts-law, critique-affordance].
- **Response ladder** [doherty-threshold + loading-states, conflict resolved below]:

| Wait | Show |
|---|---|
| 0-100 ms | Only the pressed or changed state on the element; every action gets this |
| 100-400 ms | Still only the acknowledgement; no spinner (a flashed spinner is itself disruptive) |
| 400 ms-1 s | Skeleton for a known layout, small inline spinner otherwise |
| 1-3 s | Clear loading state, layout held steady |
| 3-10 s | Determinate progress where measurable |
| over 10 s | Progress, a time estimate, cancel or "keep working in the background"; users switch context here |

  Optimistic UI when success is very likely and reversible, with a visible rollback on failure. Autocomplete shows first
  suggestions within 300 ms. A new view renders its layout shell at once; never a blank screen.
- **Motion** [animation-principles, micro-interaction-spec, interfaces-that-feel]: press and toggle feedback 50-100 ms;
  tooltips, fades, small moves 150-250 ms; modals and page transitions 250-400 ms; a choreographed sequence under 700 ms
  total with 30-50 ms stagger; 400-600 ms only for a meaning-carrying moment that does not block input. Ease-out entering,
  ease-in exiting, ease-in-out moving, linear only for continuous progress. Interruptible; `prefers-reduced-motion`
  honoured; animate transform and opacity, `will-change` only on the element about to move. Intentional motion is not a
  wait: a deliberate 250 ms entrance does not count against the response ladder [doherty-threshold].
- **Choice and memory:** chunks of about 4 plus or minus 1 (Cowan), not "7 items" [millers-law]; 3 pricing tiers with 3-5
  bullets each [hicks-law, millers-law]; at most 1-2 open loops on screen [zeigarnik-effect].
- **Navigation:** mobile tab bar 3-5 destinations; desktop top nav 4-7; more than 7 top-level items means fix the IA first;
  segmented control 2-4 views; positions 3-5 of 7 are the memory valley [navigation-patterns, serial-position-effect].
- **Inputs:** radio buttons for up to 5 options, select or combobox for 6+ [form-design]; autocomplete after 2-3 characters,
  5-8 suggestions [search-ux].
- **Gestures:** 10-15 px movement before a gesture activates; tap vs long-press split at about 500 ms [gesture-patterns].
- **Feedback timing:** toasts auto-dismiss after 3-5 s; errors persist until resolved; status persists while relevant; leave 300-600 ms after an error before the next prompt [interfaces-that-feel].
- **Type and colour:** see lenses A3 and A4 (body 16 px, line-height 1.4-1.6, measure 45-75, contrast 4.5:1 and 3:1).
- **Research:** heuristic evaluators 3-5 for full coverage; severity 0-4; click tests 20-50 participants, first-click
  success 65 %+ [heuristic-evaluation, click-test-plan].

### Forms checklist [form-design, error-handling-ux, teslers-law, hicks-law, millers-law, fitts-law, zeigarnik-effect]
- One column; field width hints at expected length; persistent top-aligned labels (placeholder is never the label);
  helper text under the label, above the field; mark the optional fields, not the required ones; character counts always
  visible when a limit exists.
- Every field earns its place: remove what you can, ask only what only the user knows, accept any reasonable format
  (dates, phone numbers, pasted spaces) and detect what can be detected (country, region, card type).
- Input type matches the data: radios (all visible) for up to 5 options, select for 6+, checkboxes for multi-select,
  a date picker or day/month/year segments for dates (never free text), masked inputs for phone and card, show/hide on
  passwords.
- Validate on blur the first time; once a field is in error, re-check as the user types so the error clears the moment it
  is fixed. Error text under the field says what is wrong and how to fix it ("Email needs an @"). With 2+ errors or a
  server-side failure, add a focusable summary at the top that links to each field. Never clear input on error. A success
  tick only where correctness is not obvious (username free, password strength).
- Defaults: the most common answer for neutral preferences; never a pre-ticked consent, marketing or SMS opt-in, or paid
  add-on.
- Long forms: sections that each feel completable [millers-law]; multi-step with named steps, back without data loss,
  autosave or "save and continue", confirm before discarding, and a review step before submitting anything high-stakes
  (payments, legal, medical, lending).
- Submit: a specific verb label, full width below the last field on mobile, in the reading path on desktop.
- Accessibility: programmatic labels (`<label for>` or `aria-label`), errors tied with `aria-describedby`, focus order
  equals visual order, no colour-only required or error states.
- Measure field-level abandonment; it shows where to work. Test with real data, not tidy samples.

### Navigation choice [navigation-patterns]
| Situation | Pattern |
|---|---|
| Mobile, 3-5 primary destinations | Bottom tab bar, icon plus label, always visible |
| Desktop app with many or nested destinations | Side navigation |
| Simple marketing site or docs | Top nav bar |
| Deep content hierarchy | Breadcrumbs plus a local sidebar |
| Parallel views of the same content | Tabs or a segmented control |
| Occasional, non-primary access (account, settings, help) | Utility nav, top right on desktop, or an overflow menu |

Design navigation before screens; navigation errors compound. Test it with tasks that cross sections.

### Search checklist [search-ux]
- Input: placeholder says what can be searched; width invites the expected query length; autofocus when search opens;
  Enter submits plus a visible button for touch; a clear button once text exists; the query persists for refining.
- Suggestions: recent, then popular, then predicted; the typed part highlighted; keyboard navigable; include navigational
  destinations ("settings", "invoices") and put exact-match pages on top.
- Results: a count; the query highlighted in title and snippet; the metadata needed to decide (date, price, status);
  list, grid for visual items, or grouped by type; sort shown and changeable.
- Filters: only those relevant to the current results, with counts, each removable, plus "clear all".
- Zero results: echo the query, suggest a spelling fix and broader terms, offer browse, popular items or contact; never a
  blank page. Tolerate typos, synonyms, plurals and partial matches.
- Log top queries, zero-result queries, refinement rate, click position and abandonment; they are the most honest user
  feedback the product has.

### Feedback, gestures, micro-interactions, state machines
- **Feedback**: acknowledge every action; match intensity to importance; do not interrupt flow for
  minor confirmations; reversible actions get undo instead of "Are you sure?"; channels visual, text, audio, haptic, never
  colour alone.
- **Gestures** [gesture-patterns]: a visible affordance and first-use hint for each; always a non-gesture alternative (also
  for switch and voice control); feedback when the gesture starts, progress during, snap points or rubber-banding at
  thresholds; direction lock to separate scroll from swipe; return to start cancels; system gestures (back swipe,
  notification pull) win; one or two fingers; no precision timing; undo for destructive swipes.
- **Micro-interaction spec** [micro-interaction-spec]: name; trigger (user action, system event or condition); rules (logic,
  sequence, branches); feedback (visual, motion, audio, haptic); duration and easing; loops and modes (first time vs
  repeat, change over time); accessibility (reduced motion, non-visual equivalent).
- **State machine** [state-machine]: list states, events, transitions, side-effect actions and guards; name the impossible
  states to prevent (never loading and error at once); entry and exit actions per state; every state has a way out; one
  machine per concern; map each state to its UI. Common shapes: form (idle, editing, validating, submitting, success or
  error), fetch (idle, loading, success, error, retrying), wizard (steps, review, submitting, complete).

### Lo-fi wireframes [wireframe]
- Purpose: show structure (what goes where, in what order, roughly how big) without colour, brand or polish. Ask one scope
  question at most (which screens, which viewport), then go with the likeliest default and state it.
- House style, fixed: stroke `#000` at 1.5; boxes `#fff`; placeholder regions `#e6e6e6`; text `#000`, placeholder text `#666`;
  red dashed `#d33` only on an annotation layer, never inside the UI; one system font; type sizes 12 / 14 / 20 / 28 only;
  every x, y, w, h a multiple of 8, 24 px gutter. Canvases: 1280x800 desktop, 375x812 mobile, 768x1024 tablet.
- Build from the primitives in `members/wireframe/references/components.md` (copy and adjust; don't re-derive) or start from
  the closest worked example. Gotchas: `stroke="none"` and an explicit `fill="#000"` on every `<text>`, or it gets a halo.
- Deliver: the SVG file at a stated path (`wireframes/<screen>.svg`), the numbered annotation list mapping each region to its
  purpose, the assumptions made (viewport, signed-in, empty or populated); one SVG per screen plus a `flow.svg` of thumbnails
  with arrows for multi-screen flows.
- A page of all screens: one static `index.html` from `assets/site-template.html` (sticky contents, screen beside its notes
  and a "why this changes" callout, click-to-zoom, open questions at the bottom); check it at 1440, 768 and 390 px wide.
- Not for production UI, hi-fi or branded mockups (ui-studio), architecture or data diagrams (Mermaid), or art.

## When members disagree

| Between | Issue | Resolution |
|---|---|---|
| design-critique must / should / nice-to-fix vs severity 0-4 and P1-P3 | Three priority scales | Must-fix (blocks ship) = P1, should-fix (before wider rollout) = P2, nice-to-fix = P3; severity per finding stays 0-4. |
| wireframe "publish with the here-now skill" vs the user's security and publishing rules | Hosting the wireframe page | Don't install here-now (`npx skills add`) or post to a public anonymous host. Keep the files local or publish a private Artifact page; anything public asks the user first. |
| wireframe-spec vs wireframe | Spec document vs drawn SVG | SVG when the user or a reviewer must see the layout; the spec when engineering needs content rules, states and breakpoints; a big screen gets both, the spec's numbers matching the SVG's callouts. |
| loading-states vs doherty-threshold | Subtle indicator from 100 ms vs never a loading state under 400 ms | The response ladder: acknowledge on the element from 0 ms, no spinner or skeleton for in-place actions until 400 ms; a new view still renders its layout shell at once ("never a blank screen"). |
| animation-principles, micro-interaction-spec vs interfaces-that-feel | Keep motion under 400 ms vs 400-600 ms for meaningful transitions | Anything that blocks the next action stays at or under 400 ms; 400-700 ms only for rare meaning-carrying moments that never block input and can be interrupted. |
| form-design vs error-handling-ux | Validate on blur vs real-time validation | On blur first; live re-validation only once a field is already in error, so errors clear as soon as they are fixed. |
| form-design vs error-handling-ux | Errors under the field vs a summary at the top | Always under the field; add a focusable, linked summary at the top when 2+ fields fail or the server rejects the submit. |
| feedback-patterns vs error-handling-ux | Undo instead of "Are you sure?" vs confirmation dialogs for destructive actions | Reversible: act at once and offer undo. Irreversible or costly (deleting data, sending to customers, payments): confirm with a label naming the consequence ("Delete 12 contacts"); in voice, explicit confirmation. |
| fitts-law vs critique-affordance | Destructive actions small and far vs 44 px minimum targets | Keep the full minimum target; protect with distance, quieter weight and a confirm or undo step. The confirm button after an intentional step can be large. |
| form-design vs the user's consent and compliance needs | "Default to the most common answer" | Defaults only for neutral preferences; never pre-tick consent, marketing or SMS opt-ins, or anything that costs money (also conversion-lab's ethics gate). |
| jakobs-law vs navigation-patterns | Hamburger is an established convention vs it hides navigation | Fine on mobile web for secondary or many destinations; mobile apps put 3-5 primary destinations in a tab bar; never hide primary navigation on desktop. |
| serial-position-effect vs von-restorff-effect and common pricing practice | Never put the featured item in the middle vs highlight the recommended (often middle) tier | A featured middle tier is acceptable only when strongly isolated (badge, fill, elevation); otherwise place it first or last. If the choice matters to revenue, A/B test it through conversion-lab. |
| hicks-law vs teslers-law | Hide options to speed decisions vs over-hiding moves complexity onto users | Disclose progressively only what most users rarely need; frequent tasks stay visible; after simplifying, check error rate, time-on-task and support volume for where the complexity went. |
| jakobs-law vs interfaces-that-feel, aesthetic-usability | Stay conventional vs make it feel distinctive | Structure and high-frequency interactions stay conventional; warmth lives in copy, timing, motion and the peak and end moments. |
| critique-typography vs critique-visual-hierarchy | 1.25x vs 1.5x size ratios | 1.25x is the minimum between adjacent scale steps; 1.5x between levels that must read as different (title vs body). |
| critique-affordance vs fitts-law, form-design | Form CTA bottom-right vs full-width below the last field | Mobile: full width below the last field. Desktop: in the reading path at the end of the form column; dialogs follow the platform's button order. Consistent within a product. |
| critique ratings vs heuristic-evaluation vs critique commands | pass / minor / major vs severity 0-4 vs P1-P3 | Lens ratings for the summary, severity 0-4 per finding, priority from severity (P1 = 3-4, P2 = 2, P3 = 1). |
| heuristic-evaluation vs the user's cost rules | 3-5 independent evaluators vs no needless subagents | Default: independent passes in this context (new user, expert, per task). Fresh-context reviewers (2-3 subagents given only the screenshots and scope, not your findings) only for launch-critical screens or flows, announced first. |
| conversational-ux vs the user's SMS rule | Third error -> offer a live agent vs the SMS agent never hands off | SMS agent: apology plus the customer-service number from the prompt. Voice agents: only the transfer or callback the flow already has. Never promise a call-back that nobody works. |
| conversational-ux vs agent-prompt rules | Offer explicit example utterances vs the agent parrots example phrases | Constrained choices for the caller ("morning, afternoon or evening") are fine where the step is meant to be spoken; instruction text describes behaviour, never one sample line; if examples are needed, 3-4 varied ones in the global prompt. |
| conversational-ux vs doherty-threshold | Keep responses under 8 s vs flow breaks after 1 s | The 8 s figure is a smart-speaker guideline; on live calls a silence past about 1 s is dead air, so acknowledge before slow lookups. |
| critique-information-density vs the user's dashboards rule | Show the actionable metrics, not every metric vs redesigns never remove metrics | On the user's ops dashboards fix density with grouping, order, hierarchy and drill-down, never removal; dashboard-studio leads. |
| ux-lab critique vs ui-studio's design audit | Who leads a review | "Build or redesign this UI": ui-studio leads and ux-lab reviews. "Why is this confusing, critique it, test it": ux-lab leads and hands the build to ui-studio. |
| parallel-concepts vs think-and-decide prototype | Who makes the variants | ux-lab sets the question, the dimension the concepts differ on and the selection criteria; think-and-decide builds the throwaway variants. |

## Combine with
- **Super-skills:** ui-studio (builds and polishes the fixes; motion tokens; its own audit), web-a11y (WCAG depth),
  conversion-lab (A/B tests, onboarding and activation, pricing pages, form CRO), mobile-app-studio (iOS and Android
  conventions and gestures), dashboard-studio (charts and ops dashboards), copy-and-content (full copy rewrites),
  brand-studio (the brand files a Brand check reads), lifecycle-messaging (SMS and email sequences, re-engagement sends),
  think-and-decide (throwaway prototypes, council for contested calls), test-and-harden (Playwright flow tests, ops
  scenario suites).
- **Built-ins:** `artifact-design` and `artifact-capabilities` (the user's review page with picks), `artifact-diagramming` (flows
  and state diagrams; Mermaid renders natively), `run` or Playwright MCP (render screens and states), `humanizer` (copy
  that sounds like a person), `frontend-design:frontend-design` (when a fix needs visual direction), `superpowers:brainstorming`
  (before designing a new pattern), `superpowers:verification-before-completion` (step 9).
- **Agent prompts** (`~/.claude/skill-library/agents/voltagent/`, pass the file as the Agent prompt plus the scope):
  - `08-business-product/ux-researcher.md`: study design, interview and survey plans, synthesis of results.
  - `04-quality-security/ui-ux-tester.md`: flow-driven functional testing with browser tools and structured defect reports.
  - `01-core-development/ui-designer.md`: a second designer's read on visual and interaction fixes.
  - `05-data-ai/prompt-engineer.md`: prompt mechanics for voice and SMS agents after the conversational design is settled.
  - `04-quality-security/accessibility-tester.md`: assistive-technology checks beyond screen-level critique.
  - `04-quality-security/performance-engineer.md`: when the Doherty budget needs real latency work.

## House rules (the user)
- Every proposed change (screen fix, flow change, agent wording) goes on a review page: one card per change, old and new
  side by side, the reason in plain words, a pick and a note saved to the page; build only from their picks, and anything
  found mid-build gets its own card first.
- On the user's stores every critique asks "does this get more people to buy?"; back layout claims with
  conversion evidence (Baymard, NN/g, GoodUI, Shopify and web.dev data) and cut sections that only explain how shopping
  works.
- Static (scripted) voice-agent steps are spoken word for word: only the words the caller should hear, one sentence or question.
  Rules and "if they say X" go into prompt steps, edges or the global prompt; check the step type before editing.
- No single example phrase in an agent step; the agent parrots it. Don't rewrite the user's questionnaire or confirmation
  wording; propose changes and let the user decide.
- The SMS agent never hands off: upset or "real person" requests get an apology and the contact number from the
  prompt, never "someone will reach out".
- Ask the user first before paid research tools or panels, anything that sends, posts or publishes (re-engagement texts and
  emails included), and any edit to a live site or agent. No test calls; text simulations only, the user runs the apply.

## Members
| Member | Best at | Path |
|---|---|---|
| aesthetic-usability | Consistency as a trust signal; polish never masks usability problems | `members/aesthetic-usability/SKILL.md` |
| animation-principles | Easing, duration bands, stagger and choreography for one motion | `members/animation-principles/SKILL.md` |
| click-test-plan | First-click, click-path, navigation and five-second tests with success thresholds | `members/click-test-plan/SKILL.md` |
| concept-selection | Criteria before comparison, threshold vs trade-off, rejected-concept record | `members/concept-selection/SKILL.md` |
| conversational-ux | Turns, confirmation types, error reprompt ladder, voice writing, persona | `members/conversational-ux/SKILL.md` |
| critique-affordance | Clickability, state visibility, CTA clarity, action discoverability | `members/critique-affordance/SKILL.md` |
| critique-brand-consistency | Screen vs mood, voice and token files, with exact corrections | `members/critique-brand-consistency/SKILL.md` |
| critique-color | Contrast pairs with measured ratios, palette coherence, semantic colour | `members/critique-color/SKILL.md` |
| critique-composition | Balance, whitespace, rhythm and Gestalt on one screen | `members/critique-composition/SKILL.md` |
| critique-information-density | Cognitive load, content priority, scanning, progressive disclosure | `members/critique-information-density/SKILL.md` |
| critique-typography | Scale use, readability thresholds, consistency, type tokens | `members/critique-typography/SKILL.md` |
| critique-visual-hierarchy | Entry point, eye flow, weight and emphasis | `members/critique-visual-hierarchy/SKILL.md` |
| doherty-threshold | 400 ms flow threshold and the response-time perception table | `members/doherty-threshold/SKILL.md` |
| error-handling-ux | Prevent, detect, communicate, recover; error states by context | `members/error-handling-ux/SKILL.md` |
| feedback-patterns | Feedback types, hierarchy, channels, dismissal timing | `members/feedback-patterns/SKILL.md` |
| fitts-law | Target size and distance rules, touch minimums, edge targets | `members/fitts-law/SKILL.md` |
| form-design | Form layout, labels, input-type table, validation, multi-step, form a11y | `members/form-design/SKILL.md` |
| gesture-patterns | Core gestures, thresholds, conflict resolution, gesture a11y | `members/gesture-patterns/SKILL.md` |
| heuristic-evaluation | Nielsen's 10, evaluation process, severity 0-4 | `members/heuristic-evaluation/SKILL.md` |
| hicks-law | Choice count vs decision time; grouping and progressive disclosure | `members/hicks-law/SKILL.md` |
| interfaces-that-feel | Felt-state translation, emotional timing, copy voice by state | `members/interfaces-that-feel/SKILL.md` |
| jakobs-law | Where conventions are strongest, the cost of departing, when deviation is justified | `members/jakobs-law/SKILL.md` |
| law-of-closure | Implied boundaries, minimal icons, clipped-edge scroll cues | `members/law-of-closure/SKILL.md` |
| law-of-common-region | Containment grouping, weakest-container rule, nesting limit | `members/law-of-common-region/SKILL.md` |
| law-of-continuity | Alignment paths, sequences, deliberate breaks | `members/law-of-continuity/SKILL.md` |
| law-of-figure-ground | Surface stack, scrims, text on imagery, dark-mode depth | `members/law-of-figure-ground/SKILL.md` |
| law-of-proximity | Spacing ratios as the primary grouping tool, squint test | `members/law-of-proximity/SKILL.md` |
| law-of-similarity | Similarity vocabulary, unintended differences as bugs, redundant coding | `members/law-of-similarity/SKILL.md` |
| loading-states | Skeletons, spinners, progressive and optimistic loading, transitions | `members/loading-states/SKILL.md` |
| micro-interaction-spec | Trigger, rules, feedback, loops and modes spec format | `members/micro-interaction-spec/SKILL.md` |
| millers-law | Chunking (4 plus or minus 1), common misapplications of "7" | `members/millers-law/SKILL.md` |
| navigation-patterns | Global, local, utility and contextual nav; pattern choice; active states | `members/navigation-patterns/SKILL.md` |
| parallel-concepts | Behaviourally distinct concepts, sizing the set, matched fidelity | `members/parallel-concepts/SKILL.md` |
| peak-end-rule | Designing the peak and the end; duration neglect; recovery as peak | `members/peak-end-rule/SKILL.md` |
| prototype-strategy | Fidelity spectrum and method choice by question | `members/prototype-strategy/SKILL.md` |
| search-ux | Search input, autocomplete, results, filters, zero results, analytics | `members/search-ux/SKILL.md` |
| serial-position-effect | Primacy, recency and the middle valley in menus, lists and flows | `members/serial-position-effect/SKILL.md` |
| state-machine | States, events, guards, impossible states, common UI machines | `members/state-machine/SKILL.md` |
| teslers-law | Inherent vs extraneous complexity, who absorbs it, over-simplifying | `members/teslers-law/SKILL.md` |
| test-scenario | Realistic usability tasks, success criteria, observation guide | `members/test-scenario/SKILL.md` |
| user-flow-diagram | Flow notation, task vs user vs wire flows, annotation rules | `members/user-flow-diagram/SKILL.md` |
| von-restorff-effect | One isolated element per view; isolation inflation | `members/von-restorff-effect/SKILL.md` |
| wireframe-spec | Annotated wireframes: priorities, states, breakpoints, content specs | `members/wireframe-spec/SKILL.md` |
| zeigarnik-effect | Progress, resume and re-engagement without manipulation | `members/zeigarnik-effect/SKILL.md` |
| design-critique | Pre-critique context (who, job, success, place in flow), a nine-step product critique pass, must/should/nice output with strengths to keep | `members/design-critique/SKILL.md` |
| wireframe | Drawn monochrome SVG wireframes with a fixed house style, 8 px grid, primitive library, worked examples and a review viewer page | `members/wireframe/SKILL.md`, `references/components.md`, `references/examples.md`, `references/grid-system.md`, `assets/` |

If a member folder is missing (not installed), work from this file alone.
