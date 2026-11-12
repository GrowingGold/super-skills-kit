---
name: local-seo
description: "Local search end to end: Google Business Profile (GBP, GMB) setup and optimization, map pack / 3-pack / Google Maps rankings, 'why am I not in the map pack', local SEO audits, geogrid scans (ARP, ATRP, SoLV), NAP citations and data aggregators, reviews (getting more, replies, fake reviews), GBP posts, suspensions and duplicate listings, local keywords and near-me queries, location / city / service-area pages, local content briefs, LocalBusiness schema, service-area businesses (SAB), multi-location and franchise SEO, GBP API, Apple Business Connect, Bing Places, local AI answers (AI Overviews, ChatGPT, Gemini, Copilot), local links and competitors, Local Services Ads (LSA, Google Guaranteed), map pack ads, geo-targeted local PPC, local reports, audits and proposals, plus the data tools LocalSEOData, Local Falcon, BrightLocal, Whitespark, Semrush, Ahrefs, DataForSEO, SerpApi, LSA Spy, Screaming Frog, Search Console and GA4."
members: [dispatch, brief, local-seo-audit, gbp-optimization, gbp-posts, gbp-suspension-recovery, gbp-api-automation, geogrid-analysis, review-management, local-citations, apple-business-connect, bing-places, local-keyword-research, local-content-strategy, local-content-briefs, local-landing-pages, local-schema, service-area-seo, multi-location-seo, local-competitor-analysis, local-link-building, ai-local-search, lsa-ads, local-search-ads, local-ppc-ads, local-reporting, client-deliverables, localseodata-tool, local-falcon-tool, lsa-spy-tool, serpapi-tool, semrush-tool, ahrefs-tool, brightlocal-tool, dataforseo-tool, whitespark-tool, google-search-console-tool, google-analytics-tool, screaming-frog-tool]
---

# Local SEO

One skill for getting a local business found and chosen: Google Business Profile and the map pack, geogrids, reviews,
citations, local pages and schema, service-area and multi-location setups, Apple and Bing, local AI answers, Local Services
Ads and local PPC, reporting and client deliverables, and the twelve data tools behind them. It merges the 39 skills of the
localseoskills pack. Load this file first, pick a mode, and open a member (`members/<member>/SKILL.md`) or a reference only
when a row or step points there. If the upstream localseoskills pack is installed, its pack-level docs
(`docs/how-local-search-works.md`, `docs/local-seo-glossary.md`, `tasks/`, `specs/approval-workflow.md`) can be read; never run its install scripts.

## Pick the mode

| Task looks like | Mode | Do / open |
|---|---|---|
| A named business or location comes up, "pick up where we left off", a scheduled task wrote output | BRIEF | Step 0. Structure, first-run questions, resume and session-log rules: `members/brief/SKILL.md` |
| "Audit my local presence", "what's wrong with my rankings", prospect audit, health check | AUDIT | Steps 1-3. Full 7-area checklist, duplicate workflow, vertical edge cases (healthcare, legal, home services, restaurants, multi-domain, managed platforms): `members/local-seo-audit/SKILL.md` |
| "Why am I not in the map pack", GBP setup, categories, hours, photos, description, attributes | GBP | Steps 2-4 + Core rules > GBP. Playbook and map-pack diagnosis: `members/gbp-optimization/SKILL.md` |
| "What should I post on Google", post calendar, offers, events | GBP POSTS | `members/gbp-posts/SKILL.md` (types, hook/body/CTA, 4 templates, calendar). Posting is a live write: drafts only |
| Suspended, disabled, "my listing disappeared", duplicate or practitioner listings, unauthorized edits | RECOVERY | Core rules > Suspension and duplicates; `members/gbp-suspension-recovery/SKILL.md`; duplicate workflow in `members/local-seo-audit/SKILL.md` |
| Geogrid, rank grid, ARP / ATRP / SoLV, heatmap, "where am I ranking" | GEOGRID | Steps 1-2 + Core rules > Geogrid. Decision trees, multi-scan synthesis, client translations: `members/geogrid-analysis/SKILL.md`; running scans: `references/tools.md` |
| More reviews, review replies, fake reviews, reputation, velocity | REVIEWS | Core rules > Reviews; industry platforms, vertical reply rules, removal process: `members/review-management/SKILL.md` |
| Citations, NAP consistency, directories, data aggregators, Apple Maps, Bing Places | CITATIONS | Core rules > NAP and citations; `members/local-citations/SKILL.md`, `members/apple-business-connect/SKILL.md`, `members/bing-places/SKILL.md` |
| Local keywords, near-me, keyword map, "what content should I build", content brief | KEYWORDS & CONTENT | Step 5 pipeline: `members/local-keyword-research/SKILL.md` -> `members/local-content-strategy/SKILL.md` -> `members/local-content-briefs/SKILL.md` |
| Location pages, city pages, service-area pages, LocalBusiness schema | PAGES & SCHEMA | Core rules > Pages, Schema; `members/local-landing-pages/SKILL.md`, `members/local-schema/SKILL.md` |
| No storefront, hide my address, "I go to the customer", showroom plus service area | SAB | Core rules > SAB; `members/service-area-seo/SKILL.md` |
| 10-500+ locations, franchise, bulk GBP, GBP API, automation, location data sync | MULTI-LOCATION | Core rules > Multi-location; `members/multi-location-seo/SKILL.md`, `members/gbp-api-automation/SKILL.md` |
| Who outranks me, competitor GBPs, local links, sponsorships, chamber, local PR | COMPETITORS & LINKS | Comparison matrix and spam to report: `members/local-competitor-analysis/SKILL.md`; link tactics: `members/local-link-building/SKILL.md` |
| "Show up in ChatGPT / AI Overviews for [service] in [city]", Gemini, Copilot, Siri | AI LOCAL | Core rules > AI local; `members/ai-local-search/SKILL.md`; prompt-sampling method: seo-suite (AI visibility mode) |
| Local Services Ads, Google Guaranteed, LSA leads and disputes, ads in the map pack, geo-targeted Google Ads | LOCAL ADS | Core rules > Local ads; `members/lsa-ads/SKILL.md`, `members/local-search-ads/SKILL.md`, `members/local-ppc-ads/SKILL.md`. Economics, tracking, kill/scale rules: ads-and-measurement |
| Monthly report, KPIs, ROI, multi-location rollup, QBR, "is this good?" | REPORTING | Step 7 + `references/benchmarks.md`; templates, stakeholder variants, hard conversations: `members/local-reporting/SKILL.md` |
| Audit report, prospect audit, AI visibility audit, proposal, SOW, onboarding doc, case study | DELIVERABLES | `members/client-deliverables/SKILL.md` (section structures for each); data comes from the other modes |
| "Which tool", any of the 12 tools by name, credits, MCP setup | TOOLS | `references/tools.md` (which tool for what, cost, ask-the user column), then the `members/<tool>-tool/SKILL.md` it names |
| Several asks at once, unsure what to load | route | Request-pattern table: `members/dispatch/SKILL.md` |
| Technical crawl/index work beyond local pages, non-local AI search (bot access, llms.txt), general schema, programmatic sets | hand-off | seo-suite super-skill |
| Ad account structure, bidding, tracking, GA4/GTM setup, attribution, decision thresholds | hand-off | ads-and-measurement super-skill (this skill keeps the local layer only) |
| Writing the page, post or reply copy; page converts poorly; dashboards; review-request SMS/email flows; Next.js JSON-LD code | hand-off | copy-and-content, conversion-lab, dashboard-studio, lifecycle-messaging, react-next-pro |

Modes stack. A new client runs BRIEF, AUDIT, GEOGRID, then GBP, REVIEWS and CITATIONS. A ranking drop runs GEOGRID (sudden-drop tree), then RECOVERY or GBP.

## Unified workflow

Run the steps that fit the mode; the order is the point. Brackets name the member each technique comes from.

### 0. Frame the business and open the brief
- **Business model first:** storefront, SAB, hybrid, or online-only (online-only is not eligible for a GBP; send it to seo-suite).
  Single or multi-location. Vertical, because healthcare, legal, financial, home services and restaurants change the rules
  for listings, reviews, directories and copy [gbp-optimization, local-seo-audit].
- **Canonical location record:** real-world name, address (kept private for an SAB), local phone, hours, URL, primary and
  secondary categories, Place ID, service areas. Every listing, page and schema block is checked against this one record
  [gbp-api-automation master database, multi-location-seo].
- **Brief:** look for `briefs/<brand-slug>/<location-slug>/location.brief.md` in the project folder. None: ask the five
  first-run questions one at a time (primary keyword, website, service radius, own business or client, where alerts go), create
  the folders (`reports/`, `scans/`, `drafts/`, `alerts/`) and a `_brand.brief.md`. Resume: read the brief and the newest file
  in each subfolder, summarize in 2-3 sentences, state the Next Action, ask whether to continue. Do not re-run a tool whose
  result in `scans/` is under 30 days old [brief].
- **Data plan before spending:** list what is free or owned (Search Console, GA4, GBP performance, the GBP dashboard, a manual
  Maps check), then the paid calls with a credit or cost estimate, and get the user's yes before any paid call (House rules).

### 1. Baseline before touching anything
Every later result must be attributable, so measure first [local-seo-audit, geogrid-analysis, local-reporting].
- **Tracking keywords:** 3-5, one per concept cluster, clear local-pack intent, tied to revenue services, spread across the
  service areas [local-content-strategy]. The branded name must rank #1 at the centroid; if it does not, stop and find the
  fundamental problem (duplicates, suspension, wrong pin) [geogrid-analysis].
- **Geogrid** per keyword, sized to the real service area (Core rules > Geogrid). Save the exact settings (place, keyword,
  grid, radius, center): trend reports only exist across identical settings [local-falcon-tool].
- **Owned data:** GBP impressions and actions (calls, directions, website clicks), Search Console queries per location page,
  GA4 conversions per location page. If GA4 conversion events are not configured, that is the first fix, because otherwise
  you can only report traffic, never leads [google-analytics-tool, google-search-console-tool].
- **Reputation and citations:** review count, rating, velocity, response rate; citation accuracy across the core directories.
- **Competitors:** top 3-5 map-pack businesses per keyword in a comparison matrix (category, reviews, rating, velocity,
  photos, posts in 30 days, domain authority, location page, schema, citations) [local-competitor-analysis].

### 2. Diagnose the binding constraint
Validate the scan before reading it: grid size fits the business type, radius fits market density, keyword matches what
customers type and the primary category, scan under 30 days old and newer than the last major GBP change. If any check fails,
note it and rescan before deep analysis [geogrid-analysis step 0]. Then fix in constraint order: (1) identity and eligibility
(unverified, suspended, duplicate, wrong pin, ineligible address), (2) customers cannot reach the business (wrong phone, hours,
URL), (3) relevance (primary category, services, a page for the query), (4) prominence (review flow, citations, links,
engagement) [seo-suite local reference, local-seo-audit priority order]. Do not add promotional content to a broken identity.

| Symptom | Check in this order | Route |
|---|---|---|
| Not in the pack at all | verified, suspended, category, website linked, location page exists | GBP, RECOVERY |
| Strong profile, SoLV under 40% | duplicates (name, owner/practitioner, phone, old address searches), category vs keyword, pin accuracy, suspension history, website disconnect (no NAP, schema, local content), listing under 6 months old, market density | RECOVERY, GBP, PAGES |
| Good ARP, low SoLV | Google does not tie the business to the wider area | service areas, area pages, area citations |
| ATRP about equal to ARP (no proximity boost) | relevance, not distance | primary category, dedicated service page, reviews naming the service |
| Strong near the pin, fades with distance | normal proximity curve | relevance and prominence in the weak zones |
| One direction weak | a competitor owns that zone, or the area is not associated | competitor report for that zone, area content and citations |
| Weak center, strong edges | pin or grid center wrong | verify the pin and the grid centroid |
| Sudden drop | GBP edits in the last 2 weeks, accepted user or Google suggested edits, new competitor, algorithm update, website change (CMS, lost pages, broken schema, HTTPS), review bombing, aggregator pushing old NAP, lost links | RECOVERY, CITATIONS, seo-suite |
| Outranked by a rival with fewer reviews | their category more specific, keyword in their name (report it), stronger citations or site, closer | GBP, COMPETITORS |
| Volatile scan to scan | NAP conflicts, duplicates, unauthorized edits, several changes at once | CITATIONS, step 4 |

[geogrid-analysis decision trees, gbp-optimization diagnosis, ahrefs-tool lost-link recovery]

### 3. Plan the fixes and present them
- **Finding card** for every issue: finding, impact (high/medium/low), evidence (tool, query, date, screenshot), exact fix,
  priority, plus a one-sentence plain-language translation ("Your phone number on Yelp differs from Google, so Google is less
  sure which listing is you") and the mode that fixes it [local-seo-audit].
- **Default roadmap** [gbp-optimization, client-deliverables 90-day plan]:
  - Weeks 1-2: primary category, every GBP field, 10+ real photos, reply to unanswered reviews, NAP on the site, LocalBusiness schema.
  - Month 1: posting cadence, a review-request system, Tier-1 listings (Apple, Bing, Yelp, Facebook), the location page, citation fixes.
  - Months 2-3: industry citations, service-area content, local links, video.
  - Ongoing: weekly reviews, posts and edit monitoring; monthly photos, insights and hours; quarterly competitor and category review.
- A 90-day target per finding (count plus velocity for reviews, SoLV per keyword for rankings) [local-seo-audit, review-management].
- Present on the user's review page: one card per change, current vs proposed side by side, reason, pick + note (House rules).

### 4. Change live listings safely
A live GBP is a production system with suspension risk [gbp-suspension-recovery, gbp-api-automation].
- One major field per change; never name, address and category together; stagger bulk edits across days; trial on a small
  batch first; avoid edits during known Google update periods.
- Screenshot the before state; log every change with its date in the brief, because step 6 correlates rankings with this log.
- Safe low-risk edits: hours, photos, posts at a normal cadence, review replies, descriptions, services and products.
  High-risk: name, category, address, bulk creation, templated mass content.
- Review Google-suggested edits promptly and watch for unauthorized changes daily (Falcon Guard, or a saved-baseline diff of
  name, address, phone, category, website, hours) [local-falcon-tool, tasks/m3-gbp-change-monitor].
- After a reinstatement, wait about 2 weeks before any edit, then re-optimize conservatively.
- Every write (GBP, Apple, Bing, directories, review replies, LSA) is a draft until the user says yes.

### 5. Build relevance: keywords -> concepts -> vehicles -> briefs -> pages
- **Seeds from the business, not a tool:** every service, every area served, top revenue services, competitor names and the
  customer's own words ("when someone calls, what do they say they need?") [local-keyword-research].
- **Expand, then mine the SERP for free:** related searches, People Also Ask, map-pack categories, whether ads, LSAs or an AI
  Overview appear, and full-sentence versions of the recurring questions (how people prompt an assistant) [local-keyword-research].
- **Cover all ten keyword categories:** core service, geo-modified, near-me, problem/symptom, qualifiers (urgency, cost,
  quality, comparison), questions, branded procedures and products, insurance and qualification, cross-border or bilingual,
  conversational/AI. Tag intent and prioritize Emergency > Transactional > Commercial > Informational.
- **Cluster into concepts and pick a vehicle** per cluster [local-content-strategy]: location page (transactional local intent,
  enough demand for unique content), GBP service entry (a service variant too thin for a page), GBP secondary category, blog/FAQ
  (research-phase questions, AI Overview candidates), pillar page (the broad topic to own), near-me (won by GBP prominence and
  proximity; no page, and say so to the client), or no action. Then a coverage-gap pass: missing, thin, duplicate (cannibalizing),
  misassigned.
- **GBP confirmations fall out of the map:** categories, services, attributes and description concepts to add.
- **Brief each piece** [local-content-briefs]: core concept in 1-2 sentences; 10-15 related concepts plus local-specific ones
  (climate, permits, water, neighborhoods); 10-15 required entities; a depth tier per concept (comprehensive 400-600 words,
  standard 200-300, brief 75-150, entity mention); 8-10 reader questions with 3-5 flagged for direct-answer format; GBP
  consistency check; natural NAP placement; schema; internal links with concept anchors; an H1/H2/H3 outline ending in a
  conversion section. Bulk order: pillar, primary location pages, supporting location pages, blog/FAQ.
- **Publish** with the page rules below, point the right GBP's website field at it, and rescan 2-4 weeks later [local-landing-pages].

### 6. Build prominence, then measure on the right clock
- **Order:** review flow (steady, every customer asked), Tier-1 listings and aggregators, industry directories, local links
  (chamber, associations, sponsorships, local press, suppliers, .edu/.gov resource pages), brand mentions for AI
  [review-management, local-citations, local-link-building, ai-local-search].
- **Rescan with identical settings**, compare ARP, ATRP and SoLV, and tie every move to the change log and to outside events
  (algorithm updates, seasonality, competitor moves). Three months of data before calling a trend [geogrid-analysis].
- **Expected lags:** citations and aggregators 4-8 weeks, links 4-8 weeks, new pages 2-4 weeks, service-area tightening 2-4
  weeks, schema errors visible in Search Console within about 2 weeks, LSA verification 2-6 weeks; recheck consolidated
  duplicates monthly for 3 months because aggregators resurrect them (`references/benchmarks.md` has the full timing table).
- Two scans with no movement after a fix means the constraint is elsewhere: go back to step 2.

### 7. Report so the next month has work
- Every report answers: are we improving (trend), what is working (attribution), what next (action) [local-reporting].
- Lead with SoLV in plain words ("visible to 62% of nearby searchers, up from 48%"), show heatmaps, translate ARP and ATRP
  ("when you show up, you are usually 6th or 7th; most people look at the top 3"), name competitors [geogrid-analysis].
- Benchmark against the client's own history first, competitors second, industry figures third. Never grade a metric on a single
  data point; leave missing data blank with the source named, never back-filled [local-reporting QA].
- GBP call clicks have been falling across many profiles even where rankings hold; show website clicks and site conversions
  next to calls and do not present the decline as an SEO failure [local-reporting].
- Close the loop: top 3 priorities become tasks with owners and dates, and next month's report opens with their results.
- Multi-location: portfolio rollup, location scorecard with a 0-100 health score, deep dive only for flagged locations
  (`references/benchmarks.md`).

## Core rules and checklists

### Ranking model [gbp-optimization, pack doc how-local-search-works]
- Three pillars: proximity (cannot control), relevance (the primary category is the strongest lever after proximity), prominence
  (reviews, citations, links, engagement; the tiebreaker in competitive markets). Map pack and organic are separate algorithms
  that share website and link signals.
- Being open at search time is a ranking factor (since late 2023), and visibility fades in the final hour before closing:
  real, extended hours help; fake 24/7 hours backfire.
- Review recency and steady velocity beat total count. Entity consistency across GBP, site, citations, socials and schema
  concentrates signals; conflicting NAP or duplicate listings split them.
- Never promise a top-3 placement or a fixed uplift [seo-suite local reference].

### GBP fields [gbp-optimization, local-seo-audit]
- **Name:** the real-world name, character for character; keywords in the name are the top suspension cause. Report rivals who stuff.
- **Category:** primary = what the business is, most specific available, checked against top-ranking rivals; add every
  genuinely applicable secondary (up to 9), never aspirational ones.
- **Address and phone:** USPS formatting with consistent suite notation; local number as primary, the same one everywhere.
- **Hours:** accurate regular, holiday (set before the holiday) and "more hours" per service.
- **Website:** the most relevant page (home for one location, the location page for many), with a UTM tag such as
  `?utm_source=google&utm_medium=organic&utm_campaign=gbp` so GA4 can attribute it.
- **Description** (750 characters): what and where, key services, differentiators, CTA; no URLs, phone numbers, caps or stuffing.
- **Services and products** complete with descriptions; **attributes** all that apply (accessibility, ownership, free estimates,
  emergency, booking, payments).
- **Photos:** 10-15 to start, 2-3 new per month, no stock; cover, logo, interior 3+, exterior, team, work. Video 30 s-3 min.
- **Posts** 1-2 a week as maintenance on an optimized profile, never as the first fix [gbp-posts].
- **Q&A:** users can no longer ask questions on a GBP; answer whatever exists and put real FAQs on the website.
- **Messaging** only if someone staffs it; link social profiles.

### NAP and citations [local-citations, brightlocal-tool, whitespark-tool, local-seo-audit]
- Name, address, phone and URL identical everywhere ("Ste" or "Suite", pick one). A call-tracking number must also be the one on
  the website; otherwise keep the main number as primary.
- Tiers: (1) GBP, Apple Business Connect, Bing Places, Facebook, Yelp; (2) aggregators Data Axle, Neustar/Localeze, Foursquare;
  (3) BBB, YP, Angi, Thumbtack, MapQuest, Manta and similar; (4) industry directories (Healthgrades, Avvo, Houzz, Zillow...);
  (5) chamber, associations, city directories.
- Fix order: Tier 1, then aggregators (fixing at the source propagates downstream; Foursquare and Yelp feed Apple Maps), then
  high-authority sites with wrong data, then duplicates, then the rest. Correct and merge before creating new listings.
- Find existing citations free: search `"business name" "phone"` and `"business name" "address"`; record URL, NAP, status.
- Citations are not links: mass directory submission is not link building [local-link-building].
- Never publish a hidden SAB home address to satisfy a citation form [seo-suite local reference].

### Reviews [review-management, whitespark-tool, seo-suite local reference]
- Ask every customer with a genuine experience: in person first, then SMS or email 1-3 days after service with the direct link
  (`https://search.google.com/local/writereview?placeid=<PLACE_ID>`); a steady weekly flow, never bursts.
- Never: buy reviews, incentivize, gate (ask only happy customers, or skip unhappy ones), script the wording, write them
  in-house, use an in-office kiosk (same IP), or solicit on Yelp (Yelp penalizes asking).
- Reply to every review. Positive within 24-48 h: thank by name, refer to the service, vary the wording. Negative within 4-12 h:
  acknowledge, apologize for the experience, take it offline with a named contact, never argue.
- **Vertical overrides beat the templates:** healthcare (HIPAA) and legal (privilege) replies never confirm the person is a
  patient or client and never mention care, case or treatment details, even if the reviewer did. Financial services: no account
  or debt details.
- Fake or spam reviews: flag, then report through the removal form with evidence, reply calmly for the public record; a
  genuine unfavorable opinion is not removable.
- Velocity target = match or beat the top-3 map-pack rivals; fallback tables in `references/benchmarks.md`.

### Suspension and duplicates [gbp-suspension-recovery, local-seo-audit]
- Types: soft (visible to the owner), hard (removed from Maps), pending review/verification hold.
- Causes: keyword-stuffed name, virtual office/UPS box/co-working address, duplicates, ineligible business, misleading category,
  bursts of major edits, NAP conflicts, competitor reports.
- Reinstatement: find the cause, fix every issue, then one request with documents (license, utility bill or lease, signage
  photos, vehicle and uniform photos for an SAB, tax documents); follow up after 7 business days; escalate through support,
  then the Product Expert forum; never spam requests.
- Duplicates: search name variants, owner and practitioner names, the raw phone number, the address and old addresses; catalog
  each (claimed, reviews, categories, relationship). Merge true duplicates; keep distinct locations and entities separate;
  Google never transfers reviews, so with 20+ reviews on the "wrong" listing, keep the strongest one and correct it.

### Geogrid [geogrid-analysis, local-falcon-tool, localseodata-tool]
- ARP = average rank over all points (good under 5, needs work over 10); ATRP = average of the best positions (the ceiling);
  SoLV = share of points where the business appears (the client-facing number).
- Size the grid to the real service area: too small looks falsely good, too big looks falsely bad. SABs need wider grids;
  their ranking anchors on the hidden address and service-area centroid.
- Run three radii (for example 3, 7 and 15 miles) once to see the falloff curve; compare SoLV across keywords to spot category
  misalignment (a secondary keyword outranking the primary).
- Never hand raw numbers to anyone: every scan ends in 3-5 actions. Tables and costs: `references/benchmarks.md`, `references/tools.md`.

### Pages [local-landing-pages, multi-location-seo, screaming-frog-tool, google-search-console-tool]
- Types: physical location (`/locations/buffalo-ny/`: full NAP, map, hours, directions, team, unique photos and reviews),
  service-area (`/plumbing/orchard-park-ny/`), service x location (highest intent).
- Template: title `[Service] in [City, ST] | [Brand]`; H1 `[Service] in [City]`; hero with CTA and trust, overview, why us,
  service details, local context, local reviews, location FAQ, CTA with click-to-call.
- Uniqueness or no page: local conditions, permits, building types, neighborhoods, local jobs and photos, area reviews, local
  data and partnerships. A city-name swap is a doorway page.
- Scale: hand-write up to about 20 pages; 20-100 = template plus required unique sections with 300+ unique words; 100+ only
  programmatic with a real per-page data source and real demand (seo-suite Programmatic mode).
- Hub and spoke: service hub -> area spokes, spokes link nearby areas, everything within 3 clicks, breadcrumbs with schema.
- Crawl checks: duplicate titles or metas, under 300 words, 0-1 inlinks (orphan), non-self canonicals, noindex, missing from
  the sitemap; Search Console "Discovered - currently not indexed" on location pages usually means thin content.

### Schema [local-schema, local-seo-audit, seo-suite schema rules]
- JSON-LD that matches the GBP exactly (name, address, phone with country code, hours, geo), most specific `@type`
  (Plumber, Dentist, HVACBusiness, Attorney, MedicalClinic...), `areaServed`, `sameAs`, services via `hasOfferCatalog`.
- Multi-location: one block per location page with a unique `@id` (`/locations/buffalo-ny/#business`); the homepage
  `Organization` lists them under `department`. SAB: omit `address`, list `areaServed`.
- Mark up only what is visible on the page. Do not copy the GBP star rating into `aggregateRating`: reviews must be collected
  on the page itself, and Google does not show self-serving review stars for LocalBusiness anyway.
- `FAQPage` only for a real visible FAQ, as parsing context; never sold as a rich result (seo-suite has the retirement dates).
- `curl` and fetchers strip `<script>`; verify JSON-LD in a rendered browser or the Rich Results Test before reporting "no schema".

### SAB [service-area-seo]
- Verify with the real address, then hide it and set service areas (up to 20) by city, county or ZIP, specific not state-wide.
- Hiding the address costs ranking (a large Dec 2025 study found a negative correlation), yet showing a home address or using a
  virtual office is worse. Compensate: area pages (the biggest lever), area citations, reviews that mention the area, posts
  naming areas, `areaServed` schema, genuine extended hours.
- Test tightening service areas to the 3-5 most important cities, with a geogrid before and 2-4 weeks after.
- Hybrid (showroom plus service area): show the address and set service areas only if customers are really served there.

### Multi-location and API [multi-location-seo, gbp-api-automation, gbp-posts]
- Organization-level GBP access with roles (Owner corporate, Manager regional, Communications Manager local); quarterly access audit.
- Tiered effort: foundation for every location, optimization for priority locations, advanced for competitive markets; fix
  the worst performers first, since they move the portfolio most.
- Master location database (internal ID, Place ID, canonical NAP, E.164 phone, categories, service areas, hours, status) synced
  both ways: push changes, read back to catch edits made by Google or users.
- API patterns: read-compare-patch only changed fields and log; templated posts with location variables and local photos,
  never identical posts everywhere at once; exponential backoff and quota requests.
- Alert priorities: P0 suspension, verification loss, name change; P1 negative review, address or hours edit; P2 performance
  drop; P3 photo, attribute or category suggestions.
- Build vs buy: build only for 50+ locations with custom needs and dev capacity; otherwise a platform (Yext, Uberall, BrightLocal...).

### Apple and Bing [apple-business-connect, bing-places]
- Claim both; they take minutes and most rivals skip them. Apple feeds Siri and Apple Maps (pulls heavily from Yelp and
  Foursquare: fix those first; set action links; post Showcases monthly). Bing feeds Copilot and, per the members, ChatGPT
  search: import from Google, then fix categories that did not map, and recheck quarterly for drift.
- Google stays the priority; these are supplementary.

### AI local [ai-local-search, client-deliverables, localseodata-tool]
- Foundations first: the same GBP, review, citation and content work feeds AI answers. Then add complete schema, factual
  service and location pages (services listed with descriptions, explicit coverage areas, prices where possible, credentials),
  multi-platform reviews that name services and areas, brand mentions on local news, blogs and "best of" lists, Bing Places.
- Measure by prompt sampling: natural full-sentence prompts with situation and constraints, several phrasings per need, each run
  several times per engine, mention rate recorded with n (seo-suite AI visibility method); report AI search demand next to
  mentions, because no demand yet is a monitor item, not a gap [client-deliverables].
- Treat the members' AI statistics (share of local queries with AI Overviews, ChatGPT traffic share, Gemini overlap with the
  pack) as directional and dated; do not quote them to a client without re-checking.

### Local ads [lsa-ads, local-search-ads, local-ppc-ads, lsa-spy-tool]
- Three formats: LSA (pay per lead, top of page, verified badge, no keyword control), map-pack ads (Google Ads with location
  assets linked to the GBP, pay per click), and geo-targeted search/PMax.
- LSA: answer every call (return a missed one within 15 minutes, messages within an hour), keep service areas tight, broaden
  real hours, mark booked leads, dispute invalid leads within 30 days, track answer rate and CPL. Rank drivers: reviews and
  responsiveness (joint top), proximity, hours, budget, complaint history, active badge.
- Local PPC: switch location targeting to "Presence: people in or regularly in" (the default "presence or interest" pays for
  out-of-area searchers); separate campaigns per service x market; local negatives (jobs, salary, DIY, how to, free unless
  offered, unserved towns sharing a name); send traffic to the matching service or location page, never the homepage; call
  tracking is mandatory because calls are the main local conversion.
- Map-pack ads depend on GBP quality: rating, review count, open-now and category shown in the ad.
- Everything else (economics, bidding, conversion setup, attribution, kill and scale rules) follows ads-and-measurement, and
  every account change is a draft for the user.

### Reporting and deliverables [local-reporting, client-deliverables]
- Report layers: portfolio rollup (top 5, bottom 5, totals), location scorecard (health score, green/yellow/red), deep dive on demand.
- Stakeholder cut: owner (calls and bookings, 1-2 pages), marketing manager (positions, competitors, ROI, 3-5 pages), C-suite
  (one page, YoY, revenue language), franchisee (one-page scorecard vs the franchise average).
- ROI only as `GBP actions x close rate x average customer value - cost`, with measured and estimated parts labelled.
- Deliverables: audit, prospect audit (public data only; grade only what was measured, "not assessed" otherwise; exactly three
  ranked opportunities), AI visibility audit (lead with demand), proposal/SOW (explicit out-of-scope list), onboarding (access
  checklist: GBP manager, GA4, Search Console, CMS, Ads), strategy roadmap, case study (honest timeline). Executive summary
  first; competitor context on every metric; one clear next step.

## When members disagree

| Conflict | Resolution |
|---|---|
| brief "run the initial audit automatically, don't ask permission" (8 paid calls, about 220 credits) and "offer scheduled monitoring" vs the user's paid-tool rule | Ask first with a credit estimate; start from free and owned data. Scheduled monitors multiply cost (weekly 7x7 scan = ~98 credits per keyword per location per week): one explicit budget yes per setup |
| gbp-optimization, local-seo-audit, service-area-seo, lsa-ads, local-search-ads, multi-location-seo "geogrid -> Local Falcon (only option)" vs localseodata-tool, geogrid-analysis "LocalSEOData geogrid_scan is the default" | Stale "only option" lines. One-off scans: any connected scanner; trends, campaigns, GBP change watch and AI-platform grids: Local Falcon; custom builds: DataForSEO. Pick by need and cost in `references/tools.md`, not by the pack's vendor default |
| Pack-wide "LocalSEOData is the DEFAULT data source, check it first" | The pack's author also sells LocalSEOData; treat the default as vendor framing. For the user: owned data, then free tools, then the cheapest paid tool that answers the question |
| lsa-ads "responsiveness is the biggest factor" vs lsa-ads next steps, dispatch, lsa-spy-tool "reviews are #1" | Reviews and responsiveness are joint top tier; LSA Spy tells which is the gap (fewer reviews but higher rank = responsiveness or proximity) |
| Grid sizes: geogrid-analysis (plumber 7x7-9x9, regional HVAC 11x11-13x13) vs local-falcon-tool (HVAC/plumber 9x9-11x11 at 7-15 mi) vs LocalSEOData max 9x9 | Size to the real service area; above 9x9 use Local Falcon or a wider radius at 9x9; never change settings between scans you want to compare |
| SoLV bands: geogrid-analysis 3 bands (70/40) vs local-reporting 5 bands (70/50/30/15) | Reports use the 5 bands; the 3 bands are internal shorthand |
| Review velocity targets by size (review-management), by vertical (whitespark-tool), by SMB vs multi (local-reporting) | Target the top-3 rivals' velocity from real data; the tables are fallbacks; steady beats bursts |
| whitespark-tool "don't send review requests to known unhappy customers" vs review-management "don't gate" and Google policy | Dropped: selective asking is gating. Ask everyone; resolve unhappy customers through service recovery |
| review-management "add a keyword/location in replies", service-area-seo "encourage customers to mention their city" vs policy against prescribed wording | Replies may mention the service or area naturally; never script customers' words. Ask them to describe their experience |
| review-management positive-reply template (name the service) vs HIPAA/privilege rules in the same member and local-seo-audit | Vertical rules override every template |
| gbp-optimization, local-seo-audit, ai-local-search, local-competitor-analysis "seed / populate Q&A" vs gbp-optimization "users can no longer ask questions" | Q&A is retired for new questions: drop seeding tasks and Q&A checks, answer what exists, put FAQs on the site |
| local-schema template with `aggregateRating` from GBP numbers vs schema rules (mark up only on-page content, no self-serving stars) | Drop `aggregateRating` unless the reviews are collected and shown on that page; never mirror GBP stars |
| local-content-briefs "FAQPage / HowTo schema", ai-local-search "FAQ schema" vs Google's retired FAQ and HowTo rich results | FAQPage only for a visible FAQ as parsing context; no HowTo promises; never sold as rich results (seo-suite) |
| local-schema "MedicalBusiness" vs local-seo-audit "MedicalOrganization" for practices | Use the most specific LocalBusiness subtype (Dentist, Physician, MedicalClinic); MedicalOrganization alone is not a LocalBusiness |
| Word counts: local-landing-pages 800-1,500 standard, multi-location 300+ unique, local-content-briefs "length is a byproduct", pillar 2,500-4,000 | Concept coverage sets length; 300 unique words is the floor for templated location pages; under 300 is flagged thin in crawls |
| local-content-strategy "page if 50+ searches, GBP service under 50, nothing under 10" vs local-keyword-research "tools undercount local, never drop a real intent for 0 volume" | Thresholds are defaults; override with Search Console impressions, CPC and conversion value |
| gbp-posts frequency (1/week min, 2-3 recommended, daily OK) vs gbp-optimization 1-2/week vs gbp-api-automation 1-3/location/week | 1-2 a week per location after the profile is optimized; never identical posts across locations at once |
| gbp-optimization, local-seo-audit, gbp-posts "geo-tag photo EXIF" | Likely myth (Google strips EXIF on upload): harmless, never billed or prioritized |
| gbp-optimization, gbp-posts, pack doc "social signals are a confirmed ranking factor (2026)" | Unsourced: link and keep socials active for presence; no ranking promise |
| review-management "Google confirms responses are a ranking factor", "photo reviews worth 3-5x" | Reply to every review for trust and conversion; drop the ranking claim and the multiplier |
| apple-business-connect "Apple Maps has no own review system" | Likely outdated (Apple Maps collects its own ratings and photos); check Apple's current docs; the Yelp advice still stands |
| lsa-ads, lsa-spy-tool badge names "Google Guaranteed / Google Screened" | Badge naming may have changed; check current LSA docs before writing client copy |
| client-deliverables "Core Web Vitals LCP, FID/INP" | FID is retired; use INP (under 200 ms) |
| local-search-ads "Local Campaigns (legacy)" | Merged into Performance Max; plan PMax with store goals |
| local-ppc-ads bidding and benchmarks vs ads-and-measurement thresholds | Local geo rules stay here; bidding steps, kill/scale gates and benchmark discipline come from ads-and-measurement |
| local-competitor-analysis -> "map-pack-optimization", local-link-building -> "local-content" | Skills that don't exist; routed to GBP and KEYWORDS & CONTENT modes |
| client-deliverables pricing psychology ("anchor high", "filter tire-kickers") | Agency mode only, when the user sells local SEO; never for the user's own businesses |

## Combine with

- **Super-skills:** seo-suite (technical audits, crawl/index beyond local pages, non-local AI visibility and its prompt-sampling
  method, general schema rules, programmatic page sets; its Local mode hands off here), ads-and-measurement (account economics,
  GA4/GTM and call tracking, UTMs, attribution, decision thresholds for local PPC and LSA budgets), copy-and-content (page copy,
  posts, review replies; humanizer pass), conversion-lab (location pages that must turn visitors into calls), dashboard-studio
  (report dashboards), lifecycle-messaging (review-request SMS/email flows), react-next-pro (Next.js JSON-LD and metadata),
  n8n-builder and supabase-postgres-pro (scheduled pulls and report pipelines), docs-decks (PDF audits and proposals),
  research-hub (market facts).
- **Built-in skills:** `schedule` (recurring monitors, after the user approves the credit budget), `dataviz` (heatmaps, trend
  charts), `artifact-design` + `artifact-capabilities` (review pages that save the user's picks), `claude-in-chrome` or the Playwright
  MCP (render pages, read JSON-LD, check a listing when no API covers it), `deep-research` (cited market research), `humanizer`
  (posts and replies), `superpowers:verification-before-completion` (before saying a fix is live).
- **Agent prompts** (`~/.claude/skill-library/agents/voltagent/`; haiku for lookups; hand over the data, not your conclusion):
  `07-specialized-domains/seo-specialist.md` (independent site audit), `10-research-analysis/competitive-analyst.md` (rival
  matrix), `08-business-product/content-marketer.md` (content calendar from the concept map), `05-data-ai/data-analyst.md`
  (recompute a report from raw exports), `07-specialized-domains/hipaa-compliance.md` (healthcare review replies),
  `08-business-product/wordpress-master.md` (WordPress location pages and schema plugins).

## House rules

- Paid tools ask first: LocalSEOData, Local Falcon, BrightLocal, Whitespark, Semrush, Ahrefs, DataForSEO, SerpApi beyond its
  free quota, LSA Spy, a Screaming Frog licence, and any new MCP server for them (vendor-first, read it before enabling). Give a
  credit or cost estimate; recurring monitors need one explicit budget yes.
- Live writes ask first and start as drafts on a review page: GBP edits, posts, photo uploads, review replies, API bulk changes,
  Apple and Bing edits, citation submissions, review-request sends, LSA budgets, disputes and lead status, ad changes, client
  emails. One card per change with current vs proposed, the user picks.
- APIs first: GBP and Business Profile Performance APIs, Search Console API, GA4 Data API and connected tool MCPs before a
  browser; Bing Places and Apple Business Connect dashboards only where no API covers the task, saying why.
- Conversion beats rankings: judge every change by calls, bookings, direction requests, form leads or purchases, not SoLV alone;
  page and section choices need conversion evidence.
- Live profiles follow the change protocol: prove the problem with real data, game out the impact, present, then watch the
  first real results after the change.
- Briefs and client data stay in the project folder (gitignored), never in a skill repo; no API keys, customer names or phone
  numbers in briefs, posts or replies.
- Regulated verticals (law firms, debt and lending brands): attorney-advertising and financial rules apply to
  titles, posts and replies, and replies never confirm a client relationship. Review requests by SMS go through
  lifecycle-messaging's consent and carrier rules.

## Members

| Member | Best at | Path |
|---|---|---|
| dispatch | Request pattern -> which modes and data calls to combine | `members/dispatch/SKILL.md` |
| brief | Persistent per-location state: first-run questions, resume, session log, lessons flywheel | `members/brief/SKILL.md` |
| local-seo-audit | 7-area audit checklist, duplicate-listing workflow, vertical edge cases, client translations, finding -> skill bridges | `members/local-seo-audit/SKILL.md` |
| gbp-optimization | Ranking signal model, field-by-field GBP rules, map-pack playbook by week, diagnosis | `members/gbp-optimization/SKILL.md` |
| gbp-posts | Post types, hook/body/CTA, templates, calendar, multi-location posting | `members/gbp-posts/SKILL.md` |
| gbp-suspension-recovery | Suspension types and causes, prevention, reinstatement documents, escalation, timelines | `members/gbp-suspension-recovery/SKILL.md` |
| gbp-api-automation | GBP API landscape, safe vs risky API operations, master data sync, alert priorities, build vs buy | `members/gbp-api-automation/SKILL.md` |
| geogrid-analysis | ARP/ATRP/SoLV, scan validation, patterns, decision trees, multi-scan synthesis, client translations | `members/geogrid-analysis/SKILL.md` |
| review-management | Recency over volume, ask framework, industry review platforms, vertical reply rules, fake-review removal | `members/review-management/SKILL.md` |
| local-citations | NAP rules, 5 citation tiers, audit and cleanup order, multi-location tracking | `members/local-citations/SKILL.md` |
| apple-business-connect | Apple Maps claiming, action links, Showcases, Yelp/Foursquare dependency | `members/apple-business-connect/SKILL.md` |
| bing-places | Import from Google, Bing categories, Copilot visibility, bulk upload | `members/bing-places/SKILL.md` |
| local-keyword-research | Ten local keyword categories, free SERP mining, combinatoric matrix, intent priority, keyword map | `members/local-keyword-research/SKILL.md` |
| local-content-strategy | Concept clusters, content-vehicle decision logic, geogrid keyword selection, GBP confirmations | `members/local-content-strategy/SKILL.md` |
| local-content-briefs | Semantic briefs: concept depth tiers, local entities, question mapping, AI-answer formatting | `members/local-content-briefs/SKILL.md` |
| local-landing-pages | Page types, template, uniqueness strategies, hub and spoke, scale thresholds | `members/local-landing-pages/SKILL.md` |
| local-schema | LocalBusiness JSON-LD template, @type table, multi-location @id, SAB markup, validation | `members/local-schema/SKILL.md` |
| service-area-seo | SAB GBP setup, hidden-address trade-off, service-area tightening test, hybrid rules | `members/service-area-seo/SKILL.md` |
| multi-location-seo | Three-tier management, access roles, data hygiene, per-location KPIs and segmentation | `members/multi-location-seo/SKILL.md` |
| local-competitor-analysis | Per-competitor signal audit, comparison matrix, leapfrog gaps, spam to report | `members/local-competitor-analysis/SKILL.md` |
| local-link-building | Community, sponsorship, media, partner, .gov/.edu link sources, outreach rules, quality table | `members/local-link-building/SKILL.md` |
| ai-local-search | How AI engines pick local businesses, per-platform notes, AI-ready content and reviews | `members/ai-local-search/SKILL.md` |
| lsa-ads | LSA eligibility, verification, ranking factors, responsiveness playbook, disputes, metrics | `members/lsa-ads/SKILL.md` |
| local-search-ads | Ads inside the map pack: location assets, campaign types, GBP quality effect, negatives | `members/local-search-ads/SKILL.md` |
| local-ppc-ads | Geo-targeting settings, service x market structure, local negatives, landing pages, call tracking | `members/local-ppc-ads/SKILL.md` |
| local-reporting | Report structure, three-layer multi-location model, health score, benchmarks, QA checklist, hard conversations | `members/local-reporting/SKILL.md` |
| client-deliverables | Audit, prospect, AI-visibility audit, proposal, onboarding, strategy and case-study templates; pricing | `members/client-deliverables/SKILL.md` |
| localseodata-tool | LocalSEOData endpoints, location formats, credit costs, combined workflows | `members/localseodata-tool/SKILL.md` |
| local-falcon-tool | Geogrid scans, trend reports, campaigns, Falcon Guard, review analysis, credit guards | `members/local-falcon-tool/SKILL.md` |
| lsa-spy-tool | LSA market rankings, appearance frequency, ranking changes | `members/lsa-spy-tool/SKILL.md` |
| serpapi-tool | Live SERP snapshots, engines, PAA and AI Overview extraction, searcher-location simulation | `members/serpapi-tool/SKILL.md` |
| semrush-tool | Keyword Magic, keyword gap, competitor organic research, site audit, position tracking | `members/semrush-tool/SKILL.md` |
| ahrefs-tool | Link profiles, link intersect, lost links, anchor distribution, Content Explorer | `members/ahrefs-tool/SKILL.md` |
| brightlocal-tool | Citation tracker and accuracy bands, aggregator priority, review monitoring, white-label reports | `members/brightlocal-tool/SKILL.md` |
| dataforseo-tool | Bulk SERP, keyword and business data, custom grid builds, pay-per-task cost control | `members/dataforseo-tool/SKILL.md` |
| whitespark-tool | Citation Finder, managed citation building, Reputation Builder, beta grid and rank-tracker APIs | `members/whitespark-tool/SKILL.md` |
| google-search-console-tool | Ground-truth organic clicks, CTR-by-position check, index coverage for location pages | `members/google-search-console-tool/SKILL.md` |
| google-analytics-tool | Local conversion events, GBP UTM attribution, geographic and source analysis | `members/google-analytics-tool/SKILL.md` |
| screaming-frog-tool | Location-page crawl audit, custom extraction of NAP and JSON-LD, duplicate and orphan detection | `members/screaming-frog-tool/SKILL.md` |

If a member folder is missing (not installed), work from this file alone.
