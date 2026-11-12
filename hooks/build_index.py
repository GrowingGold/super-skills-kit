#!/usr/bin/env python3
"""Build the super-skill index used by skill_router.py.
Reads ~/.claude/skill-library/<area>/<super-skill>/SKILL.md (and the member SKILL.md files that are installed),
writes ~/.claude/super-skills-kit/index.json and ~/.claude/skill-library/SUPER-SKILLS.md.
Usage: python3 build_index.py [--home DIR] [--kit KIT_DIR]   (--kit limits the index to super-skills shipped in KIT_DIR/skills)"""
import json, math, os, re, sys

STOP = set('''this that with from have what your will would could should about into they them then than there their make made just like want need
also more most some such only very much many when where which while were been being does done doing able please thanks thank okay good great
something anything everything know think going keep sure here same other each every over under after before again
time times today day days week new use using get set run add show tell give look see let can how why who all any our the and for you yes not but one two now via its out
check fix change update did dont cant still skill skills best practices tools tool expert official overview guidelines basics advanced when user users
etc including include includes via per use used ask asks asked'''.split())


def norm(w):
    """Crude stemmer: tests/testing/tested -> test, planning -> plan."""
    if len(w) > 4 and w.endswith('s') and not w.endswith('ss'): w = w[:-1]
    if len(w) > 5 and w.endswith('ing'): w = w[:-3]
    elif len(w) > 4 and w.endswith('ed'): w = w[:-2]
    if len(w) > 3 and w[-1] == w[-2] and w[-1] not in 'aeioulsz': w = w[:-1]
    return w


def toks(text):
    return {norm(w) for w in re.findall(r'[a-z0-9+#]{3,}', text.lower().replace('-', ' ')) if w not in STOP}


def frontmatter(path):
    try:
        text = open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return None
    m = re.match(r'---\s*\n(.*?)\n---', text, re.S)
    if not m: return {}
    out, key, buf = {}, None, []
    for line in m.group(1).split('\n'):
        k = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
        if k and not line.startswith(' '):
            if key: out[key] = ' '.join(buf).strip()
            key, v = k.group(1), k.group(2).strip()
            buf = [] if v in ('>', '|', '>-', '|-') else [v]
        elif key:
            buf.append(line.strip())
    if key: out[key] = ' '.join(buf).strip()
    for k in out:
        v = out[k]
        if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'': out[k] = v[1:-1]
    return out


def parse_members(fm, text_path):
    raw = fm.get('members', '')
    if raw.startswith('['): raw = raw[1:-1]
    names = [x.strip().strip('\'"') for x in raw.replace('- ', ',').split(',') if x.strip().strip('\'"')]
    if not names:
        try:
            names = sorted(os.listdir(os.path.join(os.path.dirname(text_path), 'members')))
        except OSError:
            names = []
    return names


def first_sentence(desc, n=110):
    s = re.split(r'(?<=[.!?])\s', desc.strip(), 1)[0]
    s = re.sub(r'^(Use (this )?(skill )?(for|when)\s+)', '', s, flags=re.I)
    return (s[:n - 1].rstrip() + '…') if len(s) > n else s


def main(argv):
    home = os.path.expanduser('~')
    kit = None
    if '--home' in argv: home = argv[argv.index('--home') + 1]
    if '--kit' in argv: kit = argv[argv.index('--kit') + 1]
    lib = os.path.join(home, '.claude', 'skill-library')
    shipped = None
    if kit:
        shipped = set()
        for a in os.listdir(os.path.join(kit, 'skills')):
            ad = os.path.join(kit, 'skills', a)
            if os.path.isdir(ad): shipped.update((a, s) for s in os.listdir(ad) if os.path.isdir(os.path.join(ad, s)))
    supers = []
    for area in sorted(os.listdir(lib)) if os.path.isdir(lib) else []:
        ad = os.path.join(lib, area)
        if not os.path.isdir(ad): continue
        for name in sorted(os.listdir(ad)):
            sp = os.path.join(ad, name, 'SKILL.md')
            if not os.path.isfile(sp): continue
            if shipped is not None and (area, name) not in shipped: continue
            fm = frontmatter(sp) or {}
            if shipped is None and 'members' not in fm: continue
            supers.append((area, name, sp, fm))
    entries = []
    for area, name, sp, fm in supers:
        members = parse_members(fm, sp)
        installed = []
        for m in members:
            mp = os.path.join(os.path.dirname(sp), 'members', m, 'SKILL.md')
            if os.path.isfile(mp):
                mf = frontmatter(mp) or {}
                installed.append({'name': m, 'desc': (mf.get('description') or '')[:400]})
        entries.append({'name': name, 'area': area, 'desc': fm.get('description', ''), 'members': members,
                        'installed': installed, 'path': f'~/.claude/skill-library/{area}/{name}/SKILL.md'})
    docs = []
    for e in entries:
        docs.append(toks(e['name'] + ' ' + e['desc'] + ' ' + ' '.join(e['members'])))
        docs.extend(toks(m['name'] + ' ' + m['desc']) for m in e['installed'])
    n = max(1, len(docs)); df = {}
    for d in docs:
        for w in d: df[w] = df.get(w, 0) + 1
    idf = {w: round(1 + math.log(n / c), 2) for w, c in df.items()}
    os.makedirs(os.path.join(home, '.claude', 'super-skills-kit'), exist_ok=True)
    with open(os.path.join(home, '.claude', 'super-skills-kit', 'index.json'), 'w') as f:
        json.dump({'version': 1, 'entries': entries, 'idf': idf}, f)
    rows = ['# Super-skills', '',
            'Each super-skill merges its member skills. Load the super-skill first; open members only through its mode table.',
            'Protocol: `~/.claude/skill-library/planning/entry-optimizer/SKILL.md`.', '',
            '| Super-skill | Area dir | Members | Use for | Path |', '|---|---|---|---|---|']
    for e in sorted(entries, key=lambda x: x['name']):
        rows.append(f"| {e['name']} | {e['area']} | {len(e['members'])} | {first_sentence(e['desc']).replace('|', '/')} | `{e['path']}` |")
    with open(os.path.join(lib, 'SUPER-SKILLS.md'), 'w') as f:
        f.write('\n'.join(rows) + '\n')
    print(f'index: {len(entries)} super-skills')


if __name__ == '__main__':
    main(sys.argv[1:])
