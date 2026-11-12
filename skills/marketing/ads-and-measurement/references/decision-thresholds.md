# Decision thresholds: one ladder for kill, keep, graduate, scale

The members gave four different answers to "when do I judge an ad": fixed CPL multiples (ads `b2b-paid-playbook.md`), "no fixed
kill rules" (ads `audit-guardrails.md`, ads-tiktok), a TCPL-anchored decision tree with a 3x data gate (ads
`meta-decision-system.md`), "1,000+ impressions" (ad-creative) and "about five days" (ads `meta-andromeda-playbook.md`). This file
merges them into one ladder. Every number is a starting prior: recalibrate on the account's own data after 30 days. Every
action below is a recommendation in a draft for the user, never an edit made on the account.

## The anchor: target cost per result (TCR)

All thresholds are multiples of one number from step 0 of the workflow.
- Lead gen (B2B): TCR = TCPL, the target cost per *qualified* lead. From deal math: target cost per sale or demo x
  qualified-to-sale rate. From history: trailing 30-day qualified CPL x 0.8. New account: target CAC x qualified-to-customer rate,
  replaced by the history method after 30 days.
- Ecommerce (DTC store): TCR = target CPA per first purchase, set below breakeven CPA (contribution margin per first order;
  1 / margin % = breakeven ROAS).
  "Qualified" becomes a buyer who matches the target customer: new-customer share, AOV, refund rate.
- A flat dollar cutoff the user names ("kill above $40") is not an anchor until it's reconciled with this math (hard stop).

## Gates before any judgment

All must be true before a kill or graduate call; otherwise the call is HOLD.
1. Spend: at least 3x TCR on the ad (Meta). At true cost = target, 3x TCR should yield about 3 results; zero results at that spend
   happens about 5% of the time by chance, so 3x gives about 95% confidence (2x leaves a 13% false-negative rate; 5x overpays).
   Other platforms: 2-3x TCR [b2b-paid-playbook].
2. Time: at least 5-7 days live; launch day of week changes who sees it [andromeda, meta-decision-system].
3. Learning: outside the learning phase, or the learning phase itself is the problem being diagnosed.
4. Lag: the last few days are excluded or flagged; recent days always undercount conversions [operating-check].
5. Data trust: tracking and the ledger agree within normal variance. If not, INVESTIGATE overrides everything.
Impressions alone are never a gate.

## Stage 1: delivery check (day 7, Meta CBO)

- Fair-share test: minimum expected spend = (campaign daily budget / active ads) x 7 x 0.5. Below it, or zero spend: kill (Meta
  pre-screened it out).
- Ongoing: lifetime spend >= 1x TCR AND under about $10/day over the last 7 days: kill.
- When iterating a delivery kill, change hook, visual or format only; copy and CTA never got a chance to matter.

## Stage 2: quality evaluation (weekly, rolling 14 days)

Run in order; stop at the first action.
1. Spend under 3x TCR -> wait.
2. Zero platform results at 3x TCR -> swap and abandon the concept.
3. Quality (needs the CRM or store): results but zero qualified -> keep the format, change the angle. Qualified rate under 40% ->
   swap and add filtering language (at 40%, true cost per qualified result is 2.5x what the platform shows). 40-60% -> one more
   week. 60%+ -> continue.
4. Cost: cost per qualified result <= TCR -> candidate winner; 1-1.5x -> monitor (normal variance); over 1.5x -> swap.

Simpler non-Meta form [b2b-paid-playbook]: pause a new ad at 2-3x TCR spent with zero results; pause a maintained ad (past 7-14
days) whose cost runs 1.5-2x over TCR. Same gates apply.

## Graduation (testing -> scaling)

All true: 5+ qualified results, qualified rate 60%+, cost per qualified result <= TCR, live 14+ days, 1+ qualified result in the
last 7 days.

## Fatigue

| Campaign type | Safe frequency | Warning | Critical |
|---|---|---|---|
| Cold prospecting | 1.0-2.5 | 2.5-4.0 | over 4.0 |
| Retargeting | 2.0-4.0 | 4.0-6.0 | over 6.0 |
| ABM / small audiences | 2.0-5.0 | 5.0-8.0 | over 8.0 |

Other signals, most urgent first: CTR down 20%+ from the ad's baseline over 7 days; CPM up 30%+ over 2 weeks (moves before CTR);
relevance rankings below average; CPA rising with stable targeting. Scaling-campaign ads use a stricter bar: frequency 3.0-3.5 or
cost +20% -> start two iterations now (they take about 14 days); frequency over 3.5, cost +40%, or over 1.5x TCR for two weeks ->
swap. Retire the concept (don't iterate) when CTR is down 30%+ from peak or frequency crosses the critical band. Typical lifespans
(B2B): statics 14-28 days, short video and carousels 21-35, UGC and testimonials 28-42.

## Swap rules

- Never pause without a replacement staged; keep 2-3 iterations ready; replacement live within 7 days (immediately at critical fatigue).
- No replacements -> move the budget to proven ads; don't leave a zombie spending.
- What to change follows why it died: delivery kill -> hook or visual; quality kill -> angle and qualifying language; cost kill ->
  offer and audience; fatigue -> a fresh execution of the same proven concept.
- Never edit creative inside a performing ad (resets learning); launch new ads beside it. Pausing doesn't reset learning; editing does.
- Zombie campaign: dead CBO variants you still believe in can relaunch in their own ad set; about 1 in 5 revives [andromeda].

## Creative supply math [meta-decision-system]

- Test throughput per month ~= (monthly budget x 0.20) / (3 x TCR); early delivery kills free budget, so real throughput runs
  1.5-2x that.
- Win rates: iterations on winners about 25%, new concepts about 10%, blended about 1 in 6. For N winners, plan about 6N tests.
- Proven-ad inventory needed ~= monthly budget / $5,000 (B2B; each proven ad absorbs about $5K/month before fatiguing). You can't
  scale budget ahead of creative supply.
- Iteration priority on a winner: hook, then visual treatment, then format, then body copy and CTA.

## Scaling and rollback

- Preconditions: proven-ad count meets the next budget level, account frequency under 3.0, cost per qualified result <= TCR for
  2+ consecutive weeks, 3+ replacements staged.
- Rate: about +20% every 3-5 days; never +30% or more in one move [ads, meta-decision-system].
- Google: move tCPA/tROAS targets in 10-15% steps and wait 1-2 weeks; a budget-capped campaign that converts often gets cheaper
  when budget rises; daily spend up to 2x budget is normal [google-search-playbook].
- Rollback: cost per qualified result over 1.5x TCR after a step -> cut budget 20-30% at once, stabilize 2 weeks, resume at +10% per week.
- The wall (account-average frequency over 3.5, or rolling monthly reach flat or falling): expand lookalikes (1% -> 2-3%), add seed
  audiences, test broad, add partnership ads, re-open remarketing.
- Automation bars: Google smart bidding after about 30 conversions in 30 days per campaign (0-15/month manual or Maximize
  Conversions, 15-30 Maximize Conversions, 30+ stable tCPA near trailing actuals, tROAS once real values flow); Meta Advantage+
  after about 50 optimization events per week (budget ~= target CPA x 50 / 7 per day), else optimize a higher-volume event.

## Weekly cadence [meta-decision-system, operating-check]

Monday: pull rolling 14-day data, run Stage 2 on tests and fatigue checks on scaling ads. Wednesday: launch tests into freed
slots, Stage 1 on day-7 ads. Friday: scale steps or rollbacks, plus the readout. Monthly: creative library audit, TCR review,
rolling reach check, creative retro. Each step's output is a draft list of changes for the user, not an edit.

## Benchmarks (directional only)

B2B SaaS on Meta, practitioner-reported: CTR 1.0-1.5% (red flag under 0.8%), CPM $10-20 (red flag over $25), form CPL $20-50
(red flag over $75), landing-page CVR 8-12%. Q1 CPMs are the year's lowest; Q4 runs 60-80% higher. Use these only when the
account has no history, and label them as outside benchmarks.
