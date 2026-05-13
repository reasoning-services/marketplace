---
name: reasoning-guide
description: Select and orchestrate structured reasoning tools. Use PROACTIVELY when the user faces a complex decision, needs to think through a problem systematically, is comparing multiple options, wants different perspectives on an issue, or is stuck and needs to articulate their thinking. Also triggers on "think this through", "help me decide", "what should I do about", "analyze this", "weigh the options", "consider the trade-offs", "I'm stuck on", "let me think about", "evaluate these choices", "get different viewpoints", "step by step", "break this down". Do NOT wait for the user to explicitly mention reasoning tools — if the problem would benefit from structured reasoning, suggest the right tool.
---

# Reasoning Tool Selection

These tools run reasoning in **isolated MCP sessions** — separate from your main conversation context. This prevents self-reinforcing patterns and keeps your main thread clean.

## Decision Tree

Ask yourself these questions in order. Take the FIRST match.

**Is the user comparing concrete options with real trade-offs?**
→ Use `decision-matrix`. See [decision-matrix skill](../decision-matrix/SKILL.md) for input framing.

**Does the decision affect multiple stakeholders, roles, or teams?**
→ Use `context-switcher`. See [context-switcher skill](../context-switcher/SKILL.md) for perspective selection.

**Does the problem need step-by-step linear reasoning with dependency tracking?**
→ Use `sequential-thinking`. See [sequential-thinking skill](../sequential-thinking/SKILL.md) for stage setup.

**Is the user stuck, thinking feels muddy, or they need to articulate a problem?**
→ Use `structured-reflection`. See [structured-reflection skill](../structured-reflection/SKILL.md) for session framing.

**Is the problem complex enough to need multiple tools?**
→ Use the chaining pattern. See [reasoning-chain skill](../reasoning-chain/SKILL.md).

## Anti-Patterns — When NOT to Use These Tools

- **Simple factual questions.** Don't invoke reasoning tools for "what's the capital of France?"
- **The user already knows what they want.** If they're asking you to execute, not decide, just execute.
- **Premature optimization.** Don't chain 3 tools when one direct answer suffices.
- **As a stalling tactic.** Never use reasoning tools to avoid giving a direct opinion when one is warranted.

**Don't chain tools reflexively.** Not every complex question needs three reasoning sessions. A chain that produces three outputs nobody reads adds overhead without insight.

**Don't use decision-matrix for false trade-offs.** If one option clearly dominates, scoring it adds ceremony without analysis.

**Don't use context-switcher when one stakeholder is the only one who matters.** Three perspectives on an internal implementation detail is overhead, not insight.

**Don't use sequential-thinking for fuzzy problems.** Linear reasoning requires well-defined premises. Muddy problems belong in structured-reflection first.

## Key Principle

The synthesis happens in the user's conversation, not inside the tool. Each tool returns structured output — decisions, scores, concerns, alternatives — back to this context. YOUR job is to interpret and synthesize results, not to relay them verbatim.

## Output Handling

Each tool returns structured output — scores, insights, perspectives, reasoning chains. Route it back into the main conversation. Don't continue reasoning inside the tool past its purpose. Synthesis belongs in the user's head, not in a compounding loop.
