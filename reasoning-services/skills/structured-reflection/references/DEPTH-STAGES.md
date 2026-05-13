# Structured Reflection: Depth Stages

Reference for managing session progression and knowing when to call `get_insights`.

Loaded into context only when the structured-reflection skill needs depth guidance.

## Stage Definitions

### Stage 1: Surface Articulation (turns 1-2)

The user states the problem. The session reflects it back with modest reframing.

**What to watch for:**
- The stated problem may not be the actual problem — surface-level articulation often describes symptoms
- Early turns establish vocabulary and framing; don't call `get_insights` here
- First-turn reflections that feel obvious are normal — the session is calibrating

**Transition signal to Stage 2:** The session or user identifies a specific tension, assumption, or constraint that is driving the problem — something beneath the surface statement.

---

### Stage 2: Assumption Excavation (turns 3-5)

The session surfaces hidden premises. What is being taken for granted? What would have to be true for this framing to hold?

**What to watch for:**
- "I've been assuming X" — this is the signal Stage 2 is working correctly
- Resistance to reframing often means the assumption is load-bearing; don't skip past it
- In `challenging` mode, this is where productive pushback intensifies

**Transition signal to Stage 3:** A specific assumption has been named and examined. The user begins considering what changes if that assumption doesn't hold.

---

### Stage 3: Consequence Mapping (turns 6-8)

Work through what follows from the assumption examination. If the key assumption doesn't hold, what does?

**What to watch for:**
- New options or framings emerging that weren't visible in Stage 1
- Forced acknowledgment of trade-offs the user was avoiding
- In `analytical` mode, patterns across prior turns become synthesizable

**Call `get_insights` here** for deep sessions — target turns 5-6. The session has accumulated enough material for meaningful synthesis. Use the midpoint insights to redirect the remaining turns toward what hasn't been resolved yet.

---

### Stage 4: Synthesis (turns 9-12, deep mode only)

Consolidation. What has changed in how the problem is understood? What is now clearer, and what remains genuinely uncertain?

**What to watch for:**
- The user restating the problem in fundamentally different terms — this is resolution
- Reduction in hedging language as clarity emerges
- Explicit separation of false uncertainty (resolved by the session) from genuine uncertainty (still open)

**Final `get_insights` call:** At the end of Stage 4. Summary of the session arc, key reframes, and what remains open.

---

## Transition Signals

| Signal | Meaning |
|--------|---------|
| "I hadn't thought of it that way" | Stage 1 to 2 transition |
| "I've been assuming..." | Stage 2 working correctly |
| "If that's wrong, then..." | Stage 2 to 3 transition |
| "So the real question is actually..." | Stage 3 synthesis emerging |
| "I think I know what I need to do" | Resolution — call `get_insights` |
| "I keep coming back to the same thing" | Session may need `challenging` mode |

## Signs the Session Should End Early

- User reached clarity before turn 12 — synthesize and close
- User is producing one-word responses — engagement dropped
- The same insight has been restated 3+ times — nothing new is emerging
- The problem turned out to be simple — close and suggest a direct answer instead

## Signs the Session Should Go Longer

- New threads keep emerging with genuine complexity
- User explicitly says "I want to keep exploring"
- Each turn is producing genuinely new insight, not restating

---

## When to End the Session

End when:
- The user has language for something they couldn't articulate before
- The key assumption has been named, examined, and either validated or challenged
- The user has a concrete next step, decision to make, or question to answer

Do not end when:
- The session has only operated at the surface problem level
- No assumption has been named or examined
- `get_insights` has not been called
- The user is still uncertain about basic problem framing

---

## get_insights Timing Reference

| Mode | Turn count | When to call |
|------|-----------|--------------|
| `quick` / `conversational` | 3-4 | At conclusion only |
| `analytical` (default) | 5-7 | At conclusion only |
| `challenging` (deep) | 8-12 | Midpoint (turns 5-6) + conclusion |

The midpoint call in challenging mode surfaces what's been established so far and explicitly redirects the remaining turns toward unresolved territory.
