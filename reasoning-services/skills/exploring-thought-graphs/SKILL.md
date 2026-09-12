---
name: exploring-thought-graphs
description: "Explore several approaches at once, score them, then merge the strongest into one. Use when the answer is a synthesis of partial ideas rather than a winner picked from a list."
---

# Graph of Thought — Divergent Exploration with Synthesis

Runs in an isolated MCP session via the `graph-of-thought` server. This is the upgrade from linear reasoning: instead of committing to one chain and following it, you branch into alternatives, score them, prune the dead ends, and **merge** the survivors into something none of them was alone.

The merge is the point. Every other reasoning tool narrows toward one of the options you started with. This one lets the answer be a combination that did not exist when you began.

## When This Is the Right Tool

- Several approaches are viable and you cannot yet tell which wins
- The best answer is plausibly a **blend** — "take the caching from A and the failure model from B"
- You are designing something rather than choosing something
- An early idea is weak but its core is worth salvaging

**Not this tool when:** the options are fixed and you need them scored against criteria (`decision-matrix`), each step strictly depends on the last (`sequential-thinking`), or the problem is not yet articulated (`structured-reflection`).

## The Session Contract

**You supply `session_id` yourself** — on every call, including `seed`. Unlike the other reasoning services, this server does not mint one for you. Pick a stable, descriptive id at the start (`caching-arch-2026-09`) and reuse it verbatim for the whole session. A typo silently starts a second, empty graph.

Node ids are returned by `seed`, `generate`, `aggregate`, and `refine`. Keep track of them — every subsequent call addresses nodes by id.

## The Loop

### 1. Seed

`seed(session_id, problem)` — creates the root. State the problem as a question, with the constraints that make it hard. "How should we architect the caching layer?" is thin. "How should we architect the caching layer given 3 engineers, unpredictable traffic spikes, and no dedicated ops?" gives every downstream branch something to bite on.

### 2. Generate — diverge

`generate(session_id, parent_id, thoughts)` — branches a parent into N children, where `thoughts` is a list of alternative strings.

Make the alternatives **genuinely different in kind**, not three flavours of the same idea. Three variations of Redis is one branch, not three. Redis cluster / local cache with TTL / CDN-plus-app hybrid is three.

Three to five is the productive range. Two is a false binary; beyond five, scoring becomes noise.

### 3. Score — evaluate

`score(session_id, node_id, score, reasoning)` — a float from 0.0 to 1.0.

**Nodes below 0.3 are auto-pruned.** That is a real deletion from the live graph, so score deliberately: 0.25 discards a branch, 0.35 keeps it alive for refinement. Always pass `reasoning` — it is what makes the graph readable later, and what `extract_pattern` has to work with.

Calibration: 0.8+ is strong and ready to merge; 0.5–0.7 is viable with known weaknesses; 0.3–0.5 is weak but salvageable — the `refine` band; below 0.3 you are choosing to delete it.

### 4. Aggregate — converge

`aggregate(session_id, parent_ids, synthesis)` — merges N nodes into 1. **This is the key operation.**

Pass the ids of two or more strong nodes and a `synthesis` that states what the combination takes from each and what it resolves between them. A synthesis that merely concatenates both ideas has not merged anything; name the tension and say how the combination settles it.

If you finish a session without calling `aggregate`, you ran an expensive scoring exercise, not a graph of thought.

### 5. Refine — rescue

`refine(session_id, node_id, improved_content)` — spawns an improved child from a weak-but-promising node (1→1). Use it in the 0.3–0.5 band when the core idea is sound and the execution is not. Score the child afterwards; a refinement that does not beat its parent is a signal the idea really was the problem.

### 6. Inspect

`status(session_id)` — read-only summary: topology, scores, best path. Call it whenever you are unsure what to do next, and before aggregating, to confirm which nodes actually survived pruning.

`visualize(session_id)` — returns a Mermaid `graph TD` string. Render it for the user when the shape of the exploration is itself the insight.

### 7. Capture

`extract_pattern(session_id)` — derives the reusable reasoning structure from a graph that worked.

`learn(session_id, pattern_name, trigger_phrases)` — formats the session as a memory-ready template. Use it after a genuinely novel exploration, then store the result wherever your memory lives. Skip it for routine sessions; a memory full of one-off patterns is worse than an empty one.

## Presenting Results

- **Lead with the synthesis, not the tour.** The user wants the merged answer, not a replay of every branch.
- **Name what was discarded and why.** "We dropped the CDN hybrid — it assumed cache keys we don't control." Pruned branches are evidence of rigour; listing them is the difference between a decision and an assertion.
- **Show the graph when shape matters.** A wide-then-narrow graph tells a different story from a deep chain. Render the Mermaid when that story is worth telling.
- **Say when nothing merged.** If one branch dominated and no aggregation happened, report it honestly — the exploration confirmed an early instinct, which is a real result, not a failure.

## Anti-Patterns

- **Generating alternatives you have already dismissed.** Padding the graph to look thorough wastes the scoring pass.
- **Scoring everything 0.6–0.8.** Undifferentiated scores mean the graph cannot prune, and you get a wide flat tree with no signal.
- **Skipping `aggregate`.** Without the merge, this is a decision matrix with worse ergonomics.
- **Refining a node that deserved pruning.** Not every weak idea has a good core.
- **Reusing a `session_id` across unrelated problems.** The graph accumulates and the best-path calculation degrades.

## Chaining

Graph of Thought sits in the middle of a chain, where exploration belongs:

1. `structured-reflection` → establish what problem is actually being solved
2. **`graph-of-thought`** → explore approaches, prune, synthesize
3. `devils-advocate` → attack the synthesis before committing
4. `decision-matrix` → only if the merge produced two survivors that need scoring

See the [`reasoning-chain` skill](../reasoning-chain/SKILL.md) for output-threading discipline.
