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

---

## Input Contract (Frozen)

Request shape:

{
  "intent": {},
  "constraints": {},
  "context": {}
}

Required fields:

- intent.action
- intent.target
- context.identity
- context.consent
- context.timestamp
- context.system_state
- constraints.max_amount

Rules:

- Missing or null required field → DENY
- No defaults
- No inference
- No mutation

---

## Output Contract (Frozen)

The runtime produces exactly one of:

ALLOW

DENY <invariant_id>

DENY invalid_request

---

## Behavioral Guarantees

- Deterministic evaluation
- Stateless execution
- No retries
- No external data fetching
- No interpretation layer
- No partial results

---

## Non-Negotiable

If a change modifies:

- input shape
- required fields
- output format
- evaluation determinism

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

- Replace placeholder invariant mappings with canonical 512 mappings
- Integrate CVS for evidence generation
- Extend constraint richness upstream

None of the above modifies this interface.

---

## Principle

> The interface is stable.  
> The truth it enforces evolves.
