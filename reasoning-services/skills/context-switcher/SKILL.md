---
name: context-switcher
description: "Analyse one question from several stakeholder perspectives in parallel to surface blind spots. Use when a decision crosses teams, buy-in matters, or the user is locked into a single viewpoint."
---

# Context Switcher — Multi-Perspective Analysis

Runs in an isolated MCP session via `context-switcher` server. Runs a set of perspectives on the same question simultaneously, then synthesizes agreements, genuine tensions, and non-obvious concerns.

## Before Invoking

### Choose Perspectives Deliberately

Don't default to generic roles. Pick perspectives that create **productive tension** — not validation. If all perspectives are likely to agree, the analysis adds no value.

**Good set (for a database migration):**
- DBA (operational risk, performance)
- Application developer (migration effort, API changes)
- Security engineer (data exposure during migration, access control)
- Product manager (downtime impact, feature velocity)

**Bad set:**
- "Technical perspective" (too vague)
- "Positive perspective" (not a stakeholder)
- 8 perspectives (diminishing returns after 4-5)

Pick perspectives that would actually disagree in a real meeting.

### Frame the Question for Divergence

A question like "Is this a good idea?" produces shallow agreement. Instead:
- "What could go wrong with this approach from your perspective?"
- "What would you need to see before approving this?"
- "Where does this conflict with your team's priorities?"

Include relevant constraints: "within a 3-month window", "with our current team of four". Name what you're most uncertain about.

## Invoking the Tool

Use `start_context_analysis` with topic and initial perspectives (3-5 recommended). Then `analyze_from_perspectives` for parallel analysis. Use `synthesize_perspectives` to find patterns.

Use `analyze_from_perspectives_stream` for deep sessions — it produces richer per-perspective analysis and streams output progressively.

### Picking Perspectives You Wouldn't Have Picked

The quality ceiling of this tool is set entirely by the perspective list, and the list you write from inside the problem is the one already shaped by your blind spots. Two tools exist to break that, and skipping them is how sessions end up confirming what you walked in with.

- **`recommend_perspectives(request)`** — reads the problem and suggests the viewpoints worth running. Call it before committing to a list whenever the domain is unfamiliar or the stakes are real. If it returns a perspective you would not have chosen, that is the one most likely to earn its place.
- **`list_templates()`** — pre-configured perspective sets for common decision shapes. Faster than composing from scratch, and a reasonable starting point to then extend.
- **`add_perspective(request)`** — adds a domain-specific lens mid-session when the standard technical / business / user / risk set misses something crucial. A regulated product may need a compliance auditor; a migration may need the team that has to operate it at 3am.

### Reading the Session Back

- **`get_analysis(session_id, analysis_index, perspective)`** — the actual response text for one analysis round. Session summaries return *without* response bodies, so when you need what a perspective really said — to quote it, or to check a synthesis against it — this is the call. Pass `perspective` to narrow to one voice.
- **`current_session()`** — the most recent session without its id. Use it when resuming rather than starting a second analysis of the same question.

## Intensity Adaptation

This tool scales breadth and depth based on your framing:

**Deep mode** (triggered by: "leave no stone unturned", "comprehensive", "all angles", "find the blind spots"):
- 5-7 perspectives with specific focus areas, not just role names
- Streaming analysis for richer per-perspective output
- After initial analysis, proactively adds 1-2 perspectives that results revealed as missing
- Synthesis focuses on non-obvious cross-cutting concerns and second-order effects

**Quick mode** (triggered by: "sanity check", "gut check", "sense check"):
- 3 core perspectives: technical feasibility, user impact, business viability
- Standard (non-streaming) analysis
- Synthesis focuses on single highest-priority concern

**Default** (no explicit signal): 4 perspectives chosen for productive tension, standard analysis, synthesis of agreements and genuine tensions.

For deep sessions: specify each perspective with a role plus a specific concern, not just a role name. "Developer who owns long-term maintenance" produces more grounded analysis than "Developer".

## Interpreting Results

- **Lead with points of agreement.** Where multiple perspectives converge = high-confidence finding.
- **Highlight genuine tensions.** Where perspectives directly conflict = the actual decision point. Don't paper over disagreements.
- **Flag missing perspectives.** If no perspective covered regulatory/legal and the decision warrants it, say so.
- **Distinguish concerns from blockers.** A security concern about logging is not a security blocker about auth.

**What to watch for:**
- All perspectives arrive at the same conclusion — either the question has an obvious answer or the perspectives were chosen poorly
- One perspective identifies a concern no other perspective acknowledges — investigate this specifically before dismissing it
- Second-order effects: perspective A's solution creates a problem for perspective B

## Anti-Patterns

- **Don't run perspectives sequentially as a debate.** They're parallel analyses, not a conversation.
- **Don't synthesize by averaging.** "Some say yes, some say no, so maybe" is useless. Identify WHAT drives the disagreement.
- **Don't add perspectives to be thorough.** 3 sharp perspectives beat 7 diluted ones.
- **Don't use for purely technical decisions.** "Which algorithm is faster?" is a benchmark question, not a stakeholder analysis.
- **Don't synthesize prematurely.** If perspectives are still mid-analysis, calling synthesis early loses the per-perspective depth.
- **Don't treat synthesis as the answer.** The synthesis surfaces tensions. Resolution belongs to the user.

## Chaining

Context Switcher is most powerful in the EXPLORE position:

1. `structured-reflection` → clarify what you're actually exploring
2. **`context-switcher`** → surface concerns from multiple angles
3. `decision-matrix` → use surfaced concerns as criteria for scoring

See `references/PERSPECTIVES.md` for perspective combinations by domain.

---

## Trigger Reference

Retained from the pre-2.2 frontmatter description, which exceeded the 200-character
claude.ai limit. Kept here so the routing signal is not lost; `reasoning-guide` is the
skill that acts on it.

> Run parallel analysis from multiple stakeholder perspectives to surface blind spots and cross-cutting concerns. Use PROACTIVELY when a decision affects multiple teams or roles, when designing APIs or interfaces that multiple consumers will use, when the user seems locked into one viewpoint, when organizational buy-in matters, when there are competing priorities (speed vs quality, cost vs features), or when the user needs to anticipate objections. Triggers on phrases like "what am I missing", "different perspectives on", "how would X see this", "who would object to", "devil's advocate", "blind spots", "stakeholder analysis", "what would the security team think", "how does this look from", "consider all angles", "get other viewpoints", "what concerns would Y have". Do NOT use when the user needs a single deep analysis rather than breadth, or when there's genuinely only one stakeholder. See the skill body for deep, quick, and default invocation modes.
