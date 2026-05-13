# Sequential Thinking: Stage Guide

Reference for stage definitions, confidence calibration, and contradiction handling.

Loaded when the sequential-thinking skill needs stage guidance.

## Stage Definitions

### Stage 1: Problem Definition

Define the question precisely. This stage determines whether the rest of the chain answers the right question.

**Outputs:**
- The exact question being answered (not "design a cache" — "decide whether to implement a write-through or write-back cache for this specific use case and load profile")
- Known constraints and boundary conditions
- What a correct answer would look like — how would you verify it?
- Initial confidence in the problem framing itself

**Confidence here:** Reflects certainty that the problem is correctly framed. If the framing might be wrong, say so explicitly in Stage 1 rather than silently carrying forward a flawed premise.

**Common error:** Treating this stage as obvious and moving through it quickly. A poorly defined problem produces a correct answer to the wrong question. The time spent here prevents rework in later stages.

---

### Stage 2: Information Gathering (deep chains only)

Enumerate what is known, what is assumed, and what is unknown.

**Outputs:**
- Known facts relevant to the problem (label as verified or inferred)
- Explicit assumptions — things being treated as true without verification
- Information gaps — things that would increase confidence if known

**Confidence here:** High for verified facts; explicitly low for assumptions. Label each item with its epistemic status.

**Why this matters:** Downstream stages inherit the uncertainty from here. Making assumptions explicit enables contradiction detection when later stages conflict with them.

**Common error:** Treating reasoning as information. "I think X is probably true" belongs in Analysis, not here as a fact. Keep this stage grounded in what is actually known.

---

### Stage 3: Analysis

Apply reasoning to the defined problem using the gathered information.

**Outputs:**
- Evaluation of options or approaches against the criteria from Stage 1
- Trade-offs identified between options
- Confidence per analytical conclusion
- Explicit citation of which Stage 1/2 outputs each conclusion depends on

**Confidence here:** Derived from the confidence of the premises this step depends on. State the dependency explicitly: "Assuming X from Stage 2 (confidence: 0.6), this conclusion holds with confidence 0.6."

**Common error:** Introducing new information in Analysis that wasn't in Information Gathering. When this happens, either revise Stage 2 to include the new information or flag it as an unplanned assumption.

---

### Stage 4: Synthesis (deep chains and complex problems)

Integrate conclusions across the analysis. Look for cross-step conflicts, implications that no single step states individually, and gaps between what was analyzed and what was asked.

**Outputs:**
- Integrated view across analytical conclusions
- Second-order implications: what conclusions from Stage 3 together imply, beyond what each says individually
- What remains genuinely unresolved after analysis

**Confidence here:** Propagated from upstream stages. If any load-bearing step has low confidence, the synthesis confidence ceiling is set by that step.

**Common error:** Synthesis that introduces new reasoning not present in Analysis. If a synthesis conclusion requires an argument not in Stage 3, add that argument as an Analysis step, then synthesize it.

---

### Stage 5: Conclusion

State the answer derived from the chain. The conclusion must be explicitly traceable to the preceding stages.

**Outputs:**
- Direct answer to the Stage 1 question
- Confidence in the conclusion with explicit rationale (what drives it up or down)
- Conditions under which the conclusion would change — what new information would flip it

**Common error:** A conclusion that feels intuitively right but isn't traceable to the chain. If you can't trace it, either the chain is missing steps that support it, or the conclusion is a guess dressed as a derivation.

---

## Stage Transitions

Not every chain needs all 5 stages. Common patterns:

**Quick debugging (3-5 steps):** Problem Definition -> Analysis -> Conclusion
**Research-heavy (6-8 steps):** Problem Definition -> Research -> Research -> Analysis -> Synthesis -> Conclusion
**Proof chain (4-6 steps):** Problem Definition -> Analysis -> Analysis -> Analysis -> Conclusion

## Confidence Tracking

| Confidence | Meaning |
|-----------|---------|
| 0.9-1.0 | Step follows necessarily from premises |
| 0.7-0.9 | Step is well-supported but has assumptions |
| 0.5-0.7 | Step is plausible but could go either way |
| 0.3-0.5 | Step is speculative, needs validation |
| 0.1-0.3 | Step is a guess — flag explicitly |
| < 0.1 | Essentially unknown; flagging for completeness only |

**Propagation rule:** The confidence of a derived step cannot exceed the confidence of its lowest-confidence direct dependency. A chain's overall confidence is bounded by its weakest step. If step 3 is 0.4, the conclusion can't be 0.9 no matter how solid later steps are.

**Common miscalibration:** All steps at 0.8+ confidence. This indicates either a trivial problem or suppressed uncertainty. To diagnose: identify the two or three steps most likely to be wrong and calibrate those carefully. The rest will follow.

**Useful check:** If the conclusion has higher confidence than the lowest-confidence premise it depends on, something is miscalibrated.

---

## Contradiction Detection and Resolution

### Types of Contradictions

**Direct contradiction:** Step A concludes X; Step B concludes not-X on the same question.

**Scope contradiction:** Step A says "this applies in case Y"; Step B treats Y as universally applicable without the condition.

**Assumption contradiction:** Step A assumes constraint C holds; new information in Step D makes C unlikely or false.

### Resolution Patterns

**Revise the earlier step:** When new information in a later step invalidates an assumption in an earlier one, revise the earlier step explicitly. Then trace which downstream steps depend on it and update their confidence accordingly.

**Branch the chain:** When the contradiction isn't resolvable with current information and both sides have merit, branch: "Under assumption A, the chain leads to conclusion X. Under assumption B, the chain leads to conclusion Y." Present both branches explicitly.

**Flag and defer:** When resolution requires information you don't have, flag the contradiction, state what information would resolve it, continue with the higher-confidence path, and mark the conclusion as contingent.

### What Unresolved Contradictions Mean for the Conclusion

A chain with unresolved contradictions produces a conclusion that is internally inconsistent. This must be stated explicitly: "This conclusion holds under [assumption X], but Step N establishes [Y], which is in tension with X. If Y is correct, the conclusion changes to [Z]."

Never deliver an internally inconsistent conclusion without flagging the inconsistency.

### What to Do When a Contradiction Is Flagged

1. Name the two steps that conflict
2. Identify whether the issue is a wrong premise or flawed logic
3. Either revise the earlier step or fork the chain into two hypotheses
4. Do NOT paper over contradictions — they are the most valuable signal
