# HTML dashboard kit (merged)

Small, tested-by-reading building blocks merged from build-dashboard (structure, formatting, Chart.js, tables),
dashboard (inline SVG charts, admin shell) and the user's report rules (period dropdown, good-direction deltas). Use them in a
self-contained HTML snapshot or an Artifact page. In a Next.js app, port the logic and use the project's components.
Chart form and colors come from the built-in `dataviz` skill; these blocks are mechanics only.

## 1. Page skeleton

```html
<title>Growth - snapshot</title>
<style>/* tokens from section 2, layout from section 6 */</style>
<header class="top"><h1>Growth</h1>
  <label>Period <select id="period"></select></label>
  <span id="custom" hidden><input type="date" id="from"> to <input type="date" id="to"></span>
</header>
<section class="hero" id="hero"></section>        <!-- 4-5 headline numbers -->
<section class="kpis" id="kpis"></section>        <!-- every other card, grouped -->
<section class="charts"><div class="card"><h3>Converted per day</h3><canvas id="c1"></canvas></div></section>
<section class="card table-wrap"><table id="detail"></table><nav id="pager"></nav></section>
<footer>Data as of <span id="asof"></span> (<span id="tz"></span>)</footer>
<script>
const DATA = /* pre-aggregated JSON: { asof, kpis_by_day: [...], by_campaign: [...] } */ {};
</script>
```
On an Artifact page the publish step adds `<html>`, `<head>` and `<body>`; write the content directly (see
`artifact-design`).

## 2. Theme-aware tokens (Artifact rule: full light palette on :root, dark redefined twice)

```css
:root{--bg:#f6f7f9;--card:#fff;--ink:#14171a;--muted:#5d6670;--line:#e3e6ea;--good:#1a7f4b;--bad:#c0362c;--neutral:#5d6670;
      --gap:16px;--radius:8px}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){color-scheme:dark;
      --bg:#0e1116;--card:#161b22;--ink:#e8ecf1;--muted:#9aa4ae;--line:#27303a;--good:#3fb27f;--bad:#f0645a;--neutral:#9aa4ae}}
:root[data-theme="dark"]{color-scheme:dark;
      --bg:#0e1116;--card:#161b22;--ink:#e8ecf1;--muted:#9aa4ae;--line:#27303a;--good:#3fb27f;--bad:#f0645a;--neutral:#9aa4ae}
body{background:var(--bg);color:var(--ink);font:14px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
     padding-inline:16px}
```
Series colors: take them from `dataviz` (its palette file and validator), or from brand tokens that pass it.

## 3. Period presets (the user's dropdown) in one reporting time zone

```js
const TZ = 'America/Chicago';                       // say it in the footer; bucket days in this zone
const ymd = d => new Intl.DateTimeFormat('en-CA',{timeZone:TZ,year:'numeric',month:'2-digit',day:'2-digit'}).format(d);
const addDays = (s, n) => { const d = new Date(s + 'T12:00:00Z'); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); };
const firstOf = (y, m) => new Date(Date.UTC(y, m, 1, 12)).toISOString().slice(0, 10);   // m may be -1 or 12
const PERIODS = { today:'Today', yesterday:'Yesterday', this_week:'This week', last_week:'Last week',
  this_month:'This month', last_month:'Last month', this_quarter:'This quarter', last_quarter:'Last quarter', custom:'Custom range' };
const PRIOR = { today:'yesterday', this_week:'last_week', this_month:'last_month', this_quarter:'last_quarter' };

function period(key, now = new Date()) {            // returns half-open [start, end) as YYYY-MM-DD
  const today = ymd(now), d = new Date(today + 'T12:00:00Z');
  const dow = (d.getUTCDay() + 6) % 7;              // Monday = 0
  const y = d.getUTCFullYear(), m = d.getUTCMonth(), q = Math.floor(m / 3) * 3;
  switch (key) {
    case 'today':        return [today, addDays(today, 1)];
    case 'yesterday':    return [addDays(today, -1), today];
    case 'this_week':    { const s = addDays(today, -dow); return [s, addDays(s, 7)]; }
    case 'last_week':    { const s = addDays(today, -dow - 7); return [s, addDays(s, 7)]; }
    case 'this_month':   return [firstOf(y, m), firstOf(y, m + 1)];
    case 'last_month':   return [firstOf(y, m - 1), firstOf(y, m)];
    case 'this_quarter': return [firstOf(y, q), firstOf(y, q + 3)];
    case 'last_quarter': return [firstOf(y, q - 3), firstOf(y, q)];
    case 'custom':       return [document.getElementById('from').value, addDays(document.getElementById('to').value, 1)];
  }
}
const inPeriod = (row, [start, end]) => row.day >= start && row.day < end;   // row.day bucketed in TZ upstream
```
Month-to-date comparisons: compare against the same number of elapsed days of the prior month (clip the prior window to
`addDays(priorStart, daysElapsed)`), otherwise "this month" always looks down.

## 4. KPI card with a good-direction delta

```js
const fmt = (v, kind) => kind === 'currency' ? (Math.abs(v) >= 1e6 ? `$${(v/1e6).toFixed(1)}M` : Math.abs(v) >= 1e3 ? `$${(v/1e3).toFixed(1)}K` : `$${v.toFixed(0)}`)
  : kind === 'percent' ? `${v.toFixed(1)}%` : (Math.abs(v) >= 1e6 ? `${(v/1e6).toFixed(1)}M` : Math.abs(v) >= 1e3 ? `${(v/1e3).toFixed(1)}K` : v.toLocaleString('en-US'));

function delta(cur, prev, goodWhenUp = true) {
  if (prev == null) return { text: '', cls: 'neutral' };
  if (prev === 0) return { text: cur === 0 ? 'no change' : 'new', cls: 'neutral' };
  const pct = (cur - prev) / Math.abs(prev) * 100;
  if (pct === 0) return { text: 'no change', cls: 'neutral' };
  return { text: `${pct > 0 ? '+' : ''}${pct.toFixed(1)}% vs prior`, cls: (pct > 0) === goodWhenUp ? 'good' : 'bad' };
}

function kpiCard(spec, cur, prev) {                 // spec = { label, kind, goodWhenUp, definition }
  const el = document.createElement('div'); el.className = 'card kpi'; el.title = spec.definition;
  const d = delta(cur, prev, spec.goodWhenUp);
  el.innerHTML = '<div class="label"></div><div class="value"></div><div class="delta"></div>';
  el.querySelector('.label').textContent = spec.label;            // textContent: never inject raw data as HTML
  el.querySelector('.value').textContent = fmt(cur, spec.kind);
  const dEl = el.querySelector('.delta'); dEl.textContent = d.text; dEl.classList.add(d.cls);
  return el;
}
```
`.delta.good{color:var(--good)} .delta.bad{color:var(--bad)} .delta.neutral{color:var(--neutral)}` plus an arrow or
sign so color is never the only signal.

## 5. Charts

Chart.js (interactive pages; pinned include in SKILL.md):
```js
const area = (id, labels, series) => new Chart(document.getElementById(id), {
  type: 'line',
  data: { labels, datasets: series.map(s => ({ label: s.label, data: s.data, borderColor: s.color,
          backgroundColor: s.color + '33', fill: true, cubicInterpolationMode: 'monotone', pointRadius: 0, borderWidth: 2 })) },
  options: { responsive: true, maintainAspectRatio: false, animation: false,
             interaction: { mode: 'index', intersect: false },
             scales: { x: { grid: { display: false } }, y: { beginAtZero: true } } } });
// on filter change: chart.data.labels = ...; chart.data.datasets[i].data = ...; chart.update('none');
```
Give each canvas a parent with a fixed height (e.g. `height:280px`) or `maintainAspectRatio:false` collapses it.

Inline SVG (static pages, no library) [dashboard]:
```js
function smoothArea(values, w = 600, h = 160, pad = 6) {
  const max = Math.max(...values, 1), n = values.length;
  const p = values.map((v, i) => [pad + i * (w - 2 * pad) / Math.max(n - 1, 1), h - pad - v / max * (h - 2 * pad)]);
  let d = `M${p[0][0]},${p[0][1]}`;
  for (let i = 0; i < n - 1; i++) {                 // Catmull-Rom to Bezier
    const a = p[i - 1] || p[i], b = p[i], c = p[i + 1], e = p[i + 2] || c;
    d += ` C${b[0] + (c[0] - a[0]) / 6},${Math.min(h - pad, b[1] + (c[1] - a[1]) / 6)} ${c[0] - (e[0] - b[0]) / 6},${Math.min(h - pad, c[1] - (e[1] - b[1]) / 6)} ${c[0]},${c[1]}`;
  }
  return { line: d, area: `${d} L${p[n - 1][0]},${h - pad} L${p[0][0]},${h - pad} Z` };
}
// <svg viewBox="0 0 600 160" role="img" aria-label="Converted per day, last 30 days">
//   <path d="${area}" fill="currentColor" opacity=".15"/><path d="${line}" fill="none" stroke="currentColor" stroke-width="2"/></svg>
```
Control points are clamped to the baseline so the curve never dips below zero.

## 6. Layout CSS [build-dashboard + dashboard]

```css
.top{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;padding-block:16px}
.hero,.kpis{display:grid;gap:var(--gap);grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-bottom:var(--gap)}
.charts{display:grid;gap:var(--gap);grid-template-columns:repeat(auto-fit,minmax(min(400px,100%),1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px 24px}
.card canvas{height:280px!important}
.kpi .label{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px}
.kpi .value{font-size:28px;font-weight:700;font-variant-numeric:tabular-nums}
.hero .kpi .value{font-size:40px}
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}
th{text-align:left;font-size:12px;color:var(--muted);border-bottom:2px solid var(--line);cursor:pointer;white-space:nowrap}
td,th{padding:10px 12px} td{border-bottom:1px solid var(--line)}
@media (max-width:768px){.kpis{grid-template-columns:repeat(2,1fr)}}
@media print{.top select,.top input{display:none}.card{break-inside:avoid}}
```
`min(400px,100%)` keeps the chart grid from overflowing a 400 px phone.

## 7. Sortable, paginated table (safe)

```js
function table(el, pager, rows, cols, pageSize = 50) {   // cols = [{ field, label, kind }]
  let sortBy = null, dir = -1, page = 0;
  function draw() {
    const sorted = sortBy ? [...rows].sort((a, b) => (a[sortBy] > b[sortBy] ? 1 : a[sortBy] < b[sortBy] ? -1 : 0) * dir) : rows;
    const slice = sorted.slice(page * pageSize, (page + 1) * pageSize);
    el.replaceChildren();
    const head = el.createTHead().insertRow();
    cols.forEach(c => { const th = document.createElement('th'); th.textContent = c.label + (sortBy === c.field ? (dir > 0 ? ' ▲' : ' ▼') : '');
      th.onclick = () => { dir = sortBy === c.field ? -dir : -1; sortBy = c.field; page = 0; draw(); }; head.appendChild(th); });
    const body = el.createTBody();
    slice.forEach(r => { const tr = body.insertRow(); cols.forEach(c => { tr.insertCell().textContent = c.kind ? fmt(r[c.field], c.kind) : r[c.field]; }); });
    pager.textContent = rows.length ? `Showing ${page * pageSize + 1}-${page * pageSize + slice.length} of ${rows.length.toLocaleString('en-US')}` : 'No rows for this period';
  }
  draw();
  return { next() { if ((page + 1) * pageSize < rows.length) { page++; draw(); } }, prev() { if (page) { page--; draw(); } } };
}
```

## 8. CSV export

On Vercel or a local file:
```js
function csv(rows, cols) {
  const esc = v => `"${String(v ?? '').replace(/"/g, '""')}"`;
  const text = [cols.map(c => esc(c.label)).join(','), ...rows.map(r => cols.map(c => esc(r[c.field])).join(','))].join('\n');
  const a = Object.assign(document.createElement('a'), { href: URL.createObjectURL(new Blob([text], { type: 'text/csv' })), download: 'export.csv' });
  a.click(); URL.revokeObjectURL(a.href);
}
```
On an Artifact page the sandbox blocks page-started downloads: use the file hand-off capability from
`artifact-capabilities` instead.

## 9. Pre-aggregation shape (SQL side)

Aggregate in Postgres (a view or RPC function in `reporting`), bucket by day in the reporting zone, and embed only what
the page shows:
```sql
select (created_at at time zone 'America/Chicago')::date as day, campaign, count(*) as texted,
       count(*) filter (where replied) as replied, sum(cost_usd) as cost
from reporting.some_fact_table            -- pre-built fact table, never tag inference
where created_at >= now() - interval '90 days'
group by 1, 2 order by 1, 2;
```
`at time zone` on a `timestamptz` gives local wall time; on a naive timestamp it does the opposite conversion, so
check the column type first (`information_schema.columns`).
