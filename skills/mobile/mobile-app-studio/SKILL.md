---
name: mobile-app-studio
description: One skill for every mobile app task - Expo, React Native, EAS and native SwiftUI. Use it to scaffold an Expo app, build Expo Router navigation (tabs, stacks, modals, sheets, headers, search), make native-feeling screens with @expo/ui, follow iOS (HIG) vs Android (Material 3) conventions, set design tokens or fix an app that looks AI-generated, add animations, gestures and haptics, fetch data (React Query, offline, loading/empty/error states), use DOM components, migrate a website to an app, write native modules and config plugins, brownfield, App Clips, dev builds, Expo SDK upgrades, submit to TestFlight, App Store and Google Play, EAS Update OTA and update health, EAS Observe, Workflows CI, Hosting and API routes, cloud simulators, and write or review SwiftUI. Triggers - Expo, EAS, Expo Go, expo-router, React Native, iPhone or Android app, HIG, Material Design, App Store, TestFlight, Play Store, OTA, SwiftUI, Xcode, make it look native, ship my app.
members: [expo-overview, expo-project-structure, expo-router, expo-native-ui, expo-ui, expo-design-system, expo-animation, expo-data-fetching, expo-dom, expo-web-to-native, expo-module, expo-brownfield, expo-app-clip, expo-dev-client, expo-examples, expo-upgrade, eas-app-stores, eas-hosting, eas-observe, eas-simulator, eas-update, eas-update-insights, eas-workflows, swiftui-pro, platform-conventions]
---

# Mobile App Studio

Unifies Expo's 23 official skills (with `expo-overview` as the base router), Paul Hudson's `swiftui-pro` and Owl-Listener's
`platform-conventions` (the iOS HIG vs Material 3 divergence map). Load this file first. It decides the mode,
holds the merged rules that every screen and release needs, and names the one or two member files to open for depth. Do not open member
files the mode table does not name - most of them are long. EAS cloud steps cost money or publish, so they are ask-the user steps.

## Pick the mode

First gate (from expo-overview): it is Expo work when the request says Expo/EAS or `package.json` has an `expo` dependency. A native Swift app
shipped with EAS also counts (route to Ship). A bare React Native app with no `expo` dependency: use the Motion and Data rules, skip the Expo
setup rules. A pure SwiftUI app: mode SwiftUI.

| Task looks like | Mode | Do / open |
|---|---|---|
| "New app", "where do I start", "where does this file go" | Scaffold | `npx create-expo-app@latest` (ask before running: it installs), layout from `members/expo-project-structure/SKILL.md`, then route by goal |
| Build a screen, "make it look native", build from a screenshot or spec | Screens | Component check in `members/expo-ui/SKILL.md` first, then `members/expo-native-ui/SKILL.md`; refs `members/expo-native-ui/references/{controls,icons,visual-effects,media,storage}.md` as needed |
| Tabs, stacks, modals, sheets, links, headers, search, deep links | Navigation | `members/expo-router/SKILL.md`; refs `members/expo-router/references/{tabs,form-sheet,toolbar-and-headers,search,route-structure,zoom-transitions}.md` |
| "Should Android look like iOS?", which pattern on which platform, HIG / Material 3 question, platform review of a design | Platform | Core rules: Platform conventions (stance + divergence map); `members/platform-conventions/SKILL.md` for the full tables; build through `@expo/ui`, which follows each platform by itself |
| Theme, tokens, "screens look inconsistent", "looks AI-generated / generic" | Design system | `members/expo-design-system/SKILL.md`; audit `members/expo-design-system/references/audit.md`, tells `members/expo-design-system/references/native-slop.md` |
| Animation, gesture, sheet drag, press feedback, haptics, "it stutters" | Motion | `members/expo-animation/SKILL.md`, then the matching recipe in `members/expo-animation/RECIPES.md` |
| API calls, React Query/SWR, caching, offline, auth tokens, env vars, loaders | Data | `members/expo-data-fetching/SKILL.md`; refs `members/expo-data-fetching/references/{offline-and-cancellation,expo-router-loaders}.md` (loaders: web, SDK 55+) |
| Reuse a web-only library (charts, editor, syntax highlight) inside the app | DOM | `members/expo-dom/SKILL.md` |
| Turn an existing website / Next.js / Vite app into a native app | Migrate | `members/expo-web-to-native/SKILL.md` + `members/expo-web-to-native/references/{false-friends,native-patterns,verify-on-device}.md` |
| Add Stripe, Clerk, Supabase, maps, SQLite, Skia, OpenAI... | Integrate | `members/expo-examples/SKILL.md` + `members/expo-examples/references/catalog.md` (adapt the pattern, never scaffold over the app) |
| Custom native code, wrap an SDK, config plugin, Info.plist / AndroidManifest edits | Native module | `members/expo-module/SKILL.md`; refs `create-expo-module.md` first, then `native-module.md` / `native-view.md` / `config-plugin.md` |
| Put React Native screens inside an existing Swift/Kotlin app | Brownfield | `members/expo-brownfield/SKILL.md` + `members/expo-brownfield/references/comparison.md`, then `brownfield-isolated.md` or `brownfield-integrated.md` |
| App Clip, AASA, smart app banner | App Clip | `members/expo-app-clip/SKILL.md` (needs paid Apple membership; ask) |
| Dev build, custom Expo Go, "native module not in Expo Go" | Dev build | `members/expo-dev-client/SKILL.md` (local build free; EAS build ask) |
| Upgrade SDK, dependency conflicts, expo-av / React Navigation migration | Upgrade | `members/expo-upgrade/SKILL.md` + the matching ref (`react-19`, `new-architecture`, `react-compiler`, `native-tabs`, `expo-av-to-*`, `react-navigation-to-expo-router`) |
| Build/submit, TestFlight, App Store, Play Store, versions, signing, store listing | Ship | `references/ship-and-operate.md` (this skill), then `members/eas-app-stores/SKILL.md` + its `testflight.md`, `ios-app-store.md`, `play-store.md`, `app-store-metadata.md`, `native-ios.md` |
| OTA update, "my build still shows old code", channels/branches/runtime version | OTA | `references/ship-and-operate.md`, then `members/eas-update/SKILL.md` |
| "Is the update healthy", crash rate, adoption, embedded vs OTA users | Update health | `members/eas-update-insights/SKILL.md` |
| Slow startup, TTI, launch metrics, JS errors and native crashes in production | Observe | `members/eas-observe/SKILL.md` + `members/eas-observe/references/{setup,metrics,queries}.md` |
| `.eas/workflows/*.yml`, CI/CD, PR previews | CI | `members/eas-workflows/SKILL.md` |
| Deploy the Expo web build, `+api.ts` API routes, hosting env vars, domains | Hosting | `members/eas-hosting/SKILL.md` |
| Run on a cloud/remote simulator, agent-driven device session | Cloud sim | `members/eas-simulator/SKILL.md` + `members/eas-simulator/references/run-your-app.md` (on the user's Mac a local simulator is the default) |
| Write, fix or review SwiftUI / Swift code | SwiftUI | `members/swiftui-pro/SKILL.md`; load only the refs that match (`api`, `views`, `data`, `navigation`, `design`, `accessibility`, `performance`, `swift`, `hygiene`, `resizability`, `localization`) |

Bare file names in a row (`testflight.md`, `react-19`) live in that row's member `references/` folder; `references/ship-and-operate.md`
is this skill's own merged runbook.

Vague asks (expo-overview): "make it look native" = Screens (+ Navigation, Motion); "clean up the styling / set a theme" = Design system;
"ship it / get an .ipa or .apk" = Ship; "put my Swift app on TestFlight" = Ship via `native-ios.md`. Most tasks need 1-3 modes; open their
files in the order Screens -> Navigation -> Data -> Motion so structure comes before polish.

## Unified workflow

1. **Read the project before choosing anything** [expo-overview, expo-design-system "Adopt before you build", swiftui-pro]. Collect in one
   pass: `expo` version in `package.json` (= SDK), `app.json` / `app.config.*`, committed `ios/` + `android/` (CNG vs prebuild/bare),
   `eas.json` and `extra.eas.projectId`, styling library (NativeWind, Tamagui, Restyle, Unistyles), existing theme file
   (`theme.ts`, `src/theme/`, `constants/Colors.ts`), React version. For SwiftUI: deployment target, Swift version, Xcode. Read docs for
   that SDK, not `latest` (`https://docs.expo.dev/versions/v56.0.0/...`), or use context7.
2. **Classify and confirm only what matters** [expo-overview]. Map the goal to modes with the table. Ask the user only when the goal is ambiguous,
   when a step costs money or publishes, or when it adds a third-party framework to a native Swift app [swiftui-pro]. Implementation choices
   (component, curve, duration) you make yourself and state in one line [expo-animation]. For an app that ships on both platforms, set the
   platform stance once (Core rules: Platform conventions; hybrid by default) and note it in the project's theme folder [platform-conventions].
3. **Pick the cheapest run target that proves the change** [expo-native-ui, expo-dev-client, expo-animation]:
   Expo Go (SDK 56+ runs `@expo/ui` universal and DOM components) -> local dev build `npx expo run:ios` (free, needs Xcode) ->
   EAS cloud build (paid: ask). A dev build is required for local Expo modules, Apple targets (widgets, clips), native modules Expo Go
   lacks, config plugins, remote push and universal links. Judge motion only on a release build.
4. **Structure first** [expo-project-structure, expo-router]. New app: `src/app` holds routes only; screen bodies in `src/screens/`,
   shared UI in `src/components/`, server code in `src/server/` + `src/app/api/`. Existing app: keep its layout, never migrate it.
   Navigation is configured, never rebuilt: native Stack, `NativeTabs`, `presentation: "modal" | "formSheet"`, `Stack.SearchBar`,
   `Link.Preview` / `Link.Menu`.
5. **Build each screen down the component ladder** [expo-ui, expo-native-ui, expo-web-to-native]: (a) `@expo/ui` universal component
   (one tree, iOS/Android/web) -> (b) `@expo/ui/swift-ui` or `/jetpack-compose` in a `.ios.tsx` / `.android.tsx` file under
   `components/` -> (c) React Native built-ins / community library. List what is installed with
   `node members/expo-ui/scripts/list-components.js <project>` (reads local `node_modules` only). Values come from the one theme
   [expo-design-system]; colors are semantic [expo-native-ui]. Every data screen gets four states [expo-data-fetching].
6. **Add motion last, through the gate** [expo-animation]: frequency tier -> named purpose -> cheapest tool -> transform/opacity -> spring
   if a finger is involved -> UI thread -> reduced motion in the same change. Zero lines of motion is a valid result.
7. **Integrations and native code** [expo-examples, expo-module]: look up the `with-<lib>` example first (check `meta.json` for renamed or
   deprecated ones; default branch is `master`), read it in the session scratchpad - never scaffold it over the user's project - then add only
   missing deps with `npx expo install` (never copy its pinned versions), merge config plugins and permissions, recreate env var shapes.
   Need native code: config plugin or local module via `create-expo-module`, then a dev build.
8. **Quality gate before calling it done** (merged checklist below) [expo-native-ui, expo-design-system, expo-animation,
   expo-web-to-native, swiftui-pro]. Run it, do not just compile it: a green `expo export` only proves the bundle builds.
9. **Ship and operate** (`references/ship-and-operate.md`) [eas-update, eas-app-stores, eas-update-insights, eas-observe]: decide OTA vs
   new binary by the runtime rule, show the user the exact command + target + cost, run, then verify the furthest real state (build ID, Apple
   processing, tester access, update adoption, crash rate) instead of "the command succeeded".
10. **Report** [expo-animation "Output", swiftui-pro "Output Format"]: the code is the deliverable; then 2-4 lines: what was exercised,
    what could not be run, what to feel-check on device (flick, interrupt, reverse, slowest Android).

Migration sub-flow [expo-web-to-native]: assess -> write `migration-progress.md` (bucket each screen: port-as-is, nativize-now,
nativize-later, hybrid) -> scaffold shell mirroring routes -> every screen as a DOM component (shippable day one) -> nativize by value,
one screen per pass (redesign, do not reskin) -> wire data/auth/storage -> ship. Payments are a business fork: in-app digital goods need
store IAP (RevenueCat, ~30%), not Stripe - raise it with the user during assess, not at review.

## Core rules and checklists

**Setup and versions**
- Install with `npx expo install <pkg>` so versions match the SDK; if npm cache permission errors appear, prefix `npm_config_cache=/tmp/npm-cache` [expo-overview].
- SDK upgrades are their own task [expo-upgrade]: from SDK 55 or earlier skip 56 and go straight to 57 at `expo@57.0.9` or later (Hermes V1
  memory regression with reanimated/worklets); never toggle Hermes off the SDK default; then `npx expo install --fix`, `npx expo-doctor`.
- SDK 54+: `react-native-worklets` installed with Reanimated; React Compiler via `"experiments": { "reactCompiler": true }`. SDK 56+: import
  React Navigation only through `expo-router/react-navigation`; `headerLargeTitleEnabled` replaces `headerLargeTitle`. Keep `expo-constants`
  a direct dependency when `expo-router` is installed. New Architecture is the default; Reanimated 4 requires it.
- `npx expo prebuild --clean` only for CNG/prebuild projects; never prebuild a manually maintained native host [expo-upgrade, expo-brownfield].
- EAS auth only for cloud steps: `eas whoami`, `eas login`, `eas init` when `projectId` is missing [expo-overview].

**Files and code style** [expo-project-structure, expo-router, expo-native-ui]
- Kebab-case file names, no special characters, `@/*` path aliases, imports at the top. App must always have a route matching `/`.
- Remove old route files when moving routes. Platform files (`.ios/.android/.native/.web`) need identical props and a default file; they
  do not work for route files, so keep them in `components/`.
- Complex component -> folder with `index.tsx` and colocated private parts. Tests next to the file (`format-date.test.ts`).

**Library swaps (old -> use)** [expo-native-ui, expo-upgrade, expo-animation, expo-ui, expo-data-fetching]

| Old | Use |
|---|---|
| `expo-av` | `expo-audio`, `expo-video` |
| `expo-permissions` | each package's permission API |
| `@expo/vector-icons` | `expo-symbols` `SymbolView` on iOS + Material icons on Android (never SF-only) |
| `AsyncStorage` | `expo-sqlite/localStorage/install`; secrets and tokens in `expo-secure-store` |
| RN `SafeAreaView` | `contentInsetAdjustmentBehavior="automatic"` or `react-native-safe-area-context` |
| `Platform.OS`, `useContext`, `<img>`, `Dimensions.get()` | `process.env.EXPO_OS`, `React.use`, `expo-image`, `useWindowDimensions` |
| core `Animated`, `PanResponder`, `runOnJS` | Reanimated 4, `Gesture.Pan()`, `scheduleOnRN` from `react-native-worklets` |
| `TouchableOpacity` | `Pressable` with per-role feedback |
| shadow* / `elevation` props | `boxShadow: "0 1px 2px rgba(0,0,0,0.05)"` |
| `expo-linear-gradient` | `experimental_backgroundImage` CSS gradients (New Arch) |
| raw `PlatformColor` | `Color` from `expo-router` |
| `@gorhom/bottom-sheet`, RN Picker/Switch | `@expo/ui` `BottomSheet` (`isPresented` / `onDismiss`), `Picker`, `Switch` |
| axios | `expo/fetch` |

**Screen rules** [expo-native-ui, expo-ui, expo-design-system]
- Wrap every `@expo/ui` tree in `Host` (imported from `@expo/ui` root). `@expo/ui/swift-ui` crashes on Android and vice versa.
- `@expo/ui` `List` is grouped settings rows, not virtualized: feeds, search results and catalogs use `FlatList` / `FlashList`.
- Scrollable route: the ScrollView/FlatList is the first child with `contentInsetAdjustmentBehavior="automatic"`; never an outer
  ScrollView around a FlatList; pad with `contentContainerStyle` + `gap`. Account for top and bottom safe areas.
- Titles come from the stack header, never a custom `<Text>`. `borderCurve: "continuous"` on rounded corners (not capsules).
- `<Text selectable>` on data and error text; `fontVariant: ['tabular-nums']` on counters; format big numbers (1.4M, 38k).
- Forms: `keyboardShouldPersistTaps="handled"`; the primary action never sits under the keyboard (`react-native-keyboard-controller`).
- Every enabled control does what it says (search filters, Save commits). Empty handlers and success alerts are not implementations.
- Each platform wears its own idiom: HIG on iOS, Material 3 on Android; no FAB/ripple on iOS, no iOS chevrons/switches on Android
  (pattern-by-pattern map in "Platform conventions" below).
- Colors: `Color.ios.*` / `Color.android.dynamic.*` in `Platform.select` with a `default` hex for web, centralized in `theme/colors.ts`.
  On Android call `useColorScheme()` in components that render them. Never pass `Color` values into Reanimated styles.

**Platform conventions** [platform-conventions, mapped to Expo by expo-ui, expo-router, expo-native-ui, expo-animation, expo-design-system]
- Stance, decided once per app. Default is hybrid: the app looks like itself and behaves like the OS, so one visual language (brand
  color, type, illustration, card style) sits on platform-native navigation, system controls, gestures, confirmations and icons. Go
  strictly native per platform when platform fluency signals quality (finance such as the user's lending and debt-relief brands, health,
  utilities), when the app leans on OS features (share sheet, widgets, Siri / Google Assistant), or for power users. A unified look is
  fine for B2B or internal tools and cross-device continuity, but back navigation, system controls and text scaling stay native anyway.
- In doubt about one pattern: use what ships in the OS; read the current HIG or Material 3 page for that pattern only (context7 or
  WebFetch; both change often) and look at how two or three native apps on each platform handle the same interaction.
- A design system for both platforms keeps a component map next to the theme: system name | iOS name / API | Android name / API | implementation.

| Pattern | iOS (HIG) | Android (Material 3) | Build with |
|---|---|---|---|
| Back | Edge swipe from the left + back button top-left; the edge is reserved | System back gesture from either edge, predictive back, app-bar arrow | Native Stack; keep `gestureEnabled` on and guard unsaved edits with a discard confirm; never hijack Android back except to close an in-screen overlay |
| Top level | Tab bar, up to 5 labeled tabs; sidebar on iPad | Navigation bar, 3-5 labeled destinations; rail or drawer on large screens | `NativeTabs` (each platform's own bar) |
| Destructive confirm | Alert or action sheet, red destructive option, anchored to its trigger | Dialog with text buttons, error tone for the destructive one | `Alert.alert` with a `style: "destructive"` button, SwiftUI `confirmationDialog`; only for rare irreversible actions, undo for routine ones (native-slop #10) |
| Date and time | Wheel or inline calendar | Calendar dialog with a text-input option | `@expo/ui/community/datetime-picker` |
| Pick from a list | Menu, picker or action sheet | Exposed dropdown or modal bottom sheet | `@expo/ui` `Menu`, `Picker` |
| Primary action | Contextual buttons in toolbar or content; no FAB | FAB, bottom right, for the one primary action | `.ios.tsx` / `.android.tsx` component when they differ |
| Long press | Context menu with preview | Selection mode or contextual actions | `Link.Menu` / `Link.Preview` |
| Swipe on a row | Swipe actions (delete) | Swipe to dismiss or archive, by context | Swipe-to-delete recipe in `members/expo-animation/RECIPES.md`; SwiftUI `swipeActions` |
| Sheet | Slides up with a grab handle | Standard or modal bottom sheet, or full-screen dialog | `formSheet` + `sheetGrabberVisible` (iOS only: give Android another drag cue) or `@expo/ui` `BottomSheet` |
| Switch | Pill switch, right-aligned in rows | Thumb-and-track switch | `@expo/ui` `Switch` |
| Type | SF Pro, text styles (Large Title, Title 1-3, Headline, Body...), Dynamic Type | Roboto, roles Display / Headline / Title / Body / Label, `sp` with font scale | System font unless the brand says otherwise; the default ramp follows iOS styles, map it to M3 roles on Android; scaling always on |
| Icons | SF Symbols | Material Symbols (outlined, rounded, sharp) | `expo-symbols` + Material icons (swap table) |
| Shape, color | Continuous ("squircle") corners; system dynamic colors | Prominent M3 rounding; Material You color from the wallpaper | `borderCurve: "continuous"`; `Color.ios.*` / `Color.android.dynamic.*` |

**Tokens and components** [expo-design-system]
- One theme entry point. A literal used twice becomes a token; one-offs stay inline with a comment. Adopt an existing system in its own idiom.
- Default scales: spacing 4/8/16/24/32/48 (4-pt grid, add 12 or 20 only if they recur); type ramp largeTitle 34/700, title 22/600,
  headline 17/600, body 17/400, subhead 15, caption 12; radius 8/12/16/9999; shadows card/raised/overlay; motion 150/250/400 ms.
- Brand colors only as light/dark pairs through a hook (`useBrandColors`); keep them out of static token files.
- Component contract: variants, sizes (default `md`), states (default, pressed, disabled, loading), `style` merged last, accessibility
  role/state/label (icon-only and spinner buttons need explicit labels). Content props growing -> take `children`.
- Extract into `src/components/` only when it appears on 2+ screens, has a nameable role, and its API is smaller than its implementation.
- Never `allowFontScaling={false}` app-wide; let rows grow with Dynamic Type.

**Motion** [expo-animation]
- Gate: 100+ times/day (tab switch, keyboard, toggles) -> no animation; tens/day -> under 150 ms or nothing; occasional -> standard;
  rare -> delight budget. Tabs never slide (`animation: 'none'`). No nameable purpose -> do not build it.
- Tool ladder: Reanimated CSS transition -> CSS animation -> layout animations -> shared value + Gesture -> native stack options /
  `formSheet` / `NativeTabs` / `Link.Preview` / `RefreshControl` / keyboard-controller -> Lottie (illustration only) -> Skia.
- Animate `transform` and `opacity`; others re-run layout (exception: absolutely positioned childless element). Never `scale(0)`:
  start at 0.95 + opacity 0. Never animate BlurView intensity or Android elevation.
- Springs when a finger was involved: settle `{ duration: 400, dampingRatio: 1 }`, snap back `{ duration: 400, dampingRatio: 0.8, velocity }`,
  sheet `{ duration: 300, dampingRatio: 0.8, velocity }`. Easing: out `Easing.bezier(0.23, 1, 0.32, 1)`, in-out `(0.77, 0, 0.175, 1)`,
  iOS sheet `(0.32, 0.72, 0, 1)`; CSS styles use `cubicBezier(...)`, never the string. Never ease-in on UI. Press 100-150 ms, toggle 150-200 ms.
- Never `setState` in a gesture/scroll handler; `scheduleOnRN` only in `onEnd` or a threshold `useAnimatedReaction`; shared values via
  `.get()/.set()`, never read or written during render; helpers called from worklets start with `'worklet'`.
- Press: feedback on press-in; buttons `scale: 0.97` (or dim), full-width rows highlight instead; 44x44 pt / 48 dp targets via `hitSlop`.
- Haptics: selection tick / light snap / medium heavy / success-error; same frame as the visual, one per user action, never the only feedback.
- `GestureHandlerRootView` at the root; `CADisableMinimumFrameDurationOnPhone: true` for 120 fps; reduced motion keeps opacity/color, drops movement.

**Data** [expo-data-fetching]
- Four states: loading, error, empty, content. Loading is not empty; empty explains and offers the next action (`ListEmptyComponent`).
  Refetch errors keep stale data with an inline retry; `isLoading` for first load, `isFetching` for background.
- Gate the root layout on hydration of persisted auth/onboarding state before redirecting.
- Saves: disable resubmit while pending, keep the draft on failure, dismiss only after success, undo optimistic edits on failure.
- Always check `response.ok`; typed errors; backoff retries; React Query defaults `staleTime: 5 min`, `retry: 2`.
- `EXPO_PUBLIC_*` is public and inlined at build time - never secrets there; secrets live in `+api.ts` routes / server env.

**DOM components** [expo-dom]: `'use dom'` at top, one default export per file, serializable props, CSS imported in that file, async
function props for native actions, router hooks read in the native parent and passed as props, no `_layout` as DOM. Each DOM screen
carries ~2 MB of web runtime, so keep them to the parts that need the web.

**Native modules, brownfield, App Clip** [expo-module, expo-brownfield, expo-app-clip]
- Scaffold with `create-expo-module` (`--platform`, `--features Constant,Function,AsyncFunction,Event,View,ViewEvent,SharedObject`);
  add a platform with `add-platform-support`. In `expo-module.config.json` iOS lists the class name, Android the fully qualified name.
- Brownfield: inspect the host's entry, navigation owner, build system and RN versions first. Isolated (AAR/XCFramework) when the native
  team must not install Node/RN or repos release separately; integrated when one team owns both. Accept only after a Release host build
  with Metro stopped: open with input, return a result, dismiss, reopen.
- App Clip: `@bacons/apple-targets` target in `targets/clip/`, associated domains on both targets, AASA (no extension) with an `appclips`
  block, Clip `deploymentTarget: "17.6"`, mirror permission keys, header image 1800x1200 PNG without alpha, max 3 invocation URLs.

**SwiftUI** [swiftui-pro]
- Check the deployment target first; newer API only behind `#available` within that target. New apps default to iOS 27; Swift 6.4+ concurrency.
- `@Observable` classes marked `@MainActor`; `@State private` and initialized in one place; avoid `ObservableObject`/`@Published` unless unavoidable.
- Modern API: `foregroundStyle`, `clipShape(.rect(cornerRadius:))`, `Tab` API, two- or zero-parameter `onChange`, `NavigationStack`,
  `toolbarVisibility`, semantic toolbar placements, `sensoryFeedback`, `@Entry`, builder-closure `overlay/background/mask`, native `WebView` (iOS 26+).
- Structure: one type per file; extract subviews into `View` structs instead of `some View` computed properties; button actions in methods.
- Design: `ContentUnavailableView` for empty/search, `Label` over icon+text HStacks, `bold()` over `fontWeight(.bold)`, no `UIScreen.main`,
  44x44 taps, `ViewThatFits` for tight layouts, keep features at every window size (iPad, folding iPhone Duo).
- Text: interpolate, never `+` concatenation; filter with `localizedStandardContains`; `FormatStyle` instead of `String(format:)`.
- Full review order (one ref each): api -> views -> data -> navigation -> design -> resizability -> accessibility -> localization ->
  performance -> swift -> hygiene; `performance-plus.md` only for a requested deep performance review.
- Review output: findings by file -> line -> rule -> short before/after; end with a prioritized summary. Report real problems only; during
  feature work suggest unrelated modernization separately instead of applying it.

**Quality gate (run before "done")** [merged from expo-native-ui, expo-design-system, expo-animation, expo-data-fetching, expo-web-to-native, swiftui-pro]
1. Walk the primary task end to end, including one failure and recovery for anything that loads or saves.
2. Try long titles, missing images, zero results, large system text, dark mode flip, keyboard open, back/swipe-dismiss.
3. Screenshot and self-critique: hierarchy, proximity, repetition (corners/shadows/accents match), alignment. Fix in the token or shared
   component, then recheck the render.
4. Scan for native-slop tells: Web Modal, X-Button Sheet, Emoji Iconography, Purple-Gradient Hero, Floating Pill Tab Bar, Inter Everywhere,
   Everything's a Card, Shadowboxing, Wireframe Borders, alert() Confirmation, Hand-Rolled Header, 16-Everything, Squish Reflex, Grand
   Entrance, Onboarding Carousel, Cross-Platform Costume, Safe-Area Collision, Dark-Mode Amnesia, Spinner Blink, Keyboard Blindness
   (grep checks in `members/expo-design-system/references/native-slop.md`). Treat them as prompts, not bans on the user's brief.
5. Motion: reduced motion on, interrupt mid-flight, reverse, flick; record video for motion, stills for static state.
6. Platform pass, on iOS and Android (or name the one not run): back gesture and system back work everywhere, confirmations, pickers,
   menus, sheets, tab labels and icons follow the divergence map, largest text size still fits. Gestures and haptics need a physical
   device: ask the user to feel-check on their phone when only the simulator ran [platform-conventions].
7. Say what you exercised and what you could not run.

## When members disagree

| Conflict | Resolution |
|---|---|
| "Always try Expo Go first" [expo-native-ui] vs "dev clients are the setup for any real app" [expo-dev-client] | Prototype and UI iteration: Expo Go. As soon as the app needs anything on the dev-build list or is headed to the stores: local dev build (free). Performance and feel: release build only [expo-animation]. |
| Inline styles [expo-native-ui] vs `StyleSheet.create` at the file bottom [expo-project-structure] | Follow the project's existing convention. New app: inline style objects for one-offs, `StyleSheet.create` at the bottom when a style is reused in the file. Values always come from tokens. |
| Sheet: `@expo/ui` BottomSheet [expo-ui] vs `formSheet` route [expo-router, expo-animation] vs drag-to-dismiss recipe [expo-animation] | Sheet that is its own screen/URL -> `formSheet`. In-screen panel (map pin, detail) -> `@expo/ui` BottomSheet. Custom gesture sheet only for a signature interaction neither can express. |
| `@expo/ui` List [expo-ui] vs FlatList [expo-native-ui] | Short fixed groups -> List. Large or unknown length -> FlatList/FlashList. |
| "Use haptics to delight" [expo-native-ui] vs strict haptic rules [expo-animation] | expo-animation's rules win: one per user action, same frame, never the only feedback. |
| `scale 0.97` on pressables [expo-animation] vs "Squish Reflex" tell [expo-design-system] | Buttons scale or dim; full-width rows highlight their background; never `TouchableOpacity`. |
| "Make the call, never offer a menu" [expo-animation] vs "confirm intent if ambiguous" [expo-overview] vs "ask before new frameworks" [swiftui-pro] | Ask about goals, costs, publishing and new dependencies; decide implementation details yourself and give the reason in one line. |
| Tailwind "not supported, use inline styles" [expo-native-ui] vs "Tailwind projects keep tokens in global.css" [expo-design-system] | Project already on NativeWind: follow it. New app: do not add Tailwind (the `expo-tailwind-setup` skill the router mentions is not part of this kit). |
| "Start the cloud sim without asking again" [eas-simulator] vs the user's ask-first rule | On the user's Mac use a local simulator. The user explicitly asking for a cloud sim = approval for that one session with a `--max-duration-minutes` cap; always stop it after. |
| "Install agent-browser and argent, do not fall back" [expo-web-to-native] vs the user's install rules | Ask the user with the exact install command. Until the user says yes, verify web with Playwright MCP and native with the local Simulator (`xcrun simctl io booted screenshot`). |
| "Run the migration as a `/goal` loop" [expo-web-to-native] vs cost awareness | Unattended loops only with the user's OK; default is one screen per turn with a progress file. |
| `npm install -g eas-cli` [eas-app-stores] vs `npx --yes eas-cli@latest` [eas-simulator] | No global installs without the user's OK. Use `npx eas-cli@<version>` pinned to what `eas --version` or the task needs (submission commands need 23.2.0+). |
| "Avoid UIKit" [swiftui-pro] vs UIKit brownfield hosts [expo-brownfield] | Keep the host's existing UIKit; do not add new UIKit inside SwiftUI code. |
| Every member's "Submitting Feedback" footer (`npx submit-expo-feedback`) | Dropped: it sends data to Expo. Run it only if the user asks. |
| "A unified cross-platform design is appropriate" [platform-conventions] vs "Cross-Platform Costume" tell and per-platform idiom [expo-design-system, expo-native-ui] | Hybrid by default: unify the visual language, keep navigation, system controls, gestures, confirmations and icons native. A fully unified look only for B2B/internal or continuity-driven apps, and even then back, controls and text scaling stay native. |
| iOS tabs "no labels required" [platform-conventions] vs HIG and `NativeTabs` practice | Dropped: label tabs on both platforms. |
| "Read the current HIG / M3 before each major design phase" [platform-conventions] vs cost awareness | Read only the page for the pattern in doubt, via context7 or WebFetch; the divergence map covers the rest. |
| "Test on real devices for each platform" [platform-conventions] vs local simulator default | Simulator for layout and flow; gestures, haptics and motion feel need a physical device, so ask the user for a feel-check and say which platform was not run. |

## Combine with

- Superpowers: `superpowers:brainstorming` before a new app or big screen set, `superpowers:writing-plans` for migrations,
  `superpowers:systematic-debugging` for crashes and "update not showing", `superpowers:verification-before-completion` before done.
- `react-next-pro` super-skill for shared React rules (composition, re-renders, React 19) and Expo web; `supabase-postgres-pro` for a
  Supabase backend; `dataviz` before any chart.
- `ux-lab` super-skill as the reviewer (Jakob's law, critique of a rendered screen, usability tests of a flow); `ui-studio` for the web
  side and responsive breakpoints; `brand-studio` for the app icon master and brand palette.
- Docs: context7 MCP (pin the SDK version); Playwright MCP for web-side parity checks; swift-lsp / typescript-lsp plugins (always on).
- Specialist agent prompts (read the file, pass it as the Agent prompt, use only for genuinely large work):
  `~/.claude/skill-library/agents/voltagent/02-language-specialists/expo-react-native-expert.md`,
  `.../02-language-specialists/swift-expert.md`, `.../07-specialized-domains/mobile-app-developer.md`,
  `.../04-quality-security/accessibility-tester.md`, `.../04-quality-security/performance-engineer.md`.

## House rules (the user)

- EAS cloud builds, submits, production OTA publishes, hosting `--prod` deploys, Observe on a paid tier, simulator sessions and
  workflow runs cost money or publish: show the exact command, target and cost note, and run only after the user says yes. Local builds,
  Expo Go, `--help`, `eas whoami` and read-only `:list` / `:insights` queries are fine.
- Keep token use low: open only the member files the mode names; read the big references (webgpu-three 605 lines, brownfield-integrated
  551, observe setup 529, app-store-metadata 497) by section.
- Store listings, TestFlight external testers and production updates are public changes to a live system: present old vs new on a
  review page with the user's pick before applying.
- Never print or commit `EXPO_TOKEN`, App Store Connect keys, Google service-account JSON or `.env.eas-simulator` (holds a session
  token; add it to `.gitignore`).
- Pin versions, no `curl | bash`, no global installs, Expo skill telemetry stays off (`EXPO_SKILLS_TELEMETRY` unset, no
  `submit-expo-feedback`).
- Verify by running before reporting done, and say what was not run.

## Members

| Member | Best at | Path |
|---|---|---|
| expo-overview | Router, Expo-vs-not gate, shared setup rules, vague-ask translation | `members/expo-overview/SKILL.md` |
| expo-project-structure | New-app folder skeleton (routes-only app/, screens/, server/) | `members/expo-project-structure/SKILL.md` |
| expo-router | Native Stack, NativeTabs, sheets, Link preview/menus, headers, search | `members/expo-router/SKILL.md` |
| expo-native-ui | Screen styling rules, semantic colors, controls, icons, media, storage, effects | `members/expo-native-ui/SKILL.md` |
| expo-ui | `@expo/ui` native SwiftUI/Compose components and drop-in replacements | `members/expo-ui/SKILL.md` |
| expo-design-system | Tokens, component contract, drift audit, 20 native-slop tells | `members/expo-design-system/SKILL.md` |
| expo-animation | Motion decision sequence, spring/easing tables, UI-thread rules, haptics, recipes | `members/expo-animation/SKILL.md` |
| expo-data-fetching | Four screen states, React Query, auth tokens, env vars, offline, loaders | `members/expo-data-fetching/SKILL.md` |
| expo-dom | `'use dom'` components for web-only libraries | `members/expo-dom/SKILL.md` |
| expo-web-to-native | Strangler-fig website-to-app migration with worklist and parity checks | `members/expo-web-to-native/SKILL.md` |
| expo-module | Expo Modules API (Swift/Kotlin), native views, config plugins, lifecycle | `members/expo-module/SKILL.md` |
| expo-brownfield | RN inside existing native apps, isolated vs integrated | `members/expo-brownfield/SKILL.md` |
| expo-app-clip | iOS App Clip target, AASA, smart app banner, Clip metadata | `members/expo-app-clip/SKILL.md` |
| expo-dev-client | Development builds, local vs EAS, installing on sim/device | `members/expo-dev-client/SKILL.md` |
| expo-examples | Canonical `with-*` integration patterns, non-destructive adaptation | `members/expo-examples/SKILL.md` |
| expo-upgrade | SDK upgrade steps, Hermes warning, deprecated packages, migration refs | `members/expo-upgrade/SKILL.md` |
| eas-app-stores | Build/submit to TestFlight, App Store, Play; versions; metadata; native iOS | `members/eas-app-stores/SKILL.md` |
| eas-hosting | Expo web + `+api.ts` routes on EAS Hosting (Cloudflare Workers) | `members/eas-hosting/SKILL.md` |
| eas-observe | Startup/TTI metrics, errors, crashes, `eas observe:*` queries | `members/eas-observe/SKILL.md` |
| eas-simulator | Remote iOS/Android simulator sessions driven by agent-device | `members/eas-simulator/SKILL.md` |
| eas-update | OTA model (build/update/branch/channel/runtime), publish, test, debug | `members/eas-update/SKILL.md` |
| eas-update-insights | Update crash rate, adoption, embedded vs OTA split | `members/eas-update-insights/SKILL.md` |
| eas-workflows | EAS workflow YAML from the live schema, `workflow:validate` | `members/eas-workflows/SKILL.md` |
| swiftui-pro | Modern SwiftUI/Swift review: API, data flow, design, accessibility, performance | `members/swiftui-pro/SKILL.md` |
| platform-conventions | iOS HIG vs Material 3 divergence tables (navigation, controls, type, gestures, visuals), when to go native vs unified vs hybrid, platform don'ts | `members/platform-conventions/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
