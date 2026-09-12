---
name: red-teaming-ideas
description: "Attack a plan from hostile perspectives before committing to it. Use when stakes are high, the room agrees too easily, or resources are about to be spent on an untested assumption."
---

# Devil's Advocate — Adversarial Review

Runs in an isolated MCP session via the `devils-advocate` server. Generates systematic challenges from attacker, competitor, skeptic and pessimist viewpoints — deliberately outside the conversation, so the critique is not shaped by the reasoning that produced the idea.

Self-critique inside a conversation is weak for a structural reason: the same context that generated the plan also generates the objections, so it finds the flaws it was already positioned to see. Isolation is what makes the challenge real.

## When This Is the Right Tool

- Significant resources or time are about to be committed
- Every stakeholder agrees — unanimity is a warning sign, not a green light
- Failure would be expensive, public, or hard to reverse
- Someone needs to argue the other side and nobody in the room will

**Not this tool when:** the decision is cheap and reversible, the user needs encouragement rather than scrutiny, or the plan is still too vague to attack — vague plans need `structured-reflection` first.

## Starting a Session

`start_adversarial_analysis(idea, context, stakes)` — all three are required, and the quality of everything downstream depends on `stakes` being concrete.

- **idea** — what is being proposed, in one or two sentences
- **context** — the constraints that make this hard: team size, timeline, existing systems, political realities
- **stakes** — what it costs if this is wrong. "It would be bad" produces generic challenges. "Six-month rewrite and we miss the enterprise deal" produces specific ones.

Optional `perspectives` lets you name the adversarial lenses up front. Returns a `session_id` that every subsequent call needs.

## The Analyses

Run the ones that fit. They are independent, not a required sequence.

**`challenge_assumptions(session_id, focus_area)`** — surfaces the implicit beliefs the plan rests on. The highest-yield call in most sessions, because the dangerous assumptions are the ones nobody stated out loud. Use `focus_area` to aim it ("operational complexity versus team size").

**`run_premortem(session_id, time_horizon)`** — imagines the plan has already failed spectacularly, then works backwards to why. Far more productive than asking "what could go wrong?", which invites hedged answers. Set `time_horizon` to when failure would become undeniable — six months, one release, the first audit.

**`attack_tree_analysis(session_id, goal)`** — maps how an adversary achieves a goal against your system, from high-level objective down to concrete attack paths. `goal` is the attacker's objective ("exfiltrate customer records"), not yours. Security-shaped work, but it applies to any plan with an opponent — including competitors and regulators.

**`analyze_argument_structure(argument_text)`** — no session needed. Takes raw argument text and returns fallacies, contradictions, and unsupported claims. Use it on a written proposal, an RFC, or a paragraph you are about to send.

**`generate_targeted_challenges(argument_text, perspective, max_challenges)`** — also sessionless. Reads an argument and writes challenge questions tailored to the perspective you name. Good for preparing to defend a proposal before the meeting rather than during it.

**`add_perspective(session_id, name, description, custom_prompt)`** — when the standard lenses miss your domain. A regulated-industry plan may need a compliance auditor; a consumer product may need a hostile journalist.

## Synthesizing

`synthesize_challenges(session_id)` — clusters findings across every analysis, resolves conflicts between perspectives, and returns prioritized recommendations.

**Call this before reporting back.** Raw challenges from four perspectives overlap heavily and arrive unranked; handing the user thirty objections is not a review, it is noise. The synthesis is the deliverable.

## Presenting Results

- **Lead with the challenges that would actually change the decision.** A long list of survivable objections buries the one that matters.
- **Separate fatal from costly from annoying.** These demand different responses, and collapsing them is how real risks get filed alongside nitpicks.
- **Do not soften the findings.** The user asked to be attacked. Delivering a gentle version defeats the purpose and wastes the session.
- **Do not treat every challenge as a required fix.** Some risks are correctly accepted. Say which ones you would accept and why — that judgement is part of the work.
- **Report when the idea held up.** An idea that survives serious attack is a stronger result than one that was never tested. Say so plainly rather than manufacturing concerns to justify the session.

## Anti-Patterns

- **Running it after the decision is made.** Adversarial review used to validate a commitment is theatre. Run it while the answer can still change.
- **Vague stakes.** The single biggest driver of generic output.
- **Skipping synthesis.** See above — unclustered challenges are noise.
- **Using it on someone else's idea to win an argument.** The tool finds flaws in anything, including good plans. Weaponized, it produces a one-sided case that looks rigorous.
- **Attacking a plan that is still a vibe.** There must be something specific enough to be wrong.

## Chaining

Adversarial review belongs late, after there is something worth attacking:

1. `graph-of-thought` or `decision-matrix` → produce a candidate
2. **`devils-advocate`** → attack it
3. `sequential-thinking` → trace the implications of the surviving objections

A premortem that kills the candidate sends you back to step 1 — which is the system working, not a wasted session.

See the [`reasoning-chain` skill](../reasoning-chain/SKILL.md) for output-threading discipline.
