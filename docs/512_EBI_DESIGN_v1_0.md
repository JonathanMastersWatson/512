# 512 Execution Boundary Interface — Design Specification

**Jonathan M. Watson | 512 / CVS Architecture**  
**Version 1.0 | May 2026**

---

## Abstract

The **Execution Boundary Interface** (EBI) is the formal seam between an upstream caller and the 512 Commit Gate. It is not a protocol. It is a position — defined by what sits on each side: authorization intent on the left, irreversible state change on the right. The EBI fixes the contract governing that crossing.

---

## 1. Boundary Position

The EBI is position-locked. It sits between authorization and commit.
[ Upstream Caller ]  →  [ EBI ]  →  [ Commit Gate ]  →  [ State Change ]
↑
Commit Boundary

Nothing crosses the commit boundary without traversing the EBI. There is no parallel path. There is no bypass under error conditions. The position is architectural, not configurable.

---

## 2. Interface Contract

### 2.1 Request Shape

```json
{
  "intent": {
    "action": "<string>",
    "target": "<string>",
    "amount": "<number>"
  },
  "constraints": {
    "max_amount": "<number>"
  },
  "context": {
    "identity": "<string>",
    "consent": "<bool: true>",
    "timestamp": "<ISO 8601>",
    "system_state": "<string: 'healthy'>"
  }
}
```

### 2.2 Required Fields

| Field | Type | Rule |
|---|---|---|
| `intent.action` | string | Must be present and non-null |
| `intent.target` | string | Must be present and non-null |
| `context.identity` | string | Must be present and non-null |
| `context.consent` | bool | Must be `true` |
| `context.timestamp` | string | Must be present and non-null |
| `context.system_state` | string | Must equal `"healthy"` |
| `constraints.max_amount` | number | Must be present; `intent.amount` must not exceed it |

Missing or null required field → **DENY**. No defaults. No inference. No mutation.

### 2.3 Output

The gate returns exactly one of:
ALLOW
DENY <invariant_id>
DENY invalid_request

No other output is valid. The EBI produces no scores, recommendations, partial approvals, or deferred responses.

---

## 3. Invariant Mapping

The gate evaluates seven invariants in order. First failure terminates evaluation and returns DENY.

| ID | Name | Condition |
|---|---|---|
| inv_1 | identity_present | `context.identity` is not null |
| inv_2 | consent_valid | `context.consent` is `true` |
| inv_3 | action_defined | `intent.action` is not null |
| inv_4 | within_limit | `intent.amount ≤ constraints.max_amount` |
| inv_5 | timestamp_present | `context.timestamp` is not null |
| inv_6 | target_defined | `intent.target` is not null |
| inv_7 | system_healthy | `context.system_state` equals `"healthy"` |

All seven must evaluate TRUE for ALLOW. There is no weighting, no scoring, no partial pass.

---

## 4. Caller Obligations

The caller is any upstream system that presents a request to the EBI.

**MUST:**
- Construct a complete, well-formed request before calling
- Block execution until a response is received
- Treat DENY as terminal — no state change follows a DENY under any condition

**MUST NOT:**
- Cache an ALLOW response and replay it for a subsequent action
- Retry a DENY without correcting the request
- Execute the intended action before receiving ALLOW
- Route around the EBI under degraded conditions

---

## 5. Gate Obligations

The gate is the 512 Commit Gate receiving the request at the EBI.

**MUST:**
- Evaluate all invariants in declared order
- Return exactly one output token per request
- Complete evaluation within the latency budget (software target: sub-50μs)
- Be stateless — each request evaluated independently

**MUST NOT:**
- Modify the request
- Fetch external data during evaluation
- Produce side effects
- Return a result before all preceding invariants are evaluated

---

## 6. Interface Boundary Rules

These properties are architectural — they are not configuration options.

**The EBI is not advisory.** DENY is not a recommendation. Upstream systems may not implement an override path that converts DENY to conditional execution.

**The EBI is not a logging surface.** Evidence capture is the responsibility of the CVS witness layer, which operates alongside the gate. The EBI produces only the binary enforcement decision.

**The EBI is not repositionable.** A gate placed after state change is not a Commit Gate. A gate placed in a code path that can be bypassed is not a Commit Gate. The EBI exists at the commit boundary or it does not exist.

**Middleware may not intercept.** No proxy, wrapper, or middleware layer may sit between the EBI output and the caller's execution path and convert DENY to ALLOW.

---

## 7. Relationship to CVS

CVS (Cryptographic Verification Sidecar) is not part of the EBI. It is a witness layer that observes EBI events and produces independently verifiable evidence of each evaluation.
[ Caller ]  →  [ EBI / Commit Gate ]  →  [ State Change ]
↓
[ CVS Witness Layer ]
↓
[ Evidence Object ]

The EBI operates regardless of whether CVS is present. The gate enforces. The witness records. These are separable concerns. A gate operating without a witness layer produces no auditable record — enforcement continues, but proof does not.

---

## 8. Failure Modes

| Condition | EBI Behavior |
|---|---|
| Malformed JSON | `DENY invalid_request` |
| Missing required field | `DENY invalid_request` |
| Invariant fails | `DENY <invariant_id>` |
| Evaluation exception | `DENY evaluation_error` |
| Gate unreachable | Caller MUST NOT proceed — deployment obligation, not EBI obligation |

The gate does not produce silence. Every call to the EBI resolves to a token. If the gate infrastructure is unreachable, the obligation to not proceed rests with the caller's integration layer. This is specified in deployment configuration, not in the EBI contract.

---

## 9. What the EBI Is Not

| Common Misconception | Correction |
|---|---|
| A policy engine | Policy engines interpret. The EBI enforces pre-committed constraints without interpretation. |
| An audit log | The EBI produces a binary decision. CVS produces the audit record. |
| A rate limiter | Rate limiting is a constraint that may be encoded upstream. The EBI evaluates constraints already set. |
| An advisory layer | There is no "soft deny." DENY is a terminal output. |
| Configurable at runtime | The specification surface is immutable at runtime. The interface is frozen. |

---

## Document Control

| Field | Value |
|---|---|
| Document | `512_EBI_DESIGN_v1_0.md` |
| Version | 1.0 |
| Date | May 2026 |
| Author | Jonathan M. Watson |
| Status | Draft — for review |

### Changelog — v1.0

**Additions:** Initial document. Boundary position, interface contract, invariant mapping, caller/gate obligations, boundary rules, CVS relationship, failure modes, disambiguation table.

**Removals:** Nothing removed.
