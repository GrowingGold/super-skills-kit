# Send safety: consent, registration, carrier filtering, deliverability

One checklist for anything that sends. It merges the sms member's compliance reference (TCPA, 10DLC, GDPR, CASL, Australia,
STOP/HELP), its WhatsApp rules, the email rules the emails member never covered (authentication, bulk-sender requirements,
CAN-SPAM), and the carrier-filter lessons from a real lending-SMS incident.
Operational guidance, not legal advice: for programs over about 50K subscribers or with real revenue at stake, a TCPA-experienced
attorney reviews the setup [sms]. Platform rules change; confirm current details in official docs (Twilio docs connector,
Google/Yahoo sender pages, Meta pricing) before quoting them.

## 1. Classify every message first

| Class | Typical content | US SMS consent | Notes |
|---|---|---|---|
| Marketing | Promotions, offers, cart and browse reminders, win-back, cross-sell | Express written consent, captured electronically with timestamp; not a condition of purchase | An established business relationship is NOT enough for marketing texts |
| Transactional / informational | Order, shipping, delivery, OTP, account alerts, appointment confirmations | Express consent: number given for that transaction, knowing it will be texted | Still needs 10DLC or toll-free registration. Adding an offer, a money amount or urgency turns it into marketing |
| Conversational | Agent or staff replies inside a customer-started thread | Consent for that conversation | Opt-out words still end it |

## 2. US SMS: TCPA basics [sms]

- Statutory damages are $500-1,500 per message; class actions reach seven and eight figures. One settlement can run $5M-40M.
- **Opt-in disclosure**, directly next to the phone field and submit button (never in a footer), covering: brand/program name,
  recurring automated marketing texts, consent not a condition of purchase, message frequency, "Msg & data rates may apply",
  HELP and STOP instructions, links to terms and privacy. Template: `members/sms/references/compliance.md`.
- **Consent records**: timestamp, IP, page URL or keyword source, the exact disclosure text shown. Keep 4+ years (longer for EU).
- **Quiet hours** in the recipient's local time: federal 8am-9pm; Florida, Oklahoma and Washington are stricter (8am-8pm);
  carriers recommend 9am-8pm. Default 9am-8pm. HELP replies are exempt.
- **STOP**: honor STOP, END, CANCEL, UNSUBSCRIBE, QUIT, STOPALL, OPTOUT, and since the FCC's revocation rule (effective April
  2025) any reasonable plain-language opt-out such as "remove me", "don't text me", "wrong number". Platforms honor keywords in
  seconds; the legal ceiling is 10 business days, so free-text opt-outs need a human-or-agent path that flags them fast. One
  confirmation text is allowed, then nothing.
- **HELP / INFO**: reply with brand name, support contact, "Msg & data rates may apply", "Reply STOP to cancel".
- **Footer**: "Reply STOP to opt out" on the opt-in confirmation (with HELP and rates), at least quarterly on recurring
  marketing, and carrier-recommended on every promotional text. Include it on transactional flows' first message for safety.
- **Sender identity** in the text itself ("From [Brand]:"); recipients don't see a from-name.

## 3. Registration (US)

- **A2P 10DLC** (The Campaign Registry, through the platform): brand (legal name, EIN, type; trust score Standard or Verified)
  plus one campaign per use case (marketing, account notification, customer care, 2FA, delivery notification...) with sample
  messages, opt-in description and screenshot, opt-out and help text, volume estimate. Approval takes 1-7 business days.
- **Throughput** by trust and use case: verified marketing about 75-100+ msg/sec, standard 4-10, unregistered about 0.1 or blocked.
- **Common rejections**: samples that don't match real sends, an opt-in screenshot missing the disclosure, SHAFT content (sex,
  hate, alcohol, firearms, tobacco) without the right use case, vague campaign descriptions.
- **Toll-free verification**: the declared use case and monthly volume must match reality. One verification declared about
  10,000/month against roughly 50,000 actual; fix declarations before scaling volume.
- **The match rule**: what you send must look like what you registered. A new flow with new wording is a registration check.

## 4. Carrier content filtering (error 30007 and friends)

Carriers filter on content even when registration is clean. What one lender's data showed:
- Blocked up to 100%: rep-voice texts saying "I have your loan application and need to verify some information before we can
  check your rates", "call in N min to review your loan application results", and reminders with "Good news!" plus a dollar
  amount and "ASAP". Templates hadn't changed since July: the filter changed, not the copy.
- Delivered: "the loan link you requested", the Spanish versions, a plainly worded prequalified-offer text.
- Lessons for loan and debt copy:
  - Carriers and Twilio list third-party lending, debt consolidation/reduction/relief and credit repair as high-risk or forbidden
    US SMS content. Verify the current list (Twilio docs) before planning any loan or debt flow.
  - Keep it plain and expected: reference the thing the person asked for; no dollar amounts, "Good news", "approved",
    "ASAP", "act now", "results" teasers or countdowns in finance texts.
  - One branded link domain; no public shorteners (bit.ly, tinyurl), which filters treat as spam signals.
  - Consistent sender per flow; registered use case matches the content (an "account notification" campaign sending sales
    language is a mismatch).
- Volume shape:
  - Platform limits are daily ratios (a CRM may restrict a sub-account on high error or opt-out rates). A batch of risky texts on a
    quiet day (a Sunday reminder batch) produces a high ratio even when absolute numbers are small.
  - Throttle bulk sends; bursts trigger filtering [sms].
  - Failed sends must not auto-retry in a loop. Cap retries; a retry storm multiplies errors and keeps re-tripping the limit.
- When rewording: list every flow, step and template that can send the old text (CRM workflows, n8n, templates) and change all of
  them; then watch delivery for the first real sends. The first rewording missed two sibling workflows and re-tripped the limit.
- Triage order when texts fail: (1) error codes by message text and sending number in the message log; (2) which wordings fail vs
  deliver; (3) registration and verification status; (4) volume shape and retries; (5) platform-level limits. Prove the cause on
  real rows before changing anything (Change Protocol).

## 5. Email deliverability and law

- **Authentication**: SPF and DKIM on the sending domain, DMARC published (at least `p=none` to start, tighten later) and aligned
  with the From domain. Since 2024 Gmail and Yahoo require this of bulk senders (about 5,000+ messages a day to their users);
  Microsoft added the same for Outlook.com consumers in 2025. All senders need valid reverse DNS and TLS.
- **Unsubscribe**: marketing mail carries a visible unsubscribe link and one-click unsubscribe headers (List-Unsubscribe with
  List-Unsubscribe-Post, RFC 8058). Gmail expects removal within 2 days; CAN-SPAM's ceiling is 10 business days.
- **Complaints**: keep the spam rate in Google Postmaster Tools under 0.3% at all times, ideally under 0.1%.
- **CAN-SPAM** (US commercial email): truthful From and routing headers, non-deceptive subject lines (a fake "Re:" or "Fwd:" is
  deceptive, not just an AI tell), identify ads as ads, a valid physical postal address, a working opt-out. You are liable for
  vendors who send for you.
- **List hygiene**: confirmed opt-in for lead magnets when quality matters; never buy or rent lists; sunset people who haven't
  clicked or bought in 90-180 days after a re-engagement attempt [emails re-engagement "win back or clean list"].
- **Warm-up**: a new domain or dedicated IP starts with the most engaged recipients and grows volume gradually; sudden jumps from
  a cold domain land in spam.
- **Separate streams**: transactional and marketing mail on separate subdomains or streams, so a promo complaint spike doesn't
  delay receipts and password resets.

## 6. Outside the US [sms]

- **EU/UK (GDPR + ePrivacy)**: explicit affirmative opt-in (no pre-checked boxes), specific to marketing texts, informed, freely
  given; sender identity and easy opt-out in every message; access and deletion rights apply to SMS records; fines up to EUR 20M
  or 4% of global revenue.
- **Canada (CASL)**: express consent (implied only for an existing relationship within 24 months); every message carries legal
  sender name, mailing address, a contact method and an unsubscribe that works within 10 business days; penalties up to CAD 10M.
- **Australia (Spam Act 2003)**: express or narrowly inferred consent, sender ID, functional unsubscribe.
- **Mixed lists**: apply the strictest standard everywhere, store consent jurisdiction per subscriber, quiet hours 9am-8pm local.

## 7. WhatsApp [whatsapp]

- Free-form messages only inside the 24-hour window after the customer's last message; outside it, an approved template
  (marketing, utility, authentication). Free-form sends outside the window fail (error 131047).
- Opt-in must name WhatsApp specifically; honor opt-outs; blocks and reports lower the quality rating and the daily messaging limit.
- Warm up new numbers; per-message pricing changes often (check Meta's page; from October 2026 service and in-window utility
  messages are charged too).
- No marketing templates to US numbers: US marketing stays on SMS.

## 8. Pre-send checklist (run on every draft)

- [ ] Message class set (marketing / transactional / conversational) and consent on file for that class
- [ ] Registration covers it: 10DLC campaign use case or toll-free verification matches content and volume
- [ ] Sender identity in the message; brand name in the first words of each text
- [ ] Opt-out line where required; STOP/HELP replies configured and tested from a real phone (quarterly)
- [ ] Plain-language opt-outs are routed and honored
- [ ] Quiet hours enforced in recipient-local time (default 9am-8pm)
- [ ] Carrier-risk scan: no money amounts, approval teasers, "Good news", "ASAP" or countdowns in finance texts; content matches the registered samples
- [ ] One branded link domain, UTM-tagged, clicked once to confirm the landing URL keeps its parameters
- [ ] Character and segment count printed per text (GSM-7 160/153, UCS-2 70/67); no em dashes, curly quotes or stray emoji
- [ ] Volume shape: throttled, no big batch on a low-volume day, retries capped
- [ ] Every other flow that sends the old wording found and updated together
- [ ] Email: SPF, DKIM, DMARC aligned; one-click unsubscribe + visible link; postal address; honest subject; spam rate under 0.3%
- [ ] Locked text (disclosures, STOP/HELP, registered samples) untouched by the de-AI pass
- [ ] the user has approved the send or activation; first real sends watched end to end
