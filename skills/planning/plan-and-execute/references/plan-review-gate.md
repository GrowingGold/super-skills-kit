# Plan review gate (merged: blueprint review checklist + anti-patterns + rationalizations, document-review, the user's change protocol)

Run this before any plan, spec or brainstorm doc is called ready. Two layers on purpose: the author self-checks, then a reviewer checks
independently; authors have blind spots, so don't drop either layer.

- **Short gate** (feature plan, chat plan): Part A + B1-B7.
- **Full gate** (blueprint, multi-session, parallel agents): Parts A-D. Pass Parts B-D inline to a strongest-tier subagent; it cannot
  read this folder.
- **Ops gate** (any live-system change): Parts A-E.

Log every finding in the plan's Review Log (critical / important / minor). Fix critical and important ones before approval.

## Part A: Read it like an editor [document-review]

Ask, noting issues before fixing anything:
1. What is unclear?
2. What is unnecessary?
3. What decision is being avoided?
4. What assumptions are unstated?
5. Where could scope quietly expand?

Score:
| Criterion | Pass when |
|---|---|
| Clarity | Problem stated plainly; no "probably", "consider", "try to" |
| Completeness | Required sections present, constraints stated, open questions flagged |
| Specificity | Concrete enough for the next step (brainstorm -> can plan; plan -> can implement) |
| YAGNI | No hypothetical features; simplest approach chosen |
| Intent fidelity | Reflects what the user actually said; your guesses are marked as guesses |

Then name the **one critical improvement**, if one stands out. Auto-fix wording and formatting; ask the user before restructuring, removing
sections or changing meaning. Don't add requirements nobody discussed, don't rewrite the whole thing, don't add metadata sections.
Simplify content that serves hypothetical needs or repeats itself; never simplify away constraints, edge cases, rejected-alternative
rationale or open questions. Two passes, then recommend stopping.

## Part B: Plan structure [blueprint review checklist]

1. **Completeness**: does the last step reach the goal, with no gap?
2. **Granularity**: each step one-PR sized (one review sitting, about 15 files or fewer, one sentence of intent).
3. **Dependencies**: parallel steps truly independent (no shared files, no consumed outputs); every consumed artifact has an edge.
4. **Cold start**: can an agent run Step N reading only its section + Design Decisions + Invariants (+ branch workflow)?
5. **Rollback**: concrete commands per step (`git revert HEAD`, migration down, restore from backup), or "point of no return" stated.
6. **Invariants**: would they catch the real regressions? Anything missing?
7. **Exit criteria**: each one checkable by running a command and comparing output. "Works" and "clean" fail.
8. **Branch workflow** (git plans only): branch naming, strongest-tier review before push, CI gate, merge method, and the user's "push only when asked".
9. **Risk**: riskiest steps named, with manual verification; main tree + explicit rollback preferred over worktrees for subagents.
10. **Rules compliance**: nothing contradicts the project CLAUDE.md, the user's global rules or house rules.
11. **Verification commands real**: they exist in package.json scripts, Makefile, CI config or the system's API.
12. **Self-consistency**: exit criteria don't contradict invariants; design decisions don't contradict each other.
13. **Cross-step refactors declared**: when a step restructures earlier code, its Context says which file, which block, what moves where.
14. **State snapshots**: if the structure evolves step by step (pipeline stages, exports, config entries), the expected state after key
    steps is written down.
15. **Spec link**: user stories and testing decisions from the spec each map to a step; test seams match what the user confirmed.

## Part C: Anti-pattern scan [blueprint anti-patterns]

| Anti-pattern | Fix |
|---|---|
| Mega-step (several logical changes in one) | Split to one intent per step |
| Implicit cross-step dependency (reads another step's output silently) | List produced/consumed artifacts; add the edge |
| Vague exit criteria ("ensure tests pass") | Exact command + expected output |
| Copy-paste verification (same `build && test` everywhere) | Verify what that step changed (endpoint answers, schema matches) |
| Strongest tier on every step | Reserve it for architecture, breaking-change risk, review, expensive-to-reverse steps |
| Plan as narrative prose | Imperative, verb-first Tasks |
| Missing rollback on irreversible actions | Rollback field, or "point of no return" |
| Hardcoded machine paths, branch names, package manager | Placeholders resolved in pre-flight (`{default-branch}`, `{package-manager}`) |
| Skipped review ("it's simple") | Run the gate; mark UNREVIEWED if no reviewer was available |
| Everything serial | Group independent steps into explicit parallel sets |
| Undeclared refactor of an earlier step's code | Describe it in the step's Context |

## Part D: Rationalizations to reject [blueprint]

| Thought | Why it's wrong |
|---|---|
| "Skip review, it's trivial" | The author judging triviality is the weakest review there is; trivial plans pass review fast anyway. |
| "I'll update the plan later" | A resuming agent reads the file, not your memory; a stale plan gets executed as written. |
| "One big PR is faster" | Faster to open, slower to review and debug, all-or-nothing to merge. |
| "No tests needed for a refactor" | A refactor's promise is unchanged behavior; tests are the only automated proof. |
| "The plan is obvious" | Obvious to you with full context; the executor starts cold with only the file. |
| "I'll plan as I go" | That's archaeology, not a plan: no dependency graph, no exit criteria, "done" defined by fatigue. |

## Part E: Ops change checks [the user's change protocol + double-check protocol]

Every live-system step (automation workflows, voice or CRM platforms, database writes/backfills, dashboards) must show, with evidence in the plan or chat:
1. **Proven problem**: real executions, rows, call ids or payloads, for every system and copy involved; the cause explains every case;
   a second cause was looked for.
2. **Root cause at the source**: the fix sits at the step where the problem starts, plus a one-time cleanup of people already affected,
   not safety nets spread across key workflows.
3. **Impact list**: every reader and writer of what changes: downstream nodes and their `$json` use (copies differ per company), DB
   triggers (e.g. `updated_at` stampers), other workflows, dashboards, daily checks and emails, other teams' claims.
4. **Replay**: the change run on recent real data, old vs new result per case.
5. **Exact diff + machine check** that nothing else differs; for SQL functions, run them end to end into temp copies of their target
   tables (compiling alone proves nothing).
6. **Sandbox / test contacts first**; never real customers.
7. **Failure modes**: what could go wrong and how it would show up.
8. **Tested undo**.
9. **Review card** with the user's pick; anything kept against a pick has its own card.
10. **Apply by the user**, then the first real runs watched end to end in the destination system and post-change checks scheduled.
11. **Record**: in-workflow change note, worklog/memory entry.
12. **One change per step**, finished and verified before the next starts.
