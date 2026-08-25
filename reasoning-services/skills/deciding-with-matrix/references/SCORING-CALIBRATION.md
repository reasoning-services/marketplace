# Decision Matrix: Scoring Calibration

Reference for interpreting scores, detecting calibration errors, and handling specific criterion types.

Loaded into context only when the deciding-with-matrix skill needs scoring guidance.

## Score Semantics (1-5 Scale)

| Score | Meaning |
|-------|---------|
| 5 | Strongly satisfies this criterion — best realistic outcome |
| 4 | Satisfies with minor gaps |
| 3 | Neutral — partially satisfies, partially fails |
| 2 | Notable deficiency on this criterion |
| 1 | Fails this criterion — worst realistic outcome |

**Calibration baseline:** Before scoring any option, identify which option is best on this criterion (anchor at 5) and which is worst (anchor at 1 or 2). Score everything else relative to those anchors. Without this, scores cluster at 3-4 regardless of actual differentiation.

**If all options score 3-4 on most criteria:** The criteria are not discriminating. Either redefine scoring anchors (what does a 5 look like here? what does a 1 look like?) or replace the criterion with one that actually separates the options.

## NO_RESPONSE

Use when:
- The criterion is genuinely inapplicable to this option
- Scoring would require speculation beyond what's provided
- You lack domain knowledge to distinguish scores within the range

Do NOT use as a cop-out for hard scoring. If you can reason about it at all, produce a score with a justification.

## Interpreting Weighted Totals

Weighted total = sum of (score x weight) across all criteria.

**Meaningful signal:** Relative ordering between options. The option with the highest weighted total is the systematically preferred choice given these criteria and weights.

**Less meaningful:** The absolute total value. It scales with the number of criteria and the weight distribution, which varies per matrix.

**When totals are close:** If the top two options are within 5-8% of the maximum possible weighted total, the trade-offs are genuinely balanced. Don't force a winner — examine which specific criterion or criteria drive the gap and verify the weights reflect actual priorities.

**When totals are far apart:** One option dominates. If this contradicts your intuition, examine: (a) were the criteria chosen to favor this option? (b) are the weights miscalibrated? (c) or does your intuition have a blind spot the matrix is correctly surfacing?

## Bias Patterns

### Central Tendency Bias

Everything clusters at 3-4. If your scores don't use the full range, your criteria aren't differentiating. Would you be embarrassed defending this score to someone who knows the domain?

### Anchoring to the First Option

The first option defined becomes the implicit baseline. Everything else is scored relative to it, whether consciously or not.

**Mitigation:** Define the strongest contender first (sets a high anchor). Or complete the criteria and weight definitions before scoring any option, then score all options simultaneously.

### Halo Effect

One option scores high on everything because of general positive impression. Score each criterion independently — cover the option name if it helps.

### Confirmation Bias

Users who already prefer an option tend to choose criteria that favor it and assign high weights to criteria where it performs well.

**Detection:** If the preferred option scores highest on every criterion including newly added ones, the criteria may have been selected to validate rather than evaluate.

**Mitigation in deep mode:** Proactively add 1-2 criteria where the preferred option performs poorly. "What would have to be true for this option to fail?" is a useful diagnostic.

### Criteria Proliferation

Adding more criteria feels like rigor. It isn't, when criteria overlap. Two correlated criteria effectively double-weight that dimension without making it visible.

**Detection:** If swapping the scores on two criteria wouldn't change the rankings, one is likely redundant.

**Mitigation:** Before adding a criterion, ask: "Would any option score differently relative to the others on this criterion vs. one already in the matrix?" If no, the criterion adds no information.

## Criterion Types

### Quantitative Criteria

Scorable against objective thresholds. Highest signal when the user has concrete requirements.

**Calibration approach:** Define what each score level means in concrete terms before scoring.

Example for "response time at p99":
- 5 = under 100ms
- 4 = 100-200ms
- 3 = 200-500ms
- 2 = 500ms-1s
- 1 = over 1s

When threshold definitions exist, scoring becomes objective rather than subjective.

### Qualitative Criteria

Require judgment: maintainability, team skill-fit, organizational alignment. Valid, but need explicit definition to be scored consistently across options.

**Calibration approach:** Define the extreme ends before scoring the middle.

Example for "team skill-fit":
- 5 = Team has production experience with this technology
- 1 = No current team member has used it

Middle scores follow naturally from those anchors.

### Constraint Criteria

Binary constraints that aren't sliding scales: regulatory compliance, existing vendor contracts, security requirements.

**Handling:** Weight these at 5. If any option scores 1 on a constraint criterion, it is eliminated regardless of its total score. Flag this explicitly before running the full evaluation.

**Red flag:** If all options score 1 on a constraint criterion, the framing is wrong — no viable options are on the table. Stop and reframe before proceeding.

## When Scores Diverge from Intuition

A score that contradicts gut feeling is information, not an error to override.

Diagnostic steps:
1. **Check the criteria**: Do high-weight criteria actually measure what matters most, or what the user thought mattered most before the session?
2. **Check the weights**: Are they calibrated to actual priority, or to stated priority that may not reflect real trade-offs?
3. **Check for hidden criteria**: Is the gut reading measuring a factor not in the matrix? Add it explicitly and score it.
4. **Accept the divergence**: Intuition sometimes measures something real that the matrix can't capture. The matrix surfaces the divergence — the user resolves it with full information.

Never override matrix output silently. If intuition wins, state why explicitly.
