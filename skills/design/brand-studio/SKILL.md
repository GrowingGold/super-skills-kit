---
name: brand-studio
description: Build, document or apply a brand. Identity and rebrands, positioning and messaging (mission, value prop, positioning, key messages, elevator pitches, taglines), voice and tone (profile from real writing samples, or a trait chart), logos and wordmarks as code-drawn SVG concepts, numbered iterations and PNG, favicon and app-icon export, palette, type scale, design tokens synced to CSS and Tailwind, brand guidelines, corporate identity mockups (card, letterhead, signage, merch), SVG icon sets, themes for decks, docs and pages (10 presets or custom, Anthropic look on request), consistency audits and asset approval. Use for - brand, rebrand, brand kit, style guide, visual identity, logo, make me a logo, iterate on this logo, wordmark, favicon, palette, fonts, tokens, tone of voice, write in my voice, value prop, CIP, icon set, theme this deck, apply our branding, on-brand check. Banners and social images go to media-studio, slides to docs-decks, app UI systems to ui-studio.
members: [brand, design, brand-voice, brand-guidelines, theme-factory, logo-designer]
---

# Brand Studio

One entry point for brand strategy, voice, visual identity, logos, tokens, guidelines and theming. It merges the
claudekit `brand` system (frameworks, checklists, token sync scripts), the claudekit `design` umbrella (logo, CIP and
icon generators with style databases), ECC `brand-voice` (source-derived voice profiles), Anthropic `brand-guidelines`,
Anthropic `theme-factory` and neonwatty `logo-designer` (the code-drawn SVG concept, iterate and export loop). Load this first, pick a mode, follow the workflow from the step the mode names, and open a
member file only when a route says so. `members/<name>/` points at the original skill folder; in shell commands write
it as `<skill>/members/...`, where `<skill>` is `~/claude-code-resources/powerup-sources/growing-gold_super-skills/brand-studio`.

## Pick the mode

| Task looks like | Mode | Start at / open |
|---|---|---|
| New brand, rebrand, "brand kit for X" | IDENTITY | Whole workflow, steps 0-11 |
| Positioning, value prop, key messages, elevator pitch, tagline | MESSAGING | Step 2; `members/brand/references/messaging-framework.md` |
| "Write like me / like this brand", tone guide, voice profile | VOICE | Step 3; schema in `members/brand-voice/references/voice-profile-schema.md`, traits method in `members/brand/references/voice-framework.md` |
| Logo, wordmark, brand mark, logo refresh, "make me a logo" | LOGO | Steps 0, 4, 7 + "Logo SVG loop"; `members/logo-designer/SKILL.md` (preview template, size strip); style data in `members/design/references/logo-design.md` (+ `logo-style-guide.md`, `logo-color-psychology.md`, `logo-prompt-engineering.md`) |
| "Iterate on this logo", tweak an existing SVG mark | LOGO-ITERATE | Step 7d; "Logo SVG loop" (iterations, groups, size strip) |
| Export a logo, favicon, app icon; put a new logo into a repo | LOGO-EXPORT | Step 7g; "Logo SVG loop" export and repo hand-off |
| Palette, fonts, type scale, design tokens, CSS variables | TOKENS | Steps 0, 5, 6, 8; `members/brand/references/color-palette-management.md`, `typography-specifications.md`, `update.md` |
| Brand guidelines / brand book / style guide document | GUIDELINES | Step 9; `members/brand/templates/brand-guidelines-starter.md` |
| Business card, letterhead, signage, merch, office mockups | CIP | Step 10; `members/design/references/cip-design.md`, `cip-deliverable-guide.md`, `cip-style-guide.md` |
| Icon set in SVG | ICONS | Step 10; `members/design/references/icon-design.md` (SVG rules) |
| "Theme this deck / doc / page", no brand yet | APPLY-THEME | Theme rules below; `members/theme-factory/themes/<theme>.md`, `members/theme-factory/theme-showcase.pdf` |
| Apply an existing brand to an artifact | APPLY-BRAND | Brand-application recipe below (generalized from `members/brand-guidelines/SKILL.md`) |
| Anthropic look and feel requested | ANTHROPIC | `members/brand-guidelines/SKILL.md` exactly |
| Check an asset or channel is on brand; approve before publishing | AUDIT | Step 11; `members/brand/references/consistency-checklist.md`, `approval-checklist.md` |
| Organize, name, version brand assets | ASSETS | `members/brand/references/asset-organization.md` |
| Banner, social graphic, OG image, campaign visuals | elsewhere | media-studio (feed it the brand's AI-image base prompt from step 9) |
| Slides or pitch deck | elsewhere | docs-decks (apply the theme from this skill) |
| Component styling, app design system, shadcn/Tailwind UI | elsewhere | ui-studio |

## Unified workflow

0. **Inventory before creating.** Look for `docs/brand-guidelines.md`, `assets/design-tokens.*`, `:root` custom
   properties, Tailwind v4 `@theme` or a Tailwind config/preset, logo files, `.agents/product-marketing.md`, site copy
   and past posts. If a token source exists, extend it; a second, parallel token system is the most common way brands
   drift [brand sync detection]. Note what is missing; that list is the job.
1. **Brief.** Audience, category, 2-3 competitors, price position, and the one action the brand must drive (for a
   store: buy). Use `superpowers:brainstorming` for new identities and the competitive-analyst agent for competitor
   brand audits [new].
2. **Messaging** [brand messaging-framework]. Fill, in order: mission ("We [action] for [audience] by [method] so they can
   [outcome]"), vision ("A world where..."), value proposition ("For [target] who [need], [brand] is a [category] that
   [benefit]. Unlike [competitors], we [differentiator]"), positioning ("[Brand] is the [category] for [audience] who
   want [outcome] because [reason to believe]"), one primary message, 3-5 supporting messages each with audience need
   and proof point, elevator pitches at 10 / 30 / 60 s, and a message-by-audience table (pain, message, CTA). Test every
   line: clear, differentiated (a competitor could not say it), credible (provable), compelling, consistent.
3. **Voice** (merge rule in "When members disagree"). With 5-20 real samples: extract rhythm, sentence length,
   compression, capitalization, parentheticals, question use, claim style, use of numbers and receipts, transitions and
   what the author never does; split public vs private voice if the samples split [brand-voice]. Without samples:
   choose 3-5 traits written as "X, not Y", place the brand on four spectrums (formal-casual, simple-complex,
   serious-playful, reserved-expressive), write a Do/Don't chart and context shifts (social more casual, support more
   empathetic, legal more formal, sales more confident) [brand voice-framework]. Output one unified VOICE PROFILE
   (template below) and run drafts through the `humanizer` skill.
4. **Visual direction.** Draft 2-3 directions, each a mood (3-5 keywords), color logic from industry psychology
   [design logo-color-psychology], a type pairing and an imagery style (photo vs illustration, lighting, subject).
   Put them side by side on one review page for the user's pick (house rules). Build only the picked direction.
5. **Palette** [brand color-palette-management]. Primary 1-2 (CTAs, headers), secondary 2-3 (accents, illustration),
   neutrals 3-5 (backgrounds, text, borders), semantic 4 (success, warning, error, info), used roughly 60/30/10
   (neutral / primary / accent) [brand approval-checklist]. Give each hex, RGB and, if
   print matters, CMYK, plus tints/shades. Check contrast with the WCAG luminance formula: text 4.5:1 (AA), large text
   and UI 3:1, AAA 7:1. Name colors so people can say them ("Ocean Blue"), not just hex.
6. **Typography** [brand typography-specifications]. Max 2 families (display + text), confirm the license (Google Fonts
   is safest). Base 16 px, ratio 1.25 (Major Third): display 61, H1 49, H2 39, H3 31, H4 25, H5 20, body-large 18, body
   16, small 14, caption 12; line height 1.1-1.2 for display/H1, 1.5-1.6 for body; on mobile shrink H1 to about 32 px.
   Define weights, letter spacing and font loading (Google Fonts with `preconnect` and `display=swap`).
7. **Logo** [design logo-design + brand logo-usage-rules + logo-designer + media-studio rule]. a) Brief: steps 0-6
   already answer format (icon, wordmark or combination mark), style and colors; ask the user only what is still missing, in
   one batched question; on "just make something" use defaults (icon only, minimal, brand or best-fit palette)
   [logo-designer]. Add the free local style search
   `python3.12 <skill>/members/design/scripts/logo/search.py "<industry> <mood>" --design-brief -p "<Brand>"`. b) Concepts:
   3-5 genuinely different directions (vary the metaphor, letterform, layout or aesthetic, never shades of one idea),
   drawn directly as SVG to the "Logo SVG loop" conventions (free) [logo-designer]; paid AI concepts via
   `<skill>/members/design/scripts/logo/generate.py` only after the user's OK, white background, with the negative list (no
   photorealism, 3D textures, clip art, multiple logos, busy background, watermark text, fine detail). c) the user picks on the
   review page. d) Iterate on the pick as numbered SVG files, with the size strip in every round, until the user says "this is
   the one" [logo-designer]. e) Build the final as clean vector SVG: full color, horizontal and stacked lockups, icon/mark
   only, wordmark, one-color black, reversed white. f) Rules: clear space = height of the mark on all sides; minimum width
   120 px full logo, 24 px icon (32 px in UI), 35 mm / 10 mm in print; test at 16, 24, 32, 48, 64 px; list the don'ts (no
   stretch, rotate, shadow, gradient fill, outline, off-palette color, busy background, crop, rearranging, added
   elements). g) Export the PNG and ICO families; favicon and app icon derive from the `#icon` group, never the squeezed
   full lockup ("Logo SVG loop").
8. **Tokens** [brand update + sync script]. Write the palette and type into `docs/brand-guidelines.md`, then
   `node <skill>/members/brand/scripts/sync-brand-to-tokens.cjs --dry-run`, then without `--dry-run`, producing
   `assets/design-tokens.json` and `.css`. If it reports an existing token source, stop and extend that source instead;
   use `--force` only to replace its own earlier managed outputs. Verify with
   `node <skill>/members/brand/scripts/inject-brand-context.cjs --json`. Run from the project root (scripts resolve paths there).
9. **Guidelines document.** Use `members/brand/templates/brand-guidelines-starter.md`: quick-reference table, palette,
   typography, logo usage with do/don't, imagery, voice profile, messaging, and an "AI image base prompt" (brand mood
   keywords + style + palette words) that media-studio reuses [brand update step 2]. Version it (v1.0, v1.1).
10. **Applications.** CIP mockups: HTML/CSS mockups are free; paid Gemini mockups (`scripts/cip/generate.py --logo`,
    with the real logo for fidelity) only after the user's OK [design CIP]. Icons: SVG with `viewBox="0 0 24 24"`,
    `currentColor`, a `<title>`, round caps/joins for outlined sets, no embedded fonts or raster, designed at 24 and
    tested at 16 and 48 [design icon-design]. Deck/doc theme: export the brand as a theme file in theme-factory's format
    (below). Social templates and banners: hand to media-studio.
11. **Audit and approve** [brand checklists]. Run the merged checklist below; scripts help:
    `node <skill>/members/brand/scripts/validate-asset.cjs <file>` (naming, size, format, palette) and
    `node <skill>/members/brand/scripts/extract-colors.cjs <image>` (compare against the palette). Report pass/fail with fixes.

## Core rules and checklists

### Unified VOICE PROFILE [brand-voice schema + brand voice-framework]
```text
VOICE PROFILE  (brand or author: <name>; goal: <use>; confidence: <low|med|high>; sources: <list or "defined, no samples yet">)
Traits:        <3-5 "X, not Y">          Spectrums: formal-casual <1-5>, simple-complex <1-5>, serious-playful <1-5>, reserved-expressive <1-5>
Rhythm:        <sentence length, pacing, fragments>
Compression:   <dense vs explanatory>     Capitalization: <norm>     Parentheticals: <how used / not used>
Questions:     <rare, rhetorical, direct>  Claims: <how framed and supported; numbers and receipts?>
Preferred moves: <observed moves>         Banned moves: <observed or requested only>
CTA rules:     <how and when to ask>
Context shifts: social | support | sales | legal | email
Do / Don't:    <2-3 example pairs>
```
Default banned moves unless the sources show the brand uses them: fake curiosity hooks, "not X, just Y", "no fluff",
forced lowercase, LinkedIn thought-leader cadence, bait questions, "Excited to share", founder-journey filler, corny
parentheticals [brand-voice]. If sources conflict, name the split instead of averaging it [brand-voice schema].
Reuse the latest confirmed profile for the rest of the session.

### Theme files and theming [theme-factory]
- A theme is: name, one-line mood, 4-6 colors with hex and role, header font, body font, "best used for".
- No brand: pick the best-fit preset (Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden Hour,
  Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, Midnight Galaxy), say which and why, and offer
  `members/theme-factory/theme-showcase.pdf` for a different pick. None fits: create a custom theme in the same format,
  named for its mood.
- Apply consistently across every slide/page; keep contrast; never edit the showcase PDF.

### Brand-application recipe (any brand, any artifact) [generalized from brand-guidelines]
- Headings (24 pt and up) in the brand display font, body in the text font, each with a named system fallback
  (e.g. Poppins -> Arial, Lora -> Georgia) so files render on machines without the fonts.
- Text color picked for contrast against its background; non-text shapes take accent colors, cycling primary ->
  secondary -> tertiary.
- In python-pptx set exact `RGBColor` values; in HTML use the CSS variables from the tokens file; in docx use theme colors.

### Logo concepts [design logo-design + logo-prompt-engineering]
- Pick the logo type first, it decides everything after: wordmark, lettermark, pictorial mark, abstract mark, mascot,
  emblem, or combination mark. Then an aesthetic (minimalist, vintage, art deco, luxury, playful, corporate, organic,
  geometric, line art, monoline, negative space, responsive/adaptive). The local data files under
  `members/design/data/logo/` (styles, colors, industries) back the free `search.py` brief.
- Concept prompt (paid generators only, after the user's OK):
  ```text
  Professional logo design for <brand / industry>: <visual idea in one sentence>
  Style: <type + aesthetic keywords>   Colors: <2-3 palette names or hex>
  Requirements: flat vector look, centered, white background, works in one color, no text unless wordmark
  NOT: photorealistic, 3D textures, photograph, stock image, clip art, multiple logos, busy background,
       watermark text, low quality, blurry, distorted, complex detailed patterns
  ```
- Show 3-5 concepts (up to 6 when paid AI concepts join the code-drawn ones) on one page with the brand name set in the
  chosen type next to each; the user picks one or two to refine.
- Test the pick before vector work: one color, reversed, on light and dark grounds, at 16 px, on a busy photo, next to
  two competitor logos.

### Logo SVG loop [logo-designer, wired to the user's review page]
- Canvas: `viewBox="0 0 512 512"` for icons, `viewBox="0 0 1024 512"` for wordmarks and combination marks; never fixed
  `width`/`height` attributes, so one file scales to every size.
- Self-contained: no external fonts, images or `<use>` links to other files. Concepts set text in a system stack with a
  generic fallback (`font-family="Helvetica, Arial, sans-serif"`). For the final, outline the wordmark into `<path>`s in
  the brand font when a tool exists; none is installed today (no fontTools, Inkscape), so ask before installing, or keep
  the stack and say so in the hand-off.
- Groups with fixed ids: `<g id="icon">`, `<g id="wordmark">`, `<g id="tagline">`, identical across iterations, so "make
  the icon bigger" maps to one group and the user can see what changed.
- Flat fills by default; gradients only when asked or the style clearly needs them. No stray transforms, empty groups or
  namespace clutter.
- Small sizes: on the 512 canvas any outline that must survive needs `stroke-width` 6 or more; prefer solid shapes to
  thin strokes; drop details that will not read at 32 px.
- Files: `logos/concepts/concept-1..5.svg`; then `logos/iterations/iteration-N.svg` (iteration-1 = copy of the picked
  concept; every change gets the next number, nothing is overwritten; "go back to N" makes N the new base);
  `logos/preview.html` regenerated each round, newest first, with a light/dark toggle (template in
  `members/logo-designer/SKILL.md`); finals in `logos/export/`.
- Size strip in every refine preview: each iteration at 64, 32 and 16 px. For a combination mark render a square SVG of
  the `#icon` group alone; never squeeze the full lockup into a favicon cell. When detail vanishes at 32 px, propose the
  fix (thicker strokes, fewer elements) before the user has to ask.
- Single feedback ("change the blue to green"): write the next iteration yourself. Batch exploration (3+ variations of
  palette, shape or count): one parallel agent per variation (`superpowers:dispatching-parallel-agents`), each given the
  full base SVG inline, these conventions, its one variation and its target path, since agents share no context.
- Review: `logos/preview.html` is the fast working loop. Decisions go on the review page: an Artifact with every SVG
  inlined (the page cannot load local files), light and dark tiles, the size strip, and a pick + note per concept saved
  to the page store; the next round is built only from the user's stored picks.
- Export to `logos/export/`: `logo.svg`, plus `icon.svg` (the `#icon` group with a tight square viewBox) for combination
  marks; PNGs `logo-{16,32,48,192,512,1024,2048}.png` and the same `icon-*` family (icons feed favicons and app icons,
  `logo-*` goes where the full mark belongs). The member's `scripts/export.sh` needs resvg, sharp, Inkscape or
  rsvg-convert and none is installed, so use macOS `sips` (built in, keeps transparency, checked 2026-11-11), one call per
  size: `sips -s format png --resampleWidth 512 logos/export/icon.svg --out logos/export/icon-512.png`. Look at the PNGs:
  if `sips` drops a filter or font, screenshot the SVG at exact pixel size with Playwright instead [new].
- Repo hand-off, only when asked: replace only the icon files the project already uses, e.g. `favicon.svg`,
  `favicon.ico` (48 px: `sips -s format ico icon-48.png --out favicon.ico`), `apple-touch-icon.png` (180 px, flattened on
  the brand background because iOS fills transparency with black), `pwa-192x192.png`, `pwa-512x512.png`, iOS `AppIcon`
  1024 px, `manifest.json` icon entries. Work on a branch such as `chore/new-logo`; commit, push and PR only when the user asks.

### Industry color starting points [design logo-color-psychology]
| Industry | Primary | Secondary | Accent | Avoid |
|---|---|---|---|---|
| Tech | blue, purple | gray, white | teal, green | brown, beige |
| Finance (debt relief, lending) | navy, blue | gold, gray | green | bright colors |
| Healthcare | blue, green | teal, white | light purple | red, black |
| Food | red, orange | yellow, brown | green | blue |
| Fashion / apparel | black, white | gold, blush | navy | neon unless intentional |
| Eco | green, brown | beige, blue | yellow | neon, black |
| Children | multi-color | pastels | bright accents | dark, muted |
A starting point, not a rule: a challenger brand may break its category on purpose (say so in the rationale).

### Brand kit deliverables (IDENTITY done means all of these exist)
- `logo/` (or `logos/export/`): SVG master set (full color, horizontal, stacked, mark, wordmark, black, white) + PNG
  families at 16, 32, 48, 192, 512, 1024, 2048 px for both `logo-*` and `icon-*`, favicon (SVG + ICO 48 px), apple-touch
  icon 180 px, PWA 192/512 px, app icon master 1024 px.
- `docs/brand-guidelines.md` (versioned) and `assets/design-tokens.json` / `.css` (synced, single token source).
- Messaging sheet (step 2) and VOICE PROFILE (step 3), inside the guidelines or beside them.
- Theme file in theme-factory format for decks and docs; AI-image base prompt for media-studio.
- Optional: CIP mockups, social profile images (via media-studio), email signature.

### Audit and approval checklist (merged) [brand approval-checklist + consistency-checklist]
- Purpose: serves its goal, right audience, fits the campaign, no obvious errors.
- Logo: right variant for the context and background, clear space, minimum size, approved colors, unmodified, current
  version (no outdated logos in profiles, footers, email signatures).
- Color: palette only, 60/30/10 balance, semantic colors used for their meaning, consistent across elements.
- Type: brand fonts and weights, clear hierarchy, sizes fit the medium, adequate line height, no orphans or widows.
- Imagery: matches the photo/illustration style, consistent edit/filters, licensed and credited, optimized for use.
- Accessibility: text 4.5:1, large text 3:1, visible focus, color never the only signal, alt text, logical reading order,
  descriptive links.
- Copy: on voice, tone fits the context, brand terminology and capitalization, no prohibited terms, value prop and one
  clear CTA, benefits over features, no conflicting claims, proofread.
- Technical: right format, resolution and size (email assets under 1 MB), naming convention, platform specs.
- Legal: stock, music and user content cleared; no trademark conflicts; required disclosures; no misleading claims;
  prices accurate; terms and privacy linked where needed.
- Channel sweep: website (home, product, blog, footer), social (avatar, cover, bio, templates), email (header, footer,
  templates, signatures, automated messages), collateral (decks, one-pagers, cards). Cadence: website monthly, social,
  email and sales material quarterly, full audit yearly.
Report each failed item with its fix (too-small logo -> minimum size; wrong font -> brand font; low contrast -> palette
pair that passes; off-brand color -> nearest palette color; blurry image -> higher-resolution source).

### Asset naming [brand asset-organization]
`{type}_{campaign}_{description}_{YYYYMMDD}_{variant}.{ext}`, kebab-case parts, `evergreen` for non-campaign assets,
e.g. `logo_brand-refresh_horizontal-full-color_20261110.svg`. Use this in brand asset libraries; campaign banner sets
follow media-studio's convention; an existing project convention beats both.

### Quality bar
- Brand rules come only from supplied or approved sources; never invent a rule and never borrow another company's
  marks, names or trade dress [banner-design, design].
- Every color pair used for text passes AA; every logo variant works in one color at minimum size.
- Messaging lines pass the 5-question test; voice profile has examples, not just adjectives.
- Generated logo concepts are inputs to a human-reviewed vector build, never shipped as-is.

## When members disagree

| Between | Conflict | Rule |
|---|---|---|
| design vs image (media) vs logo-designer | Generate logos with Gemini (55 styles) vs AI logos are poor, always design them vs draw every concept as SVG | Code-drawn SVG is the default for concepts and finals (free, editable, matches the user's drawn-in-code site art); paid AI concepts only as extra inputs after the user's OK; finals are hand-built SVG with variants and size tests |
| logo-designer vs the user's autonomy | Interview with up to 4 AskUserQuestion prompts before drawing | Infer format, style and colors from the inventory and brand; ask only what is still missing, once, batched; otherwise use the defaults and let the review page do the choosing |
| logo-designer preview vs visual approval protocol | Ask "which number?" against a local `preview.html` | `preview.html` stays the working loop; every pick goes through the review page with stored pick + note per concept |
| logo-designer parallel agents vs cost | One Task agent per concept with `mode: "bypassPermissions"` | Write up to 3 concepts and every single tweak yourself; parallel agents only for 4-5 concepts or batch variations, each with the full brief; never bypass permissions |
| logo-designer export vs no installs | "Install resvg / Inkscape / librsvg" when export.sh finds no converter | Use built-in `sips`, or a Playwright screenshot at exact px; installing anything asks the user first |
| logo-designer Lineage canvas | Optional external canvas review with a handoff script | Explicit opt-in only: use it only if the user asks for Lineage and gives the checkout; never search for or start it |
| brand voice-framework vs brand-voice | Define voice from traits vs derive only from real sources, never generic exemplars | 5+ real samples: derive from them. New brand: traits + spectrums, labeled "defined, not yet observed"; re-derive once real content exists |
| brand-voice defaults | Built-in "Affaan / ECC" voice | Dropped; it is another person's voice |
| brand-voice vs brand | Do not store voice fingerprints in repos vs brand guidelines in `docs/` are the source of truth | Company brand voice lives in the guidelines doc. A personal author profile (the user's own writing) stays out of repos; save to memory or a workspace only when asked |
| theme-factory vs the user's autonomy | Show showcase, ask, wait for explicit choice | Existing brand: apply it, no question. No brand, one-off: pick, say why, offer the showcase. New identity: review page with options |
| design vs the user's autonomy | "ALWAYS ask about an HTML preview" | Always produce the side-by-side preview page; do not ask whether to |
| design vs library integrity | "When scripts fail, fix them directly" | Never edit library scripts (shared vetted repos); copy to the scratchpad, fix there, tell the user |
| brand-guidelines vs every other brand | Anthropic colors and fonts presented as the brand standard | Use only when the Anthropic look is asked for; otherwise reuse just its application recipe |
| brand asset naming vs banner-design naming | Two file-name schemes | Brand library: brand scheme; campaign banner sets: banner scheme; project convention first |
| design umbrella vs other super-skills | Also does slides, banners, social photos | Routed to docs-decks and media-studio so each has one owner |
| brand-voice hard bans vs a brand's real style | e.g. forced lowercase banned | Bans are defaults; a move observed in the brand's own sources or requested by the user is allowed |

## Combine with

- Built-in skills: `anthropic-skills:theme-factory` (same as the member), `anthropic-skills:canvas-design` (brand
  posters, print art), `anthropic-skills:docs` (guidelines as a shareable doc), `artifact-design` and
  `artifact-capabilities` (review page with stored picks), `frontend-design:frontend-design` (brand applied to a page).
- Personal skills: `humanizer` (voice QA), `content-research-writer` (messaging research).
- Superpowers: `superpowers:brainstorming` before any identity or naming work; `superpowers:dispatching-parallel-agents`
  (batch logo variations); `superpowers:verification-before-completion`.
- Playwright MCP: exact-pixel PNG fallback when `sips` misrenders an SVG, and screenshots of the logo preview for the
  review page.
- Agent prompts (`~/.claude/skill-library/agents/voltagent/`): `10-research-analysis/competitive-analyst.md` (competitor
  brand audit), `10-research-analysis/market-researcher.md` (audience and category), `01-core-development/ui-designer.md`
  (visual system), `08-business-product/landing-page-copywriter.md` (messaging into page copy),
  `08-business-product/content-quality-editor.md` (voice check before publishing),
  `06-developer-experience/visual-asset-generator.md` (favicon and app-icon checklist; skip its npm install step).
- Other super-skills: media-studio (banners, social, AI imagery), docs-decks (decks, docs), ui-studio (component
  styling), copy-and-content (writing in the voice), commerce-pro (store theming).

## House rules

- Paid generation asks first: the design member's logo, CIP and icon scripts call Gemini (and optionally Atlas Cloud or
  MuAPI); OpenAI images too. The local style search (`search.py`) is free.
- Identity choices are the user's: show options side by side on a review page with a pick and note per item, read the picks
  back, build only from them.
- For commerce brands, brand expression exists to sell. Humor and identity choices are judged by "does this get more people to
  buy?", backed by conversion evidence; no explainer sections.
- API or CLI before browser automation; if a browser is needed (for example a font or logo portal), say why in one line.
- Keys come from the environment or a local .env for the one command that needs them; never print them.
- Publishing brand assets to a live site, store or social profile asks the user first.
- The logo is the user's call: never apply a logo to the store or products without their pick; original art only, no
  trademarked phrases or competitor brand marks.
- Site and brand art is drawn in code where it can be: code-drawn SVG logos fit that rule.

## Members

| Member | Best at | Path |
|---|---|---|
| brand | Frameworks and checklists: messaging, voice traits, palette hierarchy, type scale, logo usage, asset naming, approval and consistency checks; token sync and asset/color validation scripts | `members/brand/SKILL.md`, `references/*.md`, `scripts/*.cjs`, `templates/brand-guidelines-starter.md` |
| design | Logo, CIP and icon production with searchable style, color and industry data (local BM25) and Gemini generators; color psychology; logo prompt negatives | `members/design/SKILL.md`, `references/logo-*.md`, `cip-*.md`, `icon-design.md`, `scripts/{logo,cip,icon}/` |
| brand-voice | Source-derived voice profile with an exact schema, hard bans and reuse rules | `members/brand-voice/SKILL.md`, `members/brand-voice/references/voice-profile-schema.md` |
| brand-guidelines | Anthropic's palette and fonts, plus a clean recipe for applying any brand's fonts and accents to files | `members/brand-guidelines/SKILL.md` |
| theme-factory | 10 ready themes (palette + font pair + use) and a custom-theme format for decks, docs and pages | `members/theme-factory/SKILL.md`, `themes/*.md`, `theme-showcase.pdf` |
| logo-designer | Code-drawn SVG logo loop: 3-5 distinct concepts, numbered iterations, preview page with light/dark toggle and 64/32/16 px size strip, `#icon` extraction, PNG export family, repo icon hand-off | `members/logo-designer/SKILL.md` (preview and size-strip HTML), `scripts/export.sh` (needs a converter; use `sips` instead), `scripts/lineage-handoff.mjs` (opt-in only) |

If a member folder is missing (not installed), work from this file alone.
