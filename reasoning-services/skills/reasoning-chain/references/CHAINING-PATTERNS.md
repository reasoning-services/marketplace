# Reasoning Chain: Output Threading and Adaptation

Reference for multi-tool chaining patterns, explicit handoff mechanics, and adaptation decision trees.

## Pattern Detail

### Pattern: Reflect → Explore → Decide

`Structured Reflection → Context Switcher → Decision Matrix`

**Problem type:** Unclear framing + stakeholder complexity + evaluation needed

```
Stage 1: Structured Reflection
  Input:  The situation as currently understood — options, leaning, what feels off
  Target: Identify the real question, surface hidden assumptions, name genuine constraints
  Output: Clarified problem statement, 1–2 named assumptions, the concern that was hard to articulate

Stage 2: Context Switcher
  Input:  Clarified problem statement from Stage 1 (not the original framing)
  Target: Surface blind spots from stakeholders identified as relevant in Stage 1
  Output: 3–4 concrete concerns from distinct perspectives, genuine tensions between groups

Stage 3: Decision Matrix
  Input:  Options informed by Stage 1 + 2; criteria informed by Stage 2 concerns
  Target: Systematic evaluation that incorporates what reflection and perspective analysis revealed
  Output: Weighted scores, trade-off structure, defensible ranking
```

**Threading checklist:**
- [ ] Stage 2 prompt uses the clarified problem statement from Stage 1, not the original framing
- [ ] Stage 2 perspectives chosen based on who was identified as affected in Stage 1
- [ ] Stage 3 criteria include at least one derived from Stage 2 perspective concerns
- [ ] Stage 3 weights reflect priorities surfaced in Stage 1 reflection, not pre-session stated priorities

---

### Pattern: Explore → Deep-Dive → Decide

`Context Switcher → Sequential Thinking → Decision Matrix`

**Problem type:** Known options, complex stakeholder tensions, logical implications need tracing

```
Stage 1: Context Switcher
  Input:  The decision + affected stakeholder groups
  Target: Surface competing priorities and genuine tensions between groups
  Output: 2–3 genuine tensions; concerns that aren't visible from a single perspective

Stage 2: Sequential Thinking
  Input:  Each major tension from Stage 1 (run separate chains per tension if needed)
  Target: Trace logical implications of each resolution path; identify what is ruled out
  Output: Chains of implications per path; logical ruling-outs; confidence per conclusion

Stage 3: Decision Matrix
  Input:  Options that explicitly address Stage 1 tensions
          Criteria weighted by Stage 1 stakeholder priorities
          Options filtered to exclude paths ruled out as logically invalid in Stage 2
  Target: Evaluation that incorporates what was surfaced and what was ruled out
  Output: Ranked options with trade-off structure visible
```

**Threading checklist:**
- [ ] Sequential analysis in Stage 2 uses exact tension language from Stage 1 output
- [ ] Options in Stage 3 matrix exclude paths ruled logically invalid in Stage 2
- [ ] Criteria in Stage 3 matrix include items from Stage 1 stakeholder priority concerns
- [ ] Confidence from Stage 2 chains informs which matrix criteria get higher weights (more uncertain = more weight on verifying that dimension)

---

### Pattern: Reflect → Decide

`Structured Reflection → Decision Matrix`

**Problem type:** Options are clear; priorities are not

```
Stage 1: Structured Reflection (challenging mode recommended)
  Input:  The decision + current leaning + what makes you uncertain
  Target: Expose the real optimization target — what are you actually optimizing for?
  Output: Clarified priorities, the trade-off the user is genuinely making vs. the one stated

Stage 2: Decision Matrix
  Input:  Options as originally stated
          Criteria and weights derived directly from Stage 1 reflection output
  Target: Confirm or challenge the pre-session leaning with an explicit weight structure
  Output: Scored evaluation — may confirm the leaning, may surface a clean override
```

**Threading checklist:**
- [ ] Stage 2 weights directly reflect what Stage 1 identified as the actual priority
- [ ] If Stage 1 identified a hidden assumption, add a criterion to test it explicitly
- [ ] Don't use the pre-session weights — the whole point is that reflection changed them

---

## Output Threading Mechanics

### What to Extract Per Tool

**From Structured Reflection:**
- The restated problem (different from the initial framing — this is the threading input for the next stage)
- Named assumptions (these become criteria or constraints in later stages)
- The concern the user was circling around but couldn't articulate (often becomes the highest-weight criterion)

**From Context Switcher:**
- Perspective concerns with highest cross-cutting relevance (affect multiple stakeholders)
- Genuine tensions between perspectives (the decision structure lives here)
- Stakeholders or concerns not in the original framing (potential new options or constraints)

**From Sequential Thinking:**
- Logical ruling-outs (paths with contradictions or confidence below threshold — these don't enter the matrix)
- Implicit dependencies (step A must be true for option B to be viable)
- Confidence floor of the chain (sets the ceiling for how confident the downstream decision can be)

### The Handoff Statement

When moving from one tool to the next, write an explicit handoff before invoking the next tool. This is not boilerplate — it is the mechanism that makes the chain coherent.

**Templates:**

> "Reflection identified [X] as the real concern — not [original framing]. Carrying [X] forward as the highest-weight criterion."

> "Perspective [Y] raised [Z] as a concern that no other perspective acknowledged. Adding it as a criterion with weight [W] because [reason drawn from the analysis]."

> "Sequential analysis shows [option A] leads to a contradiction at step [N] under [constraint C]. Removing [option A] from the matrix."

> "Confidence in [conclusion from Stage 2] is 0.4 — too low to treat as a hard constraint. Including it as a medium-weight criterion rather than a filter."

---

## Adaptation Decision Trees

### When to stop early

```
After Stage 1 (Reflection):
  Did the session resolve the decision outright?
    Yes → Stop. No further tools needed.
  Did the session reveal the options aren't yet defined?
    Yes → Generate options before proceeding.
  Did the session reveal constraints that eliminate all but one option?
    Yes → Skip to implementation planning.

After Stage 2 (Explore or Deep-Dive):
  Did the analysis reveal the decision is already made by a hard constraint?
    Yes → Stop. Document the constraint. Proceed to implementation.
  Did the analysis surface a new option not in the original set?
    Yes → Add it to the matrix before scoring.
  Did Stage 2 invalidate a Stage 1 assumption?
    Yes → Revise Stage 1 output before proceeding to Stage 3.
```

### When to extend the chain

A chain can be extended beyond three tools when warranted. Common extensions:

- After Reflect → Decide, if the matrix produces a result that re-opens the problem framing → run a second Reflect focused on the specific tension the matrix surfaced
- After Explore → Decide, if the matrix reveals a new stakeholder concern that wasn't in the original perspective set → run a second targeted Explore on that specific concern

**Limit:** Maximum useful chain length is four tools. Beyond that, the outputs become too diffuse to thread coherently.

---

## Anti-Patterns in Chaining

**Starting a chain without threading intent.** If you can't state how Stage 1's output will inform Stage 2's setup before running Stage 1, the chain will produce disconnected sessions.

**Using chaining to avoid deciding.** A chain that always produces "it depends" or "more information needed" is not working — it's deferring. At least one stage should produce a constraint, ruling-out, or priority clarification that narrows the space.

**Mechanical three-tool chains.** Running Reflect → Explore → Decide because it's "the pattern" without evaluating whether each stage is actually needed. Two well-threaded tools are better than three loosely connected ones.

**Chaining before the problem is defined.** Run Stage 1 of whichever tool is most appropriate for where the user is. Don't plan a three-tool chain before understanding what the actual problem is.
