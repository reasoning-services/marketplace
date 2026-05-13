---
name: deciding-with-matrix
description: Systematic option comparison using weighted criteria and structured scoring. Use PROACTIVELY when the user is choosing between 2-6 concrete options with meaningful trade-offs, comparing technologies or architectures, evaluating vendors or tools, making hiring or resource allocation decisions, or any choice where multiple factors matter at different weights. Triggers on "which should I pick", "compare these options", "what are the trade-offs", "evaluate these", "pros and cons of", "weigh these against each other", "which database should I use", "should I go with A or B", "help me choose", "rank these options", "what's the best option for". Do NOT use for subjective preferences with no criteria, or when the user has already decided and needs validation. When the user signals depth ("thorough comparison", "I need to defend this decision", "high stakes", "comprehensive", "what am I not considering"), use 6-8 criteria with weights deliberately spread across the full 1-5 range, proactively add 2-3 criteria the user didn't consider using add_criterion_tool, and proactively add 1-2 non-obvious alternative options using add_option_tool. When the user signals speed ("just help me pick", "quick comparison", "gut check"), use 3-4 criteria, accept the user's options as-is without adding more, and use a narrower weight range (2-4). Default (no signal): 4-5 criteria, weights spread 2-5, add criteria only if an obvious gap exists.
---

# Decision Matrix — Structured Option Evaluation

Runs in an isolated MCP session via `decision-matrix` server. Evaluates options against weighted criteria. The structured output is designed to surface the actual trade-off drivers — not just produce a winner.

## Before Invoking

Frame the problem correctly. The quality of the output depends entirely on how you set it up.

### 1. Extract Options (2-6 is ideal)

Name each option concisely. If the user is vague ("should I use a NoSQL database?"), expand into concrete options ("MongoDB, DynamoDB, CockroachDB, PostgreSQL with JSONB").

### 2. Define Criteria with Weights (1-5 scale)

This is where most analyses fail. Good criteria are:

- **Specific enough to score.** "Quality" is useless. "Test coverage achievable in 2 weeks" is scorable.
- **Independent of each other.** If two criteria always move together, merge them.
- **Weighted by actual importance, not equal weights.** Ask: "If I could only optimize for one criterion, which would it be?" That's weight 5.
- **Multi-dimensional.** Purely technical or purely business criteria miss the real trade-offs.

**Practical range**: 3 minimum (below this, scoring adds no structure over intuition), 8 maximum (above this, criteria overlap and the session loses coherence).

### 3. Provide Context for Each Option

Don't just send names. Include enough context that the evaluator can distinguish a 3 from a 7. Team size, constraints, timeline, existing infrastructure — all matter.

## Invoking the Tool

Use `start_decision_analysis_tool` with topic, options, and initial_criteria. Then call `evaluate_options_tool` to run scoring. Finally, `get_decision_matrix_tool` for the full scored matrix.

## Intensity Adaptation

This tool scales analysis depth based on your framing:

**Deep mode** (triggered by: "thorough", "high stakes", "I need to defend this", "comprehensive"):
- 6-8 criteria with weights spread across the full 1-5 range
- Proactively adds 2-3 criteria you didn't mention (risk, maintainability, team fit)
- Proactively adds 1-2 non-obvious alternative options
- Full justification text for every score

**Quick mode** (triggered by: "just help me pick", "quick comparison", "gut check"):
- 3-4 criteria, narrower weight range (2-4)
- Scores your stated options against your stated criteria — no additions
- Winner + margin + one key differentiator

**Default** (no explicit signal): 4-5 criteria, weights spread 2-5, add criteria only when an obvious gap exists.

## Interpreting Results

The matrix returns weighted scores. When presenting results:

- **Lead with the winner and the margin.** "PostgreSQL scores 38.5 vs DynamoDB's 34.2 — a meaningful but not decisive gap."
- **Highlight where the winner loses.** The most useful insight is often which criteria the top option is weakest on.
- **Flag close scores.** If the top two are within 5%, the decision depends on criteria the matrix didn't capture. Say so.
- **Never present the matrix as the final answer.** It's structured input for a human decision, not a verdict.

**Red flags:**
- Every option clusters at the same total — criteria are not discriminating; add better ones or redefine scoring anchors
- One option dominates every single criterion — the comparison was unnecessary; the answer was known before the matrix
- Scores contradict your intuition — either the criteria are miscalibrated, or your intuition has a blind spot the matrix is correctly surfacing

## What the Scores Mean

See [SCORING-CALIBRATION.md](references/SCORING-CALIBRATION.md) for the full guide.

Summary: Scores cluster 5-7 without calibration. Relative ordering matters more than absolute scores. If everything scores within 1 point, the criteria aren't differentiating.

## Anti-Patterns

- **Don't use for binary yes/no decisions.** "Should I do X?" is a reflection question.
- **Don't use when criteria can't be made concrete.** Scoring "strategic alignment" without defining what that means produces theater.
- **Don't add trivial options.** An option that will clearly lose on all criteria pollutes the signal without contributing analysis.
- **Don't conflate scoring with deciding.** The matrix surfaces the trade-off structure. The decision still belongs to the user.

## Chaining

Decision Matrix works best AFTER upstream tools have clarified the problem:

1. `structured-reflection` → articulate what you're actually deciding
2. `context-switcher` → surface criteria you'd miss from one perspective
3. **`decision-matrix`** → score options against those criteria
