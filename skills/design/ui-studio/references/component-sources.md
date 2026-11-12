# Component sources (Watermelon UI, Skiper UI, shadcn registries)

Used by SKILL.md step 4.0 and the Component sourcing mode. Facts checked against the cloned
Watermelon repo (`WatermelonCorp/watermelon-platform`, commit 27649b8, read-only) and Skiper UI's public
pages and registry JSON (read-only GETs). Registry contents change: re-read an item's JSON before every
install, never trust these numbers as current.

## 1. When to source and when not to

Source first when the part is common and its value is in correct mechanics, not in originality:
primitives and their variants, forms, tables, nav, pricing, FAQ, footers, toggles, carousels,
expandable cards, number tickers, link and hover details, dashboard shells. A block is a starting
structure; it is restyled and its copy rewritten until it passes the plan header and the anti-slop sweep.

Do not source:
- In Invent mode, or for the page's signature moment: those come from the product's concept (conflict 34).
- Code-drawn brand scenes (the brand's signature) and the user's own ops dashboards
  (dashboard-studio rules: dense, big numbers); a sourced shell may lend structure only.
- When the project already has an equivalent component: reuse beats install.
- A recognisable signature effect recreated from another brand's site (Skiper says most of its items are
  "recreations of the best out there"; Watermelon credits visual inspiration under "Inspired By"). Fine
  for mechanics in an internal tool; on the user's brands and client sites pick another item (conflict 18).
- Non-React stacks (Shopify Liquid themes, Vue, Svelte, plain HTML): read the source as a reference and
  re-implement; Shopify admin apps use Polaris.

## 2. Which source for what

| Need | Look first | Then | Notes |
|---|---|---|---|
| Primitives (button, dialog, select, tabs, tooltip, accordion, carousel) | The project's own components, then shadcn/ui (`members/ui-styling/references/shadcn-components.md`) | Watermelon `components` (516 variants by category) | Registry items pull shadcn primitives through `registryDependencies` anyway |
| Page sections (hero, features, pricing, testimonials, FAQ, CTA, footer, careers) | Watermelon `blocks` (189); `compose_page` for a whole landing page | Skiper has few sections | Structure only; copy follows `ui-copy.md`, layout rules of step 4.3 still apply |
| Interaction pieces (animated toggles, expandable cards, swap widgets, micro-interactions) | Watermelon `animated-components` (131; each has a `-base` theme-token variant) | Skiper free: theme toggle (skiper4, skiper26), animated number (skiper37), text roll nav (skiper58), gooey (skiper64), progressive blur (skiper41) | Counts against the step 5 motion budget |
| Scroll and showpiece motion (card stacks, parallax, perspective carousels, SVG follow-scroll, image reveals) | Skiper free (Next.js, framer-motion, often Lenis, GSAP or Swiper) | Watermelon animated | Only for the one memorable moment; no Lenis scroll hijack; reduced motion shows the end state |
| Link and hover details | Skiper skiper40 (CssLink: five underline styles, no dependencies) | make-interfaces patterns | CSS-only items are the safest installs |
| Dashboard layouts | Watermelon `dashboards` (12) as a composition reference | `../dashboard-studio` | Metrics and the user's dashboard house rules win |
| Templates or whole sites | Watermelon `templates` (1) | taste-skill pipeline | Reference only |

Counts are from Watermelon's MCP catalog at commit 27649b8 (849 entries) and Skiper's free registry
(37 items of about 106 listed on its site). The official shadcn registry index
(`https://ui.shadcn.com/r/registries.json`, 565 registries) lists both: `@watermelon` (1,178 items,
including `-base` variants) and `@skiper-ui` (37 items).

## 3. Finding items

**Watermelon with its MCP** (only once the user has added it; see section 6). Tools, all read-only:
- `search` {query, kinds?: components | animated-components | blocks | dashboards | templates, category?, limit 1-50}
- `get_inspiration` {prompt, kinds?, limit 3-6}: preview links to compare.
- `get_component` {slug, kind?}: source files, dependencies, registryDependencies, preview and install command.
- `compose_page` {prompt, sections? (up to 8)}: up to 3 blocks per section, a starting plan; inspect each
  preview and replace any section that does not fit the direction [watermelon-ui].
- `list_categories` {kind?}; compatibility aliases `catalog_summary`, `list_catalog_entries`, `get_catalog_entry`.

**Watermelon without the MCP:** read-only JSON, no key: `https://ui.watermelon.sh/api/catalog/summary`,
`https://ui.watermelon.sh/api/catalog/entries?kind=blocks`, the registry index
`https://registry.watermelon.sh/r/registry.json` (items without file contents) and one item
`https://registry.watermelon.sh/r/<name>.json`. Human previews: `https://ui.watermelon.sh/animated-components`,
`/blocks`, `/dashboards`, `/templates` (the site loads its own analytics; the JSON endpoints do not need a browser).

**Skiper UI:** names are numbers (`skiper1` to `skiper107`), so choose by preview, then read the item's
`component_name` and `collection_name`. Previews: `https://skiper-ui.com/components` (premium items carry
a premium badge) and `https://skiper-ui.com/v1/skiperNN`. Free list: `https://skiper-ui.com/registry/registry.json`;
one item: `https://skiper-ui.com/registry/skiperNN.json`. Its robots.txt disallows `*.json` for crawlers:
fetch only the items you are considering, never bulk-download.

**shadcn CLI 3+** can also browse namespaces without installing: `npx shadcn@<version> search @watermelon -q "pricing"`
and `npx shadcn@<version> view @skiper-ui/skiper40`. If the project's CLI lacks these, curl the item JSON.

Compare 2-4 candidates (the user's rule; Watermelon's `get_inspiration` allows up to 6) against the plan
header: fit with the direction and visitor mode, dependency weight, accessibility, how much restyling it
needs, licence. Say which you picked and why in one line each.

## 4. Registry config and install

Both namespaces resolve from the official index in shadcn CLI 3+, so `components.json` needs no change.
Declaring them pins the URLs the project trusts:

```json
{
  "registries": {
    "@watermelon": "https://registry.watermelon.sh/r/{name}.json",
    "@skiper-ui": "https://skiper-ui.com/registry/{name}.json"
  }
}
```

Install from the target project's root only (never from the skill library, this super-skill folder or the home
directory), on a branch, with the CLI version pinned and the user's npm cache:

```bash
npm_config_cache=/tmp/npm-cache npx shadcn@<version> add @watermelon/<item>        # or <item>-base
npm_config_cache=/tmp/npm-cache npx shadcn@<version> add @skiper-ui/skiper40
npm_config_cache=/tmp/npm-cache npx shadcn@<version> add https://registry.watermelon.sh/r/<item>.json   # URL form
```

Use the version the project already pins (package.json or lockfile) or one you have checked; never
`@latest` inside a live project's scripts. `add` installs the item's npm dependencies with the project's
package manager and can edit CSS variables, the Tailwind config and `.env` files, which is why section 5
runs first. Files land under the components alias: Watermelon `components/watermelon/<name>.tsx`, Skiper
`components/ui/skiper-ui/skiperNN.tsx` (its docs show a different import path; trust the CLI's
"Created" list). Never pass `--overwrite` without reading the diff.

Not used: `npx @watermelon-ui/cli init` and the repo's `.claude-plugin`, `.mcp.json` and `.cursor-plugin`
(they write MCP config: the user's decision); `npx @watermelon-ui/cli add` (a wrapper around the same registry).

**Skiper Pro (reference only, the user's decision):** Pro items return 401 without a key. Pro installs use
`"@skiper-ui": {"url": "https://skiper-ui.com/r/{name}.json", "headers": {"Authorization": "Bearer ${SKIPER_LICENSE_KEY}"}}`
with the key in the project's `.env.local`. The key is a purchase secret: never printed, committed or
copied into any file but that ignored env file and the user's credentials file. Free items are also served from `/r/`,
but with different declared dependencies (skiper40 lists `framer-motion` there and imports none), so
free items install from `/registry/`.

## 5. Safety checklist for third-party component code

Run it for every item before `add`, and again on the diff after.

1. **Read the item JSON first** (`view`, `get_component` or curl). List every `files[].path` and
   `target`; anything outside the components folder (app routes, `middleware`, `next.config`, `lib/`
   overrides, `registry:file` or `registry:page` targets) needs a reason. Note `cssVars`, `css`,
   `tailwind` and `envVars` blocks: they edit global styles or env files.
2. **Dependencies:** compare `dependencies` and `devDependencies` with the actual `import` lines.
   Watermelon derives them from imports (peer packages such as `next` can be missing); Skiper's
   endpoints disagree with each other. Each new npm package: known publisher and repo, recent
   release, real usage, no `preinstall` or `postinstall` script, licence compatible; versions pinned.
   Unknown or tiny packages (Skiper's `dialkit` in skiper106) mean another item or the user's yes. Prefer
   packages the project already has; never a second motion library (`framer-motion` next to
   `motion/react`) or a second icon set; heavy ones (GSAP, Lenis, Swiper, Three) only for the one
   memorable moment, lazy-loaded.
3. **registryDependencies:** each is another item that gets installed (shadcn primitives such as
   `carousel`, `tooltip`, `scroll-area`, or URLs into other registries); read each the same way.
4. **Code that runs or calls out:** search the file contents for `fetch(`, `XMLHttpRequest`,
   `sendBeacon`, `<script`, `next/script`, `dangerouslySetInnerHTML`, `eval`, `new Function`,
   `localStorage`, `document.cookie`, analytics or pixel IDs, `window.location` redirects, iframes,
   remote fonts, images or CDNs, and audio or video autoplay (Skiper's `use-sound`, `media-chrome`). None
   stays without a reason written in the report. No telemetry, no remote scripts.
5. **Demo content out:** demo wrappers (skiper40's full-height snap-scroll `<section>`), author emails
   and links (skiper40 ships a `mailto:` link, cursor.com and the author's site), placeholder
   images from the vendor's CDN, fake names and numbers (honest-content rule).
6. **Fix the code to house rules:** `transition-all` to explicit properties (skiper40 uses it),
   `framer-motion` imports to `motion/react` in new code (conflict 17), icons swapped to the project's
   set (Watermelon items mix `react-icons`, `lucide-react` and Hugeicons), z-index to the named scale,
   reduced-motion behaviour per step 5, focus-visible, names on icon buttons, 44px targets.
7. **Restyle to the project:** colours to semantic tokens, radii to the project's scale (concentric),
   shadows to its elevation scale, fonts to its faces, durations and curves to the step 5 tokens, copy
   rewritten by `ui-copy.md`. Watermelon's `-base` variant starts closer because it reads theme tokens.
   The user's brands keep their own look; the library's look never wins (conflict 35).
8. **Licence and attribution:** a header comment in each installed file:
   `// Adapted from Watermelon UI <item> (MIT, https://ui.watermelon.sh)` or
   `// Adapted from Skiper UI skiperNN (free tier, attribution required, https://skiper-ui.com)`.
   Skiper's free-tier attribution also needs a visible credit on the shipped site; where it goes on the user's
   or a client's site is their call (open question in analysis.json).
9. **Verify:** typecheck, lint and build; `validate-tokens.cjs`; render per step 6 in both themes with
   reduced motion; `git diff` reviewed (files created, CSS and config edits, package.json and lockfile).
10. **Report:** each sourced item with source, item name, licence, new dependencies and what was
    restyled. In a live project the item, its new dependencies and the restyle go on the user's review page
    as one card (normal build flow).

## 6. Licences, terms and the MCP server

| Source | What we found | Paid tier | What we do |
|---|---|---|---|
| Watermelon UI | MIT (LICENSE, "2026 Watermelon Platform Contributors"); site terms allow copying and use "in line with the relevant licenses"; visual inspiration credited under "Inspired By"; blocks, dashboards and templates come from a second repo (`WatermelonCorp/watermellon-registry`) whose licence was not checked | None ("free for the community"; sponsorship only) | Keep the MIT header comment; check the item page's "Inspired By" note; treat second-repo items as MIT-unverified until checked |
| Skiper UI | Three signals disagree: the quick-start page says "Free to use and modify in both personal and commercial projects. Attribution to Skiper UI is required when using the free version. No attribution required with Skiper UI Pro."; the registry index says `license: MIT` (repo `gxuri/skiper-ui-pro`); the Terms of Service (updated 2025-09-07) are a generic template reserving all rights and forbidding reproducing or redistributing site material. The author says most items are recreations of others' work | Premium $129 and Exclusive $549 (adds a Figma file), one-time, sold through Polar; licence key checked on every install | Free items only, with attribution; Pro, keys and purchases only on the user's yes; avoid recognisable recreations on brand or client sites |

**Watermelon MCP** (`https://mcp.watermelon.sh/mcp`, Streamable HTTP, no key). Reviewed code
(`mcp/worker.ts`, `mcp/catalog.ts` at 27649b8): read-only catalog tools; `get_component` fetches the
item from `registry.watermelon.sh` on the server side; the Worker writes aggregate counts (event type,
client family such as "claude", tool name) to Cloudflare Analytics Engine and, per the code, stores no
IP, session ID, prompt or tool arguments. The deployed server cannot be verified against the repo, and
Cloudflare sees request metadata like any host, so prompts sent to it carry no secrets, client names or
unreleased brand details. Adding it to Claude's config is the user's decision;
the one-line command for the user: `claude mcp add --transport http watermelon https://mcp.watermelon.sh/mcp`
(local scope by default; `--scope user` for every project). The official shadcn MCP server
(`npx shadcn@<version> mcp init`) is also their decision. Until then, use section 3's JSON and CLI routes.


## Rule for Skiper UI
Free items are allowed on the user's sites with a small footer or credits-page credit ("UI components: Skiper UI"). Check each item for look-alike designs (the author calls many items recreations) before using it on a brand site. Pro items and licence keys stay the user's call.
