# Genesis Rules for 512

This document defines the conditions under which the 512 constitution
comes into existence, how it is identified, and how it may be extended
without corruption.

These rules are descriptive, not authoritative. They do not grant
control to any person or entity.

---

## 1. Canonical Object

The file `512.md` located in `/genesis/` is the sole canonical text of 512.

No other file, format, summary, translation, or derivative document
has canonical status.

If a document conflicts with `512.md`, the document is incorrect by
definition.

---

## 2. Genesis Event

The genesis of 512 occurs exactly once.

Genesis is defined as the moment when:
- the SHA-256 hash of `512.md` is computed, and
- that hash is irreversibly anchored on a public distributed ledger.

The genesis event is a historical fact, not a claim.

---

## 3. Immutability

After the genesis event:
- `512.md` MUST NOT be modified.
- Any modification to its contents produces a different document and a
  different hash.
- Modified versions are not updates; they are new documents.

There is no mechanism for retroactive correction.

---

## 4. Descendant Versions

New documents may be created that:
- explain,
- translate,
- implement,
- annotate, or
- apply

the principles of 512.

Such documents are descendants if and only if they:
- are hashed independently, and
- explicitly reference the genesis hash of `512.md`.

Descendants do not alter 512. They point to it.

---

## 5. Forks

Forks are permitted.

A fork occurs when a document:
- changes the meaning of any invariant in `512.md`, or
- omits or weakens any invariant.

Forks MUST declare their own genesis and MUST NOT claim descent from
the original 512 genesis hash.

---

## 6. No Reserved Authority

The author of 512:
- retains no special rights,
- grants no licenses,
- and asserts no enforcement authority.

Legitimacy derives solely from cryptographic verification and voluntary
adoption.

---

## 7. Source of Truth

Git repositories, mirrors, and archives are distribution mechanisms.

The cryptographic hash anchored at genesis is the only source of truth
for identifying 512.

---

## 8. Final Statement

512 is not owned.
512 is not updated.
512 is not enforced.

512 exists.
