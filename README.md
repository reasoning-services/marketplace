<p align="center">
  <img src="./icon.svg" width="64" alt="reasoning.services" />
</p>

# reasoning.services — Claude Code Plugin

Structured reasoning tools for AI workflows. Isolated cognitive sessions that don't pollute your context or reinforce your biases.

## What You Get

4 MCP servers, installed with two commands:

| Tool | What it does |
|------|-------------|
| **Structured Reflection** | Work through complex logic in an isolated session |
| **Decision Matrix** | Systematic comparison against weighted criteria |
| **Context Switcher** | Parallel perspectives from multiple stakeholders/roles |
| **Sequential Thinking** | Linear reasoning with confidence tracking and contradiction detection |

## Install

```bash
# 1. Add this marketplace (once)
/plugin marketplace add reasoning-services/marketplace

# 2. Install the plugin
/plugin install reasoning-services@reasoning-services-marketplace
```

Restart Claude Code. All 4 servers appear in `/mcp`.

## Authentication

All tools require a subscription. Sign up at [reasoning.services](https://reasoning.services).

After subscribing, Claude Code will prompt for OAuth credentials on first tool use.

## Tools in Detail

### Structured Reflection (`structured-reflection`)

Use when thinking feels muddy, you're stuck, or you need to articulate a problem to force clarity. Runs in a separate session — won't pollute your main conversation context.

### Decision Matrix (`decision-matrix`)

Use when you have multiple viable options with real trade-offs. Define criteria, weight them, score each option. Returns structured scoring you can act on.

### Context Switcher (`context-switcher`)

Use when a decision affects multiple stakeholders or you need to surface blind spots. Runs the same question from different roles/perspectives in parallel.

### Sequential Thinking (`sequential-thinking`)

Use when a problem requires explicit step-by-step reasoning. Tracks confidence per step, maps dependencies between steps, detects contradictions.

## Chaining Pattern

For complex decisions:

1. **Reflect** — Articulate the actual problem (Structured Reflection)
2. **Explore** — Surface blind spots (Context Switcher)
3. **Decide** — Systematic evaluation (Decision Matrix)

## Support

- Documentation: [reasoning.services](https://reasoning.services)
- Issues: [github.com/reasoning-services/marketplace](https://github.com/reasoning-services/marketplace)
- Contact: [contact@reasoning.services](mailto:contact@reasoning.services)

## License

MIT
