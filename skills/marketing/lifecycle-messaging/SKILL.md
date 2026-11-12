---
name: lifecycle-messaging
description: Plan, write and safety-check email and SMS lifecycle programs, draft-only. Use for email sequences (welcome, nurture, onboarding, re-engagement, win-back, post-purchase, drip, "what emails should I send", cadence, subject lines, preview text, newsletter, launch email, HTML email template, MJML); SMS/MMS flows (abandoned cart text, browse abandonment, post-purchase, flash sale, appointment reminder, opt-in confirmation, Klaviyo SMS, Postscript, Attentive, Twilio, CRM texts); compliance and delivery (TCPA, A2P 10DLC, toll-free verification, short code, STOP/HELP, quiet hours, consent records, CAN-SPAM, SPF/DKIM/DMARC, spam folder, carrier filtering, error 30007, opt-out spike, sub-account restriction); WhatsApp Business (templates, 24-hour window, click-to-WhatsApp); email-vs-SMS channel choice. Every send asks the user. Cold outreach goes to outbound-sales.
members: [emails, email-marketing, sms]
---

# Lifecycle Messaging

One skill for every message sent to people who already know the brand: email sequences, designed emails, SMS/MMS flows and
WhatsApp. It merges the coreyhaines `emails` and `sms` skills with the Open Design `email-marketing` template, and adds the send
gate they lacked: email deliverability and the carrier-filter lessons from a real lending-SMS incident. Load this first, run the
compliance gate before any strategy, and treat every output as a draft. Sending, scheduling or switching a flow on is the user's call.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| "What emails should I send", welcome / nurture / onboarding / re-engagement sequence | EMAIL SEQUENCE | Steps 0-8. Email-by-email templates: `members/emails/references/sequence-templates.md` |
| Audit a lifecycle, find missing emails (billing, usage, retention, win-back, campaigns) | LIFECYCLE AUDIT | Step 2 with the audit checklist in `members/emails/references/email-types.md` |
| Write or fix one email, subject lines, personalization, segmentation, email tests | EMAIL COPY | Step 5. Detail: `members/emails/references/copy-guidelines.md`. Finish with copy-and-content step 7 (de-AI) |
| Designed HTML email, launch email, newsletter template, MJML | EMAIL BUILD | Step 7 layout. Original: `members/email-marketing/SKILL.md` + `example.html` (skip its Open Design output contract) |
| SMS program, cart / browse / post-purchase / win-back / promo texts | SMS FLOW | Steps 0-8. Copy with character counts: `members/sms/references/sequence-templates.md` (fix its dash and urgency lines, see conflicts) |
| Opt-in wording, TCPA, 10DLC, toll-free, STOP/HELP, quiet hours, consent records | COMPLIANCE GATE | Step 1 + `references/send-safety.md`. Jurisdiction detail and response templates: `members/sms/references/compliance.md` |
| Texts blocked or filtered, 30007, error-rate or opt-out warning, CRM sub-account restriction | CARRIER TRIAGE | `references/send-safety.md` section 4, then the house rules below. Prove the cause before rewording (Change Protocol) |
| Emails going to spam, DMARC, bulk-sender rules, domain warm-up | DELIVERABILITY | `references/send-safety.md` section 5; agent `07-specialized-domains/email-deliverability-engineer.md` |
| Which SMS or email platform | PLATFORM | `members/sms/references/platforms.md`; email tools table in `members/emails/SKILL.md` |
| Customers mostly outside the US, WhatsApp templates, click-to-WhatsApp ads | WHATSAPP | `members/sms/references/whatsapp.md` + `references/send-safety.md` section 7 |
| Cold email or outbound sequences | hand off | super-skill `outbound-sales` |
| Phone-capture popups, cancel flows, dunning strategy, in-app onboarding | hand off | super-skill `conversion-lab` (popups, churn-prevention, onboarding) |
| Building the flow in n8n or a CRM | hand off | super-skill `n8n-builder` (drafts and change notes; activation is the user's) |
| Shopify Email or Klaviyo store wiring for a store | hand off | super-skill `commerce-pro` |

## Unified workflow

### 0. Context and the message inventory
Read `.agents/product-marketing.md` and its Learnings first: offers and formats already tested are not new ideas [emails].
Then establish: what triggers entry, who these people are and what they already know, the one conversion goal, and what
success means. Build a **message inventory**: every email, text, call and automated reminder these people already receive,
across every system (for example: CRM workflows, n8n flows, templates in a CRM, voice-agent calls). A new flow that ignores the old ones
double-taps people and drives opt-outs [emails "what other emails are they receiving", extended].

### 1. Compliance gate first
List blockers before any strategy [sms output format]. Classify every planned message:

| Class | Examples | Consent needed (US) |
|---|---|---|
| Marketing | Promos, cart reminders, win-back, cross-sell, review asks with offers | Express written consent (SMS); opt-in or existing relationship plus a working unsubscribe (email) |
| Transactional / informational | Order, shipping, delivery, OTP, account alerts, appointment confirmations | The number given for that transaction; still under 10DLC rules |
| Conversational | Agent replies inside a thread the customer started | Consent for that conversation; opt-out still honored |

A transactional text that adds an offer or urgency ("put that $X to use") becomes marketing, and carriers treat it that way.
Then check consent records (timestamp, source, exact disclosure shown), registration (10DLC brand and campaign whose use case and
sample messages match what you will send; toll-free verification with a truthful volume and use case), jurisdiction (US federal
plus state, EU/UK, Canada CASL), sender identity, the opt-out path, and for email the CAN-SPAM basics and domain authentication.
Full checklist: `references/send-safety.md`.

### 2. Map the lifecycle and rank flows
For each flow write trigger -> audience -> goal -> exit conditions. Audit the program against the lifecycle checklist
(onboarding, retention, billing, usage, win-back, campaign) in `members/emails/references/email-types.md`. Build in ROI order:
- Ecommerce: abandoned cart, welcome, post-purchase, browse abandonment, win-back, then campaigns.
- SaaS: onboarding to the aha moment, failed payment, trial expiry, upgrade, usage reports.
- Lead and service businesses: instant confirmation of the request, appointment reminders, no-show recovery, nurture.

### 3. Pick the channel per message
[sms "when SMS beats email", whatsapp]
- SMS when it can't wait 24 hours: cart recovery within the hour (about 98% read within minutes vs about 20% of email in a day),
  shipping updates, OTP codes, flash sales or drops, appointment reminders. If it can wait, email it.
- Email for long-form, education, nurture, newsletters, offer detail.
- Both for win-back: SMS for the nudge, email for the detail.
- WhatsApp when most customers are in LATAM, EMEA, India or Southeast Asia. Meta doesn't deliver marketing templates to US
  numbers, so US marketing stays on SMS.
Orchestration rules: email carries the content and SMS adds one or two high-intent nudges; a conversion exits the person from
every flow on every channel; no email and SMS for the same promo on the same day; set a weekly touch cap per person across channels.

### 4. Design the sequence
Principles [emails]: one message, one job, one primary CTA; value before the ask; relevance over volume; every message moves the
person somewhere. Exit conditions are part of the design, not an afterthought.

| Flow | Email | SMS |
|---|---|---|
| Welcome | 5-7 over 12-14 days: welcome and deliver (now), quick win (day 1-2), story/why (3-4), proof (5-6), objection (7-8), core feature (9-11), conversion (12-14) | Now: confirmation + reward + STOP/HELP line. Optional: 24 h reminder, day 7 if no purchase |
| Lead nurture | 6-8 over 2-3 weeks: deliver magnet, expand, problem deep-dive, framework, case study, differentiation, objection, direct offer | Email-led; SMS only for a booked call or event reminder |
| Onboarding | 5-7 over 14 days: first step, getting started, feature, success story, check-in (day 7), advanced tip, upgrade; supports in-app, never duplicates it | Milestone nudges only |
| Abandoned cart | Follow-up carrying offer detail | 30 min reminder, 4 h with proof, 24 h with discount only if margin allows. Never discount the first message: it trains abandonment |
| Browse abandonment | Optional | One text about 1 h after the browse |
| Post-purchase | Confirmation, delivery, review ask, cross-sell | Confirmation now (transactional), shipped, delivered, +2 days review prompt and +14 days cross-sell (marketing consent) |
| Re-engagement / win-back | 3-4 over 2 weeks after 30-60 days inactive: check-in, what's new, incentive, last chance (stay or unsubscribe; then clean the list) | 60-90 days after last purchase: picks, +14 days offer, +14 days final with opt-out note |
| Campaign / promo | Newsletter, seasonal, product updates | 1-2 sends per campaign, never the same day as the email |

Timing: early messages 1-2 days apart, nurture 2-4 days, long-term weekly or biweekly; send at the recipient's local time; B2B
avoids weekends. Texts follow quiet hours in the recipient's local time: default 9am-8pm (federal law allows 8am-9pm; several
states are stricter). Area codes lie about time zones, so confirm the platform handles it [sms compliance].

### 5. Write
**Email** [emails, copy-guidelines]
- Anatomy: hook (first line), context (why it matters to them), value, one CTA, a human sign-off.
- Subject: clear over clever, specific, 40-60 characters; must hold up if it is the only line read. Preview text: 90-140
  characters, extends the subject, never repeats it.
- Length: 50-125 words transactional, 150-300 educational, 300-500 story-driven. Paragraphs of 1-3 sentences, mobile first,
  bold sparingly, a button for the primary action and plain links for secondary ones; button text = action + outcome.
- Personalization: merge fields with a fallback that reads naturally (drop the name rather than "Hi friend"), dynamic blocks by
  segment, behavior triggers beat time-based sends.
- Email-specific tells to remove: fake "Re:" or "Fwd:", "You won't believe...", emoji bait, "I hope this email finds you well",
  "Just checking in", "Feel free to reach out". Open with the reason you're writing; close with one ask or just end.

**SMS** [sms]
- Anatomy: sender ID first ("From [Brand]:"), a hook in the first five words, the specific value, one CTA with one branded short
  link, then the opt-out line where required.
- Encoding math: GSM-7 = 160 characters for one segment, 153 per segment once split. One emoji, curly quote, em dash or accented
  letter switches the whole message to UCS-2: 70 characters, 67 per segment. Write straight quotes and plain hyphens; count every
  message and print the count and segment number next to it.
- Voice: plain and conversational, like a person texting; no subject lines, no marketing-speak, no ALL CAPS except codes; no fake
  intimacy. First-name tokens lift clicks (about 20%) when the data is clean.
- MMS (image plus up to 1,600 characters) costs 3-5x an SMS: save it for high-impact moments.

Then run copy-and-content step 7 (de-AI pass) on every draft. Consent disclosures, STOP/HELP wording and registered sample text
are locked; the pass never rewrites them.

### 6. Safety review before handover
Run section 8 of `references/send-safety.md` on every draft: message class and consent, registered-sample match, carrier-risk
phrasing, link domain (branded short domain, never a public shortener), opt-out wording, segment count, quiet hours, send volume
shape, and a search of every other live flow for the wording you are replacing (old copy hides in sibling flows).

### 7. Build as drafts
- Sequence doc in the output format below, one block per message.
- Designed emails [email-marketing]: one HTML file, inline CSS, a centered 600-680px column on a tinted page background, table
  fallback. Order: masthead (wordmark + up to three nav links), hero image block (no external images: inline SVG or a tinted
  gradient placeholder), eyebrow line, 2-3 line headline in the brand's display type, a 2-3 sentence body, ONE CTA, an optional
  2x2 specs grid (big number + unit + label), footer with brand, postal address, unsubscribe and view-in-browser. Self-check:
  reads top to bottom in 8-10 seconds, accent color used at most twice, legible at 480px. Brand tokens come from the project
  (stay brand-neutral until the user's brand lands).
- Platform notes: what gets configured where (flow triggers, filters, exits, quiet hours, frequency caps). For the user's systems the
  build is a draft for the n8n-builder or the CRM's change process.

### 8. Measure and learn
- Judge email on clicks, conversions and revenue per recipient; opens are inflated by Apple Mail Privacy Protection, so never
  segment or declare winners on opens alone.
- Tag every link: `utm_source=<platform>` (klaviyo, ghl, postscript), `utm_medium=email` or `sms`, `utm_campaign=<flow-name>`,
  lowercase with hyphens (see ads-and-measurement for the full convention).
- Test one variable at a time: subject line, send time, length (SMS vs MMS), offer size and timing, first-name token, CTA wording.
- After the first real sends, check the destination end to end: delivered, clicked, converted, opt-outs, errors (the user's
  watch-live rule).

## Output format

```
Flow: [name]        Trigger: [event]        Goal: [conversion]
Channels: [email / SMS / WhatsApp]          Length: [n messages]   Timing: [delays]
Exit conditions: [purchase, reply, opt-out, booked, ...]   Suppression: [other flows this person leaves]
Consent class: [marketing / transactional / conversational]   Blockers: [none / list]

Email [#]: [purpose]   Send: [timing]
Subject: [...] ([n] chars)   Preview: [...] ([n] chars)
Body: [full copy]
CTA: [button text] -> [destination with UTM]   Segment/conditions: [...]

SMS [#]: [purpose]   Send: [timing, local window]
Text: [full copy] ([n] chars, GSM-7 or UCS-2, [n] segments)
Link: [branded short link + UTM]   Opt-out line: [yes/no and why]

Metrics plan: [KPIs, benchmarks, first test]
```

## Core rules and checklists

### Phone number types (US) [sms]

| Type | Throughput | Cost | Fit |
|---|---|---|---|
| Short code | 100+ msg/sec | about $500-1,000/month + setup | High-volume marketing, list 100K+ |
| Toll-free (verified) | about 3 msg/sec | about $10-30/month | Mid volume, support, list 10K-100K |
| 10DLC (registered long code) | 1-250 msg/sec by trust score | about $2-10/month | SMB, conversational, transactional, list under 10K |

### Platform quick picks [sms, emails]
Already on Klaviyo email for DTC -> Klaviyo SMS. Shopify store wanting deeper SMS -> Postscript. Mid-market full service ->
Attentive. Custom builds and transactional -> Twilio (Plivo cheaper). EU email + SMS -> Brevo. Behavior-based automation ->
Customer.io. Email only: Customer.io (behavior), Mailchimp (SMB), Resend or SendGrid (transactional), Kit (creators).

### Health metrics

| Metric | Healthy range | Source |
|---|---|---|
| SMS opt-in rate from email list | 5-25% | sms |
| SMS click-through | 8-15% (email about 3%) | sms |
| SMS conversion per promotional send | 1-5% | sms |
| SMS revenue per send | $0.20-2.00 | sms |
| SMS cost per send | $0.0075-0.04 plus carrier fees | sms |
| SMS opt-out per send | under 2% generally, under 0.5% for promos; on CRM accounts with restriction limits treat 1.3% as the warning line | sms, the user |
| List growth | 5-15%/month early, 1-3% steady | sms |
| Email spam complaints | under 0.3% hard ceiling, aim under 0.1% | Gmail/Yahoo sender rules |
| SMS subscribers' LTV | typically 1.5-3x email-only | sms |

### Common mistakes [sms, emails]
Skipping registration (messages show "delivered" and never arrive); treating SMS like email (daily blasts kill the list);
discounting the first cart message; no brand name in the text; ignoring quiet hours; no STOP/HELP handling; emojis everywhere
(UCS-2 halves the segment); registered samples that don't match real sends; no conversion tracking; unthrottled bursts; several
jobs in one email; emails that repeat in-app onboarding; open-rate vanity metrics.

### WhatsApp essentials [whatsapp]
Free-form messages only within 24 hours of the customer's last message; outside it, a Meta-approved template (marketing,
utility or authentication category; cart reminders count as marketing). Per-message pricing applies to every marketing template,
and from October 2026 also to service replies and in-window utility messages; check Meta's pricing page before quoting. Blocks and
reports lower the quality rating and shrink daily limits. The Business app suits a solo operator; automation needs the Cloud API
directly or through a provider.

## When members disagree

| Between | Conflict | Rule |
|---|---|---|
| sms (internal) | "Emojis are fine, one per message" vs "emojis everywhere double the cost" | Default: no emoji. A DTC promo may use one only after the UCS-2 count is checked. Finance and lending brands: never |
| emails vs sms | Merge-field fallback "friend" vs "don't fake intimacy (Hey friend!)" | Fallback drops the name ("Hi," or no greeting). Never "friend" |
| emails vs copywriting/humanizer | "Test emoji in subject lines" vs emoji bait as an AI tell | No emoji subjects for the user's finance brands; DTC may test one after a clean baseline |
| sms vs lending-SMS evidence | "STOP footer required on opt-in and quarterly" vs texts that said "Reply 'remove'" | STOP language on the first message of every flow and on marketing texts; honor any plain-language opt-out ("remove me", "stop texting") as STOP |
| sms vs CRM platform limits | Opt-out "under 2% per send" is healthy vs platform warnings and restrictions near 1.3-1.5% | the stricter line wins on those accounts |
| emails vs sms | Welcome = 5-7 emails vs welcome = 1-3 texts | One orchestrated program: email carries the content, SMS adds 1-2 nudges, total touches capped per week |
| emails vs lending-SMS evidence | "B2C: test weekends" vs the Sunday pattern where a batch of reminder texts on a quiet day tripped a CRM's daily error limit | Error and opt-out limits are daily ratios: spread risky volume, avoid big automated bursts on low-volume days |
| sms "transactional OK without marketing consent" vs carrier reality | Reminders that added money amounts and urgency were blocked | Keep transactional texts strictly transactional; anything with an offer gets marketing treatment |
| sms templates vs encoding rules | Templates put an em dash after "WELCOME10" and use "selling fast" urgency while claiming 1 segment | Plain hyphen or a period (GSM-7); urgency only when true |
| sms "short links mandatory" vs carrier filtering | Any short link vs public shorteners being filtered | Branded short domain only (or the platform's tracked domain) |
| email-marketing vs claims rules | "Generate a real wordmark and product name, no placeholders" vs never invent | Real brand and product data for the user's brands; missing items get visible `[NEED: ...]`; invented names only on clearly labeled design mockups |
| email-marketing vs this skill | Open Design runtime: injected DESIGN.md, `<artifact>` tags, `data-od-id` attributes | Dropped: write a plain HTML file with project tokens |

## Combine with

- Sibling super-skills: copy-and-content (de-AI pass and long-form for newsletters), conversion-lab (popups, churn-prevention,
  onboarding, ab-testing), ads-and-measurement (UTMs, attribution, click-to-WhatsApp ads), outbound-sales (cold email, revops
  lifecycle stages), n8n-builder (the user's flows), commerce-pro (Shopify Email, Klaviyo).
- Skill tool: `humanizer` (always on), `artifact-design` (the user's review page for drafts), `superpowers:verification-before-completion`
  (before saying a flow works), `superpowers:systematic-debugging` (carrier-block triage).
- Docs: Twilio docs connector (`mcp__claude_ai_Twilio__twilio__search`, read-only) for current 10DLC, toll-free and forbidden-content rules.
- Agent prompts in `~/.claude/skill-library/agents/voltagent/` (model haiku for lookups):
  - `07-specialized-domains/email-deliverability-engineer.md`: SPF/DKIM/DMARC, provider setup, spam-folder diagnosis.
  - `04-quality-security/compliance-auditor.md`: a cold review of consent capture and records.
  - `04-quality-security/gdpr-ccpa-compliance.md`: EU/UK or California subscribers.
  - `08-business-product/legal-advisor.md`: opt-in disclosure and terms wording before a lawyer sees it.
  - `08-business-product/content-quality-editor.md`: an independent AI-tell read on a batch of messages.

## House rules

- Draft-only. Every send, schedule, flow activation, list import or template change in a CRM, Klaviyo, Shopify Email, Twilio
  or n8n asks the user first.
- Carrier blocks (lending-SMS case study): loan texts like "I have your loan application and
  need to verify...", "call in N min to review your loan application results" and "Good news! ...put that $X to use ASAP" were
  blocked (30007) up to 100%, while "the loan link you requested" delivered. The CRM then restricted the sub-account (about 10% error,
  about 1.5% opt-out). When rewording, search every flow for the old text: copies survived in sibling workflows and re-tripped the
  limit days later.
- Failed sends never retry in a loop: an hourly re-send of failures (about 490 per hour) multiplied the error rate in the
  incident. If an opt-out burst guard already exists in n8n or the CRM, check it before building new monitoring.
- An SMS agent should not promise a human hand-off it cannot deliver (no "someone will reach out"); upset or human-request replies get an apology and
  the customer-service number from the prompt; replies are capped per lead.
- Any live flow change follows the Change Protocol: prove the problem with real message data, game out every flow that reads or
  sends the same thing, present it on the user's review page, then watch the first real sends end to end.
- Every n8n or CRM workflow change gets an in-workflow note.
- Never copy phone numbers, sender IDs, API keys or contact data into drafts, skills or reports; secrets stay in a local .env or secrets manager.

## Members

| Member | Best at | Path |
|---|---|---|
| emails | Sequence types, lengths and timing, subject and preview rules, email copy anatomy, lifecycle audit checklist, email AI tells, output format | `members/emails/SKILL.md` (+ `members/emails/references/sequence-templates.md`, `email-types.md`, `copy-guidelines.md`) |
| email-marketing | Single-column HTML email layout (masthead, hero, eyebrow, headline lockup, one CTA, specs grid, footer) with a readability self-check | `members/email-marketing/SKILL.md` (+ `example.html`) |
| sms | SMS vs email choice, TCPA/10DLC/CASL/GDPR compliance, STOP/HELP templates, number types, segment math, flow templates with character counts, platforms, metrics, WhatsApp | `members/sms/SKILL.md` (+ `members/sms/references/compliance.md`, `sequence-templates.md`, `platforms.md`, `whatsapp.md`) |

If a member folder is missing (not installed), work from this file alone.
