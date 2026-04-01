# 512 Properties Checklist

This checklist defines the minimum observable properties a system
must exhibit to satisfy 512's constraints at the execution boundary.

Satisfaction is binary. A system that does not exhibit all properties
does not satisfy 512's properties — regardless of naming or intent.

This checklist is a developer reference, not a certification instrument.

> **Pre-hardening phase in progress.** See [`PRE_HARDENING_NOTICE.md`](../PRE_HARDENING_NOTICE.md).

---

## Boundary Properties

- [ ] No private data is recorded on the public ledger —
      only cryptographic fingerprints and minimal metadata

- [ ] Settlement occurs only at the commit boundary —
      the point at which a proposed action becomes irreversible

- [ ] The canonical kernel hash is referenced in the implementation —
      SHA-256: `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

- [ ] Settlement cost is explicitly allocated to the party
      asserting finality — cost is not hidden or deferred

- [ ] Consent may be withdrawn and exit is possible
      prior to settlement — no action becomes irreversible
      before the commit boundary is crossed

- [ ] The system fails open — on failure, governing rules
      are revealed and control returns to the human party

- [ ] All seven invariants are evaluated at every execution
      boundary — partial evaluation is non-satisfaction

---

## Commit Path Properties

- [ ] There exists exactly one path to irreversible state change —
      no parallel, fallback, admin, or override paths reach the
      execution surface without passing through boundary evaluation

- [ ] The evaluation result is the structural prerequisite for the
      commit path to open — not a prior check, not a message passed
      to a downstream layer, not advisory input to an independent
      execution surface

- [ ] No procedural control (access policy, documented prohibition,
      contractual restriction) is relied upon as a substitute for
      structural elimination of bypass paths — the paths must not
      exist, not merely be restricted

- [ ] Evaluation and execution are not structurally separated —
      a pre-check architecture where evaluation runs before an
      independently operable execution surface does not satisfy
      this property

---

## What This Checklist Does Not Cover

This checklist does not address:

- correctness of upstream constraint definitions
- identity, governance, or enforcement logic
- witness or evidence architecture (see Evidence-Sidecar repo)
- regulatory or legal sufficiency in any jurisdiction

Those are outside 512's scope.

---

## Reference

Invariant definitions: `512-core/KERNEL/INVARIANTS.md`
Boundary mechanics: `512-ops/COMMIT_BOUNDARY_REFERENCE.md`
Commit path ownership and non-conformant patterns: `512-ops/COMMIT_BOUNDARY_REFERENCE.md §8–9`
Drift patterns: `ANTI_DRIFT.md`
Kernel text: `512-core/KERNEL/512-kernel.txt.txt`
