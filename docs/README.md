# Documentation

This directory contains explanatory and design documentation for 512.

Canonical runtime behavior is defined in:

- `/runtime/INTERFACE_LOCK.md`

The runtime implementation lives in:

- `/runtime/`

The runtime interface is authoritative.
Documentation explains the interface but does not redefine it.

---

## Purpose

- Describe execution-boundary behavior
- Define interface semantics
- Explain invariant mappings
- Provide runtime usage guidance
- Document conformant and non-conformant patterns

---

## Key Files

- `512_EBI_DESIGN_v1_0.md`
- `512_EBI_DESIGN_v1_1.md`

These documents describe:

- the Execution Boundary Interface (EBI)
- proposal and decision semantics
- invariant mappings
- runtime topology
- boundary placement requirements

---

## Principle

Documentation supports the runtime.

If runtime behavior and documentation diverge:

> the runtime interface is authoritative.
