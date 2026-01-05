# SPEC_HASH (512)

SPEC_HASH binds **meaning**, not prose.

Kernel text may vary across languages and paraphrases.  
Canonical IR must not.

---

## Definition

**SPEC_HASH = HASH( JCS( CANONICAL_IR.json ) )**

Where:

- **CANONICAL_IR.json** is the invariant target set in this repository.
- **JCS(...)** is JSON Canonicalization Scheme (RFC 8785) or an equivalent deterministic canonicalization:
  - stable key ordering
  - normalized numbers
  - UTF-8
  - no insignificant whitespace differences
- **HASH(...)** is a cryptographic hash function (e.g., SHA-256).

---

## Required Properties

- If two kernel texts compile to the same canonical IR, they MUST produce the same SPEC_HASH.
- Any semantic mutation that changes an invariant MUST change SPEC_HASH.
- SPEC_HASH does not convey authority, authorship, or approval.
  It is only an identity for semantic equivalence.

---

## Operational Use

- Systems MAY publish SPEC_HASH alongside kernel text.
- High-stakes use SHOULD require multi-interpreter consensus on canonical IR prior to accepting a SPEC_HASH claim.
- On disagreement, systems MUST fail open and default to human choice / non-action.

