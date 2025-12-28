# Commitment Boundaries Under 512

512 distinguishes clearly between actions that are reversible and
actions that are irreversible.

Only irreversible actions require cryptographic settlement.

This document defines that boundary.

---

## 1. Reversible Actions (No Settlement)

The following actions are reversible and MUST NOT be settled on a
ledger:

- reasoning and computation
- negotiation of terms
- drafting of agreements
- signaling of intent
- conditional or provisional consent
- revocation prior to acceptance

These actions may be logged, cached, or recorded internally, but they
do not require public finality.

Recording reversible actions on a ledger is unnecessary and harmful to
scalability and privacy.

---

## 2. Irreversible Actions (Settlement Required)

An action crosses a commitment boundary when reversal would:
- impose harm on another party,
- create enforceable obligations, or
- be relied upon by third parties.

The following actions are irreversible and MUST be settled:

- acceptance of a binding contract
- finalization of a payment
- transfer of ownership or rights
- delegation of authority
- expiration of revocation rights
- anchoring of constitutional or policy text

At this boundary, settlement becomes mandatory.

---

## 3. Settlement Mechanism

Settlement consists of:
- hashing the committed artifact,
- recording the hash on a public ledger,
- achieving deterministic finality.

The ledger records proof, not content.

Settlement does not execute rules.
Settlement records the fact that commitment occurred.

---

## 4. Cost Allocation

Settlement has a non-zero cost.

Under 512:
- the party asserting finality bears the settlement cost,
- the cost is explicit and predictable,
- the cost is proportional to the value of finality.

This cost discourages frivolous or abusive commitments.

---

## 5. Privacy Preservation

Private data MUST NOT be recorded on the ledger.

Only cryptographic fingerprints and minimal metadata are permitted.

This ensures:
- confidentiality of terms,
- compliance with data protection regimes,
- verifiability without disclosure.

---

## 6. Enforcement

512 does not enforce behavior.

Systems MAY refuse to act on commitments that lack verifiable
settlement.

This refusal is local, voluntary, and mechanical.

---

## 7. Failure Modes

If settlement does not occur:
- the action remains reversible,
- no enforceable commitment exists,
- no third party is obligated to recognize the action.

This default protects all participants.

---

## 8. Summary

- Reversible actions are free.
- Irreversible actions are settled.
- Settlement records commitment, not intent.
- Finality is explicit and paid for.

This boundary is fundamental to scalability, freedom, and accountability
under 512.
