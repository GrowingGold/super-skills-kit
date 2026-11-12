#!/usr/bin/env python3
"""Super-Skills Kit installer. Python 3 standard library only (works with the macOS system python3).

  python3 install.py            show what would change (a dry run, nothing is touched)
  python3 install.py --apply    install (safe to run again)
  python3 install.py --undo     remove everything this installer added

Options: --home DIR (use another home folder, for tests), --only owner_repo,owner_repo (fetch only those repos, for tests).
"""
import datetime, hashlib, json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

KIT = os.path.dirname(os.path.abspath(__file__))
START, END = '<!-- super-skills-kit:start -->', '<!-- super-skills-kit:end -->'
ENV_KEYS = {'CLAUDE_CODE_SUBAGENT_MODEL': 'sonnet', 'DISABLE_TELEMETRY': '1', 'DO_NOT_TRACK': '1'}
FALLBACK_BLOCK = f"""{START}
## Super-Skills Kit
- On every message a hook suggests matching super-skills. Load the ones that fit before acting:
  `~/.claude/skill-library/SUPER-SKILLS.md` lists all of them.
- Protocols (entry optimizer, token diet, visual approval, change protocol): `~/.claude/super-skills-kit/protocols/`.
- Ask before any send, call, publish, purchase or delete on a live system.
{END}
"""


def say(msg=''):
    print(msg, flush=True)


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest() if os.path.isfile(path) else None


def run(cmd, cwd=None, timeout=900):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env, timeout=timeout)
    return r.returncode, (r.stdout + r.stderr).strip()


class Kit:
    def __init__(self, home, only):
        self.home = os.path.abspath(home)
        self.cd = os.path.join(self.home, '.claude')
        self.settings = os.path.join(self.cd, 'settings.json')
        self.claude_md = os.path.join(self.cd, 'CLAUDE.md')
        self.lib = os.path.join(self.cd, 'skill-library')
        self.srcdir = os.path.join(self.cd, 'skill-sources')
        self.kitdir = os.path.join(self.cd, 'super-skills-kit')
        self.hooks = os.path.join(self.cd, 'hooks')
        self.manifest_path = os.path.join(self.kitdir, 'manifest.json')
        self.sources = json.load(open(os.path.join(KIT, 'sources.json')))
        self.only = set(only) if only else None
        self.manifest = json.load(open(self.manifest_path)) if os.path.isfile(self.manifest_path) else None

    # ---------- helpers ----------
    def repo_dir(self, url):
        owner, repo = url.rstrip('/').split('/')[-2:]
        return f'{owner}_{repo}'

    def repos(self):
        out = {}
        for s in self.sources:
            if s['status'] != 'ok': continue
            d = self.repo_dir(s['repo_url'])
            if self.only and d not in self.only: continue
            r = out.setdefault(d, {'url': s['repo_url'], 'commit': s['commit'], 'paths': set()})
            r['paths'].add(s['path'])
        return out

    def supers(self):
        out = []
        sk = os.path.join(KIT, 'skills')
        for area in sorted(os.listdir(sk)) if os.path.isdir(sk) else []:
            ad = os.path.join(sk, area)
            for name in sorted(os.listdir(ad)) if os.path.isdir(ad) else []:
                if os.path.isfile(os.path.join(ad, name, 'SKILL.md')): out.append((area, name))
        return out

    def read_settings(self):
        if not os.path.isfile(self.settings): return {}
        try:
            data = json.load(open(self.settings))
            if not isinstance(data, dict): raise ValueError('not an object')
            return data
        except Exception as e:
            say(f'STOP: {self.settings} is not valid JSON ({e}).')
            say('Nothing was changed. Fix or rename that file, then run this again.')
            sys.exit(2)

    def block_text(self):
        p = os.path.join(KIT, 'templates', 'claude-md-block.md')
        text = open(p).read().strip() if os.path.isfile(p) else FALLBACK_BLOCK.strip()
        if START not in text: text = f'{START}\n{text}\n{END}'
        return text + '\n'

    # ---------- plan ----------
    def plan(self):
        self.read_settings()
        repos, supers = self.repos(), self.supers()
        n_members = sum(1 for s in self.sources if s['status'] == 'ok' and (not self.only or self.repo_dir(s['repo_url']) in self.only))
        say('Super-Skills Kit: here is what --apply would do (nothing is changed yet).')
        say()
        say(f'1. Check that git and python3 are installed.')
        say(f'2. Back up ~/.claude/settings.json and ~/.claude/CLAUDE.md to ~/.claude/backups/super-skills-kit-{datetime.date.today()}/.')
        say(f'3. Download {len(repos)} public skill repositories from their authors into ~/.claude/skill-sources/ '
            f'(only the {n_members} skill folders needed, pinned to a fixed version).')
        say(f'4. Install {len(supers)} super-skills into ~/.claude/skill-library/ and link their member skills to the downloads.')
        say('5. Copy the kit rules (protocols) to ~/.claude/super-skills-kit/protocols/ and the skill picker to ~/.claude/hooks/.')
        say('6. Build the skill index (~/.claude/super-skills-kit/index.json and ~/.claude/skill-library/SUPER-SKILLS.md).')
        say('7. Add one UserPromptSubmit hook to ~/.claude/settings.json (your existing hooks stay).')
        say('8. Add these settings only if you do not have them: ' + ', '.join(f'{k}={v}' for k, v in ENV_KEYS.items()) + ', outputStyle=Concise.')
        say('9. Add a marked block to ~/.claude/CLAUDE.md (your own text stays untouched).')
        say()
        say('Undo any time with: python3 install.py --undo')
        say('To go ahead: python3 install.py --apply')

    # ---------- apply ----------
    def mkdirs(self, path):
        todo = []
        p = path
        while not os.path.isdir(p):
            todo.append(p); p = os.path.dirname(p)
        for d in reversed(todo):
            os.mkdir(d); self.m['created_dirs'].append(d)

    def backup(self, path, key):
        rel = os.path.relpath(path, self.cd)
        dest = os.path.join(self.m['backup_dir'], rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(path, dest)
        self.m['backups'][key] = dest

    def apply(self):
        for tool, hint in (('git', 'Run: xcode-select --install   (then run this again)'),
                           ('python3', 'Install Python 3 from https://www.python.org/downloads/ or run: xcode-select --install')):
            if not shutil.which(tool):
                say(f'STOP: {tool} is not installed. {hint}'); sys.exit(1)
        settings = self.read_settings()
        first = self.manifest is None
        self.m = self.manifest or {'created_dirs': [], 'backups': {}, 'replaced': {}, 'super_dirs': [], 'hook_files': [],
                                  'env_added': [], 'outputStyle_added': False, 'settings_existed': os.path.isfile(self.settings),
                                  'claude_md_existed': os.path.isfile(self.claude_md), 'hook_cmd': None,
                                  'hooks_key_created': False, 'ups_key_created': False, 'date': str(datetime.date.today())}
        m = self.m
        m['backup_dir'] = m.get('backup_dir') or os.path.join(self.cd, 'backups', f'super-skills-kit-{datetime.date.today()}')
        self.mkdirs(self.cd); self.mkdirs(self.kitdir)
        # 2. back up
        if first:
            for p, k in ((self.settings, 'settings'), (self.claude_md, 'claude_md')):
                if os.path.isfile(p): self.backup(p, k)
            say(f'Backed up your files to {m["backup_dir"]}' if m['backups'] else 'No existing settings or CLAUDE.md to back up.')
        self.save()
        # 3. fetch repos
        repos = self.repos()
        say(f'Downloading {len(repos)} skill repositories (this can take a few minutes)...')
        self.mkdirs(self.srcdir)
        failed = {}

        def job(item):
            d, r = item
            ok, msg = self.fetch(d, r)
            return d, ok, msg
        with ThreadPoolExecutor(4) as ex:
            for d, ok, msg in ex.map(job, sorted(repos.items())):
                say(f'  {"ok  " if ok else "FAIL"} {d}' + ('' if ok else f'  ({msg[:120]})'))
                if not ok: failed[d] = msg
        # 4. super-skills + links
        installed, linked, skipped = 0, 0, []
        for area, name in self.supers():
            dest = os.path.join(self.lib, area, name)
            if os.path.lexists(dest) and [area, name] not in m['super_dirs']:
                skipped.append(f'{area}/{name} (you already have a skill folder with that name; left alone)'); continue
            self.mkdirs(os.path.join(self.lib, area))
            if os.path.lexists(dest): shutil.rmtree(dest)
            shutil.copytree(os.path.join(KIT, 'skills', area, name), dest, symlinks=True)
            if [area, name] not in m['super_dirs']: m['super_dirs'].append([area, name])
            installed += 1
            for s in self.sources:
                if s['super'] != name or s['status'] != 'ok': continue
                rd = self.repo_dir(s['repo_url'])
                if rd in failed or (self.only and rd not in self.only): continue
                target = os.path.join(self.srcdir, rd, s['path'])
                link = os.path.join(dest, 'members', s['member'])
                if os.path.lexists(link) or not os.path.isdir(target): continue   # kit ships its own folder, or not downloaded
                os.makedirs(os.path.dirname(link), exist_ok=True)
                os.symlink(target, link); linked += 1
        say(f'Installed {installed} super-skills, linked {linked} member skills.')
        for s in skipped: say('  skipped: ' + s)
        # 5. protocols + hooks
        pd = os.path.join(KIT, 'protocols')
        if os.path.isdir(pd):
            shutil.copytree(pd, os.path.join(self.kitdir, 'protocols'), dirs_exist_ok=True)
        else:
            say('  note: no protocols/ folder in the kit yet; skipped.')
        self.mkdirs(self.hooks)
        for fn in ('skill_router.py', 'build_index.py'):
            dst = os.path.join(self.hooks, fn)
            if os.path.isfile(dst) and fn not in m['hook_files'] and fn not in m['replaced'] and sha(dst) != sha(os.path.join(KIT, 'hooks', fn)):
                self.backup(dst, 'hooks/' + fn); m['replaced'][fn] = dst
            shutil.copy2(os.path.join(KIT, 'hooks', fn), dst)
            if fn not in m['hook_files']: m['hook_files'].append(fn)
        # 6. index
        sd = os.path.join(self.lib, 'SUPER-SKILLS.md')
        if os.path.isfile(sd) and 'SUPER-SKILLS.md' not in m['replaced'] and not m.get('index_written'):
            self.backup(sd, 'SUPER-SKILLS.md'); m['replaced']['SUPER-SKILLS.md'] = sd
        self.mkdirs(self.lib)
        code, out = run([sys.executable, os.path.join(self.hooks, 'build_index.py'), '--home', self.home, '--kit', KIT])
        say('Index: ' + out.splitlines()[-1] if out else 'Index built.')
        m['index_written'] = True
        # 5-8 settings
        cmd = f'python3 {self.home}/.claude/hooks/skill_router.py'
        m['hook_cmd'] = cmd
        if 'hooks' not in settings or not isinstance(settings.get('hooks'), dict):
            settings['hooks'] = {}; m['hooks_key_created'] = m['hooks_key_created'] or first
        ups = settings['hooks'].get('UserPromptSubmit')
        if ups is None:
            ups = settings['hooks']['UserPromptSubmit'] = []; m['ups_key_created'] = m['ups_key_created'] or first
        have = any(h.get('command') == cmd for e in ups if isinstance(e, dict) for h in e.get('hooks', []) if isinstance(h, dict))
        if not have: ups.append({'hooks': [{'type': 'command', 'command': cmd}]})
        if not isinstance(settings.get('env'), dict):
            settings['env'] = {}; m['env_key_created'] = m.get('env_key_created') or first
        env = settings['env']
        for k, v in ENV_KEYS.items():
            if k not in env:
                env[k] = v
                if k not in m['env_added']: m['env_added'].append(k)
        if not settings.get('outputStyle'):
            settings['outputStyle'] = 'Concise'; m['outputStyle_added'] = True
        with open(self.settings, 'w') as f:
            json.dump(settings, f, indent=2); f.write('\n')
        m['settings_sha'] = sha(self.settings)
        # 9. CLAUDE.md
        block = self.block_text()
        text = open(self.claude_md).read() if os.path.isfile(self.claude_md) else ''
        if START in text and END in text:
            a, b = text.index(START), text.index(END) + len(END)
            text = text[:a] + block.rstrip('\n') + text[b:]
        else:
            text = text + ('' if not text or text.endswith('\n') else '\n') + ('\n' if text else '') + block
        with open(self.claude_md, 'w') as f: f.write(text)
        m['claude_md_sha'] = sha(self.claude_md)
        self.save()
        say()
        if failed:
            say(f'{len(failed)} repositories could not be downloaded (their member skills show as not installed; the super-skills still work):')
            for d, msg in failed.items(): say(f'  - {d}')
        say('Done. Everything this installer created is listed in ~/.claude/super-skills-kit/manifest.json.')
        say('Restart Claude Code to finish.')

    def save(self):
        os.makedirs(self.kitdir, exist_ok=True)
        json.dump(self.m, open(self.manifest_path, 'w'), indent=1)

    def fetch(self, d, r):
        dest = os.path.join(self.srcdir, d)
        paths = sorted(r['paths'])
        try:
            if os.path.isdir(os.path.join(dest, '.git')):
                c, head = run(['git', 'rev-parse', 'HEAD'], cwd=dest)
                if c == 0 and head == r['commit'] and all(os.path.isdir(os.path.join(dest, p)) for p in paths): return True, 'already there'
            os.makedirs(dest, exist_ok=True)
            if not os.path.isdir(os.path.join(dest, '.git')):
                run(['git', 'init', '-q'], cwd=dest)
            c, _ = run(['git', 'remote', 'get-url', 'origin'], cwd=dest)
            run(['git', 'remote', 'set-url' if c == 0 else 'add', 'origin', r['url']], cwd=dest)
            pats = ['/' + p.strip('/') + '/' if p else '/*' for p in paths]
            c, out = run(['git', 'sparse-checkout', 'set', '--no-cone'] + pats, cwd=dest)
            if c: return False, out
            c, out = run(['git', 'fetch', '-q', '--depth', '1', '--filter=blob:none', 'origin', r['commit']], cwd=dest)
            if c: return False, out
            c, out = run(['git', '-c', 'advice.detachedHead=false', 'checkout', '-q', '-f', 'FETCH_HEAD'], cwd=dest)
            if c: return False, out
            missing = [p for p in paths if not os.path.isdir(os.path.join(dest, p))]
            return (True, '') if not missing else (False, f'{len(missing)} folders missing, e.g. {missing[0]}')
        except Exception as e:
            return False, str(e)

    # ---------- undo ----------
    def undo(self):
        m = self.manifest
        if not m:
            say('Nothing to undo: no manifest found at ' + self.manifest_path); return
        self.read_settings()
        # settings.json
        if os.path.isfile(self.settings):
            if sha(self.settings) == m.get('settings_sha') and m['backups'].get('settings') and os.path.isfile(m['backups']['settings']):
                shutil.copyfile(m['backups']['settings'], self.settings)
            else:
                s = self.read_settings()
                hooks = s.get('hooks', {}) if isinstance(s.get('hooks'), dict) else {}
                ups = hooks.get('UserPromptSubmit', [])
                for e in list(ups):
                    if isinstance(e, dict):
                        e['hooks'] = [h for h in e.get('hooks', []) if h.get('command') != m.get('hook_cmd')]
                        if not e['hooks']: ups.remove(e)
                if 'UserPromptSubmit' in hooks and not ups and m.get('ups_key_created'): del hooks['UserPromptSubmit']
                if 'hooks' in s and not hooks and m.get('hooks_key_created'): del s['hooks']
                for k in m['env_added']: s.get('env', {}).pop(k, None)
                if 'env' in s and not s['env'] and m.get('env_key_created'): del s['env']
                if m.get('outputStyle_added') and s.get('outputStyle') == 'Concise': del s['outputStyle']
                if not s and not m['settings_existed']: os.remove(self.settings)
                else: json.dump(s, open(self.settings, 'w'), indent=2); open(self.settings, 'a').write('\n')
            if not m['settings_existed'] and os.path.isfile(self.settings) and sha(self.settings) == m.get('settings_sha'):
                os.remove(self.settings)
        say('Removed the hook and settings this kit added.')
        # CLAUDE.md
        if os.path.isfile(self.claude_md):
            if sha(self.claude_md) == m.get('claude_md_sha') and m['backups'].get('claude_md'):
                shutil.copyfile(m['backups']['claude_md'], self.claude_md)
            else:
                t = open(self.claude_md).read()
                if START in t and END in t:
                    a, b = t.index(START), t.index(END) + len(END)
                    pre = t[:a].rstrip('\n'); post = t[b:].lstrip('\n')
                    t = pre + ('\n\n' if pre and post else '\n' if pre else '') + post
                    if not t.strip() and not m['claude_md_existed']: os.remove(self.claude_md)
                    else: open(self.claude_md, 'w').write(t)
            if not m['claude_md_existed'] and os.path.isfile(self.claude_md) and not open(self.claude_md).read().strip():
                os.remove(self.claude_md)
        say('Removed the kit block from CLAUDE.md.')
        # folders and files
        for area, name in m['super_dirs']:
            p = os.path.join(self.lib, area, name)
            if os.path.isdir(p) and not os.path.islink(p): shutil.rmtree(p)
        if os.path.isdir(self.srcdir): shutil.rmtree(self.srcdir)
        for fn in m['hook_files']:
            p = os.path.join(self.hooks, fn)
            if os.path.isfile(p): os.remove(p)
        sd = os.path.join(self.lib, 'SUPER-SKILLS.md')
        if os.path.isfile(sd): os.remove(sd)
        for key, dst in m['replaced'].items():       # put back files the kit had to replace
            src = m['backups'].get(key) or m['backups'].get('hooks/' + key)
            if src and os.path.isfile(src): os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst)
        if os.path.isdir(self.kitdir): shutil.rmtree(self.kitdir)
        for d in reversed(m['created_dirs']):
            if d.startswith(os.path.join(self.cd, 'backups')): continue
            try:
                if os.path.isdir(d) and not os.listdir(d): os.rmdir(d)
            except OSError: pass
        say('Removed the folders the kit created.')
        say(f'Your original files are still saved in {m["backup_dir"]} (delete it if you like).')
        say('Restart Claude Code to finish.')


def main(argv):
    if '-h' in argv or '--help' in argv:
        say(__doc__); return
    home = argv[argv.index('--home') + 1] if '--home' in argv else os.path.expanduser('~')
    only = argv[argv.index('--only') + 1].split(',') if '--only' in argv else None
    k = Kit(home, only)
    if '--undo' in argv: k.undo()
    elif '--apply' in argv: k.apply()
    else: k.plan()


if __name__ == '__main__':
    main(sys.argv[1:])
