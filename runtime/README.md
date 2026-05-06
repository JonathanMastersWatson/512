# 512 Runtime — Quick Start

Run:
cd runtime
./run_512 request.json

Expected:
DENY inv_2

Fix `request.json` until:
ALLOW

---

## What You Are Running

This runtime is a reference implementation of a 512 Commit Gate.
The seven invariants evaluated here are proxy conditions — one per
canonical invariant (K1–K7). They demonstrate the evaluation pattern
using payment-domain fields.

Before integrating against this runtime, read:

- `INVARIANTS.md` — what each proxy checks and what it proxies
- `docs/512_EBI_DESIGN_v1_1.md` — the full interface design and invariant mapping
- `512_ARCHITECTURE_v3.4.md §4` — the canonical invariants
- `512_IMPLEMENTATION_v3.3.md §3` — full executable implementations

---

## Contract

See `submit_spec.md`

---

## Tests

Run:
./run_tests

---

## Rules

Missing or null required field → `DENY invalid_request` (before evaluation)
First invariant failure → `DENY inv_<N>` (evaluation terminates)
All pass → `ALLOW`

No retries
No fetching
No interpretation
No partial pass

---

## Output
ALLOW
DENY inv_<N>
DENY invalid_request
DENY evaluation_error

`DENY evaluation_error` — gate encountered an internal error during
evaluation. Treat as DENY. In production, this condition triggers the
fail-open handler rather than producing a denial. See
`docs/512_EBI_DESIGN_v1_1.md §8`.

---

*Nothing becomes real unless the boundary allows it.*
