---
name: git-github-pro
description: Git and GitHub end to end. Git - status, commits, branches, sync, push, rebase, squash, fixup, amend, cherry-pick, merge conflicts, stash, worktrees, bisect, reflog recovery and undo, git hooks, .gitignore, big files and LFS. GitHub through the gh CLI and API - pull requests (create, review, checks, merge, update branch), issues, Actions runs, failing CI logs, reruns, releases and tags, repos, secrets, GraphQL, pagination, bulk or scripted operations, rate limits, auth and token errors, dependabot. Changelogs, release notes and announcements from commits or merged PRs (CHANGELOG.md, GitHub releases, app store what's-new, in-app note, launch post, weekly update), and docs drift after a change (README, CLI or API docs). Use for any git or gh command, "push this", "open a PR", "PR description", "reply to review comments", "what changed since", "undo that commit", "which commit broke it", a rejected push, release notes, or "update the docs", even when git is not named.
members: [git-advanced, github-ops, changelog-generator, github-pr-workflow, doc-maintenance, release-announcement]
---

# Git + GitHub Pro

Unifies git-advanced (local git craft), github-ops (gh CLI and API), github-pr-workflow (reviewable PRs), changelog-generator and
release-announcement (release notes per channel) and doc-maintenance (docs that match behavior) into one safe change loop.
Load this first; pick the mode; open a member reference only when the route names it. Everything here is written for Claude's
non-interactive shell: no editors, no TTY prompts.

## Pick the mode

| Task looks like | Mode | Do / open |
|---|---|---|
| Save or sync work: status, commit, push, pull, new branch | **Daily loop** | Unified workflow 1-7 |
| Clean history: squash, fixup, reword, split, drop, reorder, cherry-pick | **History surgery** | Core rules: Safety guards, then Non-interactive history edits |
| Undo or rescue: bad reset, lost commit, deleted branch, botched rebase, old version of a file | **Recovery** | Core rules: Recovery |
| "Which commit broke it?" | **Bisect** | Core rules: Bisect; root cause with `superpowers:systematic-debugging` (or the debug-lab super-skill) |
| Two branches at once, parallel agents | **Worktrees** | Core rules: Worktrees; `superpowers:using-git-worktrees`; Agent tool `isolation: "worktree"` |
| Merge or rebase conflicts | **Conflicts** | Core rules: Conflicts |
| Git hooks (pre-commit, commit-msg, pre-push) | **Git hooks** | Core rules: Git hooks. Claude Code hooks are a different thing: `update-config` |
| Pull request: create, view, review, checks, merge, update branch, reply to review comments | **PR** | Workflow 8; Core rules: PRs; `members/github-pr-workflow/SKILL.md`; deep: `members/github-ops/references/pr_operations.md`; review: `code-review` skill or the user-typed `/review-pr <n>` |
| Issues: create, label, triage, search, close | **Issues** | `members/github-ops/references/issue_operations.md`; the user-typed `/fix-issue <n>` |
| GitHub Actions: failing run, logs, rerun, artifacts, manual dispatch | **CI** | Core rules: CI; deep: `members/github-ops/references/workflow_operations.md` |
| `gh api`, GraphQL, bulk or scripted operations, GitHub Enterprise | **API and bulk** | Core rules: gh CLI and API; deep: `members/github-ops/references/api_reference.md`, `best_practices.md` |
| Changelog, release notes, "what changed since X", app store text, weekly update, launch post, in-app note | **Release notes** | Workflow 9 + Core rules: Changelog; channel templates `members/release-announcement/SKILL.md` (skip its Paperclip Cases block); sample output `members/changelog-generator/SKILL.md`; wording pass `humanizer` |
| Behavior changed and docs may now be wrong: README, CLI flags, API, config keys, env vars, examples | **Docs drift** | Core rules: Docs drift; `members/doc-maintenance/SKILL.md` |
| Batch of dependabot PRs | **Dependabot** | the user-typed `/merge-dependabot <owner/repo>` |
| Push rejected, "Invalid username or token", 403 | **Auth** | House rules: token workaround |
| Create or delete a repo, visibility, secrets, branch protection | **Repo admin** | Ask the user first; Core rules: CI (secrets) |

## Unified workflow: the safe change loop

1. **Orient (read-only).** `git status -sb`, `git branch --show-current`, `git remote -v`, `git log --oneline -10`, `git stash list`.
   For GitHub work also `gh auth status` and `gh repo view --json nameWithOwner,defaultBranchRef`. Classify the repo: the user's synced repo,
   another the user repo, or someone else's. Done when you know branch, remote, default branch, dirty state and repo class [git-advanced aliases `st`, `lg`].
2. **Sync.** `git fetch --prune`; on synced repos `git pull --rebase` at session start [cross-machine-sync]. Dirty tree first:
   `git stash push -u -m "<why>"` or a WIP commit.
3. **Branch.** On the default branch, anything other than a synced-repo WIP save gets its own branch from fresh upstream:
   `git switch -c <type>/<short-desc> origin/<default>`. Parallel work: a worktree, not stash juggling [git-advanced worktrees].
4. **Stage deliberately.** Read `git diff`; stage by path (`git add <paths>`, never a blind `git add .`); read `git diff --staged`
   [git-advanced anti-patterns]. Then run the pre-commit checks in Core rules: Commit hygiene (secrets, env files, big files).
5. **Commit.** One logical change per commit, Conventional Commits header, body says why, message passed with `-m` or `-F <file>`
   (heredoc for multi-line), ending with the attribution lines the session's system reminder gives [git-advanced commit-msg pattern].
6. **Tidy before sharing.** Unpushed only: fold fixes in with fixup + autosquash (Core rules: Non-interactive history edits). Commits
   someone may have pulled are never rewritten; undo them with `git revert` [git-advanced anti-patterns].
7. **Push.** `git push -u origin <branch>`. After rebasing your own unshared branch: `git push --force-with-lease --force-if-includes`.
   Auth failure: House rules. Done when `git status -sb` shows no ahead/behind and `git ls-remote origin <branch>` matches `git rev-parse HEAD`.
8. **PR.** `gh pr create --base <default> --title "<conventional title>" --body-file <file>`; body = What / Why / How tested / Risks +
   `Closes #N` + attribution footer [github-ops PR best practices]. `gh pr checks <n> --watch`; review with the `code-review` skill (or
   `/review-pr` when the user types it); handle feedback with `superpowers:receiving-code-review`. Merge only on the user's ask:
   `gh pr merge <n> --squash --delete-branch` (or `--auto` to merge once checks pass); then `git switch <default> && git pull && git branch -d <branch>`
   [superpowers:finishing-a-development-branch].
9. **Release (when asked).** Last tag `git describe --tags --abbrev=0`; collect commits and merged PR titles since then; write notes per
   Core rules: Changelog, and run the docs drift pass for every user-visible change; the user reviews the draft; then `git tag -a vX.Y.Z -m "vX.Y.Z"`, `git push origin vX.Y.Z`,
   `gh release create vX.Y.Z --title "vX.Y.Z" --notes-file notes.md` (asks the user). Semver from the commit types: breaking = major, feat = minor, fix = patch
   [changelog-generator + conventional commits].
10. **Verify end to end.** The remote has the commit, CI is green (`gh pr checks`), the release page shows the notes (`gh release view vX.Y.Z`).
    Report the link, not just "pushed".

Copy for any change that leaves the machine:
```
Ship a change:
- [ ] Oriented: branch, remote, default branch, dirty state, repo class
- [ ] Own branch from fresh origin/<default> (or synced-repo WIP save)
- [ ] Staged by path; staged diff read; secret / env / big-file checks clean
- [ ] Tests or lint pass locally
- [ ] Conventional commit with attribution lines
- [ ] Pushed; remote tip matches HEAD
- [ ] PR body What / Why / How tested / Risks; checks green
- [ ] Merged on the user's ask; local branch cleaned up
```

## Core rules and checklists

### Commit hygiene
- Header `type(scope)!: subject`, max 72 chars, imperative ("add", not "added"). Types: feat, fix, perf, refactor, docs, test, build, ci, chore, style, revert. `!` or a `BREAKING CHANGE:` footer marks breaking changes.
- Body: why the change, what it affects; wrap around 72 chars. Reference issues (`Closes #12`).
- Before committing, check the staged set:
  - secrets, file names only: `git diff --staged --name-only | xargs grep -lE '(sk-[A-Za-z0-9]|ghp_|github_pat_|xox[bp]-|AKIA[0-9A-Z]{12}|-----BEGIN [A-Z ]*PRIVATE KEY|(api[_-]?key|secret|password|token)["'"'"' ]*[:=])' 2>/dev/null`
  - env and key files: `git diff --staged --name-only | grep -E '(^|/)\.env|\.pem$|\.key$|credentials'`
  - big files: `git diff --staged --stat`; GitHub rejects files over 100 MB and warns over 50 MB; big binaries go to LFS or `.gitignore`.
- `.gitignore` covers build output (`dist/`, `.next/`), dependencies (`node_modules/`), `.env*`, keys, OS junk [git-advanced].
- A secret that was already committed is leaked: the user rotates it; rewriting history (`git filter-repo`) comes second and only with the user.

### Safety guards (before anything destructive)
Destructive = `reset --hard`, `rebase`, `push --force*`, `branch -D`, `clean -fd`, `restore`/`checkout -- <path>`, `stash drop|clear`, `filter-repo`.
- Backup ref first, it costs nothing: `git branch backup/$(date +%Y%m%d-%H%M)-<what>`; also note `git reflog -5` [git-advanced: reflog before destructive ops].
- Uncommitted work at risk: stash (`-u`) or WIP-commit it first. Throwing away uncommitted work the user made needs the user's OK.
- `--force-with-lease --force-if-includes`, never bare `--force`; never force the default branch or a branch others push to [git-advanced].
- Dry run first where one exists: `git clean -fdn` before `-fd`, `git push --dry-run` before a risky push.

### Non-interactive history edits
Claude's shell has no editor: `git rebase -i`, `git add -i/-p` and bare `git commit` hang or fail. Use these instead.

| Goal | Command |
|---|---|
| Fix the last commit (unpushed) | `git commit --amend --no-edit` (content) or `git commit --amend -m "<msg>"` (message) |
| Fold a fix into an older commit | `git commit --fixup=<sha>`, then `git rebase --autosquash <base>` (Git 2.44+; older: `GIT_SEQUENCE_EDITOR=: git rebase -i --autosquash <base>`) |
| Squash the last N | `git reset --soft HEAD~N && git commit -m "<msg>"` |
| Squash the whole branch | `git reset --soft $(git merge-base HEAD origin/<default>) && git commit -m "<msg>"` |
| Reword or edit an older commit | `S=$(git rev-parse --short <sha>); GIT_SEQUENCE_EDITOR="sed -i.bak 's/^pick $S /edit $S /'" git rebase -i <sha>^` (the sed edits the todo list, so no editor opens), then `git commit --amend -m "<msg>"` (or change files and `git commit --amend --no-edit`), then `GIT_EDITOR=true git rebase --continue` |
| Split an older commit | same `edit` stop, then `git reset HEAD^`, add and commit in parts, `GIT_EDITOR=true git rebase --continue` |
| Drop a commit | `git rebase --onto <sha>^ <sha>` |
| Move recent commits to a new branch | `git branch <new>` then, on the old branch, `git reset --hard <base>` (backup ref first) |
| Copy one commit | `git cherry-pick -x <sha>` |
| Update your branch with the default | own unshared branch: `git fetch && git rebase origin/<default>`; shared branch: `git merge origin/<default> --no-edit` |
| Partial staging | `git diff <file> > p.patch`, edit the patch, `git apply --cached p.patch` |
| Bail out | `git rebase --abort`, `git cherry-pick --abort`, `git merge --abort` |

Other editor traps: `git merge --no-edit`, `GIT_EDITOR=true git rebase --continue`, `git tag -a <t> -m "<msg>"`, `git revert --no-edit <sha>`.

### Recovery [git-advanced]
- Undo the last commit, keep changes staged: `git reset --soft HEAD~1`; keep them unstaged: `git reset HEAD~1`.
- Anything lost after reset, rebase or amend: `git reflog` (or `git log -g --oneline`), then `git branch rescue <sha>`; only then move branches.
- Undo a rebase: find the pre-rebase entry in `git reflog`, backup ref, `git reset --hard HEAD@{N}`.
- Deleted branch: find its tip in the reflog, `git switch -c <name> <sha>`.
- Dangling commits or a dropped stash: `git fsck --lost-found` / `git fsck --unreachable | grep commit`, then `git show <sha>`.
- One file from an older commit: `git restore --source=<sha> -- <path>`.
- Undo a pushed commit: `git revert --no-edit <sha>` (a merge commit: add `-m 1`).

### Conflicts
- List: `git diff --name-only --diff-filter=U` [git-advanced alias `conflicts`]. Context: `git log --merge --oneline -- <file>`, then read both sides.
- Resolve by intent: keep both changes when both matter; take one side (`git checkout --ours|--theirs <file>`) only when one clearly wins.
  During a rebase "ours" is the branch you are rebasing onto, "theirs" is your commit.
- After resolving: run the tests, `git add <file>`, `GIT_EDITOR=true git rebase --continue` or `git commit --no-edit`.
- The same conflict keeps coming back: suggest `git config rerere.enabled true` for that repo.

### Bisect [git-advanced]
- `git bisect start <bad> <good>`, then `git bisect run <cmd>`: exit 0 = good, 1-124 = bad, 125 = skip (cannot test). Read "first bad commit", then `git bisect reset`.
- Make the test a tiny script that reproduces only the bug, so the loop is fast and its verdict is unambiguous. Manual fallback: `git bisect good|bad`.

### Worktrees [git-advanced]
- `git worktree add ../<repo>-<branch> -b <branch> origin/<default>`; `git worktree list`; `git worktree remove <path>` after merging; `git worktree prune` for stale entries.
- One branch per worktree. Dependencies are not shared: install them in the new folder. Use for parallel agents or a hotfix during feature work instead of stashing.

### Git hooks [git-advanced]
- pre-commit: lint only staged files (`git diff --cached --name-only --diff-filter=d`) and fail on errors. In JS repos prefer lint-staged; the member's `eslint --fix` then `git add $FILES` re-stages whole files and sweeps in unstaged hunks.
- commit-msg: `^(feat|fix|perf|refactor|docs|test|build|ci|chore|style|revert)(\(.+\))?!?: .{1,72}$` on the first line (the member's regex lacked perf, build, ci, revert and `!`).
- pre-push: run the tests; `exit 1` blocks the push.
- `.git/hooks` is not versioned: share hooks via `git config core.hooksPath .githooks` on a tracked folder. `--no-verify` only on the user's ask.

### gh CLI and API [github-ops]
- Target explicitly: pass `--repo <owner/name>` whenever you are not inside the target repo, and on forks (canonical = remote `upstream` if it exists, else `origin`).
- Machine output: `--json <fields> --jq '<expr>'`, asking only for the fields you need (`gh pr view 12 --json number,title,state,reviews`); `--template` for text.
- Pagination: `--limit 200` on list commands (`gh pr list` has no `--page` flag, so the member's page loop does not work); REST `gh api --paginate 'repos/{owner}/{repo}/pulls?state=all'`; GraphQL `gh api graphql --paginate -f query='...'` with `$endCursor`.
- `{owner}` and `{repo}` placeholders fill in automatically inside a repo. Fields: `-f key=value` (string), `-F key=value` (number, bool, `@file`); `--method PATCH|POST|DELETE`.
- Debug: `GH_DEBUG=api gh ...`. Rate limit: `gh api rate_limit --jq .resources.core`.
- Retries: only 5xx and secondary rate limits, exponential backoff (1, 2, 4, 8 s, max 5 tries); a 4xx means fix the request.
- Bulk operations: list first as a dry run (`--json number,title`), show the user the list, then loop over it. No interactive `read` prompts (no TTY).
- Enterprise: `gh auth login --hostname <host>`, or `GH_HOST=<host>` per command.

### PRs [github-ops]
- One feature or fix per PR; conventional-style title; body with what, why, how tested, risks, `Closes #N`; reviewers who know the code.
- Test locally with `gh pr checkout <n>`; read `gh pr diff <n>`; watch `gh pr checks <n> --watch`.
- Review explicitly: `gh pr review <n> --approve`, or `--request-changes -b "<specific points>"`; follow up on your own feedback.
- Suggest (ask the user) for active repos: PR template, CODEOWNERS, branch protection requiring checks, `--auto` merge for trusted changes.
- Write `@name` in PR or issue text only for a real login the user wants notified; it pings that person.
- Open only when the change is functionally complete; before opening, rebase on (or merge) the fresh base, squash WIP into reviewable
  commits, remove debug prints, commented-out code and untracked TODOs, and run tests, typecheck and lint, noting any skip [github-pr-workflow].
- Title: imperative, under 70 characters, no trailing period, the user-visible change first ("Allow CSV export from reports table",
  not "Update reports.tsx"); follow the repo's prefix convention if it has one [github-pr-workflow].
- Evidence in the body: exact commands run; for UI, screenshots of the golden path and one edge case (light and dark if both exist);
  for migrations, the dry-run plan and the reversal steps; for performance, a before/after measurement, not adjectives. Green CI is
  necessary, not sufficient. Don't mix a refactor and a behavior change without separating them in the body [github-pr-workflow].
- Review replies: answer every comment, even "fixed in <sha>"; push fixes as new commits while review is active (amend or force-push
  only if the reviewer agrees, and say so); disagree in one sentence and let the reviewer decide; re-request review after pushing; one
  commit per round of feedback, never an "address feedback" commit full of unrelated edits [github-pr-workflow].
- Before merge: required checks green, every comment resolved, title and body still match the final scope, linked issue moved, branch
  deleted unless long-lived [github-pr-workflow].
- Body template (write it to a file, pass `--body-file`):
  ```
  ## What
  <one paragraph: the change>
  ## Why
  <the problem, linked issue>
  ## Implementation notes
  <anything non-obvious: trade-offs, rejected alternatives, migration or config impact>
  ## How tested
  - <command or steps> -> <result>; screenshots for UI
  ## Risks and rollback
  <what could break, how to undo>  (skip only for typo or docs-only PRs)

  Closes #<n>

  <attribution footer from the session's system reminder>
  ```

### CI (GitHub Actions) [github-ops]
- Failing run: `gh run list --branch <b> --limit 5`, then `gh run view <id> --log-failed`; jobs: `gh run view <id> --json jobs`.
- Read the failing step's log before touching code. A flake gets one rerun (`gh run rerun <id> --failed`); a second failure is real.
- Watch: `gh run watch <id> --exit-status`; artifacts: `gh run download <id>`; manual run: `gh workflow run <file> --ref <branch> -f key=value`.
- Secrets go in through stdin, never as a command-line argument or echo: `printf %s "$VALUE" | gh secret set NAME` (value read from your env or .env in the same shell, never printed).

### Common errors

| Message | Cause | Fix |
|---|---|---|
| `! [rejected] ... (fetch first)` / non-fast-forward | The remote has commits you do not | `git pull --rebase`, then push; never force a shared branch |
| `src refspec <b> does not match any` | No commit yet, or a wrong branch name | `git branch --show-current`; commit first |
| `Your local changes ... would be overwritten` | Dirty tree before checkout, pull or merge | Commit or `git stash push -u`, then retry |
| `You are in 'detached HEAD' state` | A sha or tag is checked out | Keep work: `git switch -c <name>`; leave: `git switch <branch>` |
| `refusing to merge unrelated histories` | Two separate repo inits, or the wrong remote | Check `git remote -v` first; `--allow-unrelated-histories` only when intended |
| `Invalid username or token` / 401 on push | Bad `GITHUB_TOKEN` in the environment | House rules: token workaround |
| `could not read Username ... terminal prompts disabled` | No credential helper in a non-interactive shell | `gh auth setup-git`, then retry (with `env -u GITHUB_TOKEN` if needed) |
| `gh api` 404 on a repo that exists | Private repo the token cannot see, or a wrong owner/name | `gh auth status`; check `--repo` |
| `Resource not accessible by integration` (403) | The token or app lacks that permission | Different auth, or ask the user for the scope |
| `File ... exceeds GitHub's file size limit of 100.00 MB` | A big file in the pushed commits | Last commit: `git rm --cached <file>`, amend, add to `.gitignore` or LFS; older commits: history rewrite, with the user |
| `hook ... failed` / pre-commit errors | A repo hook check failed | Fix what it reports; `--no-verify` only on the user's ask |
| `CONFLICT (content)` | Overlapping edits | Core rules: Conflicts |

### Changelog and release notes [changelog-generator]
- Range: since the last tag (`git log <tag>..HEAD --no-merges --pretty='%h %s'`), by date (`--since=2026-11-01`), or merged PRs
  (`gh pr list --state merged --search "merged:>=2026-11-01" --json number,title,labels,mergedAt`). PR titles often read better than commits.
- Sort by type: feat -> New; perf and user-visible refactor -> Improved; fix -> Fixed; security fixes -> Security; `!`/breaking -> Breaking
  (first, with what users must do). docs, test, chore, ci, build, style and internal refactors stay out of customer notes (keep them in internal notes).
- Rewrite each kept line for users: the benefit first, what they can do now, no file names, hashes or jargon ("Files sync about 2x faster",
  not "optimize sync worker pool"). Merge related commits into one line; quote numbers only when measured. Examples:
  - `feat(ws): add team workspaces` -> "New: Team workspaces. Invite people and keep each project separate."
  - `fix(upload): handle >10MB images in multipart` -> "Fixed: Large photos now upload reliably."
  - `refactor(db): tune pool size` -> left out (internal), unless users feel it, then "Improved: Pages load faster."
- Formats:
  - CHANGELOG.md in Keep a Changelog style: `## [Unreleased]` on top, then `## [1.4.0] - 2026-11-10` with Added / Changed / Fixed / Removed / Security.
  - GitHub release: `--notes-file`; `--generate-notes` output is raw input to rewrite, not the final text.
  - App store "what's new": short, top 2-3 changes; check the store's current length limit.
  - Weekly product update: a headline plus 3-5 bullets.
- The project's own style file (e.g. CHANGELOG_STYLE.md) or existing CHANGELOG beats these defaults; emoji headings only if the project already uses them.
- Output is a draft for the user; publishing a release, store text, email or post asks the user first.

### Announcements by channel [release-announcement]
- Pick the audience first; one release often needs several write-ups, never one blended text. Existing power users: changelog or
  in-app note (terse, links). Developers on your API: release notes or dev blog (examples, migration, version pins). Prospects: landing
  page or marketing post (problem -> solution, proof; copy-and-content owns the copy). Broad audience: social post or newsletter (one-line
  pitch and a link). Internal team: Slack or Discord (what changed, who to ping if it breaks).
- Every channel leads with three things: what changed (in the user's words), who it affects, what to do (migrate now, opt in, nothing).
- Templates: release notes = changelog plus a migration section with before/after code, a compatibility table, known issues and
  workarounds, thanks; dev blog 300-800 words = hook paragraph, 3-5 new things each with one example, upgrade paragraph, one line on
  what's next (no promised dates); in-app note = one sentence and one link; social = one sentence, one link, one image or clip, no
  thread-bait.
- Writing: "You can now export to CSV" beats "We've added CSV export"; numbers beat adjectives and cite how they were measured; date
  every post; `**Breaking:**` prefix repeated in every channel; no "we are excited to announce"; nothing announced before it ships.
- After publishing (the user's yes): changelog in source control, post date equals ship date, every link works, breaking changes also in the
  upgrade guide, the internal team told before the public post.

### Docs drift [doc-maintenance]
- Anchor the pass to behavior: a commit range (since the last tag or a named PR), then list every user-visible change: CLI flags, API
  shapes, defaults, config keys, endpoints, env vars, supported versions. No behavior change, no docs pass; "improve the docs" is a
  separate planned project.
- For each change find every page that mentions it (README, CLI, API and config references, migration guide, FAQ, examples) and edit
  only the lines that must change; don't rewrap untouched paragraphs, it buries the real edits in the diff.
- New flag, env var or endpoint gets its reference entry, not just a changelog line. Re-run every code example that touches the change;
  examples go stale fastest. Search for the old wording and fix stragglers.
- Drift signs: documents something that no longer exists, an example that doesn't run, a default that differs from the code, a wrong
  supported-versions list, a "coming soon" that shipped or was cancelled. Fix it in the same pass and list it under Fixed.
- Style: second person, present tense, language tag on code blocks, link the first mention per page, never document unreleased behavior
  (mark it experimental or leave it out). Commit message says what changed and why.

## When members disagree

1. **Interactive rebase.** git-advanced cleans history with `git rebase -i`; Claude's shell cannot drive an editor.
   **Rule:** the non-interactive recipes above (sequence-editor `sed`, autosquash, soft reset).
2. **PR title prefix.** github-ops requires `NOJIRA:` / `GR-1234:` (another company's Jira gate). **Rule:** drop it; conventional-style titles;
   a ticket reference only where the repo already uses one.
3. **Pagination and bulk confirm.** github-ops loops over `gh pr list --page` and asks with interactive `read`. **Rule:** `--limit` or
   `gh api --paginate`; confirmation happens in chat after a dry-run list.
4. **Auto-fix in pre-commit.** git-advanced re-adds whole files after `eslint --fix`. **Rule:** a hook that only checks and fails, or lint-staged, so partial staging survives.
5. **Rebase versus "never rebase pushed commits".** **Rule:** rebase your own unshared branch, including your own PR branch (then
   `--force-with-lease`); merge the default branch into branches other people push to.
6. **Write straight to CHANGELOG.md** (changelog-generator tips) versus "review before publishing" (same member). **Rule:** write the draft,
   the user reviews, then tag and release.
7. **Emoji section headings** in the changelog example. **Rule:** the project's existing style wins; default is plain headings.
8. **the user's sync rule versus "commit or push only when asked; branch first on the default branch".** **Rule:** on synced repos
   (cross-machine-sync list) the user's standing instruction is the ask: pull at start, WIP commit and push at session end, announced in one line,
   never forced. Everywhere else commit when asked; push, PR and merge only when asked.
9. **Trail of Bits commands** (`/review-pr`, `/fix-issue`, `/merge-dependabot`) say "do not stop or ask" and push or merge. **Rule:** the user
   typing the command is the ask for that PR, issue or repo. Their Exa research step uses WebSearch unless the user OKs Exa (paid), and
   `/review-pr` needs the installed-off pr-review-toolkit plugin enabled for the project first (`/powerup enable`).
10. **PR title style.** github-ops says conventional-style titles; github-pr-workflow says plain imperative, user-visible change first.
    **Rule:** the repo's existing convention wins; with none, conventional type prefix plus a user-visible imperative subject under 70
    characters (`feat: allow CSV export from reports table`).
11. **Release notes vs announcements.** changelog-generator and release-announcement both write release text. **Rule:** the changelog
    is the source of truth (Keep a Changelog sections, plus Deprecated and Breaking when needed); channel write-ups are built from it.
    release-announcement's Paperclip Cases block only applies inside Paperclip; skip it.
12. **Docs PR flow.** doc-maintenance (repo version) opens its own branch and PR per pass. **Rule:** docs edits ride in the same
    change or a follow-up commit; branches, pushes and PRs only when the user asks (sync rule aside).

## Combine with

- Superpowers: `superpowers:using-git-worktrees`, `superpowers:finishing-a-development-branch`, `superpowers:requesting-code-review`,
  `superpowers:receiving-code-review`, `superpowers:verification-before-completion`, `superpowers:systematic-debugging` (with bisect).
- Built-in skills: `code-review` (diff or PR review; `--comment` posts inline, which asks the user), `security-review` (pending branch changes), `humanizer` (release note wording).
- Slash commands the user types: `/review-pr <n>`, `/fix-issue <n>`, `/merge-dependabot <repo>`, `/deep-review` (staged changes), `/deploy-check`.
- Installed-off plugins: `commit-commands`, `pr-review-toolkit` (`/powerup enable <id>`, then /reload-plugins).
- Super-skills: debug-lab (root cause after bisect), test-and-harden (failing tests in CI), copy-and-content or docs-decks (customer announcements built from release notes).
- Agent prompts (Read, pass as the Agent prompt), under `~/.claude/skill-library/agents/voltagent/`:
  `06-developer-experience/git-workflow-manager.md` (branching strategy, messy history), `04-quality-security/code-reviewer.md` (PR review),
  `06-developer-experience/dependency-manager.md` (dependabot and upgrades), `03-infrastructure/deployment-engineer.md` (Actions pipelines),
  `08-business-product/technical-writer.md` (polished release notes).

## House rules

- **Token workaround.** If push or gh fails with "Invalid username or token", a stale `GITHUB_TOKEN` in the environment is often the cause: rerun
  with `env -u GITHUB_TOKEN git push` / `env -u GITHUB_TOKEN gh ...` so the gh keyring login is used. Run
  `gh auth status` first; the lasting fix is the user's (re-login or replace the token).
- **GitHub is the source of truth** for projects across machines: pull at session start, commit and
  push at session end on synced repos (WIP commits are fine).
- **Never in git:** API keys, env files, credential files, large source assets, `node_modules`/`dist`. Never print a token; secret scans report file names, not values.
- **Ask the user first:** push, PR or merge, pushing tags or releases, repo create, delete or visibility changes, branch
  protection, secrets, force-pushes, rewriting pushed history, and anything posted to other people's repos.
- **Attribution:** commit messages and PR bodies end with the lines from the session's system reminder.
- **Token-light output:** `--json` + `--jq`, `git log --oneline -n <N>`; RTK already compresses git output.

## Members

| Member | Best at | Path |
|---|---|---|
| git-advanced | Local git craft: worktrees, bisect (incl. `bisect run`), rebase operations, hook scripts, reflog/fsck recovery, aliases, anti-patterns checklist | `members/git-advanced/SKILL.md` |
| github-ops | gh CLI and REST/GraphQL API depth: PRs, issues, Actions, output formats, retries, enterprise; 2,100 lines of references | `members/github-ops/SKILL.md` + `members/github-ops/references/pr_operations.md`, `issue_operations.md`, `workflow_operations.md`, `api_reference.md`, `best_practices.md` |
| changelog-generator | Turning commits into customer-friendly notes: categories, noise filter, user language, example output, use cases | `members/changelog-generator/SKILL.md` |
| github-pr-workflow | A PR a reviewer can land without questions: pre-open hygiene, title rules, evidence per change type, review replies, merge checklist, anti-patterns | `members/github-pr-workflow/SKILL.md` |
| release-announcement | Release write-ups per channel: audience table, what/who/what-to-do lead, templates for notes, blog, in-app, social, post-publish checklist | `members/release-announcement/SKILL.md` |
| doc-maintenance | Minimum-churn docs drift pass anchored to a commit range: map changes to pages, edit only changed lines, drift signs, style baseline | `members/doc-maintenance/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
