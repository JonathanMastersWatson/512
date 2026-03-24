# Upstream: Constraint Architecture

512 enforces admissibility at the commit boundary.

It does not define what is admissible. That is the function of the
upstream Constraint Architecture discipline.

---

## The Stack

| Layer | Function |
|---|---|
| Constraint Architecture | Defines what is admissible — the boundaries within which execution is permitted |
| 512 | Enforces admissibility at the commit boundary — binary, deterministic, at machine speed |
| CVS | Witnesses execution and produces independently verifiable evidence |

Constraint Architecture defines the world.
512 enforces it.
CVS proves it.

---

## Separation

512 receives compiled constraint specifications.
It evaluates them deterministically.
It does not define them.

The formation of constraint boundaries — consent logic, authority
models, thresholds, domain-specific admissibility rules — is the
responsibility of the Constraint Architecture layer.

Errors in constraint definition are upstream failures.
512 will faithfully enforce incorrectly defined constraints.
That is by design.

---

## Reference

Constraint Architecture is documented at:

https://github.com/JonathanMastersWatson/Constraint-Architecture

---

## What This Means for Builders

If you are building a system that satisfies 512's properties,
you need to answer one question before you touch the boundary:

**What is the declared admissible state space?**

That question is answered upstream, not at the boundary.
The boundary enforces the answer. It does not produce it.
