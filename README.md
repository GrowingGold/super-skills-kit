# Super-Skills Kit

A ready-made setup for Claude Code that makes it noticeably better at real work.

## What you get
- **29 super-skills.** Each one bundles many specialist skills for an area: marketing, web design, React, databases, debugging, mobile apps, research, planning and more.
- **An automatic skill picker.** On every message, a small local script suggests the super-skills that fit, so Claude loads the right know-how without you asking.
- **A prompt optimizer.** Claude restates your request as a clear goal before acting, and tells you which skills it is using.
- **Token-saving rules.** Defaults that keep Claude fast and cheap (smaller helper models, short answers, one phase per session).
- **Visual approval pages.** For bigger changes, Claude shows a review page with before and after, and you pick what goes ahead.

## Start in 3 steps
1. Accept the GitHub invite and make sure you are signed in to GitHub.
2. Open Claude Code and paste:
   `Clone https://github.com/GrowingGold/super-skills-kit into ~/super-skills-kit, then follow its SETUP.md`
3. When Claude is done, close Claude Code and open it again.

## What it changes on your computer
- Adds a hook to `~/.claude/settings.json` (your own hooks stay), plus three settings only if you do not already have them.
- Adds one marked block to `~/.claude/CLAUDE.md` (your own text stays).
- Creates folders under `~/.claude/` (skill-library, skill-sources, super-skills-kit, hooks).
- Before touching anything it saves your original files to `~/.claude/backups/`.
- Nothing is sent anywhere. The picker runs on your machine only.

## Undo
In `~/super-skills-kit` run `python3 install.py --undo`, then restart Claude Code.

## Update
In `~/super-skills-kit` run `git pull`, then `python3 install.py --apply`.

## Credits
The skills inside the super-skills come from many open projects, downloaded from their authors at install time. See [CREDITS.md](CREDITS.md).
