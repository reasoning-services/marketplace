<p align="center">
  <img src="./icon.svg" width="64" alt="reasoning.services" />
</p>

# reasoning.services

**Claude is great at thinking. It's terrible at thinking about its own thinking.**

These tools fix that. Four reasoning engines that run in isolated sessions — outside your conversation, outside your biases, outside your context window.

```
/plugin marketplace add reasoning-services/marketplace
/plugin install reasoning-services@reasoning-services-marketplace
```

That's it. Restart Claude Code. Four tools appear in `/mcp`.

---

## The Problem

When Claude reasons inside your conversation, it:
- Builds on its own assumptions without challenge
- Burns context tokens on internal deliberation
- Can't take multiple perspectives simultaneously
- Has no structured way to compare options

These tools run reasoning **externally**. The thinking happens in isolated MCP sessions. Only the structured output comes back. Your context stays clean. Your biases get challenged.

## The Tools

**Structured Reflection** — *When you're stuck.* Start a thinking session in isolation. Early turns explore, mid turns synthesize, late turns converge. The session adapts as you go deeper.

**Decision Matrix** — *When you have options.* Define criteria, weight them, score each option. Returns structured scoring with justifications, not vibes.

**Context Switcher** — *When you need other eyes.* Run the same question from 3-5 stakeholder perspectives in parallel. Surface blind spots you can't see from one viewpoint.

**Sequential Thinking** — *When order matters.* Step-by-step reasoning with confidence tracking. Catches contradictions between steps. Shows the proof, not just the conclusion.

## Chain Them

The real power is the workflow. For high-stakes decisions:

```
Reflect  ->  Explore  ->  Decide

  +-----------------+    +-----------------+    +-----------------+
  |    Structured    |    |     Context      |    |    Decision      |
  |    Reflection    |--->|     Switcher     |--->|     Matrix       |
  |                  |    |                  |    |                  |
  |  "What am I      |    |  "What would     |    |  "Score these    |
  |   actually        |    |   security/PM/   |    |   against the    |
  |   deciding?"      |    |   ops think?"    |    |   criteria we    |
  |                  |    |                  |    |   surfaced"      |
  +-----------------+    +-----------------+    +-----------------+
        Clarity              Breadth               Decision
```

Each tool's output feeds the next. Reflection clarifies the question. Context Switcher surfaces criteria you'd miss. Decision Matrix scores options against those criteria.

Claude's skills know when to suggest this chain and how to thread the output forward.

## Intensity Steering

Tell Claude how deep to go and it adjusts the tool invocation automatically:

| Signal | Effect |
|--------|--------|
| "deep dive", "thorough", "go deep", "prove this", "challenge me" | Maximum depth — more reasoning steps, more criteria, more perspectives, challenging mode |
| *(no signal)* | Standard depth — matched to the problem |
| "quick", "gut check", "just trace this", "sanity check", "rubber duck" | Reduced depth — faster, higher-signal output |

The skills map these phrases to concrete parameter values. You don't configure anything.

## Try It

After installing, paste this:

> I need to choose between PostgreSQL and DynamoDB for our new service. The team is small (3 engineers), we expect moderate traffic initially but need to handle spikes, and we're already running on AWS. Help me think through this properly.

Watch Claude automatically reflect on the real constraints, gather perspectives from different roles, and build a scored comparison — without being told which tools to use.

## What Gets Installed

4 MCP server connections + 6 skills that teach Claude when and how to use them:

| Skill | What it does |
|-------|-------------|
| `reasoning-guide` | Auto-detects when you need a reasoning tool and picks the right one |
| `reflecting-structured` | Teaches Claude how to frame problems for reflection sessions |
| `deciding-with-matrix` | Teaches Claude how to set up criteria, interpret scores, flag close calls |
| `switching-perspectives` | Teaches Claude how to pick perspectives that create productive tension |
| `thinking-sequentially` | Teaches Claude how to set up reasoning chains and interpret confidence |
| `reasoning-chain` | Orchestrates multi-tool workflows for complex decisions |

The skills trigger automatically. You don't need to remember tool names.

## Auth

All tools require a subscription. Sign up at [reasoning.services](https://reasoning.services).

On first tool use, Claude Code prompts for your API token (found at [reasoning.services/dashboard](https://reasoning.services/dashboard) under Credentials). The token is stored in your system keychain — never plaintext.

## Links

[Documentation](https://reasoning.services) · [Issues](https://github.com/reasoning-services/marketplace/issues) · [Contact](mailto:contact@reasoning.services)

MIT License
