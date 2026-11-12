---
name: test-and-harden
description: Decide what to test and how, write acceptance criteria and tests that prove behavior, check web apps in a real browser with evidence, build a verify skill for a repo, prune bad tests, harden apps, and hold Python to a clear bar. Use for "write tests", "test plan", "acceptance criteria", "QA plan", "given/when/then", "coverage", "unit/integration/e2e", "Playwright", "click through the site", "screenshot the page", "console errors", "reproduce this UI bug", "verify skill", "how do I prove the app works", "prune/dedupe tests", "slow CI", "contract test", "snapshot", "property-based", "mock", "pytest", "TDD", "test everything", "test contacts", "scenario test", "security review", "harden", "XSS", "CSRF", "SQL injection", "CSP", "headers", "rate limiting", "JWT", "npm audit", "before deploy", "type hints", "mypy". Writes expected results first, picks the seam and test type, gathers browser evidence, applies a merged security checklist, and verifies results where they land.
members: [testing-strategies, webapp-testing, security-hardening, python-best-practices, qa-acceptance, agent-browser, create-verification-skill, test-audit]
---

# Test and Harden

Eight skills (test strategy, acceptance criteria, browser testing and browser evidence, project verify skills, test pruning,
security hardening, Python quality) on top of the always-on
`superpowers:test-driven-development` (red-green-refactor: no production code without a failing test first) and the built-in
`security-review` skill. This skill decides *what* to test, *at which seam*, *with which kind of test*, how to check a web app in a real
browser, which security rules a change must meet, and what "done" means for the user: expected results written first, evidence from every
connected system. The `security-guidance` plugin already warns on risky edits; this is the deliberate pass. Load this first; open
member files for code patterns.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| Building a feature or fixing a bug in code | TDD | Skill `superpowers:test-driven-development`; pick the test type with the matrix below. |
| "Write tests for X", test plan, coverage of an existing module | Test design | Workflow 1-3, matrix. Patterns: `members/testing-strategies/SKILL.md` |
| A feature or PR heads to QA, "acceptance criteria", "how will we know it works", release smoke pass | Acceptance | Workflow 1 + Core rules: Acceptance criteria. `members/qa-acceptance/SKILL.md` |
| "Does the page work", click through, screenshot, console errors, reproduce a UI bug | Browser: interactive | Playwright MCP tools (navigate, snapshot, click, console, network); recon then action; evidence rules in Core. `members/agent-browser/SKILL.md` |
| Repeatable browser regression script | Browser: scripted | Script skeleton (Core rules) + `members/webapp-testing/scripts/with_server.py`; examples in `members/webapp-testing/examples/` |
| Two services or a webhook must agree on a payload | Contract | Consumer-driven contract (Pact) or a JSON-schema check on both sides. `members/testing-strategies/SKILL.md` |
| Algorithm, parser, sorter, money math | Property | fast-check (TS) or hypothesis (Python) over invariants. |
| Logic that lives in the database | Integration | Real database: local Supabase stack or testcontainers (both need Docker). |
| Ops build or change (automation, voice, CRM or database flows) | Scenario suite | Expected results first, test contacts and sandbox lines, check every connected system, record the test, re-run after edits. |
| A repo has no scripted way to launch and drive the app; "make a verify skill for this project" | Verify skill | Core rules: Project verify skill. `members/create-verification-skill/SKILL.md` + `references/feature-map-example/` (its section 3 is Paperclip-only). |
| Tests are redundant, vacuous or slow; "prune", "dedupe", CI too slow | Test audit | Core rules: Test audit gate. `members/test-audit/SKILL.md`, `references/audit.md`, `references/validation.md` (skip `references/paperclip.md`). |
| Review pending changes for vulnerabilities | Security review | Skill `security-review`, then the checklist below for anything it doesn't cover. |
| Hardening an app before deploy | Harden | Security checklist. Code patterns: `members/security-hardening/SKILL.md` |
| Python script or service quality | Python bar | Python rules below. Examples: `members/python-best-practices/SKILL.md` |
| A test is flaky or a failure makes no sense | Debug | `debug-lab` super-skill (Flaky mode). |
| Accessibility checks on UI | A11y | `web-a11y` super-skill. |

## Unified workflow

### 1. Write down what "passing" looks like before running anything [the user test-everything rule]
For each scenario, write the expected result first: inputs, the observable outcome, and where it shows (screen, API response, row,
message, call). Cover the happy path, unhappy paths, edges (empty, max length, duplicates, time zones and DST, retries) and an attempt at
something that should be impossible. Expected-first stops you from grading a result by what it happened to be. For a feature or PR,
write them as one-line Given/When/Then acceptance criteria a reviewer can run on the live app without asking the author, cover the
eight areas in Core rules (or write "N/A: why"), and mark must-pass apart from nice-to-have [qa-acceptance].

### 2. Choose the seam [testing-strategies + the seam rule shared with plan-and-execute]
Test through the highest seam that still exercises the real behavior: the module's interface is its test surface. Prefer existing seams
and as few as possible. Tests that reach past the interface into internals break on refactors and prove little. If the only reachable
seam is too shallow to show the real bug pattern, say so (that's an architecture finding, see `debug-lab` step 7).

### 3. Pick the test type [testing-strategies]

| Need | Type | Rule of thumb |
|---|---|---|
| Behavior of one module | Unit, AAA | real collaborators where cheap, doubles at boundaries you don't own |
| Invariant over many inputs (length kept, order holds, round-trip, totals add up) | Property-based | fast-check / hypothesis; let it shrink the failing case |
| Consumer and provider agree on an API or webhook | Contract | consumer expectations verified without both services running |
| Rendered output or formatted text | Snapshot | inline for small outputs; review every diff; never blind-update |
| Code plus its database | Integration | real DB (local Supabase stack or testcontainers), migrations applied, reset per test |
| User journey in the browser | E2E | Playwright, few and focused on the money paths |
| Live-ops flow | Scenario suite | test contacts, sandbox lines, checks in every connected system |

### 4. Write it red first [superpowers:test-driven-development, testing-strategies, python-best-practices]
Arrange-Act-Assert, one behavior per test, named by the behavior ("rejects an order with no items"), independent of order and of other
tests' state (reset in `beforeEach` / fixtures). Watch it fail for the right reason before writing code. Python: pytest functions,
shared fixtures in `conftest.py`, `pytest.mark.parametrize` for variations, `tmp_path` for files, `asyncio_mode = "auto"` for async.
Doubles stay minimal and behavior-focused (a fake that records what was sent beats a mock that asserts call order).

### 5. Browser checks: recon, then action [webapp-testing + Playwright MCP]
- Interactive (most checks): Playwright MCP. Navigate, take an accessibility snapshot or screenshot, read console and network, then act
  with selectors taken from what actually rendered.
- Scripted (regressions you will re-run): `sync_playwright`, headless Chromium, one script per journey. If the server isn't running,
  `python members/webapp-testing/scripts/with_server.py --server "npm run dev" --port 5173 -- python your_test.py` (repeat
  `--server/--port` pairs for backend + frontend). Static HTML: open it via `file://` and read the file for selectors.
- Wait for the app to be ready before inspecting the DOM; then assert with auto-waiting locators (role, text, test id), not fixed sleeps.
- Capture console logs on the page (`page.on("console", ...)`) and screenshots to the session scratchpad. Close the browser at the end.
- `claude-in-chrome` only when the user's logged-in session is required; for data checks, an API beats the browser.
- Before launching, decide the URL, the state that should be true, the viewport and the evidence you need; if `curl` can see the page,
  skip the browser. Capture evidence right after the wait succeeds, act one click at a time, re-capture after each meaningful change, and
  report it as "navigated X, observed Y, clicked Z, observed W" with console errors and every non-2xx response [agent-browser].
- No repeatable way to launch and drive the app yet? Build a verify skill once (Core rules) so every later check is one command
  [create-verification-skill].

### 6. Harden [security-hardening + `security-review`]
Run `security-review` on the pending changes, then walk the security checklist (Core rules) for whatever it didn't cover: input
validation at every boundary, output encoding, parameterized SQL, CSRF where cookies authenticate, CSP and headers, rate limits, JWT
handling, secrets, dependency audit. Fix, then add a test for each fixed hole (an injection string, an oversized body, a missing token).

### 7. Run and verify end to end [the user verify-errors rule, superpowers:verification-before-completion]
Run the real command and read its output before claiming anything. For anything that writes, sends or syncs, check the result where it
lands (the row, the contact, the delivered message, the call record), not just the test's own assertion. Label each result verified end
to end or inferred.

### 8. Record, re-run, report [the user test-everything rule]
Record each test (scenario, expected, actual, evidence ids) in the project's tests folder (ops: a `tests/` folder in the project notes). Re-run the whole scenario suite after any edit, not just the case you touched. Flaky tests get fixed at the root
cause, never skipped or retried into green. Report what was tested and the evidence, not "done": acceptance passes come back as
**Pass** (one-line evidence each), **Fail** (exact reproduction) and **Blocked** (could not run, why) [qa-acceptance]. A failing must-pass
criterion blocks acceptance unless the user waives it with a tracked follow-up; "known issue" with no follow-up is not a waiver; a criterion
added mid-pass restarts the pass, because partial coverage hides regressions.

## Core rules and checklists

### Acceptance criteria [qa-acceptance]
- Format: `**Given** <starting state>, **when** <action>, **then** <observable outcome>.` One `when` and one `then` per line; split the
  rest. Example: "Given a CSV export with 0 rows, when the user clicks Export, then the file has only the header row and the UI shows
  'Exported 0 rows'."
- Every plan covers, or says "N/A: why": (1) golden path end to end; (2) empty and minimum states (zero, one, optional inputs missing);
  (3) boundary inputs (max length, max number, unicode, RTL); (4) error states (network failure, permission denied, validation, 409
  conflict, 404); (5) concurrency and ordering (two users at once, background job races, refresh mid-save); (6) performance envelope (the
  largest realistic input without hangs or timeouts); (7) backward compatibility (old data, old URLs, saved preferences); (8) telemetry
  and audit (the events, logs or activity rows the change must emit).
- Evidence per criterion: screenshot or clip for UI, copied console/network output for APIs, a log line or row for telemetry, a timing
  for performance. "Looks good" is not a pass.
- Stay observable: criteria never depend on selectors, query plans or other internals; acceptance is what is true after shipping,
  tests are how you check it. Skip acceptance plans for unit-only refactors.

### Browser evidence [agent-browser]
- Viewports: desktop 1366x768 (or the 1280x900 script default), phone 390x844; a passing screenshot proves nothing about viewports you
  didn't load. Wait for a selector or a network signal, never an arbitrary sleep.
- Bug repro record: exact steps, viewport and device pixel ratio, first load vs after interaction, console errors, failing requests.
- Login-gated pages: prefer programmatic auth (API token, magic link); UI login only with credentials the user gives for this run; credentials
  never in logs, screenshots or output. Skip sites whose terms forbid automation and sensitive accounts (banking, health, government).
- Politeness on shared or public hosts: one navigation every few seconds, respect `robots.txt`, about 30 s page timeout, retry once with a
  longer timeout, then escalate. Unattended scraping is not this mode.
- Failure modes: selector not found = screenshot the real state, then adjust; click does nothing = offscreen, covered by a modal or in a
  shadow DOM (scroll into view or pierce the root); headless detection = headed mode only on the user's own sites or with authorization;
  cross-origin iframe = can't inspect it, get the data elsewhere.
- Close every browser you opened; long sessions leak memory and hold ports. Never close the user's own Chrome tabs.

### Project verify skill [create-verification-skill]
- Interview the repo, not the user: surface (web, CLI/TUI, API, mobile; pick the primary), run command (the repo's own dev script; ports, env,
  seed data, auth), drive (existing Playwright/Cypress specs and helpers first, then browser/CDP for web, tmux/PTY for CLI, HTTP for
  services), observe (screens, transcripts, bodies, logs, exit codes, DB state), isolate (can two instances run side by side? if not, the
  skill refuses to double-drive a shared one).
- If the checkout doesn't build or start, fix that or report it precisely first; a skill written against a broken base teaches wrong steps.
- Write `.claude/skills/verify-<app>/SKILL.md` with frontmatter (name plus a description naming the app, surface and when to use it) and
  sections grounded in what you found, no placeholders: **Launch** (exact command, readiness signal, teardown), **Doctor** (one read-only
  "is this instance worth driving" check: process up, right build, port ours, auth valid), **Drive** (real selectors and commands; stable
  handles such as ARIA labels, data attributes, routes over coordinates), **Evidence** (what to capture and where), **Cleanup** (kill only
  what the run started, never by process name; evidence survives cleanup), **Helpers** (executable, invocation shown).
- Proof standards: drive the real user path, not internal setters or test-only endpoints; capture the action and the resulting state;
  verify side effects (files, rows, messages) as well as the screen; mocks only where a production boundary already isolates the outside
  system; for a "dry run" mode, observe what it actually skips (files, network, git refs) instead of trusting its name.
- Feature map: `features/README.md` plus one file per top 3-5 user-facing features with four H2s: Sub-features, How to get to it (user
  POV), Driving it with <harness>, Gotchas.
- Prove it once before handing it over: launch, doctor, drive one mapped feature, capture evidence, clean up, confirm the evidence still
  exists. A generated skill never executed is a draft.

### Test audit gate [test-audit]
- For each test you'd remove, answer: which observable contract and plausible regression does it cover? Which kept test catches that
  regression through the production code responsible (or why is it vacuous)? Does it uniquely cover a transport, permission, lifecycle,
  storage, platform or default? What improves (runs, fixtures, processes, maintenance, runtime)?
- Similarity, size, slowness or "looks AI-written" never justify deletion alone; keeping a test after review is a valid result.
- New tests: name the regression existing proof misses; extend an existing owner or table before adding a suite; never a mock that
  supplies the very result being asserted, or a production hook added only for tests; a negative case reaches its guard with otherwise
  valid inputs.
- Order: pin the base, read candidates and keepers, prove the baseline, move unique assertions first, then retire duplicates, re-run
  keepers and siblings. Report removals, keepers, deferred items, and cost evidence labeled measured, estimated or historical.

### Test anti-patterns [testing-strategies]
- Testing implementation details instead of behavior.
- Shared mutable state between tests; tests that depend on run order.
- Mocking everything instead of using real dependencies for integration tests.
- Ignoring or auto-retrying flaky tests instead of fixing the cause.
- Testing trivial getters while edge cases go untested.
- Blindly updating snapshots.

### Test checklist [testing-strategies + the user]
- [ ] Expected results written before the run, per scenario.
- [ ] Tests organized by behavior, AAA, independent.
- [ ] Contract tests on every inter-service payload you own one side of.
- [ ] Property tests for algorithmic or money code.
- [ ] Integration tests hit a real database.
- [ ] Doubles minimal; external HTTP mocked with a `spec` (Python `AsyncMock(spec=httpx.AsyncClient)`) so the fake can't drift from the real API.
- [ ] Snapshot diffs reviewed.
- [ ] CI fails on flaky-test detection.
- [ ] Evidence recorded; suite re-run after edits.

### Browser testing rules [webapp-testing]
- Always headless Chromium in scripts; descriptive selectors (`role=`, `text=`, ids); appropriate waits (`wait_for_selector`, locator
  assertions); always close the browser.
- Reconnaissance first: screenshot (`full_page=True`), `page.content()`, `page.locator('button').all()`, then act.
- Bundled scripts are black boxes: run `--help` first. `with_server.py` (105 lines, reviewed) starts each server with `shell=True`, polls
  the port (30 s default `--timeout`), runs your command, and terminates the servers on exit. It pipes server output without reading
  it, so a very chatty dev server can stall mid-run; if a long run hangs, start the server yourself in the background and run the test
  script directly.
- Example files write screenshots to `/mnt/user-data/outputs/`; on the user's Mac use the session scratchpad instead.

Script skeleton (merged from the three member examples, with auto-waiting assertions instead of fixed sleeps):
```python
import os, sys
from playwright.sync_api import sync_playwright, expect

URL = os.environ.get("APP_URL", "http://localhost:5173")
OUT = os.environ.get("OUT_DIR", ".")          # point at the session scratchpad
logs: list[str] = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
    page.goto(URL)
    page.wait_for_load_state("domcontentloaded")
    page.screenshot(path=f"{OUT}/before.png", full_page=True)      # recon
    page.get_by_role("button", name="Export").click()               # act with a discovered selector
    expect(page.get_by_text("Export ready")).to_be_visible()        # expected result, auto-waits
    page.screenshot(path=f"{OUT}/after.png", full_page=True)
    browser.close()

errors = [l for l in logs if l.startswith("[error]")]
print("\n".join(logs))
sys.exit(1 if errors else 0)                                       # console errors fail the run
```

### Security checklist [security-hardening]
- **Input:** validate type, length, format and range at every boundary with a schema (zod in TS, Pydantic in Python); allowlists over
  denylists; uploads checked by MIME type, extension and magic bytes; request body capped at the proxy (e.g. 1 MB). Client-side
  validation is never enough.
- **Output:** rely on framework auto-escaping; no `dangerouslySetInnerHTML` with user input; `encodeURIComponent` for URL parts;
  `JSON.stringify` for JSON; never build HTML strings from user input.
- **SQL:** parameterized queries only (`$1` / `%s` placeholders) or an ORM/query builder; never string-built SQL.
- **CSRF:** tokens (32 random bytes, timing-safe compare) on state-changing requests when cookies authenticate; Bearer-token APIs don't
  need them.
- **CSP:** start strict (`default-src 'self'`, script nonces instead of `'unsafe-inline'`, `frame-ancestors 'none'`, `base-uri 'self'`,
  `form-action 'self'`), ship as `Content-Security-Policy-Report-Only` first, collect reports, then enforce.
- **Headers on every response:** `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`, `X-Content-Type-Options:
  nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(),
  geolocation=()` (helmet or the framework's equivalent).
- **Rate limits:** sliding window, per user and endpoint; login 5 per 15 min, register 3 per hour, writes 60/min, reads 120/min;
  answer `429` with `Retry-After`; stricter on auth routes.
- **JWT:** access tokens about 15 min; refresh tokens 7-30 days in httpOnly cookies; RS256 across services, HS256 inside one app; no
  sensitive data in the payload; verify `iss`, `aud`, `exp`, `nbf` with a pinned algorithm list; revocation via denylist or short
  expiry + rotation.
- **Secrets:** never in code or git (`.env` in `.gitignore`); environment variables at runtime; different secrets per environment;
  `gitleaks detect` / `gitleaks protect --staged` to catch leaks. Never print them.
- **Dependencies:** `npm audit --omit=dev` (older npm: `--production`), `pip-audit`, `govulncheck ./...`; run in CI on every PR; block
  critical/high; pin versions; automated update PRs.
- **Before deploy:** inputs schema-validated; SQL parameterized; headers set; HTTPS + HSTS; secrets external; dependencies audited; rate
  limits on public endpoints; tokens expire and rotate; error messages leak no internals; security events logged without sensitive data.

### Python bar [python-best-practices]
- Type every signature with modern syntax: `list[str]`, `X | None`, 3.12 `type` aliases and generics, `TypedDict` for structured dicts;
  `mypy --strict` or pyright in CI; `type: ignore` only with a reason.
- `@dataclass(frozen=True, slots=True)` for internal value objects; Pydantic (`strict`) at boundaries: API input, config, external data.
- Async: `httpx.AsyncClient` in `async with`; `asyncio.gather` for concurrency; `asyncio.Semaphore` to cap it (rate limits); never
  blocking I/O inside async code (`asyncio.to_thread` for legacy calls).
- Layout: `src/` package, `tests/` with `conftest.py`, all tool config in `pyproject.toml`; Ruff (rules E, F, I, N, UP, B, SIM, RUF;
  line length 100) instead of flake8 + isort + black.
- Environments: always a venv (`uv venv` + `uv pip install -e ".[dev]"`, or `python -m venv .venv`); never global installs; lock exact
  versions (`uv.lock` or a frozen requirements file).
- Errors: a custom exception hierarchy with codes; catch the most specific exception, never bare `except:`; `logger.exception()` to keep
  tracebacks.
- Idioms: unpacking, comprehensions over map/filter, context managers, walrus for assign-and-test, `match` for structured dispatch.
- Local setup: a recent Python 3 (Homebrew on macOS), `PYTHONUNBUFFERED=1` for live output, `python3 -I` for any script that reads downloaded data.

### Scenario suites for ops builds [the user]
- Build the whole unit, then test each block, then each twin/copy, then the full system together; turn it on in steps.
- Test contacts and sandbox lines only; preflight the setup before every test (clean line, correct test data).
- After each run, check every connected system (database, SMS or voice provider, CRM, the app) against the expected result.
- Record each test in the project's `tests/` folder; re-run the scenario suite after any edit.
- Fast but never at the cost of reliability: run independent scenarios in parallel, don't pad, don't skip.

Test record (one file per scenario run, in the project's `tests/` folder):
```
Scenario: <id + plain title>            Date: <yyyy-mm-dd>      Build/version: <workflow or agent version>
Setup: <test contact / sandbox line used, preflight done>
Expected: <written before the run, per system; Given/When/Then lines for features>
Actual: <per system: database row, SMS or call log, CRM record, app screen>
Evidence: <ids, query output, screenshots in the scratchpad>  (no secrets, no customer data)
Verdict: pass / fail, verified end to end / inferred      Re-runs: <dates after later edits>
```

## When members disagree

| Between | Issue | Rule |
|---|---|---|
| superpowers:test-driven-development vs prototypes and spikes | "No code without a failing test" vs "prototypes get no tests" | Throwaway prototypes and spikes are exempt; anything kept re-enters through TDD and is rewritten with tests. |
| testing-strategies vs python-best-practices | "Don't mock everything" vs the `AsyncMock` HTTP example | Mock only boundaries you don't own (third-party HTTP), always with `spec=`; repositories and SQL run against a real database. |
| webapp-testing vs the user's security rule | "Don't read the scripts, run them" vs "read code before running third-party code" | `with_server.py` has been read (summary above); use it as a black box. Any new third-party script is read once before its first run. |
| webapp-testing vs current Playwright guidance | `networkidle` is "critical" vs it being unreliable on apps that poll or stream | Use `networkidle` only for first recon on simple apps; assert with auto-waiting locators or `wait_for_selector`; never a fixed `wait_for_timeout` as the main sync. |
| webapp-testing scripts vs Playwright MCP / claude-in-chrome | Three browser routes | Interactive checks: Playwright MCP. Re-runnable regressions: Python script. The user's logged-in session needed: claude-in-chrome. Data checks: the API, not a browser. |
| security-hardening vs the user's ops-audit rule | "Rotate secrets every 90 days, scan history" vs "don't raise hardcoded-key or rotation items in ops audits" | Apply the secrets rules to new app code and deploy checklists; in ops audits leave key-rotation items out unless the user asks. |
| security-hardening vs tool changes | `safety check` and `npm audit --production` | `safety` now needs an account: use `pip-audit`. Use `npm audit --omit=dev` on current npm. |
| testing-strategies vs the user's environment | testcontainers needs Docker | Prefer the project's local Supabase stack when it has one; installing Docker is an install, so ask first. |
| python-best-practices vs the user's existing scripts | "httpx not requests", src layout, strict typing | New code follows the bar; working scripts keep their conventions unless the user wants a refactor. |
| the user "fast as possible" vs "test everything" | Speed vs thoroughness | Never trade reliability for speed: parallelize independent scenarios; never skip one. |
| qa-acceptance "criteria are not tests" vs superpowers:test-driven-development "test first" | Which comes first | Both, at different layers: acceptance criteria are written first for the feature (step 1); TDD tests prove each unit while building. |
| agent-browser "realistic user agent, beat headless detection" vs the user's security rules and site terms | Evading bot checks | Only on the user's own sites or with written authorization; never to get past another site's protection. |
| agent-browser "close the browser" vs claude-in-chrome | Whose browser | Close what you opened (Playwright); never close the user's own Chrome tabs or session. |
| create-verification-skill `.agents/skills/verify-<app>/` vs Claude Code | Where the skill lives | `.claude/skills/verify-<app>/` in the user's repos (Claude Code loads it), unless the repo already uses `.agents/skills`; commit only when the user asks. |
| create-verification-skill "fix the checkout, add scaffolding" vs the user's change protocol | Making it start | Local scaffolding only, clearly marked and removed in cleanup; never a live system. Ops flows use the scenario suite instead. |
| test-audit "delete redundant tests" vs the user "test everything" | Removing coverage | Delete only with the four-question evidence; deleting files needs the user's yes, so present removals as a list the user approves. |

## Combine with
- `superpowers:test-driven-development` (always on): the red-green-refactor loop and its `writing-good-tests.md`.
- `security-review` (built-in) for pending changes; the `security-guidance` plugin warns on edits.
- `superpowers:verification-before-completion` before any pass claim; `run` skill to launch the app; `debug-lab` for flaky or confusing
  failures; `plan-and-execute` to put a test suite into a plan; `web-a11y` for accessibility; `ux-lab` when the question is "is this
  confusing" rather than "does it work"; `claude-builder` for skill-writing quality when building a verify skill.
- Agent types available here: `design-review` (UI change review with Playwright), `pragmatic-code-review`.
- Specialist prompts (file = Agent prompt):
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/test-automator.md`: building a test framework or CI test stage.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/qa-expert.md`: a full test plan and quality metrics.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/security-auditor.md`: a systematic audit before a launch.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/penetration-tester.md`: authorized active testing of the user's own apps only.
  - `~/.claude/skill-library/agents/voltagent/02-language-specialists/python-pro.md`: typed, production-grade Python.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/ui-ux-tester.md`: exploratory UI testing of a flow.

## House rules (the user)
- Double-check and test every piece before it runs or before moving on: expected result first, test contacts, every connected system
  checked, the test recorded, the suite re-run after edits; report evidence, not "done".
- A failure or a pass counts only once confirmed where the result lands; label verified vs inferred; say "unconfirmed" when you can't
  read the destination.
- No test calls or texts to real customers; sandbox and test lines only; third-party systems stay read-only.
- Never print secrets; tests read them from the environment.
- Installs only in a venv or with `npm --cache /tmp/npm-cache`, pinned; new tools (Docker, Playwright browsers) ask first.
- Paid APIs and anything that sends, publishes, posts, buys or calls a live system ask the user first.

## Members

| Member | Best at | Path |
|---|---|---|
| testing-strategies | Test-type patterns with code: AAA, Pact contracts, snapshots, fast-check properties, testcontainers, minimal doubles, anti-patterns | `members/testing-strategies/SKILL.md` |
| webapp-testing | Python Playwright scripts with a server-lifecycle helper, recon-then-action, console capture, static HTML | `members/webapp-testing/SKILL.md`, `scripts/with_server.py`, `examples/` |
| security-hardening | Concrete hardening rules and numbers: validation, encoding, SQL, CSRF, CSP, headers, rate limits, JWT, secrets, audits, deploy checklist | `members/security-hardening/SKILL.md` |
| python-best-practices | Modern Python bar: 3.12 typing, dataclass vs Pydantic, async httpx, pyproject + Ruff + mypy, uv, pytest, error handling | `members/python-best-practices/SKILL.md` |
| qa-acceptance | Given/When/Then acceptance criteria, the eight must-cover areas, evidence per criterion, Pass/Fail/Blocked report, waiver rules | `members/qa-acceptance/SKILL.md` |
| agent-browser | Supervised browser verification: evidence to capture, bug-repro record, login-gated and politeness rules, common failure modes | `members/agent-browser/SKILL.md` |
| create-verification-skill | Generating a repo's own verify skill (Launch, Doctor, Drive, Evidence, Cleanup), proof standards, feature map, prove-it-once | `members/create-verification-skill/SKILL.md`, `references/feature-map-example/` |
| test-audit | Evidence-gated test pruning and a gate against new duplicate or vacuous tests | `members/test-audit/SKILL.md`, `CAMPAIGN.md`, `references/audit.md`, `references/validation.md` |

If a member folder is missing (not installed), work from this file alone.
