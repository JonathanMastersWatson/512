# Semantic Equivalence in 512

This document defines how meaning is preserved across implementations,
translations, and explanations of 512.

---

## Canonical Meaning

The canonical meaning of 512 is defined solely by the contents of `512.md`
identified by the genesis hash.

Meaning is derived from invariants, not wording.

---

## Equivalent Documents

A document is semantically equivalent if and only if:

- all invariants in `512.md` are preserved
- no invariant is weakened, omitted, or reinterpreted
- no new authority or enforcement is introduced

Equivalent documents may differ in language, format, or structure.

---

## Descendant Documents

A descendant document must:

- reference the genesis hash of `512.md`
- declare itself non-canonical
- preserve all invariants without modification

Descendants explain or apply 512.  
They do not redefine it.

---

## Forks

A fork occurs when a document:

- alters the meaning of any invariant
- introduces new mandatory constraints
- asserts authority over interpretation or enforcement

Forks must declare independent genesis and MUST NOT reference the original
genesis hash.

---

## Dispute Resolution

Disputes are resolved by:

- comparing claims against the canonical text
- verifying preservation of invariants
- validating hashes

Author intent, popularity, and adoption are irrelevant.

---

## Summary

512 does not evolve through consensus.

512 remains fixed.
