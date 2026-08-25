---
name: reasoning-chain
description: "Orchestrate multi-tool reasoning when one tool is not enough. Use for high-stakes problems spanning unclear framing, real options, and stakeholder impact. Pattern: Reflect then Explore then Decide."
---

# Reasoning Chain — Multi-Tool Orchestration

Chains multiple reasoning.services tools for complex problems. Output from each stage feeds explicitly into the setup of the next.

## When Chaining Adds Value

Chain when:
- The problem framing is unclear AND options need evaluation — framing must be resolved before the matrix is set up
- Multiple stakeholder perspectives are needed AND a decision must follow — don't evaluate options without knowing who is affected
- A reflection session revealed something that changes which perspectives are relevant

**When chaining does not add value:**
- One tool is sufficient — don't add tools to appear thorough
- The outputs of stage N would be ignored when setting up stage N+1
- The user needs a quick answer — a three-tool chain is not the response to "just help me pick"

## Available Patterns

### Pattern 1: Reflect -> Explore -> Decide (Most Common)

`Structured Reflection -> Context Switcher -> Decision Matrix`

**When**: The user faces a decision but the problem framing is unclear — they don't yet know what they're actually deciding.

**Workflow:**
1. **Reflect**: Articulate the actual problem. What is really being decided? What assumptions are embedded in the current framing? Pass the raw confusion — don't pre-filter. Output: Clarified problem statement, separated concerns, named assumptions.
2. **Explore**: Run the clarified problem through relevant perspectives. Who is affected? What concerns won't surface without explicit perspective analysis? Feed the reflection output as the topic. Pick perspectives based on what the reflection revealed. Output: Per-perspective analysis, points of agreement, genuine tensions.
3. **Decide**: Set up the matrix using options and criteria informed by stages 1 and 2. Use tensions from context-switcher as weighted criteria. Use options that emerged from the full analysis, not just the original ones. Weights should reflect what reflection and perspective analysis revealed as actually important. Output: Weighted scores, winner with margin, sensitivity analysis.

**Synthesis (yours to do):** Combine all three outputs. Lead with the matrix winner but qualify it with the reflection's nuance and the perspectives' concerns.

---

### Pattern 2: Explore -> Deep-Dive -> Decide

`Context Switcher -> Sequential Thinking -> Decision Matrix`

**When**: The options are known but the stakeholder impact and logical implications need to be traced before evaluating.

**Workflow:**
1. **Explore**: Run stakeholder perspectives. Identify the 2-3 genuine tensions between groups.
2. **Deep-Dive**: Use sequential thinking to trace the logical implications of each tension. What does each resolution path lead to? What is logically ruled out?
3. **Decide**: Set up the matrix with options that address the tensions from stage 1, criteria derived from stakeholder priorities, and constraints from the sequential analysis in stage 2.

---

### Pattern 3: Reflect -> Deep-Dive

`Structured Reflection -> Sequential Thinking`

**When**: Problem is unclear AND technical, but doesn't have multiple stakeholders.

**Workflow:**
1. **Reflect**: Separate the tangled concerns.
2. **Deep-Dive**: Take the most important thread and reason through it linearly.

---

### Pattern 4: Reflect -> Decide

`Structured Reflection -> Decision Matrix`

**When**: Options are clear but what matters is not. The user needs to clarify their actual priorities before scoring.

**Workflow:**
1. **Reflect**: What does success look like? What is the user actually optimizing for, versus what they say they're optimizing for?
2. **Decide**: Set up the matrix with weights directly informed by what the reflection session surfaced.

---

### Pattern 5: Explore -> Explore (Rare)

`Context Switcher -> Context Switcher`

**When**: Initial perspectives surfaced a completely unexpected concern needing its own analysis.

**Workflow:**
1. **First pass**: Run with obvious perspectives.
2. **Focused pass**: Run again focused on the surprise concern with NEW perspectives.

## Rules of Engagement

- **Don't chain for ceremony.** If the first tool answered the question, stop.
- **Thread output forward.** Each tool should receive the output of the previous one as context.
- **Synthesize between steps.** Tell the user what you learned before invoking the next tool.
- **Adapt the plan.** If reflection reveals the problem is simpler than expected, skip ahead.
- **Maximum 3 tools per chain.** More than that means the problem needs decomposition, not more tools.

## When to Suggest a Chain vs a Single Tool

| Signal | Recommendation |
|--------|---------------|
| "I don't even know what the question is" | Start with reflection, chain from there |
| Clear options, clear criteria | Single decision-matrix |
| One perspective, needs others | Single context-switcher |
| Needs step-by-step logic | Single sequential-thinking |
| "This is a big decision" + unclear scope | Chain: Reflect -> Explore -> Decide |
| Prior single-tool output was insufficient | Add one more tool, not a full chain |

## Output Threading

The key discipline of chaining is **explicit handoff**: the output of each stage must explicitly inform the setup of the next.

**Implicit (not enough):** "I ran structured reflection. Now I'll set up a decision matrix."

**Explicit (what's required):** "The reflection identified that the real concern is long-term maintainability, not initial velocity. Setting up the matrix with 'maintainability over 18 months' weighted at 5 and 'time-to-first-deploy' weighted at 2."

Explicit threading is the difference between three isolated sessions and one coherent reasoning workflow.

## Adapting Mid-Chain

A chain plan is not fixed once started. Adaptation is expected.

**Triggers to stop early:**
- Reflection resolves the decision outright — skip the matrix
- Perspective analysis reveals constraints that eliminate all but one option — skip evaluation, proceed to implementation planning
- Sequential analysis surfaces a contradiction that invalidates the original option set — add options before running the matrix

**Triggers to revise:**
- Stage 1 reveals the problem was different than expected — revise the plan before running stage 2
- A new option surfaces in stage 2 — add it to the matrix before scoring
- User disengages ("just pick one") — summarize what you have and make a recommendation

## Anti-Patterns

- **Don't run all three tools on every complex problem.** Match the chain to the actual problem structure. Two well-connected tools beat three loosely connected ones.
- **Don't treat chain outputs as independent.** The value of chaining is the handoff. If you're not explicitly threading outputs, just run each tool separately.
- **Don't start a chain without a plan.** Know which pattern you're using and why before invoking the first tool. Improvising the chain mid-session loses the coherence.

See `references/CHAINING-PATTERNS.md` for detailed output threading examples and adaptation decision trees.

---

## Trigger Reference

Retained from the pre-2.2 frontmatter description, which exceeded the 200-character
claude.ai limit. Kept here so the routing signal is not lost; `reasoning-guide` is the
skill that acts on it.

> Orchestrate multi-tool reasoning workflows by chaining structured reflection, context switching, decision matrix, and sequential thinking. Use when a problem is too complex for a single reasoning tool, when the user explicitly wants a thorough multi-angle analysis, when stakes are high enough to justify the investment (architecture decisions, strategic pivots, major technical bets), or when prior single-tool results were insufficient. Triggers on "analyze this thoroughly", "give me the full treatment", "I need a comprehensive analysis", "this is a big decision", "chain the reasoning tools", "go deep on this", "high-stakes decision", "bet-the-company", "I want multiple angles AND a structured comparison". Do NOT use for routine decisions — single tools are usually enough.
