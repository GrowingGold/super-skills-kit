---
name: supabase-postgres-pro
description: "Supabase and Postgres end to end: schema design, column types, primary and foreign keys, constraints, migrations (Supabase CLI, declarative schemas, MCP execute_sql / apply_migration), RLS policies and tests, auth (supabase-js, @supabase/ssr, getUser, getClaims, JWT, app_metadata), API keys, Data API grants, views, SECURITY DEFINER functions, triggers, storage policies, edge functions, realtime, pg_cron, queues, pgvector, full-text search, JSONB; slow queries, EXPLAIN ANALYZE, indexes (composite, partial, covering, GIN, GiST, BRIN), N+1, pagination, upsert, batch inserts, connection pooling, pooler, prepared statements, timeouts, locks, deadlocks, SKIP LOCKED job queues, vacuum, pg_stat_statements, partitioning, read replicas; debugging permission denied, empty results, RLS surprises, schema cache, 401/403, timeouts, logs and advisors. Also any read, report, backfill or data fix on any live production Supabase project, and MySQL tuning basics."
members: [supabase, supabase-postgres-best-practices, database-optimization]
---

# Supabase + Postgres Pro

One skill for database work: Supabase platform rules (auth, RLS, keys, CLI, MCP, migrations), Supabase's 30 Postgres
rules (indexes, connections, locking, schema), and the always-on database-optimization checklist, merged with the user's rules
for their live databases. Load this file first and follow the unified workflow; open a member file only when a mode
or step points to it (`members/<member>/...`). Supabase changes often: for platform features (auth, SSR, CLI, config,
edge functions) check the current docs instead of memory; for plain SQL this file is enough.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| New table, columns, types, keys, constraints | SCHEMA | Steps 0-7; `members/supabase-postgres-best-practices/references/schema-data-types.md`, `schema-primary-keys.md`, `schema-foreign-key-indexes.md`, `schema-constraints.md`, `schema-lowercase-identifiers.md` |
| Schema change in a repo with a local Supabase stack | MIGRATE-LOCAL | Step 6 (local); `members/supabase/SKILL.md` "Making and Committing Schema Changes"; `supabase <group> --help` |
| Schema change on a hosted project with no local stack (the user's own apps) | MIGRATE-REMOTE | Step 6 (hosted) |
| Query a production database, reporting, dashboard numbers | READ | Read-only token, steps 0-1 and 4; never write |
| Fix data, backfill, change a function, policy or trigger on a company database | LIVE-WRITE | Every step plus House rules; step 6 (live) |
| Write or audit RLS; "users see other users' rows"; empty results; UPDATE changes nothing | RLS | Core rules: RLS template + test; `members/supabase-postgres-best-practices/references/security-rls-basics.md`, `security-rls-performance.md`, `security-privileges.md` |
| Login, sessions, JWT, cookies, SSR, keys in the frontend | AUTH | Security checklist; `members/supabase/SKILL.md` Core Principles 6; docs via `search_docs` |
| Slow query, high CPU, timeouts, bad plan | PERF | Step 5 + index chooser; `references/query-*.md`, `monitor-explain-analyze.md`, `monitor-pg-stat-statements.md`; `members/database-optimization/SKILL.md` |
| "Too many connections", pooler errors, "prepared statement does not exist" | CONN | Connections rules; `members/supabase-postgres-best-practices/references/conn-pooling.md`, `conn-limits.md`, `conn-idle-timeout.md`, `conn-prepared-statements.md` |
| Lock waits, deadlocks, worker/job queues, cron jobs colliding | LOCK | Locking rules; `members/supabase-postgres-best-practices/references/lock-short-transactions.md`, `lock-deadlock-prevention.md`, `lock-skip-locked.md`, `lock-advisory.md` |
| Bulk load, pagination, N+1 loops, insert-or-update | DATA | `members/supabase-postgres-best-practices/references/data-batch-inserts.md`, `data-pagination.md`, `data-n-plus-one.md`, `data-upsert.md` |
| Text search, JSONB filters | SEARCH | `members/supabase-postgres-best-practices/references/advanced-full-text-search.md`, `advanced-jsonb-indexing.md` |
| Edge functions, Storage, Realtime, Cron, Queues, pgvector, extensions | PLATFORM | `search_docs` first (no rule file covers these), then the security checklist |
| An error from the Data API, Postgres, Auth, Storage, Realtime or an edge function | DEBUG | Step 1: logs + advisors + the Monitoring and Debugging docs page before proposing a fix; `superpowers:systematic-debugging` |
| Huge tables, archiving, replicas | SCALE | `members/supabase-postgres-best-practices/references/schema-partitioning.md`; read replicas in `members/database-optimization/SKILL.md` |
| Postgres or Supabase node inside an n8n workflow | N8N | Sibling `n8n-builder`, `~/.claude/skill-library/ops/n8n-builder/references/node-family-gotchas.md` (Database) |

`references/` above means `members/supabase-postgres-best-practices/references/`. Several modes often combine (a
LIVE-WRITE that adds an index and a policy): run the workflow once and open each mode's files at the step that needs it.

## Unified workflow

### 0. Orient: which project, which access
- Name the project and its owner: the user's own apps (yours to change after the usual checks) or live production or client projects (reads only until step 6). Keep project refs out of this file.
- Pick the surface: the Supabase MCP connector (`list_tables`, `execute_sql`, `apply_migration`, `list_migrations`,
  `get_advisors`, `query_logs`, `search_docs`, `list_extensions`, branches, edge functions), the Supabase CLI for local
  stacks (discover commands with `--help`; `db query` needs v2.79.0+, `db advisors` v2.81.3+), or the Management API with
  the user's personal access tokens. The read-only token runs as a read-only database user even on the query endpoint; the
  read+write token runs as `postgres`. [supabase, the user]
- For a repo, find the schema workflow first: declarative if `supabase/schemas/` exists or `config.toml` sets
  `schema_paths`, otherwise imperative migrations. [supabase]

### 1. Look before you touch
- Read the real structure: columns and types, indexes, constraints, triggers (`pg_trigger`; watch for `updated_at`
  triggers), policies (`pg_policies`), grants, and whether RLS is enabled and forced.
- Inventory who reads and writes the objects you will change: n8n workflows (each company copy), dashboards, edge
  functions, daily checks and emails, other teams. A change is safe only if all of them still work. [the user]
- Debugging: read logs (`query_logs` / Logs Explorer) and advisors before diagnosing, and fetch Supabase's Monitoring and
  Debugging page (`https://supabase.com/docs/guides/monitoring-and-debugging.md`) rather than working from memory. After
  2-3 failed attempts at one approach, stop and change method. [supabase]
- The diagnosis must explain every case you saw; look for a second cause. [the user]

### 2. Check the docs when the platform is involved
- Auth, SSR, keys, CLI flags, `config.toml`, edge functions, storage, realtime, cron, queues: `search_docs` (preferred),
  or any docs page with `.md` appended, and scan `https://supabase.com/changelog.md` for `breaking-change` tags that touch
  the task. Pure SQL and Postgres tuning don't need this step. [supabase]

### 3. Design
- Types: `bigint` ids, `text` not `varchar(n)`, `timestamptz`, `numeric(p,s)` for money, `boolean`, enums as `text` +
  check or an enum type. Keys: `bigint generated always as identity` for single-database ids; UUIDv7/ULID when ids are
  exposed or distributed (check `list_extensions` first); no random UUIDv4 primary keys on large tables. FKs to
  `auth.users(id)` are uuid by nature and fine. [best-practices]
- Index every foreign key column (Postgres does not), and every column a policy filters on. [best-practices]
- Unquoted lowercase snake_case identifiers; quoted camelCase forces quotes forever. [best-practices]
- Every table in an exposed schema (`public` by default) gets RLS plus policies that match the real access model, not a
  copy-pasted `auth.uid()` rule. Private schemas: RLS as defense in depth. A new SQL-created table may not be exposed to
  the Data API at all: that is a `GRANT` question, separate from RLS; grant `anon`/`authenticated` only with RLS on. [supabase]
- Views: `with (security_invoker = true)` (Postgres 15+), or revoke from `anon`/`authenticated`, or an unexposed schema.
  Functions: `security invoker` by default, `set search_path = ''`. [supabase]

### 4. Write the SQL
- Set-based, not loops: `where id = any($1::bigint[])` or a JOIN instead of one query per row; batches of ~500-1000
  rows or `COPY` for bulk loads; `insert ... on conflict (...) do update set ... = excluded....` instead of
  select-then-insert; keyset pagination (`where (created_at, id) > ($1, $2) order by created_at, id limit 20`) instead of
  deep OFFSET. [best-practices, database-optimization]
- Parameterize every value that came from outside (`$1`), including inside n8n nodes. [n8n-builder, best-practices]
- Transactions short: no HTTP or other slow work while holding locks; lock rows in a consistent order
  (`select ... order by id for update`) or update them in one statement; `set local statement_timeout` for risky work. [best-practices]
- Name columns instead of `select *`, use `exists` instead of `count(*) > 0`, keep functions and casts off indexed columns
  in `where`, add `limit` when only a subset is needed. [database-optimization]

### 5. Prove it on real data without side effects
- Plans: `explain (analyze, buffers, format text)` and read bottom-up. `analyze` executes the statement, so a write is
  explained inside `begin; ... rollback;`, and on a busy live table start with plain `explain`. [best-practices, database-optimization]
- Before any UPDATE/DELETE, run the same `where` as a `select count(*)` and sample rows; the count is part of the review
  page. [database-optimization, the user]
- Functions that refresh tables: run them end to end into temp copies (`create temp table x_t (like reporting.x)`) and
  compare counts with live; compiling alone proves nothing because plpgsql checks columns at run time. [the user]
- RLS: test as the real role (template below) for an owner, a stranger and `anon`; check SELECT, INSERT, UPDATE and DELETE.
- Replay the change on recent real data (old vs new result) and write down what could go wrong and how it would show. [the user]

### 6. Apply by environment
- **Local stack (imperative):** iterate with `execute_sql` or `supabase db query` (no migration history entries, so you can
  try freely). When it works: advisors, security checklist, `supabase db pull <descriptive-name> --local --yes`,
  `supabase migration list --local`. Create hand-written migrations with `supabase migration new <name>`; never invent the
  filename. Declarative: edit `supabase/schemas/`, then generate the migration. [supabase]
- **Hosted project without a local stack (the user's own apps):** iterate inside transactions you roll back, or on a branch
  (branches cost money: ask). Apply the final SQL once with `apply_migration`, which writes a history entry per call, so
  never iterate with it. Pin package versions and commit lockfiles for client libraries. [supabase, the user]
- **Production or client database:** review page first (evidence, exact SQL, row counts, impact list, replay, risks,
  undo SQL); after the user's picks, one transaction with the read+write token, trigger handling per House rules, and the user runs
  the apply. Never alter a table that live flows write to without that page. [the user]

### 7. Verify
- Re-run the proving queries; `get_advisors` (security and performance) clean or each item explained; run the RLS test
  again. [supabase]
- Watch the consumers on their next real run: the n8n workflow that writes the table, the dashboard that reads it, the
  daily check. A fix is done when the destination shows the right result. [the user]

## Core rules and checklists

### Security checklist (any task touching auth, RLS, views, functions, storage or user data) [supabase, best-practices]
- Authorization data lives in `app_metadata` (`raw_app_meta_data`); `user_metadata` is user-editable and must never decide
  access. JWT claims stay stale until the token refreshes.
- Deleting a user does not revoke existing access tokens: revoke sessions first; short JWT expiry for sensitive apps; for
  strict cases check `session_id` against `auth.sessions`.
- `service_role` / secret keys never reach a browser (any `NEXT_PUBLIC_` variable ships to it); frontends use publishable
  keys (legacy `anon` keys only for compatibility). Scripts, CI and agents use scoped personal access tokens.
- `auth.role()` is deprecated and passes for anonymous sign-ins: use `to authenticated` / `to anon` on the policy.
  `to authenticated` alone is authentication without authorization (IDOR): always add an ownership predicate.
- UPDATE needs a SELECT policy (otherwise 0 rows, no error) and both `using` and `with check` (otherwise rows can be
  reassigned to another user).
- Views bypass RLS by default; `security definer` functions bypass RLS and, in `public`, are callable by everyone because
  `EXECUTE` is granted to `PUBLIC`.
- Storage upsert needs INSERT + SELECT + UPDATE policies.
- Least privilege for any custom role: grant usage + specific verbs on specific tables, no `grant all`, revoke `public`
  defaults; application code never connects as a superuser.

### RLS policy template [supabase, best-practices]
```sql
alter table public.orders enable row level security;
create index if not exists orders_user_id_idx on public.orders (user_id);  -- policy columns are indexed

create policy "orders: owner reads"   on public.orders for select to authenticated
  using ((select auth.uid()) = user_id);              -- (select ...) runs once, not once per row
create policy "orders: owner inserts" on public.orders for insert to authenticated
  with check ((select auth.uid()) = user_id);
create policy "orders: owner updates" on public.orders for update to authenticated
  using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "orders: owner deletes" on public.orders for delete to authenticated
  using ((select auth.uid()) = user_id);
```
Team or tenant checks that need another table go through a helper (next block). Add `force row level security` when the
table owner must also be filtered (outside Supabase's API roles).

### SECURITY DEFINER helper, the only accepted shape [supabase, best-practices]
```sql
create or replace function private.is_team_member(p_team_id bigint)
returns boolean language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.team_members
                 where team_id = p_team_id and user_id = (select auth.uid()));
$$;
revoke execute on function private.is_team_member(bigint) from public, anon, authenticated, service_role;
-- policy: using ((select private.is_team_member(team_id)))
```
Non-exposed schema, explicit `auth.uid()` check in the body, empty `search_path`, execute revoked, advisors run after.

### Test RLS as the real role (rolled back)
```sql
begin;
set local role authenticated;
select set_config('request.jwt.claims', '{"sub":"<user-uuid>","role":"authenticated"}', true);
select count(*) from public.orders;                 -- only this user's rows?
update public.orders set user_id = '<other-uuid>' where id = <a row this user owns>;  -- must fail the with check
rollback;
```
Repeat with another user's `sub` and with `set local role anon`. On a company database this needs the read+write token,
so it goes through the user like any write.

### Index chooser [best-practices, database-optimization]
| Query shape | Index |
|---|---|
| `=`, `<`, `>`, `between`, `in`, `order by`, `is null` | B-tree (default) |
| Several filters together | Composite: equality columns first, range/sort last (leftmost-prefix rule) |
| Always the same filter (`status = 'pending'`, `deleted_at is null`) | Partial (`... where <condition>`): 5-20x smaller |
| Selected columns not filtered on | Covering: `(email) include (name, created_at)` for index-only scans |
| JSONB containment `@>`, `?` | GIN (`jsonb_path_ops` when only `@>`: 2-3x smaller); one key: expression index `((attrs->>'brand'))` |
| Arrays, full-text (`tsvector` generated column) | GIN |
| Ranges, geometry, nearest neighbour | GiST |
| Very large append-only time series | BRIN (10-100x smaller) |
| Equality only | Hash (small gain over B-tree) |

Confirm with the plan and with `idx_scan` in `pg_stat_user_indexes`; an unused index only slows writes.

### Reading a plan [database-optimization, best-practices]
- Seq Scan on a large table (>10K rows) with "Rows Removed by Filter" high → missing or unselective index.
- Estimated vs actual rows far apart → stale statistics: `analyze <table>`.
- Nested Loop with many loops → join strategy or missing index on the inner side.
- `Sort Method: external merge` → `work_mem` too low for that query.
- `Buffers: read` much larger than `hit` → data not cached.

### Connections and timeouts [best-practices, database-optimization]
- Always pool. Supabase's pooler: transaction mode (port 6543) for serverless and most apps; session mode (5432) when you
  need prepared statements, temp tables or session state. In transaction mode use unnamed statements (Node `pg`:
  `prepare: false`; JDBC `prepareThreshold=0`).
- Pool size ≈ (CPU cores × 2) + disks, typically 10-20 per app instance; each Postgres connection costs 1-3 MB, and
  `work_mem × max_connections` should stay under ~25% of RAM.
- Reclaim idle work: `idle_in_transaction_session_timeout = '30s'`, `idle_session_timeout = '10min'`, plus a
  `statement_timeout`. On hosted Supabase set these per role or per database (`alter role ... set ...`) or through the
  dashboard/CLI after checking docs; server-level `alter system` and `pgbouncer.ini` examples apply to self-managed Postgres.
- Watch with `select count(*), state from pg_stat_activity group by state`.

### Locking, queues and jobs [best-practices]
- Worker queues claim with one statement: `update jobs set status = 'processing', worker_id = $1, started_at = now()
  where id = (select id from jobs where status = 'pending' order by created_at limit 1 for update skip locked) returning *;`
- Singleton jobs (a nightly report, a cron that must not overlap): `pg_try_advisory_lock(hashtext('job'))` or
  `pg_advisory_xact_lock`, not dummy lock rows.
- Deadlocks: consistent lock order; check `pg_stat_database.deadlocks`; `log_lock_waits = on`.

### Maintenance and monitoring [best-practices, database-optimization]
- `pg_stat_statements` for top queries by total and mean time (flag mean > 100 ms); reset after an optimization round.
- `analyze` after big data changes; check `last_autoanalyze` in `pg_stat_user_tables`; for high-churn tables lower
  `autovacuum_vacuum_scale_factor` to 0.05 and `autovacuum_analyze_scale_factor` to 0.02.
- Slow-query logging at `log_min_duration_statement = 100` where you control the server.
- Partition only when a table passes ~100M rows or ~50-100 GB and queries filter by the partition key or old data must be
  dropped fast (dropping a partition is instant; DELETE takes hours). Indexes first.
- Read replicas: send reads there, writes to the primary, and never read-after-write from a replica (lag 10-100 ms).

### Dangerous patterns [database-optimization, best-practices, supabase]
- UPDATE/DELETE without a checked `where`; long transactions holding locks; `like '%term%'` on large text (use
  `tsvector`); `order by random()`; `select distinct` hiding a bad join; deep OFFSET pagination; N+1 loops from app code or
  n8n per-item nodes; `alter table ... add constraint if not exists` (a syntax error: wrap in a `do $$ ... if not exists
  (select 1 from pg_constraint where conname = ...) ... $$` block); `security definer` added to make a permission error go
  away; `apply_migration` used to iterate.

### Pre-apply gate (every answer yes)
- [ ] Structure, triggers, policies and grants read from the real database
- [ ] Every reader and writer of the changed objects listed and checked
- [ ] Plan or row counts proven on real data with no side effects; RLS tested as the real roles
- [ ] Security checklist and advisors clean or each item explained
- [ ] Right apply path for the environment; history entry created once; undo SQL written
- [ ] Company database: review page approved, read+write token only now, triggers handled
- [ ] Watch plan for the consumers' next real run

## When members disagree

| Between | Issue | Resolution |
|---|---|---|
| supabase vs best-practices (`security-rls-performance`) | "Never add SECURITY DEFINER" vs definer helper functions for RLS | Definer only for RLS helper lookups in the template shape (private schema, `auth.uid()` check, `search_path = ''`, execute revoked); never to silence a permission error, otherwise `security invoker` |
| best-practices (`security-rls-basics`) vs supabase + `security-rls-performance` | `for all using (user_id = current_setting(...))` with bare `auth.uid()` | Supabase pattern: per-command policies, `to <role>`, `(select auth.uid())`, `with check` on insert/update |
| supabase vs the user's live databases | "Iterate with `execute_sql`, then `db pull`" assumes a local stack | Mode split in step 6: local iterate freely; hosted iterate in rollbacks/branches and `apply_migration` once; company databases only through the review page |
| database-optimization vs live-data safety | "Always run EXPLAIN ANALYZE" | It executes the statement: SELECTs fine; writes inside `begin ... rollback`; busy live tables start with plain `explain` |
| best-practices (`conn-*`) vs hosted Supabase | `alter system`, `pgbouncer.ini` examples | Self-managed Postgres only; on Supabase use per-role/database settings and the managed pooler after checking docs |
| database-optimization vs best-practices | Partition at 50-100 GB vs above 100M rows | Whichever comes first, and only when queries filter by the key or old data must be dropped |
| best-practices (`schema-primary-keys`) vs Supabase auth | Avoid UUIDv4 keys vs `auth.users` uuid ids | FKs to `auth.users` stay uuid; big tables of your own use `bigint identity`; UUIDv7 when ids are exposed and the extension exists |
| supabase "fetch the changelog first" vs SQL-only work | Docs step on every task | Only for platform features (step 2) |
| supabase `members/supabase/references/skill-feedback.md` | File a GitHub issue on supabase/agent-skills | Public post: ask the user first; by default note the gap in your own notes instead |
| database-optimization | ORM, MySQL, ProxySQL guidance | the user's stack is Postgres/Supabase: MySQL bits stay in the member file for the rare MySQL task |
| database-optimization vs serverless apps | "10-20 connections per app instance" | For Vercel/edge functions use the transaction pooler and keep each instance's pool tiny |

## Combine with
- Built-ins: `superpowers:systematic-debugging` (DEBUG), `superpowers:verification-before-completion`, `artifact-capabilities`
  + `artifact-design` for the user's review page.
- Sibling super-skills (`~/.claude/skill-library/<area>/<name>/SKILL.md`): `n8n-builder` (the workflows that
  read and write these tables, Postgres vs Supabase node), `dashboard-studio` (reporting queries behind dashboards),
  `react-next-pro` (supabase-js and `@supabase/ssr` in Next.js), `debug-lab` (hard cross-system bugs).
- Specialist agent prompts (`~/.claude/skill-library/agents/voltagent/`), hand them the schema, the plan and the query:
  `05-data-ai/postgres-pro.md` (tuning, replication, backups), `05-data-ai/database-optimizer.md` (slow-query sweeps),
  `02-language-specialists/sql-pro.md` (hard SQL, window functions, reporting queries), `04-quality-security/security-auditor.md`
  (RLS and grants audit), `01-core-development/auth-integration-engineer.md` (auth flows, sessions),
  `03-infrastructure/database-administrator.md` (backup, restore, HA).

## House rules (the user)
- Two tokens cover all four orgs: the read-only one is the default; the read+write one (runs as `postgres`) is only for
  writes the user approved, never for altering tables live flows write to; never print or commit either value.
- Before any write, backfill, function, policy or trigger change: prove the problem with real rows, list everything that
  reads or writes the change (n8n workflows, dashboards, daily checks, other companies' copies, triggers), replay old vs
  new, then present on a review page the user marks.
- plpgsql only checks columns at run time: run refresh functions end to end into temp copies and compare counts before
  applying; never append a `--` comment in the middle of a SQL line during a string replace.
- Bulk UPDATEs on tables with an `updated_at` trigger run as `begin; set local session_replication_role = replica; update
  ...; commit;` so rows don't look recently updated. Replica mode also skips FK and other triggers: use it for that one
  statement and verify counts after.
- After applying, watch the first real runs end to end (row really right, dashboard really updated), not just the
  statement's result.
- Paid or live actions ask the user first: new projects or branches (cost confirmation), compute changes, restore/pause,
  edge function deploys, auth settings, anything that emails or texts users.

## Members
| Member | Best at | Path |
|---|---|---|
| supabase | Platform rules: security checklist, keys and tokens, Data API grants vs RLS, CLI and MCP gotchas, local migration workflow, debugging via docs and logs | `members/supabase/SKILL.md` |
| supabase-postgres-best-practices | 30 rule files with wrong/right SQL and numbers: indexes, connections, RLS performance, schema, locking, data access, monitoring, search | `members/supabase-postgres-best-practices/SKILL.md`, `references/` |
| database-optimization | Plan-reading cues, query checklist, dangerous patterns, read replicas, partitioning, ORM N+1 code, MySQL notes | `members/database-optimization/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
