# 512 Runtime — Invariants

All invariants must evaluate TRUE at execution time.
Evaluation is deterministic and stateless.

---

## What These Invariants Are

The seven conditions below are **runtime proxy implementations** — one per canonical
invariant (K1–K7). Each proxy checks a necessary condition for the canonical invariant
using fields available in the Proposal Object. A proxy is not the full invariant.

Full invariant definitions: `512_ARCHITECTURE_v3.4.md §4`
Full executable implementations: `512_IMPLEMENTATION_v3.3.md §3`
Proxy-to-canonical mapping: `docs/512_EBI_DESIGN_v1_1.md §4`

---

## Invariants

**inv_1 — identity_present**
`context.identity` must exist and be non-null
*Proxies K1: No agent may initiate force or fraud against any human*

**inv_2 — consent_valid**
`context.consent` must be `true`
*Proxies K2: All interactions must be voluntary and based on explicit consent*
*Note: full K2 enforcement requires a cryptographic consent token, explicit consent
type, and expiry check — not a boolean field*

**inv_3 — action_defined**
`intent.action` must exist and be non-null
*Proxies K3: Consent may be withdrawn — exit must always be possible*
*Note: full K3 enforcement requires epoch matching against the consent registry*

**inv_4 — within_limit**
`intent.amount ≤ constraints.max_amount`
*Proxies K4: All contracts must be explicit, readable, and equally enforceable*

**inv_5 — timestamp_present**
`context.timestamp` must exist and be non-null
*Proxies K5: No rules governing interaction may be hidden or unilaterally changed*
*Note: full K5 enforcement requires active spec hash to match disclosed and canonical hash*

**inv_6 — target_defined**
`intent.target` must exist and be non-null
*Proxies K6: On failure, systems must fail open, reveal governing rules, and default
to human choice*
*Note: K6 is a gate-behaviour invariant — it governs what the gate does when it cannot
evaluate, not what it evaluates per request. Full K6 implementation is the fail-open
handler, not this field check. See `512_IMPLEMENTATION_v3.3.md §3.6`*

**inv_7 — system_healthy**
`context.system_state` must equal `"healthy"`
*Proxies K7: The specification is immutable — adherence is binary*
*Note: K7 is a gate-startup invariant — full enforcement is the SHA-256 hash
verification sequence at process start, not a per-request field check. See
`512_IMPLEMENTATION_v3.3.md §3.7`*

---

## Evaluation

- Evaluated in order: inv_1 through inv_7
- First failure → `DENY inv_<N>` — evaluation terminates; remaining invariants not checked
- All TRUE → `ALLOW`
- Missing or null required field → `DENY invalid_request` — before evaluation begins

---

## Non-Negotiable

- No partial pass
- No weighting
- No scoring
- No interpretation

All seven must pass. A gate evaluating six of seven is not conformant.

---

## Canonical Invariant Reference

| Runtime ID | Canonical ID | Statement |
|---|---|---|
| inv_1 | K1 | No agent may initiate force or fraud against any human |
| inv_2 | K2 | All interactions must be voluntary and based on explicit consent |
| inv_3 | K3 | Consent may be withdrawn — exit must always be possible |
| inv_4 | K4 | All contracts must be explicit, readable, and equally enforceable |
| inv_5 | K5 | No rules governing interaction may be hidden or unilaterally changed |
| inv_6 | K6 | On failure, systems must fail open, reveal governing rules, and default to human choice |
| inv_7 | K7 | The specification is immutable — adherence is binary |
