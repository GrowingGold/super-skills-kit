# Super-Skills Kit

**Make Claude Code faster, cheaper and better at real work, with one paste.**

Free setup for Claude Code on a Mac: 29 expert skill bundles, an automatic skill picker, prompt optimizer, token-saving defaults and review pages that let you approve changes before they happen. It backs up your settings first and has a one-command undo.

**Before:** you type "make my site faster", Claude guesses, loads nothing special and burns tokens.
**After:** Claude restates it as a clear task, loads the web-performance and SEO skills on its own, uses small helper models for lookups, and shows you a review page before changing anything big.

To install, paste this into Claude Code:

`Clone https://github.com/GrowingGold/super-skills-kit into ~/super-skills-kit, then follow its SETUP.md`

## What you get
- **29 super-skills.** Each one bundles many specialist skills for an area: marketing, web design, React, databases, debugging, mobile apps, research, planning and more.
- **An automatic skill picker.** On every message, a small local script suggests the super-skills that fit, so Claude loads the right know-how without you asking.
- **A prompt optimizer.** Claude restates your request as a clear goal before acting, and tells you which skills it is using.
- **Token-saving rules.** Defaults that keep Claude fast and cheap (smaller helper models, short answers, one phase per session).
- **Visual approval pages.** For bigger changes, Claude shows a review page with before and after, and you pick what goes ahead.

## Start in 3 steps
1. Install Claude Code on a Mac (no GitHub account needed; the repo is public).
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
Made by Ben.

The kit's own files are MIT licensed ([LICENSE](LICENSE)). The third-party skills are not included in this repo; the installer downloads them from their authors, and each keeps its own license.

The skills inside the super-skills come from many open projects, downloaded from their authors at install time. See [CREDITS.md](CREDITS.md).
