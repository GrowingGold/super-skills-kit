# Local SEO numbers: benchmarks, specs and timings

Merged from 16 members so every threshold lives in one place, with the members' disagreements already resolved (see the
SKILL.md conflict table). All figures are member-supplied and directional. Compare against the client's own history first,
competitors second, these tables third, and re-check platform limits against current docs before quoting them to anyone.

## Geogrid [geogrid-analysis, local-falcon-tool, local-reporting, localseodata-tool]
- ARP (1-20, 20 = not in the top 20): good under 5, OK 5-10, needs work over 10. ATRP = average of the best positions.
- SoLV bands for reports: Dominant 70%+, Strong 50-69%, Average 30-49%, Weak 15-29%, Invisible under 15%.
- Heatmap colours: 1-3 green, 4-7 yellow, 8-13 orange, 14-20 red, not found grey.

| Business | Grid | Radius |
|---|---|---|
| Neighbourhood: coffee shop, salon, restaurant | 5x5-7x7 | 1-3 mi |
| City-wide: dentist, chiropractor, single-location medical | 7x7-9x9 | 3-7 mi |
| Home services: plumber, electrician, HVAC | 9x9-11x11 | 7-15 mi |
| Regional or metro: hospital system, franchise | 13x13-15x15 | 10-20 mi |
| Rural | 7x7-9x9 | 15-30 mi |

- Density override: dense urban 1-3 mi even for services, suburban 3-10 mi, rural 15-30 mi. LocalSEOData stops at 9x9.
- Cadence: weekly during active work, biweekly steady state, monthly maintenance, and before/after every change.

## Reviews [review-management, whitespark-tool, local-reporting]

| Metric | Good | Needs work |
|---|---|---|
| Rating | 4.5+ | under 4.0 |
| Count | 2x the nearest rival | below the top-3 rivals |
| Response rate | 100% | under 75% |
| Response time | within 24 h | over 72 h |

- Reply timing: positive 24-48 h, negative 4-12 h. Ask volume: a steady 5-10 requests a week.
- Monthly velocity fallbacks when rival data is missing. By size: solo 4-8, 5-20 staff 10-20, multi-location 20-50+ per
  location. By vertical: restaurant 15-30, medical 8-15, home services 5-10, legal 3-5, B2B 2-4. Under 2 a month needs work.

## GBP and listing specs [gbp-optimization, gbp-posts, service-area-seo, bing-places, apple-business-connect]
- Description 750 characters; up to 9 additional categories; up to 20 service areas for an SAB.
- Photos: 10-15 to start, 2-3 new a month, 720 px+ wide, JPG or PNG, cover 16:9; restaurants weekly. Video 30 s-3 min, under 75 MB.
- Posts: hook in the first 80-100 characters (the preview), body up to 1,500 characters and under 300 words, photo at least
  400x300 (1200x900 recommended), 1-2 a week per location.
- Bing description up to about 300 words. Apple Showcases monthly, 1:1 or 16:9 images.

## Citations [brightlocal-tool]
Accuracy: 95-100% excellent (monitor quarterly), 85-94% good (fix the rest), 70-84% needs work (top directories and
aggregators first), under 70% critical (clean up before other optimization).

## GBP action trends, per location per month [local-reporting]
- Search impressions: stable or growing is healthy; declining 3+ months is a warning.
- Calls: a drop over 20% month on month is a warning, but read it against the broad click-to-call decline.
- Direction requests: a sharp drop usually means a data issue. Website clicks falling while impressions grow = a CTR problem.

## Location health score, 0-100 [local-reporting]

| Component | Weight | Scoring |
|---|---|---|
| SoLV, primary keyword | 25% | SoLV % maps directly |
| Review rating | 15% | 4.5+ = 100, 4.0 = 75, 3.5 = 50, under 3.0 = 25 |
| Review velocity | 10% | on target = 100, under half of target = 50, declining = 25 |
| Response rate | 10% | 100% = 100, under 50% = 25 |
| GBP completeness | 15% | all fields = 100, missing critical fields lower |
| Citation accuracy | 10% | accuracy % maps directly |
| GBP action trend | 15% | growing = 100, flat = 60, declining = 30 |

Colour: 80+ green, 60-79 yellow, under 60 red. With 50+ locations show top N / bottom N and exceptions only, plus a CSV export.

## Organic and on-site [google-search-console-tool, google-analytics-tool, semrush-tool, ahrefs-tool, local-keyword-research]
- Expected organic CTR by position: 1 = 25-35%, 2 = 12-18%, 3 = 8-12%, 4-5 = 5-8%, 6-10 = 2-5%, 11-20 = 0.5-2%. Below the
  band for its position = rewrite the title and meta.
- GA4 on location pages: conversion rate 3-5% for local services; engagement rate under 50% or engagement time under 30 s =
  content mismatch. Traffic mix: organic 40-60%, direct 20-30%, referral 5-15%; organic under 30% means SEO needs work.
- Core Web Vitals: LCP under 2.5 s, INP under 200 ms, CLS under 0.1; pages load under 3 s.
- Semrush: local volume under 100 is normal; KD under 40 reachable; CPC over $5 commercial.
- Ahrefs DR for local sites: 20-40 typical, 40-60 strong, 60+ brand or multi-location. Healthy anchors: brand 40-60%, generic
  15-25%, location 10-20%, exact match under 10%. Under 50% followed links is weak.

| Market size | Service keyword volume / mo | Geo-modified volume / mo |
|---|---|---|
| Major metro | 5,000-50,000 | 500-5,000 |
| Mid-size city | 1,000-10,000 | 100-1,000 |
| Small city or suburb | 100-1,000 | 10-100 |
| Rural or small town | 10-100 | 0-10 |

Tools undercount local volume; Search Console impressions and CPC beat tool volume as evidence.

## Content sizes [local-content-briefs, local-content-strategy, local-landing-pages, multi-location-seo]
- Brief depth tiers: comprehensive 400-600 words (2-3 per piece), standard 200-300 (4-6), brief 75-150 (4-6), entity
  mentions 1-2 sentences. 15+ concepts per piece; pillar pages 2,500-4,000 words and 20+ concepts; 8-10 reader questions,
  3-5 in direct-answer format.
- Location pages: 300+ unique words is the floor for templated pages; blog posts about 800-1,500 words, guides 1,500-2,500;
  2-4 local pieces a month.
- Content-vehicle defaults: a dedicated page at about 50+ monthly searches, a GBP service entry below that, no action under
  10, each overridden by Search Console impressions, CPC or conversion value.
- Scale: hand-write up to about 20 pages; template plus required unique sections up to about 100-200; programmatic beyond that
  only with a real per-page data source.

## Local ads [lsa-ads, local-ppc-ads]
- LSA cost per lead: home services $15-80, legal $50-300, healthcare $20-100 (overall $5-300+). Answer rate 90%+; lead to
  booked job 30-50%; return missed calls within 15 min, messages within 1 h; disputes within 30 days (credit in 1-5 business days).
- Local PPC: CTR 3-5%, lead conversion 5-15%, mobile bids +10-30%, 10-20% of budget held for tests, conversion-based bidding
  once a campaign has 30+ conversions (thresholds and kill rules: ads-and-measurement).

## Timelines [several members]

| Change | Expect or recheck |
|---|---|
| Citation fixes at aggregators | 4-8 weeks to propagate; re-audit then |
| Managed citation building | 2-4 weeks to process; re-audit at 6-8 weeks |
| Local links | 4-8 weeks before rankings move |
| New location or area pages | geogrid 2-4 weeks after publishing |
| Service-area tightening | geogrid before and 2-4 weeks after |
| Schema | Rich Results Test at once; Search Console enhancements for 2 weeks |
| Duplicate consolidation | recheck monthly for 3 months |
| After reinstatement | no edits for about 2 weeks; watch 30 days |
| Calling a ranking trend | 3+ months of same-settings scans |
| Local SEO results overall | 3-6 months (say so in proposals) |
| Listings on Apple or Bing | days to appear after claiming |
| LSA verification | 2-6 weeks |
| Suspension reinstatement | soft, first time 3-7 days; hard with a clear fix 1-3 weeks; repeated 2-4 weeks; competitor-triggered 1-2 weeks; multi-location mass 2-6 weeks; each appeal after a denial 1-3 weeks |

## Deliverable pricing, agency mode only [client-deliverables]
- Audits (US ranges): prospect free, GBP $200-500, website $800-2,500, Ads/LSA $400-1,000, local visibility $500-1,500, AI
  visibility $750-2,500, comprehensive $1,500-5,000.
- Engagements: per location $25-400 a month, flat retainer $500-3,000 a month, projects $1,500-15,000, setup plus monthly
  (for example $2,500 + $500), or tiered by location count.
