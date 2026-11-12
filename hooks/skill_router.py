#!/usr/bin/env python3
"""Per-message skill router (UserPromptSubmit hook).
On every real message it adds a short entry-optimizer reminder, an entry-tier hint (reply / task / build / spec)
and up to 5 matching super-skills from ~/.claude/super-skills-kit/index.json (built by build_index.py).
Local only: no network, no prompt text stored. Never blocks the prompt. Skips empty messages and `!` shell entries."""
import json, os, re, sys

INDEX = os.path.join(os.path.expanduser('~'), '.claude', 'super-skills-kit', 'index.json')
STOP = set('''this that with from have what your will would could should about into they them then than there their make made just like want need
also more most some such only very much many when where which while were been being does done doing able please thanks thank okay good great
something anything everything know think going keep sure here same other each every over under after before again
time times today day days week new use using get set run add show tell give look see let can how why who all any our the and for you yes not but one two now via its out
check fix change update did dont cant still skill skills best practices tools tool expert official overview guidelines basics advanced when user users
etc including include includes per used ask asks asked'''.split())
OPT = ("Entry optimizer (full: ~/.claude/skill-library/planning/entry-optimizer/SKILL.md): tier, optimize, load matching super-skills, act. "
       "Reply line 1: `Optimized: <task, max 20 words> · Skills: <super-skill (mode)> or none`.")
BUILD = re.compile(r'\b(build|create|design|redesign|launch|make (me |a |an |the )|new (app|site|page|feature|workflow|agent|brand)|set up|implement|from scratch)\b')
SPEC = re.compile(r'\b(spec|requirements|prd|feature list|user stories)\b')
MOBILE = re.compile(r' (expo|ios|android|eas|testflight|react native|swiftui|iphone|ipad|mobile apps?|app store|play store|apk) ')
LOCAL = re.compile(r' (local|gbp|google business|business profile|map pack|maps|near me|citations?|nap|service.area|lsa|local services|geogrid|multi.location|locations|google reviews|yelp|apple business|bing places) ')
SEO_CUE = re.compile(r' (rank|ranks|ranking|rankings|seo|serp|google search|search console|organic traffic) ')
RESEARCH_CUE = re.compile(r' (reddit|forums?|what people say|people are saying|reviews online|market research|research) ')
GATES = {'mobile-app-studio': MOBILE, 'local-seo': LOCAL}      # only when the message has that cue
BOOSTS = {'seo-suite': (SEO_CUE, 6), 'research-hub': (RESEARCH_CUE, 6)}
GENERIC = set('best practices patterns pattern feel better expert official overview guidelines creator builder development system pro'.split())
SUPER_BONUS = 2


def norm(w):
    """Crude stemmer: tests/testing/tested -> test, planning -> plan."""
    if len(w) > 4 and w.endswith('s') and not w.endswith('ss'): w = w[:-1]
    if len(w) > 5 and w.endswith('ing'): w = w[:-3]
    elif len(w) > 4 and w.endswith('ed'): w = w[:-2]
    if len(w) > 3 and w[-1] == w[-2] and w[-1] not in 'aeioulsz': w = w[:-1]
    return w


def words(text):
    return {norm(w) for w in re.findall(r'[a-z0-9+#]{3,}', text.lower().replace('-', ' ')) if w not in STOP}


def route(prompt, idx):
    t = ' ' + re.sub(r'[^a-z0-9.+&#_ -]', ' ', prompt.lower()) + ' '
    t = re.sub(r' mobile[ -](first|friendly|responsive) ', ' responsive ', t)          # a layout word, not an app task
    if not MOBILE.search(t):
        t = re.sub(r' (on|for) mobile ', ' responsive ', t)
        t = re.sub(r' mobile (users|visitors|traffic|view|layout|version|web|site|page|pages|screen|screens|device|devices|checkout|conversion|conversions) ', r' responsive \1 ', t)
    ptoks = {w for w in re.findall(r'[a-z0-9+#]{3,}', t) if w not in STOP}
    pn = {norm(w) for w in ptoks}
    idf = idx.get('idf', {})
    best, sup = {}, {e['name']: e for e in idx['entries']}

    def sc(ws, wt):
        return sum(wt * idf.get(w, 1) for w in ws)

    for e in idx['entries']:
        nm = words(e['name']); mem = {norm(w) for m in e['members'] for w in m.split('-') if len(w) > 3 and w not in GENERIC}
        rest = words(e['desc'])
        mn = pn & nm; mm = (pn & mem) - mn; mr = (pn & rest) - mn - mm
        s = sc(mn, 4) + sc(mm, 1.5) + sc(mr, 1) if (mn or mm or mr) else 0
        hit_members = []; seen = set(mn | mm | mr); named = bool(mn or mm)
        for m in e['installed']:
            mname = words(m['name']); mdesc = words(m['desc'])
            a = pn & mname; b = (pn & mdesc) - a
            ms = 0.8 * (sc(a, 2.5) + sc(b, 1))
            if ms > 0:
                hit_members.append((ms, m['name'])); seen |= a | b; named = named or bool(a)
        hit_members.sort(reverse=True)
        top_m = hit_members[0][0] if hit_members else 0
        s = max(s, top_m + (1 if len(hit_members) > 1 else 0))      # a member hit counts for its super-skill
        s += min(3, max(0, len(hit_members) - 1))                    # several members hit = strong signal the group fits
        if s > 0 and (len(seen) >= 2 or named):                       # one weak description word alone is not enough
            best[e['name']] = [s + SUPER_BONUS, [m for _, m in hit_members[:4]]]
    for nm, g in GATES.items():
        if nm in best and not g.search(t): del best[nm]
    for nm, (rx, add) in BOOSTS.items():
        if nm in sup and rx.search(t) and not (nm == 'seo-suite' and LOCAL.search(t)):
            b = best.setdefault(nm, [0, []]); b[0] = max(b[0], 7) + add
    broad = len(pn) > 25 and len(best) > 8                      # a pasted log or long status touches everything
    floor = 12 if broad else min(9, 3 + 2.5 * (len([w for w in pn if w in idf]) - 1))      # short messages have fewer words to match
    ranked = sorted(((v[0], k, v[1]) for k, v in best.items() if v[0] >= floor), reverse=True)
    picks = []
    top = ranked[0][0] if ranked else 0
    for s, k, ms in ranked:
        if s < 0.7 * top: continue
        picks.append((k, ms, round(s, 1)))
        if len(picks) == 5: break
    return picks, sup


def main():
    try: inp = json.load(sys.stdin)
    except Exception: return
    prompt = inp.get('prompt') or ''
    if not prompt.strip() or prompt.lstrip().startswith('!'): return
    if '<task-notification>' in prompt or 'SYSTEM NOTIFICATION' in prompt: return      # background events are not user entries
    lines = [OPT]
    if len(prompt.split()) >= 3:                                                         # keyword routing is meaningless on "yes" / "go"
        picks, sup = [], {}
        try:
            idx = json.load(open(INDEX))
            picks, sup = route(prompt, idx)
        except Exception:
            picks = []
        low = ' ' + prompt.lower() + ' '
        tier = 'spec' if (len(prompt.split()) > 150 or SPEC.search(low)) else 'build' if BUILD.search(low) else 'task'
        lines.append({'build': 'Entry tier: build -> run superpowers:brainstorming before building (live changes: change protocol + visual approval page).',
                      'spec': 'Entry tier: spec -> EARS pass from the entry-optimizer before planning.',
                      'task': 'Entry tier: task.'}[tier])
        if picks:
            lines.append('Skills for this entry. Load before acting, then the skill-fit brainstorm:')
            for k, ms, _ in picks:
                e = sup[k]
                extra = f"; matched members: {', '.join(ms)}" if ms else ''
                lines.append(f"- {k} [super-skill{extra}]: {first(e['desc'])} -> {e['path']}")
            lines.append('Use picks that fit; installs and paid or live-system tools ask the user first.')
        lines.append('No fitting pick? Full super-skill index: ~/.claude/skill-library/SUPER-SKILLS.md')
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'UserPromptSubmit', 'additionalContext': '\n'.join(lines)}}))


def first(desc, n=70):
    s = re.split(r'(?<=[.!?])\s', desc.strip(), 1)[0]
    s = re.sub(r'^(Use (this )?(skill )?(for|when)\s+)', '', s, flags=re.I)
    return s[:n]


try: main()
except Exception: pass     # never break the user's prompt
