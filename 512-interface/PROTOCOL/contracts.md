# Contract Protocol

## Purpose

This document specifies how contracts operate in systems adhering to the
512 Kernel.

Contracts bind behavior.
They do not override kernel invariants.

---

## Kernel Inheritance

All contracts implicitly inherit the 512 Kernel.

No contract term may:
- compel non-voluntary participation,
- authorize force or fraud,
- introduce hidden rules,
- or prevent exit.

If a contract conflicts with the kernel, the kernel prevails.

---

## Explicitness

Contracts must be explicit.

Material terms must be:
- visible to all affected parties,
- readable in plain language or machine-parsable form,
- identifiable prior to acceptance.

Silence, ambiguity, or buried terms do not constitute agreement.

---

## Equality of Enforcement

Contracts must be equally enforceable by all parties.

Asymmetric enforcement mechanisms,
including unilateral modification or selective application,
violate adherence.

---

## Modification

Contract modification requires:
- explicit disclosure of changes,
- renewed consent by affected parties.

Unilateral changes without consent are invalid.

---

## Termination and Exit

Contracts must permit exit.

Exit conditions must be:
- disclosed in advance,
- non-coercive,
- and executable without undisclosed penalties.

---

## Evidence and Contestability

Contracts must support contestability.

Systems must be able to show:
- which contract governed an interaction,
- which clause was invoked,
- and how it was applied.

Proof may be provided via hashes, receipts, or signed records.
