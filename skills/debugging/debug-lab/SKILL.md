---
name: debug-lab
description: Find the real cause of hard bugs, slowdowns, flaky failures, broken live workflows and stuck AI-agent runs, then fix at the source and prove it end to end. Use for "debug this", "diagnose", "why is this failing", "it's broken", "throws", "error", "stack trace", "test failing", "regression", "it got slow", "performance", "flaky", "sometimes fails", "works locally", "bisect", "root cause", "postmortem", "n8n execution failed", "workflow didn't fire", "wrong data in Supabase", "call went wrong", "webhook not arriving", "agent is looping", "stuck", "retrying", "max tool calls", "context drift", "command denied", "tool keeps failing". Builds a tight red-capable feedback loop first, minimises, ranks falsifiable hypotheses, instruments one variable at a time, adds a regression test at the right seam, and verifies in the destination system; has a separate capture-diagnose-recover-report loop for agent failures.
members: [diagnosing-bugs, agent-introspection-debugging]
---

# Debug Lab

Two library skills on top of the always-on `superpowers:systematic-debugging` (its iron law: no fix without root-cause investigation)
and the `/debug` report format. `diagnosing-bugs` adds the part that decides most hunts: build a tight feedback loop before forming
any theory, minimise, rank falsifiable hypotheses, tag instrumentation, and lock the fix in at the correct seam.
`agent-introspection-debugging` adds a loop for when the agent itself is failing. On top sit the user's live-ops rules: prove the cause for
every company copy, fix at the origin, verify in the destination system. Load this first; open member files only when a route says so.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| Error, stack trace, failing test, wrong output in code | Code bug | Workflow 0-10. `members/diagnosing-bugs/SKILL.md` |
| "It got slow", timing regression, heavy query | Perf | Baseline measurement, then bisect; logs are usually the wrong tool. Perf branch (Core rules); agent `performance-engineer` |
| "Sometimes fails", flaky test, race | Flaky | Raise the reproduction rate (loop 100x, parallelise, stress, narrow timing). `superpowers:systematic-debugging` file `condition-based-waiting.md` for waits |
| Worked at version/commit/dataset X, broken at Y | Bisect | Bisection harness + `git bisect run`, or a differential loop old vs new. |
| n8n execution, voice-agent call, CRM workflow, webhook, Supabase rows or dashboard numbers wrong | Ops incident | Workflow with the ops loops (Core rules); prove across every copy; fix through the user's change protocol. |
| The agent run is failing: loops, retries, max tool calls, context drift, tools or commands denied | Agent failure | Agent loop (Core rules). `members/agent-introspection-debugging/SKILL.md` |
| Small, obvious bug right in front of you | Quick | `superpowers:systematic-debugging` + `/debug` format; still reproduce before fixing. |
| A human must click to reproduce | HITL loop | Copy `members/diagnosing-bugs/scripts/hitl-loop.template.sh` to the scratchpad and edit the steps. The Bash tool can't take keyboard input, so give the user one `! bash <path>` line to run; read the KEY=VALUE block it prints. Sign-ins stay the user's `step`, never a `capture`. |
| Can't build any loop | Stop | Say so, list what you tried, ask for access, a redacted artifact, or permission to instrument. |
| No seam can hold a regression test, or 3 fixes failed | Architecture | Hand to `plan-and-execute` (architecture scan) or `think-and-decide`. |
| Fix is in; now tests and hardening | Test | `test-and-harden` super-skill. |

## Unified workflow

### 0. Redact first [diagnosing-bugs]
Everything you show (commands, outputs, payloads, headers) has secrets replaced with `<REDACTED>`. Build loops against environment
variables so credentials stay out of what you print; quote only the lines that carry the signal. If redacted output isn't enough,
say so and ask. Never read the credentials file into output.

### 1. Capture the failure [agent-introspection Phase 1, systematic-debugging Phase 1]
Write down, before touching anything: the exact symptom in the user's words; the full error text and stack (read it all; it often holds
the answer); the last step known to work; recent changes (git log/diff, deploys, workflow versions, config, dependencies); and the
environment assumptions to verify (cwd, branch, port, env vars, which company copy or account). Read `GLOSSARY.md` and ADRs in the area
if they exist [diagnosing-bugs].

### 2. Build a feedback loop [diagnosing-bugs Phase 1]
This is the skill; everything after it is mechanical. With a tight pass/fail signal that goes red on this bug, bisection, hypotheses and
instrumentation all just consume it. Without one, staring at code won't save you. Be creative and refuse to give up. Options, roughly
in order: failing test at the seam that reaches the bug; curl/HTTP script against a dev server; CLI run with a fixture diffed against a
known-good snapshot; headless browser script asserting on DOM/console/network; replay of a captured request, payload or event log;
throwaway harness (one service, mocked deps, one call); property/fuzz loop over many random inputs; bisection harness; differential
loop (old vs new, config A vs B); HITL script as the last resort. Live-ops equivalents are in Core rules.

Then tighten it: faster (cache setup, narrow scope), sharper (assert the exact symptom, not "didn't crash"), deterministic (pin time,
seed RNG, isolate filesystem, freeze network). A 30-second flaky loop is barely better than none; a 2-second deterministic one is a
superpower.

**Gate:** name one command you have already run (show it and its redacted output) that is red-capable (drives the real code path and
asserts the user's symptom), deterministic, fast and agent-runnable. No such command, no hypotheses. If you catch yourself reading code
to build a theory before it exists, stop.

### 3. Reproduce, minimise and prove the scope [diagnosing-bugs Phase 2 + the user]
Run the loop and watch it go red. Confirm it is the user's failure, not a nearby one (wrong bug, wrong fix); reproducible across runs (or
at a pinned high rate); symptom captured for later comparison. Then minimise: cut inputs, callers, config, data and steps one at a time,
re-running after each cut, until every remaining element is load-bearing. The minimal repro shrinks the hypothesis space and becomes the
regression test. For ops: check the cause explains every case and every company copy, and look for a second cause before moving on.

### 4. Compare with what works [systematic-debugging Phase 2]
Find similar code, a workflow copy, or a past execution that works. List every difference however small; read a reference
implementation fully, not skimmed; note what config, environment and dependencies each side assumes.

### 5. Rank falsifiable hypotheses [diagnosing-bugs Phase 3]
Write 3-5 ranked hypotheses before testing any (one hypothesis anchors on the first plausible idea). Each states its prediction: "If X is
the cause, changing Y makes the bug disappear / changing Z makes it worse." No prediction = a vibe; sharpen or drop it. Show the ranked
list to the user as a cheap checkpoint ("we just changed #3" saves hours); don't block if they are away.

### 6. Instrument one variable at a time [diagnosing-bugs Phase 4, systematic-debugging Phase 1.4-1.5]
Each probe maps to one prediction. Prefer a debugger or REPL (one breakpoint beats ten logs), then targeted logs at the boundaries that
separate hypotheses; never log everything and grep. In multi-component chains (webhook -> n8n -> API -> DB), put one tagged entry/exit
probe per boundary and run once to find the failing layer, then dig only there. Trace bad values backward to where they originate.
Tag every debug line with a unique prefix like `[DEBUG-a4f2]` so cleanup is one grep. **Perf:** measure a baseline first (timing harness,
`performance.now()`, profiler, `EXPLAIN ANALYZE`), then bisect; measure first, fix second.

### 7. Fix at the source, test first [diagnosing-bugs Phase 5, superpowers:test-driven-development, the user]
- Regression test before the fix, only at a **correct seam**: one where the test exercises the real bug pattern as it happens at the call
  site. A too-shallow seam gives false confidence. If no correct seam exists, that is a finding: record it and route to the architecture
  scan.
- Turn the minimal repro into the failing test; watch it fail (if you forced red by mutating code or a fixture, `diff` against a pristine
  copy to prove the mutation landed); apply the fix; watch it pass; re-run the original, un-minimised loop.
- Fix where the problem originates with the smallest change, plus a one-time cleanup of records already affected; no safety nets
  sprinkled across key workflows.
- Live systems: the fix goes through the user's change protocol: impact list (every reader/writer, `$json` users per copy, DB triggers,
  dashboards, daily checks), replay old vs new on real data, risks, tested undo, a review card, and the user runs the apply.

### 8. When a fix doesn't hold [systematic-debugging Phase 4.4-4.5, planning-with-files]
Stop and count. Under three attempts: back to step 3 with what you learned; never stack another fix on a failed one, never repeat the
same action. At three: stop fixing and question the architecture (each fix exposing a new problem elsewhere is the tell), then escalate
to the user with the attempt log.

### 9. Verify end to end and clean up [diagnosing-bugs Phase 6, superpowers:verification-before-completion, the user]
- The step-2 loop no longer reproduces; regression test passes (or the missing seam is documented).
- The real outcome is confirmed where it lands (the Supabase row, the CRM contact, the delivered message, the source-system record, the
  dashboard number), not only in the step that changed. For live fixes, watch the first real runs end to end.
- `grep` the debug tag: zero hits. Throwaway harnesses deleted or moved to a marked debug folder.
- Each finding labeled **verified end to end** or **inferred**.

### 10. Report [/debug format + agent self-debug report]
```
Issue: <symptom in the user's words>
Reproduction: <the loop command; minimal repro>
Root cause: <the hypothesis that proved correct, with the evidence>
Fix applied: <change at the source + one-time cleanup> (or: proposed, awaiting the user's pick)
Verified: <checks run, destination-system evidence; verified vs inferred>
Follow-up / prevention: <seam gap, monitoring, memory lesson>
```
State the winning hypothesis in the commit or PR message (when the user asks for one) so the next debugger learns. A lesson that should change
future behavior becomes a memory file.

## Core rules and checklists

### Feedback loops for the user's live systems (new in this merge)
| System | Red-capable loop (read-only unless the user approves) |
|---|---|
| Supabase / Postgres data | A "red query": SQL that returns the bad rows and returns zero once fixed. For functions, run them end to end into temp copies of their target tables (`create temp table <t>_t (like reporting.<t>)`) and compare counts; plpgsql only checks columns at run time, so compiling proves nothing. |
| n8n workflow | Pull the failed execution's input via the API and replay it into a copy of the workflow or the single failing node; diff output against a good execution. Check each company's copy: their nodes and `$json` use differ. |
| Voice/SMS agent platform | Read the call or chat transcript and node path; check every edge type (`edge`, `edges`, `always_edge`, `else_edge`, `skip_response_edge`) before calling a node a dead end. New test calls only in the sandbox and with the user's OK. |
| CRM / webhooks | Replay the captured webhook payload to a local or copy endpoint; confirm the destination record by its source-system ID. |
| Twilio / delivery | Error codes alone don't prove loss: check whether the message or reply actually landed in the destination before calling it an error. |
| Dashboards | Per-card before/after on the same period, not totals; a total can hide a per-card bug. |

### Worked example: an ops incident through the loop (illustrative, no real ids)
"Some approved offers never show as confirmed on the dashboard."
1. Capture: symptom in the user's words; which company; first bad date; the workflow version changed that week.
2. Loop: a red query that lists approved-but-unconfirmed offers since that date; it returns rows now and must return zero after the fix.
3. Scope: run it per company. Only one company's copy has rows, so the cause lives in what differs between the copies.
4. Compare: diff that copy's workflow against a working copy; one node now passes different data to the next.
5. Hypotheses: (a) the next node reads `$json` from the changed node; (b) a DB trigger overwrites the field; (c) the dashboard filter
   changed. Each with a prediction (e.g. a: replaying one failed execution with the old node output turns it green).
6. Instrument: replay one captured execution into a copy of the workflow; (a) confirmed, (b) and (c) ruled out by the trigger list and
   the dashboard query.
7. Fix: smallest change at the origin node + one-time cleanup for the rows the red query lists; impact list, replay on recent
   executions old vs new, review card, the user applies.
8. Verify: red query returns zero; the next real executions land correctly in the table and on the dashboard; findings labeled verified.

### Perf branch [diagnosing-bugs, systematic-debugging]
- Write down the baseline number and how it was measured (same input, warm vs cold, several runs, median and worst) before changing
  anything; logs that "feel slow" are not a baseline.
- Change one thing, re-measure the same way, keep or revert. Bisect commits or config when the regression appeared between two states.
- SQL: `EXPLAIN (ANALYZE, BUFFERS)` before and after; index and query rewrites belong to the `supabase-postgres-pro` super-skill.
- Report before/after numbers side by side; "faster" without numbers is not a result.

### Loop and phase gates [diagnosing-bugs]
- [ ] Loop: one already-run command; red-capable, deterministic, fast, agent-runnable.
- [ ] Repro: the user's exact failure, reproducible, symptom captured.
- [ ] Minimal: every remaining element is load-bearing (removing any one turns it green).
- [ ] Hypotheses: 3-5, ranked, each with a prediction.
- [ ] Probes: one variable each, tagged, tied to a prediction.
- [ ] Fix: regression test red then green at a correct seam (or seam gap documented); original loop green.
- [ ] Cleanup: tags grepped out, throwaways removed, winning hypothesis written down.

### Non-deterministic bugs [diagnosing-bugs]
The goal is a higher reproduction rate, not a clean repro: loop the trigger 100x, parallelise, add load, inject sleeps, narrow timing
windows. 50% flake is debuggable; 1% isn't yet, so keep raising it. Replace arbitrary sleeps in tests with condition-based waits.

### When you genuinely cannot build a loop [diagnosing-bugs]
Stop and say so explicitly, list what you tried, and ask the user for one of: access to the environment that reproduces it; a redacted
captured artifact (HAR, log dump, execution id, call id, screen recording with timestamps); or permission to add temporary production
instrumentation (for n8n or a voice/CRM platform that is a change: it goes through the change protocol). Don't hypothesise without a loop.

### Agent-failure loop [agent-introspection-debugging]
1. **Capture** (before any retry): task, goal in progress, error, last successful step, last failed tool/command, repeated pattern,
   environment assumptions to verify, context pressure (repeated plans, pasted logs, runaway notes).
2. **Classify** the pattern before changing anything:

| Pattern | Likely cause | Check |
|---|---|---|
| Max tool calls / same command repeating | loop with no exit condition | last N calls for repetition |
| Degraded reasoning, context overflow | unbounded notes, duplicate plans, huge logs | recent context for low-signal bulk |
| `ECONNREFUSED` / timeout | service down or wrong port | health, URL, port (the user: 8080 is busy, use 8888) |
| `429` / quota | retry storm, missing backoff | count calls, check spacing |
| File missing after write / stale diff | wrong cwd, race, branch drift | path, cwd, `git status`, file exists |
| Tests still red after the "fix" | wrong hypothesis | isolate the failing test, re-derive (back to step 3) |
| Bash call returns "no verdict, a hook changed this input" | the RTK hook rewrote the command | re-issue the exact rewritten input once; if denied again, stop and tell the user |
| `npm` permission error | npm cache permissions | add `--cache /tmp/npm-cache` |
| `git push` auth rejected | stale `GITHUB_TOKEN` in env | push with the token unset |
| claude.ai connectors disappear | `ANTHROPIC_API_KEY` exported in the shell | unset it; export it only in the shell that needs it |

   Ask: logic, state, environment or policy failure? Did the agent drift to the wrong subtask? Deterministic or transient? What is the
   smallest reversible action that would confirm the diagnosis?
3. **Contained recovery**, smallest first: restate the real objective in one sentence; verify world state instead of trusting memory;
   shrink scope to one command, file or test; run one discriminating check; only then retry. Other safe moves: stop retries and restate
   the hypothesis, trim low-signal context, switch from speculation to direct observation, escalate when high-risk or externally
   blocked. Never claim an auto-heal ("reset agent state") you didn't actually perform with a real tool.
4. **Report:** task, failure, root cause, recovery action, result (success / partial / blocked), token or time burn risk, follow-up,
   preventive change to encode later (a memory file or a skill note).

Bad pattern: retrying the same action three times with different wording. Good pattern: capture, classify, one direct check, change
the plan only if the check supports it.

### Incident write-up for live problems (merged: /debug report + agent self-debug report + think decision record)
After a live incident is fixed and watched, leave a short write-up in the project doc so the next change report and the next debugger
have it:
```
Incident: <one line, plain words>          Window: <first bad run> to <fix verified>
Impact: <count per company/copy, from the red query; who was affected>
Root cause: <origin step + the hypothesis that proved it>     Second cause checked: <yes, what>
Fix: <source change>   Cleanup: <one-time fix for affected records, count done>   Undo: <tested command>
Evidence: <execution/call ids, query before/after counts>   Labels: verified end to end / inferred
Prevention: <seam or monitor added, memory lesson file>
```

### Instrumentation hygiene [diagnosing-bugs, systematic-debugging]
- Debugger before logs; targeted boundary logs before broad ones; one variable per probe.
- Unique tag per session (`[DEBUG-xxxx]`); untagged logs survive, tagged ones die.
- Never leave instrumentation in a live workflow; adding a probe node to an n8n, voice or CRM workflow is itself a change.


**Eval lessons (super-skill vs earlier picks, 20 graded runs):**
- Close silent fallbacks on the bug path in the same change: when the fix touches a lookup with a default (time zone, mapping,
  config), make the unknown case fail loudly or get flagged, unless the user asked for the one-line fix only. Causes outside the
  path go on their own card (the eval run fixed the casing but left unmapped states silently on Pacific time).
- Capture the original reproduction output (for example `node run.js` before the fix) in the evidence, not only the new tests.
- If writing a report file is refused, put the full findings in the final reply; never route around the refusal.

## When members disagree

| Between | Issue | Rule |
|---|---|---|
| systematic-debugging vs diagnosing-bugs | "Form a single hypothesis" vs "3-5 ranked hypotheses" | Generate 3-5 ranked (anti-anchoring), then test them one at a time with one variable per probe. Both satisfied. |
| /debug vs diagnosing-bugs / TDD | Add the regression test after the fix vs before | Before the fix, red first, at a correct seam; if no seam exists, document that instead of writing a false-confidence test. |
| diagnosing-bugs vs ops reality | "No loop, no hypothesis" vs incidents that already happened on a live system | A read-only replay or red query over captured real data counts as the loop. If even that is impossible, stop and ask the user for an id or screenshot. Never create a live test event (call, text, write) to reproduce without the user's OK. |
| diagnosing-bugs vs the user's approval protocol | "Show hypotheses, don't block" vs "approve before changing" | Hypotheses are a non-blocking FYI; any fix to a live system blocks on the user's pick. |
| agent-introspection vs the user "operate autonomously" | "Escalate to a human" vs "don't ask permission" | Diagnosis, reads and local reversible steps: autonomous. Live writes/sends, high-risk or externally blocked failures, or 3 strikes: escalate. |
| systematic-debugging vs diagnosing-bugs | "Log at every component boundary" vs "never log everything and grep" | Boundary probes are targeted: one tagged entry/exit probe per boundary, run once to locate the layer, then removed. |
| systematic-debugging defense-in-depth vs the user's source-fix rule | Add validation at every layer vs fix only at the origin | Default to the source fix + one-time cleanup. An extra guard elsewhere is its own review card with a reason. |
| agent-introspection vs debug-lab scope | Agent failures vs code bugs | Agent-failure loop only when the agent run itself is failing; code and system bugs use the main workflow. |

## Combine with
- `superpowers:systematic-debugging` (always on): the iron law plus its technique files (`root-cause-tracing.md`, `defense-in-depth.md`,
  `condition-based-waiting.md`, `find-polluter.sh` for test pollution) in the superpowers plugin's `skills/systematic-debugging/`.
- `/debug` slash command: the short interactive version; its report format is step 10.
- `superpowers:test-driven-development` for the red-first regression test; `superpowers:verification-before-completion` before "fixed".
- `think-and-decide` (Think mode) for postmortems; `plan-and-execute` for multi-step fixes and the architecture scan; `test-and-harden`
  after the fix; Playwright MCP for browser-side loops.
- Specialist prompts (file = Agent prompt; give them the loop command and the ranked hypotheses, not the whole transcript):
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/debugger.md`: a second pair of eyes on a stubborn root cause.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/error-detective.md`: correlating errors across services and logs.
  - `~/.claude/skill-library/agents/voltagent/04-quality-security/performance-engineer.md`: perf baselines, profiling, bottlenecks.
  - `~/.claude/skill-library/agents/voltagent/03-infrastructure/incident-responder.md`: an active outage that needs coordinated recovery.
  - `~/.claude/skill-library/agents/voltagent/09-meta-orchestration/error-coordinator.md`: recurring failure and cascade patterns across runs.
  - `~/.claude/skill-library/agents/voltagent/03-infrastructure/sre-engineer.md`: monitoring and alerting so it can't recur silently.

## House rules
- Before any fix: prove the problem with real data for every company and copy, game out the fix system-wide, replay it, then present
  evidence, impact list, risks and undo; after applying, watch the first real runs.
- Never report an error from a code or one system's log alone: confirm the real outcome in the destination system, label each finding
  verified or inferred, and say "unconfirmed" when you can't read the destination.
- Fix at the source with the smallest change plus a one-time cleanup; explain it in 2-3 plain steps with yes/no questions.
- Live-system fixes go on a review page and the user runs the apply.
- No test calls or texts outside a sandbox, systems of record stay read-only, and secrets are never printed.
- Paid APIs and anything that sends, publishes, posts, buys or calls a live system ask the user first.

## Members

| Member | Best at | Path |
|---|---|---|
| diagnosing-bugs | Feedback-loop-first discipline: 10 loop types, tightening, red-capable gate, minimisation, ranked falsifiable hypotheses, tagged probes, perf branch, correct-seam regression tests, cleanup checklist, HITL script | `members/diagnosing-bugs/SKILL.md`, `members/diagnosing-bugs/scripts/hitl-loop.template.sh` |
| agent-introspection-debugging | When the agent itself fails: capture template, failure-pattern table, contained recovery, recovery heuristics, self-debug report | `members/agent-introspection-debugging/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
