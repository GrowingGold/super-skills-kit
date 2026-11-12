# Node family gotchas (merged)

One catalog built from four sources: `n8n-node-configuration` (NODE_FAMILY_GOTCHAS, OPERATION_PATTERNS),
`n8n-node-configuration-official` (its 8 reference files), `n8n-workflow-patterns` (integration gotchas) and
`n8n-binary-and-data` / `n8n-agents` where a node family is involved. Tags in brackets: [nc] node-configuration,
[off] official, [wp] workflow-patterns, [bin] binary-and-data, [ag] agents, [eh] error-handling.

Field names and defaults drift between n8n versions. The live schema (`get_node` or `get_node_types` with
discriminators) decides the exact shape; this file covers what the schema does not tell you: the consequences.
Every item here validates clean and fails quietly.

## Any node

- Set `resource` and `operation` (and `mode` where it exists) first; most "field does not exist" errors are a missing
  parent value. When the operation changes, rebuild from the new shape instead of carrying old fields. [nc][off]
- UI label and stored value often differ: Slack "Send a message" = `post`, Gmail/Supabase "Get Many" = `getAll`,
  Postgres "Delete" = `deleteTable`. Read the value list, never the label. [nc][off]
- Dropdowns and resource locators (channels, sheets, tables, models, labels) come from live methods. Resolve the real
  value with `explore_node_resources` / `n8n_explore_node_resources` using a real credential id; an invented id validates
  and points at nothing. If several match and intent is unclear, ask. [off][nc]
- `alwaysOutputData: true` keeps a chain alive when a node can legally return 0 items (lookups, writes). [nc]
- Network nodes: `retryOnFail: true`, `maxTries: 3`, `waitBetweenTries: 5000` (caps 5 tries / 5000 ms; retries on any
  error, no status filter). [eh][off]
- Comms nodes append an "n8n attribution" line by default; switch it off for anything a customer reads. [off]

## HTTP Request

- `authentication` is the switch: `none`, `predefinedCredentialType` (native credential exists, prefer it) or
  `genericCredentialType` (header/basic/OAuth2/query). A credential attached while `authentication: none` is silently
  ignored. Tokens in header/query/body parameters are plain text in the workflow JSON: always a credential. [off]
- Body and query each have a second discriminator (`contentType` + `specifyBody`, `specifyQuery`). Fields set under the
  wrong discriminator do nothing. [off]
- Timeout: runtime default is 5 minutes when `options.timeout` is unset (the UI shows 10 s once toggled). Set ~10000 ms
  for external APIs so a hung call cannot stall the run. [off]
- `options.response`: `fullResponse` for headers/status (rate-limit headers), `neverError` to branch on status yourself,
  `responseFormat: "file"` for downloads (otherwise the bytes arrive as garbled text in `$json`). [off][bin]
- Use built-in pagination modes before building a loop with `$pageCount`. [off]
- Don't set the same header through both `headerParameters` and a header-auth credential; they conflict. [validation REVIEW_CHECKLIST]

## Webhook trigger and Respond to Webhook

- Paths are global per instance; two workflows on one path conflict. Static descriptive paths or UUIDs, never
  expressions. [off][expression-syntax]
- Use the trigger's own `authentication` (`basicAuth` / `headerAuth` + credential) for anything that mutates state,
  sends messages or costs money. An IF comparing a header to a hardcoded token is not auth. [off][REVIEW_CHECKLIST]
- `responseMode`: `onReceived` (default, 200 at once, caller never sees output), `lastNode`, `responseNode` (use for
  request/response APIs), `streaming`. [off][nc]
- Output: `{headers, params, query, body, webhookUrl, executionMode}`; payload under `body`; multipart uploads land in
  `$binary`, form fields in `$json.body`. [off][bin]
- Respond `responseCode` defaults to 200 on every branch, including error branches: set it on each one. [nc][off][eh]
- `respondWith: "json"`: pass the object in expression mode (`={{ {status: "ok", id: $('Create').item.json.id} }}`).
  `JSON.stringify(...)` double-encodes. [nc][off]
- Several Respond nodes are fine; the first one that fires answers. [off]

## IF / Filter / Switch

- Switch with no `options.fallbackOutput: "extra"` drops unmatched items. Name the fallback (`renameFallbackOutput`)
  and every rule output (`renameOutput: true`, `outputKey`), and wire the fallback to something real. [nc][off]
- IF error output (when `onError: continueErrorOutput`) is `main[2]`; `main[1]` is the normal false branch. Same idea
  on Switch and Split In Batches: the error slot is the last one. [REVIEW_CHECKLIST]
- Unary operators (`isEmpty`, `true`) need `singleValue: true`; auto-sanitization adds it on save. Real errors: a
  v1-shaped `conditions` object on a v2 node, an empty filter, legacy v1 operator names. [validation-expert]
- A JS error inside a condition expression resolves to `null`, so every item fails the check and the run stays green.
  [expression-syntax]

## Merge

- `numberOfInputs` defaults to 2 (Append/Combine modes). A third wire lands on an input that does not exist and its
  items vanish. Set it to the wire count, then confirm in the saved JSON. [nc][off]
- Choose Branch: `useDataOfInput: "N"` is 1-indexed and fed by the connection at `main[N-1]`. Getting it backwards
  passes through the wrong branch with the right shape. [nc][off]
- `combineByPosition` pairs item N from each input; the counts must line up. It is also the trick to re-attach binary
  after a JSON-only transform (bypass branch). [bin]

## Database: Postgres, MySQL, Supabase, MongoDB

- `{{ }}` inside `parameters.query` is pasted into the SQL before binding: injection. Use `$1, $2` placeholders +
  `options.queryReplacement` (comma-separated, each piece one parameter). The n8n MySQL node uses `$1` too, not `?`.
  Mongo uses object filters. [nc][off]
- No cross-node transactions. Atomic multi-step writes go in one `executeQuery` with
  `options.queryBatching: "transaction"` (set it explicitly; the default has shifted). Pre-compute lookups upstream. [nc][off]
- Zero matched rows = zero items = downstream silently skipped; INSERT/UPDATE/DELETE often return 0 items too.
  `alwaysOutputData: true` + an IF on the result, or read later data via `$('Upstream').all()`. [nc][off]
- Upsert (`INSERT ... ON CONFLICT DO UPDATE` or the `upsert` operation) instead of SELECT → IF → INSERT/UPDATE: one
  query, no race. [off]
- Supabase node wraps PostgREST: per-row CRUD only, no transactions. For joins, CTEs, aggregates, RPC or atomic writes
  use the Postgres node on the same database (direct connection details; RLS does not apply there, so it sees every
  row). [off]
- Supabase node filters: no `isTrue`/`isNull`/`in` conditions; use `condition: "is"` with `keyValue`
  `null|true|false|unknown`. Default optional filter values to a known-empty value so an undefined filter does not
  return everything or a 400. Empty results usually mean the wrong key role: `anon` respects RLS, `service_role`
  bypasses it. [off]
- Bulk/backfill UPDATEs on tables with `updated_at` triggers fake "recently updated"; see supabase-postgres-pro house
  rules before any such write. [the user]

## Slack

- Block Kit must be an object: `={{ { "blocks": $('Build Message').item.json.blocks } }}`. A bare array posts as
  plain text with no error. No stringify-then-reparse hybrids. [nc][off]
- Thread replies need `thread_ts` (moved out of `otherOptions` in newer versions); `reply_broadcast: true` to echo in
  channel. [nc][off]
- `select` decides channel vs user; both are live lookups. [off]
- Chat triggers: exclude the bot's own user id (Slack Trigger `options.userIds` is an exclusion list) or replies
  re-trigger the workflow forever. [ag]

## Gmail, SMTP, Discord, Telegram

- Gmail: `sendTo`, `subject`, `emailType`, `message` are top level; `ccList`, `bccList`, `replyTo`, `senderName`,
  `attachmentsUi` sit under `options`. Comma-separated recipients. Label ids via live lookup. [off]
- SMTP (Send Email): `emailFormat` text/html/both decides which body fields exist; `ccEmail`/`bccEmail` naming differs
  from Gmail. Good fallback when a provider node is rate-limited. [off]
- Discord: `authentication: "webhook"` to post to one channel; OAuth only for bot features. Embed color takes a hex
  string. [off]
- Telegram: `parse_mode` is snake_case under `additionalFields`; MarkdownV2 needs strict escaping, HTML is easier. A bot
  can only message chats it was added to. [off]
- Anything that can re-fire (retries, re-runs, schedules) checks a Data Table/DB record before sending. [off]

## Google Sheets and Drive

- Sheets nodes run once per input item: 100 items = 100 API calls. Aggregate first and write once. [wp][nc]
- Never `append` to sheets with formula columns; use the Sheets API `values.update` (PUT) through HTTP Request with a
  `googleApi` credential. Write numbers as numbers (`parseFloat`), or formulas like `ADD()` break. `UNFORMATTED_VALUE`
  returns numbers, not "N/A" text. [wp]
- Drive `convertToGoogleDocument: true` makes a Google Doc, not a Sheet. CSV download link:
  `https://drive.google.com/uc?id=<fileId>&export=download`. [wp]

## Schedule Trigger

- Timezone comes from Workflow Settings, not the rule. Set it explicitly for local-time jobs (DST, instance moves). [nc][off]
- Cron takes 5 or 6 fields; interval modes are clearer for "every Monday 9am". [nc][off]
- A restart at fire time skips the run (no catch-up). Business-critical schedules are idempotent and can detect a missed
  run at start. [nc][off]

## Execute Workflow Trigger / Execute Workflow

- Input modes: Define Below (typed fields, the default and the only agent-tool-friendly one), JSON example,
  passthrough (only for binary input or zero inputs). [off][subworkflows]
- Caller `mode: each` when the body assumes one item; `waitForSubWorkflow: false` only with a completion tracker.
  Renaming an input field breaks callers silently (`undefined`, no error). [subworkflows]
- `toolWorkflow.workflowId` has no live lookup method: find the id with workflow search, use `mode: "id"`. [off]

## Split In Batches / Loop Over Items

- `main[0]` = done (once, after all batches), `main[1]` = each batch (loop body, wire back to the loop input). Put a
  Limit 1 after done. [wp][nc][code-javascript]
- After the loop, `$('Node inside loop').all()` holds only the last batch; accumulate in
  `$getWorkflowStaticData('global')` (reset before, push inside, read after). [wp]
- Nested loops: inner done → back to the outer loop input; outer done → final aggregate. [wp]
- Iterations are the cost (~0.8 ms engine overhead each): largest batch the real limit allows; batchSize 1 only for
  one-id APIs or nested-loop control. Don't loop at all when nothing limits batch size. [wp]

## AI Agent and LangChain sub-nodes

- Sub-nodes connect from themselves to the agent on `ai_languageModel` / `ai_memory` / `ai_tool` / `ai_outputParser`
  (also `ai_embedding`, `ai_vectorStore`, `ai_document`, `ai_textSplitter`). A tool wired to `main` shows as
  disconnected. All tools stack on `ai_tool` index 0. [ag][mcp-tools-expert]
- Answer is in `$json.output`. [ag]
- `options.maxIterations`: the default is low (single digits to 10); 15-30 for a focused sub-agent, 50+ for a multi-tool
  orchestrator. Hitting it throws "Max iterations reached" or returns empty. [ag][off]
- `temperature: 0` on the model for extraction/classification; model ids come from a live lookup. Small models for
  routing, big ones for reasoning. `options.batching` (`batchSize`, `delayBetweenBatches`) for rate-limited volume. [off]
- Streaming needs all three aligned: trigger (`responseMode: "streaming"`), agent `enableStreaming`, responder. [off]
- `passthroughBinaryImages: true` lets the model see images only; tools never receive binary. [ag][bin][off]
- Memory `contextWindowLength` defaults to 5: start at 50. Key memory on a stable session id from the trigger; never
  `"default"`, never via `$fromAI`. [ag]
- Structured output parser: `schemaType: "manual"` with a real JSON Schema + `autoFix: true` + a coding-capable fixer
  model on the parser's model slot. [ag]
- Text Classifier: every category needs a name and a description (routing reads the description);
  `enableAutoFixing: true`. [ag]

## Data Table node vs data table tool

- In-workflow `dataTable` node reads/writes rows on each run; the `n8n_manage_datatable` tool sets tables up from
  outside. Column type cannot change after creation; `deleteColumn` drops the values with no undo; `deleteRows` needs a
  filter, use `dryRun: true` first. [mcp-tools-expert]
