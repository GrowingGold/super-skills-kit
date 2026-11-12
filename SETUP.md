# SETUP: steps for Claude to follow

The user said something like "set this up for me". Follow these steps in order. The user is a beginner on a Mac, so keep explanations short and plain.

1. **Check the tools.** Run `git --version` and `python3 --version`.
   - If git is missing on macOS, tell the user to run `xcode-select --install`, wait for it to finish, then continue.
   - If python3 is missing, same command (it ships with the same tools).
2. **Dry run.** From this folder run `python3 install.py`. It changes nothing and prints the plan.
3. **Explain the plan** in 3-5 plain lines (what gets downloaded, that their settings and CLAUDE.md are backed up first, that existing hooks stay, that it is fully undoable) and ask the user to say "go".
4. **Install.** After they say go, run `python3 install.py --apply`. The download takes a few minutes. Some repositories may fail; that is fine, the report lists them and the super-skills still work.
5. **Verify.**
   - `python3 -c "import json,os;d=json.load(open(os.path.expanduser('~/.claude/super-skills-kit/index.json')));print(len(d['entries']))"` should print 29.
   - `grep -c skill_router ~/.claude/settings.json` should print 1 or more.
   - `grep -c "super-skills-kit:start" ~/.claude/CLAUDE.md` should print 1.
6. **Finish.** Tell the user to restart Claude Code (close it and open it again), then try a message like "make me a landing page for my bakery". At the top of the reply they should see an `Optimized: ...` line naming the skills used.

## Optional: superpowers plugin
The kit works best with the official `superpowers` plugin (brainstorming, planning, debugging). Ask the user before installing it. If they agree, run `/plugin install superpowers@claude-plugins-official` (or `claude plugin install superpowers@claude-plugins-official`).

## Update
In this folder run `git pull`, then `python3 install.py --apply` again. It is safe to repeat.

## Undo
Run `python3 install.py --undo`, then restart Claude Code. It removes only what the installer added (the hook, the settings it added, the CLAUDE.md block and the folders it created). Backups of the original files stay in `~/.claude/backups/`.

## If something goes wrong
- "settings.json is not valid JSON": the installer stopped without changing anything. Ask the user to fix or rename that file, then run it again.
- A repository failed to download: re-run `python3 install.py --apply` later (usually a network blip).
