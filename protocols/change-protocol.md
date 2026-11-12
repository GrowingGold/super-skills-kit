# Change protocol

Use this before any fix or change to something live: automations, databases, dashboards, apps, sites, agents. The goal is to solve the problem, not to create new ones.

## 1. Prove the problem

- Trace every step of the real path with real data: runs, rows, payloads, logs.
- Check every copy or variant, not just one.
- Double-check the diagnosis. Does it explain every case? Is there a second cause?

## 2. Game out the fix system-wide

- List everything that reads or writes what you will change: downstream steps and how they use the data, database triggers, other automations, dashboards, scheduled checks, other copies.
- Replay the fix on recent real data and compare old against new.
- Write down what could go wrong and how it would show up.

## 3. Adjust and repeat

Any adjustment sends you back through steps 1 and 2.

## 4. Present, then apply

Present through the review page described in `~/.claude/super-skills-kit/protocols/visual-approval.md`. It carries:

- the evidence
- the fix
- the impact list
- the replay result
- the risks
- how to undo it

Apply only what the user picked.

## 5. After applying

Watch the first real runs end to end in the destination system, not only the new step's output. Keep checking the runs that follow for a while.

## Always

Ask first before anything outward-facing or paid: send, call, publish, buy, invite.
