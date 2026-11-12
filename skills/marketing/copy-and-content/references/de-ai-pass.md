# De-AI pass: the merged catalog

One catalog built from three overlapping lists: copywriting's `members/copywriting/references/ai-tells.md` (marketing-copy blacklist with bans,
caps and second-generation tells), humanizer's `members/humanizer/references/patterns.md` (24 Wikipedia-derived patterns) and copy-editing's
AI-tell check, plus the channel-specific tells from emails and ad-creative. Duplicates are merged under one name; the source tag
says where each came from. Use it for step 7 of the copy-and-content workflow on any text: page copy, long-form, email, SMS,
ads, docs, posts.

**Ban** = a tell even once. **Cap** = fine once, chosen on purpose; a tell when repeated or stacked.
**Short copy** = headlines, subheads, hero, CTAs, ads, social posts, subject lines, preview text, SMS.
**Section** = one hero, one page section, or one whole short post.

Most of these are old human rhetoric. Generated text gives itself away by using them by default, stacked, with nothing specific
behind them. Structure gives text away faster than any single word, so start with the shapes.

## 1. Structural shapes

| # | Pattern | Level | Looks like | Fix | Source |
|---|---|---|---|---|---|
| S1 | Contrast reveal / negative parallelism | Ban | "It's not X, it's Y." "Not because X. Because Y." "Not just X, but Y." "Less X, more Y." "X? Think again." | State Y directly with the reason. To correct a real wrong belief, state the fact and the evidence | ai-tells 1, humanizer 9 |
| S2 | Negation list | Ban | "No setup call, no templates, no waiting on IT. No contract." "Zero X, zero Y." | Say what happens, in order. One real absence near the CTA. Ad variant: stacked negations to fit a character limit, keep the one that matters | ai-tells 2, ad-creative |
| S3 | Trailing pile-on / superficial -ing tail | Ban | "...the data you have, no exports, no spreadsheets." "...ensuring nothing slips through the cracks." "...highlighting the importance of..." | End at the claim; give a real benefit its own sentence. A clause adding a new fact stays ("Imports run nightly, keeping your existing IDs") | ai-tells 3, humanizer 3 |
| S4 | Self-answered question | Ban | "The result? 3x faster." "The catch? There isn't one." "Why does this matter? Because..." | Delete the question, keep the answer. FAQ questions and a reader's own question are fine | ai-tells 4 |
| S5 | Colon reveal | Ban | "The best part: it learns." "One word: speed." | Normal sentence. Colons are for lists, labels, quotes | ai-tells 5 |
| S6 | Fragment drumbeat / staccato bursts | Cap 1 per section | "Simple. Fast. Done." "It's fast. It's simple. And it just works." | Merge into one sentence that carries a fact | ai-tells 6, second-gen |
| S7 | Reflexive threes | Cap 1 per section | "Fast, secure, and scalable." "Innovation, inspiration, and insights." | As many items as the facts support; often the single strongest concrete claim | ai-tells 7, humanizer 10 |
| S8 | Dashes | Ban in short copy, cap 1-2 per page in long copy | "It's not a tool, it's a teammate" carried by a dash; "--" pairs | Period, comma, colon, parentheses | ai-tells 8, humanizer 13 |
| S9 | Uniform rhythm / perfect balance | Cap | Every sentence 12-18 words; every section heading + two sentences + three bullets | Sentence length follows the thought; let the strongest section run long and the weakest shrink | ai-tells 9, second-gen |
| S10 | Copula dodging | Cap | "serves as", "stands as", "boasts", "represents", "features" | "is", "has", or the real verb | ai-tells 10, humanizer 8 |
| S11 | Abstract subjects | Cap | "The platform empowers teams to..." | Make the customer the subject: "Your team ships experiments without filing a ticket" | ai-tells 11 |
| S12 | False ranges | Cap | "From startups to enterprises." "From the Big Bang to dark matter." | Name the segment or steps actually covered | ai-tells 12, humanizer 12 |
| S13 | Synonym cycling | Cap | dashboard, interface, portal, hub for one thing | Pick the customer's word and repeat it | ai-tells 13, humanizer 11 |
| S14 | Formulaic "challenges" section | Ban | "Despite its success, X faces challenges... Despite these challenges, it continues to thrive." | Concrete problems with dates and causes, or nothing | humanizer 6 |

## 2. Openers, closers, setups (Ban)

| Pattern | Example | Instead |
|---|---|---|
| Era opener | "In today's fast-paced world..." | The customer's problem |
| False-choice opener | "Whether you're a solo founder or a Fortune 500..." | Name who it is for |
| "Imagine..." | "Imagine never chasing an invoice again." | The actual before and after |
| "When it comes to..." | "When it comes to billing, ..." | Start with the subject |
| Throat-clearing | "Here's the thing:" "The truth is" "Let me be clear" "Here's what nobody tells you" | Cut. If the claim can't stand alone it needs evidence, not a drumroll |
| Announcing / self-narration | "In this guide, we'll explore..." "Let's dive in" "Here's why this matters" "This is where it gets interesting" | Start with the content |
| Recap ending | "In conclusion" "Ultimately" "At the end of the day" | End on the last concrete point or the CTA |
| Tidy closer / fake-profound kicker | "Because your team deserves better." "And that changes everything." "The future looks bright." | End on a number, a named customer, the offer, or the CTA |
| Filler transitions | "It's worth noting" "Moreover" "Additionally" "Importantly" | Delete; the sentence usually works without it |

## 3. Marketing phrases (Ban)

"Say goodbye to X / say hello to Y" -> show the new workflow. "Unlock / unleash the power of" -> the outcome and the number.
"X, reimagined / redefined" -> what is actually different. "Take it to the next level" -> the metric and the target.
"Transform the way you work" -> a before and after with numbers. "The X you deserve" -> the gap you close. "The future of X is
here" -> what ships today. "Built for teams who move fast" -> the real customer and trigger. "Everything you need" / "all-in-one"
-> the 2-3 things buyers check. "Effortless" / "in just a few clicks" -> the real step count or time. "Join thousands of happy
customers" -> the real count, logos or a named quote. "Game-changer" -> what changes, for whom, by how much. [ai-tells]

## 4. Vocabulary

Swapping a banned word for a synonym makes a new tell. Replace the word with the fact it stood in for ("robust" -> "99.99% uptime
over two years"). Favored words drift as models change; the structural shapes don't go stale.

- **Ban:** delve, tapestry, testament to, realm, embark, beacon, multifaceted, paradigm, synergy, myriad, plethora, meticulous,
  intricate/intricacies, interplay, utilize, leverage (verb), supercharge, turbocharge, game-changer, "ever-evolving landscape",
  "plays a crucial/pivotal role", "indelible mark", "setting the stage for" [ai-tells, humanizer 1 and 7]
- **Cap (two in one paragraph = rewrite it):** seamless, robust, streamline, empower, elevate, unlock, unleash, harness, foster,
  enhance, optimize, showcase, highlight (verb), underscore, garner, align with, additionally, crucial, vital, pivotal, key
  (adjective), valuable, enduring, vibrant, cutting-edge, innovative, revolutionary, transformative, holistic, comprehensive,
  powerful, next-level, world-class, best-in-class, landscape, navigate, ecosystem, journey (unless literal) [ai-tells, humanizer 7]
- **Cap, empty intensifiers:** truly, genuinely, incredibly, deeply, fundamentally, significantly, simply, actually, literally,
  quietly, very, really, extremely, just, basically [ai-tells, copy-editing]
- **Promotional (Ban in neutral or informational text):** boasts, nestled, in the heart of, rich (figurative), profound,
  breathtaking, stunning, must-visit, renowned, groundbreaking, exemplifies, commitment to [humanizer 4]

## 5. Content patterns

| Pattern | Level | Signal | Fix | Source |
|---|---|---|---|---|
| Inflated significance / importance puffery | Ban | "marks a pivotal moment", "reflects a broader movement", "redefines the category" | State the fact; let the reader judge | humanizer 1, ai-tells |
| Undue notability | Ban | Lists outlets or follower counts without context | One specific, dated citation of what was said | humanizer 2 |
| Vague attribution / weasel sources | Ban | "experts argue", "industry reports", "studies show", "trusted by industry leaders" | Name the source or customer, or cut | humanizer 5, ai-tells |
| Hedge stacks | Cap | "could potentially possibly help reduce" | State what you know or scope it honestly ("may affect") | humanizer 23, ai-tells |
| Filler phrases | Ban | "in order to", "due to the fact that", "at this point in time", "in the event that", "has the ability to", "it is important to note that" | to, because, now, if, can, (delete) | humanizer 22 |
| Generic positive conclusion | Ban | "Exciting times lie ahead." | The next concrete plan or number | humanizer 24 |
| Invented labels | Cap | "the integration tax", "the growth trap" | Coin a term only if you define it and use it site-wide | ai-tells |
| Wisdom-shaped sentence | Ban | "Great tools get out of the way." "Speed is a feature." | The specific fact it gestures at, or cut | ai-tells second-gen |
| Performed cleverness | Cap | "Your inbox, minus the noise." | Keep one if the brand is playful and it says something true | ai-tells second-gen |
| Omniscient casual | Cap | Relaxed voice, total certainty, no limits | Scope claims; say who it isn't for | ai-tells second-gen |
| Reflexive specificity | Cap | Every claim has a round stat or a too-neat anecdote | Every number and story real and sourced, else `[NEED: proof]` | ai-tells second-gen |

## 6. Tone and communication artifacts

- Chatbot phrases (Ban): "I hope this helps", "Of course!", "Certainly!", "Let me know if you'd like...", "Here is a..." [humanizer 19]
- Knowledge-cutoff disclaimers (Ban): "as of my last update", "while details are limited", "based on available information" [humanizer 20]
- Sycophancy and chummy openers (Ban): "Great question!", "You're absolutely right", "Let's be honest...", "We get it." [humanizer 21, ai-tells]
- Fake vulnerability (Ban): "I'll be honest, I was skeptical too..." with no real story [ai-tells]
- Over-explaining (Cap): "Let's break this down", "Think of it as..." [ai-tells]
- Hype punctuation (Ban): "Ready to level up?!", exclamation points in body copy [ai-tells, copywriting]

## 7. Formatting

- Emoji as structure or decoration (Ban): leading bullets or headings with emoji [humanizer 17, ai-tells]
- Bold label on every bullet / inline-header lists (Cap): "**Performance:** Enhanced through..." Keep for reference tables [humanizer 14-15, ai-tells]
- Excessive boldface (Cap): bolding every term [humanizer 14]
- Parallel bullet openers (Cap): every bullet "Ensures... / Provides... / Enables..." Start with the customer outcome, vary grammar [ai-tells]
- Title Case Everywhere (Cap): sentence case unless the brand guide says otherwise [humanizer 16, ai-tells]
- Label headings (Cap): "What / Why / How" sections. Headings that make a claim [ai-tells]
- Unicode decoration (Ban): arrows, multiplication signs, bold-letter Unicode in body copy [ai-tells]
- Curly quotes (Cap): use straight quotes; in SMS, curly quotes force UCS-2 (70-character segments) [humanizer 18, sms]

## 8. Channel-specific tells

- **Email** [emails]: fake "Re:" or "Fwd:" subjects (also deceptive under CAN-SPAM), "You won't believe...", "Big news" with an
  emoji, "I hope this email finds you well", "Just checking in", "Great news!", "Feel free to reach out if you have any
  questions". Open with the reason you're writing; end with one specific ask or just end. No dashes in subject or preview text.
- **Ads** [ad-creative]: generic "POV:", "Stop scrolling", "Here's what nobody tells you about X" hooks (a hyper-specific POV is
  fine); CTA slop ("Get started today", "Join thousands of happy customers"); ten variations that all open the same way.
- **SMS** [sms]: "Hey friend!" fake intimacy, ALL CAPS (except codes), emoji runs, marketing-speak. Write like a person texting.

## 9. The soul check

Removing patterns is half the job. Clean but voiceless text is just as obvious [humanizer]. Signs: every sentence the same length,
no opinion, no admitted limit, no edge, reads like a press release. Fix by returning to "find the writer" (workflow step 3), with
the guard rails from the conflicts table: constructed opinions are allowed, invented experiences are not; "I" only when it carries
a real fact; asides only in long-form.

## 10. Leave these alone

FAQ questions; one "No card required" by the CTA; a list of three when there really are three; a single "without" headline; a
clause after a comma that adds a new fact; a formal brand voice that makes specific claims; legal and compliance wording; direct
quotes; required product names.

## 11. Rewrite rules

1. Rewrite from the facts: the mechanism, the number, the customer, the step. Not from a thesaurus.
2. Specificity test: every claim sentence has a number, a name, a mechanism or a concrete action.
3. Swap test: if it works unchanged on a competitor's site, rewrite it, or flag `[NEED: differentiator vs named competitors]`.
4. Stacking test: two or more Cap patterns in one paragraph means rewrite the paragraph.
5. Don't invent to de-slop. Mark `[NEED: proof]` and ask.
6. Choose devices on purpose. One fragment you picked is copywriting; the same device on every line is slop.
7. Keep the brand's register. Don't flatten an enterprise voice into clipped startup copy, which is its own tell.
8. Vary the fixes. If every reveal becomes ", because..." that is the new tic.
9. Across a batch (ads, subject lines, SMS variants), vary sentence shapes; ten fine lines with one shape read as generated.

## 12. The self-check (run before delivering)

1. Search short copy for "not ", "isn't", "no ", "without", "?", ":" and dashes; check each hit against S1-S5 and S8.
2. Read every sentence over 20 words; more than two commas -> check for S3.
3. Count caps per section (fragments, threes, cap vocabulary).
4. Read aloud; mark anything that sounds like a press release or a LinkedIn post.
5. Swap test on the headline, subhead and every section heading.
6. Second-generation scan: the last line of every section (tidy closer?), wisdom-shaped sentences, section lengths (all equal?).
7. If a fix needs a fact you don't have, flag it; don't write around it.
