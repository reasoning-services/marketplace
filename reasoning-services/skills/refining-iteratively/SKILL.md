---
name: refining-iteratively
description: "Run draft, critique, revise until the output stops improving, with convergence measured rather than guessed. Use when the first draft is never the deliverable and quality matters more than speed."
---

# Iterative Refinement — Draft, Critique, Revise, Converge

Runs in an isolated MCP session via the `iterative-refinement` server. Implements a Draft → Critique → Revise → Converge loop with **measured** convergence: the session tracks how much each iteration actually changed the output and stops when the changes stop mattering.

The isolation matters more here than almost anywhere else. Self-critique inside a conversation degrades fast — the model that wrote the draft is primed to defend it, and each round tends to elaborate rather than improve. Running the loop outside the conversation breaks that attachment, and the convergence metric replaces the usual stopping rule, which is whoever gets bored first.

## When This Is the Right Tool

- Writing that has to be right: a spec, an ADR, an incident report, external copy
- A definition, policy or explanation that must survive being read adversarially
- Any artifact where the first draft is reliably not the deliverable

**Not this tool when:** the task has a verifiable correct answer (use a solver or a test), speed beats polish, or nothing has been drafted yet — refinement needs something to refine.

## The Loop

**`start_refinement(prompt, domain)`** — begins a session. `prompt` is what you want produced, stated as an instruction with its quality bar, not just a topic. "Write an ADR for the caching decision" is thin; "Write an ADR for the caching decision that a new engineer could act on without asking follow-up questions" gives the critique pass something to measure against.

Set `domain` when you know it — it selects domain-appropriate critique. Leave it off and the service detects one.

**`continue_refinement(session_id)`** — advances exactly one draft→critique→revise cycle and reports convergence. Call it repeatedly. Omit `session_id` to advance the current session.

Stepping one iteration at a time is the point: you can read each cycle's critique and stop early when a revision goes sideways. Fire-and-forget refinement occasionally polishes its way past the good version.

**`get_refinement_status(session_id)`** — convergence metrics and iteration state without advancing. Use it to decide whether another round is worth it.

**`current_session()`** — the active session's details without needing its id.

**`list_refinement_sessions()`** — paginated list of active sessions, with `cursor` and `page_size`. Use it when returning to work you left open.

## Reading Convergence

Convergence measures how much the latest revision changed. It is a stopping signal, not a quality score.

- **Still changing substantially** — keep going; the loop is finding real improvements.
- **Changes have gone cosmetic** — stop. Further iterations rearrange rather than improve.
- **Converged** — the loop is done. More rounds cost tokens and risk drift.

**A converged draft is not automatically a good one.** Convergence means the process stabilized, which can also mean it stabilized on something mediocre. If the converged output is weak, the fix is a better `prompt` with a sharper quality bar, not more iterations.

Watch for the opposite failure too: an output that keeps changing every round without getting better usually means the prompt is underspecified, so each critique pass optimizes for something different.

## Presenting Results

- **Deliver the final draft, not the history.** Nobody wants the intermediate versions unless they asked.
- **Say what the loop changed.** One line — "tightened the failure-mode section and cut the duplicated rationale" — tells the user whether the work was worth it.
- **Report the iteration count and convergence.** "Converged after four rounds" is useful; "I refined it" is not.
- **Flag it when you stopped early.** If you halted because a revision was getting worse, say so and say which version you kept.
- **Keep your own judgement.** The converged draft is a strong candidate, not a verdict. If it lost something the earlier version had, fix it.

## Anti-Patterns

- **Refining a fundamentally wrong draft.** The loop improves execution, not premises. A well-polished wrong answer is worse than a rough right one, because polish reads as confidence.
- **Running it on something already good enough.** Diminishing returns arrive faster than they feel like they should.
- **Ignoring convergence and iterating a fixed number of times.** The measurement is the feature; overriding it with a habit throws it away.
- **Using it for factual accuracy.** Refinement makes text better, not truer. Verify facts separately — `formal-logic` for entailment, real sources for claims.
- **Leaving sessions open across unrelated work.** `current_session` will hand you the wrong one.

## Chaining

Refinement is a finishing pass, so it goes last:

1. `graph-of-thought` or `structured-reflection` → work out what to say
2. `devils-advocate` → find what the draft gets wrong
3. **`iterative-refinement`** → make the surviving content good

Refining before the content is settled polishes text you are about to throw away.

See the [`reasoning-chain` skill](../reasoning-chain/SKILL.md) for output-threading discipline.
