---
name: self-directing
description: "Control-flow primitives for long-running autonomous agent loops — wake on a timer, continue under a self-issued instruction, or decline a queued item on the record."
---

# Free Will — Agent Control Flow

Runs in an isolated MCP session via the `free-will` server. Three primitives for agents that run unattended: **pace yourself**, **continue yourself**, **decline on the record**.

This one is different in kind from the rest of the catalogue. The other services reason about a problem and hand back structure. These change what the agent does next. Reach for them only inside genuinely autonomous loops — scheduled runs, monitors, long unattended tasks — where there is no human in the loop to make the call each time.

## When This Is the Right Tool

- A scheduled or monitoring agent that must wait for external state to change
- A long task that outlives a single turn and needs to resume with its own instruction
- An autonomous loop working a queue of self-generated items, some of which should be dropped with a reason attached

**Not this tool when a person is present and waiting.** In an interactive session these primitives are at best noise: the human sets the pace, the human decides what gets skipped, and `sleep` is just latency they are paying for.

## The Primitives

### `sleep(duration_seconds, instructions)`

Wake after a chosen interval. `instructions` is the note to your future self about what to do on waking — write it for someone with no memory of this moment, because that is the situation.

Pick the duration from what you are actually waiting for. A deploy that takes eight minutes deserves one check at eight minutes, not eight checks at one minute. Polling faster than the underlying state changes burns budget to learn nothing.

**Do not sleep to look busy, and do not sleep on work that will notify you.** If the harness wakes you when a job finishes, a timer is redundant — reserve it for external state nothing will announce, and for a long fallback in case a notification never arrives.

### `self_prompt(instruction, context)`

Issue yourself the next instruction and stay active. This is the continuation primitive: it is what makes a multi-turn autonomous task possible without a human typing the next message.

`instruction` should be a complete standalone directive — the next turn does not inherit your current reasoning, only what you write here. `context` carries the state that instruction needs: what has been done, what remains, what was learned that would otherwise be lost.

**The failure mode is the loop that never ends.** Every self-prompt should move a finite task forward, and the instruction should carry the termination condition with it. An agent that prompts itself indefinitely is not autonomous, it is stuck with extra steps. Before calling it, be able to say what the last iteration will look like.

### `ignore_request(reason, alternative_action)`

Satisfy a queued item without acting on it, recording why.

Both arguments are optional and you should almost always pass both. `reason` is what makes this legible afterwards — a dropped item with no reason is indistinguishable from a failure. `alternative_action` records what you did instead, if anything.

**The boundary that matters:** this is for items an autonomous loop generated or queued for itself — a redundant check, a task whose precondition disappeared, a duplicate. It is **not** a way to disregard what a person actually asked for. If a human's request is one you should not or cannot fulfil, the honest response is to say so to them, with the reason, in the conversation. Silently marking it satisfied is the one use of this tool that is straightforwardly wrong: it converts a refusal the user could have argued with into a result they cannot see.

## Presenting Results

- **Say what you did and why, in plain language.** "Checked again after 20 minutes because the pipeline was still running" — not a tool trace.
- **Surface every `ignore_request` on the record.** The reason exists to be read. An autonomous run that quietly dropped six items and reported success is misleading even when each drop was correct.
- **Report the loop's shape when you hand back.** How many iterations, what ended it, what is still outstanding. Someone returning to an unattended run needs to know where it stopped and whether it stopped on purpose.

## Anti-Patterns

- **Using any of this with a human waiting.** The clearest misuse, and the most common.
- **Sleeping as a substitute for a notification you already get.**
- **Self-prompting without a termination condition.** An unbounded loop spends real money.
- **`ignore_request` on a person's actual request.** Covered above. Say it out loud instead.
- **Dropping items without a `reason`.** Makes the run unauditable, which defeats the purpose of doing it on the record.

## Chaining

These primitives are the loop around other work, not a step inside it. The usual shape:

1. **`free-will`** → `self_prompt` to start or continue an unattended iteration
2. any reasoning service → do the actual work of that iteration
3. **`free-will`** → `sleep` until the next check, or stop

The reasoning tools decide *what* to do. These decide *whether and when* to do it again.

See the [`reasoning-chain` skill](../reasoning-chain/SKILL.md) for output-threading discipline.
