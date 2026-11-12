# Scales and systems (merged)

The concrete values behind SKILL.md steps 2-4, merged from the nine Owl-Listener ui-design skills
(color-system, dark-mode-design, typography-scale, spacing-system, layout-grid, readable-measure,
responsive-design, visual-hierarchy, illustration-style), impeccable's colorize, typeset, layout, adapt
and operate references, and the values ui-studio already held. A brand system, an existing DESIGN.md or
a chosen preset overrides any default here; the guards (contrast, targets, measure) do not move.

## 1. Colour system

Build it in this order [color-system, impeccable colorize]:

1. **Strategy** (decide before any hex) [impeccable new-work]:
   | Strategy | What it means | Fits |
   |---|---|---|
   | Restrained | neutrals tinted from the world plus one accent | Operate and Read surfaces (the floor), calm brands |
   | Committed | one saturated colour carries 30-60% of the surface | Persuade pages, one report or welcome screen in an app |
   | Full palette | 3-4 named colour roles | playful, editorial, multi-category stores |
   | Drenched | the surface is the colour | campaign and launch pages |
   Colour commits at page scale: a field that owns a region, not specks scattered over grey.
2. **Brand ramp:** each brand hue as a full tonal scale (50-950), not single swatches. New palettes in
   OKLCH: step lightness evenly, lower chroma near white and black instead of keeping it high for uniform
   maths [color-system, impeccable colorize].
3. **Neutral ramp:** one temperature for the whole project (all warm or all cool), for text, grounds,
   borders and surfaces; a second neutral layer for sidebars, toolbars and panels, slightly warmer or
   cooler than the content surface [ui-studio step 2, impeccable operate].
4. **Semantic roles:** success, warning, error, info, each with background, foreground, border and icon
   variants; always paired with an icon or text [color-system]. Product UIs also standardise hover,
   focus, active, disabled, selected and loading colours [impeccable operate].
5. **Extended:** data-visualisation series (built-in `dataviz`; dashboards go to dashboard-studio),
   illustration subset (section 7), gradient definitions only if the direction uses them [color-system].
6. **Roles, not swatches:** canvas and raised surfaces, primary and secondary text, action, focus and
   selection, borders and separators, status, data [impeccable colorize]. Theme switches remap roles,
   so plan the dark mappings from the start, not after launch [color-system].

Checks: every foreground/background pair measured (text 4.5:1, AAA 7:1, large text and UI parts 3:1)
in every state and both themes, text on images included; simulate the common colour-vision
deficiencies; secondary text on a coloured surface is tinted from that hue or the foreground, never a
generic grey; prefer explicit colours over stacked translucent overlays, whose contrast changes with what
sits under them [color-system, impeccable craft floor, impeccable colorize].

## 2. Dark mode

Designed from the light system's semantic tokens, never inverted [dark-mode-design, impeccable colorize].

| Layer | Starting point | Holds |
|---|---|---|
| Ground | about `#121212` (never `#000`) | page |
| Surface 1 | one step lighter | cards, raised panels |
| Surface 2 | lighter again | dropdowns, modals |
| Surface 3 | lightest dark | tooltips, menus |

- Elevation comes from the lighter surface step; shadows only supplement [dark-mode-design].
- Primary and brand colours desaturated 10-20%; error and warning re-tuned for the dark ground.
- Body text off-white (about `#E0E0E0`), never pure white; borders low-opacity white.
- Light text on dark: slightly more line height, a touch more tracking, one weight step up when the face
  needs it [impeccable typeset].
- Images dimmed slightly; dark variants of illustrations; a light-on-dark logo; avoid big bright areas.
- Apps: follow `prefers-color-scheme` and offer a manual toggle; switching is smooth and every component
  is checked in dark. Marketing pages: one theme, chosen by the use scene (SKILL.md conflict 12).

## 3. Type scale

| Role | Size (16px base) | Line height | Tracking |
|---|---|---|---|
| Caption | 12px | 1.4 | +0.05em in caps |
| Body small | 14px | 1.45-1.5 | 0 |
| Body | 16px (web floor; 16-20 on marketing pages) | 1.45-1.6 | 0 |
| Subheading | 20px | 1.3 | 0 |
| H3 / H2 / H1 | 24 / 32 / 40px | about 1.2 | -0.01 to -0.02em |
| Display | 48-64px, fluid, max 6rem | 0.9-1.1 | -0.02 to -0.04em (floor) |

[typography-scale, ui-studio step 3, impeccable craft floor]. Weights 400 / 500 / 600 / 700, at most 3
per family. 4-5 sizes in regular use. Ratio: 1.25 or 1.333 with fluid display on Persuade pages; 1.125-1.2
on a fixed rem scale for product UI, often one family carrying everything [impeccable operate]. Long-form
reading may relax to 1.75 [typography-scale]. Test with real copy at every breakpoint, never lorem.

## 4. Measure

Characters per line, spaces included [readable-measure]:

| Context | Target |
|---|---|
| Long-form articles, docs | 55-70 |
| UI body copy, descriptions | 45-65 |
| Captions, helper text | 40-60 |
| Pull quotes, callouts | 30-45 |

`max-width: 65ch` is the default body setting, but `ch` is approximate: count a real paragraph. Wide
faces (Georgia) need narrower columns, condensed faces a little wider. Each column of a multi-column
layout meets the rule on its own. Wider measure needs more leading. Display type and short UI strings are
exempt; data tables may run 120ch+ [readable-measure, impeccable operate].

## 5. Spacing and grid

**Scale** (4px base; an 8-only scale misses the useful middle steps) [spacing-system, impeccable layout]:
2xs 2, xs 4, sm 8, md 16, lg 24, xl 32, 2xl 48, 3xl 64, then 96 for marketing sections.
**Spacing jobs:** inset (padding inside a container, equal or squish/stretch), stack (vertical between
siblings), inline (horizontal between siblings), gap (grid and flex). Related items get sm/md, distinct
groups lg/xl, more space above a heading than below it. Density modes move every value one step down
(compact, data views) or up (spacious, reading) [spacing-system, impeccable craft floor].

**Grid** [layout-grid]:

| Viewport | Columns | Gutter | Outer margin |
|---|---|---|---|
| Phone | 4 | 16px | 16px |
| Tablet | 8 | 16-24px | 24-32px |
| Desktop | 12 | 24-32px | 24-48px, inside a max-w-7xl or 1400px container |

Grid types: column (general), modular (columns plus rows, for bentos and galleries), baseline (4px
vertical rhythm), compound (overlapping grids for editorial layouts). Patterns: full-bleed, contained,
asymmetric sidebar plus main, auto-fill card grids. Align to the grid and break it only on purpose, for
emphasis. A component that appears at several widths uses container queries [impeccable layout].

## 6. Responsive and hierarchy

**Responsive** [responsive-design, impeccable adapt]: mobile-first and content-first (add a breakpoint
where the content breaks, not at a device width); patterns: column drop, reflow (row to stack),
off-canvas for secondary content, priority+ (show the most important, overflow the rest). Adaptation
rethinks the experience for the context (glance vs focused, touch vs pointer, slow network), it does not
scale pixels. Input: touch targets 44px, hover effects only under `@media (hover:hover) and
(pointer:fine)`, visible focus and logical tab order for keyboards, clear labels for voice. Images:
`srcset` with width descriptors and `sizes`; `<picture>` for art direction (a different crop per
breakpoint). Check landscape and portrait, real devices when possible, and slow connections.

**Hierarchy** [visual-hierarchy, impeccable layout]: four levels: primary (page title, main action),
secondary (section heads, key content), tertiary (supporting text, metadata), quaternary (fine print,
timestamps). Tools, used together: size (about 1.5x between levels), weight, colour and contrast, space
around an element, position (top-left first in LTR; F and Z scanning), isolation. One primary action per
view. Patterns: card = image > title > description > action; form = label > input > helper > error; nav
= current > available > disabled. Squint test: blurred, the primary, secondary and major groups still
read in order.

## 7. Illustration style guide

Write it once per brand before commissioning or generating illustrations [illustration-style]:
- **Style axes:** geometric or organic; flat, 2.5D isometric or 3D; detailed or minimal; abstract or
  representational; line weight, corners and endpoints.
- **Colour:** a subset of the product palette with primary, secondary and accent illustration colours;
  rules for gradients and shadows; dark-mode variants.
- **Characters** (if any): proportions, face detail, diversity and representation, a pose and expression set.
- **Types and sizes:** spot (inline UI), hero (featured storytelling), empty state, onboarding, error
  state; size limits per context, aligned to the grid, animation rules.
- **Use rules:** when not to illustrate; never the only carrier of information; one consistent style and a
  reusable element library; test at display size.
Generated illustration is paid (media-studio owns the tools): the user says yes first.
