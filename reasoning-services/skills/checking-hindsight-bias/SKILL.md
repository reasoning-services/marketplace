---
name: checking-hindsight-bias
description: "Separate what was actually knowable at the time from what looks obvious now. Use for postmortems, retros, and any 'we should have seen it coming' that needs testing before it becomes a rule."
---

# Hindsight — Bias-Corrected Retrospection

Runs in an isolated MCP session via the `hindsight` server. Analyzes past decisions from multiple temporal perspectives to separate genuine lessons from hindsight bias.

The failure mode this exists to prevent: a team reviews an incident, concludes the warning signs were obvious, and adopts a rule that would not have fired on the information anyone actually had. That rule costs real effort and prevents nothing. Outcome knowledge contaminates judgement about what was knowable, and it does so invisibly — the corrected memory feels like the original one.

## When This Is the Right Tool

- Running a postmortem or retro on something that went wrong
- Someone is confident they "knew it all along"
- Extracting lessons that are about to become policy
- Deciding whether a pattern across incidents is real or assembled after the fact

**Not this tool when:** the question is what to do next rather than what to learn, or the outcome is not yet known — there is no hindsight to correct.

## Pick the Entry Point

Five ways in, scaled by how much you have and how much it matters.

**`quick_check(thought, reality)`** — fastest. One belief against what actually happened, optional `confidence_then`. Use mid-conversation when someone says "obviously that was going to fail" and you want it tested without derailing the discussion.

**`analyze_hindsight(thought, reality)`** — the all-in-one call, and the right default for most single decisions. Optional `confidence`, `context`, `quick`, `session_id`. Start here unless you have a reason not to.

**`reflect(situation, what_happened)`** — narrative entry. Takes the story in natural language, with optional `confidence_then`, `why_confident`, `lessons_learned`. Best when the user is telling you what happened rather than presenting a clean decision record. Passing their stated `lessons_learned` lets the tool test the lessons rather than invent new ones.

**`start_hindsight_analysis(event, outcome, initial_assessment)`** — full multi-perspective session for decisions that matter. Returns a `session_id`. Use `initial_confidence` to capture how sure they were *then*, if that is recoverable.

**`pattern_check(current_situation, past_similar_situations, past_outcomes)`** — tests whether a perceived pattern is real. Use it the moment someone says "this always happens" — accumulated anecdote and genuine pattern feel identical from the inside.

## The Call That Does the Real Work

`add_timeline_context(decisions_made, information_available, information_missing, constraints)` — the highest-value call in the service, and the one most often skipped.

All four arguments are required, and that is deliberate. Separating **information_available** from **information_missing** is the entire mechanism: it forces an explicit reconstruction of the epistemic state at decision time, before outcome knowledge leaks in. **constraints** captures what was not actually choosable — deadlines, headcount, a dependency nobody controlled. Optional `outcomes` and `session_id`.

Gather these from the user before calling. Guessing them defeats the purpose — you would be reconstructing the past from the present, which is the bias itself.

## Presenting Results

- **State what was genuinely knowable.** That is the finding everything else rests on.
- **Name the lessons that do not survive.** "We should have monitored X" dies if nothing available at the time suggested X. Retiring a false lesson is as valuable as keeping a true one — it saves the effort a useless rule would have cost.
- **Keep the lessons that do.** Bias correction is not absolution. Some failures were genuinely foreseeable, and the tool is not there to make anyone feel better.
- **Separate process from outcome.** A good decision can have a bad outcome. Teams that punish outcomes instead of process learn to avoid risk rather than to decide well.
- **Be careful with the human element.** Postmortems involve people who made the call. Report on decisions and available information, not on character.

## Anti-Patterns

- **Skipping `add_timeline_context`.** Without the knowable/unknowable split you get a summary, not a correction.
- **Using it to excuse everything.** "Nobody could have known" is sometimes true and sometimes a way to avoid a real lesson. The tool distinguishes them; do not use it to launder the second as the first.
- **Running it before the outcome is clear.** Premature retrospection on an unfinished situation produces confident nonsense.
- **Reconstructing the epistemic state from memory alone.** Memory of prior belief is exactly what hindsight corrupts. Prefer contemporaneous artifacts — the ticket, the thread, the commit message — over recollection.
- **Treating one incident as a pattern.** That is what `pattern_check` is for.

## Chaining

Hindsight feeds forward — its output is the input to the next decision:

1. **`hindsight`** → establish what was actually knowable and which lessons hold
2. `context-switcher` → how the surviving lessons land on different teams
3. `decision-matrix` → score process changes against the lessons that survived

Running the matrix first means scoring options against lessons that have not been tested.

See the [`reasoning-chain` skill](../reasoning-chain/SKILL.md) for output-threading discipline.
