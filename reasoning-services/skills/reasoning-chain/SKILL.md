---
name: reasoning-chain
description: "Orchestrates multi-tool reasoning workflows when one tool is insufficient. Chains output from each stage into the next. Invoke with: 'I need to reflect then decide', 'chain these reasoning tools', 'multi-step analysis', 'this needs more than one approach', 'explore perspectives then decide'."
---

# Reasoning Chain

Chains multiple reasoning tools into a single workflow. Output from each stage feeds explicitly into the setup of the next.

## When Chaining Adds Value

Chain when:
- The problem framing is unclear AND options need evaluation — framing must be resolved before the matrix is set up
- Multiple stakeholder perspectives are needed AND a decision must follow — don't evaluate options without knowing who is affected
- A reflection session revealed something that changes which perspectives are relevant

**When chaining does not add value:**
- One tool is sufficient — don't add tools to appear thorough
- The outputs of stage N would be ignored when setting up stage N+1
- The user needs a quick answer — a three-tool chain is not the response to "just help me pick"

## Core Chaining Patterns

### Reflect → Explore → Decide

`Structured Reflection → Context Switcher → Decision Matrix`

**When**: The user faces a decision but the problem framing is unclear — they don't yet know what they're actually deciding.

**Workflow:**
1. **Reflect**: Articulate the actual problem. What is really being decided? What assumptions are embedded in the current framing?
2. **Explore**: Run the clarified problem through relevant perspectives. Who is affected? What concerns won't surface without explicit perspective analysis?
3. **Decide**: Set up the matrix using options and criteria informed by stages 1 and 2. Weights should reflect what reflection and perspective analysis revealed as actually important.

**Handoff discipline**: The clarified problem from Reflect informs the framing passed to Context Switcher. The concerns surfaced in Explore inform the criteria added to the matrix.

---

### Explore → Deep-Dive → Decide

`Context Switcher → Sequential Thinking → Decision Matrix`

**When**: The options are known but the stakeholder impact and logical implications need to be traced before evaluating.

**Workflow:**
1. **Explore**: Run stakeholder perspectives. Identify the 2–3 genuine tensions between groups.
2. **Deep-Dive**: Use sequential thinking to trace the logical implications of each tension. What does each resolution path lead to? What is logically ruled out?
3. **Decide**: Set up the matrix with options that address the tensions from stage 1, criteria derived from stakeholder priorities, and constraints from the sequential analysis in stage 2.

**Handoff discipline**: Perspective tensions from Explore become constraints and criteria in the matrix. The sequential analysis rules out options that are logically invalid before the matrix runs.

---

### Reflect → Decide

`Structured Reflection → Decision Matrix`

**When**: Options are clear but what matters is not. The user needs to clarify their actual priorities before scoring.

**Workflow:**
1. **Reflect**: What does success look like? What is the user actually optimizing for, versus what they say they're optimizing for?
2. **Decide**: Set up the matrix with weights directly informed by what the reflection session surfaced.

**Handoff discipline**: Weights in the matrix reflect the priorities that reflection identified — not the priorities stated before the session.

---

## Output Threading

The key discipline of chaining is **explicit handoff**: the output of each stage must explicitly inform the setup of the next.

**Implicit (not enough):** "I ran structured reflection. Now I'll set up a decision matrix."

**Explicit (what's required):** "The reflection identified that the real concern is long-term maintainability, not initial velocity. Setting up the matrix with 'maintainability over 18 months' weighted at 5 and 'time-to-first-deploy' weighted at 2."

Explicit threading is the difference between three isolated sessions and one coherent reasoning workflow.

## Adapting Mid-Chain

A chain plan is not fixed once started. Adaptation is expected.

**Triggers to stop early:**
- Reflection resolves the decision outright → skip the matrix
- Perspective analysis reveals constraints that eliminate all but one option → skip evaluation, proceed to implementation planning
- Sequential analysis surfaces a contradiction that invalidates the original option set → add options before running the matrix

**Triggers to revise:**
- Stage 1 reveals the problem was different than expected → revise the plan before running stage 2
- A new option surfaces in stage 2 → add it to the matrix before scoring

## Anti-Patterns

**Don't run all three tools on every complex problem.** Match the chain to the actual problem structure. Two well-connected tools beat three loosely connected ones.

**Don't treat chain outputs as independent.** The value of chaining is the handoff. If you're not explicitly threading outputs, just run each tool separately.

**Don't start a chain without a plan.** Know which pattern you're using and why before invoking the first tool. Improvising the chain mid-session loses the coherence.

See `references/CHAINING-PATTERNS.md` for detailed output threading examples and adaptation decision trees.
