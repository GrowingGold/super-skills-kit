# Style directions (opt-in presets)

Each preset is a complete aesthetic. Use one per project, only when the user names it or the design read
clearly calls for it and the plan header says so. Never blend two presets' looks. The preset governs
palette, type, components and motion character; ui-studio's guards (accessibility, performance,
reduced motion, honest content, anti-slop copy) still apply. Where a preset demands something a guard
forbids, the guard wins, and the plan says which line was overridden.

## Direction table

Moved here from SKILL.md "Pick the mode". One per project, only when
named by the user or clearly matched and written in the plan header. The preset owns the look; ui-studio's
guards still apply.

| Direction | Fits | Signature | Open |
|---|---|---|---|
| Industrial Brutalist | dev tools, data brands, manifestos | Swiss print (light, one red) or CRT telemetry (dark); radius 0; heavy grotesk + mono caps; `gap:1px` hairlines | `members/taste-brutalist-skill/SKILL.md` |
| Editorial Minimalist | doc-style product sites, calm B2B | warm monochrome + spot pastels, 1px `#EAEAEA`, serif display, flat bento | `members/taste-minimalist-skill/SKILL.md` |
| Soft Premium | premium consumer, health, portfolio | double-bezel cards, pill CTA with icon-in-circle, island nav, spring curves | `members/taste-soft-skill/SKILL.md` |
| Motion-rich AIDA | launch pages, scroll storytelling | AIDA order, 2-3 line H1, gapless bento, GSAP pin/scrub/stack | `members/taste-gpt-tasteskill/SKILL.md` |
| High-agency React (v1) | React SaaS marketing | dials 8/6/4, Bento 2.0 perpetual-motion cards, creative arsenal | `members/taste-taste-skill-v1/SKILL.md` |
| Anti-slop dial-driven (v2) | landing, portfolio, redesign | brief inference, design-system map, hard layout rules, GSAP skeletons | `members/taste-taste-skill-v2-experimental/SKILL.md` |
| Company-site pipeline (2.5) | full company sites with a gate | kind-of-business plan, one section per screen, dealt heroes, copy-lint | `members/taste-skill/SKILL.md` |
| Spatial / Antigravity | immersive tech showcases | floating layers, glass, isometric `rotateX(60deg) rotateZ(-45deg)`, GSAP floats, parallax | `members/antigravity-design-expert/SKILL.md` |
| Bold tone | open briefs, "make it memorable" | one extreme from ~40 tones, committed fully | `members/bencium-impact-designer/SKILL.md` |

A sourced component (Watermelon, Skiper UI) never sets the direction: it is restyled into the chosen
preset or the project's own look (`component-sources.md`).

The quick specs below let you work without opening the member; open it for the full text.

## Industrial Brutalist [members/taste-brutalist-skill/SKILL.md]

- Use for: developer tools, data-heavy brands, manifestos, technical products.
- Pick ONE substrate and never mix: **Swiss print** (ground `#F4F4F0` or `#EAE8E3`, ink `#050505`-`#111111`,
  one accent `#E61919`/`#FF2A2A`) or **Tactical telemetry** (ground `#0A0A0A`/`#121212`, text `#EAEAEA`,
  same red, optional `#4AF626` on a single element only).
- Type: heavy neo-grotesk display (Archivo Black, Monument Extended, Neue Haas Grotesk Black) at
  `clamp(4rem, 10vw, 15rem)`, tracking -0.03 to -0.06em, leading 0.85-0.95, uppercase; mono micro text
  (JetBrains Mono, IBM Plex Mono) uppercase, +0.05-0.1em. A high-contrast serif only as a dithered texture.
- Layout: rigid CSS grid, visible 1-2px rules, `display:grid; gap:1px` on a contrasting parent for
  hairlines, radius 0 everywhere, bimodal density (packed metadata next to vast empty space).
- Details: ASCII framing `[ DELIVERY SYSTEMS ]`, `>>>`, crosshairs at grid intersections, barcodes,
  warning stripes, scanlines `repeating-linear-gradient(0deg, transparent 0 2px, rgba(0,0,0,.1) 2px 4px)`,
  halftone, global noise. Semantic tags: `data`, `samp`, `kbd`, `output`, `dl`.
- Guard note: telemetry micro text people must read stays at 12px or more and meets 4.5:1.

## Editorial Minimalist [members/taste-minimalist-skill/SKILL.md]

- Use for: document-style product sites, workspace and writing tools, calm B2B.
- Palette: ground `#FFFFFF` or `#F7F6F3`/`#FBFBFA`, cards `#FFFFFF`/`#F9F9F8`, borders `#EAEAEA` or
  `rgba(0,0,0,.06)`, text `#111111`/`#2F3437` at line-height 1.6, secondary `#787774`. Spot pastels
  (ground/text): red `#FDEBEC`/`#9F2F2D`, blue `#E1F3FE`/`#1F6C9F`, green `#EDF3EC`/`#346538`,
  yellow `#FBF3DB`/`#956400`.
- Type: editorial serif display (Newsreader, Lyon Text, Playfair Display) tracking -0.02 to -0.04em,
  leading 1.1; sans UI (Geist, Switzer, SF Pro); mono for meta and keys.
- Components: bento with exactly 1px `#EAEAEA`, radius 8-12px, padding 24-40px; primary button `#111`
  on white, radius 4-6px, no shadow, hover `#333` or `scale(.98)`; pastel pill tags uppercase +0.05em;
  FAQ accordions with only a bottom border and a sharp +/-; `<kbd>` keys; faux-OS window chrome for
  product mockups. Shadows under 0.05 opacity. Icons: Phosphor Bold/Fill or Radix.
- Motion: enter `translateY(12px)` + opacity over 600ms `cubic-bezier(0.16,1,0.3,1)`, stagger
  `calc(var(--index) * 80ms)`, card hover shadow to `0 2px 8px rgba(0,0,0,.04)`. Content width
  max-w-4xl/5xl, sections py-24/32.
- Guard note: the warm-paper ground overlaps the premium-consumer palette tell; fine for doc-style
  products, not for a cookware or wellness store. It suggests Instrument Serif: pick another serif
  unless the brand asks for it.

## Soft Premium [members/taste-soft-skill/SKILL.md]

- Use for: premium consumer, health, portfolio, lifestyle, agency.
- Pick one vibe: **Ethereal glass** (`#050505`, radial mesh orbs, `backdrop-blur-2xl` cards with
  white/10 hairlines), **Editorial luxury** (`#FDFBF7` creams, sage or espresso, variable serif display,
  grain at 0.03), or **Soft structuralism** (silver-grey or white, bold grotesk, diffused shadows).
- Layout: asymmetric bento (`col-span-8 row-span-2` beside stacked `col-span-4`), Z-axis cascade
  (-2 to 3 degree rotations, removed under 768px), or editorial split. Sections py-24 to py-40.
- Components: **double bezel** (outer shell `bg-black/5 ring-1 ring-black/5 p-1.5 rounded-[2rem]`,
  inner core with its own ground, `shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]` and
  `rounded-[calc(2rem-0.375rem)]`); pill CTAs `px-6 py-3` with the trailing arrow in its own
  `w-8 h-8 rounded-full` circle; floating island nav (`mt-6 mx-auto w-max rounded-full`); hamburger
  lines morph into an X; full-screen menu overlay with staggered links.
- Motion: `cubic-bezier(0.32,0.72,0,1)` around 700ms; magnetic hover (inner icon `translate-x-1
  -translate-y-[1px] scale-105`); `active:scale-[0.98]`.
- Guard notes: its `transition-all` becomes named properties; its "every element fades in on scroll"
  yields to the motion budget; eyebrows obey the one-per-three-sections cap; glass orbs are never violet.

## Motion-rich AIDA landing [members/taste-gpt-tasteskill/SKILL.md]

- Use for: launch pages that need scroll storytelling.
- Order: nav (floating pill or minimal split) → Attention hero → Interest bento → Desire (GSAP pin,
  horizontal pan or word scrub) → Action CTA and footer. py-32 md:py-48 between sections.
- Hero: H1 in max-w-5xl/6xl at `clamp(3rem,5vw,5.5rem)`, 2-3 lines max, exactly two contrasting CTAs;
  no stats, badges or pill tags in the hero.
- Bento: `grid-flow-dense`, 3-5 cards, spans verified to interlock. Hover `group-hover:scale-105
  duration-700 ease-out` inside `overflow-hidden`. Scroll: images 0.8 → 1 scale, fade to 0.2 on exit;
  paragraph words scrub opacity 0.1 → 1; cards stack. Inline pill images inside headings; horizontal
  accordions; one marquee. Wrap `main` in `overflow-x-hidden`. Fonts: Satoshi, Cabinet Grotesk, Outfit, Geist.
- Guard notes: its "simulated Python RNG" becomes real randomness (a `node -e` one-liner); picsum
  photos only in drafts; under reduced motion every pin, scrub and stack shows its static end state.

## High-agency React, taste v1 [members/taste-taste-skill-v1/SKILL.md]

- Use for: React/Next marketing sites and SaaS feature sections where a project depends on v1's output.
- Baseline dials 8/6/4. Display `text-4xl md:text-6xl tracking-tighter leading-none`; body `text-base
  text-gray-600 leading-relaxed max-w-[65ch]`. Geist, Outfit, Cabinet Grotesk or Satoshi; dashboards use
  Geist + Geist Mono or Satoshi + JetBrains Mono.
- Bento 2.0: ground `#f9fafb`, white cards `border-slate-200/50`, `rounded-[2.5rem]`,
  `shadow-[0_20px_40px_-15px_rgba(0,0,0,0.05)]`, titles below the cards, p-8/p-10. Five card archetypes:
  auto-sorting list (`layoutId`), command input typewriter, live status with breathing dots and an
  overshoot badge for 3s, infinite data-stream carousel, focus-mode toolbar. Loops memoised and isolated
  in their own client components.
- Liquid-glass edge: `border-white/10` + `shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]`. Magnetic buttons
  via `useMotionValue`/`useTransform`, never `useState`. A creative arsenal of ~40 named patterns (dock
  magnification, gooey menu, dynamic island, spotlight border, curtain reveal, text scramble).
- Guard notes: its `transition: all` example and "every card loops" yield to ui-studio rules; tilt cards
  live only inside this preset.

## Anti-slop dial-driven, taste v2-experimental [members/taste-taste-skill-v2-experimental/SKILL.md]

The source of most ui-studio guards. Open it for: the design-system map (§2: Fluent, Material 3, Carbon,
Polaris, Atlassian, Primer, GOV.UK, USWDS, Bootstrap, Radix Themes, shadcn) and the honest-aesthetic
table (§2.B); GSAP sticky-stack, horizontal-pan and reveal skeletons (§5.A-5.C); the redesign protocol
(§11); the block-library schema (§12); its 50-line preflight (§14); install commands and canonical docs
(appendices); the honest Liquid Glass web approximation (appendix C). Not for dashboards, data tables,
multi-step forms, editors, native mobile or realtime collaboration UIs (it says so itself).

## Company-site pipeline, tasteskill 2.5 [members/taste-skill/SKILL.md]

The full company-website builder: business-kind table, page plans per kind, a kit (`starter.html`,
`system.css`, motion layer, heroes, moments), dealt palettes, pairings and heroes with history so pages
differ, the copy layer (`references/copy*.md`) with `copy-lint.mjs`, browser checkers
(`consistency.mjs`, `assets/layout/check.mjs`, `shoot.mjs`, `perf.mjs`) and a finish gate
(`gate.mjs`: PASS, OPEN, DONE). Nine house rules: no captions, every visual renders at
1440/1024/768/390, one section per screen, equal edges, a hover micro-animation layer, more real
photographs, real full-colour icons, shader effects only on tech pages, addresses as street and district
only. Needs Node 22+ and a local Chrome; `photos.mjs` searches Wikimedia Commons over the network (free).
Its Stop hook is declared in its own frontmatter and fires only if it is installed as an active skill;
reading it from the skill folder does not arm it.

## Spatial / Antigravity [members/antigravity-design-expert/SKILL.md]

- Use for: immersive product showcases and tech landing pages; never dense ops dashboards.
- React/Next, Tailwind plus custom 3D CSS, GSAP ScrollTrigger (elements float in from the Y axis with a
  slight rotation), React Three Fiber or CSS 3D (`perspective`, `rotateX/Y`).
- Weightless cards with soft diffused shadows (`0 20px 40px rgba(0,0,0,0.05)`), Z-axis layering, glass
  (`backdrop-filter: blur(12px)` + semi-transparent borders), isometric grids
  (`transform: rotateX(60deg) rotateZ(-45deg)`), card grids staggered 0.1s, parallax backgrounds slower
  than foregrounds.
- Guard notes: reduced motion disables all of it; `will-change` only around measured animations and
  removed afterwards; never animate `box-shadow` or `filter` continuously.

## Bold tone [members/bencium-impact-designer/SKILL.md]

For an open brief or "make it memorable": pick one extreme from the menu below, commit fully, and match
code complexity to the vision (maximalism needs elaborate effects; minimalism needs precision).

**Tone menu.** Reduction: brutally minimal, Neo-Swiss grid, Nordic calm, museum exhibition,
monastic/wabi-sabi, playful minimal (one smile detail), coastal/airy, desert modern. Editorial:
magazine, high-fashion lookbook, cinematic noir, monochrome high-contrast, kinetic typography, duotone
pop. Historic: Bauhaus, Constructivist propaganda, Futurist speed, art deco, Memphis, Riso print,
weathered vintage patina, botanical apothecary, whimsical storybook. Tech: retro-futuristic, Y2K cyber
gloss, vaporwave, synthwave night drive, glitch/digital noise, military command UI, scientific/technical,
architectural blueprint, isometric systems, data-driven dashboard, industrial/utilitarian, brutalist/raw,
anti-grid experimental. Tactile: organic/natural, soft/pastel, modern skeuomorphic, clay/soft 3D,
startup crisp.

**Reframing prompts** when the work drifts safe. Designer lens: Sagmeister (provocation, hand-made),
Brody (type as art), Studio Dumbar (bold colour, Dutch directness), Rams (radical reduction), Carson
(feeling over reading). Context shift: a magazine spread, a museum exhibit, street signage, a vinyl
cover, a protest poster. Era lens: 1960s Swiss, 1990s Emigre/Ray Gun, 1920s Bauhaus, 2000s Flash,
cyberpunk.

**Atmosphere parameters.** Grain 0.03-0.08 opacity on a fixed `pointer-events:none` layer; gradient
mesh of 2-4 radial layers at 0.1-0.4 opacity, offset 20-30% from the edges, drifting 10-30% over
15-30s; ambient orbs 8-20s with 5-20px travel; layered shadows tinted with the accent; marquee cycle
20-60s with the content duplicated twice.

## Force variety (only when the brief is open)

Roll for real, never pretend: temperature (warm / cool), layout (left-heavy / right-heavy / centre with
edge tension / diagonal), type personality (geometric sans / humanist sans / serif / slab / display /
mono), motion (minimal / choreographed / playful), density (generous / controlled) [bencium-impact].

```bash
node -e "const p=a=>a[Math.floor(Math.random()*a.length)];console.log(p(['warm','cool']),p(['left','right','centre','diagonal']),p(['geometric','humanist','serif','slab','display','mono']),p(['minimal','choreographed','playful']),p(['generous','controlled']))"
```

Inside the company-site pipeline use its dealers (`start.mjs deal`, `moments.mjs pick`) instead; they
keep a history. In Invent mode never roll: form comes from subject evidence [bencium-innovative].

## Breaking a rule on purpose [bencium-impact]

Break a guideline, a preset rule or a ui-studio default only when all four are yes: you can state the
creative intent; it is a choice, not laziness; it serves the user, brand and context; a senior designer
would defend it. A brand that already uses Inter gets Inter used brilliantly. Accessibility,
performance, honest content and the user's house rules are not breakable.
