---
name: proving-with-logic
description: "Decide logic questions with solvers instead of judgement — SAT, entailment, consistency, FOL/SMT proofs, temporal traces. Use when a wrong answer is expensive and you need a real proof."
---

# Formal Logic — Deterministic Proof

Runs in an isolated MCP session via the `formal-logic` server. **This server is deterministic and LLM-free.** Every answer comes from PySAT, SymPy or Z3 — the same input always returns the same result, and a proof is a proof rather than a confident opinion.

That property is the whole value. Language models are unreliable at long logical chains and reliably wrong about satisfiability at scale. Hand those questions to a solver.

## When This Is the Right Tool

- Checking whether a set of rules, permissions or constraints can all hold at once
- Verifying a conclusion actually follows from stated premises
- Confirming a refactor preserved the meaning of a condition
- Checking an execution trace against a temporal property
- Any place where "it looks right" is not good enough

**Not this tool when:** the premises are fuzzy, the question is about values or trade-offs, or the hard part is deciding what to model rather than solving it. Formalizing an ill-posed question produces a rigorous answer to the wrong problem.

## Formula Syntax

**Propositional** — variables `p`, `q`, `r`; operators `&` (and), `|` (or), `~` (not), `->` (implies), `<->` (iff).

**First-order** — quantifiers `forall`, `exists`; predicates `P(x)`; functions `f(x)`.

**Temporal (LTL)** — `G` always, `F` eventually, `X` next, `U` until.

Getting syntax wrong is the most common failure. When a call errors, re-read the formula before re-reading the tool.

## Propositional Tools

**`is_satisfiable(formula)`** — can this be true at all? Pass `return_all_models` and `max_models` to enumerate satisfying assignments; `algorithm` selects the PySAT backend. An unsatisfiable formula means your constraints contradict each other — usually the finding, not an error.

**`check_consistency(formulas)`** — takes a *list* and asks whether they can all hold simultaneously. This is the workhorse for rule sets: permission models, feature-flag combinations, business rules accumulated over years. Inconsistency here is a real bug in the rules.

**`entails(premises, conclusion)`** — does the conclusion necessarily follow? SAT-based refutation. Pass `generate_proof` when you need to show the work, not just the verdict. This is the tool for "we concluded X from these facts — is that actually sound?"

**`simplify(formula)`** — minimal equivalent form via SymPy. Best use: paste a gnarly nested condition from real code and see what it actually says. Conditions that simplify to `True` or to a single variable are live bugs.

**`to_cnf(formula)` / `to_dnf(formula)`** — normal-form rewrites, each with an optional `simplify`. CNF for solver input; DNF for enumerating the cases a condition covers.

## First-Order and SMT

**`fol_prove(premises, conclusion)`** — Z3-backed first-order proof. Use when propositional variables cannot express the claim because it quantifies over things.

**`smt_prove(smtlib_source)`** — takes SMT-LIB v2 directly, bypassing the FOL string parser. Reach for this with arithmetic, bitvectors, arrays, or anything the FOL parser rejects. Set `logic` when you know the fragment; it is faster and fails more clearly.

Both accept `timeout_ms`. Z3 not returning is a result too — say "the solver did not decide within the timeout", never "it is false".

## Temporal

**`ltl_check(formula, trace)`** — verifies an LTL formula against an execution trace. Use it on state machines, retry and backoff logic, and lifecycle invariants: "the connection is never used after close" is `G(close -> X G ~use)`.

## Presenting Results

- **Report the verdict plainly, then what it means.** "Unsatisfiable" is the answer; "these three permission rules cannot all hold, so this role is unreachable" is the finding.
- **Translate back to the user's domain.** Nobody asked about `p & ~q`. They asked about their retry logic.
- **A counterexample is the deliverable.** When a formula is satisfiable in a way that surprises the user, that assignment is the bug. Show it.
- **Distinguish "proved false" from "not proved".** Failure to prove entailment does not establish the negation. Conflating these is the one error that makes formal tooling actively misleading.
- **Show the formalization.** The translation from English to formula is the step where mistakes hide. Let the user check it.

## Anti-Patterns

- **Formalizing what you have not understood.** A precise answer to a mis-modelled question is worse than no answer, because it carries unearned authority.
- **Using it for questions of degree.** Logic decides true and false, not "better".
- **Silently dropping premises that were hard to encode.** If a constraint could not be expressed, say so — the proof is only over what you actually gave it.
- **Treating a timeout as a negative.** It is "unknown".
- **Reaching for `fol_prove` when propositional would do.** Propositional tools are faster and their output is easier to read.

## Chaining

Formal logic verifies rather than explores, so it belongs near the end:

1. `sequential-thinking` → lay out the argument step by step
2. **`formal-logic`** → check the steps actually entail the conclusion
3. `devils-advocate` → attack the premises the proof depends on

A proof is only as good as its premises. Verifying the inference and never questioning the inputs is a classic way to be rigorously wrong.

See the [`reasoning-chain` skill](../reasoning-chain/SKILL.md) for output-threading discipline.
