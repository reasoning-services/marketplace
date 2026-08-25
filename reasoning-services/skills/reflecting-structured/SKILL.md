---
name: reflecting-structured
description: "Work through muddy, circular or stuck thinking in an isolated reflection session. Use when a problem needs articulation before it can be solved, or the main thread is too cluttered to think in."
---

# Structured Reflection — Isolated Thinking Sessions

Runs in an isolated MCP session via `structured-reflection` server. The session state is completely separate from your main conversation — it cannot see this context and will not be contaminated by it.

## When This Tool Shines

Structured reflection is for problems where **the problem itself is unclear**. If you can already name the problem precisely, you probably need a different tool. This one is for:

- "I know something is wrong with this architecture but I can't name what"
- "I keep redesigning this and nothing feels right"
- "There are three things tangled together and I need to separate them"
- The user has been talking for 5+ messages and hasn't landed on anything concrete

## Before Invoking

### Frame the Opening, Not the Solution

Start the reflection session with the *confusion*, not a hypothesis:

**Good:** "I'm designing an auth system and I keep going back and forth between JWT and sessions. I think the real confusion is that I don't know what my actual threat model is."

**Bad:** "Should I use JWT or sessions?" (That's a decision-matrix problem, not a reflection problem.)

A good reflection prompt:
- States the situation, not just the question: "I'm choosing between X and Y. I'm leaning toward X but something feels off."
- Includes what's already been tried or thought through
- Names the sticking point explicitly if you can identify it

A poor reflection prompt:
- "Help me think about my codebase" — too open, nothing to reflect on
- Single words or single phrases — the session needs enough context to work with
- "What should I do?" without any stated situation — this is a decision question, not a reflection question

### Choose the Right Style

- **Conversational** (default): Exploratory, follow the thread
- **Analytical**: Structured decomposition, good for technical tangles
- **Challenging**: Pushes back on assumptions, good when the user needs to be unstuck from a position
- **Supportive**: Gentler framing, probes without pressure — still asks hard questions
- **Quick**: Fast synthesis, good when time-constrained

## During the Session

The tool adapts over the course of a session:

- **Early turns (1-5):** Exploratory. Wide search. Follow the user's threads. The stated problem may not be the actual problem — surface-level articulation often describes symptoms.
- **Mid turns (6-11):** Focused. Synthesize themes, name patterns, connect threads. Hidden premises surface. What is being taken for granted?
- **Late turns (12+):** Convergent. Drive toward key insight, name takeaways, suggest next action. What has changed in how the problem is understood?

If the session feels like it's going in circles after 8-10 turns, it's time to synthesize and close, not keep exploring.

## Tool Invocation

Call `start_reflection` with your content and a chosen style.

Run multiple turns using `reflect`. Each call builds on prior session state. The session becomes more useful as it accumulates context.

Call `get_insights` to retrieve synthesized takeaways. Don't call it after the first turn — wait until the session has developed substance.

## Intensity Adaptation

This tool adapts session depth based on your framing:

**Deep mode** (triggered by: "challenge me", "push back", "go deep", "don't let me off easy"):
- Style: challenging — actively pushes back on assumptions
- 8-12 reflection turns before concluding
- Midpoint insight extraction at turn 5-6 to reframe the second half
- Push past first clarity — the obvious answer is often a defense against the real one

**Quick mode** (triggered by: "quick take", "help me unstick", "rubber duck this"):
- Style: conversational or quick
- 3-4 reflection turns, then conclude
- Optimize for the single most useful reframe, not comprehensive exploration

**Default** (no explicit signal): style: analytical, 5-7 turns, conclude when genuine new insight stops emerging.

## Interpreting Results

The output is a thinking partner's contribution, not an answer. When bringing results back:

- **Name the clarity that emerged.** "The reflection surfaced that your actual problem isn't auth mechanism — it's that you haven't defined your trust boundaries."
- **Don't over-quote the session.** Synthesize in your own words. The user doesn't need the full transcript.
- **Suggest the next tool.** Reflection often reveals that the real problem is suitable for another tool: a decision (matrix), a multi-stakeholder concern (context-switcher), or a step-by-step breakdown (sequential-thinking).
- **On scores or confidence levels**: if the tool returns them, relative ordering is the signal. Absolute values are less reliable.

## Anti-Patterns

- **Don't use for decisions between concrete options.** If you have a defined option set with real trade-offs, that's decision-matrix territory.
- **Don't use for stakeholder or perspective analysis.** That's context-switcher.
- **Don't use reflection as a substitute for missing information.** Reflection surfaces what is already known or believed — it cannot supply facts that aren't there.
- **Don't call get_insights immediately.** A 1-2 turn session has not developed enough material for synthesis to be useful.

## Chaining

Structured Reflection is the natural FIRST step:

1. **`structured-reflection`** → articulate the actual problem
2. `context-switcher` → explore it from multiple angles
3. `decision-matrix` → score concrete options that emerged

See `references/DEPTH-STAGES.md` for stage definitions and transition signals.

---

## Trigger Reference

Retained from the pre-2.2 frontmatter description, which exceeded the 200-character
claude.ai limit. Kept here so the routing signal is not lost; `reasoning-guide` is the
skill that acts on it.

> Work through complex, muddy, or stuck thinking in an isolated reflection session. Use PROACTIVELY when the user seems stuck or going in circles, when a problem is vague and needs articulation, when the user is conflating multiple problems, when emotional weight is making technical decisions harder, when someone needs to think out loud but the main conversation is too cluttered, or when the user says they're overwhelmed. Triggers on phrases like "I'm stuck", "I can't figure out", "I keep going back and forth", "let me think about this", "this is confusing", "I don't know where to start", "help me think through", "I'm overthinking this", "something feels off but I can't name it", "I need to untangle", "my head is spinning", "rubber duck this", "talk this through with me". Do NOT use when the user has a clear question with a clear answer — just answer it. See the skill body for depth, speed, and default invocation modes.
