---
name: sequential-thinking
description: "Use when a problem needs step-by-step linear reasoning with explicit confidence tracking and dependency mapping. Maintains an auditable reasoning chain. Invoke with: 'step by step', 'walk me through', 'trace this logic', 'show your reasoning', 'prove this', 'what follows from'."
---

# Sequential Thinking

Builds a linear reasoning chain with explicit confidence, dependency tracking, and contradiction detection. Each step in the chain is discrete and auditable.

## When to Use This Over Other Tools

Use sequential thinking when:
- Steps have explicit dependencies (step 4 cannot be evaluated until step 2 is resolved)
- The reasoning must be shown — for documentation, communication, or verification
- Contradictions across steps need to be formally detected and resolved
- Confidence varies across steps and that variance is meaningful to capture

Use structured-reflection instead when the problem is fuzzy or unstructured. Sequential thinking requires well-defined premises to produce value.

## Setting Up the Chain

Set `total_thoughts` before starting. Match it to the problem:
- Simple verification: `3–4`
- Moderate analysis: `5–8`
- Deep argument construction: `10–15`

If the chain needs extension mid-session, state it explicitly before adding steps. Most server implementations support extending the chain.

## Stage Structure

Each `process_thought` call is one step. The server maintains chain state across calls.

**Stage mapping by problem type:**

*Problem Definition → Analysis → Conclusion*: sufficient for well-scoped problems where the question is already clearly defined.

*Problem Definition → Information Gathering → Analysis → Synthesis → Conclusion*: for complex problems requiring research, multi-source integration, or building a complete argument that must hold under scrutiny.

## Confidence Tracking

Assign confidence per step (range: 0.0–1.0).

**What confidence measures**: your certainty that this step's premise or conclusion is correct given everything established in prior steps.

**Low confidence is useful information.** Don't inflate it. A chain that correctly identifies "I'm 40% confident in step 3" is more valuable than one that suppresses uncertainty.

**Confidence propagates**: if step 3 has 0.4 confidence and step 5 depends on step 3, step 5's confidence ceiling is 0.4 regardless of how well-reasoned step 5 is internally.

## Contradiction Detection

When a step contradicts an earlier step, flag it explicitly rather than silently overriding.

How to handle contradictions:
1. Flag which steps are in tension and why
2. Identify the source: new information, different assumption, scope change
3. Resolve by revising the earlier step or branching the chain

Don't continue a chain with unresolved contradictions. Downstream steps inherit the inconsistency and the conclusion will be internally invalid.

## Output Interpretation

The chain output contains steps in sequence with their content, confidence per step, explicit dependencies, flagged contradictions, and a summary at the chain end.

**What makes a high-quality chain:**
- Confidence varies across steps — uniform high confidence throughout indicates the problem wasn't analyzed with real rigor
- Dependencies are explicit — each step references what it builds on
- The conclusion is derived from preceding steps, not introduced fresh at the end

## Anti-Patterns

**Don't use for open-ended or exploratory problems.** "What should I build?" is not a sequential reasoning problem — it belongs in structured-reflection or decision-matrix.

**Don't set total_thoughts too low for complex problems.** A 3-step chain on an architecture decision will be shallow. Match chain length to problem complexity.

**Don't ignore contradictions.** Resolving them is how the chain produces trustworthy output. Flagging and skipping is not resolution.

**Don't use when you're not actually tracking dependencies.** If every step is independent, this is just a list. Sequential thinking adds no value over simple enumeration when there are no real dependencies.

## Intensity Adaptation

| Signal | total_thoughts | Stages | Assumptions per step |
|--------|---------------|--------|---------------------|
| "deep dive", "ultrathink", "prove this", "build the full argument" | 10–15 | All 5 | 2+ per step, explicit |
| "quick", "just trace this", "sketch this out", "gut check" | 3–4 | Problem Definition → Analysis → Conclusion | Skip |
| No signal | 5–8 | Matched to problem shape | As they arise |

See `references/STAGE-GUIDE.md` for stage definitions, confidence calibration, and contradiction handling patterns.
