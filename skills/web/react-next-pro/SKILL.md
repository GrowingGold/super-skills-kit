---
name: react-next-pro
description: One skill for React and Next.js work - building, reviewing and speeding up React components and Next.js App Router apps, plus multi-component claude.ai HTML artifacts. Covers Server vs Client Components, data fetching without waterfalls (Promise.all, Suspense streaming, React.cache), Server Actions with validation and auth, caching and revalidation (ISR, revalidateTag, use cache), middleware/proxy, route groups, parallel routes, loading/error files, bundle size (barrel imports, next/dynamic, optimizePackageImports), re-render fixes (memo, derived state, transitions, refs), hydration issues, component API design (compound components, no boolean props, explicit variants, providers, React 19 ref and use()), and React + Tailwind + shadcn/ui artifacts bundled to one HTML file. Triggers - React, Next.js, App Router, RSC, server component, server action, use client, Vercel, hydration error, slow page, bundle size, re-render, compound component, shadcn, Vite React, artifact.
members: [react-best-practices, composition-patterns, nextjs-mastery, web-artifacts-builder]
---

# React + Next Pro

Unifies Vercel's React performance rules (70 rules, 8 categories), Vercel's composition patterns, the user's always-on `nextjs-mastery`
and Anthropic's `web-artifacts-builder`. Load this file first: it picks the mode, carries the merged build order and the top rules
with their rule ids. Open `members/react-best-practices/rules/<rule-id>.md` only for the rule you are applying - never the 105 KB
`AGENTS.md` whole. For Next.js API details, check the installed version and pull current docs (context7) before trusting any example.

## Pick the mode

| Task looks like | Mode | Do / open |
|---|---|---|
| New Next.js page, route, layout, API route, Server Action, middleware/proxy | Next build | Unified workflow steps 1-7; `members/nextjs-mastery/SKILL.md` for the route map; rules `server-*`, `async-*` |
| "This page is slow", LCP/INP, waterfalls, cold starts, big bundle | Performance | Rules by priority (CRITICAL first): `async-*` -> `bundle-*` -> `server-*` -> `client-*` -> `rerender-*` -> `rendering-*` -> `js-*` |
| Component with many boolean props, reusable library, compound component, context design | Compose | `members/composition-patterns/AGENTS.md` (22 KB, readable whole) or its `rules/<id>.md` |
| Too many re-renders, input lag, effects firing too often | Re-render | `rerender-*` rules; check React Compiler first (see conflicts) |
| Hydration mismatch, flicker, theme flash, client-only data | Hydration | `rendering-hydration-no-flicker`, `rendering-hydration-suppress-warning`, `rendering-conditional-render` |
| Review a React/Next PR or file | Review | Review checklist below, findings ordered by rule priority with rule ids |
| Upgrade Next.js or React (15, 16, React 19) | Upgrade | Version notes below + context7 docs for the target version; composition `react19-*` |
| claude.ai artifact with state, routing or shadcn/ui | Artifact (rich) | Load `artifact-design` skill, then Skill `anthropic-skills:web-artifacts-builder` (same as `members/web-artifacts-builder/SKILL.md`) |
| Simple one-file interactive page or widget | Artifact (simple) | Load `artifact-design`; write one HTML file with pinned CDN React; no scaffold |
| React Native / Expo screen | - | Use the `mobile-app-studio` super-skill (it reuses this skill's composition and re-render rules) |

## Unified workflow

1. **Read the facts first** [nextjs-mastery, react-best-practices, composition-patterns]: `next`, `react`, `react-dom` versions;
   App Router or Pages; `next.config.*` flags (`cacheComponents`, `experimental.optimizePackageImports`, `reactCompiler`); styling
   (Tailwind, shadcn); data layer (Supabase, Prisma, Drizzle); host (Vercel). The version decides which APIs are real - see Version notes.
2. **Draw the server/client line** [nextjs-mastery, server-serialization]: Server Components by default; `'use client'` only on
   interactive leaves, never on a top-level layout or page. Pass the minimum serializable data across the boundary
   [`server-serialization`, `server-dedup-props`].
3. **Plan data with no waterfalls** [async-*, server-*]: start independent work together (`Promise.all`) [`async-parallel`], start
   promises early and await late [`async-api-routes`, `async-defer-await`], check cheap sync conditions before awaiting flags
   [`async-cheap-condition-before-await`], restructure parent/child fetches so they run in parallel [`server-parallel-fetching`,
   `server-parallel-nested-fetching`], and wrap each independent slow section in `<Suspense>` so the shell streams
   [`async-suspense-boundaries`]. Dedup per request with `React.cache()` [`server-cache-react`]; cross-request with a keyed LRU
   [`server-cache-lru`]; non-blocking logging/analytics after the response with `after()` [`server-after-nonblocking`].
4. **Write mutations as public endpoints** [server-auth-actions, nextjs-mastery]: every Server Action and route handler runs
   validate (zod `safeParse`) -> authenticate -> authorize -> mutate -> revalidate (`revalidatePath` / tag API for your version) ->
   return typed state for `useActionState`. Middleware/proxy and layout guards are convenience redirects, not security.
5. **Design the component API before the markup** [composition-patterns]: no boolean mode props; compound components sharing one
   context; the provider is the only place that knows where state lives (interface `{ state, actions, meta }`); explicit variant
   components (`ThreadComposer`, `EditComposer`) instead of flags; `children` over `renderX` props (render props only when the parent
   hands data back, like `renderItem`).
6. **Keep the client cheap** [bundle-*, rerender-*, rendering-*]: direct imports or `optimizePackageImports`; `next/dynamic` for heavy
   widgets; analytics after hydration; no components defined inside components; derive state during render, not in effects; transitions
   for non-urgent updates.
7. **Use the file conventions** [nextjs-mastery]: `loading.tsx` and `error.tsx` for key routes, `not-found.tsx` + `notFound()`, route
   groups `(name)` for organization, parallel routes `@slot` for simultaneous panes, `route.ts` handlers under `app/api/`.
8. **Verify by running** [web-artifacts-builder step 5, the user's rules]: `next build` (read the route table: static vs dynamic, first-load
   JS), run the app on a free local port, click the primary flow, check the browser console and one failure path; Playwright MCP for a screenshot
   or Lighthouse-style check when performance was the goal. Report what you ran.
9. **Report or review** [react-best-practices]: list changes or findings by impact (CRITICAL -> LOW) with the rule id, the file:line,
   and a short before/after.

## Core rules and checklists

**Eliminating waterfalls - CRITICAL** [react-best-practices]
- `async-parallel`: independent awaits go in one `Promise.all`. `async-dependencies`: partial dependencies - start each promise as soon
  as its inputs exist (chain `.then` on the shared promise) before reaching for a helper library.
- `async-defer-await`: move `await` into the branch that uses it. `async-suspense-boundaries`: one boundary per independent slow section.

**Bundle size - CRITICAL** [react-best-practices]
- `bundle-barrel-imports`: barrels cost 200-800 ms per cold start (lucide-react loads ~1,583 modules). In Next.js 13.5+ add
  `experimental.optimizePackageImports: ['lucide-react', '@mui/material', ...]` and keep normal imports; elsewhere import from the
  file path (check the subpath ships types - lucide's deep paths do not). Usual suspects: lucide-react, @mui/*, @tabler/icons-react,
  react-icons, @headlessui/react, @radix-ui/react-*, lodash, ramda, date-fns, rxjs, react-use.
- `bundle-analyzable-paths`: static import and file paths so the bundler and tracer do not pull whole folders.
- `bundle-dynamic-imports` (`next/dynamic` for heavy components), `bundle-conditional` (load on feature activation),
  `bundle-defer-third-party` (analytics/logging after hydration), `bundle-preload` (preload on hover/focus).

**Server - HIGH** [react-best-practices, nextjs-mastery]
- `server-auth-actions`: auth and authorization inside every action (they are public endpoints).
- `server-no-shared-module-state`: never keep request or user data in module-level variables - concurrent renders leak it across users.
  Allowed: immutable config/static assets, correctly keyed shared caches, stateless singletons.
- `server-hoist-static-io`: read fonts, logos, static config once at module level. `server-serialization`: pass only the fields the
  client needs. `server-cache-react`, `server-cache-lru`, `server-after-nonblocking` as in the workflow.
- Middleware/proxy stays lightweight (auth redirect, headers); it runs on every matched request [nextjs-mastery].

**Client data - MEDIUM-HIGH** [react-best-practices]
- `client-swr-dedup`: when data must load on the client, use SWR/React Query (dedup, cache) - never a raw `useEffect` fetch.
- `client-event-listeners`: one shared global listener; `client-passive-event-listeners`: `{ passive: true }` on scroll/touch.
- `client-localstorage-schema`: version and minimize what you store; wrap access in try/catch.

**Re-renders - MEDIUM** [react-best-practices]
- `rerender-no-inline-components`: never define a component inside another (remounts every render).
- `rerender-derived-state-no-effect`: compute from props/state during render; `rerender-derived-state`: subscribe to the derived boolean.
- `rerender-defer-reads`: do not subscribe to state only used inside callbacks; `rerender-use-ref-transient-values`: refs for
  high-frequency values (pointer, scroll).
- `rerender-functional-setstate`, `rerender-lazy-state-init` (`useState(() => expensive())`), `rerender-dependencies` (primitive deps),
  `rerender-split-combined-hooks`, `rerender-move-effect-to-event` (interaction logic in handlers, not effects).
- `rerender-transitions` / `rerender-use-deferred-value`: keep typing responsive under heavy renders.
- `rerender-memo`, `rerender-memo-with-default-value` (hoist `[]`/`{}` defaults), `rerender-simple-expression-in-memo` (no memo for
  cheap primitives) - only without React Compiler or where measured.

**Rendering - MEDIUM** [react-best-practices]
- `rendering-conditional-render`: `cond ? <X/> : null`, not `count && <X/>` (renders a stray 0).
- `rendering-hydration-no-flicker`: inline script for client-only values (theme) before paint; `rendering-hydration-suppress-warning`
  only for expected mismatches (timestamps).
- `rendering-content-visibility` for long lists, `rendering-activity` (`<Activity>`) for show/hide that keeps state,
  `rendering-hoist-jsx` for static JSX, `rendering-animate-svg-wrapper` (animate a wrapping div), `rendering-svg-precision`,
  `rendering-usetransition-loading`, `rendering-resource-hints`, `rendering-script-defer-async`.

**JavaScript hot paths - LOW-MEDIUM** (apply in loops and large lists only) [react-best-practices]: `js-set-map-lookups`,
`js-index-maps`, `js-combine-iterations`, `js-flatmap-filter`, `js-early-exit`, `js-hoist-regexp`, `js-min-max-loop` (no sort for
min/max), `js-tosorted-immutable`, `js-cache-storage`, `js-cache-function-results`, `js-batch-dom-css`, `js-request-idle-callback`.

**Advanced - LOW** [react-best-practices]: `advanced-effect-event-deps` (never list a `useEffectEvent` result as a dependency),
`advanced-event-handler-refs`, `advanced-use-latest`, `advanced-init-once`.

**Composition** [composition-patterns]
- `architecture-avoid-boolean-props` (each boolean doubles the states), `architecture-compound-components`.
- `state-decouple-implementation`, `state-context-interface` (`state`, `actions`, `meta`), `state-lift-state` (siblings outside the
  visual frame read the same provider - no `useEffect` syncing up, no reading state from refs on submit).
- `patterns-explicit-variants`, `patterns-children-over-render-props`.
- `react19-no-forwardref`: on React 19+ `ref` is a normal prop and `use(Context)` replaces `useContext` (and may be called conditionally).

**Next.js checklist** [nextjs-mastery + server rules]
- [ ] Server Components by default; `'use client'` only on interactive leaves.
- [ ] Data fetched on the server with caching set; independent sections in `<Suspense>`.
- [ ] `loading.tsx` / `error.tsx` on key routes; `notFound()` for missing records.
- [ ] Every Server Action: zod validation, auth, authorization, then revalidation.
- [ ] Middleware/proxy limited to redirects, headers, coarse auth.
- [ ] `params` / `searchParams` / `cookies()` / `headers()` awaited (async since Next 15).
- [ ] No request data in module scope; secrets never in `NEXT_PUBLIC_*`.

**Patterns to start from** (merged from nextjs-mastery, react-best-practices, composition-patterns)

```tsx
// Server page: start fetches together, await only what the shell needs, stream the rest.
const getProduct = cache(async (id: string) => db.product.findUnique({ where: { id } })); // React.cache: per-request dedup

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const productP = getProduct(id);
  const reviewsP = getReviews(id);           // started now, awaited inside <Reviews>
  const product = await productP;
  if (!product) notFound();
  return (
    <>
      <ProductHeader name={product.name} price={product.price} />   {/* pass fields, not the whole row */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews promise={reviewsP} />
      </Suspense>
    </>
  );
}
async function Reviews({ promise }: { promise: Promise<Review[]> }) {
  const reviews = await promise;
  return <ul>{reviews.map((r) => <li key={r.id}>{r.text}</li>)}</ul>;
}
```

```ts
// Server Action: validate -> authenticate -> authorize -> mutate -> revalidate -> typed state.
'use server';
const schema = z.object({ name: z.string().min(2).max(100) });
type State = { errors?: Record<string, string[] | undefined>; ok?: boolean };

export async function updateProfile(_prev: State, formData: FormData): Promise<State> {
  const parsed = schema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: parsed.error.flatten().fieldErrors };
  const session = await verifySession();
  if (!session) throw new Error('Unauthorized');
  await db.user.update({ where: { id: session.user.id }, data: parsed.data }); // id from the session, never from the form
  revalidatePath('/profile');
  return { ok: true };
}
```

```tsx
// Compound component with provider-owned state (React 19: use(), ref as a prop).
type ComposerCtx = { state: ComposerState; actions: { update: (fn: (s: ComposerState) => ComposerState) => void; submit: () => void }; meta: { inputRef: React.RefObject<HTMLTextAreaElement | null> } };
const Ctx = createContext<ComposerCtx | null>(null);
function useComposer() {
  const v = use(Ctx);
  if (!v) throw new Error('Composer parts must sit inside a Composer provider');
  return v;
}
export const Composer = { Frame, Input, Footer, Submit }; // each part reads useComposer(); providers decide where state lives
```

**Version notes (verify against the installed version with context7)** - nextjs-mastery's examples date from Next 14/15:
- Next 15: request APIs and route `params` are async; `fetch` is no longer cached by default.
- Next 16: `middleware.ts` is renamed `proxy.ts`; `revalidateTag(tag, profile)` takes a cache-life profile; `updateTag()` gives
  read-your-writes inside Server Actions; Cache Components (`cacheComponents: true` + `'use cache'` with `cacheLife` / `cacheTag`)
  is the new caching model; Turbopack is the default bundler; React 19.2 (`<Activity>`, `useEffectEvent`).
- Older versions keep `middleware.ts` and one-argument `revalidateTag`. Follow what the project runs; propose upgrades separately.

**Artifacts** [web-artifacts-builder + Artifact tool rules]
- Simple page: one HTML file, starts with `<title>` and `<style>`, no `<html>/<head>/<body>` wrapper, React from
  `https://cdnjs.cloudflare.com/ajax/libs/react/18.3.1/umd/...` (pinned), light/dark tokens, works at 400 px.
- Rich app (routing, state, shadcn/ui): in the scratchpad run `bash members/web-artifacts-builder/scripts/init-artifact.sh <name>`
  (React 18 + TS + Vite + Tailwind 3.4.1 + 40+ shadcn components), build, then `bash scripts/bundle-artifact.sh` -> `bundle.html` with
  everything inlined. Before publishing, strip the outer `<html>/<head>/<body>` tags and keep `<title>` first.
- Look: avoid AI-slop defaults - centered-everything layouts, purple gradients, uniform rounded corners, Inter. Take direction from
  `artifact-design` / `frontend-design`.

**Review checklist (order findings by this)**: waterfalls -> bundle -> server security/leaks -> client fetching -> re-renders ->
rendering/hydration -> JS hot paths -> component API (boolean props, prop drilling) -> conventions (loading/error files).

## When members disagree

| Conflict | Resolution |
|---|---|
| "No `useEffect` data fetching; fetch in Server Components" [nextjs-mastery] vs `client-swr-dedup` [react-best-practices] | Server first. Client fetching only for user-driven or after-hydration data, and then through SWR/React Query, never a bare effect. |
| Middleware handles auth redirects [nextjs-mastery] vs "do not rely on middleware" [server-auth-actions] | Middleware/proxy does coarse redirects; the real auth + authorization check lives in every action, route handler and data-access function. |
| Manual `memo` / `useMemo` rules [rerender-memo] vs React Compiler | If `babel-plugin-react-compiler` / `reactCompiler: true` is on, do not add manual memoization; fix structure (inline components, derived state) instead. Without the compiler, apply the memo rules where a render is measurably expensive. |
| React 19 APIs (`use()`, ref as prop) [composition-patterns] vs React 18 scaffold [web-artifacts-builder] | Gate on the installed `react` version: React 19+ use `react19-*`; React 18 keeps `forwardRef` and `useContext`. |
| Next 14-15 APIs in nextjs-mastery vs current Next | The installed version wins; check context7. Never "fix" a working older API into a newer one during an unrelated change. |
| `async-dependencies` recommends the `better-all` package | Try native promise chaining first; adding a dependency is a separate, stated choice. |
| "Testing the artifact is optional, avoid it upfront" [web-artifacts-builder] vs the user's verify-before-done rule | Present fast, but open the artifact once (Playwright screenshot or preview) before sending the link; deeper testing only if asked. |
| init script installs `pnpm` globally and uses `vite@latest` [web-artifacts-builder] vs the user's pin/no-global rules | Check `pnpm -v` first; if missing ask the user before any global install; run npm with `--cache /tmp/npm-cache`; note the unpinned Vite in the report. |
| Bundled `bundle.html` is a full HTML document vs the Artifact tool's no-wrapper skeleton | Strip `<html>/<head>/<body>` before publishing; keep inline `<style>`/`<script>`; nothing loads from non-allowed hosts. |
| `server-cache-lru` (shared cache) vs `server-no-shared-module-state` | Not a real conflict: a shared cache is allowed when keyed by everything that varies (user, tenant, params) and holds no per-request mutable state. |

## Combine with

- Built-in skill `anthropic-skills:web-artifacts-builder` (identical to the member; use either), `artifact-design` (required before any
  artifact), `frontend-design:frontend-design` for visual direction, `dataviz` before any chart.
- Superpowers: `superpowers:test-driven-development` for logic, `superpowers:systematic-debugging` for hydration and caching bugs,
  `superpowers:requesting-code-review` after a feature, `superpowers:verification-before-completion` before done.
- the user's always-on `nextjs-mastery` skill is a member here; when both load, this file's version notes and conflict rules win.
- Sibling super-skills: `mobile-app-studio` (React Native/Expo), `supabase-postgres-pro` (database), `ui-studio` / `web-a11y` (design and
  accessibility), `seo-suite` (metadata, sitemaps).
- Specialist agent prompts (read the file and pass it as the Agent prompt for large, separable work):
  `~/.claude/skill-library/agents/voltagent/02-language-specialists/nextjs-developer.md`,
  `.../02-language-specialists/react-specialist.md`, `.../02-language-specialists/typescript-pro.md`,
  `.../01-core-development/frontend-developer.md`, `.../04-quality-security/performance-engineer.md`,
  `.../04-quality-security/code-reviewer.md`.

## House rules (the user)

- Keep token use low: open single rule files, never the 105 KB `AGENTS.md`; targeted reads of big components; batch edits.
- Pick a free dev-server port; if npm cache permission errors appear, use `--cache /tmp/npm-cache`.
- Production deploys (Vercel `--prod`, promoting a preview, DNS) are live publishes: ask the user first; for changes to a live app or
  dashboard, show old vs new on a review page with their pick before applying.
- Secrets stay server-side: never in `NEXT_PUBLIC_*` or client bundles, never printed in output or logs.
- Run it before calling it done and say what was not run.

## Members

| Member | Best at | Path |
|---|---|---|
| react-best-practices | 70 prioritized React/Next performance rules with incorrect/correct code and impact numbers | `members/react-best-practices/SKILL.md` (rules in `rules/<id>.md`) |
| composition-patterns | Component API design: compound components, provider-owned state, explicit variants, React 19 changes | `members/composition-patterns/SKILL.md` (full text `AGENTS.md`) |
| nextjs-mastery | Compact App Router map: RSC data fetching, ISR/revalidation, middleware, Server Actions with zod, anti-patterns, checklist | `members/nextjs-mastery/SKILL.md` |
| web-artifacts-builder | Scaffold + single-file bundling for React/Tailwind/shadcn claude.ai artifacts | `members/web-artifacts-builder/SKILL.md` (scripts in `scripts/`) |

If a member folder is missing (not installed), work from this file alone.
