---
name: dashboard-studio
description: Build, change or fix dashboards, reports and charts. Live ops dashboards on Vercel / Next.js reading Supabase (lead, call, SMS, campaign, cost and conversion metrics from n8n and CRM or voice tools), dead-simple cost and count reports with a period dropdown, self-contained HTML dashboards from query results or CSV (KPI cards, Chart.js, filters, sortable tables), Artifact pages, executive overviews, admin screens, and Grafana or SigNoz monitoring boards. Also redesigns, wrong or low numbers, per-card before/after checks, metric definitions, attribution, and chart choice and encoding (which chart, bar vs line, pie, histogram, scatter, heatmap, bullet chart, axis at zero, annotations, accessible and mobile charts). Use for dashboard, report, KPI, metrics page, scorecard, analytics, admin panel, monitoring, Grafana, cost per lead, funnel, chart, data visualization, stat tile, sparkline, numbers look wrong, redesign the dashboard, add a card. Charts follow the built-in dataviz skill.
members: [build-dashboard, dashboard-builder, dashboard, data-visualization]
---

# Dashboard Studio

One entry point for every dashboard and report the user's teams read. It merges Anthropic's `build-dashboard` (self-contained
HTML with KPI cards, Chart.js, filters and tables), ECC's `dashboard-builder` (operator-question monitoring boards),
Open Design's `dashboard` (admin layout with inline SVG charts) and Owl-Listener's `data-visualization` (chart choice by
question, encoding, chart accessibility and phone-width charts), and wraps them in the user's dashboard rules, which are
strict and come first. Load this file, pick the mode, follow the workflow. The built-in `dataviz` skill is the chart
standard; open member files only when a route names them (`members/<name>/` points at the original skill folder).
Code kit: `references/html-kit.md`.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| New live dashboard for a team (leads, calls, SMS, campaigns) on Vercel with Supabase | OPS-DASHBOARD | Full workflow; react-next-pro + supabase-postgres-pro for the app and SQL |
| "How many / how much did X cost" for a period, per platform | REPORT | Dead-simple report spec (Core rules); smallest version first |
| Turn query results or a CSV into a shareable, offline page | SNAPSHOT | Workflow with embedded JSON; `members/build-dashboard/SKILL.md` patterns + `references/html-kit.md` |
| Change, redesign or add to an existing dashboard | CHANGE | Change procedure (Core rules); open that dashboard's project notes or README first |
| Numbers look wrong, low, shifted, or attribution is guessed | DATA-FIX | Trace upstream; per-card before/after; fix at the source (supabase-postgres-pro / n8n-builder); `superpowers:systematic-debugging` |
| System health board: Grafana, SigNoz, uptime, queues, latency | MONITORING | `members/dashboard-builder/SKILL.md` questions + checklist |
| Admin / analytics screen prototype (sidebar, top bar, KPI grid) | ADMIN-UI | `members/dashboard/SKILL.md` layout + `members/dashboard/example.html` |
| Dashboard published as a claude.ai page, live data or saved picks | ARTIFACT-PAGE | Load `artifact-design`, and `artifact-capabilities` before any live data or stored state |
| Proposed dashboard changes for the user to mark | REVIEW-PAGE | Review-card format (Core rules) + `artifact-capabilities` (db + user) |
| One chart, KPI tile, sparkline, palette question, "which chart for this", chart accessibility or mobile chart | CHART | Built-in `dataviz` first; Core rules > Chart choice and encoding for the quick pick, axis, labels, annotations, a11y and phone rules [data-visualization]; then `references/html-kit.md` for mechanics |
| Report as a spreadsheet file (.xlsx, CSV) or a PDF to send | FILE-REPORT | docs-decks (built-in `anthropic-skills:xlsx` / `anthropic-skills:pdf`), numbers from the same metric spec |
| Report fed into a Google Sheet by a workflow (daily tabs, call outcomes) | SHEET-FEED | n8n-builder for the flow; this skill for the metric spec and per-card checks |

## Unified workflow

1. **Start from the reader and their questions, not the layout.** Who opens it, what they decide, and the questions it
   must answer at a glance: is it healthy, where is the bottleneck, what changed, what should someone do
   [dashboard-builder], plus the dimensions people filter by (company, campaign, channel, agent, period) [build-dashboard]. When the user names a reference dashboard or a list of numbers, copy their metric names verbatim and
   take the look from that reference.
2. **Write a metric spec before any UI.** One row per card: name as the user says it, exact definition (filter, count vs
   distinct, numerator/denominator), source table and columns, time column and its type and time zone, period behavior,
   comparison period, and whether a higher value is good. Facts come from dated rows captured upstream (`reporting.*`,
   `outreach.events`, CRM history); never infer campaign, day or credit from tags or template labels. A number that cannot be computed from recorded facts becomes an upstream
   tracking task, shown as "not tracked yet", never as an estimate.
3. **Choose the surface.**
   - Vercel / Next.js app: live data, login, team use, the user's existing ops dashboards. Read pre-built tables, views or
     RPC functions; no heavy logic in the browser [tracking-protocol rule 7].
   - Artifact page: private claude.ai page. Outside fetches are blocked, so data is either embedded JSON (snapshot) or
     comes through a runtime capability (load `artifact-capabilities`). Theme-aware tokens required (`artifact-design`).
   - Local HTML file: offline snapshot to send as a file [build-dashboard].
   - Grafana / SigNoz JSON: infrastructure monitoring [dashboard-builder].
   - Spreadsheet or PDF: when the reader lives in files or email; same metric spec, built through docs-decks.
   Default for the user's team dashboards: a Vercel app reading Supabase; default for a one-off
   answer: a REPORT in chat, with a page offered in one line.
4. **Size the data** [build-dashboard]: under 1,000 rows embed raw; 1,000-10,000 embed and pre-aggregate for charts;
   10,000-100,000 aggregate server-side and embed only aggregates; above 100,000 use the app/BI layer or paginate.
   Pre-aggregate in SQL into one `DATA` object (`kpis`, `daily`, `by_campaign`, ...).
5. **Lay it out big-numbers-first.** Hero row of 4-5 headline numbers on top; it is a highlight, never a cut. Then grouped KPI cards (label, value, delta vs prior period), one primary chart (largest
   area), secondary charts, then the detail table [build-dashboard]. Monitoring boards group as overview -> performance
   -> resources -> service-specific [dashboard-builder]. For the user: 2-3 screens unless they ask for more, no tabs they did
   not ask for.
6. **Pick charts with `dataviz`** (form, palette, marks, accessibility). The user's explicit picks for a dashboard override it
   (for example: dark modern look, smooth area charts, no bar charts). Name the question each chart answers (compare,
   trend, part of whole, distribution, relationship, target vs actual) and take the simplest form that answers it; give
   each series one colour on every chart of the page; label lines directly; mark known events on time charts (launch,
   outage, rule or price change) so a jump explains itself [data-visualization]. Mechanics: Chart.js for interactive
   pages, inline SVG for a few static charts, the project's chart library inside a Next.js app (rule in "When members
   disagree").
7. **Wire interactivity** [build-dashboard]: one period selector and filters that update every KPI, chart and table
   together; `chart.update('none')` on filter change; sortable columns; 50 rows a page with "Showing 1-50 of N"; CSV
   export where the old dashboard had one.
8. **Finish the edges.** Units and titles on every panel, sane thresholds, number formatting (K/M, currency, %),
   empty states that say why, a footer with "Data as of <time> <time zone>", a SAMPLE DATA banner if any number is
   not real [build-dashboard, dashboard-builder], and a text alternative for every chart: a one-sentence takeaway as
   its accessible name plus a table view of the same numbers [data-visualization].
9. **Verify like the user reads.** Screenshot desktop and phone widths (Playwright MCP); at phone width charts carry fewer
   points and larger labels, tooltips open on tap, and the table view is reachable [data-visualization]. Recompute every card from SQL and
   compare. For any change: per-card and per-campaign numbers at 30 and 90 days before vs after, plus an element count
   (cards, KPIs, tables, charts, CSV buttons, drill-downs) before vs after.
10. **Approve, ship, watch.** Changes go on a review page first and are built only from the user's picks. Deploys and data writes follow the Change Protocol; after shipping, load the
    live page and re-check the cards against SQL on real traffic.

## Core rules and checklists

### Metric spec sheet (write it before any UI) [dashboard-builder questions + tracking-protocol + before/after]
| Card (the user's words) | Definition | Source (table.column) | Time column, type, zone | Period / compare | Good when | Status |
|---|---|---|---|---|---|---|
| Converted | distinct leads signed in the period | `<schema.table.signed column>` | timestamptz, Central | period vs prior | up | tracked |
| Cost per lead | touch cost / leads contacted | `<events table.cost column>` + basis | timestamptz, Central | period vs prior | down | tracked |
| Booked via AI SMS | bookings whose source step is the SMS agent | (not captured yet) | - | - | up | upstream task |
The rows show the format only: fill every row from the real schema (`information_schema.columns`), never from memory. "Status" is tracked,
partial (explain) or upstream task. Keep the sheet next to the code (`docs/metrics.md`) and on the review page.

### Dead-simple report spec
- One table. Rows = platforms or channels; columns = count and cost for the period (texts sent + cost, calls made +
  cost, and so on).
- Period dropdown: Today, Yesterday, This week, Last week, This month, Last month, quarters, plus optional custom range.
  Code in `references/html-kit.md`.
- Monthly-billed items (Twilio minimum, CRM, Supabase, n8n) live in a separate monthly table, never mixed into
  per-period usage, and per-touch costs are never added to invoice totals [tracking-protocol rule 3].
- No definitions, changelog or health tabs, ratio columns or conditional colors unless asked. Raw data hidden. Show the
  smallest version first and add only what the user asks for.

### Delivering a REPORT
- In chat: the table itself (period, platform, count, cost, total), then one line on where the numbers came from.
- As a page (when they want to reuse it): the same table with the period dropdown, nothing else; offer it in one line.
- Numbers come from the live source at answer time; say the time zone and the "as of" time.

### Ops dashboard rules [memories: comprehensive, upstream-tracking, tracking-protocol, change-before-after]
- Never remove a KPI, chart, table, list, CSV button or drill-down in a redesign. Fewer hero numbers means a highlight
  row on top.
- Attribution: credit goes to the campaign workflow the lead was in when they signed; isolate "eventually" numbers
  (for example Drop Off) instead of folding them in.
- Cost per touch carries its basis (provider-reported vs estimated).
- Privacy: no names, phone numbers or message text on a dashboard unless the user asks; never SSN, DOB or bank data; AI
  labels and redacted quotes only.
- New columns copy the exact type of the column they mirror (check `information_schema` first); a naive Central
  timestamp next to a `timestamptz` shifts every time and hides behind matching totals. Views that depend on a column
  block type changes: drop and recreate in one transaction.
- Time zones: one reporting zone for the whole page, written in the footer; day buckets computed in that zone.

### Card and KPI rules [build-dashboard + new]
- Every card: label, value, unit, delta vs the prior equal period, and a tooltip with the exact definition.
- Color the delta by whether the change is good, not by its sign: cost, opt-outs, drop-offs and errors going up are
  bad. Prior value 0 -> show "new", not a division by zero. Compare like with like (month-to-date vs the same days of
  last month).
- Format: `$1.2K`, `1.2M`, `12.3%`; one decimal for rates; thousands separators in tables.

### Chart performance and limits [build-dashboard]
- Line charts under 500 points per series (downsample), bar charts under 50 categories, scatter capped at 1,000 points.
- Many charts: `animation: false`; filter updates with `chart.update('none')`; batch DOM updates with
  `requestAnimationFrame`; update only changed elements; tables show 100-200 rows max, paginate the rest.
- Chart.js include (pinned, allowed on Artifact pages):
  `<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1" integrity="sha384-jb8JQMbMoBUzgWatfe6COACi2ljcDdZQ2OxczGA3bGNeWe+6DChMTBJemed7ZnvJ" crossorigin="anonymous"></script>`.
  Smooth area series: `fill: true, cubicInterpolationMode: 'monotone'` (no overshoot below zero, unlike plain `tension`).

### Chart choice and encoding [data-visualization; built-in dataviz decides where they differ]
| The chart answers | Use | Watch |
|---|---|---|
| Compare categories (campaign, agent, platform) | Bar, sorted; grouped bar for 2-3 series | Starts at zero; horizontal when labels are long |
| Actual vs target (daily quota, budget burn) | Bullet chart, or a bar with a target line | Target labelled with its value |
| Trend over time | Line; area when volume matters; sparkline inside a KPI card | Areas start at zero; lines may zoom to the data range with a labelled axis |
| Part of a whole | Stacked bar; pie or donut only for 2-5 parts of one total at one moment; treemap for a hierarchy | Parts must add up to a real total |
| Distribution (call length, time to sign, cost per lead) | Histogram or box plot | State the bin width |
| Relationship (spend vs leads, hour x weekday) | Scatter; bubble for a third value; heatmap | Heatmap on a sequential scale |
- Data-ink: every mark carries data; light or no gridlines, no 3D, no shadows on marks. The simplest chart that
  answers the question wins.
- Colour: one colour per series on every chart and page (fix the campaign or platform colour map once in the page
  tokens); sequential for ordered values, diverging around a midpoint (vs target, vs prior period), categorical for
  unrelated groups; colour-blind safe, never red vs green alone.
- Labels and context: axis titles with units; direct labels at the line end or bar when about 5 series or fewer fit,
  otherwise a legend; annotate the event or insight ("SMS block began") on the chart; show a target line, prior period
  or benchmark beside the number so good or bad is visible.
- Accessibility (check it with web-a11y): marks and the gridlines needed to read them reach 3:1 against the background
  (WCAG 1.4.11); dash styles, point shapes or patterns in addition to colour when series are compared; SVG charts get
  `role="img"` and an `aria-label` that states the takeaway. Chart.js draws on a canvas that screen readers and the
  keyboard cannot enter, so the canvas gets `role="img"` plus that label and the same numbers sit in a table (visible
  or behind a "Show table" toggle); every chart control is keyboard reachable.
- Phone width: aggregate to fewer points (daily to weekly), fewer ticks, larger labels, tooltips on tap (Chart.js
  `interaction: { mode: 'index', intersect: false }`), and the table instead of a dense chart.
- Test with real data, not a tidy sample: long names, zeros, gaps, one huge outlier. Detail comes on demand (tooltip,
  drill-down, table), not all at once.

### Layout patterns
- KPI grid `repeat(auto-fit, minmax(200px, 1fr))`, chart grid `minmax(400px, 1fr)`, 16 px gap, cards 8 px radius;
  below 768 px: KPIs 2 per row, charts 1 per row, filters stacked [build-dashboard].
- Admin shell [dashboard]: fixed left sidebar 220-260 px (brand mark, 6-8 nav links, active state in the accent), top
  bar (title left, search and user right), sidebar and top bar sticky while main scrolls; accent used at most twice;
  density matches the mood (ops and trading tighter, executive airier). Semantic `aside / header / main / section`.
  Prototypes use specific, plausible metric names and values, never "Metric A".
- Print: hide filters, `break-inside: avoid` on charts, borders instead of shadows [build-dashboard].

### Monitoring board checklist [dashboard-builder]
- Sections: health/availability, latency (p50/p95/p99), throughput, saturation/resources, service-specific risk.
- Study the platform's existing dashboards first (JSON structure, query language, variables, thresholds).
- Valid dashboard JSON; titles and units everywhere; meaningful threshold colors; variables for common filters;
  sensible default time range and refresh; every panel answers a real operator question.
- Example sets: API gateway (request rate, p50/p95/p99, error rate, upstream health, connections); queues (depth, age
  of oldest, consumer lag); n8n (executions, failures by workflow, duration) [new example].
- If a daily read-only "System check" already exists per company, for ops health
  questions, read that note first and extend its collector and page instead of building a second monitoring board;
  a parallel board splits the truth and doubles upkeep.

### Change procedure (CHANGE and DATA-FIX) [Change Protocol]
1. Snapshot before: per-card and per-campaign numbers at 30 and 90 days; element inventory; screenshot.
2. Prove the problem on real rows (which card, which campaign, which rows, why), and check for a second cause.
3. Fix at the source when the data is wrong (upstream capture, view or function), not with front-end math.
4. Review page: one card per change, old vs new side by side (numbers and screenshot), the reason in plain words,
   a pick (accept / alternative / keep original / my wording) and a note; the suggested pick tagged; an "accept all
   suggestions" button. Picks save to the page's store (`artifact-capabilities`: db + user); read them back with the
   Artifact `read_db` action and record them with the date in the project notes.
5. Build only from the picks; anything kept against a pick, or found mid-build, gets its own card first.
6. After: same 30/90-day per-card table, old vs new, with every difference explained:
   | Card | Campaign | 30 d before | 30 d after | 90 d before | 90 d after | Why it moved |
   Then watch the live page on real traffic.

### Security and hygiene [new]
- Escape every value written into the DOM (`textContent`, or an escape helper) - `build-dashboard`'s table builds HTML
  strings from raw data, which is unsafe once names or message text appear.
- Browser code uses only public/anon keys with row-level security or a server route; service keys stay server-side and
  are never printed.
- Embedded snapshots contain only aggregates the page shows, never raw PII rows.

### Vercel / Next.js pattern [new: the user's stack]
- Server components or route handlers query Supabase views/RPCs; the browser gets aggregates only.
- Auth in front (Supabase auth or Vercel protection) because ops numbers are internal.
- Cache with revalidation sized to the data (for example 5 minutes for daily metrics) and show "Data as of".
- One query per screen section where possible; slow ones get an index or a materialized table (database-optimization).

### Pre-ship checklist (merged) [build-dashboard step 7 + dashboard self-check + dashboard-builder checklist + the user]
- Every card has title, unit, definition tooltip, delta colored by good direction; every chart has axis units and a source.
- Every chart: bars and areas from zero, one colour per series across the page, a takeaway label plus a table view,
  readable at 400 px; colour is never the only way to tell series apart.
- All filters move every KPI, chart and table together; empty periods show "No rows for this period", not zeros.
- Numbers match SQL for at least two periods; per-campaign cards checked, not only totals.
- Element count equals or exceeds the previous version (CHANGE mode).
- Desktop and 400 px phone screenshots look right; no horizontal page scroll; contrast passes.
- Footer shows data time and time zone; SAMPLE DATA banner present if anything is not real.
- No PII or message text unless the user asked; values written with `textContent`; no service key in the browser.
- Artifact pages: light and dark tokens, no page-started downloads, external scripts only from allowed CDNs.

### Lessons from the user's past dashboards (why the rules exist)
| What happened | Rule it produced |
|---|---|
| A 9-tab comms workbook was called "ugly, way overdone" | REPORT mode: one table and a period dropdown first |
| A "cleaner" redesign dropped numbers the team used | Never remove; highlights go on top; count elements before/after |
| Campaign credit was guessed from template labels and tags | Credit only from dated upstream facts; untracked = "not tracked yet" |
| A new `timestamptz` column beside a naive Central timestamp shifted signings 10 h; totals still matched | Per-card 30/90-day before/after; copy column types exactly |
| A growth redesign "did too much"; they wanted it simple, dark, modern, smooth area charts, no bars | Start from the reference they name, their numbers verbatim, 2-3 screens |


**Eval lessons (super-skill vs earlier picks, 20 graded runs):**
- Build what was literally asked first (the named chart, control and periods), then add extras; never swap the asked-for view
  for a "better" one without saying so on the review page.
- Every data component ships loading, error and empty states.
- The real component takes data as a required prop; mock data lives in a Demo wrapper and is never the default.
- Ship a small verify script (node or python) that recomputes every headline number from the source rows; run it before
  saying done and keep it with the deliverable.

## When members disagree

| Between | Conflict | Rule |
|---|---|---|
| dashboard-builder vs the user (comprehensive) | Cut vanity panels vs never remove a metric | New dashboard: build the minimum that answers the questions. Existing dashboard: never remove; propose any cut as a review card |
| the user (dead-simple) vs the user (comprehensive) | Smallest version vs keep everything | A REPORT answers one question: smallest version. An OPS-DASHBOARD the team works from: comprehensive, highlights on top |
| build-dashboard vs the user (no guessing) | Invent a realistic sample dataset when no data is given | Sample data only for templates and mockups, with a SAMPLE DATA banner. Ops dashboards show real rows or "not tracked yet" plus an upstream task |
| build-dashboard vs dashboard | Chart.js for all charts vs inline SVG only, no JS libraries | Interactive filters or many charts: Chart.js pinned. Static page with 1-3 charts: inline SVG. Next.js app: the project's chart library |
| build-dashboard vs the user's taste vs artifact-design | Light, system-font, white-gray look vs dark, modern, impressive vs theme-aware light+dark | the user's named reference wins on look; Artifact pages still define both palettes (dark-first designs swap roles consistently) |
| build-dashboard COLORS vs dataviz | Fixed six-color palette vs validated palette method | dataviz palette (or brand tokens that pass its validator) |
| build-dashboard (2-4 KPI cards) vs the user's metric lists | Few headline numbers vs 10-15 named numbers | Hero row of 4-5, the rest as grouped KPI cards below; nothing dropped |
| dashboard-builder vs the user (reference first) | Start from questions vs start from the reference they name | Reference sets look and metric names; the questions set grouping and order |
| dashboard (Open Design) | Reads an injected DESIGN.md, `data-od-id` tags, `<artifact>` output | Outside that app: project tokens or artifact-design, publish with the Artifact tool, drop the tags |
| build-dashboard KPI colors | Any increase green, any decrease red | Color by good direction per metric |
| data-visualization vs dataviz | A quick chart table and colour types vs the built-in form heuristic and validated palette | dataviz decides form and palette; data-visualization's table is the quick pick, and its encoding, a11y and phone rules add to it. Its "colour ramp belongs to `color-system`" maps here to dataviz or brand tokens (color-system now lives in ui-studio) |
| data-visualization vs build-dashboard | Label directly and avoid legends vs a Chart.js legend on every chart | Direct labels when about 5 series or fewer fit; more series, or an interactive Chart.js view, gets a clickable legend; same colours either way |
| data-visualization vs the user's picks | Pie or donut for part of whole, bars for comparison vs their named style (for example: no bars) | the user's picks win; pie or donut only for 2-5 parts of one total; when bars are off, compare with a sorted table or dot plot |
| data-visualization "y-axis at zero for bars" vs smooth line and area charts | Which charts need a zero baseline | Bars and areas start at zero (length and area encode size); lines may zoom to the data range when the axis is labelled |

## Combine with

- Built-in skills: `dataviz` (chart form, palette, marks; load before chart code), `artifact-design` (any Artifact
  page), `artifact-capabilities` (live data, stored review picks, viewer identity), `frontend-design:frontend-design`.
- Personal skills: `nextjs-mastery` (Vercel app dashboards), `database-optimization` (slow dashboard queries, indexes).
- Superpowers: `superpowers:brainstorming` (new dashboard scope), `superpowers:writing-plans` (multi-screen builds),
  `superpowers:systematic-debugging` (DATA-FIX), `superpowers:verification-before-completion` (before "done").
- Agent prompts (`~/.claude/skill-library/agents/voltagent/`): `05-data-ai/data-analyst.md` (metric definitions and
  insight), `05-data-ai/data-engineer.md` (upstream capture and pipelines), `05-data-ai/postgres-pro.md` (views,
  functions, types), `01-core-development/frontend-developer.md` (Next.js dashboard build),
  `04-quality-security/ui-ux-tester.md` (click-through of filters and drill-downs),
  `04-quality-security/accessibility-tester.md` (contrast, keyboard, screen reader).
- Other super-skills: supabase-postgres-pro (SQL, RLS, migrations), n8n-builder (tracking inside flows), react-next-pro
  (app code), brand-studio (tokens), ui-studio (color-system palette and dark-mode tokens), web-a11y (scan and keyboard
  check of chart text alternatives, contrast and table views), docs-decks (xlsx, PDF or slide versions of a report).

## House rules

- Comprehensive dashboards: a redesign never drops a KPI, chart, table, list, CSV or drill-down; prove it with an
  element count before and after.
- Reports are dead simple: one table, period dropdown, counts and cost per platform, monthly bills apart; start from their
  reference and their numbers verbatim, 2-3 screens, no extra tabs.
- Build reporting on dated upstream facts, never on guessed tags or template labels.
- After any dashboard data change compare per-card and per-campaign numbers at 30 and 90 days, not just totals; copy
  column types exactly.
- New flows record what dashboards will show; dashboards read pre-built tables; no PII beyond the rules.
- Every non-trivial change goes on a review page the user marks; build only from their picks.
- Supabase writes, migrations, n8n edits and production deploys are live-system changes: Change Protocol first, and
  anything that sends, publishes or writes to a live system asks the user. Never print keys.

## Members

| Member | Best at | Path |
|---|---|---|
| build-dashboard | Complete self-contained HTML dashboard: layout, base template, KPI and format helpers, Chart.js line/bar/doughnut, combined filters, sortable and paginated tables, CSS, data-size and chart-performance limits | `members/build-dashboard/SKILL.md` |
| dashboard-builder | Operator-question method, monitoring section order, example panel sets, quality checklist, no vanity panels | `members/dashboard-builder/SKILL.md` |
| dashboard | Admin shell layout (sidebar, top bar, KPI row, charts), inline SVG charts, accent and density self-check | `members/dashboard/SKILL.md`, `members/dashboard/example.html` |
| data-visualization | Chart choice by question (comparison, trend, part of whole, distribution, relationship), bullet charts for target vs actual, zero baseline, direct labels, annotation, consistent series colour, chart accessibility, phone-width charts | `members/data-visualization/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
