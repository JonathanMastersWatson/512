# 512 Properties Checklist

This checklist defines the minimum observable properties a system
must exhibit to satisfy 512's constraints at the execution boundary.

Satisfaction is binary. A system that does not exhibit all properties
does not satisfy 512's properties — regardless of naming or intent.

This checklist is a developer reference, not a certification instrument.

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
Kernel text: `512-core/KERNEL/512-kernel.txt.txt`
