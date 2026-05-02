# 512 Repository Archive Hash

This document records the cryptographic hash of the sealed repository
archive produced on 2026-05-01, following the hardening and BUILDERS
phase.

---

## Archive Details

| Field | Value |
|---|---|
| File | `512-main-2026-05-01.zip` |
| Date sealed | 2026-05-01 |
| Algorithm | SHA-256 |
| Hash | `DDC508C498CF156B4A86C83EBBE54E3F643EBC786C8A9027C41D8CD9BA254E290` |

---

## What This Hash Covers

This hash covers the complete repository state as downloaded from
`github.com/JonathanMastersWatson/512` on 2026-05-01, following
the May 2026 hardening pass which included:

- `CANONICAL_COMMITMENT.md` — new, permanent priority record
- `AARM_AND_512.md` — new, architectural positioning vs AARM/CSA
- `PRE_HARDENING_NOTICE.md` — updated to sealed status record
- `LIVING_DOCUMENTS.md` — updated to reflect sealed release
- `FAILURE_MODES.md` — pre-hardening banner removed
- `ANTI_DRIFT.md` — pre-hardening banner removed
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — pre-hardening banner removed
- `BUILDERS/` — new folder with full reference document suite:
  - `README.md`
  - `512_ARCHITECTURE_v3.4.md`
  - `512_IMPLEMENTATION_v3.3.md`
  - `AARM_AND_512.md`
  - `512_CVS_ENTERPRISE_v1_0.md`
  - `EXECUTION_BOUNDARY_PRINCIPLE.md`
  - `UNAUTHORIZED_BY_DESIGN.md`
  - `UNINSURABLE_BY_DESIGN.md`

Repository status: **Active**
Pre-hardening phase: **Closed**

---

## Verification

To verify this hash, download the archive and run:

```powershell
(Get-FileHash "512-main-2026-05-01.zip" -Algorithm SHA256).Hash
```

The output must match the hash recorded above exactly.

---

## Relationship to Kernel Hash

This archive hash records the state of the full repository.

It is distinct from the canonical kernel artifact hash:
`7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`

That hash covers only the 512-byte padded kernel file.
Both hashes are independently verifiable.

---

## Prior Sealed Archive

| Date | File | SHA-256 |
|---|---|---|
| 2026-03-24 | `512-main-2026-03-24.zip` | `DF27F6C5C8DDBBD5341FB15EA943D92B3388331B386C26F44A145673F6C8D218` |
| 2026-05-01 | `512-main-2026-05-01.zip` | `DDC508C498CF156B4A86C83EBBE54E3F643EBC786C8A9027C41D8CD9BA254E290` |

Full priority record: `CANONICAL_COMMITMENT.md` at repo root.
