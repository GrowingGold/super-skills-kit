# Impeccable inside ui-studio

impeccable (pbakaus, v4.8.2, Apache-2.0) is a full design skill: visitor modes, a craft floor, a new-work
direction process and 24 commands, each with its own reference in `members/impeccable/reference/`. Its
engine (`scripts/impeccable`: context, detect, concept-seed, serve-question, comp-spec, build-phase,
critique-storage, live, hooks) was deliberately not copied into this kit: the launcher downloads a
binary and the hooks run after every edit. This page says how to use the skill without it.

## Engine-less rules (from the note at the top of members/impeccable/SKILL.md; they win)

- Setup always takes the "launcher unavailable" path: say once that context loading did not run, then
  read PRODUCT.md and DESIGN.md (or the project's own design notes) directly. Never invent missing context.
- Any step that calls `scripts/impeccable <verb>` is skipped: do the same check by reading the code and
  looking at the rendered page (Playwright MCP screenshots), and name the skipped step in the report.
- Never turn on hooks or live mode, never download the engine, without the user's yes.
- the user's visual approval protocol wins over "finish the job": changes to a live or shared project become
  review cards (old vs new, reason) and only their picks get built.
- Questions go to the user in chat or on a review page; there is no AskUserQuestion decision page here.

## Command map

Open `members/impeccable/reference/<file>` for the command, apply the engine-less rules, and fold the
result into the ui-studio step named. Native platforms use the `.native.md` variants plus `ios.md` or
`android.md`.

| Command | Use it for | ui-studio step | Notes |
|---|---|---|---|
| `shape` | discovery brief, no code | 0-1 | 1-2 rounds of 2-3 product questions; returns a 3-7 part brief |
| `init` | PRODUCT.md (product truth: user, job, mechanism, constraints, platform, stack) | 0 | never writes DESIGN.md |
| `document` | DESIGN.md from existing code, official format (YAML tokens + 8 sections) | 2 | Spec handoff; conflict 32 |
| `extract` | pull repeated values and components (3+ uses) into the system | 2 | asks where the system lives first |
| `critique` | heuristic UX review with scores | 6 | self-check only; ux-lab leads real critiques (conflict 31) |
| `audit` | technical audit, 5 dimensions scored 0-4 | 6 | a11y depth goes to web-a11y |
| `polish` | final pass on a working feature | 5 | triage order below |
| `bolder` / `quieter` / `distill` | amplify, calm, simplify an existing design | 5 | Tune rules below |
| `colorize` | add strategic colour to a grey UI | 2 | strategies in scales-and-systems.md §1 |
| `typeset` | type hierarchy and fonts | 3 | also its Line breaks section |
| `layout` | spacing, rhythm, hierarchy, structure | 4 | squint test, spatial thesis |
| `animate` | purposeful motion | 5 | one focal moment |
| `delight` | personality at moments that earn it | 5 | one delight thesis; never on routine clicks |
| `overdrive` | push past convention (morphing dialogs, million-row tables) | 5 | propose 2-3 directions, the user picks before code |
| `clarify` | UX copy, labels, errors | Core rules: UI copy | one fact, next action, context, tone |
| `adapt` | other screen sizes, devices, print, email | 4 | rethinks, never just scales |
| `harden` | edge cases, i18n, errors, overflow | 6 | list below |
| `optimize` | UI performance | 4.9, 6 | measure before and after |
| `onboard` | first-run, empty states, activation | 4 | flows and activation strategy: conversion-lab |
| `live`, `generate`, `hooks`, `pin`, `doctor` | engine features | none | skipped (engine not installed) |

`craft` is a dead alias for ordinary new work; `teach` aliases `init`. With no command, behave as
general design work inside the ui-studio workflow.

## Visitor modes (step 0)

The mode names what success looks like for the visitor on this surface; choose it from the surface, not
the product (a tool's landing page is Persuade; a fashion brand's docs are Read).
- **Persuade:** landing, pricing, store, campaign. The first viewport makes the offer clear and desirable,
  shows the primary action in its working form (add to cart, open booking slots, a route search), and
  demonstrates something only this product can prove. The world may structure the page, but every part
  still works as a page: navigation reads as links, text is set text, the action is plainly clickable.
- **Operate:** app UI, dashboards, admin, settings, tools. A category-fluent user knows where everything
  is before noticing the style. The direction lends only type, palette, density and one signature move
  (e.g. service health drawn as a transit map); layout, navigation model and controls stay standard.
  Restrained colour is the floor; skeletons, not centre spinners; empty states that teach.
- **Read:** docs, articles, help, changelogs. The world owns the frame (masthead, rail, openers, how code
  and tables are set); the reading column stays calm at a real measure.
- **Experience:** portfolios, galleries, showcases. The work leads from the first viewport.

## New visual world, by hand (step 1)

Use when there is no brand system or the user asks for a replacement look. A section or feature inside an
existing site inherits that site; never turn a local addition into an identity exercise.
1. Decide what is already true: redesign (keep product truth, content and function, replace the look),
   established world (inherit and document it), incomplete brand (keep confirmed assets, extend), none.
2. Name the product's mechanism in one sentence, the audience's real scene, its cultural home, and what
   this first page must prove. Name the page this category always ships and its predictable opposite:
   both are the rut and stay off the list.
3. List seven concrete things the audience knows by heart (artifacts, places, publications, rituals,
   graphic and screen traditions), each with why it fits and how it looks (ground, main colours, type
   voices, one signature). On Operate and Read surfaces never draw from the tools the audience operates
   (a terminal or control panel becomes a costume). If more than three share one material family, dig
   until the list spans at least three. Ask what the thing would be as a physical object, and what its
   world looked like before the web.
4. Turn the best three into complete directions (world, first viewport, visitor path, signature
   interaction, honest risk) and put them on the user's review page with the category standard as a quiet
   fourth option. No dice engine: ties break with the node one-liner in style-directions.md.
5. Calibrate before building: if someone could guess the aesthetic from the category alone, rework. The
   AI default looks are listed in anti-slop.md (Calibration).
6. Record the pick as a direction contract in the plan (never in shipped code, comments or data
   attributes): THESIS (the idea this page owns and the default it refuses), OWN-WORLD (palette and
   component language, recognisable with content removed), STORY (what the visitor understands, believes,
   does), FIRST VIEWPORT (exact composition and where the action sits), FORM (chosen form, "pinned" or
   "picked by the user"), FINISH (reviewed and documented, or it is not finished).

## Tune: bolder, quieter, distill

- **Scope is sovereign:** touch only the named target; add no colour, font, radius, shadow or primitive
  the system does not already own without asking the user which addition and why [bolder].
- **Bolder** brings the flat part up to the strongest moves its neighbours already make, in the system's
  own vocabulary; one decisive move made completely, everything around it quieter. Reaching for more
  effects is the opposite of bold. Skeleton test: strip the copy; the structure alone should still say
  what the section is and why it matters.
- **Quieter** finds the intensity sources (saturation, contrast extremes, weight, motion, complexity,
  flat scale) and lowers them while keeping the point of view; quiet is not grey text on white plus
  identical cards. Persuade keeps drama, reduced; Operate removes noise.
- **Distill** finds the one goal, removes or hides what does not serve it (progressive disclosure),
  merges duplicates, and keeps features: simplicity removes obstacles, not capabilities.

## Polish triage [polish]

Fix in this order: broken or blocked tasks, data loss, misleading state, inaccessible paths; missing
loading, empty, error, success, disabled and permission states; flow, hierarchy, responsive and system
drift; visual and motion inconsistencies; code and asset cleanup (debug output, dead styles, duplicates).
Classify each drift: missing token, one-off implementation (a shared component exists), conceptual
mismatch (flow differs from neighbouring areas), local defect; fix at the narrowest correct level. Polish
never smuggles in a redesign: if the concept is wrong, say so and recommend redesign or bolder.

## Harden [harden]

Feed every list, card and form: very long and very short text, emoji, accents and RTL text, huge
numbers, 1000+ items and 50+ options, no data. Errors: offline, slow, timeout, 400/401/403/404/500,
validation, permission, rate limits, double submits. i18n: German runs about 30% longer, RTL (logical
properties: `margin-inline-start`, `inset-inline-*`; `left:50%` plus `translateX(-50%)` centring is
direction-agnostic and stays), CJK, date, number and currency formats. RTL style and product picks come
from ui-ux-pro-max with `--rtl` (`full` mirrors cleanly, `partial` needs per-component checks, `caveats`
encodes reading direction: say so first). Chat and search inputs follow the IME-safe Enter rule
(ui-ux-pro-max guideline 120). Touch drags need `touch-action`, cancel handling and no stuck state.

## Audit scoring [audit]

Five dimensions, each 0-4: accessibility, performance, theming (tokens, dark mode), responsive (fixed
widths, targets, touch gestures, overflow, text scaling, RTL), implementation integrity (repeated
shortcuts, system drift, decorative content, structure interchangeable with an unrelated product; start
the report with this verdict). Total /20: 18-20 excellent, 14-17 good, 10-13 acceptable, 6-9 poor, 0-5
critical. Findings carry P0-P3 severity. Report, do not fix, in an audit.

## Finish review [new-work §7]

After the build, one batched screenshot round at the shipped sizes (driving hover, focus, open, error,
empty and overlong states), fix, one final round: two rounds is the ceiling. Validate captures first
(motion settled, full page from the top, no blank regions). Then a fresh subagent with no conversation
history reviews the screenshots, the plan header or direction contract, and `references/anti-slop.md`,
using `members/impeccable/reference/degraded/finish-reviewer.md` as its prompt (its engine-only checks are
skipped). Its first line is one word: recapture, rebuild, fix or ship. Report that word as given; a fix
list with open items is never announced as a pass. Applied fixes go back to the same reviewer for a
resolved / partial / unresolved verdict.
