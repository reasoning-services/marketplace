---
name: structured-reflection
description: "Use when thinking feels muddy, circular, or stuck. Runs an isolated reflection session — won't pollute your main context. Invoke with: 'I'm stuck', 'talk this through', 'help me think out loud', 'something feels wrong but I can't name it', 'I keep coming back to this'."
---

# Structured Reflection

Runs an isolated reflection session on a problem. The session state is completely separate from your main conversation — it cannot see this context and will not be contaminated by it.

## Input Framing

A good reflection prompt:
- States the situation, not just the question: "I'm choosing between X and Y. I'm leaning toward X but something feels off."
- Includes what's already been tried or thought through
- Names the sticking point explicitly if you can identify it

A poor reflection prompt:
- "Help me think about my codebase" — too open, nothing to reflect on
- Single words or single phrases — the session needs enough context to work with
- "What should I do?" without any stated situation — this is a decision question, not a reflection question

## Tool Invocation

Call the `reflect` tool with your content and a chosen style:

- `analytical` — examines the situation systematically, identifies patterns and gaps in reasoning
- `challenging` — actively pushes back, surfaces hidden assumptions, does not accept the framing at face value
- `conversational` — collaborative tone, helps externalize thinking without confrontation
- `quick` — brief, high-signal responses that surface the one or two most important observations

Run multiple turns. Each `reflect` call builds on prior session state. The session becomes more useful as it accumulates context.

Call `get_insights` to retrieve synthesized takeaways. Don't call it after the first turn — wait until the session has developed substance.

## Output Interpretation

The tool returns:
- **Reflection content**: the session's response to your input, built on the accumulated session state
- **Insights** (on `get_insights`): structured takeaways distilled from the full session arc

Insights are synthesized from the complete session, not just the last turn. If insights feel shallow, the session needs more turns before synthesis is meaningful.

**On scores or confidence levels**: if the tool returns them, relative ordering is the signal. Absolute values are less reliable. If everything clusters at the same level, the inputs are not differentiating enough.

## Anti-Patterns

**Don't use for decisions between concrete options.** If you have a defined option set with real trade-offs, that's decision-matrix territory.

**Don't use for stakeholder or perspective analysis.** That's context-switcher.

**Don't use reflection as a substitute for missing information.** Reflection surfaces what is already known or believed — it cannot supply facts that aren't there.

**Don't call get_insights immediately.** A 1–2 turn session has not developed enough material for synthesis to be useful.

## Intensity Adaptation

Adjust style and turn count based on what the user signals:

| Signal | Style | Turns | get_insights |
|--------|-------|-------|--------------|
| "challenge me", "push back", "go deep", "don't let me off easy" | `challenging` | 8–12 | Midpoint (turns 5–6) + conclusion |
| "quick take", "rubber duck", "help me unstick", "just let me think" | `conversational` or `quick` | 3–4 | Conclusion only |
| No signal | `analytical` | 5–7 | Conclusion only |

For deep sessions in challenging mode: the midpoint get_insights call serves as a redirect — surface what the session has established so far, then use the remaining turns to push into what hasn't been resolved yet.

See `references/DEPTH-STAGES.md` for stage definitions and transition signals.
