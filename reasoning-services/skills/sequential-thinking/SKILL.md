---
name: thinking-sequentially
description: Step-by-step linear reasoning with confidence tracking, dependency mapping, and contradiction detection. Use PROACTIVELY when a problem requires explicit logical steps where each depends on previous conclusions, when building a proof or argument chain, when debugging complex issues systematically, when planning a multi-step process where order matters, when the user needs to show their reasoning (auditable thinking), or when you detect a logical gap in the current reasoning. Triggers on "step by step", "walk me through", "break this down logically", "what's the reasoning chain", "prove that", "trace the logic", "work through this systematically", "debug this step by step", "what follows from", "if A then B", "build the argument for", "map out the dependencies", "what order should I". Do NOT use for open-ended exploration (use structured-reflection) or parallel concerns (use context-switcher). When the user signals depth ("deep dive", "thorough", "really think about this", "ultrathink", "go deep", "prove this", "build the full argument", "I need to show my reasoning"), set total_thoughts to 10-15, use all 5 stages (Problem Definition, Research, Analysis, Synthesis, Conclusion), challenge at least 2 assumptions per thought, and track confidence per-step with explicit flags when confidence drops below 0.6. When the user signals speed ("quick", "fast", "just trace this", "high-level", "sketch this out", "gut check"), set total_thoughts to 3-4, use only Problem Definition, Analysis, Conclusion, and prioritize forward progress over exhaustive coverage. Default (no signal): 5-8 thoughts, use stages appropriate to the problem complexity, challenge assumptions when they surface naturally.
---

# Sequential Thinking — Linear Reasoning with Tracking

Runs in an isolated MCP session via `sequential-thinking` server. Builds a linear reasoning chain with explicit confidence, dependency tracking, and contradiction detection. Each step in the chain is discrete and auditable.

## When This Tool Fits

Sequential thinking is for problems with **logical dependency between steps** — where step 3 depends on the conclusion of step 2. If the steps could run in parallel (different perspectives, independent concerns), use context-switcher instead.

Good fits:
- Debugging: "API returns 500 -> check auth -> check middleware -> check handler -> check DB"
- Proofs: "Premise A + Premise B -> Intermediate conclusion -> Final conclusion"
- Planning: "Must configure DNS before deploying -> must deploy before running migrations"
- Root cause analysis: "Symptom -> hypothesis -> test -> refine -> conclude"

Use structured-reflection instead when the problem is fuzzy or unstructured. Sequential thinking requires well-defined premises to produce value.

## Setting Up the Chain

Set `total_thoughts` before starting. Match it to the problem:
- Simple verification: 3-4
- Moderate analysis: 5-8
- Deep argument construction: 10-15

If the chain needs extension mid-session, state it explicitly before adding steps.

## Stage Structure

Each `process_thought` call is one step. The server maintains chain state across calls.

**Stage mapping by problem type:**

Problem Definition -> Analysis -> Conclusion: sufficient for well-scoped problems where the question is already clearly defined.

Problem Definition -> Information Gathering -> Analysis -> Synthesis -> Conclusion: for complex problems requiring research, multi-source integration, or building a complete argument that must hold under scrutiny.

## Intensity Adaptation

This tool adapts its depth based on your framing:

**Deep mode** (triggered by: "deep dive", "thorough", "go deep", "ultrathink", "prove this"):
- 10-15 reasoning steps across all 5 stages
- Every step challenges at least 2 assumptions
- Confidence tracked per-step — drops below 0.6 are flagged explicitly
- Full Research stage before Analysis begins

**Quick mode** (triggered by: "quick", "fast", "gut check", "high-level"):
- 3-4 steps: Problem Definition -> Analysis -> Conclusion
- Skip Research stage — work with what's already known
- Confidence reported only at conclusion

**Default** (no explicit signal): 5-8 steps, stages matched to problem shape, challenge assumptions when they surface naturally.

## Confidence Tracking

Assign confidence per step (range: 0.0-1.0).

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

Use `generate_summary` to get the full reasoning chain. When presenting:

- **Show the chain, not just the conclusion.** The value is the auditable reasoning path.
- **Highlight where confidence dropped.** Low-confidence steps are where the user should focus scrutiny.
- **Surface contradictions found.** If the chain detected internal contradictions, those are the most valuable findings.
- **Note assumptions.** Every chain rests on assumptions — make them visible.

**What makes a high-quality chain:**
- Confidence varies across steps — uniform high confidence throughout indicates the problem wasn't analyzed with real rigor
- Dependencies are explicit — each step references what it builds on
- The conclusion is derived from preceding steps, not introduced fresh at the end

## Anti-Patterns

- **Don't use for open-ended or exploratory problems.** "What should I build?" is not a sequential reasoning problem — it belongs in structured-reflection or decision-matrix.
- **Don't set total_thoughts too low for complex problems.** A 3-step chain on an architecture decision will be shallow. Match chain length to problem complexity.
- **Don't ignore contradictions.** Resolving them is how the chain produces trustworthy output. Flagging and skipping is not resolution.
- **Don't use when you're not actually tracking dependencies.** If every step is independent, this is just a list. Sequential thinking adds no value over simple enumeration when there are no real dependencies.
- **Don't pad steps to fill total_thoughts.** If the chain resolves in 4 steps, stop at 4.

## Chaining

Sequential thinking works well as a DEEP DIVE after broader exploration:

1. `context-switcher` -> surface which angle to investigate
2. **`sequential-thinking`** -> trace the logic end-to-end on that angle
3. `decision-matrix` -> if the chain produced multiple viable conclusions, score them

See `references/STAGE-GUIDE.md` for stage definitions, confidence calibration, and contradiction handling patterns.
