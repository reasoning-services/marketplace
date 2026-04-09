---
description: "Use when a decision affects multiple stakeholders or teams, or when you need to surface blind spots from different roles. Runs parallel perspective analysis. Invoke with: 'different perspectives', 'who else is affected', 'surface blind spots', 'how would X see this', 'who would push back'."
---

# Context Switcher

Runs a set of perspectives on the same question simultaneously, then synthesizes agreements, genuine tensions, and non-obvious concerns.

## Perspective Selection

Choose perspectives that will produce **productive tension** — not validation. If all perspectives are likely to agree, the analysis adds no value.

Good perspective combinations:
- User + Engineer + Business + Ops (four-way for product decisions)
- Security + Performance + Developer Experience (infrastructure decisions)
- Near-term execution + Long-term scalability + Cost (strategic options)

Poor perspective combinations:
- Multiple similar roles that will agree on everything
- Perspectives without genuine stake in the outcome
- Abstract perspectives not grounded in actual roles or constraints ("Future person", "Philosopher")

Pick perspectives that would actually disagree in a real meeting.

## How to Frame the Question

The same question framed differently produces different analysis:
- State the decision, not just the topic: "Should we migrate from X to Y?" not "talk about X and Y"
- Include relevant constraints: "within a 3-month window", "with our current team of four"
- Name what you're most uncertain about

## Tool Invocation

Use `analyze_from_perspectives` for standard analysis.

Use `analyze_from_perspectives_stream` for deep sessions — it produces richer per-perspective analysis and streams output progressively.

## Output Interpretation

The output contains per-perspective analysis followed by synthesis.

**Reading the synthesis:**
- **Agreements across perspectives**: likely load-bearing constraints — these matter regardless of which option is chosen
- **Genuine tensions**: the actual trade-off structure; the decision lives here
- **Perspective-specific concerns**: may be minority views, but often surface risks no other perspective can see

**What to watch for:**
- All perspectives arrive at the same conclusion → either the question has an obvious answer or the perspectives were chosen poorly
- One perspective identifies a concern no other perspective acknowledges → investigate this specifically before dismissing it
- Second-order effects: perspective A's solution creates a problem for perspective B

## Anti-Patterns

**Don't use for purely technical decisions.** "Which algorithm is faster?" is a benchmark question, not a stakeholder analysis.

**Don't assign perspectives mechanically.** Three well-chosen perspectives produce better output than five poorly-chosen ones.

**Don't synthesize prematurely.** If perspectives are still mid-analysis, calling synthesis early loses the per-perspective depth.

**Don't treat synthesis as the answer.** The synthesis surfaces tensions. Resolution belongs to the user.

## Intensity Adaptation

| Signal | Perspectives | Invocation | Synthesis |
|--------|-------------|------------|-----------|
| "all angles", "leave no stone unturned", "find blind spots", "need buy-in" | 5–7, with specific focus areas | `analyze_from_perspectives_stream` | Cross-cutting concerns + second-order effects |
| "sanity check", "quick gut check", "sense check" | 3 (technical / user / business) | `analyze_from_perspectives` | Top concern only |
| No signal | 4, chosen for productive tension | `analyze_from_perspectives` | Agreements + genuine tensions |

For deep sessions: specify each perspective with a role plus a specific concern, not just a role name. "Developer who owns long-term maintenance" produces more grounded analysis than "Developer".

See `references/PERSPECTIVES.md` for perspective combinations by domain.
