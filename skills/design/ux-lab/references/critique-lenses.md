# Critique lenses (merged)

Built from the seven critique-* members, the eight Gestalt / perception members, the UX-law members, heuristic-evaluation
and the interaction-pattern members. Step 4 of the unified workflow in `../SKILL.md` runs these. For each lens: ask the
questions, measure what can be measured, write findings in the §D format, and rate the lens `pass` / `minor issue` /
`major issue`. Thresholds referenced as "Numbers" live in SKILL.md > Core rules > Numbers that matter.

## A. Visual lenses (one rendered screen, every state you captured)

### A1 Hierarchy [critique-visual-hierarchy, von-restorff-effect, serial-position-effect]
- **Entry point:** one dominant element, set by size, contrast or position, and it is the thing that serves the user's goal.
- **Eye flow:** F-pattern for text, lists and tables; Z-pattern for hero + CTA layouts; no dead ends, loops or jumps; the
  path ends at the primary action.
- **Weight:** at least 1.5x size difference between levels that must read as different; bold used sparingly so it keeps
  its signal; fills, strokes and icons support the order instead of fighting it.
- **Emphasis:** exactly one primary emphasis zone per view; it survives grayscale (colour plus size, weight or shape);
  the most emphasised element is the highest user and business priority.
- **Order:** critical items first or last in any list or menu; positions 3-5 of a 7-item menu are the serial-position
  valley, so anything important there needs isolation or a move.
- **Failures:** competing primaries; flattened levels; decoration outweighing function; CTA quieter than the content
  around it; "isolation inflation" (every feature asked for a highlight, so nothing stands out).

### A2 Composition and Gestalt [critique-composition, law-of-proximity, law-of-common-region, law-of-similarity, law-of-closure, law-of-continuity, law-of-figure-ground]
- **Balance:** weight spread on purpose (symmetric or asymmetric), a clear centre of gravity, nothing tipping the layout.
- **Whitespace:** generous macro space between sections, consistent micro space between labels, icons and neighbours;
  space guides attention without fragmenting the page.
- **Rhythm:** every interval from one spacing scale (4, 8, 16, 24, 32...); repeated items uniform in size and gap;
  dividers earn their place.
- **Proximity:** label closer to its input than to the next field; heading closer to its content than to the section
  above; within-group space smaller than between-group space (the ratio matters, not a pixel value). Squint: the groups
  must read without reading the words.
- **Common region:** the weakest container that does the job (background, then border, then card surface); nesting at
  most two levels; containers still visible in dark mode and low contrast; not every group needs a card.
- **Similarity:** elements with the same role look identical (radius, height, stroke, type); unintended differences are
  bugs because users read them as categories; all interactive elements share a property static ones lack; critical
  categories use redundant coding (shape plus colour).
- **Closure:** remove borders one at a time; if the group still reads, the border was noise; a clipped item at the edge
  signals horizontal scroll; icons still close at 16-20 px.
- **Continuity:** one shared left edge per column; single-pixel misalignments break the path (check every breakpoint);
  sequences (steps, timelines) get a connecting line; deliberate breaks (bigger gap, divider, indent) announce a new
  section or a sub-level.
- **Figure-ground:** modals get a scrim; the surface stack (base, raised, overlay, modal) has clear steps; text never sits
  straight on photography (overlay, blur or gradient); the selected item is unmistakable; re-check in dark mode, where
  shadows vanish (use light borders or lighter fills).
- **Failures:** equal-weight two-column layout with no primary; padding of 16, 20 and 24 px with no system; orphaned
  elements; a crowded section next to an empty one; dividers multiplying; cards inside cards with no luminance step.

### A3 Typography [critique-typography]
- **Scale:** only defined steps, each used for its role, at least 1.25x between adjacent steps.
- **Readability:** body 16 px by default (14 px is the floor, for secondary text only; inputs stay at 16 px or more so
  iOS Safari does not zoom); line-height 1.1-1.3 for headings, 1.4-1.6 for body; measure 45-75 characters; tracking
  neither stretched nor crushed; contrast per A4.
- **Consistency:** equivalent elements share one style; alignment chosen, not mixed (no centred headings over left-aligned
  body without a reason); no more than two weight levels on a screen; no one-off orphan styles.
- **Tokens:** family, size, weight, line-height and tracking come from tokens; list each raw value with its token.
- **Failures:** 1-2 px scale drift; display sizes with body line-height; alignment mixing; hard-coded sizes; bold everywhere.

### A4 Colour [critique-color]
- **Contrast:** body text 4.5:1; large text 3:1, where WCAG "large" means 24 px regular or about 18.7 px bold (the member's
  "18 px / 14 px bold" mixes up points and pixels); buttons, inputs and focus rings 3:1 against adjacent surfaces. Report
  every failing pair with its measured ratio and the minimum. Placeholder and disabled text people must read count too.
- **Palette:** only token colours; neutrals, primaries and accents in their roles; no vibrating neighbours; the warm, cool
  or neutral register fits the context.
- **Semantic use:** colour is never the only signal of state (add an icon, label or pattern); status colours consistent
  (red error, green success, amber warning); interactive colour distinct from decorative colour.
- **Vision:** deuteranopia and protanopia simulation, forced-colours mode, grayscale.
- **Failures:** link colour under 4.5:1 once the underline is removed; red-only errors; 40 %-opacity placeholders; one-off
  hex values; interactive and static elements sharing a colour. Full WCAG audit: web-a11y.

### A5 Brand [critique-brand-consistency]
- **Sources:** mood (DESIGN.md or the brand guidelines from brand-studio), voice (brand voice doc), tokens (token file,
  Tailwind theme). A missing source means you skip that dimension and say so; never invent brand rules.
- **Mood:** imagery, illustration, icons and colour feel match the personality keywords; nothing tonally off.
- **Voice:** tone, banned and required words; CTAs, labels, errors and microcopy all in voice.
- **Tokens:** list every hard-coded colour, spacing, radius, shadow and type value with its token equivalent.
- **Failures:** values drifting from tokens; generic UI copy; off-brand imagery; mixed radii or shadows on one screen.

### A6 Affordance [critique-affordance, fitts-law, gesture-patterns]
- **Clickability:** interactive things look interactive (colour, shape, underline, elevation); no false affordances
  (static things that look clickable), no missing ones (clickable things that look static).
- **Targets:** at least 44x44 pt (iOS) / 48x48 dp (Android) for touch and 24x24 px for pointer, grown with padding rather
  than visual size; actions sit next to the content they act on.
- **States:** default, hover, active, focus, disabled and selected all distinct; focus visible and high-contrast (never
  `outline: none` without a replacement); disabled not shown by colour alone; loading or skeleton where content is async.
- **CTA:** one filled primary per view, secondaries ghost or text; a specific verb label ("Save changes", not "OK");
  placed at the end of the content it completes, in the reading path (mobile: full width below the last field, in thumb
  reach).
- **Discoverability:** nothing essential lives only on hover (touch has no hover); contextual actions visible or hinted;
  every gesture has a visible hint and a button alternative; empty states say what to do next; destructive actions look
  different and sit apart from constructive ones.
- **Failures:** ghost buttons whose border disappears on low contrast; several filled CTAs; edit and delete only on hover;
  empty states with no way forward.

### A7 Density [critique-information-density, hicks-law, millers-law, teslers-law]
- **Cognitive load:** count the decisions and items the primary task needs; one user goal per screen; cut what does not
  serve the current task.
- **Priority:** what the user acts on is above the fold and visually first; supporting context is subordinate; nothing
  critical is buried in a tooltip, collapsed section or low-contrast text.
- **Scanning:** left-aligned labels; numbers, dates and statuses aligned and formatted alike; short chunks, headers, bullets.
- **Progressive disclosure:** detail deferred to detail views; expanders, tabs and modals hide secondary content, never the
  primary action; advanced options separated; one obvious starting point.
- **Chunking:** groups of about 4 (plus or minus 1); long forms split into sections that each feel completable; codes and
  phone numbers formatted in chunks.
- **Failures:** every metric shown instead of the actionable ones (on the user's ops dashboards fix this with grouping, order and
  drill-down, never by removing metrics); detail pages that inline every related object; 10+ column tables where 3 columns
  do 90 % of the work; all-at-once long forms; onboarding that explains before the user has done anything.

## B. Interaction lenses (flows, states, behaviour)

### B1 Status and waiting [doherty-threshold, loading-states]
- Every action is acknowledged on the element itself within 100 ms, whatever the backend is doing.
- Waits follow the response ladder (Numbers); no spinner flashes under 400 ms; skeletons match the real layout; no layout
  shift when content lands; scroll position kept on refresh; one loading indicator at a time; cancel or back on long loads.
- System status is visible: progress, badges (pending, active, complete), syncing and typing indicators.
- Feedback sits as close to the action as possible: inline, then component, then page, then system.

### B2 Errors [error-handling-ux, form-design, interfaces-that-feel, search-ux]
- **Prevent:** constrained inputs (pickers, masks, dropdowns), smart defaults, inline validation, autosave, undo or confirm
  for destructive acts.
- **Detect:** field validation, form-level validation on submit, network and timeout handling, permission and session checks.
- **Communicate:** what happened, why (when it helps), what to do now; human words, no codes; next to the source; severity
  matched (error, warning, info); never blame the user; a system failure is owned with a brief apology and a way forward.
- **Recover:** input preserved; retry for transient failures, auto-retry with backoff for network; an alternative path; undo.
  After an error, leave 300-600 ms before the next prompt or motion so recovery is not rushed.
- **By context:** forms (inline per field, plus a focusable summary when 2+ fields fail), pages (full-page state with retry
  and back), network (toast or banner with retry), empty results (suggestions, alternatives), permissions (what access is
  needed and how to get it).
- **Failures:** "Something went wrong"; cleared forms; red-only messages; errors that only appear at the top of a long form.

### B3 Forms and input
Use the Forms checklist in SKILL.md > Core rules (merged from form-design, error-handling-ux, teslers-law, hicks-law,
millers-law, fitts-law, zeigarnik-effect).

### B4 Navigation and wayfinding [navigation-patterns, jakobs-law, serial-position-effect, search-ux]
- **Where am I:** active state shown by more than colour (weight, underline, indicator bar), page title, breadcrumbs in deep
  hierarchies.
- **Where can I go:** labels with scent, in the users' words, never internal product names; destinations predictable before
  the click.
- **How do I get back:** logo returns home; back keeps state; every state has a way out.
- **Fit:** the pattern matches the structure (Navigation table in SKILL.md); placement and structure identical across
  screens; global and local navigation never share one component; primary navigation never hidden behind a hamburger on
  desktop; primary destinations in thumb reach on mobile.
- **Retrieval:** search present wherever users retrieve rather than browse (on mobile it is often the main navigation);
  zero-results state designed.

### B5 Conventions and consistency [jakobs-law, law-of-similarity, aesthetic-usability]
- Universal conventions hold: logo top-left goes home, cart icon goes to checkout, magnifier means search, X closes,
  underlined text is a link.
- Every departure is named and justified: the convention fails a real need, the domain has its own convention, a test
  showed the convention performs worse, or no convention exists yet. Differentiation and taste are not reasons.
- Internal consistency: same component, same look, same behaviour everywhere; error, empty and loading states designed with
  the same care as the main screens, because one rough screen lowers trust in the screens around it.

### B6 Motion and micro-interactions [animation-principles, micro-interaction-spec, gesture-patterns]
- Every animation communicates something (state change, attention, spatial relation); durations and easing per Numbers;
  interruptible; reduced-motion honoured; animate transform and opacity.
- Related elements move in one choreographed sequence with one direction, leading with the most important element.
- Gestures: activation threshold, direction lock, cancel zone, feedback during the gesture, a non-gesture alternative.

### B7 Emotion and memory [interfaces-that-feel, peak-end-rule, zeigarnik-effect, aesthetic-usability]
- The felt state is named for each key moment; copy matches it: loading present and calm ("Getting your data", not
  "Loading..."), empty invitational, user error directive and blame-free with one next step, system error owns it, success
  warm and brief, onboarding about what they can do rather than how the app works.
- Peak and end are designed: the completion moment is satisfying and named; the flow never ends on an administrative or
  transition screen or an error; if the peak is negative (long wait, failure), the recovery is designed to become the peak.
- Open loops are honest: progress and the exact resume point shown, one or two at a time, always with a path to finish;
  autosave comes first.
- Strip colour and imagery: does the emotional signal survive in copy and timing alone?

## C. Nielsen coverage check [heuristic-evaluation]
Tag every finding with one heuristic. Before finishing, give any heuristic with zero findings one deliberate look.

| # | Heuristic | Look at | Lenses / laws |
|---|---|---|---|
| 1 | Visibility of system status | acknowledgement, progress, saved state | B1, Doherty |
| 2 | Match between system and real world | users' words and order, no jargon or internal names | A5 voice, B4 |
| 3 | User control and freedom | undo, cancel, back, exit from every state | B2, state machine |
| 4 | Consistency and standards | category and platform conventions, internal similarity | B5, Jakob, Similarity |
| 5 | Error prevention | constraints, defaults, confirm or undo | B2, Tesler |
| 6 | Recognition rather than recall | options visible, context carried between steps | A7, Miller, Serial position |
| 7 | Flexibility and efficiency of use | shortcuts, smart defaults, expert paths | Hick, Tesler |
| 8 | Aesthetic and minimalist design | nothing irrelevant competing for attention | A1, A2, A7, Aesthetic-usability |
| 9 | Help users recognize, diagnose and recover from errors | message format, preserved input | B2 |
| 10 | Help and documentation | contextual help where needed, findable | B4 search |

## D. Finding format, severity, priority

| Field | Content |
|---|---|
| Lens | A1-A7 or B1-B7 |
| Observation | What is there, neutral and factual |
| Problem | What breaks for the user and why; the law or heuristic named as the cause |
| Fix | The specific change: value, token, copy, placement or pattern |
| Severity | 0 not a problem, 1 cosmetic, 2 minor, 3 major (fix before release), 4 catastrophe (blocks release) |
| Evidence | Screenshot crop, measured value (ratio, px, ms, step count), transcript line or metric |
| Confidence | Observed (data, recording, transcript) or expert judgment |
| Heuristic | Nielsen 1-10 |

Priority: **P1** = severity 3-4 (blocks the task, hides a required action, fails a contrast or target minimum, breaks brand
compliance, or leaks conversion on the main path; fix before shipping). **P2** = severity 2 (slows or confuses; next).
**P3** = severity 1 (polish). Inside a level, order by task frequency times position on the main path; tag effort S/M/L.

Lens rating table for the report: one row per lens run, rating, the one-line reason.
