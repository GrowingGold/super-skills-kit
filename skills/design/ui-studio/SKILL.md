---
name: ui-studio
description: "UI design-and-build skill (34 skills incl. impeccable, ui-ux-pro-max, taste, Watermelon UI) for web pages, components and design systems: direction, tokens and scales (colour, dark mode, type, spacing, grid, measure), component sourcing (Watermelon UI, Skiper UI, shadcn registry, npx shadcn add), build in React, Next.js, Tailwind, shadcn/ui, polish, motion, audit. Use to build, redesign, restyle or review a landing page, store, company site, app UI or dashboard look; find a component library, block or animated component; 'make it look better / premium', 'looks generic / AI-made', 'feels off', visual hierarchy, layout grid, responsive, typography, design tokens, DESIGN.md, theming, illustration, animation, GSAP, UI copy; /impeccable commands (shape, polish, bolder, quieter, distill, harden, colorize, typeset, layout, delight, overdrive, clarify, adapt, optimize, animate); styles (brutalist, minimalist, soft, glass, tasteskill, Stitch). Critique: ux-lab. Accessibility: web-a11y."
members: [ui-ux-pro-max, bencium-controlled-ux-designer, bencium-impact-designer, bencium-innovative-ux-designer, design-audit, make-interfaces-feel-better, typography, ui-styling, design-system, web-design-guidelines, content-design, antigravity-design-expert, motion-foundations, motion-patterns, taste-skill, taste-brutalist-skill, taste-gpt-tasteskill, taste-minimalist-skill, taste-soft-skill, taste-stitch-skill, taste-taste-skill-v1, taste-taste-skill-v2-experimental, impeccable, color-system, dark-mode-design, typography-scale, spacing-system, layout-grid, readable-measure, responsive-design, visual-hierarchy, illustration-style, watermelon-ui, design-styles]
---

# UI Studio

One path through 33 design skills: direction, then system and tokens, type, build, polish and motion,
then audit. Load this file first and follow the workflow; open a member file only when a mode row or a
step points to it. Paths are relative to this folder (`members/<name>/` links to the original skill); run
member scripts from the project root as `$UI/members/...` with
`UI=~/.claude/skill-library/design/ui-studio`. Accessibility: `~/.claude/skill-library/design/web-a11y/SKILL.md`.
Concrete scale values (colour, dark mode, type, measure, spacing, grid, hierarchy, illustration) are in
`references/scales-and-systems.md`; impeccable's commands, used without its engine, in `references/impeccable-playbook.md`;
free component sources (Watermelon, Skiper UI, shadcn registries) and their safety checklist in `references/component-sources.md`.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| New page, site, app screen or component from a brief | **Build** (default) | Full Unified workflow below. Data assist: `members/ui-ux-pro-max/SKILL.md` (`--design-system`). |
| Full company or marketing website with automated checks, or the user says "tasteskill" / "taste-skill" | **Company-site pipeline** | `members/taste-skill/SKILL.md` end to end (Node 22+, local Chrome, its gate). House rules here still apply. |
| A new visual language where originality matters (new brand, campaign, publication) and the user will choose | **Invent** | `members/bencium-innovative-ux-designer/SKILL.md` and its `references/`: ten typography-only HTML directions A-J, the user locks one, then Round 2. Alternative: impeccable's new-world derivation (`references/impeccable-playbook.md`). |
| the user names a look or wants a style menu ("in a glass / retro / bento / riso style", 60+ options) | **Style library** | `members/design-styles/index.md` (67 named styles with tokens), then only the chosen `styles/<name>/DESIGN.md` and `SKILL.md`; one style per project. |
| the user names a style or wants a specific look | **Style direction** | Nine opt-in presets (Industrial Brutalist, Editorial Minimalist, Soft Premium, Motion-rich AIDA, taste v1, v2, company-site pipeline, Spatial / Antigravity, Bold tone), one per project, named in the plan header: direction table and quick specs in `references/style-directions.md`. |
| the user wants to approve each colour, font or layout choice, or brand stakes are real (logo, company colours) | **Controlled** | Present 2-3 options with trade-offs before each decision; examples in `members/bencium-controlled-ux-designer/SKILL.md`. |
| Tokens, theme, design system, colour system or tonal ramps, dark-mode palette, spacing scale | **System** | Step 2 and `references/scales-and-systems.md` §1, 2, 5. `members/design-system/references/token-architecture.md`, `semantic-tokens.md`, `component-specs.md`, `states-and-variants.md`, `tailwind-integration.md`; `members/color-system/SKILL.md`, `members/dark-mode-design/SKILL.md`, `members/spacing-system/SKILL.md`; impeccable `members/impeccable/reference/colorize.md`, `extract.md`; template `members/bencium-controlled-ux-designer/DESIGN-SYSTEM-TEMPLATE.md`. |
| DESIGN.md for another agent or Google Stitch, or from existing code | **Spec handoff** | Format: `members/impeccable/reference/document.md` (official spec, YAML tokens); prose and bans: `members/taste-stitch-skill/SKILL.md`, example `members/taste-stitch-skill/DESIGN.md`; agent prompt `design-bridge`. Conflict 32. |
| Typography fix, type scale, line length, wrong quotes or dashes, text looks amateur | **Type** | Step 3. `members/typography/SKILL.md`; CSS baseline `members/typography/css-templates.md`; entities `members/typography/html-entities.md` (both sit at the member root, not in `references/`); `members/typography-scale/SKILL.md`, `members/readable-measure/SKILL.md`, impeccable `typeset.md`. |
| Page structure: grid, columns, breakpoints, responsive behaviour, "what should the eye see first" | **Layout** | Steps 4.3-4.4 and `references/scales-and-systems.md` §5-6; `members/layout-grid/SKILL.md`, `members/responsive-design/SKILL.md`, `members/visual-hierarchy/SKILL.md`; impeccable `layout.md`, `adapt.md`. |
| shadcn/Tailwind components, dark mode, theming in React | **Components** | Step 4. `members/ui-styling/references/shadcn-components.md`, `shadcn-theming.md`, `shadcn-accessibility.md`, `tailwind-customization.md`, `tailwind-responsive.md`; stack notes via ui-ux-pro-max `--stack`. |
| A component, block, section or page start a free library may already have; "Watermelon", "Skiper", `npx shadcn add @ns/item`, "is there a component for this" | **Component sourcing** | Step 4.0 and `references/component-sources.md` (which source for what, registry config, licences, safety checklist); `members/watermelon-ui/SKILL.md` for its MCP tools. Compare 2-4, read the item JSON, install in the target project, restyle. |
| Animation, transitions, springs, scroll, GSAP | **Motion** | Step 5. `members/motion-foundations/SKILL.md` (tokens, SSR, reduced motion), `members/motion-patterns/SKILL.md` (button, modal, toast, stagger, page transition, layout), GSAP pin and pan skeletons in `members/taste-taste-skill-v2-experimental/SKILL.md` §5.A-5.C, timing tables `members/bencium-controlled-ux-designer/MOTION-SPEC.md`, impeccable `animate.md`. |
| "Feels off, flat, cheap, jumpy", a small polish pass | **Polish** | Step 5 polish list; `members/make-interfaces-feel-better/SKILL.md` with code in `surfaces.md`, `animations.md`, `typography.md`, `performance.md` (member root); impeccable `polish.md` (triage order in the playbook); report as before/after tables grouped by principle. |
| Make an existing design bolder, quieter, simpler, more colourful or more delightful | **Tune** | `references/impeccable-playbook.md` § Tune; impeccable `bolder.md`, `quieter.md`, `distill.md`, `colorize.md`, `delight.md`, `overdrive.md` (overdrive: the user picks one of 2-3 directions before code). Scope is sovereign. |
| `/impeccable` with or without a command | **Impeccable** | `references/impeccable-playbook.md`: command map, engine-less rules (no engine, hooks or live mode). Then the matching mode here. |
| Production-ready: edge cases, long text, i18n, RTL, errors, offline, performance | **Harden** | Playbook § Harden; impeccable `harden.md`, `optimize.md`; ui-ux-pro-max `--rtl`; `references/preflight.md` §12. |
| Audit an existing UI, redesign plan, "make it look better" on a live product | **Audit / Redesign** | Step 6 and `references/redesign-protocol.md`; `members/design-audit/SKILL.md`, `members/design-audit/audit-template.md`, `members/design-audit/design-principles.md`; impeccable `audit.md` (0-4 scores); the user approves a review page before any build. |
| Critique a rendered screen, "why is this confusing", UX laws, usability test | **Critique** (ux-lab leads) | `~/.claude/skill-library/design/ux-lab/SKILL.md`; ui-studio builds the fixes it lists. Conflict 31. |
| Review UI code against best practices, `file:line` findings | **Code review** | `members/web-design-guidelines/SKILL.md` (WebFetch the current Vercel guidelines) plus `references/preflight.md`. |
| Button labels, errors, empty states, tooltips, dialogs, /copy, /ux-copy | **UI copy** | `references/ui-copy.md`; `members/content-design/SKILL.md` (skip its n8n-only sections outside the n8n codebase); impeccable `clarify.md`. |
| Illustration style guide, spot, hero or empty-state illustrations | **Illustration** | `references/scales-and-systems.md` §7; `members/illustration-style/SKILL.md`; generation goes to media-studio after the user's yes. |
| Accessibility, WCAG, contrast, keyboard, screen reader | **A11y** | `~/.claude/skill-library/design/web-a11y/SKILL.md`. |
| Native app UI (iOS, Android, React Native, Flutter) | **App UI** | ui-ux-pro-max `--stack <stack>` and its Apple Native Experience style (`"apple native" --domain style`), `members/ui-ux-pro-max/references/pro-rules.md`; impeccable `ios.md`, `android.md`, `audit.native.md`, `adapt.native.md`; `~/.claude/skill-library/mobile/mobile-app-studio/SKILL.md`. |
| Internal dashboard, KPI screen, the user's own ops screens | **Dashboard** | Density dial 8-10, sans plus mono numbers, no cards at high density, impeccable Operate mode; `~/.claude/skill-library/data/dashboard-studio/SKILL.md`; charts with built-in `dataviz`. |
| Theme an artifact, document or deck | **Theme** | Built-in `anthropic-skills:theme-factory`; decks go to `~/.claude/skill-library/docs/docs-decks/SKILL.md` (skip design-system's slide system here). |

## Unified workflow

### 0. Read the room (every mode)

1. Classify the job: greenfield, redesign-preserve, redesign-overhaul, or polish-only [v2 §11.A].
   Refinement keeps the incumbent look; a redesign replaces it and never polishes it [impeccable].
2. Name the **visitor mode** of the surface, not the product [impeccable]: Persuade (landing, pricing,
   store: decide and act), Operate (app, dashboard, admin), Read (docs, help), Experience (portfolio).
   Operate and Read show ambition as precision; their direction lends type, palette, density and one
   signature move, never the layout, nav model or controls.
3. Detect the stack from `package.json`, `pubspec.yaml`, `Package.swift`, `composer.json`; never assume
   one, a wrong default misroutes every later choice [ui-ux-pro-max]. Note the Tailwind major version
   before writing a class: v4 syntax breaks v3 projects [v1].
4. Load what already exists: PRODUCT.md, DESIGN.md, `design-system/<slug>/MASTER.md` and any
   `pages/<page>.md` override (the override wins), token files, brand assets (logo, colours, fonts,
   photographs) [ui-ux-pro-max, design-audit, impeccable]. Existing brand and system beat every default in
   this file; a missing DESIGN.md does not make a coherent site greenfield [impeccable].
5. Ask or proceed by the rule in When members disagree, items 1 and 23.

### 1. Direction

1. Write the plan header, five lines, at the top of the plan and as a comment at the top of the page:
   - **Design read:** "Reading this as: <page kind> for <audience>, with a <vibe> language, leaning
     toward <system or aesthetic>." [v2 §0.B]
   - **Kind and mode:** software, gaming, tech hardware, product, service, or place, plus the visitor
     mode. The kind decides which visuals are allowed: shader effects, loops, counters and dark heroes
     belong to tech kinds; a place (cafe, gym, shop) is carried by photographs (12-20 on a full page); a
     product page shows the product big, whole, and a new picture in each section [taste-skill §1-2].
   - **Main action:** the one transaction the page exists for (Order, Book, Start free trial) [taste-skill].
     On the user's stores the goal is conversion (House rules).
   - **Dials:** VARIANCE / MOTION / DENSITY, 1-10 each, inferred from the brief [v2 §1.A]: calm, minimal,
     editorial 5-6 / 3-4 / 2-3; premium consumer 7-8 / 5-7 / 3-4; playful or agency 9-10 / 8-10 / 3-4;
     default landing 7-9 / 6-8 / 3-5; trust-first, public sector, regulated 3-4 / 2-3 / 4-5; dashboards
     3 / 2-3 / 8-10; redesign-preserve matches the existing site with motion +1.
   - **Direction and signature:** the aesthetic in plain words, plus the one thing a visitor will remember
     [bencium-impact Q4, bencium-innovative "signature relationship"]. Light or dark comes from one
     sentence of use scene (who, where, under what light), not the category [impeccable].
2. Choose the direction in this order: brand assets, a named preset, then the design read choosing from
   the tone menu in `references/style-directions.md` [bencium-impact]; a new world with no brand is
   derived (rut, seven candidates, three directions on the user's review page; playbook) [impeccable]. Run
   `python3 "$UI/members/ui-ux-pro-max/scripts/search.py" "<product> <industry> <vibe>" --design-system --variance V --motion M --density D -p "<Name>"`
   (local, no network). One dominant intent, 2-5 terms; check the result fits the product before using
   it; retry once with a narrower query; a zero-result search is reported as "no match, defaults used",
   never dressed up as data; RTL projects add `--rtl` to style and product queries [ui-ux-pro-max].
3. Break ties with real randomness, never with taste and never with "simulated RNG" prose: the `node -e`
   one-liner in `references/style-directions.md`, or the pipeline's dealers with history [taste-skill,
   bencium-impact]. In Invent mode never roll; form comes from subject evidence [bencium-innovative].
4. If the work drifts safe, use the reframing prompts (designer, context and era lenses), then sweep
   `references/anti-slop.md` [bencium-impact]; a look guessable from the category alone is reworked [impeccable].

### 2. System and tokens

- **Three layers:** primitive values, semantic aliases, component tokens; components never touch raw hex
  [design-system]. CSS variables on `:root`; Tailwind v4 maps them in `@theme`, v3 projects keep
  `tailwind.config` [ui-styling, design-system tailwind-integration].
- **Colour:** 4-5 neutrals, all warm or all cool for the whole project, plus one brand accent (saturation
  under 80%) and semantic status colours that always pair with an icon or text [bencium, v1, stitch,
  ui-ux-pro-max]. The accent is locked across the page [v2]. No pure `#000`/`#fff` surfaces. Hover
  darkens 10-15%; disabled is 40-50% opacity with no hover [bencium]. Strategy first (Restrained,
  Committed, Full palette, Drenched; conflict 13), then tonal ramps 50-950 (OKLCH for new palettes) and
  semantic roles with bg, fg, border and icon variants [impeccable, color-system; scales §1].
- **Contrast at token time:** text 4.5:1, large text (24px, or 18.66px bold) and UI parts or focus
  indicators 3:1, checked in each theme separately [ui-ux-pro-max, v2]; secondary text on a coloured
  surface is tinted from that hue, never grey; simulate colour-vision deficiencies [impeccable, color-system].
- **Dark mode** is designed, not inverted (lighter, desaturated tonal steps); one strategy (Tailwind
  `dark:` or CSS variables); one theme per page, no section flips [v2 §4.11, §8]. Elevation is a lighter
  surface step from a `#121212`-ish ground, accents desaturated 10-20%, text about `#E0E0E0`, borders
  low-opacity white [dark-mode-design]; light text on dark gets more leading and weight (scales §2) [impeccable].
- **Space:** 4px base; the density dial picks the scale: spacious 24-96px, standard 16-64px, dense
  8-32px [ui-ux-pro-max dials]. Space with `gap` on grid/flex wrappers, not margins on children [bencium].
  Spacing jobs: inset, stack, inline, gap; more space above a heading than below [spacing-system, impeccable].
- **Grid:** 4 / 8 / 12 columns on phone / tablet / desktop, gutters 16-32px, margins 16px to 24-48px;
  break it only on purpose; reused components use container queries [layout-grid, impeccable layout].
- **Radius:** one written scale (sharp 0, soft 12-16px, or pill for interactive parts) [v2 shape lock];
  nested surfaces follow outer radius = inner radius + padding [make-interfaces].
- **Elevation:** one shadow scale; a shadow says "this sits above" (popover, modal, raised card), a
  border says "this is separate" or "focused" [make-interfaces, ui-ux-pro-max]. Tint shadows to the
  ground hue [v1]; shadows carry an offset and a soft blur [impeccable].
- **Layers:** a named z-index scale (0 / 10 / 20 / 40 / 100 / 1000 for base, sticky, dropdown, overlay,
  modal, toast); no arbitrary `z-50` [ui-ux-pro-max, v2 §6.F].
- **Persist the system** where the next session finds it: a DESIGN.md (conflict 32 for the format;
  stitch's atmosphere, palette roles, type rules, components, layout, motion and bans fill it), or
  ui-ux-pro-max `--persist -p "<Name>" --output-dir <project-root>` for `MASTER.md` plus `pages/`. Read an
  existing MASTER.md first and never pass `--force` without the user [ui-ux-pro-max, stitch, impeccable]. Mark
  what is fixed, project-specific and adaptable [bencium DESIGN-SYSTEM-TEMPLATE].
- **Verify:** `node "$UI/members/design-system/scripts/validate-tokens.cjs" --dir src/` lists hardcoded
  values [design-system].

### 3. Type

1. **Body text first:** font, size (16-20px on the web; inputs at least 16px so iOS does not zoom), line
   height and measure. Every other style calibrates against these four [typography, bencium].
2. **Faces:** a display face and a text face, two families; a mono only for code or data [typography,
   bencium]. A brand font always wins. Otherwise avoid reflex picks (Inter, Roboto, Arial, Open Sans,
   Space Grotesk as a brand face; Fraunces or Instrument Serif as the reflex serif; impeccable's longer
   list for Persuade pages in `references/anti-slop.md`); a serif needs a reason such as editorial,
   heritage or luxury [bencium-impact, v2 §4.1, impeccable]. Software UIs and dashboards use sans faces
   only and mono numbers from density 8 [v1, stitch]; Inter or system fonts are fine for internal tools
   [v2]. Do not reuse the previous project's pairing. Pairings with imports: ui-ux-pro-max `--domain typography`.
3. **Scale:** ratio 1.25 (calm) or 1.333 (dramatic) from a 16px base on marketing pages, display sizes
   fluid with `clamp()`, at most 6rem; product UI uses 1.125-1.2 on a fixed rem scale (conflict 27);
   mobile sizes 20-30% smaller with fewer levels [bencium, impeccable]. Role ladder and 4-5 sizes in
   regular use: `references/scales-and-systems.md` §3 [typography-scale]. Most heroes sit at text-4xl to
   text-6xl; text-7xl and up only for 3-5 word headlines; the H1 stays within 2 lines on desktop [v2 §4.7,
   gpt-taste]. At most 3 weights per family; build hierarchy from size, weight and colour together [v1].
4. **Spacing:** body line-height 1.45-1.6, UI labels 1.2-1.4, headings about 1.2, display 0.9-1.1
   (italic words with descenders at least 1.1 plus a `pb-1` reserve) [typography, ui-ux-pro-max, v2,
   typography-scale]. Measure 45-75 characters, aim for 65ch, 35-60 on phones, by context in scales §4;
   count a real paragraph (`ch` is approximate); wider columns need more leading [readable-measure].
   Tracking: display -0.02 to -0.04em, body 0, caps and labels +0.05 to +0.12em [typography, bencium].
5. **Rendering:** `text-wrap: balance` on headings and short titles, `pretty` on short body text (never
   on long prose or code); `font-variant-numeric: tabular-nums` on prices, timers, counters and tables;
   antialiased smoothing at the root; kerning on; fonts through `next/font` or self-hosted with
   `font-display: swap`, preloading only critical faces [make-interfaces, typography, ui-ux-pro-max, v2].
6. **Characters**, applied silently to every output: curly quotes and apostrophes, a real ellipsis `…`,
   `×` in dimensions, nbsp in "Fig. 3", "© 2026" and "§ 4", one space after a period, real © ™ ®. In
   JSX text put the actual character or `{'\u2019'}`: a bare `\u2019` escape between tags renders literally
   [typography]. Dashes: When members disagree, item 9.
7. **Emphasis:** bold or italic, never both; all caps only on labels under one line, always letterspaced;
   no underline for emphasis, while links in running text keep an underline or another non-colour cue
   [typography].

### 4. Build

0. **Source before you build** [watermelon-ui; `references/component-sources.md`]. Search common parts
   first: Watermelon (MCP once the user enables it, else its JSON catalog) and Skiper UI's free registry.
   Compare 2-4 against the plan header; read the item JSON (files, targets, dependencies,
   registryDependencies, CSS or env edits, code that fetches or runs); `npx shadcn@<version> add
   @watermelon/<item>` or `@skiper-ui/<item>` in the target project only; restyle to its tokens, icons,
   motion and copy, strip demo content, record source and licence. The user's brands keep their own look
   and the signature moment is designed (conflicts 34-35).
1. **Stack and dependencies.** The existing stack wins. Check `package.json` before any import and print
   the install command first [v1, v2]. Use the official system when the surface demands it (Shopify admin
   app: Polaris; public sector: GOV.UK or USWDS); otherwise shadcn/ui on Tailwind, customised (never its
   default radii, colours and shadows), or plain HTML/CSS for a static page [v2 §2, ui-styling]. One
   design system and one icon family per project (Phosphor for new projects; keep a project's existing
   set; one stroke weight) [v2 §3.C, bencium]. New React motion imports `motion/react` [motion-foundations].
2. **Copy before layout.** Write every visible string first: the h1 names the category and the buyer or
   place; one hard fact on the first screen; a noun in every heading; buttons are a verb plus an object;
   by default a section holds a headline of 8 words or fewer and a sub-paragraph of 25 words or fewer;
   nothing invented (no reviews, logos or figures), assumed facts marked [taste-skill copy.md, v2 §4.9,
   content-design]. The user's or a client's own copy is kept word for word [bencium-innovative].
3. **Plan as screens.** One line per section: id, its one idea, its picture, its layout family
   [taste-skill §4]. Use a layout family once per page, at least 4 families across 8 sections, at most 2
   image/text splits in a row, no generic row of three equal cards, and a bento with exactly one cell per
   item [v2 §4.7]. The hero owns the first screen with its CTA visible, at most 4 text elements and top
   padding no more than pt-24 [v2, taste-skill]. On Persuade pages the first viewport shows the primary
   action in its working form (size picker plus add to cart, open booking slots), not only a link to it,
   and demonstrates something only this product can prove [impeccable mode-persuade].
4. **Layout mechanics.** CSS Grid over flex percentage maths; a max-w-7xl or 1400px container; equal
   left and right content edges [taste-skill]; full-height blocks `min-h-[100dvh]`, never `h-screen`
   [v1]; a declared mobile collapse for every multi-column section (single column under 768px, `w-full
   px-4`) [v1, v2]; no sideways scroll at 320px; safe-area insets on fixed bars; content never hidden
   behind sticky bars [ui-ux-pro-max]. Breakpoints follow the content; column drop, reflow, off-canvas,
   priority+; `srcset` and `<picture>` art direction; hover only under `(hover:hover) and (pointer:fine)`;
   popovers escape clipping parents (`<dialog>`, popover API, portal) [responsive-design, impeccable].
5. **Hierarchy.** Four levels (title and main action; section heads; supporting text; fine print) built
   from size (about 1.5x apart), weight, contrast, space, position and isolation together; one primary
   action per view; the squint test passes [visual-hierarchy, impeccable layout].
6. **Every state, every component:** default, hover, focus-visible, active (`scale(0.96-0.98)` or a 1px
   drop), disabled, loading (a skeleton shaped like the result; buttons disabled during async work),
   empty (what this area is for plus the next step), error (inline: what happened, then what to do),
   success [v1 rule 5, content-design, ui-ux-pro-max, impeccable].
7. **Forms:** visible label above, optional helper, error below linked with `aria-describedby`, input
   kept on error, a focused and linked error summary after a multi-error submit [bencium,
   ui-ux-pro-max pro-rules]. Fields that send on Enter stay IME-safe (preflight §8) [ui-ux-pro-max #120].
8. **Images and visuals.** Order of sources: the user's or the client's real assets; free licensed stand-ins,
   listed in the report (taste-skill's `photos.mjs` searches Wikimedia Commons); picsum seeds only in
   throwaway drafts; paid generation only after the user says yes [taste-skill, v2 §4.8, House rules]. No
   div-built fake screenshots: show the product's real UI as live HTML in one app frame [taste-skill, v2].
   Declare width and height or `aspect-ratio`, serve WebP/AVIF, give the hero priority, lazy-load the
   rest [ui-ux-pro-max]. Never draw a look-alike of a real logo [taste-skill]. Demo data is labelled
   synthetic; prices, customers and benchmarks are never invented [impeccable]. Illustrations follow one
   written style guide (scales §7) and never carry information alone [illustration-style].
9. **Accessibility built in:** landmarks, one h1, no skipped heading levels, native `button`/`a`/`input`
   before a `div` with `tabindex`, a skip link as the first Tab stop, a visible focus ring (2-4px, 3:1),
   names on icon buttons, alt text (empty alt on decorative images), colour never the only signal, touch
   targets 44x44 (WCAG floor 24x24) with 8px gaps, modals with focus trap, Esc, scroll lock,
   `role="dialog"` and `aria-modal` [ui-ux-pro-max, motion-patterns, bencium]. Deeper checks in step 6.
10. **Performance budget:** LCP under 2.5s, INP under 200ms, CLS under 0.1 [v2 §6.D]; `backdrop-filter`
   only on fixed or sticky layers; grain only on a fixed `pointer-events:none` layer; Motion, GSAP and
   Three lazy-loaded below the fold [soft, v1, v2]. Measure before and after any optimisation [impeccable].

### 5. Polish and motion

**Motion budget.** By default a page moves in three places: the hero enters once on load (about 1.1s,
then it stands), one memorable moment in a section of its own (two on pages with 8+ sections), and a
hover/press layer on every link, button, linked card and photo (cards lift 2px, photos zoom 1.02-1.03
inside their frame, buttons press) [taste-skill motion.md]. Give each motion a one-line purpose (guide
attention, show a state change, keep spatial continuity, acknowledge an action) and cut any that only
"looks cool" [motion-foundations, v2 §5]. The memorable moment comes from this product's concept; a
generic fade-and-rise is not one [impeccable animate]. The page reads completely at rest, without script.

| Token | Duration | Use |
|---|---|---|
| instant | 80ms | tooltip, focus ring, badge update |
| fast | 150-180ms | button feedback, icon swap, hover, chip toggle |
| normal | 250-350ms | modal, card expand, tab switch, element enter |
| slow | 500-600ms | hero entrance, full-page transition (an authored focal entrance may run to 800ms) |

Exits run at 60-70% of the enter time (about 150ms) with a small fixed offset (about -12px), never the full
height unless position matters (drawer, card back to its list) [ui-ux-pro-max, make-interfaces]. Ease-out to enter,
ease-in to leave, linear only for constant loops [bencium]. Curves: smooth `[0.22,1,0.36,1]`, sharp
`[0.4,0,0.2,1]`, confident arrival `cubic-bezier(0.16,1,0.3,1)`; no bounce or elastic by reflex
[impeccable]; springs come from one map: snappy 300/30, gentle 120/14, bouncy 400/10, instant
600/35, release 200/20 (stiffness/damping) [motion-foundations]. Split entrances into semantic groups
(title, text, actions) about 100ms apart, headline words about 80ms, list items 40-80ms; the whole
sequence stays under 1s [make-interfaces, motion-patterns, ui-ux-pro-max, bencium-impact].

**Library choice.** CSS transitions for hover and state changes (they retarget when the user changes
their mind mid-motion) and keyframes for one-shot entrances [make-interfaces]; `motion/react` for React
presence, layout and gestures [motion-foundations, motion-patterns]; View Transitions for continuity
between states or pages [impeccable]; GSAP with ScrollTrigger only for
pin, scrub and horizontal pan, inside `gsap.context` with cleanup and `start: "top top"` (skeletons in
v2 §5.A-5.B); Three/WebGL isolated in its own leaf. Never mix GSAP or Three with Motion in one
component tree [v1, v2].

**Hard rules.**
- Animate `transform` and `opacity` only, never `box-shadow` or `filter` in a loop. Exceptions: a small disclosure panel (grid rows
  `0fr` to `1fr`, or Motion `layout` on a subtree of 5 or fewer children), and a one-shot bounded effect
  (clip-path or mask reveal, small blur) on an isolated region that stays smooth on the target device
  (conflict 25); never squash text with `scaleY` [motion-foundations, motion-patterns, impeccable].
- Never `transition: all` or `will-change: all`; `will-change` only on elements animating now, removed
  after [make-interfaces, antigravity].
- SSR: `initial` equals what the server renders; `"use client"` on every motion file; no `window` or
  `navigator` at module level [motion-foundations].
- AnimatePresence needs the wrapper, a keyed direct child and an `exit`; page swaps use `mode="wait"`;
  `layout` only on small subtrees (about 5 children), `layout="position"` on text inside [motion-patterns].
- No `window.addEventListener('scroll')` and no scroll position in React state; use IntersectionObserver,
  `useScroll`, ScrollTrigger or CSS `animation-timeline`; pointer-driven values use `useMotionValue`,
  never `useState` [v2 §5.D, v1].
- Scroll reveals are rare, `once: true`, never on every section; no parallax on text, no scroll-jacking
  [taste-skill, motion-patterns].
- Anything moving longer than 5s gets a pause control; at most one marquee per page, pausing on hover and
  focus [taste-skill, v2, bencium-impact]. Non-essential loops stop when offscreen or hidden [impeccable].
- Reduced motion: transforms off, opacity fades at 200ms or less, loops, parallax and pins collapse to
  their end state, nothing stays hidden, and feedback that confirms an action stays legible (no global
  0.01ms kill) [motion-foundations, gpt-taste, v2, impeccable]. Gate decorative motion off
  on low-end devices (`hardwareConcurrency <= 4`) [motion-foundations].

**Polish pass** [make-interfaces unless noted; code in its `surfaces.md`, `animations.md`]: concentric
radii (past 24px of padding pick each radius on its own); icons optically centred (play triangles 2px
right, the icon side of a button 2px less padding); shadows for depth, borders for separation and focus
(conflict 36); images get a 1px inset outline in pure black at .1 (white at .1 in dark), never slate,
zinc or brand-tinted; press `scale(0.96)`, never below 0.95, with a `static` opt-out; small controls get
a pseudo-element hit area, shrunk only where it would overlap a neighbour; icon swaps: scale .25 to 1,
opacity, blur 4px to 0, spring 0.3s bounce 0, or a CSS cross-fade with both icons in the DOM when the
project has no motion library (never add one for this); `AnimatePresence initial={false}` on toggles,
tabs and icon swaps, never on staged entrances; balanced headings; tabular numbers; browser surfaces themed from the palette
(`::selection`, `caret-color`, scrollbars, focus ring, `text-underline-offset`) [impeccable craft floor].
Atmosphere only where the direction asks for
it, using the grain, mesh and orb parameters in `references/style-directions.md` [bencium-impact]. Glass
only in glass-friendly directions: a 1px inner border and inset highlight, a solid fallback under
`prefers-reduced-transparency`, and contrast that holds without the blur [v1, v2 appendix C]. A larger
polish job follows impeccable's triage order (`references/impeccable-playbook.md`) [impeccable polish].

### 6. Audit and ship

1. **Look at it.** Render at 1440, 1024, 768 and 390 and walk 320 for overflow, in both themes and with
   reduced motion on. Use the pipeline's checkers in Company-site mode, otherwise Playwright MCP headless
   screenshots. Read every screenshot against the plan header [taste-skill, ui-ux-pro-max, v2 §8.D].
   Drive the states too (hover, focus, open, error, empty, overlong); two looking rounds, fixes batched
   between them [impeccable].
2. **Copy self-audit.** Re-read every visible string and rewrite broken grammar, unclear referents,
   cute-but-wrong lines and tells [v2 §4.9, taste-skill copy-tells].
3. **Preflight.** Run `references/preflight.md` in its priority order: accessibility, touch, performance,
   style, layout, type and colour, motion, forms, navigation, charts, hardening [ui-ux-pro-max, impeccable].
4. **Accessibility.** Run web-a11y's scan on the running page, fix the mechanical findings, walk the
   keyboard (`~/.claude/skill-library/design/web-a11y/SKILL.md`).
5. **Code review** (when asked, or on a PR): WebFetch Vercel's Web Interface Guidelines and report terse
   `file:line` findings [web-design-guidelines]; run `validate-tokens.cjs`.
6. **Finish review** (launch pages, big redesigns, or when the user asks; otherwise one self-check against
   `references/preflight.md`, because the extra pass doubled time and tokens in evals): a fresh no-history subagent, prompted with
   `members/impeccable/reference/degraded/finish-reviewer.md`, reviews the screenshots against the plan
   header and anti-slop list; report its word (ship, fix, rebuild, recapture) as given [impeccable].
7. **Report.** Audits use design-audit's phases: Critical (hurts use or breaks consistency), Refinement
   (below professional standard), Polish (works, not yet premium); each finding is "what's wrong → what
   it should be → why it matters", with implementation notes exact enough to build without
   interpretation (file, component, property, old value → new token) [design-audit]. Technical audits add
   impeccable's five 0-4 scores (/20) [impeccable audit]. Polish passes use before/after tables grouped by
   principle, every change listed, untouched ones omitted [make-interfaces]. Sourced components are
   listed with source, licence and new dependencies. Always say what you could not check.
8. **Redesign protocol** (live products): `references/redesign-protocol.md`, audit first, ordered levers,
   nothing changed silently, reduction filter, the user's review page before any build [v2 §11, design-audit].

## Core rules and checklists

**UI copy** [content-design, typography, v2, taste-skill, impeccable clarify]: `references/ui-copy.md`, applied in
step 4.2 and the step 6.2 self-audit: sentence case, buttons a verb plus an object in 3 words or fewer,
errors say what happened and what to do, empty states give the next step, "Loading orders…", "Order saved".

**Honest content** [v1, v2, taste-skill, impeccable]: realistic names, no fake-perfect numbers, no invented
specs, reviews or logos; stand-ins, synthetic demo data and assumed facts listed in the report; no emoji
as icons or in UI copy.

**Anti-slop:** the merged tell list with replacements is `references/anti-slop.md` (impeccable's Refuse
list and AI-look calibration included). The ten that matter most: AI purple and the beige-brass premium
palette by default; reflex fonts; centered hero plus three equal cards; eyebrows; hero clutter (badges,
version tags, trust strips); div-built fake screenshots; invented data; slop words that replace facts;
em-dash pauses; fade-in on every scroll.
**Before delivery:** `references/preflight.md`, the merged checklist.


**Eval lessons (graded runs):**
- The brief's voice is a requirement, not decoration: if it asks for humor or personality, it shows in the headline, microcopy,
  empty and success states. Rigor never replaces it (the old picks won on voice).
- What the brief names as the point (countdown, buy or book action, signup) sits inside the first phone screen.
- One h1 per page; no dev-only controls (state switchers, "prototype" buttons) in the shipped UI; use `?state=` URLs instead.
- Browser checks run in your own headless Chrome on a private port and profile; never attach to an existing debugging port,
  which can be another session's browser.

## When members disagree

1. **Ask or commit.** controlled: always ask first; impact: ask context, then commit boldly; innovative:
   zero preliminary questions; v2: one question only if readings diverge; design-audit: present the
   plan, wait. **Rule:** greenfield work asks nothing, states the design read and builds; ask exactly one
   question only when two plausible readings would produce opposite work. Changes to a live product go
   through the user's review page first. Controlled mode only when the user asks for it or brand stakes are real.
2. **Fonts.** impact bans Inter, Roboto, Arial, Space Grotesk; v1 and stitch ban Inter; v2 only
   discourages it; brutalist lists Inter Black; impeccable adds Playfair, DM Sans, IBM Plex and more on
   Persuade pages. **Rule:** brand font first; reflex fonts are avoided on brand and marketing pages;
   internal tools may use Inter or system fonts; inside a preset its list wins.
3. **Serif.** minimalist and stitch recommend Instrument Serif or Fraunces; v2 bans both as reflexes and
   discourages serif by default. **Rule:** a serif needs a stated reason; when one is justified, pick from
   v2's rotation pool (v2 §4.1) and do not repeat the last project's.
4. **Depth.** controlled wants flat, no shadows, no glass; impact wants dramatic shadows but no glass;
   antigravity and soft are built on glass and soft shadows. **Rule:** depth is a property of the
   direction: flat by default, one shadow scale always, glass only in glass directions with fallbacks.
5. **Centered hero.** v1, v2 and stitch ban it above variance 4; gpt-taste prefers "cinematic center".
   **Rule:** variance 4 or less, or a manifesto or launch page, may centre; otherwise asymmetric, unless
   the gpt-taste preset is chosen.
6. **Randomness.** impact rolls dice; gpt-taste simulates RNG; taste-skill deals with history; innovative
   forbids dice and matrices; impeccable rolls with its engine. **Rule:** the brief decides first; real
   randomness only breaks ties on open briefs; no simulated RNG; none in Invent mode (see also 24).
7. **Scroll reveals.** minimalist, soft, v1 and gpt-taste reveal everything on scroll; taste-skill bans
   stock reveals; v2 asks for motivated motion. **Rule:** the motion budget in step 5; a preset may add
   reveals with `once: true`, never on the CTA, price or form, and never under reduced motion.
8. **Perpetual loops.** v1 and stitch loop every card; v2 says not every card; taste-skill allows loops
   only on tech pages at 2.5-4s. **Rule:** loops only where they show live state, tech kinds only outside
   presets, a pause control past 5s.
9. **Dashes.** typography wants real en and em dashes; v2 bans both as AI tells. **Rule:** no em dash in
   new copy (restructure the sentence); en dash only in numeric ranges in typeset content, hyphens in UI
   labels; never `--`; the user's or a client's own copy keeps its punctuation.
10. **Icons and SVG.** controlled and impact use Phosphor; minimalist bans Lucide, Feather, Heroicons;
    soft bans thick strokes; v2 discourages Lucide and bans hand-rolled SVG icons; ui-ux-pro-max accepts
    Heroicons and Lucide; innovative never writes SVG. **Rule:** keep the project's set (shadcn projects
    often ship Lucide); Phosphor for new ones; no hand-drawn icons or logos; the no-SVG law applies in
    Invent mode only.
11. **Images.** gpt-taste, minimalist, v1 use picsum; v2 says use an image generator first; taste-skill
    wants real or licensed stand-in photos; impeccable says ship real imagery the brief implies. **Rule:**
    step 4.8 order; image generation is paid, so the user says yes first.
12. **Dark mode.** v2 makes both modes mandatory for consumer pages; taste-skill keeps dark grounds for
    tech kinds; impeccable picks from the use scene; dark-mode-design wants a toggle. **Rule:** apps and
    dashboards ship both modes through tokens, follow `prefers-color-scheme` and offer a toggle; a
    marketing page picks the one theme its brand and use scene call for, locked page-wide.
13. **Accent count and colour dosage.** bencium allows 1-3 accents; v1 and stitch one; impeccable offers
    Committed and Drenched. **Rule:** one brand accent plus status colours; the strategy sets how much
    surface it owns; Operate and Read stay Restrained; bolder strategies only where the brand carries them.
14. **Line height.** typography says 1.2-1.45 (print-derived); ui-ux-pro-max 1.5-1.75; minimalist 1.6;
    typography-scale 1.2 headings, 1.5 body, 1.75 long-form. **Rule:** step 3.4 ranges; the page must also
    survive WCAG 1.4.12's 1.5 spacing override.
15. **Custom cursors.** impact suggests them; v1, v2, stitch ban them. **Rule:** none; use `pointer`,
    `grab`, `grabbing` semantics only.
16. **Target size.** 44x44 (ui-ux-pro-max, bencium, taste-skill, responsive-design), 40 minimum
    (make-interfaces), 24x24 (WCAG 2.5.8). **Rule:** design to 44, audit failures at 24.
17. **framer-motion vs motion/react.** bencium imports `framer-motion`; motion-foundations forbids it.
    **Rule:** `motion/react` in new code; leave an existing project's imports unless migrating it whole;
    never both in one tree.
18. **Inspiration.** controlled and impact send you to Awwwards, Framer and studios; innovative forbids
    contemporary references while inventing. **Rule:** references are fine in Build mode for mechanisms,
    never copied code, copy or signature effects; none in Invent mode.
19. **Full-height sections.** v1 and v2 use `min-h-[100dvh]`; taste-skill fixes sections at 1-2 screens
    of `svh` and bans `dvh`. **Rule:** inside the pipeline its `system.css` rules; elsewhere `min-h-[100dvh]`.
20. **Eyebrows.** soft puts one above every heading; v2 caps them at one per three sections; impeccable
    bans kickers outright. **Rule:** none by default; a named preset or the user's brief may bring them back,
    capped at one per three sections.
21. **Underlines.** typography says never underline; links need a non-colour cue (WCAG 1.4.1). **Rule:**
    no underline for emphasis; links in running text keep a thin offset underline.
22. **Built-in frontend-design.** The always-on plugin shares bencium-impact's stance (intent over
    templates). **Rule:** when both fire, follow this workflow; nothing in it contradicts the plugin.
23. **Questions first.** impeccable asks 2-3 product questions before new work. **Rule:** item 1 holds;
    with the user present and the audience or proof missing, ask those in one round, never aesthetic ones.
24. **Engine.** impeccable runs `scripts/impeccable` (concept-seed, decision page, detect, hooks, live); the
    this copy has none. **Rule:** skip and name engine steps; directions go on the user's review page; no
    engine download, hooks or live mode without their yes.
25. **Animated properties.** motion-foundations and make-interfaces: transform and opacity only;
    impeccable: also blur, clip-path, mask. **Rule:** step 5 hard rule 1; loops stay on transform/opacity.
26. **Spacing base.** spacing-system allows 4 or 8px; ui-ux-pro-max and impeccable use 4. **Rule:** 4px.
27. **Type ratio.** bencium and typography-scale use 1.25/1.333; impeccable Operate 1.125-1.2 fixed rem.
    **Rule:** marketing 1.25-1.333 with fluid display; product UI and dashboards 1.125-1.2, fixed rem.
28. **Display tracking.** bencium goes to -0.05em; impeccable floors at -0.04em. **Rule:** -0.02 to -0.04em.
29. **Dark elevation.** dark-mode-design lightens surfaces instead of adding shadows. **Rule:** in dark
    themes elevation is a lighter surface step; shadows only supplement it.
30. **Finish authority.** impeccable finishes the job and reviews itself; the user's protocol wants review
    cards. **Rule:** greenfield finishes fully; live or shared projects build only the user's picks, then review.
31. **Ownership.** impeccable `critique` and `onboard` overlap ux-lab and conversion-lab. **Rule:** ux-lab
    leads critiques and usability tests, conversion-lab onboarding strategy and A/B tests; ui-studio builds
    the screens and runs impeccable critique only as a self-check on its own build.
32. **DESIGN.md format.** stitch writes seven prose sections; impeccable `document` writes the official spec
    (YAML tokens, then Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and
    Don'ts). **Rule:** new files use the official spec with stitch's content inside; existing files keep theirs.
33. **Breakpoints.** layout-grid 375/768/1024/1440, responsive-design 640/1024/1440. **Rule:** content
    decides (the project's Tailwind set if any); the step 6 render sizes stay as the check.
34. **Source or build.** watermelon-ui searches before writing; bencium-innovative and impeccable derive
    form from the subject. **Rule:** source utility parts and common sections (a block is a start); the
    signature moment, Invent mode and code-drawn brand scenes are designed; restyle until it fits.
35. **Library look vs the project.** Items bring their own palette, icons (react-icons, lucide, Hugeicons),
    `framer-motion`, `transition-all`, Lenis and demo copy. **Rule:** the project's tokens, icons, `motion/react`
    (17), step 5 rules and copy win; Watermelon's `-base` variant first; Lenis is scroll-jacking, left out.
36. **Shadows or borders.** make-interfaces swaps card and button borders for a shadow ring. **Rule:** cards and
    bordered buttons may use `--shadow-border`; dividers, cells, inputs and hairlines keep borders; dark: one ring.

## Combine with

- **Built-in skills:** `frontend-design:frontend-design` (always on; same intent), `anthropic-skills:theme-factory`
  (themes for artifacts, docs, decks), `dataviz` (charts, KPI tiles, dashboards), `artifact-design` (when
  the output is a claude.ai artifact).
- **Superpowers:** `superpowers:brainstorming` before creative work bigger than a component;
  `superpowers:verification-before-completion` before calling it done (screenshots and check output are
  the evidence).
- **Agents:** the built-in `design-review` agent type for a Playwright-driven review of a live UI change;
  a fresh general-purpose agent prompted with impeccable's `degraded/finish-reviewer.md` for the finish review.
  Voltagent prompts under `~/.claude/skill-library/agents/voltagent/` (Read the file, pass it as the Agent
  prompt): `01-core-development/ui-designer.md` (visual systems), `01-core-development/frontend-developer.md`
  (multi-framework builds), `01-core-development/design-bridge.md` (DESIGN.md into build instructions),
  `02-language-specialists/nextjs-developer.md` (App Router builds), `04-quality-security/ui-ux-tester.md`
  (flow-driven UI testing), `08-business-product/ux-researcher.md` (evidence for layout and conversion).
- **MCP servers (off until the user adds them):** Watermelon (`https://mcp.watermelon.sh/mcp`, read-only, no key) and the
  official shadcn MCP; review notes and the command for the user in `references/component-sources.md` §6.
- **Sibling super-skills:** `../ux-lab` (UX laws, interaction patterns, critique, usability tests: reviewer
  of ui-studio builds), `../web-a11y` (accessibility), `../dashboard-studio` (charts), `../brand-studio`
  (logos, identity), `../media-studio` (images, video, Higgsfield), `../react-next-pro`, `../commerce-pro`
  (Shopify), `../conversion-lab` (A/B tests, onboarding), `../copy-and-content`,
  `../mobile-app-studio` (platform conventions), `../docs-decks`.

## House rules (the user)

- Stores and landing pages convert first: every section and layout choice answers "does this get more
  people to buy?", backed by conversion evidence (Baymard, NN/g, GoodUI, web.dev); cut sections that only
  explain how shopping works; keep playful moments only where they push toward buying.
- Paid image or video generation (gpt-image-1, fal, Higgsfield and similar), paid stock, and anything that
  publishes, deploys or pushes to a live site (Vercel production, Shopify theme publish) ask the user first; his
  own photos or free licensed stand-ins come first.
- Brand scenes drawn in code can be the signature; AI photos and video (Higgsfield) are optional, no stock images; credits still need the user's yes.
- APIs, CLIs and headless scripts before browser automation; if the user's own Chrome must be driven, say why
  in one line.
- Changes to a live site, app or dashboard go through a review page: one card per change, old and new side
  by side, the user picks, only the picks get built.
- Dashboard redesigns never drop a metric, chart or table; ops dashboards keep their existing style: dense, big
  numbers, no gimmicks.
- the user's home address never appears on a public page; demo contacts use `.example` and street plus district
  only.
- New packages, plugins or MCP servers: versions pinned, `npm --cache /tmp/npm-cache` if the default cache fails, dev servers on a free port.
- Third-party components stay free and reviewed: Skiper UI Pro ($129 / $549), any paid kit or licence key,
  and adding an MCP server to Claude's config are the user's decision; new npm dependencies in a live project go
  through the normal build flow and review page.
- Skiper UI free items: allowed on their sites with a small footer or credits-page credit ("UI components:
  Skiper UI"); check each item for look-alike designs before using it on a brand site.

## Members

| Member | Best at | Path |
|---|---|---|
| ui-ux-pro-max | Searchable local database (80 styles incl. Apple Native Experience, 192 product palettes, 74 pairings, 120 UX rules, 22 stacks), `--rtl` filter for style and product, design-system generator with dials and MASTER.md persistence, priority-ordered rules, app pre-delivery checklist | `members/ui-ux-pro-max/SKILL.md` |
| bencium-controlled-ux-designer | Collaborative ask-first mode, colour architecture, UI type specs, UX principles, design-system template, motion timing tables | `members/bencium-controlled-ux-designer/SKILL.md` |
| bencium-impact-designer | Bold direction: ~40 tone extremes, reframing prompts, force-variety dimensions, atmosphere effect parameters, rule-breaking checklist | `members/bencium-impact-designer/SKILL.md` |
| bencium-innovative-ux-designer | Original visual languages: evidence-only isolation, ten typography-only HTML directions, explicit lock, Round 2 production and style guide | `members/bencium-innovative-ux-designer/SKILL.md` |
| design-audit | 15-dimension visual audit, reduction filter, phased plan template with exact implementation notes, visual-only scope | `members/design-audit/SKILL.md` |
| make-interfaces-feel-better | Design-engineering polish with code in `surfaces.md`, `animations.md`, `typography.md`, `performance.md`: concentric radius, optical alignment, shadow-as-border ring, neutral image outlines, icon-swap values, press scale, `initial={false}`, transition scope, hit areas, before/after tables (Watermelon copy) | `members/make-interfaces-feel-better/SKILL.md` |
| typography | Butterick's rules enforced silently: characters, spacing, emphasis, layout, the JSX escape trap, CSS baseline, entity table | `members/typography/SKILL.md` |
| ui-styling | shadcn/ui + Tailwind implementation references (components, theming, accessibility, responsive, customisation) | `members/ui-styling/SKILL.md` |
| design-system | Three-layer token architecture, component specs and states, Tailwind integration, token validator | `members/design-system/SKILL.md` |
| web-design-guidelines | Code review against Vercel's live Web Interface Guidelines, terse `file:line` output | `members/web-design-guidelines/SKILL.md` |
| content-design | UI copy patterns, tone, grammar and an audit grep table (n8n-specific parts apply only in n8n) | `members/content-design/SKILL.md` |
| antigravity-design-expert | Spatial preset: weightless glass layers, isometric tilt, GSAP ScrollTrigger floats, parallax | `members/antigravity-design-expert/SKILL.md` |
| motion-foundations | motion/react tokens and springs, `shouldAnimate` gate, reduced-motion priority, SSR hydration safety | `members/motion-foundations/SKILL.md` |
| motion-patterns | Copy-paste motion/react patterns: button, stagger, modal, toast, page transition, scroll reveal, layout, layoutId | `members/motion-patterns/SKILL.md` |
| taste-skill | Company-site pipeline 2.5: kinds, page plans, kit, dealt choices, copy layer and lint, browser checkers, finish gate | `members/taste-skill/SKILL.md` |
| taste-brutalist-skill | Industrial brutalist preset (Swiss print or CRT telemetry) | `members/taste-brutalist-skill/SKILL.md` |
| taste-gpt-tasteskill | Motion-rich AIDA landing preset with GSAP and gapless bento | `members/taste-gpt-tasteskill/SKILL.md` |
| taste-minimalist-skill | Editorial minimalist preset (warm monochrome, spot pastels, flat bento) | `members/taste-minimalist-skill/SKILL.md` |
| taste-soft-skill | Soft premium preset (double bezel, island nav, spring motion) | `members/taste-soft-skill/SKILL.md` |
| taste-stitch-skill | DESIGN.md writer for Google Stitch and agent handoff | `members/taste-stitch-skill/SKILL.md` |
| taste-taste-skill-v1 | High-agency React preset: dials 8/6/4, Bento 2.0, creative arsenal | `members/taste-taste-skill-v1/SKILL.md` |
| taste-taste-skill-v2-experimental | Dial-driven anti-slop rules, design-system map, redesign protocol, GSAP skeletons, 50-line preflight | `members/taste-taste-skill-v2-experimental/SKILL.md` |
| impeccable | Visitor modes (Persuade, Operate, Read, Experience), craft floor and Refuse list, colour strategies, new-world derivation and direction contract, 24 command playbooks (polish, bolder, quieter, distill, harden, typeset, layout, audit...), fresh-eyes finish review; engine not installed | `members/impeccable/SKILL.md` |
| color-system | Colour system layers: tonal ramps 50-950, neutrals, semantic roles with bg/fg/border/icon variants, extended palette, colour-blind checks | `members/color-system/SKILL.md` |
| dark-mode-design | Dark palette from a light one: surface elevation ladder, 10-20% desaturation, off-white text, image and logo variants, toggle | `members/dark-mode-design/SKILL.md` |
| typography-scale | Modular type role ladder (12-64px), weights, line-height and tracking tiers, 4-5 sizes in use | `members/typography-scale/SKILL.md` |
| spacing-system | Spacing scale and jobs (inset, stack, inline, gap), density modes | `members/spacing-system/SKILL.md` |
| layout-grid | Columns, gutters, margins per breakpoint; column, modular, baseline and compound grids | `members/layout-grid/SKILL.md` |
| readable-measure | Line length by context with `ch` caveats and per-column rule | `members/readable-measure/SKILL.md` |
| responsive-design | Responsive strategies and patterns (column drop, reflow, off-canvas, priority+), input-method adaptation, art direction | `members/responsive-design/SKILL.md` |
| visual-hierarchy | Six hierarchy tools, four levels, squint test, one primary action per view | `members/visual-hierarchy/SKILL.md` |
| illustration-style | Illustration style guide: style axes, palette subset, characters, types and use rules | `members/illustration-style/SKILL.md` |
| watermelon-ui | Source-first workflow for free MIT React/Tailwind UI (849 entries): read-only MCP (search, get_inspiration, get_component, compose_page), kinds to pick from, adapt to the project's system | `members/watermelon-ui/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
