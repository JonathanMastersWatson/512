# Tests

This directory contains deterministic validation for the 512 runtime interface.

Tests verify:

- invariant evaluation behavior
- request validation behavior
- output token correctness
- evaluation ordering
- early-exit behavior
- boundary-condition handling

---

## Principles

Tests must be:

- deterministic
- reproducible
- stateless
- version-aligned with the locked interface

Tests validate runtime behavior against the canonical interface contract.

They do not redefine runtime semantics.

---

## Scope

Validation includes:

- ALLOW paths
- DENY paths
- malformed requests
- invariant ordering
- edge conditions
- replay consistency

---

## Non-Negotiable

If runtime behavior and tests diverge:

> the locked interface contract is authoritative.
