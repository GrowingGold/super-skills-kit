---
name: copy-and-content
description: Write, edit and plan marketing copy and content, then strip every AI tell. Use for page copy (homepage, landing, pricing, product, about, hero, headline, CTA, value prop, tagline, "write copy for", "this copy is weak"); editing (review, proofread, polish, tighten, copy sweep, too wordy, refresh outdated content, content audit); de-AI any text ("sounds like AI", "AI slop", "de-slop", "humanize", "make it sound human"); researched long-form (blog post, article, newsletter, case study, tutorial, outline, hook, citations); content strategy (what to write about, pillars, topic clusters, editorial calendar, repurposing); lead magnets (gated content, checklist, ebook, template, opt-in freebie, course as a skill); free tools (calculator, generator, grader); plain technical English for instructions, SOPs, plans and error text ("simplified English", "make it simpler"). Email/SMS flows go to lifecycle-messaging, ad copy at volume to ads-and-measurement.
members: [copywriting, copy-editing, content-strategy, lead-magnets, free-tools, content-research-writer, humanizer, simplified-english]
---

# Copy and Content

One skill for everything the user's brands put into words: page copy, edits, refreshes, researched long-form, content plans, lead
magnets and free tools. It merges five coreyhaines marketing skills with the user's personal humanizer (always-on) and content-research-writer.
Load this first, pick a mode, run the unified workflow, and end every deliverable with the de-AI pass (step 7). Open a member
file only when a row below sends you there.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| "Write copy for...", new page, hero, headline, CTA, value prop, tagline, product description | WRITE | Steps 0-8. Headline formulas, section types, page templates: `members/copywriting/references/copy-frameworks.md`. Transitions: `members/copywriting/references/natural-transitions.md` |
| "Fix this headline", "tighten paragraph two", "is this line OK?" | POINT EDIT | Step 1 (Situation C), then step 7 on the changed lines only. Point-edit checklist: `members/copy-editing/references/checklist.md` |
| "Edit / polish / review my copy", "too wordy", "sharpen this" | EDIT | Steps 0-2, then 6 (Seven Sweeps) and 7. Full sweep checklist: `members/copy-editing/references/checklist.md` |
| Page is stale, traffic dropping, stats 12+ months old | REFRESH | Gap grid and Keep/Revise/New outline: `members/copy-editing/references/content-refresh.md`, then EDIT |
| "Sounds like AI", "humanize", or any draft (yours included) before delivery | DE-AI PASS | Step 7. Merged catalog: `references/de-ai-pass.md` |
| Blog post, article, newsletter, case study, tutorial, thought leadership, anything needing sources | RESEARCHED LONG-FORM | Track L1-L8 below. Feedback and review templates: `members/content-research-writer/SKILL.md`. Report-grade evidence: Skill `deep-research` |
| "What should we write about", pillars, clusters, calendar, distribution | STRATEGY | Strategy track below. Flywheel, half-lives, atomization: `members/content-strategy/references/content-distribution.md`. CMS choice: `members/content-strategy/references/headless-cms.md` |
| "What can we give away for emails", gated PDF, checklist, template, mini-course, quiz | LEAD MAGNET | Offer track below. Per-format build guide: `members/lead-magnets/references/format-guide.md`. Benchmarks: `members/lead-magnets/references/benchmarks.md` |
| Package a course, podcast or archive as an installable agent skill | CONTENT-TO-SKILL | `members/lead-magnets/references/content-to-skill.md` (+ `content-to-skill-corpus-design.md`, `content-to-skill-release.md`) |
| Calculator, generator, grader, checker, "should we build a free tool" | FREE TOOL | Offer track below. Ideas by type and industry: `members/free-tools/references/tool-types.md`. Sourced cases: `members/free-tools/references/tool-benchmarks.md` |
| Plain-English word swaps | lookup | `members/copy-editing/references/plain-english-alternatives.md` |
| Instructions, SOPs, how-to steps, plans, status notes or error text that must be understood the first time (ops staff, non-native readers, other agents) | SIMPLE ENGLISH | Core rules: Simplified Technical English; `members/simplified-english/SKILL.md`; then step 7 |
| Email or SMS sequences, launch emails, text copy | hand off | super-skill `lifecycle-messaging` (run step 7 here on its drafts) |
| Ad copy, RSA headlines, hooks at volume | hand off | super-skill `ads-and-measurement` |
| Page layout, forms, popups, offers, pricing pages as a CRO problem, A/B tests | hand off | super-skill `conversion-lab` |
| Keyword research, technical SEO, AI-search citations, schema | hand off | super-skill `seo-suite` |
| Social posts, atomizing a flagship | hand off | super-skill `audience-growth` |

## Unified workflow

The spine for WRITE and EDIT. The three tracks after it reuse these steps.

### 0. Load context, ask only for gaps
Read `.agents/product-marketing.md` (or `.claude/product-marketing.md`) first, including its Learnings section: angles and
claims already tested there are not new ideas [copywriting]. For the user's brands, read the project's notes before writing.
Then fill only what is missing, in one round:
- Piece: type, and the ONE action the reader should take.
- Reader: who, the problem in their own words, objections, what they already know, where they arrive from (ad, search, email).
- Offer: what it is, how it differs from the alternatives, which proof exists (numbers, reviews, cases).
- Voice: formality, personality, a writing sample if one exists.
If there is enough to start, start, and list assumptions at the top of the draft instead of running a question round.

### 1. Diagnose the input and set your license
[copywriting, copy-editing]

| Situation | Signs | License |
|---|---|---|
| A. Blank or slop | One-line ask, or generic company-speak with no point of view | Build the argument from brief and facts. Free on angle, never on facts |
| B. Real voice | An angle, an opinion, recognizable words, rough execution | Restore it. Keep their argument, vocabulary, emphasis and scope |
| C. Point edit | "Fix this line", "tighten this paragraph" | Change only that, plus the minimum around it to make it fit |

State the diagnosis in one line with evidence before writing ("B: argues against agencies in the founder's voice, uses 'ship'
and 'stuff'"). In B and C, read taste out of the input: vocabulary is a voice choice ("stuff" stays "stuff"), where they spent
words is a priority choice, what they left out is a scope choice, their angle is the positioning (deepen it, don't replace it).
A writing sample beats the default voice: match its sentence length, punctuation, paragraph openings and a few of its words.

### 2. Build the claims ledger
List every claim the piece will make and the source behind it [copywriting, copy-editing Sweep 4, content-research-writer].
- Supported: keep it, note the source.
- Wanted but unsupported: don't write it and don't drop it silently. Name the claim, say why it falls short, offer the closest
  supportable line, and name the evidence that would unlock it (review export, written guarantee, certification, citable study).
  A declined claim with an unlock path is an action item; without one it is a dead end [copywriting].
- Missing fact: mark `[NEED: number / customer / differentiator / source]`.

Never fill a gap with an invented stat, customer, quote, testimonial or anecdote. Replacing "industry-leading" with a made-up
number is worse than the puffery [ai-tells]. Fake reviews and testimonials also break the FTC consumer-reviews rule (in force
since October 2024).

### 3. Find the writer (Situation A rewrites; in B the writer already exists)
Answer silently [ai-tells "build a writer", humanizer "add soul"]: who is writing and why; what they know cold (it gets the most
words); what bores them (compress or cut); one honest opinion someone could disagree with ("Most onboarding checklists are busywork.
Ours has three steps."); what goes first if a third must be cut (cut it now). The answers give uneven density, mixed register,
honest limits and lopsided sections, which generated copy lacks. Opinions and emphasis can be constructed. Experiences, feelings,
customers and stories cannot: use what the user gave or mark `[NEED: founder story]`. Keep the brand's register; a formal voice
with specific claims is fine.

### 4. Structure before sentences
- Hero spine = the Human Action Model [copywriting]: current discomfort in the reader's words, then the better vision, then the
  path (product + CTA). Miss a beat and the reader stalls. SavvyCal's "You shouldn't have to feel awkward sending out your
  scheduling link" hit all three and roughly tripled conversions.
- One idea per section, each section advancing one argument down the page [copywriting, copy-editing Rule of One].
- Default sections: hero, social proof, problem, benefits (3-5), how it works (3-4 steps, only when the mechanism is
  unfamiliar; see conflicts), objection handling (FAQ, comparison, guarantee), final CTA with risk reversal.
- Page jobs: homepage = broadest value plus a path per visitor intent; landing page = one message, one CTA, headline matched to
  the ad or traffic source; pricing = answer "which plan is me" and make the recommended plan obvious; feature page = feature,
  then benefit, then outcome; about = why you exist, connected to the customer, still with a CTA.
- Perception gap [copywriting]: one benefit reads as a plus to one segment and a red flag to another ("ship in a weekend" is
  momentum to a startup, immaturity to an enterprise buyer). Segment the traffic or the page; don't average into mush.

### 5. Draft by decompose-and-lock
[copywriting] Break the piece into named units (headline, subhead, CTA, each section head and body, proof lines). Per unit,
draft 2-3 candidates, keep the best, fix its worst flaw, lock it. In B, lines that already work are locked from the start.
Run every line you write or keep through the three-question gate:
1. Can the reader picture it?
2. Can it be proven true or false?
3. Could a competitor write this exact sentence? (swap test)

Three passes, keep it. Two, sharpen the weak one. One or none, rewrite from the facts or flag `[NEED: ...]`. Then:
- "Now you can..." test on each headline and benefit line: the result must be compelling and true.
- Ration the punch: one or two punchy moments per page (usually the headline and one section); everything else plain,
  specific and declarative. When every line tries to land, none do.
- CTA = action verb + what they get + qualifier ("Get the complete checklist", "See pricing for my team"). Not Submit,
  Sign up, Learn more, Click here or a bare Get started.
- Clear beats clever. If the reader has to decode a line, it fails.
Assemble the units and read the whole piece once for flow.

### 6. Edit in sweeps (A and B; skip for C)
[copy-editing] One dimension per pass. After each sweep, re-check the earlier ones, since an emotion edit can break clarity.
1. Clarity: confusing structure, unclear pronouns, jargon, the point buried in qualifications. Confirm one idea per section and
   that the copy speaks to the reader ("you").
2. Voice and tone: casual drifting into corporate, "we" vs "the company", random technical terms. Read it aloud.
3. So what: every feature gets its "which means..." bridge to something the reader wants.
4. Prove it: each claim backed by the ledger, with the proof placed near the claim.
5. Specificity: vague verbs (improve, enhance, optimize), outcomes without numbers or timeframes. What can't be made specific
   is usually filler; cut it.
6. Heightened emotion: paint the before-state with concrete detail and small real stories. Emotion serves the message; no fake
   urgency or scarcity.
7. Zero risk: answer every hesitation near the CTA (guarantee, trial, "No card required", what happens next, privacy).

Leave-it-alone test after the sweeps: is each change measurably better or just different? Revert any change you can't give a
reason for [copywriting, copy-editing]. When editing someone's own copy, present findings with specific rewrites and let the
author decide; re-check earlier sweeps after each round.

### 7. De-AI pass (every deliverable, every mode)
[copywriting ai-tells, copy-editing AI-tell check, humanizer] Short version here; the merged catalog is `references/de-ai-pass.md`.
1. In short copy (headlines, subheads, CTAs, ads, posts, subject lines) search for "not ", "isn't", "no ", "without", "?", ":" and
   dashes. Check each hit against the six bans below.
2. Read every sentence over 20 words. More than two commas usually hides a trailing pile-on.
3. Count caps per section: one fragment, one list of three, and cap-list words (two in one paragraph means rewrite the paragraph).
4. Scan the content patterns: inflated significance, vague attribution, "-ing" tails ("highlighting...", "ensuring..."),
   promotional words, "serves as" for "is", false ranges, synonym cycling, generic upbeat endings, chatbot residue ("I hope this
   helps", "Great question", knowledge-cutoff disclaimers).
5. Second-generation tells: wisdom-shaped sentences, a tidy closer on every section, staccato bursts, perfectly balanced
   sections, a relaxed voice that never admits a limit, self-narration ("Here's why this matters").
6. Soul check: if the text is clean but flat (same sentence lengths, no opinion, no limits), go back to step 3, not to a thesaurus.
7. Read it aloud. Fix from the facts, since synonym swaps create new tells, and vary the fixes so ", because..." doesn't become
   the new tic.

Exempt (locked) text: legal and compliance wording (SMS opt-in disclosures, STOP/HELP language, disclaimers, terms), direct quotes,
exact product names. De-AI the copy around it, never the locked text itself.

### 8. Gate and deliver
- Expert panel for high-stakes copy (launch, pricing, top landing pages, sales pages) [copy-editing]: 3-5 personas suited to the
  piece (conversion copywriter, UX writer, skeptical target buyer, brand strategist; for long-form an editor and an SEO
  specialist). Each scores 1-10 with specific fixes; revise the lowest first; repeat until every persona gives 7+ and the average
  is 8+. Skip it for point edits and quick updates.
- Output by mode. POINT EDIT: only the changed lines, a one-line reason each, one alternative if the call is close, and one line
  at the end naming any serious problem elsewhere (unfixed). WRITE: copy by section, short annotations on key choices, 2-3
  headline and CTA alternatives with a rationale each, page title and meta description for web pages. EDIT: findings per sweep
  with specific rewrites. Every `[NEED: ...]` collected in one list at the end.

## Researched long-form track (L1-L8)

[content-research-writer, content-strategy, copywriting] For articles, newsletters, case studies, tutorials, thought leadership.
- L1. Information-gain gate [content-strategy]: read the current top results for the query and write one sentence on what this
  piece adds that none of them has (original data, a real example, a working template, a clearer answer, a stronger opinion).
  No sentence, no piece: it would be the eleventh copy of the same article, and neither Google nor AI assistants would prefer it.
- L2. Working folder [content-research-writer]: `~/writing/<slug>/` or the project's content dir, with `outline.md`,
  `research.md`, `draft-v1.md`, `final.md`, `sources/`. Research stays out of the draft file; version drafts instead of overwriting.
- L3. Outline: hook, intro (context, problem, what it covers), sections each with key points, evidence and
  `[Research needed: ...]`, a conclusion with one CTA, and a research to-do list. Write 10 title options before drafting
  [content-strategy]. Build distribution in now: subheads that stand alone as posts, liftable sections, stats that can become graphics.
- L4. Research: credible, recent, original sources. Open and read every source you cite and record the quote, number, date and
  URL in `research.md`; balance perspectives. A citation you haven't opened is a `[NEED: source]`, never a plausible guess.
  Citation style on request: inline (Author, Year), numbered [1] with a reference list, or footnotes. Free web search and
  context7 first; paid search or scrape APIs ask the user.
- L5. Hook: three options of different types (specific data, a real story, the reader's own question), each with one line on
  why it works; check curiosity, promised value, specificity, audience fit. Hooks still obey the bans: no self-answered
  "The result?" openers, no invented stories.
- L6. Draft section by section using the section-feedback shape [content-research-writer]: what works; clarity, flow, evidence
  and style fixes; exact line edits as original -> suggested -> why. If the user is writing, suggest and offer options; if Claude
  writes, use decompose-and-lock (step 5).
- L7. About five passes [content-strategy]: structure, clarity, evidence, line edit, headline/SEO. Then step 7.
- L8. Pre-publish: every claim sourced, citations formatted and live, examples clear, transitions smooth, one CTA, proofread;
  evergreen pieces show "Last updated" and the year beside every statistic [copy-editing refresh]. Then the atomization list:
  3-5 standalone posts, one thread or carousel, 1-2 stat graphics, one email to the owned list, a reshare schedule [content-strategy].

Variants [content-research-writer]: newsletter = hook ideas, quick outline, one-session draft, link check. Tutorial = steps,
tested code or examples, explanations, troubleshooting section, accuracy review. Thought leadership = angle, existing views,
thesis, strong point of view backed by evidence.

## Strategy track

[content-strategy]
1. Treat each piece like a product launch: planned, shipped and distributed. Every piece is searchable, shareable or both, and
   searchable is the foundation.
2. Pillars: 3-5 topics the brand will own, found product-led, audience-led, search-led and competitor-led. Each spawns a
   cluster. Most content lives under `/blog` with strong internal links; build the hub before its spokes.
3. Ideas from evidence: sales and support calls (questions, objections, exact phrases), surveys (30%+ mention = high priority),
   keyword exports (clusters, buyer stage, intent, quick wins, gaps), forums (`site:reddit.com [topic]`), competitor blogs (gaps,
   outdated posts).
4. Buyer stage by modifier: awareness (what is, how to, guide), consideration (best, vs, alternatives), decision (pricing,
   reviews, demo), implementation (templates, examples, tutorial, setup).
5. Score each idea 1-10 on customer impact (40%), content-market fit (30%), search potential (20%), resources (10%); weighted
   sum; make the top scores first.
6. Calendar 60/30/10: searchable / shareable / experimental. A starting ratio, not a law.
7. Pick the format by its job. For backlinks, stat roundups earned about 4.25x their page share, glossaries 1.47x, free tools
   1.38x, how-tos 1.36x, original research only 0.80x (one 2026 B2B SaaS vendor study; directional). Pair original research with
   your own stat page so you catch the links it generates.
8. Distribute twice: one flagship, atomized and routed borrowed -> rented -> owned (email list, blog, community). Owned is the
   only durable asset; rented reach can vanish (Facebook organic went from about 20% to under 2%).

Output: pillars with rationale, priority topics (title, searchable/shareable, type, keyword, stage, the evidence behind it), and
a cluster map.

## Offer track: lead magnets and free tools

[lead-magnets, free-tools] Both trade value for an email, so plan them with one method.
1. Problem: one specific pain your product also solves ("cold emails that get replies", not "marketing guide"), matched to the
   buyer stage (awareness = educate, consideration = compare, decision = implement), with a natural path to the product.
2. Format:

| Need | Format | Effort |
|---|---|---|
| Quick win, process steps | Checklist, cheat sheet | 1-4 hours |
| Repeatable work | Template (doc, sheet, Notion), swipe file | 2-8 hours |
| Authority, depth | Ebook/guide, email or video mini-course, webinar | 1-4 weeks |
| Segmentation | Quiz or assessment | 1-2 weeks |
| A numbers decision, or judging their own work | Calculator, generator, grader, analyzer, tester (free tool) | MVP in days |
| Product experience | Free trial, community access | Varies |

   Consumable in under 30 minutes (ideally 10), one format, works on mobile, needs no special software.
3. Free tools get scored before building (1-5 each): search demand, audience match to buyers, uniqueness, path to product, build
   feasibility, maintenance burden (inverse), link potential, share-worthiness. 25+ strong, 15-24 promising, under 15 reconsider.
   Build only if lead value x expected leads beats build plus upkeep. MVP = the one job, clear input, obvious output, mobile,
   email capture; skip accounts, saved results and edge cases. Build custom when it is core and unique, use no-code (Tally,
   Typeform, Outgrow) to test demand, embed when something good already exists. Tool pages target "[thing] calculator",
   "[thing] generator" and "free [tool]" queries, backed by "how to [use case]" articles; useful, unique tools earn links.
4. Gate:

| Gate | Use when | Trade-off |
|---|---|---|
| Full | High-value, bottom-funnel | Max capture, low reach |
| Partial (preview or result summary free, full report gated) | Most guides and tools | Balance |
| Ungated + optional capture | Top-funnel education, SEO tools | Max reach |
| Content upgrade (post-specific bonus) | Blog traffic | Converts 2-5x a generic sidebar CTA |

   Ask for email only unless the offer is high value; each extra field costs roughly 5-10% conversion. Frame the trade: what they
   get, a preview (contents, first page, sample result), real social proof, "No spam. Unsubscribe anytime."
5. Page and delivery: headline (what they get and why it matters), mockup, 3-5 "what's inside" bullets, proof, short form, FAQ.
   Deliver on a thank-you page plus an email copy. Use the thank-you page: confirm delivery, one next step, a share prompt,
   related content.
6. Promote: in-post CTAs and content upgrades, exit-intent or scroll popups matched to the page (conversion-lab), social
   snippets, paid promotion (ads-and-measurement), partner newsletters. The post-capture nurture goes to lifecycle-messaging.
7. Measure: landing conversion 20-40% warm traffic and 5-15% cold, lead-to-customer rate, engagement and unsubscribes after
   delivery; for tools, leads and trial or purchase conversion, never visitors alone. Test headline, format, gate level, fields, CTA.

Pitfalls: building before demand exists (Unsplash began as a Tumblr with Dropbox links), no path to the product, tools that rot
or become attack surfaces (budget the upkeep), vanity usage numbers.

## Core rules and checklists

### Writing style
- Simple over complex (use, help), specific over vague, active over passive, customer words over company words, benefits over
  features, outcomes over adverbs [copywriting].
- Cut very, really, extremely, just, actually, basically, "in order to", things, stuff; undo nominalizations ("make a
  decision" -> "decide") [copy-editing].
- Replace a vague word with the fact, not a synonym: innovative -> what it does that others don't; robust -> the uptime or
  scale; seamless -> the real step count or minutes [copy-editing, ai-tells].
- Sentences: one idea, usually 25 words or fewer, at most three conjunctions, point first, length varied on purpose.
  Paragraphs 2-4 sentences on the web [copy-editing].
- No exclamation points or hype punctuation in body copy; sentence-case headings unless the brand guide says otherwise; no
  emojis as structure or decoration; straight quotes, not curly (curly quotes also push SMS into costlier UCS-2 encoding)
  [copywriting, ai-tells, humanizer, sms].

### Simplified Technical English [simplified-english]
For procedures and explanations, not for selling (ASD-STE100 style):
- Short sentences: procedures 20 words or fewer, descriptions 25 or fewer; one instruction per sentence; one topic per paragraph.
- Active voice, present tense, positive instructions ("Close the form", not "Don't leave the form open"); keep "the" and "a",
  never drop words to save space.
- One word, one meaning: pick the term and keep it (no synonym cycling, which is also an AI tell); no jargon; the simplest
  common word when unsure: start/stop (not initiate, terminate), make (not implement, leverage), use (not utilize), before/after
  (not prior to, subsequent to), about (not regarding), help (not facilitate).
- Technical names and verbs the subject needs stay as they are (node names, field names, menu labels).

### The six bans

| Ban | Example | Fix |
|---|---|---|
| Contrast reveal | "It's not X, it's Y." "Not because X. Because Y." "Not just X, but Y." | State Y directly, with the reason |
| Negation list | "No setup, no templates, no waiting on IT." | Say what does happen; one real absence by the CTA ("No card required") is fine |
| Trailing pile-on | "...the data you have, no exports, no spreadsheets." "...it syncs, ensuring nothing slips." | End at the claim; a clause that adds a new fact may stay |
| Self-answered question, colon reveal | "The result? 3x faster." "The best part: it learns." | Keep the answer as a plain sentence |
| Stock openers and phrases | "In today's fast-paced world", "Whether you're X or Y", "Here's the thing", "Imagine...", "Say goodbye to", "X, reimagined", "Unlock the power of", "Take it to the next level" | Open with the reader's problem or the fact |
| Em dashes in short copy | Headlines, subheads, CTAs, ads, posts, subject lines | Period, comma, colon or parentheses. Long copy: 1-2 per page. Never "--" as a stand-in |

Still fine: FAQ questions; a question in the reader's voice followed by what to do ("Need to share a screenshot? Drop it in the
thread."); one "without" or "Never X again" headline; a list of three when there really are three features.

### Proof and claims
- Every claim sentence carries a number, a name, a mechanism or a concrete action [ai-tells].
- Proof to look for: named testimonials with specifics, case studies, data, third-party validation, guarantees, logos, review
  scores [copy-editing]. "Trusted by thousands" -> which thousands; "industry-leading" -> by whom; "experts say" or "studies
  show" -> a named source, or cut it [copy-editing, humanizer].
- Numbers come only from the source. A suspiciously round stat or a too-neat anecdote reads as generated and is a liability.

### Common problems and fixes [copy-editing]
Wall of features -> "which means..." after each. Corporate speak -> "how would a person say this?". Weak opening (company history)
-> lead with the reader's problem. Buried CTA -> early, obvious, repeated. No proof -> a testimonial or number next to the claim.
Generic claim -> who, how, how much. Mixed audiences -> one audience per page. Feature overload -> the 3-5 benefits that matter most.

### Refresh rules [copy-editing]
Refresh when a page that used to perform is losing traffic, stats are 12+ months old, the product changed, competitors updated,
or AI-search citations matter. Six passes: freshness, accuracy, voice, SEO (has intent shifted?), proof, structure. Keep the URL
(301 if it must move), heading anchors other pages link to, sections that rank for their own queries, and the voice. Details
outdated -> refresh; angle, audience or search intent shifted -> rewrite. Cadence: pricing and product pages quarterly,
comparison pages every 3-6 months, high-traffic posts every 6 months, evergreen guides yearly. Show the gap grid and a
Keep/Revise/New outline before rewriting, and never promise a ranking.

## When members disagree

| Between | Conflict | Rule |
|---|---|---|
| humanizer vs copywriting ai-tells | "Have opinions, use I, let some mess in, be specific about feelings" vs "never invent experience; fake vulnerability is banned; first person only when it means something" | Voice comes from facts. Arguable opinions and uneven emphasis may be constructed; feelings, anecdotes and "I" statements need a real source (the user, the client, a sample). Tangents and asides only in long-form and blogs, never in landing copy |
| humanizer vs copywriting/copy-editing | Humanizer writes "--" freely in its own examples; copywriting bans dashes in short copy | No dashes of any kind in short copy, 1-2 per page in long copy, never "--" as a substitute |
| humanizer vs copywriting/copy-editing | Humanizer says skip legal/compliance text; the others run the AI-tell check on every edit | Compliance text is locked (step 7 exemption); the pass runs on everything around it |
| copywriting (internal) | "Use rhetorical questions" vs the ban on self-answered questions | A reader's-voice question about their own pain, followed by what to do, is fine. A question that labels your own claim is banned |
| copywriting/copy-editing vs humanizer | "Confident over qualified, remove almost/very" vs "acknowledge uncertainty and mixed feelings" | Cut empty hedges ("could potentially help"); keep honest scope (who it isn't for, what isn't known). Total certainty in a casual voice is itself a tell |
| copy-editing Sweep 5 vs ai-tells | "2,847 teams beats many customers" vs "reflexive specificity" and never-invent | Specific numbers only from the ledger; otherwise `[NEED: number]` |
| copywriting page template vs the user's rules | "How It Works (3-4 steps)" is a core section vs a conversion-first rule: no how-it-works explainers | Shops and familiar flows: cut it. Keep it only where the mechanism is unfamiliar and the section removes a real objection |
| content-research-writer vs copywriting and the user's cost rule | Ask many clarifying questions, "suggest, don't replace", check "does this sound like you?" often vs decompose-and-lock drafting and the user's "do it yourself" | When the user is writing (their draft, their voice), run the collaborative loop. When Claude writes for the user, ask real gaps once, then deliver a finished draft with assumptions listed |
| content-strategy vs the user | Searchable-first traffic calendar vs "convert the most visitors into buyers" | For commerce brands, favor decision and implementation content that sells (buying guides, comparisons, product-led pieces); traffic for its own sake ranks last |
| copy-editing Sweep 6 vs ai-tells | "Fear of missing out, heighten emotion" vs hype bans and honest-copy rules | Emotion through concrete before-state detail and real stories; urgency or scarcity only when true |
| content-research-writer vs humanizer | Templates end with "Ready to publish!" plus a rocket emoji and use check-mark emojis vs the decorative-emoji ban | No emojis in deliverables or feedback |
| content-research-writer examples vs claims ledger | Illustrative citations that look real ("Gartner: 80% of PMs...") | Never cite a source you haven't opened; illustrative numbers are marked `[NEED: source]` |
| lead-magnets vs free-tools | Two separate gating tables and capture rules | One merged gate table (offer track step 4) |
| simplified-english vs humanizer soul check and Writing style | Uniform short sentences and fixed vocabulary vs "vary sentence length on purpose", voice and opinion | SIMPLE ENGLISH mode (procedures, SOPs, error text, plans, agent instructions): STE rules win. Marketing and long-form: the voice rules win. Mixed pages: STE inside the steps, voice around them |

## Combine with

- Skill tool: `humanizer` and `content-research-writer` (always on; already folded in here, call them only for a standalone
  request), `deep-research` (report-grade evidence and citations), `superpowers:brainstorming` (angles and positioning before a
  big page), `superpowers:verification-before-completion` (before saying copy is live), `artifact-design` (the user's review page),
  `pdf-creator` or `anthropic-skills:pdf` (lead magnet PDFs), `anthropic-skills:docs` (shareable drafts).
- Sibling super-skills: conversion-lab, seo-suite, lifecycle-messaging, ads-and-measurement, audience-growth, brand-studio
  (voice and guidelines), growth-strategy (customer research, positioning), research-hub.
- Agent prompts in `~/.claude/skill-library/agents/voltagent/` (the user's rule: model haiku for lookups; give the agent the copy,
  not your conclusion):
  - `08-business-product/landing-page-copywriter.md`: an independent second draft of a hero to compare against yours.
  - `08-business-product/content-quality-editor.md` and `04-quality-security/ai-writing-auditor.md`: a cold de-AI read that
    isn't anchored on your draft.
  - `08-business-product/content-marketer.md`: multi-channel content plans.
  - `07-specialized-domains/seo-specialist.md`: the keyword side of a long-form brief.
  - `10-research-analysis/research-analyst.md`: source gathering for long-form.

## House rules

- Stores are conversion first: every section must answer "does this get more people to buy?"; cut sections that only
  explain; back layout and copy calls with conversion evidence (Baymard, NN/g, GoodUI).
- Drafts are free. Anything that publishes, posts, deploys or sends (site, Shopify, social, email, blog CMS) asks the user first.
- Copy changes to a live page go through the user's review page: one card per change, old and new side by side, the reason in plain
  words, a pick + note box; build only from their picks.
- Paid research and scraping APIs (Exa, Firecrawl and the like) ask first; free web search and context7 come first.
- Loan and debt-relief wording in texts is carrier-sensitive: route it through
  lifecycle-messaging's carrier check.
- Keep chat replies short; long drafts go in files and the reply names the file.

## Members

| Member | Best at | Path |
|---|---|---|
| copywriting | A/B/C diagnosis, decompose-and-lock, three-question gate, claims with unlock paths, Human Action Model, the AI-tells blacklist | `members/copywriting/SKILL.md` (+ `members/copywriting/references/ai-tells.md`, `copy-frameworks.md`, `natural-transitions.md`) |
| copy-editing | Seven Sweeps with loop-backs, point-edit mode, expert panel scoring, quick word/sentence checks, content refresh gap grid | `members/copy-editing/SKILL.md` (+ `members/copy-editing/references/checklist.md`, `content-refresh.md`, `plain-english-alternatives.md`) |
| content-strategy | Searchable vs shareable, information-gain gate, pillars, buyer-stage keywords, 40/30/20/10 scoring, 60/30/10 calendar, link-earning formats, distribution flywheel | `members/content-strategy/SKILL.md` (+ `members/content-strategy/references/content-distribution.md`, `headless-cms.md`) |
| lead-magnets | Format-by-stage choice, gating and form-field trade-offs, landing and thank-you pages, benchmarks, content-to-agent-skill packaging | `members/lead-magnets/SKILL.md` (+ `members/lead-magnets/references/format-guide.md`, `benchmarks.md`, `content-to-skill*.md`) |
| free-tools | Engineering-as-marketing ideation, 8-factor scorecard, MVP scope, build vs buy, pitfalls | `members/free-tools/SKILL.md` (+ `members/free-tools/references/tool-types.md`, `tool-benchmarks.md`) |
| content-research-writer | Collaborative long-form: outline template, research with citations, hook options, section-by-section feedback, draft file layout | `members/content-research-writer/SKILL.md` |
| humanizer | 24-pattern AI-writing catalog (content, language, style, chatbot artifacts, hedging) and the "soulless but clean" check | `members/humanizer/SKILL.md` (+ `members/humanizer/references/patterns.md`) |
| simplified-english | ASD-STE100 core rules for text that must be understood the first time: sentence limits, one instruction per sentence, one meaning per word, house word swaps | `members/simplified-english/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
