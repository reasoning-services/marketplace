---
description: "Routes to the correct reasoning tool when the right cognitive approach is unclear. Proactively invoke when the problem maps to a specific tool. Invoke with: 'help me think through this', 'which reasoning tool', 'how should I approach this', 'help me work through', 'I need clarity on'."
---

# Reasoning Tool Selection

These tools run reasoning in isolated sessions — separate from your main conversation context. Isolation prevents self-reinforcing patterns and keeps thousands of tokens of internal reasoning out of the user's working context.

## Decision Tree

### structured-reflection
- Thinking feels muddy, circular, or stuck
- The user can't articulate why something feels wrong
- A problem needs to be voiced to be understood
- Assumptions need surfacing or challenging

### decision-matrix
- Multiple viable options with real trade-offs exist
- Criteria can be weighted and applied consistently across options
- A defensible, structured comparison is needed
- The decision needs to be explained or defended to others

### context-switcher
- A decision affects multiple stakeholders or teams
- Designing APIs, interfaces, or systems with multiple consumers
- Blind spots from a single perspective are a meaningful risk
- Organizational or cross-functional impact is significant

### sequential-thinking
- The problem requires explicit step-by-step linear reasoning
- Dependencies between steps must be tracked
- Confidence per step needs to be visible
- Contradictions in the reasoning must be detected and resolved

### reasoning-chain
- The problem spans multiple cognitive modes (unclear framing AND options AND stakeholders)
- Problem framing must be resolved before options can be evaluated
- Output from one session should explicitly inform the setup of the next
- A two or three-tool workflow is warranted by the problem's complexity

## Anti-Patterns

**Don't chain tools reflexively.** Not every complex question needs three reasoning sessions. A chain that produces three outputs nobody reads adds overhead without insight.

**Don't use decision-matrix for false trade-offs.** If one option clearly dominates, scoring it adds ceremony without analysis.

**Don't use context-switcher when one stakeholder is the only one who matters.** Three perspectives on an internal implementation detail is overhead, not insight.

**Don't use sequential-thinking for fuzzy problems.** Linear reasoning requires well-defined premises. Muddy problems belong in structured-reflection first.

## Output Handling

Each tool returns structured output — scores, insights, perspectives, reasoning chains. Route it back into the main conversation. Don't continue reasoning inside the tool past its purpose. Synthesis belongs in the user's head, not in a compounding loop.
