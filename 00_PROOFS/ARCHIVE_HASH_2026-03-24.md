# 512 Repository Archive Hash

This document records the cryptographic hash of the sealed repository
archive produced on 2026-03-24, following the hardening pass.

---

## Archive Details

| Field | Value |
|---|---|
| File | `512-main-2026-03-24.zip` |
| Date sealed | 2026-03-24 |
| Algorithm | SHA-256 |
| Hash | `DF27F6C5C8DDBBD5341FB15EA943D92B3388331B386C26F44A145673F6C8D218` |

---

## What This Hash Covers

This hash covers the complete repository state as downloaded from
`github.com/JonathanMastersWatson/512` on 2026-03-24, following
the hardening pass which included:

- README.md navigation and language hardening
- INVARIANTS.md corrected to 7 invariants
- KERNEL_EQUIVALENCE_AND_SPEC_HASH.md corrected to I1–I7
- COMPLIANCE_CHECKLIST.md replaced with Properties Checklist
- ANTI_DRIFT.md — new, 12 hardening additions
- COMMIT_BOUNDARY_REFERENCE.md — new developer boundary worksheet
- LICENSE — new CC BY 4.0 root licence
- UPSTREAM.md — new three-layer stack reference
- 512-core/CANON/README.md — properties language, I1..I7 corrected
- STS-0000 renamed — MANIFESTO removed from filename

---

## Verification

To verify this hash, download the archive and run:
```powershell
(Get-FileHash "512-main-2026-03-24.zip" -Algorithm SHA256).Hash
```

The output must match the hash recorded above exactly.

---

## Relationship to Kernel Hash

This archive hash records the state of the full repository.

It is distinct from the canonical kernel artifact hash:
`7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

That hash covers only the 512-byte padded kernel file.
Both hashes are independently verifiable.
