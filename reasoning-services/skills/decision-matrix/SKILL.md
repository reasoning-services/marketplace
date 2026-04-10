---
name: decision-matrix
description: "Use when multiple viable options exist with real trade-offs and systematic comparison is needed. Returns structured scoring across weighted criteria. Invoke with: 'which should I pick', 'compare these options', 'pros and cons of', 'help me decide between', 'should I choose X or Y'."
---

# Decision Matrix

Evaluates options against weighted criteria. The structured output is designed to surface the actual trade-off drivers — not just produce a winner.

## Criteria Design

The quality of the matrix depends on criteria quality. Good criteria are:
- **Independent**: scoring one criterion doesn't constrain another
- **Discriminating**: they differentiate between options (if every option scores the same, remove it)
- **Concrete enough to score**: "good performance" is ambiguous; "response time under 200ms" is scorable
- **Multi-dimensional**: purely technical or purely business criteria miss the real trade-offs

**Practical range**: 3 minimum (below this, scoring adds no structure over intuition), 8 maximum (above this, criteria overlap and the session loses coherence).

## Adding Criteria and Options

Use `add_criterion_tool` to add criteria the user may have missed.

For deep/high-stakes sessions, proactively add 2–3 non-obvious criteria:
- Second-order effects ("what does maintaining this look like in 18 months?")
- Hidden costs ("migration complexity", "team ramp-up time")
- Reversibility ("can we change this decision if assumptions prove wrong?")

Use `add_option_tool` to surface alternatives the user hasn't listed.

For deep sessions, add 1–2:
- "Do nothing / status quo" — always worth scoring explicitly
- "Hybrid approach" — if a combination of options is feasible
- "Defer until X is known" — if the decision hinges on currently unknown information

## Weighting

Weight range 1–5 where 1 = minor consideration, 5 = non-negotiable constraint.

**Standard sessions**: use range 2–5. If a criterion barely matters, remove it rather than weighting it 1.

**Deep sessions**: use the full 1–5 range deliberately. Having a 5-weight and a 1-weight criterion in the same matrix makes the priority structure explicit and visible.

## Output Interpretation

The matrix returns scores per criterion per option, weighted totals, and rankings.

**What signals are meaningful:**
- **Relative ordering**: the actual signal — which option consistently outperforms
- **Score clustering**: if top options are within 5% of maximum possible, the criteria aren't differentiating enough, or the options are genuinely equivalent

**Red flags:**
- Every option clusters at the same total → criteria are not discriminating; add better ones or redefine scoring anchors
- One option dominates every single criterion → the comparison was unnecessary; the answer was known before the matrix
- Scores contradict your intuition → either the criteria are miscalibrated, or your intuition has a blind spot the matrix is correctly surfacing

## Anti-Patterns

**Don't use for binary yes/no decisions.** "Should I do X?" is a reflection question.

**Don't use when criteria can't be made concrete.** Scoring "strategic alignment" without defining what that means produces theater.

**Don't add trivial options.** An option that will clearly lose on all criteria pollutes the signal without contributing analysis.

**Don't conflate scoring with deciding.** The matrix surfaces the trade-off structure. The decision still belongs to the user.

## Intensity Adaptation

| Signal | Criteria | Weights | Proactive additions |
|--------|----------|---------|---------------------|
| "thorough", "high stakes", "defend this", "board presentation" | 6–8 | Full 1–5, spread | 2–3 criteria + 1–2 options |
| "just pick", "quick", "gut check", "low stakes" | 3–4 | 2–4 | None |
| No signal | 4–5 | 2–5 | Add only if obvious gap |

See `references/SCORING-CALIBRATION.md` for score semantics, bias patterns, and criterion type guidance.
