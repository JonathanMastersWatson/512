# Interface

This directory contains canonical interface contracts for 512.

Interfaces define:

- boundary request structure
- boundary response structure
- versioned integration surfaces

Interfaces are:

- deterministic
- language-agnostic
- immutable once sealed

Runtime implementations may evolve.

Canonical interfaces must not.

---

## Scope

This directory is reserved for:

- proposal schemas
- decision schemas
- interface version definitions

It does not contain:

- runtime logic
- invariant implementation
- orchestration logic
- policy interpretation
