---
name: web-a11y
description: Web accessibility (a11y) testing, repair and test planning against WCAG 2.2 AA - automated rule scan of a live page, hands-on inspection (keyboard and focus, screen-reader names, roles and states, reflow at 320px, 200-400% zoom, text spacing, reduced motion, forms, target size), mechanical fixes with a baseline-edit-verify loop, regression diff of a change or branch, WCAG-EM site audits with per-criterion conformance, and test plans for real assistive-technology users (AT matrix per key flow, VoiceOver, NVDA, JAWS, TalkBack, voice control, switch, zoom; participants with disabilities; session protocol). Use for "is this page accessible", "check a11y", WCAG, Section 508, ADA, contrast, alt text, labels, ARIA, keyboard trap, tab order, screen reader, "fix the a11y issues", "did my change break accessibility", CI a11y gate, accessibility audit, conformance report, accessibility test plan, testing with disabled users. Runs on the AccessLint CLI or, with no install, the Playwright MCP.
members: [accesslint-accessibility-scan, accesslint-accessibility-inspect, accesslint-accessibility-fix, accesslint-accessibility-diff, accesslint-accessibility-audit, accessibility-test-plan]
---

# Web A11y

The five AccessLint skills as one pipeline: **locate** (scan, inspect), **assess** (audit), **remediate**
(fix), **guard** (diff), plus Owl-Listener's `accessibility-test-plan` to **plan** the human testing the
pipeline hands off (AT matrix, participants, session, reporting). Load this file first; open a member file
only for its exact commands and report formats. Member paths are relative to this folder. The shared doctrine the five AccessLint members follow lives
outside the member folders, at
the accesslint plugin's shared `methodology.md` (public `accesslint/claude-marketplace` repo).
Building accessible UI from the start (patterns, tokens, focus rings) is `~/.claude/skill-library/design/ui-studio/SKILL.md` step 4.8;
this skill checks and repairs.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| "Is this page accessible?", contrast, alt text, labels on one URL, verify a UI change | **Scan** | Step 2. `members/accesslint-accessibility-scan/SKILL.md` |
| Keyboard, focus order, screen-reader names, reflow and zoom, reduced motion, "operable, not just lint-clean" | **Inspect** | Step 3. `members/accesslint-accessibility-inspect/SKILL.md` and `members/accesslint-accessibility-inspect/references/checkpoints.md` (`--deep` drives every triggered area fully) |
| "Fix the a11y issues", add alt and labels, apply a findings list | **Fix** | Step 4. `members/accesslint-accessibility-fix/SKILL.md` |
| "Did my change break accessibility?", PR check, CI gate | **Diff** | Step 5. `members/accesslint-accessibility-diff/SKILL.md` |
| Whole site or product, WCAG / Section 508 / ADA conformance report, several pages | **Audit (WCAG-EM)** | Steps 1-6. `members/accesslint-accessibility-audit/SKILL.md` plus the methodology file |
| Plan testing with screen-reader or other AT users, an AT test matrix for a release, recruit participants with disabilities, a11y in the definition of done | **Test plan** | Step 7. `members/accessibility-test-plan/SKILL.md`; feed it the ○ handoff list from Inspect or Audit |
| AccessLint not installed or not approved yet | **Fallback** | Playwright recipes in step 3; automated tier graded no higher than ◐ for contrast on non-flat grounds |
| Explain a rule or success criterion | **Explain** | `explain_rule` (AccessLint MCP) if enabled, else WebFetch the W3C "Understanding" page for that SC |
| Designing or building new UI | **Build-time** | `~/.claude/skill-library/design/ui-studio/SKILL.md` step 4.8 and `~/.claude/skill-library/design/ui-studio/references/preflight.md` §1, then Scan before shipping |

## Tools (decide once per session)

1. **AccessLint CLI** (scan, diff, and the baseline/verify inside fix). The members call
   `npx -y @accesslint/chrome@latest ensure` (prints JSON with the debug `port`; never hardcode 9222),
   `npx -y @accesslint/cli@latest scan <url|target> --port "$PORT" --format json`, and
   `npx -y @accesslint/chrome@latest stop --all` to tear down (skip when `ensure` reported
   `"managed":false`). The user pins versions: on first use ask him, look up the current version once
   (`npm view @accesslint/cli version`, same for `@accesslint/chrome`), then call those exact versions,
   prefixed `npm_config_cache=/tmp/npm-cache`. Useful flags: `--selector`, `--wait-for "<css>"`,
   `--include-aaa`, `--disable <rules>`. Targets can live in `accesslint.config.json` (plus a gitignored
   `accesslint.config.local.json`); `npx @accesslint/cli init` writes one into the repo, so ask first.
   Exit code 2 means a bad URL or target, or the page never loaded: check the dev server.
2. **AccessLint MCP** (`audit_live`, `audit_html`, `explain_rule`, `list_rules`) exists only when the
   accesslint plugin's MCP server is enabled, and that server runs `npx -y @accesslint/mcp@latest`. Treat
   it as installed-off: enabling it means asking the user, reading the package, pinning the version. Without
   it, fix mode uses the CLI scan as baseline and verify, and a raw HTML file is served locally (port
   a free port) and scanned by URL.
3. **Browser for the manual tier.** The members expect the `chrome-devtools` MCP. The user has the Playwright
   MCP (headless, use it) and claude-in-chrome (their real Chrome: only for pages behind their login, and say
   why in one line). Tool map:

| Member calls | Playwright MCP |
|---|---|
| `navigate_page`, `wait_for` | `browser_navigate`, `browser_wait_for` |
| `take_snapshot` (a11y tree) | `browser_snapshot` (`target` for one subtree, `boxes: true` for sizes) |
| `evaluate_script` | `browser_evaluate` (`function`, optional `target`) |
| `press_key`, `click`, `fill`, `fill_form`, `hover` | `browser_press_key`, `browser_click`, `browser_type`, `browser_fill_form`, `browser_hover` |
| `resize_page` | `browser_resize` |
| `emulate` (reduced motion) | `browser_emulate_media` (`reducedMotion: "reduce"`; also `colorScheme`, `forcedColors: "active"`, `contrast: "more"`) |
| `take_screenshot` | `browser_take_screenshot` |

## Unified workflow

### 1. Scope (every mode; the full version for Audit)

- State the target and its boundary, the goal (WCAG 2.2 AA by default; AAA only on request), the
  technologies in use, and the assistive-technology baseline the human handoff should cover (for example
  NVDA + Firefox, JAWS + Chrome, VoiceOver + Safari on macOS and iOS, TalkBack + Chrome, keyboard only,
  zoom to 400%, voice control). You scope that baseline; you do not test it [audit]. Test plan mode
  (step 7) turns it into a matrix people run.
- One URL with no sampling is a scan, not an audit. Say which one you did [methodology].
- Audit only: explore routes, templates, shared components, key flows and stateful UI with Glob and Grep
  (`accesslint.config.json` targets are a start), then sample: a structured set (entry page, each key
  flow end to end, every page with a new template or complex widget, key states such as empty, error,
  modal open, signed in) plus a small random set, each with its reason [audit].
- Hold async content with `--wait-for` / the target's `waitFor`; scope a component with `--selector`.

### 2. Locate: automated tier (Scan)

1. Run the CLI scan (or `audit_live`) with `--format json` against the running page.
2. Report counts by impact, then one entry per violation: **where** (selector verbatim, plus
   `file:line (symbol)` only when the result carries `source`, which comes from React DevTools fibers on
   dev builds; otherwise say "source mapping unavailable; located by selector only"), **evidence**
   (contrast ratio, missing attribute, empty name), **fix** (the mechanical change, or `NEEDS HUMAN`) [scan].
3. The engine owns the statically detectable criteria: name and label presence, `lang`, `autocomplete`,
   semantic markup, text contrast on flat grounds. The manual tier never re-checks them [inspect, audit].
4. Scan locates; it never edits. Fixes happen in step 4 [scan].
5. Automation catches roughly 57% of real defects (Deque); a clean scan is not conformance [methodology].

### 3. Locate and grade: manual tier (Inspect)

**The ledger is a denominator, not a script.** Every SC in the areas below ends the run in exactly one
state: ● pass or fail, ◐/○ flagged, engine-owned, N/A (the feature is absent, decided from the snapshot,
free), or not exercised (reported as undetermined, never as a pass). Drive only what the page's features
and the engine's gaps demand [inspect, methodology].

| Area | SCs | Drive when |
|---|---|---|
| Keyboard and focus | 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11 | Always: one batched walk |
| Structure and semantics | 1.3.1, 1.3.2, 2.4.1, 2.4.6 | Always: read from the first snapshot (landmarks, one `main`, one h1, no skipped levels, semantic lists and tables) |
| Names, roles, states | 4.1.2, 2.5.3, 4.1.3 | Custom widgets or stateful controls present (label-in-name is inspect's) |
| Visual adaptation | 1.4.1, 1.4.4, 1.4.10, 1.4.12, 1.3.4, 2.3.3, 1.4.11 | Reflow and zoom on every page; motion checks only if motion exists |
| Forms and errors | 3.3.1-3.3.3, 1.3.5, 3.3.7, 3.3.8 | A form is present |
| Media and timing | 1.2.x, 2.2.1, 2.2.2 | Video, audio, autoplay or timeouts present |
| Pointer and target | 2.5.1, 2.5.7, 2.5.8 | Target size comes free from the walk; drag checks only with drag UI |
| Content and navigation | 3.1.1-3.1.2, 2.4.4, 3.2.3-3.2.4, 3.2.6 | `lang` and link purpose from the snapshot; cross-page consistency belongs to Audit |

**Drive efficiently.** Take one full snapshot after the wait gate; it settles structure, names, roles,
states and every N/A. After a state change read only the widget that changed (`browser_snapshot` with
`target`, or a scoped `browser_evaluate`); a full re-snapshot per interaction is the biggest avoidable
cost [inspect]. Then one batched keyboard walk in a single evaluate call:

```js
() => {
  const q = 'a[href],area[href],button,input:not([type=hidden]),select,textarea,summary,iframe,[tabindex],[contenteditable="true"],[contenteditable=""]';
  const shown = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(e).visibility !== 'hidden'; };
  const els = [...document.querySelectorAll(q)].filter(e => !e.disabled && e.tabIndex >= 0 && shown(e));
  const order = [...els.filter(e => e.tabIndex > 0).sort((a, b) => a.tabIndex - b.tabIndex), ...els.filter(e => e.tabIndex === 0)];
  return order.map((e, i) => {
    e.focus();
    const r = e.getBoundingClientRect(), s = getComputedStyle(e);
    const top = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
    return { i, el: e.tagName.toLowerCase() + (e.id ? '#' + e.id : ''), text: (e.getAttribute('aria-label') || e.textContent || e.value || '').trim().slice(0, 50),
      focused: document.activeElement === e, outline: `${s.outlineStyle} ${s.outlineWidth} ${s.outlineColor}`, ring: s.boxShadow !== 'none',
      size: `${Math.round(r.width)}x${Math.round(r.height)}`, covered: !!top && !e.contains(top) && !top.contains(e), tabindex: e.tabIndex };
  });
}
```

Read it as: order (2.4.3, ◐ for coherence), `focused: false` (unreachable or redirected focus),
`tabindex > 0` (order bug), no outline and no ring (2.4.7 suspect), `covered: true` (2.4.11 suspect,
screenshot it), size under 24x24 (2.5.8 ●, unless the spacing exception applies). Two limits: scripted
`focus()` may not trigger `:focus-visible` styles the way a real Tab press does, so a missing ring is a
suspect until a real `Tab` confirms it; `text` only approximates the accessible name, the snapshot holds
the real one. The walk finds candidates; real key presses confirm behaviour only at the suspects:
composite widgets (roving tabindex, `aria-activedescendant`), elements whose handlers may capture Tab or
Esc, anything the walk could not reach. A ● keyboard-trap claim needs real `Tab`/`Esc` at that widget
[inspect].

**Visual adaptation recipes** (each one resize, one evaluate, one screenshot):
- Reflow 1.4.10: `browser_resize` to 320x800, then
  `() => ({ sw: document.documentElement.scrollWidth, vw: innerWidth, wide: [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1).slice(0, 10).map(e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '')) })`.
  Overflow is a ● fact; whether it fails is ◐ (data tables, maps and toolbars are exempt).
- Zoom 1.4.4: `document.documentElement.style.zoom = '2'` (then '4'); real browser zoom is not exposed,
  so this stays ◐ and the report says so.
- Text spacing 1.4.12: inject
  `*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}p{margin-bottom:2em!important}`
  as a `<style>` and look for clipped or overlapping text.
- Reduced motion 2.3.3 and 2.2.2: `browser_emulate_media({ reducedMotion: "reduce" })`, reload, observe
  that motion stops and nothing stays hidden; anything moving past 5s needs a pause control.
- Non-text and state contrast 1.4.11, colour alone 1.4.1: screenshot focus, hover and selected states;
  the engine misses text on images and focus or hover contrast. Optional: `forcedColors: "active"`.
- Fallback contrast (only when no engine ran; ◐ unless both colours are flat and opaque):

```js
() => {
  const cx = Object.assign(document.createElement('canvas'), { width: 1, height: 1 }).getContext('2d', { willReadFrequently: true });
  const rgba = c => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = c; cx.fillRect(0, 0, 1, 1); return cx.getImageData(0, 0, 1, 1).data; };
  const lum = d => [0, 1, 2].reduce((a, i) => { const v = d[i] / 255; return a + [0.2126, 0.7152, 0.0722][i] * (v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4); }, 0);
  const ground = e => { for (; e; e = e.parentElement) { const d = rgba(getComputedStyle(e).backgroundColor); if (d[3] > 0) return d; } return rgba('#fff'); };
  const hits = [];
  for (const e of document.querySelectorAll('body *')) {
    if (![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
    const s = getComputedStyle(e); if (s.visibility === 'hidden' || !e.getClientRects().length) continue;
    const a = lum(rgba(s.color)), b = lum(ground(e)), ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
    const px = parseFloat(s.fontSize), need = px >= 24 || (px >= 18.66 && +s.fontWeight >= 700) ? 3 : 4.5;
    if (ratio < need) hits.push({ el: e.tagName.toLowerCase() + (e.id ? '#' + e.id : ''), text: e.textContent.trim().slice(0, 40), ratio: +ratio.toFixed(2), need });
  }
  return hits.slice(0, 40);
}
```

  The canvas round-trip turns `oklch()` and other modern colour syntaxes (Tailwind v4) into RGB. It does
  not blend semi-transparent text or grounds and cannot see background images or gradients; those cases
  stay ◐ with a screenshot.

**Forms:** submit invalid input; programmatic association of errors (`aria-invalid`, `aria-describedby`)
is ● (3.3.1); whether the message helps recovery is ◐ (3.3.3); redundant entry (3.3.7) and accessible
sign-in, with paste and password managers allowed (3.3.8), are ◐ after exercising the flow [checkpoints].

**High-risk patterns** (drag and drop, rich-text editors, tree views, data grids, custom comboboxes or
menus, carousels, toast or live-region heavy UIs): name the APG pattern and the keyboard and ARIA contract
it owes, verify what you can (●/◐), hand the rest off as ○ with the AT steps to run [methodology].

### 4. Remediate (Fix)

1. **Input:** a findings worklist (apply it directly) or a target (baseline it first with the same tool
   you will verify with). Given neither, ask what to fix; never sweep a codebase unprompted [fix].
2. **Find the source:** a `Source:` line opens at that file and line (several joined by `←`: the first is
   the JSX literal, the rest enclosing components; `Symbol` disambiguates). Without one, grep stable hooks
   (`data-testid`, `id`, `aria-label`), then visible text, then tree position [fix].
3. **Apply** mechanical fixes as given; contextual or visual ones get a `TODO` with the rule ID. Never
   invent alt text, labels or link text. Group edits per file. Confirm scope before touching files outside
   the obvious target or before more than about 10 fixes [fix]. Typical mechanical fixes: `lang` on
   `<html>`; `<label for>` or wrapping label; `alt=""` plus `aria-hidden` on clearly decorative images and
   icons; `type="button"` on non-submit buttons; remove positive `tabindex`; restore a `:focus-visible`
   ring; swap a failing colour to the nearest design token that passes; `aria-expanded` on disclosure
   toggles; native `<button>` in place of a clickable `div`.
4. **Verify** with the same audit: every targeted violation gone, no new one. For a precise new / fixed /
   pre-existing comparison on a URL, run Diff. If a violation has no `Fix:` directive, leave a TODO; if
   verification fails, report it and stop instead of iterating silently [fix].
5. **Output per cycle:** the tool used, violations by impact, what was applied (file and rule), what was
   deferred and why, before and after counts. Large remediations can run in a subagent for context
   isolation, same steps [fix].

### 5. Guard (Diff)

- **Stash mode** (default, uncommitted changes): tell the user first ("stashing your changes to capture a
  baseline, then restoring"), `git stash push -u -m "accesslint-diff-baseline"`, scan with
  `--snapshot accesslint-diff --snapshot-dir /tmp --update-snapshot`, `git stash pop && sleep 2`, scan
  again with `--format json`. If `git stash push` fails, stop [diff].
- **Branch mode** (`--branch <name>`): stash if the tree is dirty, check out the branch, baseline,
  `git checkout -` and pop, scan again; pass `--wait-for` as the rebuild gate or warn the baseline may be
  stale [diff].
- **After either mode** confirm `git status` matches the start and no `accesslint-diff` entry is left in
  `git stash list`; on a pop conflict stop and tell the user; never resolve it by discarding their work.
- Pass the same `--selector` and `--include-aaa` to both runs; if the change touches
  `accesslint.config.json`, use an explicit URL. Large DOM changes cause selector drift; rerun a full
  scan then [diff].
- Report "N new · N fixed · N pre-existing hidden", then each new violation with where, evidence and fix.
  Wiring Diff into CI changes the repo's CI config: propose it, the user approves.

### 6. Report and conformance (Audit)

- **Evaluate** each sampled page or state with scan first, then inspect on the same rendered state (same
  URL, `--selector`, `--wait-for`), passing the scan's covered SCs into inspect so ownership is decided
  before driving. Where both tiers still cover one SC on one element, the scan result wins [audit].
- **Conformance per SC across the whole sample:** pass or fail only for ● criteria; everything ◐, ○ or not
  exercised is undetermined and goes to a human. One failing page fails the SC for the scope; never
  average it away [methodology].
- **Report shape** (full template in `members/accesslint-accessibility-audit/SKILL.md`): scope, sample
  (structured and random, with reasons), conformance counts with bare SC lists and undetermined SCs grouped
  by shared reason, findings by severity tagged ●/◐ with tier and location, the ○ handoff list,
  recommendations (root-cause fixes that clear many instances, what goes to human AT testing on which
  flows, Diff in CI). Words go to failures, flags and handoffs; a pass is its SC number [audit].
- **State what was not covered:** pages outside the sample, ○ criteria, skipped areas. Omitting it reads
  as "all clear" [methodology].

### 7. Plan human testing (Test plan)

Steps 2-6 stop at the ○ handoff: Claude scopes AT testing but never performs or emulates it. This step
turns that handoff into a plan people can run [accessibility-test-plan; joined to the ledger in the merge].

1. **Layers, cheapest first** [accessibility-test-plan]: automated (step 2 on every page and state, kept
   in CI through Diff) -> manual (keyboard only, a screen-reader walkthrough, real browser zoom at 200% and
   400%, Windows high contrast or forced colours, reduced motion; the parts step 3 graded ◐ get a person's
   call here) -> assistive technology (screen readers VoiceOver on macOS and iOS, NVDA, TalkBack, JAWS
   where the audience is enterprise; Voice Control and Dragon; switch control; screen magnification) ->
   users with disabilities.
2. **Test matrix:** rows are the key flows (the Audit sample's flows, or the money paths: checkout,
   signup, booking, payment); columns are keyboard only, VoiceOver, NVDA, zoom 200%, high contrast,
   reduced motion, plus TalkBack and iOS VoiceOver for mobile flows and voice control where forms dominate.
   Each cell carries the ○ items it settles (SC, ability, what to try), an owner and a status: pass, fail,
   blocked, not run.
3. **Participants** (only when the user approves recruiting; see House rules): a spread across vision, motor,
   cognitive and hearing; they use their own devices, AT and settings (remote sessions make that easy);
   tasks are real goals ("buy the hoodie in your size"), not compliance checkboxes. Ask only what the test
   needs about anyone's disability, and keep it out of the report.
4. **Session protocol** [new in merge, around the member's points]: consent, including for recording;
   accessible materials and scheduling; the AT and version noted at the start; tasks read as goals; the
   moderator does not help until the participant is stuck, and notes it when they do; a short debrief on
   the hardest moment. Moderation technique in general is ux-lab's (test scenarios).
5. **Report each human finding** with the step 6 grades plus [accessibility-test-plan]: description, WCAG
   SC, severity by user impact, AT + version + browser or device affected, steps to reproduce,
   remediation. A cell a person ran and reproduced becomes pass or fail for that SC, so the conformance
   from step 6 updates; cells not run stay undetermined.
6. **Keep it continuous:** test early, not just before launch; propose an accessibility definition of
   done for the project (Diff clean, keyboard walk of every changed flow, the matrix rows the change
   touches); prioritize fixes by user impact, not only by conformance level [accessibility-test-plan].

## Core rules and checklists

**Two grades per finding, kept separate** [methodology]:
- Evidence basis: ● verified (deterministic, reproducible, with selector, interaction and observed DOM or
  tree fact), ◐ flagged (evidence attached, a person decides), ○ human-required (needs AT or lived
  experience; handed off, never emulated). Unsure between two grades: take the lower. A finding that
  stacks a ● fact on an interpretive call takes the lower grade (status dots: "no programmatic status in
  the tree" is ● 1.3.1; "colour is the only carrier" stays ◐ 1.4.1). The symbols differ by fill, not
  colour, so the report reads for colour-blind readers.
- Severity (user impact): critical (blocks a core task, no workaround: a keyboard-trapped checkout, an
  unlabelled sole submit button), serious (possible but hard: illogical focus order through a form, body
  text failing contrast), moderate (friction, still completes: a missing skip link), minor (polish).

**Evidence budget** (uncertainty must be cheaper than false certainty): ● gets full proof, gathered once;
◐ gets one selector, one screenshot if the question is visual, an opinion and what a person should
confirm, then stop; ○ gets no driving at all, only the ability, the AT and the flow already exercised
[methodology].

**No proxy for human experience:** usability enters only as labelled ◐ heuristics ("valid but hard to
follow"); no personas, synthetic sessions or predicted screen-reader behaviour. The a11y tree shows machine
state, not what is announced: `aria-live` present is ●, that it announces is ○. Each ○ names the functional
ability (Section 508 FPC wording: without vision, limited vision, without perception of colour, without
hearing, limited hearing, without speech, limited manipulation, limited reach and strength, limited
language, cognitive and learning abilities), the AT, and the flow [methodology].

**Grounding:** selector plus visible text; `file:line` only from source maps; never fabricate a location
or content [methodology].

**WCAG 2.2 AA numbers to hold:** text contrast 4.5:1, large text (24px, or 18.66px bold) 3:1, UI parts and
focus indicators 3:1 (1.4.3, 1.4.11); targets 24x24 CSS px or spaced (2.5.8); reflow at 320 CSS px with no
two-way scrolling (1.4.10); text resizable to 200% (1.4.4); content survives spacing of 1.5 line height,
2x paragraph spacing, 0.12em letters, 0.16em words (1.4.12); focus never fully hidden by sticky UI
(2.4.11); no keyboard trap (2.1.2); visible label text inside the accessible name (2.5.3); single-pointer
alternative to dragging (2.5.7); pause, stop or hide for motion past 5s (2.2.2); status messages
programmatic (4.1.3); consistent help placement (3.2.6); no redundant entry (3.3.7); sign-in without a
cognitive test (3.3.8).

**Coverage numbers are different metrics:** "~57% of defects caught by automation" (Deque) and "~64% of
criteria partially auto-detectable" (GitHub) are not interchangeable; never quote either as a conformance
rate [methodology]. accessibility-test-plan's "30-40% of issues" has no source or date: not used. All three
agree on the point that matters: automation is necessary, never sufficient.

## When members disagree

1. **Edit or not.** scan and diff say "don't edit", then suggest applying mechanical fixes and re-running.
   **Rule:** Scan, Inspect, Audit and Diff never edit; edits happen in Fix mode, which may follow in the
   same session when the user asked for fixes.
2. **Which browser.** inspect is written for the chrome-devtools MCP. **Rule:** Playwright MCP through the
   tool map; claude-in-chrome only behind the user's login, with the reason stated.
3. **Subagents.** audit gives every sampled page its own Task; the user's cost rule says no subagents for small
   work. **Rule:** inline for one or two pages; for bigger samples batch two or three pages per subagent;
   mechanical scan-only runs may use haiku, inspect needs a stronger model because it judges.
4. **`@latest`.** every member calls npm packages at `@latest`; the user's security rules pin versions.
   **Rule:** ask once, pin, reuse the pinned version (Tools, item 1).
5. **Fix freely or ask.** fix applies mechanical fixes up to about 10 before confirming; the user's change
   protocol covers any change to a live product. **Rule:** on a local or feature branch, fix follows its
   own limits; on a live site, app or dashboard, findings and the fix list go to the user's review page first.
6. **Target size.** WCAG 2.5.8 fails below 24x24; ui-studio designs to 44x44. **Rule:** fail at 24; under
   44 is a minor recommendation, never a conformance failure.
7. **Same SC in both tiers.** **Rule:** scan's result wins at the same element; inspect never re-derives
   an engine-owned SC [audit].
8. **Diff's stash.** diff stashes the working tree; the user's repos may hold unrelated uncommitted work.
   **Rule:** announce it, verify the restore, prefer branch mode when the tree is mid-merge or mid-rebase
   (or skip Diff and scan twice by hand).
9. **Who tests with AT.** accessibility-test-plan says test with real AT and AT users; the methodology says
   ○ items are handed off, never emulated. **Rule:** Claude writes the plan, the matrix and the report
   template; people run the AT cells; Claude never fills an AT cell from a snapshot or an emulation.
10. **Automated tools.** accessibility-test-plan names axe, Lighthouse and WAVE; this skill runs AccessLint
   or the Playwright fallback. **Rule:** AccessLint or Playwright by default; a tool the project's CI already
   runs (for example Lighthouse) may stay; nothing new is installed without the user (House rules).
11. **How much automation catches.** 30-40% [accessibility-test-plan] vs ~57% (Deque) [methodology].
   **Rule:** quote the sourced figure only, and never as a conformance rate (Core rules).
12. **Zoom and high contrast.** accessibility-test-plan lists 200%/400% zoom and high-contrast mode as
   manual checks; inspect can only approximate them (CSS zoom, `forcedColors` emulation, graded ◐).
   **Rule:** inspect's result is the flag; the Test plan matrix carries the real-browser check.

## Combine with

- `~/.claude/skill-library/design/ui-studio/SKILL.md`: build-time accessibility patterns (step 4.8), design-token fixes for contrast,
  focus-ring styling, reduced-motion rules (step 5), and its preflight.
- `~/.claude/skill-library/testing/test-and-harden/SKILL.md` for wiring Diff into CI; `~/.claude/skill-library/web/react-next-pro/SKILL.md` for React source
  fixes; `~/.claude/skill-library/web/commerce-pro/SKILL.md` for Shopify theme pages.
- Superpowers: `superpowers:verification-before-completion` (a re-scan is the evidence before saying
  "fixed"); `superpowers:requesting-code-review` after a large remediation.
- Built-in agent type `design-review` for a Playwright review that also covers visual consistency.
- ux-lab super-skill (`~/.claude/skill-library/design/ux-lab/SKILL.md`): usability test
  scenarios and session moderation for the Test plan's participant sessions; ux-lab owns general usability
  research, this skill owns the accessibility plan.
- Voltagent prompts under `~/.claude/skill-library/agents/voltagent/` (Read the file, pass it as the
  Agent prompt): `04-quality-security/accessibility-tester.md` (WCAG and AT testing),
  `04-quality-security/ui-ux-tester.md` (flow-driven UI testing), `01-core-development/frontend-developer.md`
  (implementing fixes across React, Vue, Angular).

## House rules (the user)

- Installing anything (AccessLint CLI or Chrome via npx, the AccessLint MCP or plugin, the chrome-devtools
  MCP) asks the user first; versions pinned, never `@latest`; `npm_config_cache=/tmp/npm-cache`; read MCP code
  before enabling.
- CLIs and headless checks before browser automation; Playwright headless before the user's own Chrome, and
  say why when their browser is needed.
- Fixes on a live site, app or dashboard go through the change protocol: evidence, a review page with old
  and new per change, the user picks, then build, then watch the first real result.
- On store and landing pages, accessibility fixes must make buying easier, never harder: flag any fix that
  adds friction to the path to purchase (extra steps, hidden or demoted CTAs) instead of applying it
  silently.
- Alt text, labels and link text come from the user or the page's copy owner; leave a TODO rather than invent
  them (accesslint methodology; matches the user's "solve problems, don't create more").
- Local dev servers for scanning run on a free port.
- Recruiting test participants, paying them, or booking a paid AT-testing panel or service asks the user first;
  Claude drafts the plan and the outreach, never sends it. Disability details are sensitive health data:
  collect only what the test needs and keep names and diagnoses out of reports.

## Members

| Member | Best at | Path |
|---|---|---|
| accesslint-accessibility-scan | Automated tier: @accesslint/core rule engine over CDP, WCAG 2.2 worklist grounded to selector and `file:line` | `members/accesslint-accessibility-scan/SKILL.md` |
| accesslint-accessibility-inspect | Manual tier: SC ledger as denominator, ●/◐/○ grading, evidence budget, batched keyboard walk, per-checkpoint procedures | `members/accesslint-accessibility-inspect/SKILL.md` |
| accesslint-accessibility-fix | Baseline, edit, verify loop; source location from React fibers; mechanical fixes only, TODOs for judgment | `members/accesslint-accessibility-fix/SKILL.md` |
| accesslint-accessibility-diff | Regression check against uncommitted changes (stash) or a branch: new, fixed, pre-existing | `members/accesslint-accessibility-diff/SKILL.md` |
| accesslint-accessibility-audit | WCAG-EM umbrella: scope, explore, sample, evaluate both tiers, per-SC conformance report with AT handoffs | `members/accesslint-accessibility-audit/SKILL.md` |
| accessibility-test-plan | Human side of testing: four layers, AT list (screen readers, voice control, switch, magnification), flow x AT test matrix, participants with disabilities, finding report fields, a11y in the definition of done | `members/accessibility-test-plan/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
