# Layer Reference

This document defines the three-layer architecture of a system
satisfying 512's properties and the boundaries between layers.

It is a semantic firewall. Each layer has a defined function and
a defined set of things it must not do. Conflating any two layers
produces a system that cannot be independently verified.

---

## The Three Layers

| Layer | Function | Must Not Do |
|---|---|---|
| **Kernel** | Define the seven invariants. Establish what constraint satisfaction means. Provide the canonical commitment hash. | Enforce constraints. Capture evidence. Define domain-specific constraint logic. Interpret its own invariants at runtime. |
| **Commit Boundary (Gate)** | Evaluate Proposal Objects against the compiled constraint set. Produce ALLOW or DENY. Maintain exclusive commit authority over the non-bypassable commit path. Produce Evaluation-Unavailable DENY when evaluation cannot complete — commit path remains closed. | Define constraints. Interpret policy. Produce scores, recommendations, or probabilistic outputs. Capture or store evidence. Allow parallel execution paths. |
| **Witness Layer (CVS)** | Observe execution events out-of-band. Record cryptographic evidence. Classify ungoverned periods as evidence chain gaps. Anchor Merkle batch commitments to a public settlement ledger. | Influence execution. Enforce constraints. Produce gate outputs. Block execution. Control the commit path. |

---

## What Each Layer Produces

| Layer | Output |
|---|---|
| Kernel | Seven invariants. Canonical commitment hash. Spec hash mechanism. |
| Commit Boundary | ALLOW or DENY. No third value. When evaluation cannot complete: DENY (evaluation_unavailable); commit path remains closed; CVS sidecar records gap. |
| Witness Layer | Evidence Objects. Hash-chained records. Merkle batch anchors on public ledger. Evidence chain gap records for ungoverned periods. |

---

## What No Layer May Claim

| Prohibited Claim | Reason |
|---|---|
| "The gate has three outputs" | The gate produces ALLOW or DENY only. Evidence chain gaps are a witness layer classification. |
| "CVS is optional in a full 512/CVS system" | A gate without a witness layer enforces constraints but produces no independently verifiable record. In a full deployment, the witness layer is required for evidentiary accountability. |
| "The kernel defines enforcement" | The kernel defines invariants. Enforcement is the gate's function. |
| "The gate interprets constraints" | The gate evaluates a compiled constraint set. Interpretation occurs upstream, at definition time — not at evaluation time. |
| "The witness layer can influence execution" | The witness layer is passive. Any architecture in which CVS can alter, delay, or block execution is not a witness architecture. |
| "A pre-check satisfies the boundary requirement" | A system that evaluates proposals upstream of an independently operable execution surface has no commit boundary. It has a check and a separately governed execution surface. |

---

## Layer Separation Is Structural, Not Procedural

Layer separation is not achieved by policy, documentation, or
access controls. It is achieved by structural isolation:

- The gate does not have write access to the evidence store
- The witness layer does not have access to gate configuration
  or constraint specifications
- No single operator role controls both the gate and the
  witness layer simultaneously
- The commit path has exactly one entry point: gate evaluation

Procedural controls do not substitute for structural separation.
A system that relies on documented prohibitions to maintain layer
separation has not achieved layer separation.

---

## The Core Invariant of This Architecture
There exists exactly one path to irreversible state change.
That path is owned and resolved by the gate.
If any execution path exists outside gate control,
the system is non-conformant.

---

## Related Files

- `512-core/KERNEL/INVARIANTS.md` — the seven kernel invariants
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — boundary mechanics,
  non-conformant patterns, commit path ownership
- `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — upstream constraint
  definition (kernel → compiled constraint set)
- `512-ops/REFERENCE_FLOW.md` — end-to-end sequence from intent
  to anchored evidence
- `TERMS.md` — canonical vocabulary for all three layers
- `ANTI_DRIFT.md` — how implementations drift from this model
