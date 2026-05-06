# 512 Runtime — Interface Lock

This directory defines the **execution interface** for 512.

As of this commit, the interface is **frozen**.

---

## Scope

The lock applies to:

- `run_512`
- `evaluator.py`
- `submit_spec.md`
- `request.json`
- `tests.json`
- `run_tests`
- `README.md` (within `/runtime/`)

The following documents describe the interface but are not themselves
part of the locked surface — they may be updated without constituting
a breaking change:

- `INVARIANTS.md` — proxy-to-canonical mapping documentation
- `docs/512_EBI_DESIGN_v1_1.md` — full interface design specification

---

## Input Contract (Frozen)

Request shape:

```json
{
  "intent":      {},
  "constraints": {},
  "context":     {}
}
```

Required fields:

- `intent.action`
- `intent.target`
- `context.identity`
- `context.consent`
- `context.timestamp`
- `context.system_state`
- `constraints.max_amount`

Rules:

- Missing or null required field → `DENY invalid_request`
- No defaults
- No inference
- No mutation

---

## Output Contract (Frozen)

The runtime produces exactly one of:
ALLOW
DENY inv_<N>
DENY invalid_request
DENY evaluation_error

`DENY inv_<N>` — invariant N failed; N is 1–7; evaluation terminated
`DENY invalid_request` — malformed request; evaluation did not begin
`DENY evaluation_error` — internal gate error during evaluation

All DENY tokens are terminal. The reason code is diagnostic. No state
change follows any DENY under any condition.

---

## Behavioral Guarantees

- Deterministic evaluation
- Stateless execution
- No retries
- No external data fetching
- No interpretation layer
- No partial results
- Early-exit: first invariant failure terminates evaluation

---

## Non-Negotiable

If a change modifies:

- input shape
- required fields
- output format
- evaluation determinism
- invariant evaluation order

→ it is a **breaking change**

Breaking changes require:

- explicit versioning
- new interface surface
- not modification of this one

---

## Purpose

This lock exists to ensure:

- developers have a stable integration surface
- upstream systems can build against a fixed contract
- invariant mapping can evolve without changing the interface

---

## Future Work (Outside This Lock)

- ~~Replace placeholder invariant mappings with canonical 512 mappings~~
  **Complete** — see `INVARIANTS.md` and `docs/512_EBI_DESIGN_v1_1.md §4`
- Integrate CVS for evidence generation
- Extend constraint richness upstream

None of the above modifies this interface.

---

## Principle

> The interface is stable.
> The truth it enforces evolves.
