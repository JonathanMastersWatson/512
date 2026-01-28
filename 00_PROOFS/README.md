# Proofs and Verification Artifacts

This directory contains **cryptographic and external proofs** that attest to
the existence, integrity, and verification of artifacts referenced elsewhere
in this repository.

Materials in this directory do **not** define 512.
They provide **verifiable evidence** about specific representations or events.

---

## Scope

`00_PROOFS/` is reserved for:

- Cryptographic hashes
- External anchoring receipts
- Timestamped attestations
- Verification procedures

All files here are **append-only**.
Existing proofs MUST NOT be modified or replaced.

---

## Contents

### 512 Kernel — Padded Artifact Hash

- **File:** `512_KERNEL_PADDED_SHA256.md`
- **Artifact:** `512-core/KERNEL/512-kernel-padded.txt`
- **Purpose:**  
  Records the SHA-256 hash of the fixed-width, 512-byte padded representation
  of the canonical 512 kernel text.

This proof verifies **byte-level integrity only**.
Canonical meaning remains defined by the unpadded kernel text in `/512-core/CANON/`.

---

### External Anchoring

- **File:** `XRPL_GENESIS_RECEIPT.md`
- **Purpose:**  
  Records external anchoring evidence for historical reference.

---

## Interpretation Rules

- Proofs document **what exists**, not **what is authoritative**
- Proofs do not confer ownership, control, or governance
- Proofs may be independently verified by any third party

---

## Status

This directory is a **verification ledger**.

New proofs may be added.
Existing proofs are immutable.
