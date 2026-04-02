# Living Documents

This file identifies documents in the 512 repository that are dynamic —
subject to ongoing revision, hardening, or alignment updates.

Living documents are not frozen. They may not always be in full
alignment with each other during active hardening phases. Implementers
should treat them as directional references, not sealed specifications.

---

## Current Living Documents

| Document | Location | Why Dynamic |
|---|---|---|
| `512_ARCHITECTURE` | External canon repo | CTO/Board-level architecture reference. Under active language hardening. Version-bumped on content change. |
| `512_IMPLEMENTATION` | External canon repo | Engineer-level build reference. Under active normative framework development. Version-bumped on content change. |
| `ANTI_DRIFT.md` | Repo root | Expanded as new drift patterns are identified. |
| `512-ops/COMMIT_BOUNDARY_REFERENCE.md` | `/512-ops/` | Developer boundary reference. Being tightened to eliminate implementation ambiguity. |
| `512-ops/COMPLIANCE_CHECKLIST.md` | `/512-ops/` | Properties checklist. Updated as conformance criteria are hardened. |

---

## What Living Means

A living document:

- reflects the current best understanding of the constraint or pattern
- may be revised without a major version bump during hardening phases
- will converge toward a sealed version at the end of the current hardening pass
- will not relax constraints — only clarify or tighten them

A living document does **not**:

- change the canonical kernel (`512-core/KERNEL/512-kernel-padded.txt`)
- alter the seven invariants
- modify the canonical SPEC_HASH
- introduce new constraints not derivable from the seven invariants

---

## Frozen Documents

The following are frozen and will not change:

| Document | Why Frozen |
|---|---|
| `512-core/KERNEL/512-kernel-padded.txt` | Canonical artifact — hash-sealed |
| `512-core/KERNEL/512-kernel.txt.txt` | Canonical kernel text |
| `512-core/KERNEL/INVARIANTS.md` | Invariant definitions |
| `512-core/00_GENESIS/` | Genesis record — immutable by design |
| `00_PROOFS/` | Hash and XRPL proof record |
| `PRIMITIVE_BOUNDARY.md` | Defines the fixed scope boundary of the 512 primitive — not subject to revision |

---

## Sealed Release

At the end of the current hardening pass, living documents will be
version-sealed. `PRE_HARDENING_NOTICE.md` will be updated to reflect
sealed status and a new archive hash will be committed.

See `PRE_HARDENING_NOTICE.md` for current hardening phase status.
