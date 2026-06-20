Full output contract: `ALLOW`, `DENY inv_<N>`, `DENY invalid_request`,
`DENY evaluation_error`

---

## Request Shape

```json
{
  "intent":      {},
  "constraints": {},
  "context":     {}
}
```

All three top-level fields must be present.

---

## Required Fields

| Field | Proxies canonical invariant |
|---|---|
| `intent.action` | K3 — exit rights |
| `intent.target` | K6 — Transparent Denial / Human Default |
| `context.identity` | K1 — no force or fraud |
| `context.consent` | K2 — voluntary explicit consent |
| `context.timestamp` | K5 — no hidden rules |
| `context.system_state` | K7 — immutable specification |
| `constraints.max_amount` | K4 — explicit, enforceable contracts |

Canonical invariant definitions: `512_ARCHITECTURE_v3.4.md §4`
Full field requirements for production: `512_IMPLEMENTATION_v3.3.md §3`
Proxy-to-canonical mapping: `docs/512_EBI_DESIGN_v1_1.md §4`

---

## Rules

Missing or null required field → `DENY invalid_request` (before evaluation)
First invariant failure → `DENY inv_<N>` (evaluation terminates)
All pass → `ALLOW`

No defaults
No inference
No mutation

---

## Output
ALLOW
DENY inv_<N>
DENY invalid_request
DENY evaluation_error

`DENY inv_<N>` — invariant N failed; N is 1–7
`DENY invalid_request` — malformed request; evaluation did not begin
`DENY evaluation_error` — internal gate error; treat as DENY; see
`docs/512_EBI_DESIGN_v1_1.md §8` for production Evaluation-Unavailable DENY behaviour
