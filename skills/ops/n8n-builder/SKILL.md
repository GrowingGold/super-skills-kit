---
name: n8n-builder
description: "Build, change, debug, review and harden n8n workflows on any instance (self-hosted or cloud) through n8n-mcp tools, n8n's own instance MCP or the REST API. Use for any n8n or automation task: designing a workflow (webhook, HTTP API, database, scheduled, batch, AI agent), configuring nodes (HTTP Request, Webhook, Respond to Webhook, IF, Switch, Merge, Postgres, Supabase, Slack, Gmail, Sheets, Schedule, Execute Workflow), {{ }} expressions, $json, $('Node'), $jmespath, Luxon, Code node JavaScript or Python, Custom Code Tool, AI Agent, LLM chain, Text Classifier, $fromAI, memory, structured output, RAG, binary files, PDFs, images, onError, retryOnFail, status codes, Error Trigger, sub-workflows, validation errors, false positives, failed or silent executions, wrong instance or NOT_FOUND, data tables, credentials, templates, n8n API 403, self-hosting, Python task runners."
members: [using-n8n-mcp-skills, n8n-mcp-tools-expert, n8n-workflow-patterns, n8n-node-configuration, n8n-node-configuration-official, n8n-expression-syntax, n8n-code-javascript, n8n-code-python, n8n-code-tool, n8n-agents, n8n-binary-and-data, n8n-error-handling, n8n-subworkflows, n8n-validation-expert, n8n-multi-instance, n8n-self-hosting]
---

# n8n Builder

One skill for every n8n job: new builds, changes to live company workflows, debugging, reviews and hosting. It merges the
16 n8n skills (the n8n-mcp-skills pack plus n8n's own node-configuration skill) with house rules for live instances. Load this file first and follow the unified workflow; open a member file only when a mode or step points
to it (`members/<member>/...`). n8n and both MCP servers change between releases: when a live tool (`get_node`,
`get_node_types`, `tools_documentation`) disagrees with anything here, trust the tool and tell the user about the drift.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| "Build / automate / connect X to Y", a new workflow | BUILD | Steps 0-9. Pattern file: `members/n8n-workflow-patterns/` `webhook_processing.md`, `http_api_integration.md`, `database_operations.md`, `scheduled_tasks.md`, `ai_agent_workflow.md` |
| Change or fix anything on a live production instance or any active workflow | LIVE-CHANGE | Every step, no shortcuts, plus House rules. Step 8 is where most damage is prevented |
| "It failed / stopped / sends nothing / data is wrong / items missing" | DEBUG | Step 1, then the silent-failure catalog below; recovery strategies in `members/n8n-validation-expert/SKILL.md`; built-in `superpowers:systematic-debugging` |
| Review or audit a workflow or a whole instance | REVIEW | `members/n8n-validation-expert/REVIEW_CHECKLIST.md` + catalog + `n8n_audit_instance`; report MUST / SHOULD / NICE; change nothing without the user's OK |
| Configure a node, a field "doesn't exist", which operation | NODE | Step 3 + `references/node-family-gotchas.md`; deep: `members/n8n-node-configuration/DEPENDENCIES.md`, `OPERATION_PATTERNS.md` |
| Expressions, field mapping, dates, nested JSON | EXPRESSION | Step 4; `members/n8n-expression-syntax/SKILL.md`, `COMMON_MISTAKES.md`, `EXAMPLES.md` |
| A Code node seems needed | CODE-JS | Gatekeeper (step 4) first; `members/n8n-code-javascript/SKILL.md` + `DATA_ACCESS.md`, `BUILTIN_FUNCTIONS.md`, `ERROR_PATTERNS.md`, `COMMON_PATTERNS.md` |
| the user asks for Python, or a Python Code node errors | CODE-PY | `members/n8n-code-python/SKILL.md`, `COMMON_PATTERNS.md` |
| Code that an AI Agent calls (`toolCode`) | CODE-TOOL | `members/n8n-code-tool/SKILL.md`, `INPUT_SCHEMA.md`, `ERROR_PATTERNS.md` |
| AI Agent, LLM chain, classifier, extractor, memory, RAG, chat bot, approvals | AGENT | `members/n8n-agents/SKILL.md` + `TOOLS.md`, `SYSTEM_PROMPT.md`, `STRUCTURED_OUTPUT.md`, `MEMORY.md`, `HUMAN_REVIEW.md`, `CHAT_AGENT_PATTERNS.md`, `RAG.md`, `EXAMPLES.md` |
| A persisted n8n Agent (`n8n_manage_agents`) | AGENT-PERSISTED | "Persisted n8n Agents" in `members/n8n-agents/SKILL.md`; publish only when the user asks |
| Files, PDFs, images, attachments, base64, vision | BINARY | `members/n8n-binary-and-data/SKILL.md` + `AGENT_TOOL_BINARY.md`, `MERGE_FOR_CONTEXT.md`, `CDN_REQUIREMENT.md` |
| Webhook API, status codes, retries, alerts, "fails silently" | ERRORS | Step 5; `members/n8n-error-handling/SKILL.md` + `API_WORKFLOWS.md`, `RESPONSE_SHAPES.md`, `ERROR_WORKFLOWS.md`, `NODE_ERROR_OUTPUTS.md` |
| Reuse, workflow over ~10-15 nodes, Execute Workflow, parallel runs | SUBWORKFLOW | `members/n8n-subworkflows/SKILL.md` + `SUBWORKFLOW_PATTERNS.md`, `NAMING_AND_DISCOVERY.md` |
| `validate_*` returned errors or warnings | VALIDATE | Step 6; `members/n8n-validation-expert/ERROR_CATALOG.md`, `FALSE_POSITIVES.md` |
| Thousands of items, slow runs | PERF | "Performance" rules below; `members/n8n-code-javascript/DATA_ACCESS.md` (Mode Performance) |
| Which instance, NOT_FOUND, empty reads, copy between instances | INSTANCE | Step 0; `members/n8n-multi-instance/SKILL.md` |
| Exact tool shapes: templates, data tables, folders, credentials, versions, test runs, audit | TOOLS | `members/n8n-mcp-tools-expert/SKILL.md` + `SEARCH_GUIDE.md`, `VALIDATION_GUIDE.md`, `WORKFLOW_GUIDE.md` (1285 lines: open by section), `OPERATIONS_GUIDE.md` |
| Deploy or host n8n, Docker, queue mode, "Python runner unavailable", backups | HOSTING | `members/n8n-self-hosting/SKILL.md` + `TASK_RUNNERS.md`, `QUEUE_MODE.md`, `SECURITY.md`, `DAY2.md`. The user's existing instances: House rules |
| n8n API 403 or "Database is not ready" on the user's instances | ACCESS | House rules (allowlist script, Railway restart) |

Several modes often apply at once (a LIVE-CHANGE that touches an AGENT and a Code node). Run the workflow once and open
each mode's files at the step where it matters.

## Unified workflow

### 0. Orient: which instance, which surface
- Name the instance before the first call: your own (for example Railway), a cloud instance, or a client's. Any live production instance: read freely, change nothing until step 8.
- Identify the tool surface that is actually connected; the same job has different names on each:

| Job | n8n-mcp (community) | n8n instance MCP (official) | REST API (the user's scripts) |
|---|---|---|---|
| Find a node | `search_nodes({query})` | `search_nodes([...])` | - |
| Node schema | `get_node({nodeType:"nodes-base.x"})` standard → `mode:"search_properties"` → `detail:"full"` | `get_node_types([{name, resource, operation, mode}])` | - |
| Live dropdown / locator values | `n8n_explore_node_resources` (needs `N8N_MCP_ACCESS_TOKEN`) | `explore_node_resources` + `list_credentials` | - |
| Validate one node | `validate_node({profile:"runtime"})` | `validate_node_config([{type, typeVersion, parameters, isToolNode}])` | - |
| Validate workflow | `validate_workflow` (JSON) / `n8n_validate_workflow({id})` | `validate_workflow` | - |
| Read a workflow | `n8n_get_workflow` (`structure`, `filtered`+`nodeNames`, `active`) | `get_workflow_details`, `search_workflows` | `GET /api/v1/workflows/{id}` |
| Edit | `n8n_update_partial_workflow({id, intent, operations})` | per its tool list | full `PUT`, only through the helpers in House rules |
| Run / executions | `n8n_test_workflow`, `n8n_executions` | `test_workflow` (pinned data) | `GET /api/v1/executions?workflowId=…&includeData=true` |

  Node-type form trap on n8n-mcp: `get_node` / `validate_node` take SHORT `nodes-base.x` / `nodes-langchain.agent`;
  workflow JSON uses LONG `n8n-nodes-base.x` / `@n8n/n8n-nodes-langchain.agent`. `search_nodes` returns both. [n8n-mcp-tools-expert]
- Preflight: `n8n_health_check({mode:"diagnostic"})` names the resolved instance and reports the `officialMcp` block; read
  it before reaching for token-gated tools (persisted agents, live lookups, pinned runs, native history). [n8n-mcp-tools-expert]
- Multi-instance n8n-mcp: `n8n_instances({mode:"list"})`, then pass `instance:"<name>"` on every call (stateless; never
  rely on the shared default, which other chats can move). An unexpected `NOT_FOUND` or unfamiliar data is a misroute:
  retry on the right instance, never recreate. Switch only in its own turn. [n8n-multi-instance]
- No `n8n_*` tools visible: nothing is broken, the offline tools (search, get, validate, templates) still work. A
  UI-built workflow you can't see usually has "Available in MCP" off; turning it on is a visible persistent change, so
  ask. [using-n8n-mcp-skills]

### 1. Prove the problem before touching anything (DEBUG, LIVE-CHANGE, REVIEW)
- Pull cheaply: `structure` for topology, then `filtered` + `nodeNames` for heavy nodes (a full fetch of a big workflow
  truncates). The body is the draft; `mode:"active"` is the published graph that runs. They can differ. [n8n-mcp-tools-expert]
- Read real executions for a failing case and a good case, in every company copy involved. Find the first node whose
  output is wrong, not the node that finally errored. Inspect values: `null` where data was expected is the symptom of a
  swallowed expression error. [verify-before-fix, n8n-expression-syntax]
- The diagnosis has to explain every case. Look for a second cause. If the user says it's broken, believe them even when the
  execution is green. [the user, using-n8n-mcp-skills]
- Isolate with binary search (disable half, test), `cleanStaleConnections` for "node not found". [n8n-validation-expert]

### 2. Design the shape (BUILD, LIVE-CHANGE)
- Pick the pattern and read its file. Most "simple" flows end up at 10+ nodes, so plan error paths and empty-data cases
  now. [n8n-workflow-patterns]
- Search before building: an existing sub-workflow (names are the only discovery surface; tags can't be filtered), then
  `search_templates`. Tell the user when you reuse one. [n8n-subworkflows, n8n-mcp-tools-expert]
- Fix at the source: the smallest change at the step where the problem starts, plus a one-time cleanup of people already
  affected, rather than safety nets spread over key workflows. [the user]
- Inline vs side branch: a node inserted between two nodes changes the next node's `$json`. Read that node's expressions
  in each company's copy; prefer a side branch for logging/fill steps. In v1 execution order a branch placed above the
  main chain runs first, and one failing node stops the whole run.
- Branches run one after another, never in parallel. Real concurrency = Execute Workflow `mode: each` +
  `waitForSubWorkflow: false` + a Data Table tracking completion. [n8n-subworkflows, REVIEW_CHECKLIST]
- Extract a sub-workflow when logic is reusable, generic (auth, parsing, formatting, ids) or 5+ nodes of one concern;
  not for one bare HTTP call. A 20-node workflow is fine only if it is mostly sub-workflow calls and decisions. [n8n-subworkflows]
- Error posture by trigger: webhook APIs and unattended runs (schedule, queue, agent tool) need full handling; a run the user
  watches themselves can stop on error. [n8n-error-handling]
- Choose the AI node: Agent (tools, memory, multi-turn), Basic LLM Chain (one shot), Text Classifier (route to N
  branches, not Agent + Switch), Information Extractor (fields), Sentiment, Summarization, and the provider's native node
  for image/audio/video (never inside an Agent). [n8n-agents]

### 3. Configure each node from the live schema
1. Set `resource`, `operation` (and `mode`) first, then fetch the schema with those discriminators: generic shapes miss
   operation-specific required fields. Changing the operation means re-deriving, not carrying fields. [both node-config members]
2. Resolve dropdown and resource-locator values with the live lookup (n8n-mcp needs all six: LONG `nodeType`, `version`,
   `methodName` + `methodType` copied from `dynamicOptions`, `credentialType`, `credentialId`; dependencies in
   `currentNodeParameters` keeping `{__rl:true, mode, value}`). Use the returned `value`, never `name`, never a guess. [official, node-configuration]
3. Node JSON hygiene: UUID v4 node ids; current `typeVersion` from the schema; no `credentials` block with a placeholder
   id (it locks the selector in the UI); omit it, or list credentials and use a real id nested as
   `{"httpHeaderAuth": {"id", "name"}}`; secrets only in credentials. [n8n-mcp-tools-expert]
4. Start minimal, validate the single node, add the fields its errors ask for (2-3 rounds is normal). Mark `ai_tool`
   sub-nodes `isToolNode: true` on the official validator. Don't hand-fix operator metadata; auto-sanitization does it. [node-configuration, official, validation-expert]
5. Check the family in `references/node-family-gotchas.md` before moving on.
6. Edit surgically: `n8n_update_partial_workflow` with `intent`; `updateNode` takes `updates` (a `null` removes a
   property); `patchNodeField` for code/HTML/JSON strings (errors on zero or multiple matches, which is the point); smart
   params `branch:"true"` / `case:0`; AI wiring via `sourceOutput:"ai_tool"` etc. Build iteratively, not one shot. [n8n-mcp-tools-expert]

### 4. Wire the data
- `{{ }}` belongs in node fields only, never in Code nodes, webhook paths or credential fields. Webhook data is under
  `$json.body`; uploaded files are in `$binary`. Bracket notation for keys with spaces. [n8n-expression-syntax]
- Reference upstream by name, `$('Node').item.json.x` (`.first()`, `.all()`), instead of deep `$json.x`, which breaks
  silently when a node is inserted or item context resets. Where branches converge, add a NoOp ("Combine Inputs") and
  reference it; use a Set instead if the branch shapes differ. [n8n-expression-syntax]
- Transform gatekeeper, stop at the first that fits: (1) expression in the consuming field, `$jmespath` for nested JSON;
  (2) arrow-function IIFE inside an Edit Fields field `={{ (() => { ... })() }}`; (3) Code node, only for whole-dataset
  aggregation, allowlisted libraries or async work. Native nodes first for hashing (Crypto), XML/SOAP/RSS (XML), HTML. [n8n-expression-syntax, n8n-code-javascript]
- A Set node feeding 0-1 consumers goes: inline its expression. It stays for 2+ consumers of a non-trivial value, a
  sub-workflow's final Return node, or a deliberate rename/whitelist. Build email/Slack/SMS bodies inside the comms node. [n8n-expression-syntax, official]
- `$jmespath(object, "query")`: object first, `'strings'` in single quotes (double quotes mean a field), `` `numbers` ``
  in backticks, `&&`/`||`; over `.all()` keep the `json.` prefix. Mistakes return `[]` or `null` without failing. [n8n-expression-syntax]
- Nodes aggregating `.all()` need `executeOnce: true`, or they rerun per item. Never paste commented code into an
  expression. Date math in Luxon inline, not a Date & Time node. [REVIEW_CHECKLIST]

### 5. Harden
- `retryOnFail: true, maxTries: 3, waitBetweenTries: 5000` on every network node, first, so transient 429s never reach
  error paths. [n8n-error-handling]
- Error output = two moves: `onError: "continueErrorOutput"` and a wire on the node's last `main[]` slot (`main[1]` on
  HTTP, `main[2]` on IF). One without the other silently loses errors or leaves the handler unreachable. Add-on nodes in
  live chains get `continueRegularOutput` instead (see conflicts). [n8n-error-handling, REVIEW_CHECKLIST, the user]
- Webhook APIs: `responseMode: "responseNode"`; 4xx decided upstream (IF or the Set-node schema validator), 5xx from
  error outputs; explicit `responseCode` on every Respond; one expression-driven Respond when branches differ only in
  code and message; body `{error, message}` with no stack, SQL, upstream body or token. [n8n-error-handling]
- Unattended workflows: an Error Trigger workflow (workflow name, editor + execution links, failed node, the real
  message) that alerts on a different channel than the monitored flows, with a Data Table fallback. Assigning it is a UI
  setting: give the user the exact click path. [n8n-error-handling]
- Guard the data, not just the node: after a transform whose output matters, an IF checks the field exists, because
  expression errors become `null` and Python static rejections pass input through as "success". [n8n-error-handling, n8n-code-python]
- Anything that sends or can re-fire (retries, schedules after a restart) checks a record before sending. [official, workflow-patterns]

### 6. Validate, then verify the wiring yourself
- `validate_workflow` with the `runtime` profile while building; `ai-friendly` / `strict` before production (they are
  stricter, not looser). Fix every error; judge advisories (retry, error handling, unbounded query) against the context;
  security and deprecation warnings are real. [n8n-validation-expert]
- Autofix: preview first (`applyFixes:false`), then apply `confidenceThreshold:"high"`. When the "error handlers in
  main[0]" error is the known n8n-mcp#1111 false positive (Respond/Send Email on the success path by design), keep the
  wiring, say so, and exclude `error-output-config`. [n8n-validation-expert]
- Validation proves shape, not logic. Pull the saved workflow and read `connections`: Merge `numberOfInputs` equals the
  wire count and `useDataOfInput: "N"` sits on `main[N-1]`; Switch fallback goes somewhere; each error output has both
  halves; sub-nodes hang on `ai_*`, not `main`; no fan-out branch dead-ends; parameters actually landed. [workflow-patterns, error-handling, official]
- Walk the MUST FIX and SHOULD FIX sections of `members/n8n-validation-expert/REVIEW_CHECKLIST.md`. [n8n-validation-expert]

### 7. Test without surprises
- A test run fires real nodes: Code, HTTP, DB writes, SMS and email, paid AI calls. `pinned` stubs only trigger,
  credentialed and HTTP Request nodes; `direct` runs everything; `executionMode:"production"` changes context, not side
  effects. On company instances there are no casual test runs: ask the user first. [n8n-mcp-tools-expert, the user]
- Safe path for live changes: a throwaway inactive copy, send/write nodes disabled or pointed at test data, a real saved
  payload with the same headers the real caller sends; then read the output values, not the green badge. With write nodes
  disabled, downstream verify nodes receive the request body, so make them tolerant. workflow-patterns]
- Run shapes: `pinData` is `{"Node Name": [{"json": {...}}]}`; `auto` fires webhook/form/chat triggers and needs the
  workflow active; Manual/Schedule/sub-workflows need `prepare` then `pinned` (token + "Available in MCP", ask before
  `exposeToMcp:true`); `direct` returns at start, so poll `n8n_executions`. [n8n-mcp-tools-expert]
- Binary: confirm the `binary` slot per node in the execution; validation can't see a stripped file. [n8n-binary-and-data]

### 8. Present, then apply (LIVE-CHANGE)
- Document first, change nothing: a review page with one card per change (old vs new side by side, the reason in plain
  words, pick + note saved to the page's store). Read the picks back and build only from them; a note beats a radio
  pick; anything kept against a pick or found mid-build gets its own card.
- The page carries the evidence (step 1), the impact list (every node, workflow, dashboard, daily check and company copy
  that reads or writes what changes), a replay on recent real runs (old vs new), risks and the undo.
- Apply in one write that also adds the change-log note, after a backup; append the company change register; never write
  over a teammate's unpublished draft. The user runs the apply (one `!` command as the last line). Claude-built workflows also
  get or refresh their notes and doc section.
- Activate only after steps 6-7 pass and the user said yes; activating a flow that sends is itself a live change.

### 9. Watch the first real runs
- Follow the first real executions end to end into the destination system (row written, offer confirmed, message
  delivered), not just the new node's output, and keep checking the runs that follow.

## Core rules and checklists

### Silent-failure catalog (validates clean, runs green, wrong result)
| Trap | Fix |
|---|---|
| Switch without fallback drops unmatched items | `options.fallbackOutput:"extra"`, named, wired |
| Merge third source vanishes / wrong branch passed | `numberOfInputs` = wires; `useDataOfInput "N"` ↔ `main[N-1]` |
| Error output half-wired | `onError` + wire on last `main[]` slot, verify both |
| Error branch answers 200; `onReceived` hides output; stringified JSON body | explicit `responseCode`; `responseNode`; pass the object |
| JS error inside `{{ }}` becomes `null` (Filter drops all, run green) | test with real items; temporary `try { return JSON.stringify(x) } catch (e) { return 'ERROR: ' + e.message }` IIFE |
| `$json` after an inserted node or converging branches | `$('Node').item.json`, NoOp anchor |
| `{{ }}` in SQL | `$1..$n` + `queryReplacement` |
| 0 rows / write ops return 0 items, chain stops | `alwaysOutputData:true` + IF |
| Credential attached but `authentication:"none"` | set the auth mode |
| Slack blocks as bare array / reply without `thread_ts` | `{ "blocks": ... }` object; set `thread_ts` |
| Code node or Edit Fields drops `$binary` | re-attach `binary`, `includeOtherFields`, or Merge `combineByPosition` bypass |
| Python import/dunder rejected or bad return shape: input passes through as success | import-free code, right shape, test run |
| `.all()` after a loop = last batch only; `main[0]` is done, not each | static data accumulator; Limit 1 after done |
| Aggregating `.all()` without `executeOnce` | `executeOnce:true` |
| Schedule in host timezone; restart skips a run | workflow timezone; idempotent + missed-run check |
| Sub-workflow input renamed; callers send old name → `undefined` | migrate every caller in the same change |
| Chat bot answers itself forever | exclude the bot user id at the trigger |
| Agent stops at "max iterations"; memory forgets after 5 turns | raise `maxIterations`; `contextWindowLength` 50 |
| Side branch above the main chain fails first and stops everything | add-ons `continueRegularOutput`, tested in a copy |
| UI label used as value (`send`, `getMany`) | read the value list (`post`, `getAll`) |

### Code runtimes at a glance
| | Expression / Edit Fields IIFE | Code node JS | Code node Python | Custom Code Tool | Persisted-agent custom tool |
|---|---|---|---|---|---|
| Input | `$json`, `$('Node')`, `$now` | `$input.all()` / `.first()` / `.item` | `_items` / `_item` (dicts) | `query` (JS) / `_query` (Py) | per `action:"reference"` |
| Return | a value | `[{json:{...}}]` | `[{"json":{...}}]` / `{"json":{...}}` | a string (`JSON.stringify`) | TypeScript, imports `@n8n/agents`, `zod` only |
| Helpers | Luxon, `$jmespath` | `this.helpers.httpRequest` (no auth), Luxon, `$jmespath`, `$getWorkflowStaticData` | none; imports blocked | Luxon only | - |
| Use when | default | whole dataset, libs, async | only on the user's request | pure computation an agent calls | `n8n_manage_agents` |

### JavaScript Code node [n8n-code-javascript]
- "Run Once for All Items" by default; Each Item only for per-item isolation. Every branch returns `[{json}]` (a bare
  object auto-wraps in All Items mode; a primitive or `null` fails). `$input.item` exists only in Each Item mode.
- `this.helpers.httpRequest()` works; the bare `$helpers` global is undefined; `httpRequestWithAuthentication` is
  deny-listed, so authenticated calls go through an HTTP Request node. `$env` is blocked on n8n 2.x defaults;
  `require()` only for instance-allowlisted modules (use them when the instance allows; ask when unsure).
- New items that don't map 1:1 need `pairedItem: {item: i}`; compare money in cents (`Math.round(a*100)`); threshold
  checks use `Math.abs(diff) > limit` so crashes are caught as well as spikes; optional chaining for missing fields; a
  one-line comment saying why an expression wasn't enough. [+ n8n-workflow-patterns]

### Python Code node [n8n-code-python]
- Only when the user asks. `_items` (all-items) / `_item` (each-item), dict access only; legacy `_input`, `_json`, `_node`,
  `_now`, `_jmespath` raise `NameError`. No imports unless confirmed on that instance (Cloud: none), no classes,
  `type()`, `getattr`, dunders; `nonlocal` not `global`. Sets become strings and datetimes `str(dt)` on output: convert.
  Each-item `None` drops the item. "Python runner unavailable" is infrastructure (task-runner sidecar), not code.

### Custom Code Tool [n8n-code-tool]
- Returns a string; input is `query`/`_query`; no `$fromAI`, `$input`, `$json`, `$helpers`, `$jmespath`, static data.
  Name `[A-Za-z0-9_]+`, verb-first; the description says when to call it and, in unstructured mode, shows the JSON
  string to send; `specifyInputSchema: true` for typed multi-field input. Error messages are written for the model
  (what was wrong, what a valid call looks like). Need `$fromAI`, helpers or credentials → `toolWorkflow` instead.

### AI agents [n8n-agents]
- Tool names and descriptions are the prompt: verb-first specific names, real descriptions, one tool with a mode
  parameter rather than two near-twins. Per-tool usage lives in the tool description; persona, global rules and
  `{{ $now }}` in the system prompt.
- `$fromAI('name', 'specific description with format and example', 'type')` only for what the model should decide;
  plumb identity, limits and session ids from workflow context. `$fromAI` carries JSON only, never binary.
- Sends, payments, refunds and account changes sit behind a HITL review node (wrapped tool → review → agent on
  `ai_tool`); the approval message shows `{{ $tool.parameters.<name> }}`, not a paraphrase. Whether to gate is the user's call.
- Files reach tools as storage keys or URLs (pre-stage upload, inject keys in the system prompt, `executeOnce` on the
  agent); chat surfaces need an HTTPS URL, signed for sensitive content. Ask which storage the user uses. [n8n-binary-and-data]
- RAG last: exact lookups use a DB/Data Table, fresh facts a search tool; vector store as `retrieve-as-tool`, same
  embedding model for documents and queries.
- Persisted agents: `reference` → `discover_assets` → `create` → `mutate` (send the latest `configHash` back as
  `args.baseConfigHash`) → `validate`; `call` is a live run whose `approvals[]` only the user decides; name test agents
  `[TEST] …` and delete them.

### Sub-workflow contract [n8n-subworkflows]
- Define Below typed inputs (passthrough only for binary or zero inputs); verb-first prefixed name (`Subworkflow:`,
  `<Domain>:`, `Tool:`); description lists inputs, outputs and keywords; final `Return` Set node with natural shapes;
  expected failures return `{ok:false, error}`; side effects stated in name and description; caller `mode` and
  `waitForSubWorkflow` set on purpose. N divergent input contracts → N outer workflows + one shared core.

### Performance (measured on n8n 2.x) [n8n-workflow-patterns, n8n-code-javascript, n8n-expression-syntax]
- Per item: Code All Items ~0.02 ms, any expression ~0.2 ms, Code Each Item ~0.6 ms (25-30x All Items); every node hop
  re-copies all items (~0.05 ms/item); each loop iteration ~0.8 ms; Code node cold start can reach 500-1000 ms; Python
  ~0.4 s (1 s cold). Expression complexity is nearly free: cut node and iteration counts instead.
- Below a few hundred items none of this matters, and most real workflows are I/O-bound: profile before optimizing.

### Tool-call hygiene (n8n-mcp) [n8n-mcp-tools-expert]
- `get_node` standard detail covers most needs; `full` only when stuck. Pass `profile:"runtime"` explicitly.
- Credentials: `n8n_manage_credentials` never returns secrets; `getSchema` before `create`; `includeUsage:true` before
  rotating or deleting to see what breaks. Name the instance on every credential write. [n8n-multi-instance]
- Folders: placement is write-only (verify through the folder's counts); deleting a folder without
  `transferToFolderId` archives its workflows. Versions: `source:"local"` = n8n-mcp snapshots, `"native"` = n8n's own
  history including UI edits.

### Pre-apply gate (every answer yes)
- [ ] Problem proven on real executions in every affected copy; second cause ruled out
- [ ] Each touched node configured from the live schema; family gotchas checked
- [ ] Downstream `$json` readers checked in each company's copy; add-ons are side branches
- [ ] No secrets in fields, no placeholder credentials, webhooks with side effects authenticated
- [ ] Error posture fits the trigger; error outputs fully wired; status codes explicit
- [ ] `validate_workflow` clean (or advisories justified) and `connections` read by hand
- [ ] Tested safely with real-shaped data; output values inspected
- [ ] Review page approved; change note + undo in the same write; register updated
- [ ] Watch plan for the first real runs


**Eval lessons (graded runs):**
- Retry sub-flows: exponential backoff with jitter, honour `Retry-After` on 429/503, retry only network errors, 408, 425, 429
  and 5xx, keep in-node waits under 65 s (use a Wait node beyond), and redact keys and auth headers from alert payloads
  (the old picks added jitter, Retry-After and redaction; keep them).
- Writes that can be re-delivered (webhooks, voice or form vendors) are idempotent: upsert or appendOrUpdate on the event id.

## When members disagree

| Between | Issue | Resolution |
|---|---|---|
| expression-syntax examples vs its own branch rule | `$node["Name"].json` vs `$('Name').item.json` | New work uses `$('Name')`; leave legacy `$node[...]` in existing flows unless the change touches that field |
| workflow-patterns quick starts vs expression-syntax | Examples map fields in a Set node | The Set-node rule wins; the examples are outdated |
| workflow-patterns | `{{$json[0].field}}` for "first item" | Wrong (`$json` is one item): `$('Node').first().json.field` or `executeOnce` |
| workflow-patterns vs REVIEW_CHECKLIST | "Parallel processing" branches | Branches run sequentially; concurrency only via each + no-wait sub-workflows |
| error-handling vs the user's lesson and validation-expert's sample suggestion | `continueRegularOutput` "rare, usually wrong" vs "every new node continueRegularOutput" | Mode switch: add-on side-branch nodes in a live chain (logging, fill, notify) use `continueRegularOutput` so they can never stop the main run; nodes whose result matters use `continueErrorOutput` + a wired handler; never half-wired |
| mcp-tools-expert vs workflow-patterns gates vs the user | "activateWorkflow → go live", "don't forget to activate" | Activate only after validate + verify + safe test, and on company instances only after the user approves |
| mcp-tools-expert vs the user's "no test calls" | `n8n_test_workflow` as a routine step | Runs are live; ask first, prefer a throwaway inactive copy with sends disabled |
| node-configuration vs node-configuration-official | `get_node` + detail levels vs `get_node_types` + discriminators | Same rule (live schema, operation first) on two servers: use the connected one; on n8n-mcp apply the discriminator idea through `search_properties` and per-operation validation |
| node-configuration-official | Points to sibling `*-official` skills (ai-nodes, credentials-and-security, loops, expressions, error-handling) | Not included: route to n8n-agents, n8n-mcp-tools-expert, n8n-workflow-patterns, n8n-expression-syntax, n8n-error-handling |
| node-configuration-official | `merge.input(n)` / `.onTrue()` SDK syntax | That is n8n's code SDK; the MCP and REST paths use JSON connections; only the index rule carries over |
| expression-syntax vs REVIEW_CHECKLIST | `$env` works unless blocked vs "doesn't work" | Treat as blocked (n8n 2.x default) and never use it for secrets: credentials, `$vars` or a Data Table |
| n8n-agents vs official AI_NODES | `maxIterations` 15 / 50-200 vs "raise to 30-50+" | 15-30 for a focused sub-agent, 50+ for a multi-tool orchestrator; read the live default |
| validation-expert (older docs) | `ai-friendly` described as looser | It is stricter than `runtime` (cumulative profiles) |
| code-javascript older text vs current | Bare-object return "fails" | Auto-wrapped in All Items mode now; still write `[{json}]` |
| n8n-error-handling examples vs n8n-mcp-tools-expert | `updateNode` with `changes: {...}` vs `updates: {...}` | Use `updates` (the tools guide and its common-mistakes list); if the server rejects it, read `tools_documentation` for `n8n_update_partial_workflow` |
| using-n8n-mcp-skills | "Invoke each specialist skill with the Skill tool" | This super-skill replaces the router: read the member file path from the mode table |
| n8n-self-hosting vs the user's setup | Docker + Caddy template on a fresh VM | Use it only for a brand-new deployment; the user's existing instances (Railway, two company droplets behind nginx) follow House rules and get no infra changes beyond those |
| n8n-mcp partial edits vs the user's REST helpers | Diff ops vs full PUT | Prefer partial ops when n8n-mcp reaches the instance; full PUT only via the helpers (fresh GET, backup, change note in the same PUT, refuse unpublished drafts) |

## Combine with
- Built-ins: `superpowers:systematic-debugging` (DEBUG), `superpowers:verification-before-completion` (before saying
  done), `superpowers:brainstorming` for a vague new automation, `artifact-capabilities` + `artifact-design` for the user's
  review page, `anthropic-skills:docs` for the Claude-built workflows doc.
- Sibling super-skills (`~/.claude/skill-library/<area>/<name>/SKILL.md`): `supabase-postgres-pro` for
  the SQL behind Postgres/Supabase nodes, `debug-lab` for hard multi-system bugs, `dashboard-studio` when a workflow feeds
  a dashboard.
- Specialist agent prompts (`~/.claude/skill-library/agents/voltagent/`), give them the workflow JSON and the executions:
  `04-quality-security/error-detective.md` (correlate failures across workflows), `09-meta-orchestration/workflow-orchestrator.md`
  (state, retries, compensation for long flows), `05-data-ai/prompt-engineer.md` (agent system prompts and tool
  descriptions), `05-data-ai/llm-architect.md` (RAG and multi-model design), `04-quality-security/security-auditor.md`
  (instance audit: secrets, open webhooks), `01-core-development/api-designer.md` (webhook API contracts).

## House rules (the user)
- Prove, game out system-wide, replay, then present on a review page the user marks; build only from their picks; afterwards
  watch the first real runs end to end.
- Every change to any n8n workflow leaves an in-workflow change-log sticky (what, how, why with numbers, date + approver,
  exact undo), written in the same PUT, plus a change register; keep a workflow backup so the undo is one restore.
- Every Claude-built workflow gets the purple "How this workflow works" note, a blue note under every node, and its
  section with a Mermaid map in the Claude-built workflows doc; refresh them on every change.
- Copies of a workflow on different instances can differ: check downstream `$json` use in each copy before inserting a node, prefer side branches,
  new nodes `continueRegularOutput`, no commented code in expressions, dry-run in an inactive copy.
- Fix at the origin step with the smallest change plus a one-time cleanup; explain it in 2-3 plain steps.
- On a Railway-hosted instance: REST with Python `urllib` (curl mangles JSON); "Database is not ready" with a
  healthy Postgres is fixed by restarting the n8n deployment.
- An API 403 on a self-hosted instance can mean an IP allowlist in front of it: check that first, and use server access for nothing else.
- Anything that sends, calls, publishes, activates or runs paid AI on a live instance asks the user first; no casual test
  calls; keys live in environment variables or a credentials file outside the repo and are never printed or pasted into node fields.

## Members
| Member | Best at | Path |
|---|---|---|
| using-n8n-mcp-skills | Router: red-flag thoughts, drift rule, two tool tiers, "can't find UI workflow" | `members/using-n8n-mcp-skills/SKILL.md` |
| n8n-mcp-tools-expert | Exact n8n-mcp tool shapes: forms, partial ops, test methods, versions, folders, data tables, credentials, audit | `members/n8n-mcp-tools-expert/SKILL.md` (+ 4 guides) |
| n8n-workflow-patterns | Six architectures, lifecycle gates, batching and loops, Sheets/Drive gotchas | `members/n8n-workflow-patterns/SKILL.md` (+ 5 pattern files) |
| n8n-node-configuration | Operation-aware config, displayOptions, detail ladder, patchNodeField, family gotchas | `members/n8n-node-configuration/SKILL.md`, `NODE_FAMILY_GOTCHAS.md` |
| n8n-node-configuration-official | Discriminator-first flow, never-guess lookups, per-family references (HTTP, webhook, comms, DB, AI, triggers, Merge, Switch) | `members/n8n-node-configuration-official/SKILL.md`, `references/` |
| n8n-expression-syntax | `{{ }}` rules, gatekeeper, `$jmespath`, Set antipattern, NoOp convergence, null-on-error debugging | `members/n8n-expression-syntax/SKILL.md` |
| n8n-code-javascript | Code node modes, data access, sandbox limits, static data, performance model | `members/n8n-code-javascript/SKILL.md` |
| n8n-code-python | Native Python runtime limits, return shapes, onError passthrough trap | `members/n8n-code-python/SKILL.md` |
| n8n-code-tool | Custom Code Tool contract (string out, `query` in) | `members/n8n-code-tool/SKILL.md` |
| n8n-agents | AI node choice, tools as prompt, structured output, memory, HITL, chat topologies, persisted agents | `members/n8n-agents/SKILL.md` |
| n8n-binary-and-data | `$binary` vs `$json`, keeping files alive, agent-tool boundary, CDN for chat | `members/n8n-binary-and-data/SKILL.md` |
| n8n-error-handling | Two-step error outputs, retries, 4xx/5xx map, error workflows | `members/n8n-error-handling/SKILL.md` |
| n8n-subworkflows | Search-before-build, typed contracts, all vs each, parallel dispatch, naming | `members/n8n-subworkflows/SKILL.md` |
| n8n-validation-expert | Profiles, error types, false positives, autofix, review checklist | `members/n8n-validation-expert/SKILL.md`, `REVIEW_CHECKLIST.md` |
| n8n-multi-instance | Per-call `instance`, misroute recovery, safe credential writes | `members/n8n-multi-instance/SKILL.md` |
| n8n-self-hosting | Docker + Caddy deploy, queue mode, task runners, secrets, day-2 | `members/n8n-self-hosting/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
