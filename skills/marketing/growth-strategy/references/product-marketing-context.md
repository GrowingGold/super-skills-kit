# The product-marketing context doc (shared by every marketing super-skill)

One file per brand or product holds the foundation every marketing task needs: product, audience, ICP, competitors, voice, approved
claims, approvals and learnings. It exists so the user never explains the same business twice. growth-strategy owns its structure and
versioning; every marketing super-skill reads it first.

Merged from: product-marketing (sections, template, versioning, Learnings), marketing-plan (economics, team, stage, quality gate),
customer-research (verbatims with confidence, provisional personas), competitor-profiling (observed vs inferred, dated dossiers),
prospecting (ICP pass/fail, disqualifiers, signals), sales-enablement (claims reps can defend, where we lose), marketing-loops outbound
operator (approved claims), influencer-marketing and referrals (disclosure and redlines), and the user's approval rules.

## Where it lives (lookup order)

1. `<project>/.agents/product-marketing.md` (canonical; every member skill already looks here).
2. `<project>/.claude/product-marketing.md` or the legacy `product-marketing-context.md` in either folder: read it, then offer to move it
   to `.agents/product-marketing.md`.
3. Brand with no repo yet: `~/marketing-plans/<brand-slug>/product-marketing.md` (slug = lowercase `[a-z0-9-]`, reject `..`, `/` and
   absolute paths). Move it into the repo's `.agents/` when one exists.

One doc per brand. Never mix two brands in one file; when a task names a brand, load that brand's doc only.

### Where things live (index this in the doc's "Artifacts" line)

| Artifact | Default location | Written by |
|---|---|---|
| Context doc | `<project>/.agents/product-marketing.md` | growth-strategy |
| Marketing plans | `~/marketing-plans/<slug>/` (`progress.md`, `sections/`, `final_plan.md`) | growth-strategy Plan mode |
| Competitor dossiers | `<project>/competitor-profiles/` (+ `raw/<slug>/<date>/`) | growth-strategy Competitor mode |
| Outbound brief, claims, plays, suppression | `<project>/.agents/outbound/` | outbound-sales |
| Loop state and logs | `<project>/.agents/loops/` | growth-strategy Loops mode |
| Custom council advisors | `<project>/.agents/advisors/` | growth-strategy Council mode |

## Read-first contract (for every marketing super-skill)

1. **Read before asking.** Load the doc at the start of any marketing task; ask the user only for what the task needs and the doc lacks.
2. **Cite, don't restate.** Use the ICP, voice, claims and redlines as written. If the task needs a claim that is not in Approved Claims,
   the draft waits for the user instead of inventing one.
3. **Respect Approvals.** The Approvals section is the gate for anything that sends, posts, publishes, spends, buys, calls or changes a
   live system. Absent an entry, the answer is "ask the user".
4. **Propose, never write silently.** A skill that learns something (finished test, new objection, new verbatim, competitor change)
   proposes the edit or a Learnings row; it lands after the user's yes, with a version bump and a changelog line.
5. **Missing doc?** Hand off to growth-strategy Step 0 (auto-draft) or, for a quick task, proceed on stated assumptions and list them at
   the end as proposed context entries.

### Section owners (who proposes updates)

| Section | Primary updater |
|---|---|
| Product, Economics, Goals, Approvals | growth-strategy (from the user) |
| ICP checklist, Personas, Customer Language | growth-strategy customer research; outbound-sales adds ICP disqualifiers it discovers |
| Competitive Landscape | growth-strategy competitor research; outbound-sales win-loss adds "where we lose" |
| Brand Voice | brand-studio (deep extraction), summary lives here |
| Approved Claims / Proof | whoever has the evidence; the user approves each new claim |
| Channels & Accounts | audience-growth, lifecycle-messaging, ads-and-measurement |
| Paid Ads | ads-and-measurement |
| Compliance & Redlines | any skill that hits a rule; lifecycle-messaging owns SMS rules |
| Learnings | any skill, via proposal |

## Auto-draft procedure (new doc)

1. Read: repo README, homepage/landing copy, product or store data (titles, descriptions, prices), meta descriptions, about page, any
   `research/` folder, the brand's notes file, existing plans or dossiers.
2. Draft every section you can; write "unknown" rather than inventing; mark each inferred line `(inferred)`.
3. Present the draft with a short gap list (max 8 items, most decision-relevant first). Unknown CAC, margin and conversion goal are the
   gaps that change the most downstream work.
4. Save as v1 with a changelog line once the user confirms or corrects.

## Template

```markdown
# Product Marketing Context: <Brand>

**Document version:** v1
**Last updated:** YYYY-MM-DD
**Artifacts:** plans <path> · competitor dossiers <path> · outbound <path> · loops <path>

## Product Overview
**One-liner:**
**What it does (2-3 sentences):**
**Category (the shelf customers search on):**
**Type:** SaaS / DTC store / service / app / marketplace / other
**Business model and pricing:**
**Archetype (client-types):** B2B SaaS / D2C app / hardware / marketplace / dev tool / deep-tech / Commerce-DTC / services

## Economics and Stage
**AOV or ARPC:**            **Gross margin:**
**Blended CAC (ads + tools + content + people):**   **Retention / repeat rate:**   **LTV:**
**Monthly marketing budget by line (paid / tools / people / retainers):**
**Growth phase:**            **Next budget or funding milestone and what it unlocks:**
**Market-quality quadrant (problem size x frequency):**
**Team: who touches marketing and what each owns:**

## Target Audience and ICP
**Target customers (who, size, situation):**
**Decision-maker / buyer:**
**Primary use case:**   **Jobs to be done (functional / emotional / social):**
**ICP pass/fail checklist:**
- [ ] firmographic or demographic fit:
- [ ] signal that makes timing right (with freshness window):
- [ ] reachable through a lawful, public channel:
**Disqualifiers (skip):**
**Never infer or segment cold prospects on:** health, financial hardship, politics, sexuality, religion or other sensitive traits
seen in public posts. A brand whose offer addresses one of these (e.g. debt relief, loans) works only from consented, inbound data.

## Personas
| Persona | Cares about | Challenge | Value we promise | Evidence (n, source) or "provisional: proxy" |
|---|---|---|---|---|

## Problems and Pain Points
**Core problem:**   **Why alternatives fall short:**   **What it costs them:**   **Emotional tension:**

## Competitive Landscape
| Competitor (direct / secondary / indirect) | Falls short because (observed, dated) | Where they beat us | Dossier |
|---|---|---|---|

## Differentiation
**Key differentiators:**   **Why customers choose us (evidence or "hypothesis"):**
**Where we lose, and to whom:**

## Objections and Anti-Personas
| Objection (as heard) | Real concern | Response | Proof |
|---|---|---|---|
**Anti-persona (not a fit):**

## Switching Dynamics
**Push:**   **Pull:**   **Habit:**   **Anxiety:**

## Customer Language
| Verbatim | Source + date | Theme | Confidence |
|---|---|---|---|
**Words to use:**   **Words to avoid:**   **Glossary:**

## Brand Voice (summary; detail from brand-studio)
| Attribute | Means | Doesn't mean | Example line |
|---|---|---|---|
**Tone by context:** support · launch · errors · sales/outreach · social · SMS
**Never use (and why):**

## Approved Claims and Proof
*Only claims in this table may appear in ads, outreach, creator briefs, PR pitches or sales collateral.*
| Claim | Evidence | Source + date | OK for (ads / outreach / PR / creators / site) |
|---|---|---|---|
**Testimonials (with permission and any incentive disclosure):**

## Channels and Accounts
| Channel | Handle or list | Size | Status (working / not / untested) | Owner |
|---|---|---|---|---|
*No passwords, keys or tokens here. Ever.*

## Compliance and Redlines
**Disclosure policy (#ad + platform paid-partnership label for any material connection):**
**Regulated topics or words to avoid (e.g. loan, health, income claims):**
**Countries or channels excluded for cold outreach:**
**SMS rules (consent, wording that trips carrier filters):**
**Brand-safety redlines (partners, topics):**

## Goals and North Star
**Primary business goal:**   **Key conversion action:**   **North-star metric:**
**Leading indicators by AARRR stage:**   **Current metrics (with date):**

## Approvals
**Claude may, without asking:** read, research, analyze, score, draft, stage, recommend, write local files in this project's `.agents/`.
**Claude asks the user first for:** sending, posting, publishing, scheduling, contacting anyone, spending or buying (ads, tools, creators,
incentives, paid APIs), changing live settings (store, CRM, n8n, ads accounts), deleting or suppressing records.
**Standing approvals the user has given (exact loop or task, caps, date):**

## Paid Ads (optional, owned by ads-and-measurement)
**Target CPA / ROAS and hard floor:**   **Budget and daily variance:**   **Conversions that count:**
**Known tracking weaknesses:**   **Campaign names and purpose:**

## Learnings
*Decisions and tested lessons. Newest first. About 20 active rows.*
| Date | Learning | Evidence (test, number, sample) | Applies to | Status |
|---|---|---|---|---|

## Changelog
*Newest first. One line per revision: what changed and why.*
- v1 (YYYY-MM-DD): Initial context.
```

## Versioning and Learnings rules

- Substantive change: bump the version, update "Last updated", prepend one changelog line naming the sections touched and the reason
  (e.g. "v3 (2026-11-10): added AOV and repeat rate from Shopify; new objection from creator DMs"). Never rewrite past entries.
- Typo-only fix: save without a bump.
- A real repositioning says so plainly in the changelog, because every downstream skill will now write against it.
- Learnings earn a row when: a test reached its planned sample, the same pattern appeared in 2+ campaigns or runs, the user made a decision
  with a reason, or the user gave the same correction more than once. Single anecdotes stay in run logs or get status `watch`.
- Retire a row (status `retired` + reason, move to the bottom) when a later test contradicts it, the market or offer changed under it,
  or it has been irrelevant for two quarters. Archive retired rows once active rows pass about 20.
- A new objection goes to Objections and a new verbatim to Customer Language, not to Learnings.
