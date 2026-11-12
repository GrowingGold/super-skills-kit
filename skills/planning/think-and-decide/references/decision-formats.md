# Decision formats (merged from grilling, think, council, product-lens, domain-modeling + the user's review cards)

Use the one that fits the mode. All of them stay short: they are read on a phone.

## 1. Grilling round [grilling]

```
**Q1 - <question title>**: <question body; may include the choices>

-> Recommended: <your answer>

---

**Q2 - <question title>**: <...>

-> Recommended: <your answer>
```

- Word each question so "yes" accepts the recommendation.
- Only frontier questions (prerequisites settled). Downstream ones wait for the next round.
- Facts you are still looking up: say "checking X, Q4-Q5 wait on it", ask the rest now.

## 2. Decision card for the user's review page [visual approval protocol]

One card per decision or change. Fields:

| Field | Content |
|---|---|
| Title | Plain words, what is being decided |
| Old | Current text / state / behavior (verbatim where it exists) |
| New | Proposed text / state / behavior, side by side with Old |
| Why | 1-3 plain sentences; the evidence (Observed) behind it |
| Risk / undo | What could go wrong, how it would show, how to undo |
| Pick | accept (tagged "suggested") / alternative / keep original / my own wording |
| Note | Free text. A note always beats the radio. |

Page extras: an "accept all my suggestions" button for the rest; picks save themselves to the page store; Claude reads them back
(Artifact `read_db`) and copies them into the project folder with the date before building. Load `artifact-design` and
`artifact-capabilities` before writing the page.

## 3. Think decision record [think]

```markdown
## Decision
<recommendation or artifact>

## Evidence
<observed facts and the important inferences (with their bridge)>

## Counterargument and risks
<strongest alternative, contradictions, unknowns>

## Verification
<checks performed (commands, sources) and checks still needed>

## Growth loop
<feedback signal, revisit condition, reusable lesson>
```

Think-lite = Decision + Evidence + Counterargument and risks, three lines each.

## 4. Council [council]

Voice prompt (each fresh subagent gets only this):

```text
You are the <Skeptic | Pragmatist | Critic> on a four-voice decision council.

Question:
<one-sentence decision question>

Context:
<only the snippets, numbers or constraints that matter>

Respond with:
1. Position - 1-2 sentences
2. Reasoning - 3 concise bullets
3. Risk - biggest risk in your recommendation
4. Surprise - one thing the other voices may miss

Be direct. No hedging. Under 300 words.
```

Verdict:

```markdown
## Council: <short decision title>
**Architect:** <position> - <why, one line>
**Skeptic:** <position> - <why>
**Pragmatist:** <position> - <why>
**Critic:** <position> - <why>

### Verdict
- **Consensus:** <where they align>
- **Strongest dissent:** <most important disagreement>
- **Premise check:** <did the Skeptic challenge the question itself?>
- **Recommendation:** <the synthesized path; say if a voice changed it>
```

## 5. Product brief [product-lens]

```markdown
# Product brief: <name>   (date)
1. Who is this for: <a specific person>
2. The pain: <how often, how bad, what they do today>
3. Why now: <what changed>
4. 10-star version: <unlimited time/money>
5. MVP: <smallest thing that proves the thesis>
6. Anti-goal: <what we are explicitly not building>
7. How we know it works: <metric + target>
Risks: <top 3>
Recommendation: GO / NO-GO / GO IF <condition>  ->  next step: <one concrete action>
```

ICE table (impact 1-5 x confidence 1-5 / effort 1-5):

| Option | Impact | Confidence | Effort | ICE | Evidence for the scores |
|---|---|---|---|---|---|

Rank, apply constraints (runway, team size, dependencies), keep the top 2-3 with rationale.

## 6. ADR and glossary entry [domain-modeling]

```md
# <Short title of the decision>

<1-3 sentences: the context, what we decided, and why.>
```

Only when hard to reverse + surprising without context + a real tradeoff. File: `docs/adr/NNNN-slug.md` (repo) or a dated entry in the
project doc (ops).

```md
**Order**:
A customer's request to buy one or more products, from placement until delivery or cancellation.
_Avoid_: Purchase, transaction
```

## 7. Prototype header [prototype]

First visible block of any prototype:

```
PROTOTYPE - throwaway. Question: <the one question this answers>.
How to use: <click the walkthrough tabs / flip ?variant=A..C>.
Assumption (if the user wasn't around to confirm the branch): <logic vs UI choice and why>.
```

When it is done, write the verdict next to the question: "<variant/model> won because <reason>; settled <date>".
