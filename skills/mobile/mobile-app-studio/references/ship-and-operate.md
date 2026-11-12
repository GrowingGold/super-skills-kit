# Ship and operate - merged EAS runbook

Merged from eas-app-stores, eas-update, expo-dev-client, eas-update-insights, eas-observe, eas-hosting, eas-workflows and
eas-simulator. Every step marked **ASK** costs EAS plan resources or publishes to users: show the user the exact command, the target
(project, profile, channel, platform, environment) and the cost note, then wait for their yes. Read-only steps run freely.

## 0. Preflight (free)

1. `eas whoami` (or `npx eas-cli@<pinned> whoami`); `extra.eas.projectId` present, else `eas init` (**ASK**: creates a remote project).
2. Read `eas.json`: profiles, `appVersionSource`, existing channels. Preserve existing identifiers and channel assignments.
3. Detect the project path [eas-app-stores]:
   - Expo / React Native app -> sections 1-3.
   - SwiftUI/UIKit app with no RN runtime -> `members/eas-app-stores/references/native-ios.md` first; Xcode project stays the source of truth.
   - Native Android app -> keep its build; submission via `members/eas-app-stores/references/play-store.md`.
   - RN screens inside a native app -> `members/expo-brownfield/SKILL.md`, come back here for distribution.
4. Decide **OTA or new binary** [eas-update]: JS, styles and bundled assets the installed runtime supports -> OTA. Anything that adds or
   changes native code or native config (most new native libraries, SDK upgrades, permissions, plugins) -> new build. Never change the
   runtime-version policy as a side fix; it decides which installed builds can receive future updates.

## 1. Builds

| Need | Command | Cost |
|---|---|---|
| Local dev client | `npx expo run:ios` / `run:android`, or `eas build -p ios --profile development --local` | free (needs Xcode / Android SDK) |
| Cloud dev client | `eas build -p ios --profile development` | **ASK** |
| Store build | `npx eas-cli@<v> build -p ios|android --profile production` | **ASK** |
| Build + submit | add `--auto-submit` (iOS: App Store Connect; Android: track in `submit.production`) | **ASK** |
| Expo/RN quick TestFlight | `npx testflight` | **ASK** |

- Profiles: `"appVersionSource": "remote"` + `"autoIncrement": true` on production; development profile has `"developmentClient": true`
  and `"distribution": "internal"` [eas-app-stores, expo-dev-client].
- Signing problems: `eas credentials`; stale cache: `--clear-cache`.
- Install local builds: `xcrun simctl install booted <App.app>`, `adb install build.apk`; device via Xcode Devices window.
- Native iOS: when versioning, bundle IDs or icons change, inspect the archived `CFBundleVersion` - the remote counter alone does not prove
  Xcode used it [eas-app-stores native-ios.md].

## 2. Submit and verify the real state

- iOS credentials: App Store Connect API key preferred over Apple ID auth (`members/eas-app-stores/references/ios-app-store.md`).
- Android: service account JSON linked in Play Console; tracks internal -> closed -> open -> production; staged rollout options in
  `play-store.md`. The key file path lives in `eas.json`; never print or commit the file.
- A finished build or a queued submission is not Apple acceptance. Verify in order and report the furthest verified state with the exact
  build ID and version: build finished -> submission accepted -> Apple processing done -> TestFlight testers can install -> review
  state (`members/eas-app-stores/references/testflight.md`). `eas submit:list -p ios --json` / `submit:view <id> --json` need EAS CLI 23.2.0+.
- Store listing text and screenshots: `eas metadata:pull`, edit `store.config.json`, `eas metadata:push` (**ASK**: public listing).
  ASO limits: title 30 chars, subtitle 30, keywords 100 (`app-store-metadata.md`).

## 3. OTA updates (EAS Update)

1. `npx expo install expo-updates`, then `npx eas-cli@<v> update:configure` and review its diff. Do not hand-write `updates.url`,
   `runtimeVersion` or channels; if linking or authorization is missing, stop and explain what remains [eas-update].
2. Model: a build carries platform + runtime version + channel; a channel points to a branch; the build gets the newest compatible update
   on that branch. `eas channel:edit` remaps every build on the channel (**ASK**).
3. Publish (**ASK**; production only with the user's explicit yes - never inferred from the git branch):
   `npx eas-cli@<v> update --channel <channel> --message "<msg>" --environment <env>` (SDK 55+ requires `--environment`).
   Prefer a preview/staging channel first, then promote the same artifact.
4. QA on release builds: fully kill the app, reopen, wait, kill and reopen once more - up to two cold launches. Dev clients preview updates
   through the Extensions UI instead. Do not change `fallbackToCacheTimeout` to skip the second launch.
5. "Build still shows old code" - check in order: published to the right project/channel/platform/environment -> runtime version matches
   the build -> the build actually contains the update URL and channel (config changes need a new build) -> channel-to-branch mapping and
   active update -> two cold launches -> https://docs.expo.dev/eas-update/debug.md. Never bypass anti-bricking safeguards.

## 4. Watch after release (read-only, free to query)

- Update health [eas-update-insights]: latest group id
  `eas update:list --branch production --json --non-interactive | jq -r '.currentPage[0].group'`, then
  `eas update:insights <group> --json --non-interactive`. Crash rate = failedInstalls / (installs + failedInstalls) x 100. Investigate a
  spike, platform asymmetry, or crash rate above 1% in the last day (`--days 1`). Metrics lag: installs are downloads, crashes are
  self-reported on the next check, fresh publishes show zeros for a while.
- Embedded vs OTA users: `eas channel:insights --channel <name> --runtime-version <v>` (run inside the project; `otaTotalUniqueUsers`
  sums only the top-N updates).
- Startup and crashes [eas-observe]: needs a dev or production build (not in Expo Go). `ObserveRoot` on SDK 56+ (`AppMetricsRoot` on 55),
  mark interactive with `useObserve()` / `<ObserveInteractiveMarker />` (SDK 56+) or `markInteractive()` (55). Query with
  `eas observe:metrics-summary`, `observe:routes`, `observe:errors`; thresholds and TTI param meaning in
  `members/eas-observe/references/metrics.md`. Free plan covers up to 10,000 MAU; beyond that is paid (**ASK** before relying on it).

## 5. CI with EAS Workflows [eas-workflows]

- Files live in `.eas/workflows/*.yml`, max 16 KiB each. Fetch the live schema before writing:
  `node members/eas-workflows/scripts/fetch.js https://api.expo.dev/v2/workflows/schema` (plain GET with an ETag cache in the skill dir).
- Validate every changed file: `npx -y eas-cli@<v> workflow:validate .eas/workflows/<file>.yml --non-interactive` until it prints
  `Workflow configuration YAML is valid.` Validation is free; every job that runs consumes build minutes (**ASK** before triggering or
  merging a workflow that auto-runs on push).
- Store-release and PR-preview examples: `members/eas-app-stores/references/workflows.md`.

## 6. Web and API routes [eas-hosting]

- Author `app/api/*+api.ts` with named `GET/POST/...` exports; server secrets via non-`EXPO_PUBLIC_` env; validate input; proper status
  codes; CORS headers plus an `OPTIONS` handler for web clients. Test locally with `npx expo serve` (localhost:8081).
- Runtime is Cloudflare Workers: no `fs`, no native Node modules, ~30 s CPU limit, no persistent sockets; use Web Crypto and `fetch`;
  use a hosted DB (Supabase, Turso, D1, Neon).
- Deploy: `npx expo export -p web`, then `npx eas-cli@<v> deploy` (preview URL, **ASK**) or `deploy --prod` (**ASK**, live).
  Production secrets: `eas env:create --environment production` (**ASK**; never echo the value).

## 7. Cloud simulator [eas-simulator]

On the user's Mac use the local Simulator. Use EAS Simulator only when the user asks for a cloud/shareable session (**ASK** covers one session):
`simulator:availability --json` first (do not start if unavailable) -> `simulator:start --platform ios --type agent-device
--non-interactive --name "<purpose, 3-6 words>" --max-duration-minutes <n>` -> drive with
`simulator:exec npx agent-device@<pinned> snapshot -i | press @eN | screenshot` -> `simulator:stop` and reset `.env.eas-simulator`.
Live edits need a dev build (mode C); a leftover release build never hot-reloads. Never print the preview API URL (it carries a token).
