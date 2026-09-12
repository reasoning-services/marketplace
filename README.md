<p align="center">
  <img src="./icon.svg" width="64" alt="reasoning.services" />
</p>

# reasoning.services

**Claude is great at thinking. It's terrible at thinking about its own thinking.**

These tools fix that. Ten reasoning engines that run in isolated sessions — outside your conversation, outside your biases, outside your context window.

```
/plugin marketplace add reasoning-services/marketplace
/plugin install reasoning-services@reasoning-services-marketplace
```

That's it. Restart Claude Code. Ten engines appear in `/mcp`.

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

**Graph of Thought** — *When the answer is a combination.* Branch into alternatives, score them, prune the dead ends, then **merge** the survivors. The only engine here that returns an answer none of your starting options contained.

**Devil's Advocate** — *Before you commit.* Attacker, competitor, skeptic and pessimist go at your plan. Premortems, attack trees, assumption challenges. Unanimity in the room is a warning sign, not a green light.

**Formal Logic** — *When "it looks right" isn't enough.* PySAT, SymPy and Z3. Deterministic and LLM-free: satisfiability, entailment, consistency, FOL/SMT proofs, temporal traces. A proof, not a confident opinion.

**Hindsight** — *After it went wrong.* Separates what was actually knowable at the time from what looks obvious now, so your postmortem doesn't produce a rule that would never have fired.

**Iterative Refinement** — *When the first draft never ships.* Draft → critique → revise, with convergence measured rather than guessed at. Stops when the changes stop mattering.

**Free Will** — *For unattended runs.* Control-flow primitives for autonomous loops: wake on a timer, continue under a self-issued instruction, decline a queued item on the record.

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

10 MCP server connections + 12 skills that teach Claude when and how to use them:

| Skill | What it does |
|-------|-------------|
| `reasoning-guide` | Auto-detects when you need a reasoning engine and picks the right one |
| `reasoning-chain` | Orchestrates multi-engine workflows for complex decisions |
| `reflecting-structured` | Frames problems for reflection sessions |
| `deciding-with-matrix` | Sets up criteria, interprets scores, flags close calls |
| `switching-perspectives` | Picks perspectives that create productive tension |
| `thinking-sequentially` | Sets up reasoning chains and interprets confidence |
| `exploring-thought-graphs` | Branches into alternatives, prunes, and **merges** the survivors |
| `red-teaming-ideas` | Attacks a plan from hostile perspectives before you commit |
| `proving-with-logic` | Hands logic questions to SAT/SMT solvers instead of judgement |
| `checking-hindsight-bias` | Separates what was knowable then from what looks obvious now |
| `refining-iteratively` | Draft → critique → revise until convergence is measured, not guessed |
| `self-directing` | Control flow for unattended agent loops — pace, continue, decline |

The skills trigger automatically. You don't need to remember tool names.

### Also available via `npx skills`

The whole set installs into 75+ agents — Cursor, Copilot, Cline, Windsurf and the rest — with:

```
npx skills add reasoning-services/marketplace
```

That installs the skills. The engines they call need the plugin above (Claude Code) or a client MCP config with your API token — see [reasoning.services/install](https://reasoning.services/install).

## Auth

All tools require a subscription. Sign up at [reasoning.services](https://reasoning.services).

On first tool use, Claude Code prompts for your API token (found at [reasoning.services/dashboard](https://reasoning.services/dashboard) under Credentials). The token is stored in your system keychain — never plaintext.

## Links

[Documentation](https://reasoning.services) · [Issues](https://github.com/reasoning-services/marketplace/issues) · [Contact](mailto:contact@reasoning.services)

MIT License
