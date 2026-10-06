# kernel-512

**Status:** Placeholder — code to be exported from the reference build.

---

The shared TypeScript kernel library. Everything load-bearing lives here;
the web app and the API server are callers, not re-implementations.

## Expected module layout

| Module | Responsibility |
|---|---|
| `schema.ts` | The seven canonical invariants, the seven-question spine, core field identifiers/types/tiers/enumerated values, fixed attestations, kernel and worksheet version constants, domain profile registry. |
| `commit-gate.ts` | Draft and action-time constraint checks; the Commit Gate evaluator (`evaluateCommitGateCore`); gate artifacts and decision receipts. One check per invariant: check_N governs invariant N — no check spans two invariants. |
| `bind.ts` | Record compilation and validation: compiles declared fields against the profile's allowed definitions, rejects unknown/duplicate fields and bad states, produces the canonical hashed `BindRecord`. |
| `canonical.ts` | Canonical JSON normalization and SHA-256 hashing: worksheet/profile/record identity, check version hashes, evaluation cores, gate artifacts, obligations. |
| `obligation-ledger.ts` | Obligation creation inside the ALLOW artifact and the pure deterministic fold over witnessed transition events (open / overdue / disputed / settled / voided). |

## Public boundary

- The kernel is a pure library: no I/O, no network, no fetching. The
  evaluator consumes a bound record, an action proposal, and caller-supplied
  live inputs — nothing else.
- `ALLOW` means eligible under the supplied evidence. It is not execution,
  service, settlement, or charge. `DENY` names exactly one failed check and
  its invariant.
- Kernel integrity is self-checked: canonical content hashes over the
  schema, checks, and canonicalization code; the gate emits an honest-null
  denial if the self-check fails.

## Relation to doctrine

- `OBLIGATION.md` (repo root) specifies the obligation layer this module
  implements.
- `SELF_POLICING.md` (repo root) specifies the cross-action matrix; the
  one-check-per-invariant mapping is its structural expression in code.
- The canonical invariants are `512-core/KERNEL/INVARIANTS.md`. This
  library must never redefine them.
