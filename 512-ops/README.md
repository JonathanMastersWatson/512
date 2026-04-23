# 512-ops — Operational Reference

This directory contains the working reference for organisations
building systems that satisfy 512's properties at the execution
boundary.

These documents are operational. They are not the kernel.
The kernel is defined in `512-core/KERNEL/512-kernel.txt.txt`
and is immutable. These documents describe how to build against it.

---

## Start Here

| File | What it covers |
|---|---|
| [`COMMIT_BOUNDARY_REFERENCE.md`](./COMMIT_BOUNDARY_REFERENCE.md) | Where the boundary is, what crosses it, what the gate evaluates, what it produces — including non-conformant patterns |
| [`INTEGRATION_STEPS.md`](./INTEGRATION_STEPS.md) | 7-step workflow from boundary identification to verified evidence chain |
| [`CONSTRAINT_DEFINITION_LAYER.md`](./CONSTRAINT_DEFINITION_LAYER.md) | How to translate policies into binary-reducible constraints before the gate sees them |
| [`REFERENCE_FLOW.md`](./REFERENCE_FLOW.md) | End-to-end sequence: intent → proposal → evaluation → commit authorisation → execution → evidence → anchor |
| [`PROPERTIES_CHECKLIST.md`](./PROPERTIES_CHECKLIST.md) | Go-live verification checklist — binary pass/fail per property |

---

## Layer Reference

Before building, read [`LAYER_REFERENCE.md`](../LAYER_REFERENCE.md).

It defines the three-layer architecture — Kernel / Commit Boundary /
Witness Layer — and what each layer must not do. It is the semantic
firewall between the kernel, the gate, and the evidence system.

The core constraint stated there governs everything in this directory:

> There exists exactly one path to irreversible state change.
> That path is owned and resolved by the gate.
> If any execution path exists outside gate control,
> the system is non-conformant.

---

## Key Principles for Builders

**The gate is binary.** Every completed evaluation produces exactly
one of two outputs: ALLOW or DENY. There is no third output value.

**The commit path is non-bypassable.** No route to the execution
surface exists outside gate evaluation. Procedural controls —
access policies, documented prohibitions — do not satisfy this
requirement. The path must not exist, not merely be restricted.

**The gate has exclusive commit authority.** The gate's authorisation
signal is the structural prerequisite for the commit path to open.
It is not advisory. It is not delivered to a downstream layer for
interpretation or application.

**Fail-open is a system behaviour, not a gate output.** When the
gate cannot complete evaluation, it produces no output. Execution
proceeds under Invariant 6. The witness layer records the ungoverned
period as an evidence chain gap.

**Constraint definition is upstream work.** The gate evaluates
compiled constraints. It does not define them. Constraint definition
is the organisation's responsibility and must be complete before
gate evaluation begins. See `CONSTRAINT_DEFINITION_LAYER.md`.

---

## Related

- [`../LAYER_REFERENCE.md`](../LAYER_REFERENCE.md) — three-layer
  semantic firewall
- [`../TERMS.md`](../TERMS.md) — canonical vocabulary
- [`../ANTI_DRIFT.md`](../ANTI_DRIFT.md) — how implementations
  drift and how to prevent it
- [`../512-core/KERNEL/INVARIANTS.md`](../512-core/KERNEL/INVARIANTS.md)
  — the seven invariants the gate evaluates
