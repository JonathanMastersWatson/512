# Living Documents

This file identifies documents in the 512 repository that are dynamic —
subject to ongoing revision or alignment updates.

Living documents reflect the current best understanding of the architecture
or pattern. They will not relax constraints — only clarify or tighten them.

---

## Current Living Documents

| Document | Location | Why Dynamic |
|---|---|---|
| `512_ARCHITECTURE` | `/BUILDERS/` | CTO/Board-level architecture reference. Version-bumped on content change. |
| `512_IMPLEMENTATION` | `/BUILDERS/` | Engineer-level build reference. Version-bumped on content change. |
| `ANTI_DRIFT.md` | Repo root | Expanded as new drift patterns are identified. |

---

## What Living Means

A living document:

- reflects the current best understanding of the architecture or constraint
- will converge toward a sealed version at major release boundaries
- will not relax constraints — only clarify or tighten them

A living document does **not**:

- change the seven invariants
- alter the canonical kernel hash
- modify the properties specification in ways that reduce stringency
- introduce new architectural claims not derivable from the 512 constraint

---

## Frozen Documents

The following are frozen and will not change:

| Document | Why Frozen |
|---|---|
| `512-core/KERNEL/512-kernel-padded.txt` | Canonical kernel — sealed at genesis |
| `CANONICAL_COMMITMENT.md` | Priority record — append-only |
| `CANON_HASHES.md` | Cryptographic fingerprint record — sealed |
| `LICENSE` | CC BY 4.0 — fixed |

---

## Sealed Release — May 2026

Hardening phase complete. All living documents have been version-sealed
as of May 2026. Repository status is Active. Pre-hardening banners and
notices have been removed. A new archive hash will be committed to
record the sealed state.

Archive hash record: `CANONICAL_COMMITMENT.md` at repo root.
