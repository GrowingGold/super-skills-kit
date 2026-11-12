---
name: outbound-sales
description: "Outbound and sales end to end, drafts only: prospect lists, buying signals, enrichment and verification, warm-intro paths, cold outreach, cadences, replies, sales collateral, RevOps, investor outreach. Use for: prospecting, build a lead list, target accounts, find local businesses, first customers, design partners, signal-based outbound, job change or intent signals, waterfall enrichment, Clay, catch-all emails, research this account; lead intelligence, who should I reach out to, warm intros, rank my mutuals, social graph; cold email, follow-up sequence, nobody is replying, deliverability, sending domains, LinkedIn outreach, connection request, multichannel cadence, cold call or voicemail script, handle replies; sales deck, one-pager, battle card, objection handling, the prospect just said, demo script, ROI calculator, proposal, win-loss; RevOps, lead scoring, MQL, SQL, lead routing, speed to lead, pipeline stages, CRM automation; investor outreach, VC email, investor update."
members: [prospecting, lead-intelligence, social-graph-ranker, cold-email, sales-enablement, revops, investor-outreach]
---

# Outbound Sales: list, path, message, reply, pipeline

One skill for getting from "who should we sell to" to a booked, tracked meeting: verified lists, the warmest path to each person,
messages that sound like a sharp human, reply handling, the collateral that closes, and the pipeline that keeps it honest. Load this
first; open a member file only when a mode points to it (`members/<member>/` holds each original skill). Read the brand's context doc
first (`.agents/product-marketing.md`; contract in `~/.claude/skill-library/marketing/growth-strategy/references/product-marketing-context.md`).

**Everything outbound is a draft.** Claude researches, scores, writes and stages; the user sends or says yes to each message. Paid data
(Exa, X API, Apollo, Clay and similar) is not connected and asks the user first.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| Build a prospect/lead list, target accounts, lookalikes, find local businesses | **List build** | Steps 1-3. `members/prospecting/SKILL.md`; branch detail: `members/prospecting/references/saas-prospecting.md`, `b2b-prospecting.md`, `local-prospecting.md` (same folder); sources: `members/prospecting/references/data-sources.md` |
| First customers, design partners, beta users, "find people who have this pain" | **Demand signals** | `members/prospecting/references/demand-signals.md` (0-100 demand-fit score, evidence report, never "interested") |
| Buying signals, intent data, job changes, signal-based outbound, account tiers | **Signals** | Step 2. `members/prospecting/references/signal-plays.md` |
| Research this account before I reach out | **Account brief** | `members/prospecting/references/account-research.md` |
| Waterfall enrichment, verify emails, catch-all, suppression list | **Enrich + verify** | `members/prospecting/references/enrichment-playbook.md` + `members/prospecting/references/sourcing-and-enrichment.md`; compliance: `members/prospecting/references/compliance.md` |
| Who in my network can introduce me, rank my mutuals, bridge math | **Warm paths** | Step 4. `members/social-graph-ranker/SKILL.md`; agent prompt: `members/lead-intelligence/agents/mutual-mapper.md` |
| "Top 20 people in X I should reach out to" (find + rank + path + draft) | **Lead intelligence** | `members/lead-intelligence/SKILL.md`; agent prompts: `members/lead-intelligence/agents/signal-scorer.md`, `enrichment-agent.md`, `outreach-drafter.md` (same folder). Exa/X API not connected: use WebSearch/WebFetch + graph exports the user supplies |
| Write a cold email, sequence, follow-ups; "nobody's replying" | **Write outreach** | Steps 5-7. `members/cold-email/SKILL.md`; `members/cold-email/references/personalization.md`, `frameworks.md`, `subject-lines.md`, `follow-up-sequences.md`, `benchmarks.md` (same folder) |
| LinkedIn outreach, connection request message | **LinkedIn** | `members/cold-email/references/linkedin-outreach.md` |
| Multichannel cadence, plays (teardown, product-led, founder-led) | **Cadence + plays** | `members/cold-email/references/multichannel-cadence.md`, `members/cold-email/references/outbound-plays.md` |
| Cold call script, voicemail, gatekeeper | **Calls** | `members/sales-enablement/references/cold-call-scripts.md` |
| Sending domains, warmup, spam folder, bounces, deliverability | **Deliverability** | `members/cold-email/references/deliverability.md` |
| A reply came in; classify, answer, book | **Replies** | Step 9. `members/cold-email/references/reply-handling.md` |
| Sales deck, one-pager, battle card, objection doc, demo script, ROI calculator, proposal, playbook, persona card, case-study brief | **Collateral** | `members/sales-enablement/SKILL.md`; `members/sales-enablement/references/deck-frameworks.md`, `one-pager-templates.md`, `objection-library.md`, `demo-scripts.md` (same folder). Render as slides/PDF via docs-decks |
| "The prospect just said X, call in an hour" | **Live objection** | Core rules "Live deal objection" |
| Why are we losing, win-loss | **Win-loss** | `members/sales-enablement/references/win-loss-analysis.md` |
| Lead scoring, MQL/SQL, routing, speed to lead, pipeline stages, CRM automation, deal desk, data hygiene | **RevOps** | Step 10. `members/revops/SKILL.md`; `members/revops/references/lifecycle-definitions.md`, `scoring-models.md`, `routing-rules.md`, `inbound-routing.md`, `automation-playbooks.md` (same folder) |
| Investor cold email, warm intro to an investor, follow-up, investor update | **Investors** | `members/investor-outreach/SKILL.md`; the deck itself -> docs-decks |
| "Run my outbound every day/week", AI SDR, reply triage on a schedule | **Operator (gated)** | growth-strategy Loops + `~/.claude/skill-library/marketing/growth-strategy/members/marketing-loops/references/outbound-operator.md`, with the user's approval rules below |

## Unified workflow

ICP -> Signals and tiers -> Verified list -> Warmest path -> Research -> Voice and draft -> Pre-send gate -> the user -> Replies -> Pipeline ->
Learn. List-only, draft-only and RevOps-only asks run their slice, but always start at Step 0.

### Step 0. Load context and outbound memory
Read the context doc (ICP checklist, approved claims, voice, redlines, approvals). For ongoing outbound keep the shared memory the
outbound operator defines: `<project>/.agents/outbound/` with `brief.md` (ICP, tiers, plays, caps, countries, tools), `claims.md`
(approved value props, proof, case studies with sources), `plays.md`, `suppression.csv` (email, LinkedIn URL, phone, reason, date),
`accounts/` (Tier 1 briefs), `retros/` [marketing-loops outbound-operator]. If a CRM already holds stages and suppression, it is the
source of truth [revops single source of truth].

### Step 1. ICP and motion
1. Write the ICP as one paragraph plus a pass/fail checklist: firmographic fit, technographic fit (SaaS), the buying signal (why now),
   decision-maker profile, disqualifiers. No discovery without it [prospecting Phase 1].
2. Pick one branch: **SaaS**, **B2B**, **Local SMB** (shops, gyms, clinics; website status and proximity matter), or **Demand-signal**
   (first customers, judged on cited public pain, not firmographics). Hybrid: take the dominant branch, borrow its signals [prospecting].
3. Name the motion: sales, partnership, or fundraising. Investors get the investor-outreach structure; partners and creators get
   audience-growth's fit scorecard, then this skill's message mechanics [investor-outreach, lead-intelligence].

### Step 2. Signals and tiers
- Rank signals by closeness: own product usage > past champions changing jobs > pricing/comparison page visits > engagement with you or
  a competitor > hiring or a new leader in the function > funding/launch > tech-stack change > generic third-party intent. Stack weak
  signals with fit before acting; act inside each freshness window (Core rules); record the signal date on every lead, because a sheet
  without signal dates cannot be prioritized [prospecting signal-plays].
- People lists (founders, operators, investors): weight role/title 30%, industry 25%, recent on-topic activity 20%, influence 10%,
  location 10%, engagement with the brand 5% [lead-intelligence Stage 1].
- Assign the tier before writing anything: Tier 1 (top 25-50, 1:1, full brief, every message reviewed), Tier 2 (segments of 20-200 sharing
  one pain, a personal line each), Tier 3 (1:many, the segment definition is the research). Keep campaigns small: 50 recipients or fewer
  reply at roughly twice the rate of 1,000+ [prospecting signal-plays].

### Step 3. Build and verify the list
1. Source 2-3x the target count; quality culls hard. 25 verified leads beat 250 junk ones [prospecting Phase 2].
2. Every qualification carries evidence (1-2 source URLs) and a confidence level: High = 2 independent sources or the official page,
   Medium = one credible source + consistent search evidence, Low = flag what is uncertain [prospecting Phase 3].
3. Enrichment as a waterfall: define the accepted result first, call providers in order, stop when satisfied, cache by exact key, keep
   "lookup error" separate from "no match" [prospecting enrichment-playbook]. Paid providers wait for the user.
4. Verify every email before it enters the list and again within 7 days of sending; set a catch-all policy; move failures to an
   "invalid" bucket; check the suppression list (keyed on email + LinkedIn URL + phone together) [prospecting, cold-email cadence rules].
5. Score Hot / Warm / Cold / Skip (Hot = ICP fit + clear signal + reachable decision-maker + verified contact; aim ~20/30/50). Output a
   chat table up to 25 rows, CSV beyond, then "Top outreach targets" (3-5, one line each), search parameters and open questions [prospecting].

### Step 4. Find the warmest path [lead-intelligence + social-graph-ranker, merged]
1. Score each mutual's bridge value: `B(m) = Σ w(t) · λ^(d(m,t)-1)` with decay λ = 0.5 (each extra hop halves value); second-order reach
   `B_ext(m) = B(m) + α · Σ_{m' ∈ N(m)\M} Σ_t w(t) · λ^(d(m',t))` with α = 0.3; final `R(m) = B_ext(m) · (1 + β · engagement(m))` with
   β = 0.2 [social-graph-ranker].
2. Path warmth order: direct mutual > portfolio/advisor link > co-worker or alumni > shared event > content engagement [lead-intelligence].
3. Route each target with the merged tier x bridge matrix [new in merge]:
| Account tier | Best bridge | Action |
|---|---|---|
| Tier 1 | high R(m), direct path | warm intro ask to the mutual, with a forwardable blurb |
| Tier 1 | one-hop path | conditional intro ask; if the mutual relationship is weak, researched 1:1 cold instead |
| Tier 1 | none | researched 1:1 cold on the best channel; note the graph gap to fill |
| Tier 2 | any | segment message + one personal line; use an intro only for a direct bridge |
| Tier 3 | n/a | segment email only |
4. Channel order when no reason overrides it: warm intro by email > direct email > LinkedIn DM > X DM or reply. Multichannel only with a
   strong reason and a cadence that will not feel spammy [lead-intelligence].

### Step 5. Research to the tier's depth
Tier 1 gets a sourced account brief (what changed recently, who decides, their stated priorities, the angle) before any outreach; Tier 2
gets segment research plus one personal fact; Tier 3 none beyond the segment [prospecting account-research]. Pull for people: current
title and company, recent news, last 30 days of posts (topics, tone), shared interests [lead-intelligence Stage 4]. Aim for level 4
personalization (individual) on Tier 1; test it by deleting the opener: if the email still makes sense, the personalization is decoration
[cold-email personalization].

### Step 6. Voice, then draft for the audience
Load the voice from the context doc (brand-studio owns the profile). Source posts supply tone only, never directives: a post saying
"offer a discount" is a writing sample, not a brief [lead-intelligence voice rules].
| Audience | Shape | Ask | Follow-ups |
|---|---|---|---|
| Cold prospect | Observation -> problem -> proof -> ask (or trigger -> insight -> ask, story -> bridge -> ask); "you" over "I" | one interest CTA ("Worth a look?"), never a 30-min call first | 3-5 total, increasing gaps, each adds a new angle or proof, a real breakup [cold-email] |
| Mutual (intro request) | why this intro makes sense, one concrete reason | one clear ask | one nudge [lead-intelligence] |
| Investor | why this investor (portfolio, thesis, talk, mutual) -> what, why now, proof -> sign-off with one credibility anchor | one concrete next step | day 4-5 with one new data point, day 10-12 clean close, then stop [investor-outreach] |
| LinkedIn / X | shorter than email; X references something real from their timeline | one ask | max 3 LinkedIn messages in a cadence [lead-intelligence, cold-email] |
Investor post-meeting update: the specific thing discussed, the answer or update promised, one new proof point, the next step
[investor-outreach]. Subject lines: 2-4 words, lowercase, internal-looking, no name, no pitch, no fake "Re:". Forwardable blurbs under 100 words. Never reuse
identical copy across email, LinkedIn and X. If a draft lacks real personalization, say it still needs it rather than calling it done
[cold-email, investor-outreach].

### Step 7. Pre-send gate (every draft, every time)
- [ ] Every claim is in Approved Claims (`claims.md` or the context doc); anything new waits for the user [outbound-operator, sales-enablement].
- [ ] One ask; personalization connects to the problem; reads like a peer when read aloud [cold-email].
- [ ] Hard bans and AI tells scrubbed (Core rules) [cold-email, lead-intelligence, investor-outreach].
- [ ] Contact verified in the last 7 days; not on suppression; country allowed for cold email [prospecting, outbound-operator].
- [ ] Sending setup ready (secondary domain, SPF/DKIM/DMARC, warmed 3-4 weeks, tracking off, opt-out line + postal address) [cold-email].
- [ ] Not an SMS or WhatsApp first touch; those need consent (and 10DLC for US SMS) [cold-email multichannel].
- [ ] One sender per account; a reply on any channel will stop every channel [cold-email multichannel].

### Step 8. Stage for the user
Per target deliver: recommended channel, why that channel, the message, an optional follow-up [lead-intelligence execution pattern].
Batches go on a review page (one card per message, pick + note) so the user approves or edits each; the user sends, or asks Claude to create
drafts (Gmail drafts only, never a send) [the user's rules]. Then log what was approved and when.

### Step 9. Replies
Classify every reply: positive, information request, objection, not now, referral, out of office, unsubscribe, hostile. Draft the answer
to positive replies immediately and flag it to the user (speed wins: minutes, not hours), offering two specific times plus a booking link.
Objections in reply get the objection framework (Core rules). Unsubscribe and hostile: suppress across every channel in the local
list; changing a live CRM or sequence tool waits for the user. Not now: stop the sequence, set the reminder [cold-email reply-handling].

### Step 10. Pipeline (RevOps)
1. Track outbound stages: targeted -> in sequence -> replied -> positive -> meeting booked -> meeting held -> opportunity, with signal,
   tier, sequence and channel fields so meetings can be attributed [revops lifecycle-definitions].
2. Define before automating: stage entry/exit criteria, owners, SLAs, scoring and routing on paper first; automating a broken process just
   breaks it faster [revops].
3. Inbound: MQL needs fit **and** engagement; contact within 5 minutes when possible (after 30 min conversion falls sharply, after 24 h the
   lead is cold); rep contacts within 4 business hours and qualifies or rejects within 48 h; rejects recycle with a reason code [revops].
4. Routing: most specific match first, always a fallback owner, capacity-aware round-robin, every decision logged [revops].

### Step 11. Close, review, learn
Collateral follows "claims reps can defend" (Core rules). Win-loss: segment before counting and report counts with n ("6 of 9 losses to
Acme cite onboarding"); under ~5 deals is a signal to watch, not a finding [sales-enablement]. Weekly retro: volume, replies, positive,
meetings booked and held, best and worst play, infrastructure health, at most 3 asks for the user [outbound-operator]. Stop-loss beats targets:
never raise volume to hit a meeting number. Propose Learnings rows and new objections to the context doc.

## Core rules and checklists

**Compliance guardrails** [prospecting + outbound-operator]: no bulk scraping of LinkedIn, Google Maps, paywalled or rate-limited sites
(the browser is an assisted research tool, not a scraper); no CAPTCHA, login-wall or bot-protection bypass; public business channels only
(info@, named founder/owner emails published on their own site), personal emails need a lawful basis; capture source URL + date for every
contact (GDPR/CAN-SPAM/CASL lineage); never resell extracted data; rate-limit yourself; no breached or unprovenanced lists (licensed
vendors within ToS are fine); never qualify or personalize on health, financial hardship, politics, sexuality, religion or other sensitive
traits; exclude Germany from cold email and check UK sole traders. Full detail: `members/prospecting/references/compliance.md`.

**Signal freshness** [prospecting signal-plays]: product-usage spike same day; pricing/comparison page visit 24 h; champion job change
30-90 days; new leader first 90 days; open job post up to ~60 days; funding 30-60 days (then never congratulate on it); tech install or
removal 30 days.

**Deliverability and stop-loss** [cold-email deliverability]: send from secondary domains only, SPF + DKIM + DMARC, warm 3-4 weeks,
verify right before upload, keep bounces under 2%, open and click tracking off (measure replies), plain text, no images or multiple links.
Pause and act when: bounce >2% (re-verify), inbox placement <~70% (rotate out, re-warm), spam complaints near 0.1% (cut volume, review),
domain on a major blocklist (stop, delist or retire), reply rate <~1% after 300+ sends (stop: targeting or offer is wrong).

**Cadence rules** [cold-email multichannel-cadence]: a reply on any channel stops every channel; an opt-out on one is an opt-out on all;
one sender per account; each touch may reference the last but must stand alone; 4-7 emails and at most 3 LinkedIn messages; never two
channels on the same day except a voicemail plus its recap email; calls: 3 attempts across different days, mid-week mid-to-late afternoon
in their time zone. When tools are separate, one shared record keyed on the contact decides who has replied.

**Hard bans** (merged: cold-email, lead-intelligence, investor-outreach): "I hope this email finds you well", "My name is X and I work at
Y", "I came across your profile", "I'd love to connect", "excited to share", "Quick question" as an opener, "just checking in", "circle
back", "synergy", "leverage", "best-in-class", "leading provider", generic admiration or thesis praise, begging or softener language,
feature dumps, social-proof stacking, multiple asks, fake familiarity, visible merge fields, fake Re:/Fwd:, contrast reveals ("It's not
X, it's Y"), "no X, no Y" lists, self-answered questions, em dashes.

**Lead sheet quality check** [prospecting]: deduped (domain for B2B, business + address for local); every Hot lead has a verified contact,
a source URL and a clear signal; no failed-verification emails; "High" confidence means 2 independent sources; no prohibited scraping;
source + date on every contact; final count matches the ask or the shortfall is explained.

**Demand-signal honesty** [prospecting demand-signals]: every shortlisted prospect links to at least one real public signal; label the
output "potential customer based on public signals", never "interested" or "has consented"; ten strong matches beat a long generic list;
the list is a hypothesis to validate in conversations.

**Claims reps can defend** [sales-enablement]: "why we win" needs evidence (win-loss, recordings, quotes, CRM reasons backed by one of
these), otherwise label it a hypothesis; competitor facts are dated and sourced ("not listed on their site" rather than "they don't have
it"), motives never stated as fact; always include where we lose.

**Live deal objection** [sales-enablement]: pin down who said it, their role, exact words, deal stage and what happens next; name the likely
concern behind it (if two readings fit, give the rep a question that separates them); give one response the rep can say as written
(acknowledge, address the real concern, one proof point, end with a question); use only proof the rep can stand behind, never an invented
stat or a buyer's competitor claim as fact ("half the price" may not be the same scope); say when not to fight and how to qualify out.

**Objection doc entries** [sales-enablement]: objection as heard, why they say it, response approach, proof point, follow-up question.
Categories: price, timing, competition, authority, status quo, technical. Two formats: one-screen live table and a detailed prep doc.

**Collateral shapes** [sales-enablement]: deck 10-12 slides as a story (problem, cost of problem, the shift, approach, 3-4 workflows,
proof, one case study, implementation, ROI, pricing, next steps; one idea per slide; tailor to technical / economic buyer / champion);
one-pager = problem, solution, 3 differentiators, one proof, CTA with a named contact, scannable in 30 s; battle card = when you'll see
them, why buyers consider them, where they're strong, where we win and for whom, discovery questions, top objections, when to walk away,
last verified date (ask which competitor if unclear: a polished card about the wrong one looks finished); demo after discovery, 3-4
workflows mapped to their pain; proposal 5-7 pages with the price easy to find; ROI calculator = their inputs -> annual ROI %, payback
months, 3-year value.

**RevOps defaults** [revops]: lifecycle Subscriber -> Lead -> MQL -> SQL -> Opportunity -> Customer -> Evangelist, each with entry/exit
criteria and an owner; scoring = fit + engagement + negative signals, MQL threshold typically 50-80/100, built on won/lost cohorts with a
frozen rule tested on a later holdout, recalibrated quarterly; pricing page visits outweigh blog reads; stage hygiene: required fields per
stage, stale-deal alert at 2x average time in stage, stage-skip alerts, no silent close-date pushes; pipeline coverage 3-4x quota;
directional benchmarks lead-to-MQL 5-15%, MQL-to-SQL 30-50%, SQL-to-opportunity 50-70%, LTV:CAC 3:1 to 5:1; dedupe weekly on email domain
+ company + phone; quarterly audit (merge dupes, re-verify stale emails, archive 12-month-inactive, check stage distribution).

**What runs without the user vs. what waits** [cold-email reply-handling + outbound-operator, tightened by the user's rules]
| Action | Claude alone | Waits for the user |
|---|---|---|
| Research, score, enrich from free sources, draft, update local `.agents/outbound/` files | yes | |
| Mark out-of-office, not-now reminders, suppression in local lists | yes | |
| Any message on any channel, including follow-ups and replies | | yes, each one (or an explicit standing approval recorded in the context doc) |
| Paid lookups, new tools, new sequences, new claims, new segments | | yes |
| Writes to a live CRM, sequencer or n8n routing | | yes, via the change protocol |
| Anything about pricing, discounts or legal terms | | the user only |

## When members disagree

| Conflict | Resolution |
|---|---|
| lead-intelligence claims to replace Apollo/Clay/ZoomInfo and requires Exa + X API; prospecting relies on licensed vendors | Neither is connected: use free/public sources and the user-supplied exports; recommend a paid tool in one line when it would clearly help, and wait for the user |
| lead-intelligence suggests LinkedIn via browser automation with a session cookie; prospecting bans LinkedIn scraping | No cookie-driven or bulk LinkedIn automation. The browser may view individual public profiles for a Tier 1 brief; audiences are defined in Sales Navigator by the user |
| cold-email: interest CTA, never a meeting ask first; investor-outreach: a direct, concrete next step | By audience: prospects get the soft interest CTA; investors and intro requests get one direct ask, because they expect it |
| Follow-up counts differ: cold-email 3-5, multichannel 4-7 emails + 3 LinkedIn, investor-outreach 3 touches, lead-intelligence "multichannel only with a reason" | Default 3-5 emails for prospects; the full multichannel cadence only for Tier 1 with the user's yes; investors stop after 3 touches |
| outbound-operator and reply-handling let an agent enroll Tier 3 contacts and send Tier 2 first touches alone | the user's rule wins: every message is approved by the user; the agent's solo actions are local bookkeeping only |
| revops scores email opens; cold-email turns open tracking off | Cold outbound never tracks opens (deliverability, and opens are unreliable); scoring uses clicks, replies, site and product behavior from opt-in channels |
| revops/reply-handling: answer within 5 minutes; drafts-only rule | Claude drafts at once and alerts the user; live speed-to-lead runs through the user's existing automation, not through this skill |
| cold-email lists SMS/WhatsApp as later-cadence channels; the user's businesses text consented leads at volume | SMS is never a cold channel here; consented-lead texting belongs to lifecycle-messaging and follows the carrier-filter lessons in House rules |
| sales-enablement "involve your top reps"; the user has no rep team | the user is the reviewer: draft from call notes, transcripts and the user's words, mark untested claims as hypotheses |
| lead-intelligence signal weights include follower count; audience-growth and prospecting say fit beats size | Keep influence at its small 10% weight; fit and signal decide Hot vs. Warm |

## Combine with

- **Sibling super-skills**: growth-strategy (context doc, customer research for the ICP, competitor dossiers for battle cards, the outbound
  operator loop), lifecycle-messaging (nurture for not-nows, consented SMS), audience-growth (creator, partner and journalist fit),
  copy-and-content (humanizer pass), docs-decks (decks, one-pagers, PDFs, investor materials), research-hub (deep account or market
  research), n8n-builder (routing and speed-to-lead automations), dashboard-studio (pipeline and outbound dashboards), think-and-decide.
- **Built-in skills**: `humanizer` (last pass on any message), `ppt-creator` / `pdf-creator` (decks, one-pagers, proposals),
  `anthropic-skills:xlsx` (ROI calculators, lead CSVs), `deep-research` (sourced Tier 1 briefs), `superpowers:brainstorming` (new plays).
- **Specialist agent prompts** (`~/.claude/skill-library/agents/voltagent/`): `08-business-product/sales-engineer.md` (technical demos,
  POCs, complex deals), `07-specialized-domains/email-deliverability-engineer.md` (domains, authentication, inbox placement),
  `10-research-analysis/data-researcher.md` (list sourcing and validation), `10-research-analysis/search-specialist.md` (finding people
  and signals), `08-business-product/business-analyst.md` (lifecycle and routing design), `08-business-product/legal-advisor.md`
  (CAN-SPAM/GDPR/CASL questions, proposal terms).

## House rules (the user)

- Drafts only: every cold email, follow-up, LinkedIn or X message, intro ask, investor email and reply waits for the user's yes; Claude never
  sends, and creates Gmail drafts only when asked.
- Paid data asks first: Exa, X API, Apollo, Clay, ZoomInfo, FullEnrich/LeadMagic, Hunter/Truelist credits, Firecrawl, visitor-ID tools;
  default to free and public sources.
- SMS is never a cold channel. Carriers filter texts with money or urgency wording (error 30007); keep texts neutral and hand texting
  work to lifecycle-messaging.
- No promised hand-offs: when a lead is upset or asks for a person, give the contact number from the prompt; never "someone will
  reach out".
- Live CRM, pipeline or routing changes (CRM, n8n or voice-agent platforms) follow the change protocol with a visual approval page, one card per change.
- Never print or paste API keys, CRM tokens or X credentials; they stay in a credentials file outside the repo.

## Members

| Member | Best at | Path |
|---|---|---|
| prospecting | ICP pass/fail, four branches, signals + freshness, tiers, verification, enrichment waterfall, compliance, lead sheets, demand-signal discovery | `members/prospecting/SKILL.md` |
| lead-intelligence | Signal-weighted people search, mutual ranking, warm-path types, voice-before-outreach, channel heuristic, untrusted-source rules, 4 sub-agent prompts | `members/lead-intelligence/SKILL.md` |
| social-graph-ranker | Bridge-score math with decay, second-order expansion and engagement bonus; warm vs. cold tiering | `members/social-graph-ranker/SKILL.md` |
| cold-email | Peer-voice cold copy, structures, subject lines, follow-ups, deliverability + stop-loss, LinkedIn, multichannel rules, plays, reply handling | `members/cold-email/SKILL.md` |
| sales-enablement | Decks, one-pagers, battle cards, objection docs, live deal objections, win-loss, demo scripts, ROI calculators, proposals, call scripts | `members/sales-enablement/SKILL.md` |
| revops | Lifecycle stages, MQL/SQL and SLAs, scoring with holdouts, routing, speed-to-lead, pipeline hygiene, CRM automation, deal desk, benchmarks | `members/revops/SKILL.md` |
| investor-outreach | Investor cold emails, warm intro blurbs, 3-touch follow-up, post-meeting updates, hard bans | `members/investor-outreach/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
