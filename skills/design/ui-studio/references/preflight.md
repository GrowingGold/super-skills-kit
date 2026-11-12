# Preflight (merged checklist)

Run before saying a UI is done. Built from v2-experimental §14, taste-skill §5, ui-ux-pro-max's
pre-delivery checklist and quick reference, make-interfaces-feel-better, bencium's decision checklist,
design-audit's dimensions, typography, impeccable's craft floor, polish, harden and audit, and the
Owl-Listener scale skills (values in scales-and-systems.md). Sections follow ui-ux-pro-max's priority order: fix in this
order when time is short. A line you could not check goes in the report as "not checked", never as a pass.
In the company-site pipeline, taste-skill's checker and gate automate many of these lines; still read
the screenshots yourself.

## 0. Process

- [ ] The plan header exists (design read, kind and visitor mode, main action, dials, direction and
      signature) and the build matches it [v2 §0.B, taste-skill, impeccable].
- [ ] Every brief requirement is present and findable within seconds [impeccable craft floor].
- [ ] Rendered and looked at 1440, 1024, 768 and 390, walked 320 for overflow, both themes, reduced
      motion on [taste-skill, ui-ux-pro-max, v2 §8.D]. App UI: also landscape and largest text size.
- [ ] Every visual draws at every width; a refused effect shows its still fallback [taste-skill].
- [ ] Copy self-audit: every visible string re-read; broken grammar, unclear referents, cute-but-wrong
      lines and tells rewritten [v2 §4.9, references/anti-slop.md].
- [ ] Launch page, big redesign or the user asked: a fresh no-history subagent ran the finish review and its word (ship, fix,
      rebuild, recapture) is reported as given [impeccable; impeccable-playbook.md].

## 1. Accessibility (critical; depth in ../../web-a11y/SKILL.md)

- [ ] Text contrast 4.5:1 (large text 3:1); UI parts, borders that carry meaning and focus rings 3:1;
      checked in both themes; buttons over photos have a scrim; placeholders, helpers and errors pass
      [ui-ux-pro-max, v2 §4.5].
- [ ] Visible focus on every control, never under a sticky header; skip link is the first Tab stop;
      Tab order follows visual order; no `tabindex` above 0 [taste-skill, ui-ux-pro-max].
- [ ] Icon buttons named; menu toggles report expanded state; decorative icons `aria-hidden`; meaningful
      images have alt; one h1; heading levels never skip; `lang` set [taste-skill, ui-ux-pro-max].
- [ ] Colour is never the only signal; links in running text have a non-colour cue [ui-ux-pro-max, typography].
- [ ] Modals: focus trap, Esc closes, scroll lock, `role="dialog"`, `aria-modal="true"`, focus returns
      to the trigger [motion-patterns].
- [ ] Anything moving longer than 5s has a pause control; carousels stop on focus and under reduced
      motion [taste-skill, ui-ux-pro-max].
- [ ] Drag has a single-pointer alternative; sign-in allows paste and password managers [ui-ux-pro-max].

## 2. Touch and interaction (critical)

- [ ] Targets 44x44 px with 8px between them (WCAG floor 24x24); small icons get a pseudo-element hit
      area that does not overlap its neighbours [ui-ux-pro-max, make-interfaces, taste-skill].
- [ ] Every button, link, linked card and linked photo answers hover and press within 100ms; pressed
      states never shift layout [taste-skill, ui-ux-pro-max].
- [ ] Async buttons disable and show progress; `touch-action: manipulation`; `cursor: pointer` on
      clickables; nothing works only on hover [ui-ux-pro-max].

## 3. Performance (high)

- [ ] LCP under 2.5s, INP under 200ms, CLS under 0.1 [v2 §6.D].
- [ ] Images: width/height or `aspect-ratio`, WebP/AVIF, the hero preloaded or `priority`, the rest
      lazy; fonts `font-display: swap`, only critical faces preloaded [ui-ux-pro-max, v2].
- [ ] `backdrop-filter` only on fixed or sticky layers; grain only on a fixed `pointer-events:none`
      layer; at most four live WebGL contexts; Motion, GSAP and Three lazy-loaded below the fold
      [soft, v1, taste-skill].
- [ ] Lists over 50 items virtualised [ui-ux-pro-max].

## 4. Style and system (high)

- [ ] One design system, one icon family and stroke weight, one button pair, one card style, one radius
      scale, one link look, two boxes deep at most [v2, taste-skill].
- [ ] Components use tokens only: no raw hex or px (`validate-tokens.cjs`) [design-system, design-audit].
- [ ] One accent across the page, one neutral temperature, one theme per page [v1, v2].
- [ ] Shadows mean elevation, borders mean separation; one shadow scale [make-interfaces, ui-ux-pro-max].
      Cards and bordered buttons on varied grounds may use the `--shadow-border` ring (light: 1px ring at
      .06 plus two soft layers; dark: one white ring at .08, .13 on hover); dividers, table cells and
      inputs keep real borders (SKILL.md conflict 36) [make-interfaces surfaces.md].
- [ ] Image outlines are pure `rgba(0,0,0,.1)` / `rgba(255,255,255,.1)` with `outline-offset:-1px`
      (Tailwind `outline-black/10 dark:outline-white/10`), never slate, zinc or an accent [make-interfaces].
- [ ] Every sourced component passed the `component-sources.md` safety checklist: item JSON read,
      dependencies checked and pinned, demo content and author links removed, restyled to the project's
      tokens, icon set and motion library, licence and attribution recorded [watermelon-ui, ui-studio].
- [ ] Anti-slop sweep done (references/anti-slop.md): no gradient text, side stripes over 1px, nested
      cards or off-world hard offset shadows; eyebrows only when a preset or the user asks, then at most
      ceil(sections / 3) [impeccable, v2].
- [ ] Browser surfaces themed from the palette: `::selection`, `caret-color`, scrollbars, focus ring,
      `text-underline-offset`, tabular numerals in data [impeccable craft floor].
- [ ] No emoji used as icons [ui-ux-pro-max].

## 5. Layout and responsive (high)

- [ ] Hero alone on the first screen; H1 at most 2 lines on desktop; subtext at most 20 words and 4
      lines; main CTA visible without scrolling; at most 4 text elements; top padding at most pt-24
      [v2 §4.7, taste-skill].
- [ ] Desktop nav on one line, 64-80px tall [v2].
- [ ] Equal left and right content edges; nothing off the grid; no sideways scroll at 320 [taste-skill].
- [ ] At least 4 layout families across 8 sections; no 3 consecutive image/text splits; bento cells equal
      the item count [v2].
- [ ] Mobile collapse declared per section: one column at 390, full-width buttons, full-screen menu
      [taste-skill, v1].
- [ ] Full-height blocks use `min-h-[100dvh]` (or the pipeline's svh system), never `h-screen`; safe
      areas respected; nothing hidden behind fixed bars [v1, ui-ux-pro-max].
- [ ] Reading measure by context (articles 55-70, UI copy 45-65, helper text 40-60 characters); no
      edge-to-edge paragraphs [typography, readable-measure].
- [ ] Columns, gutters and margins follow the grid per breakpoint; more space above a heading than below;
      the squint test still shows primary, secondary and groups in order [layout-grid, visual-hierarchy,
      impeccable layout].

## 6. Type and colour (medium)

- [ ] Body text set first; at most 2 families plus a mono; at most 3 weights each; one scale ratio
      [typography, bencium].
- [ ] Curly quotes, real ellipsis, en dash in numeric ranges, `×` in dimensions, no `--`, no em-dash
      pauses in new copy, nbsp in "Fig. 3", "© 2026"; JSX text uses real characters [typography, v2].
- [ ] Headings `text-wrap: balance` (browsers only balance blocks of 6 lines or fewer in Chromium, 10 in
      Firefox), short-to-medium body `pretty`, neither on 10+ line prose or code; tabular numerals on
      changing numbers, not on phone numbers, postcodes or version strings [make-interfaces typography.md].
- [ ] Italic display words with descenders have leading 1.1 or more and a bottom reserve [v2].
- [ ] Display type at most 6rem; tracking never tighter than -0.04em; adjacent hierarchy levels clearly
      different (about 1.5x) [impeccable craft floor, visual-hierarchy].
- [ ] All caps only on short labels, letterspaced 5-12%; never bold plus italic; no underline for
      emphasis [typography].
- [ ] Dark mode designed, not inverted: elevation by lighter surfaces, desaturated accents, off-white
      text; contrast measured separately; scrims measured on the real ground [ui-ux-pro-max,
      dark-mode-design].

## 7. Motion (medium)

- [ ] Each motion has a one-line purpose; the budget holds (hero entrance, 1-2 moments, hover/press
      layer); motion claimed is motion shown [taste-skill, v2 §5].
- [ ] Only `transform` and `opacity` animate; no `transition: all`, no `will-change: all` [make-interfaces].
- [ ] Exits shorter than enters (about 150ms, a small fixed offset such as -12px, never the full height
      unless position matters); interruptible; nothing blocks input [ui-ux-pro-max, make-interfaces].
- [ ] Icon swaps use scale .25 to 1, opacity 0 to 1, blur 4px to 0 (spring 0.3s, bounce 0; or a CSS
      cross-fade with both icons in the DOM); toggles, tabs and icon swaps use `AnimatePresence
      initial={false}`, staged entrances do not; press `scale(0.96)`, never below 0.95 [make-interfaces
      animations.md].
- [ ] AnimatePresence: keyed direct child with `exit`; page swaps `mode="wait"`; SSR `initial` matches
      the server; `"use client"` on motion files; effects clean up [motion-patterns, motion-foundations, v1].
- [ ] No scroll listeners; pins use `start: "top top"`; reduced motion collapses every animation to its
      end state with nothing left hidden [v2 §5, taste-skill].

## 8. Forms and feedback (medium)

- [ ] Visible label above, error below and linked with `aria-describedby`, inputs at least 16px, input
      kept on error, a focused error summary after a multi-error submit [bencium, ui-ux-pro-max].
- [ ] Loading skeletons shaped like the result; empty states with a next step; errors say what happened
      and what to do; a confirmation appears only after a real send [v1, content-design, taste-skill].
- [ ] Chat or search fields that send on Enter cancel the default first, then skip while an IME is
      composing (`isComposing` or keyCode 229); Shift+Enter kept; a visible send button stays
      [ui-ux-pro-max guideline 120].

## 9. Navigation (high)

- [ ] Back works, the current page is marked, scroll position is kept, deep links work, breadcrumbs past
      2 levels, bottom nav at most 5 items on mobile [bencium, ui-ux-pro-max].
- [ ] Every link lands; one label per CTA intent; one primary action per screen [taste-skill, v2, ui-ux-pro-max].

## 10. Copy and content

- [ ] Buttons are a verb plus an object, at most 3 words, never wrap at desktop; sentence case; no
      invented data; stand-in photos and assumed facts listed in the report [v2, content-design, taste-skill].
- [ ] On a store or landing page, every section earns its place by moving people toward buying
      (House rules).

## 11. Charts and data (low)

- [ ] Legends, tooltips, accessible colours, meaning never carried by colour alone; build charts with
      the built-in `dataviz` skill [ui-ux-pro-max].

## 12. Hardening (app UI and anything with user data)

- [ ] Long, short, empty and emoji/RTL text; 1000+ items; huge numbers; offline, slow and 4xx/5xx states;
      German-length (+30%) labels; date, number and currency formats [impeccable harden].
- [ ] RTL pages use logical properties and directional icons that point the right way; style and product
      picks checked with ui-ux-pro-max `--rtl` [impeccable audit, ui-ux-pro-max].
