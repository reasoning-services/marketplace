<p align="center">
  <img src="./icon.svg" width="64" alt="reasoning.services" />
</p>

# Reasoning.Services — Claude Code Plugin

Claude is great at thinking. It's terrible at thinking about its own thinking.

When you ask Claude to reason through a complex decision inside the main conversation, it anchors on whatever it said first, reinforces its own framing, and buries the actual trade-offs in thousands of tokens of context that affect every subsequent response.

These tools run reasoning in **isolated sessions** — completely separate from your main conversation context. No self-reinforcing patterns. No context pollution. Structured output that routes back to you, not into a compounding loop.

## What You Get

4 MCP servers + 6 skills, installed with two commands:

| Tool | What it does |
|------|-------------|
| **Structured Reflection** | Work through unclear thinking in an isolated session. Forces articulation. Surfaces hidden assumptions. |
| **Decision Matrix** | Systematic comparison against weighted criteria. Returns structured scoring across options. |
| **Context Switcher** | Parallel perspective analysis from multiple stakeholders or roles. Surfaces blind spots. |
| **Sequential Thinking** | Linear reasoning with explicit confidence tracking, dependency mapping, and contradiction detection. |

The 6 skills teach Claude when and how to use each tool — without you having to explain the setup every time.

## Install

```bash
# 1. Add this marketplace (once)
/plugin marketplace add reasoning-services/marketplace

# 2. Install the plugin
/plugin install reasoning-services@reasoning-services-marketplace
```

Restart Claude Code. All 4 servers appear in `/mcp`. All 6 skills load automatically.

## Authentication

All tools require a subscription. Sign up at [reasoning.services](https://reasoning.services).

Claude Code prompts for OAuth credentials on first tool use.

## Intensity Steering

Tell Claude how deep to go and it adjusts the tool invocation automatically:

| Signal | Effect |
|--------|--------|
| "deep dive", "thorough", "go deep", "prove this" | Maximum depth — more reasoning steps, more criteria, more perspectives |
| *(no signal)* | Standard depth — matched to the problem |
| "quick", "gut check", "just trace this", "sanity check" | Reduced depth — faster, higher-signal output |

The skills map these phrases to concrete parameter values. You don't configure anything.

## Chaining Pattern

For complex decisions, the tools are designed to chain:

1. **Reflect** — Articulate the actual problem (Structured Reflection)
2. **Explore** — Surface blind spots and stakeholder concerns (Context Switcher)
3. **Decide** — Systematic evaluation (Decision Matrix)

The `reasoning-chain` skill guides multi-tool workflows with explicit output threading between sessions.

## Tools in Detail

### Structured Reflection

Use when thinking feels muddy, you're stuck, or you need to articulate a problem to force clarity. The reflection session can't see your main conversation — it works from what you give it, without reinforcing what you've already said.

Supports styles: `analytical` (default), `challenging`, `conversational`, `quick`.

### Decision Matrix

Use when you have multiple viable options with real trade-offs. Define criteria, weight them, score each option. Returns structured scoring you can act on and defend.

In high-stakes mode, the skill proactively adds criteria and options you may not have considered.

### Context Switcher

Use when a decision affects multiple stakeholders, or when you need to surface what a single perspective can't see. Runs the same question from different roles simultaneously and synthesizes genuine tensions.

### Sequential Thinking

Use when a problem requires explicit step-by-step reasoning. Tracks confidence per step, maps dependencies between steps, detects and flags contradictions. Produces an auditable reasoning chain.

## Support

- Documentation: [reasoning.services](https://reasoning.services)
- Issues: [github.com/reasoning-services/marketplace](https://github.com/reasoning-services/marketplace)
- Contact: [contact@reasoning.services](mailto:contact@reasoning.services)

## License

MIT
