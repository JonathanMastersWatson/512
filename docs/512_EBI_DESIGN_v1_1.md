# 512 Execution Boundary Interface — Design Specification

**Jonathan M. Watson | 512 / CVS Architecture**
**Version 1.1 | May 2026**
**Canonical Repository:** github.com/JonathanMastersWatson/512
**Normative Authority:** `512_ARCHITECTURE_v3.4.md` · `512_IMPLEMENTATION_v3.3.md`

---

## Abstract

The **Execution Boundary Interface** (EBI) is the formal seam between an upstream caller and the 512 Commit Gate. It defines what crosses the commit boundary, in which direction, in what shape, and under what contract. It does not define what constraints are enforced — that is the Constraint Architecture layer's responsibility. It does not define how evidence is captured — that is CVS's responsibility. It defines the interface: the position, the contract, and the obligations of each party at the crossing point.

This document is authoritative for developers integrating against the 512 runtime. It is a companion to `512_ARCHITECTURE_v3.4.md §3–4` and `512_IMPLEMENTATION_v3.3.md §1–4`. Rationale for why each property exists is not repeated here — engineers who need it read the architecture document first.

---

## 1. Boundary Position

The EBI is position-locked. It sits between authorisation and irreversible state change — at the commit boundary.
[ Upstream Caller ]
|
| (carries verified authorisation credential)
v
[ Authorisation Layer ]
|
| (authorisation confirmed — request passed to gate)
v
[ EBI / Commit Gate ]   ◄── The interface defined in this document
|
| ALLOW → commit path opens
| DENY  → commit path stays closed
v
[ Irreversible State Change ]
|
v
[ CVS Witness Layer ]   ◄── Records what the gate did (separate concern)

There is one path to irreversible state change. It passes through the gate. There is no parallel path, no override path, no administrative shortcut. The existence of any path that reaches the execution surface without gate evaluation — regardless of how rarely it is used — is a non-conformance condition, not a deployment risk. See §9 for non-conformant patterns.

---

## 2. Authorisation Precedes the Gate

The gate evaluates constraints. It does not perform authorisation.

**Authorisation** — verifying who is making a request and whether they are permitted to make it — is the responsibility of the layer upstream of the gate. By the time a request arrives at the EBI, authorisation has already been established. The request carries a cryptographic proof of that authorisation: a token, certificate, or signed attestation.

If authorisation fails, the request is rejected before it reaches the gate. It never crosses the EBI.

If authorisation succeeds but constraints are violated, the gate denies and records. These are different failures with different semantics.

**Developer consequence:** Do not expect the gate to perform identity verification. `context.identity` in the reference runtime is a field the gate receives — it does not validate that the identity is who they claim to be. That validation happened upstream, before the request was constructed.

---

## 3. Interface Contract

### 3.1 Request Shape

```json
{
  "intent": {
    "action":  "<string — required>",
    "target":  "<string — required>",
    "amount":  "<number — required if constrained>"
  },
  "constraints": {
    "max_amount": "<number — required if amount is declared>"
  },
  "context": {
    "identity":     "<string — required>",
    "consent":      "<boolean: true — required>",
    "timestamp":    "<ISO 8601 — required>",
    "system_state": "<string: 'healthy' — required>"
  }
}
```

The three top-level fields — `intent`, `constraints`, `context` — are always present. Missing or null required fields produce `DENY invalid_request` before invariant evaluation begins.

### 3.2 Required Fields

| Field | Type | Failure if absent or null |
|---|---|---|
| `intent.action` | string | `DENY invalid_request` |
| `intent.target` | string | `DENY invalid_request` |
| `context.identity` | string | `DENY invalid_request` |
| `context.consent` | boolean | `DENY invalid_request` |
| `context.timestamp` | string (ISO 8601) | `DENY invalid_request` |
| `context.system_state` | string | `DENY invalid_request` |
| `constraints.max_amount` | number | `DENY invalid_request` |

No defaults. No inference. No mutation. The gate evaluates the request as received.

### 3.3 Output Tokens

The gate produces exactly one output token per request:
ALLOW
DENY inv_<N>
DENY invalid_request
DENY evaluation_error

**ALLOW** — all seven invariants evaluated TRUE. The commit path opens.

**DENY inv_\<N\>** — invariant N evaluated FALSE. First failure in evaluation order terminates evaluation. The commit path remains closed. `N` is an integer 1–7 corresponding to the canonical invariant set.

**DENY invalid_request** — the request was malformed before evaluation began. A required field is absent, null, or of wrong type. No invariants were evaluated.

**DENY evaluation_error** — the gate encountered an unexpected internal error during evaluation. This token is a runtime implementation detail. From the caller's perspective, it is a DENY — the commit path remains closed. In production implementations, an `evaluation_error` condition SHOULD trigger the fail-open handler (see §8) rather than producing a denial, because the gate failed to evaluate — it did not evaluate and find a violation. The reference runtime denies on error as a fail-safe; production deployments implement the distinction.

**Caller rule:** All DENY tokens are terminal. The reason code (`inv_2`, `invalid_request`, `evaluation_error`) is diagnostic information for the operator. It does not change the caller's obligation: no state change follows any DENY under any condition.

---

## 4. The Invariant Mapping

### 4.1 What This Section Is

The reference runtime (`evaluator.py`) implements seven proxy conditions — one per canonical invariant. Each proxy is a payment-domain approximation of the full invariant, designed to demonstrate the evaluation pattern with minimal infrastructure. A proxy checks a necessary condition for the invariant; it does not enforce the complete invariant.

This section maps each runtime proxy (`inv_1` through `inv_7`) to the canonical invariant it approximates (`K1` through `K7`), states what the proxy checks, and states what a full implementation requires. The canonical invariants are defined authoritatively in `512_ARCHITECTURE_v3.4.md §4` and implemented in `512_IMPLEMENTATION_v3.3.md §3`.

**Do not mistake the proxy for the invariant.** A production gate for Invariant 2 (consent) does not check a boolean field. It validates a cryptographic consent token, a consent type of `explicit` (not `implied`), and an expiry timestamp. The runtime's `context.consent == true` is a placeholder that demonstrates the evaluation slot, not the enforcement.

### 4.2 Mapping Table

| Runtime ID | Runtime check | Canonical invariant | What the proxy checks | What full enforcement requires |
|---|---|---|---|---|
| `inv_1` | `context.identity is not None` | **K1 — No force or fraud against any human** | Identity presence — a necessary condition for attributing coercive action | Action classification (coercive/deceptive flag), transfer amount vs. authorised limit, affected party type. See `512_IMPLEMENTATION v3.3 §3.1` |
| `inv_2` | `context.consent is True` | **K2 — Voluntary and explicit consent** | Consent boolean — stands for documented explicit prior consent | Consent token (cryptographic), consent type must be `explicit` (not `implied`), consent expiry not exceeded at evaluation time. See `512_IMPLEMENTATION v3.3 §3.2` |
| `inv_3` | `intent.action is not None` | **K3 — Consent may be withdrawn; exit must always be possible** | Declared action presence — a precondition for any evaluation | Epoch check: token epoch must match current consent registry epoch. A stale epoch indicates withdrawal since token issuance. Withdrawal must have propagated. See `512_IMPLEMENTATION v3.3 §3.3` |
| `inv_4` | `intent.amount <= constraints.max_amount` | **K4 — Contracts must be explicit, readable, and equally enforceable** | Amount within declared limit — enforces one boundary of a declared term | Contract machine-readable AND human-readable, both parties acknowledged, no enforcement asymmetry. See `512_IMPLEMENTATION v3.3 §3.4` |
| `inv_5` | `context.timestamp is not None` | **K5 — No rules may be hidden or unilaterally changed** | Timestamp presence — enables sequencing of the evidence record | Active spec hash equals disclosed spec hash equals canonical hash (`7B08C024...`), disclosure acknowledged by all parties. See `512_IMPLEMENTATION v3.3 §3.5` |
| `inv_6` | `intent.target is not None` | **K6 — On failure, systems must fail open and disclose governing rules** | Known target — a precondition for attributing affected party | K6 is a gate-behaviour invariant, not a per-request field check. It governs what the gate does when it *cannot* evaluate — not what it evaluates. The runtime proxy here is a weak stand-in. Full implementation is the fail-open handler. See `512_IMPLEMENTATION v3.3 §3.6` and §8 of this document |
| `inv_7` | `context.system_state == "healthy"` | **K7 — The specification is immutable; adherence is binary** | System health as an execution precondition | K7 is a startup and specification invariant, not a per-request field check. Full implementation is the hash verification sequence at gate startup: `sha256(spec) must equal 7B08C024...`. A gate that starts with hash mismatch refuses to start. See `512_IMPLEMENTATION v3.3 §3.7` |

### 4.3 Notes on K6 and K7

K6 and K7 are structurally different from K1–K5. K1–K5 each enforce a property of the *proposal*: what is being requested, by whom, with what consent, under what terms. K6 and K7 enforce properties of the *gate itself*: how it behaves under failure, and whether its specification is what it claims to be.

The runtime maps these to per-request field checks (`target is not None`, `system_state == "healthy"`) as a pragmatic demonstration. In production:

- K6 is implemented entirely in the gate's failure handling path — the fail-open handler. There is no K6 field in the Proposal Object. See §8.
- K7 is implemented entirely at gate startup — the hash verification sequence. There is no K7 field in the Proposal Object. What `context.system_state == "healthy"` approximates is a runtime readiness check — not specification immutability enforcement.

This distinction matters for developers defining their Proposal Object schema. K6 and K7 do not contribute fields to the EBI request. They constrain gate implementation, not request construction.

### 4.4 Canonical Invariant Reference

| Canonical ID | Statement | Architecture ref | Implementation ref |
|---|---|---|---|
| K1 | No agent may initiate force or fraud against any human | `512_ARCHITECTURE v3.4 §4.1` | `512_IMPLEMENTATION v3.3 §3.1` |
| K2 | All interactions must be voluntary and based on explicit consent | `512_ARCHITECTURE v3.4 §4.2` | `512_IMPLEMENTATION v3.3 §3.2` |
| K3 | Consent may be withdrawn — exit must always be possible | `512_ARCHITECTURE v3.4 §4.3` | `512_IMPLEMENTATION v3.3 §3.3` |
| K4 | All contracts must be explicit, readable, and equally enforceable | `512_ARCHITECTURE v3.4 §4.4` | `512_IMPLEMENTATION v3.3 §3.4` |
| K5 | No rules governing interaction may be hidden or unilaterally changed | `512_ARCHITECTURE v3.4 §4.5` | `512_IMPLEMENTATION v3.3 §3.5` |
| K6 | On failure, systems must fail open, reveal governing rules, and default to human choice | `512_ARCHITECTURE v3.4 §4.6` | `512_IMPLEMENTATION v3.3 §3.6` |
| K7 | The specification is immutable — adherence is binary | `512_ARCHITECTURE v3.4 §4.7` | `512_IMPLEMENTATION v3.3 §3.7` |

---

## 5. Caller Obligations

The caller is any upstream system that presents a request to the EBI.

**MUST:**
- Establish authorisation before constructing the request — the gate does not perform authorisation
- Construct a complete, well-formed request; validate all required fields before calling
- Block execution until a response is received from the gate
- Treat all DENY tokens as terminal — no state change follows any DENY under any condition
- Treat `evaluation_error` as DENY — not as a signal to retry without correction

**MUST NOT:**
- Cache an ALLOW response and replay it for a subsequent action — each proposal is evaluated independently
- Retry a DENY without correcting the underlying condition that caused it
- Execute the intended action before receiving ALLOW
- Route around the gate under degraded conditions — the fail-open handler is the gate's responsibility, not the caller's
- Interpret the DENY reason code as a negotiation surface — DENY is not a score

---

## 6. Gate Obligations

The gate is the 512 Commit Gate receiving the request at the EBI.

**MUST:**
- Verify the specification hash at startup; refuse to start on hash mismatch
- Validate all required fields before beginning invariant evaluation
- Evaluate all seven invariants in declared order (K1 through K7)
- Return exactly one output token per request
- Complete evaluation within the latency budget: sub-50μs in software, sub-5μs in FPGA
- Be stateless — each request evaluated independently with no carry-forward state
- Disclose the failed invariant ID on any DENY — `DENY inv_<N>` not `DENY constraint_failed`
- Forward a gap record to the witness layer on any fail-open event

**MUST NOT:**
- Modify the request before or during evaluation
- Fetch external data during evaluation — all inputs must be fully bound in the incoming request
- Produce probabilistic output — no scores, weights, or confidence values
- Operate in advisory mode — evaluation results are decisions, not recommendations
- Accept runtime modification of the invariant set or constraint specification
- Return a result before all invariants at or before the first failure are evaluated

---

## 7. Evaluation Sequence

Invariants are evaluated in order. The first FALSE result terminates evaluation and produces `DENY inv_<N>`. Subsequent invariants are not evaluated.
Request received
│
▼
Required fields present? ──No──► DENY invalid_request
│
Yes
│
▼
inv_1: identity present? ─────No──► DENY inv_1
│
Yes
▼
inv_2: consent true? ──────────No──► DENY inv_2
│
Yes
▼
inv_3: action defined? ────────No──► DENY inv_3
│
Yes
▼
inv_4: amount ≤ max_amount? ───No──► DENY inv_4
│
Yes
▼
inv_5: timestamp present? ─────No──► DENY inv_5
│
Yes
▼
inv_6: target defined? ────────No──► DENY inv_6
│
Yes
▼
inv_7: system healthy? ────────No──► DENY inv_7
│
Yes
▼
ALLOW

**Early exit is by design.** The first invariant to fail terminates evaluation. This means `DENY inv_2` tells you inv_2 failed — it does not tell you the state of inv_3 through inv_7. Fix the failing invariant, resubmit, and the next evaluation may reveal a different failure.

---

## 8. Fail-Open Mechanics

### 8.1 The Gate Does Not Block on Failure

When the gate is unavailable or encounters an internal error that prevents evaluation, it does not produce DENY. A gate that blocks execution by failing closed creates a denial-of-service surface and concentrates authority at whoever controls the gate. This violates K6.

When the gate cannot evaluate:
1. The fail-open handler engages
2. Execution continues — the commit path opens
3. A gap record is generated and forwarded to the witness layer
4. The gap record documents: proposal ID, agent ID, gap start time, and reason

### 8.2 Gap Is a Witness Layer Concept

GAP is not a gate output token. The gate produces ALLOW or DENY — two values, no third. The gap concept belongs to the witness layer, which records the ungoverned execution period as an evidence chain gap. The gap record is how the absence of gate evaluation becomes independently verifiable.

**Developer consequence:** Do not implement a three-state output handler (ALLOW / DENY / GAP) at the caller. The gate returns two states. The witness layer handles gap records. These are separate layers with separate responsibilities.

### 8.3 Reference Runtime Behaviour

The reference runtime (`run_512`) denies on evaluation exception rather than engaging a fail-open handler. This is a fail-safe behaviour appropriate for a reference implementation. Production deployments MUST implement the fail-open handler as specified in `512_IMPLEMENTATION v3.3 §3.6`. An unhandled exception that produces DENY in a production gate is a K6 violation — the gate failed closed.

---

## 9. Non-Conformant Integration Patterns

The following patterns are documented in `512_IMPLEMENTATION v3.3 §1.6` as structural non-conformances. Each creates a path to irreversible state change that does not pass through gate evaluation.

| Pattern | Structure | Why it fails |
|---|---|---|
| **A — API handoff** | `[evaluation] → [API call] → [DB write]` | DB write is reachable independently of evaluation. The evaluation result is advisory to the API layer. |
| **B — Queue handoff** | `[evaluation] → [message queue] → [worker]` | Worker can consume from sources other than the evaluation path. The queue is an independently operable execution surface. |
| **C — Broker handoff** | `[evaluation] → [broker] → [runtime]` | The broker reintroduces an interpretation layer. The runtime may apply the decision differently from the evaluation output. |
| **D — Pre-check positioning** | `[evaluation check] → [execution layer]` | Decision and execution are structurally separate. The execution layer is operable without the evaluation result. This is the most common misinterpretation of 512's boundary model. |
| **E — Parallel path** | Gate path + any alternative path (admin, emergency, override) | Any path that reaches the execution surface without evaluation is a bypass. The existence of the path — not its frequency of use — is the disqualifying condition. |

**The only conformant model:**
[upstream systems]
|
v
[evaluation at commit boundary]
|
v
[irreversible state change]
Properties:

no alternate path exists
no reinterpretation occurs between evaluation and commit
no execution proceeds outside this path under any operational mode


---

## 10. Common Developer Errors

| Error | What the developer did | Why it fails | Correct behaviour |
|---|---|---|---|
| Treating DENY as advisory | Logging DENY and proceeding with execution | DENY is terminal — the commit path does not open | Stop. No state change. No retry without correction. |
| Caching ALLOW | Reusing a previous ALLOW for a new proposal | Each proposal is evaluated independently. A prior ALLOW is not a standing permission. | Evaluate every proposal. |
| Building a bypass for errors | Executing when the gate is unreachable, to preserve availability | Creates a path to state change that doesn't pass through the gate. Converts enforcement to monitoring. | Let the gate's fail-open handler engage. The gap is recorded. Do not implement your own fallback execution path. |
| Treating `evaluation_error` as retry | Retrying the identical request after `evaluation_error` | An evaluation error is not a transient state — it indicates the gate failed internally. Retrying the same request does not resolve the underlying condition. | Treat as DENY. Escalate to operator. |
| Reading `inv_N` as the full invariant | Building consent logic because DENY inv_2 means "add a consent field" | The runtime proxy for K2 is `context.consent == true`. The full K2 requires a cryptographic consent token, explicit type, and expiry check. The proxy is a placeholder. | Build against the full invariant specification in `512_IMPLEMENTATION v3.3 §3.2`. |
| Implementing K6/K7 as request fields | Adding `governing_rules_disclosed` or `spec_hash_verified` to the Proposal Object | K6 and K7 are gate-behaviour invariants, not request fields. They constrain the gate's implementation, not the caller's request. | K6: implement the fail-open handler. K7: implement spec hash verification at gate startup. Neither contributes a field to the EBI request. |
| Positioning the gate upstream | Running gate evaluation before calling the execution service, with the execution service callable directly | This is Pattern D — pre-check positioning. The gate's signal must be the direct structural prerequisite for the commit path opening. | Position the gate at the commit boundary, not upstream of it. |

---

## 11. Integration Checklist

### Pre-Integration

- [ ] Read `512_ARCHITECTURE_v3.4.md §3–4` — understand what each invariant enforces before building
- [ ] Read `512_IMPLEMENTATION_v3.3.md §1` — confirm boundary position, bypass audit, and commit path ownership requirements
- [ ] Complete upstream preparation per `512-ops/INTEGRATION_STEPS.md` — boundary identification, parallel path audit, Proposal Object definition, and constraint definition must be complete before gate evaluation begins
- [ ] Define domain-specific constraints per `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — the gate evaluates constraints; it does not define them
- [ ] Verify no bypass paths exist to the execution surface — structural audit, not procedural policy

### Per-Call

- [ ] Authorisation established and credential attached to request before calling the gate
- [ ] All required fields present and non-null in the request
- [ ] Caller blocks on gate response before any downstream action
- [ ] ALLOW received → proceed to state change
- [ ] Any DENY received → halt, log, no state change, no retry without correction

### Post-Denial

- [ ] Log the full request and the DENY token (including `inv_N` or `invalid_request` or `evaluation_error`)
- [ ] Do not convert DENY to a degraded execution path
- [ ] If DENY inv_N: identify which field or condition failed and correct it — do not infer correction from the proxy; read the full invariant in `512_IMPLEMENTATION v3.3 §3.N`
- [ ] If DENY invalid_request: validate required fields against §3.2 of this document
- [ ] If DENY evaluation_error: escalate to operator; treat as gate infrastructure issue

---

## 12. What the EBI Is Not

| What it might look like | What it is not |
|---|---|
| The gate evaluates action fields and consent | Not a policy engine — it does not define, interpret, or contextualise rules |
| The gate returns DENY with a reason code | Not an advisory layer — DENY is not a recommendation; the reason code is not an invitation to negotiate |
| The request contains identity and timestamp | Not an audit log — evidence capture is CVS's responsibility; the EBI produces a decision, not a record |
| The gate runs before execution | Not a pre-check — it is the gating condition on the commit path, not a check upstream of an independently operable execution surface |
| The gate can be configured | Not runtime-configurable — the specification is loaded at startup, hash-verified, and immutable for the process lifetime |

---

## 13. Normative References

| Document | Role relative to this document |
|---|---|
| `512_ARCHITECTURE_v3.4.md` | Authoritative source for the seven invariants, their rationale, and the Commit Gate category definition |
| `512_IMPLEMENTATION_v3.3.md` | Authoritative source for executable invariant implementations, constraint format, conformant/non-conformant patterns, and gate startup sequence |
| `512-ops/INTEGRATION_STEPS.md` | 7-step enterprise integration workflow — upstream preparation before gate evaluation begins |
| `512-ops/CONSTRAINT_DEFINITION_LAYER.md` | How to translate policies into binary-reducible executable constraints |
| `512-ops/REFERENCE_FLOW.md` | End-to-end sequence from intent declaration to anchored evidence |
| `INTERFACE_LOCK.md` | Frozen runtime interface contract — input shape, required fields, output format |
| `evaluator.py` | Reference invariant evaluation engine — seven proxy implementations |
| `CVS_ARCHITECTURE` | Witness layer architecture — Evidence Object schema, gap record handling, XRPL anchoring |

---

## Document Control

| Field | Value |
|---|---|
| Document | `512_EBI_DESIGN_v1_1.md` |
| Version | 1.1 |
| Date | May 2026 |
| Author | Jonathan M. Watson |
| Location | `JonathanMastersWatson/512/docs/` |

### Changelog — v1.1

**Additions:**
- §2: Authorisation Precedes the Gate — new section establishing that authorisation is an upstream concern; the gate evaluates constraints only; `context.identity` is received, not validated by the gate
- §4: The Invariant Mapping — central deliverable; maps runtime `inv_1–7` to canonical `K1–K7`; states what each proxy checks vs. what full enforcement requires; identifies K6 and K7 as gate-behaviour invariants that contribute no request fields
- §4.4: Canonical Invariant Reference table — cross-references architecture and implementation sections for each invariant
- §7: Evaluation Sequence — flow diagram showing early-exit evaluation order
- §8: Fail-Open Mechanics — clarifies that GAP is a witness-layer concept, not a gate output token; documents the three-step fail-open sequence; addresses `evaluation_error` as a production vs. reference runtime distinction
- §9: Non-Conformant Integration Patterns — incorporates the five non-conformant patterns from `512_IMPLEMENTATION v3.3 §1.6`
- §10: Common Developer Errors — seven-row error table covering the most common integration mistakes
- §11: Integration Checklist — pre-integration, per-call, and post-denial checklists
- §12: What the EBI Is Not — disambiguation table
- §13: Normative References — complete reference table

**Modifications:**
- §3.3: Output tokens — `DENY evaluation_error` added as documented fourth token; distinguished from invariant denial and explained as a production vs. reference runtime concern
- §5–6: Caller and Gate Obligations — expanded to reflect authorisation-first model, evaluation_error handling, and fail-open distinction
- §1: Boundary Position — diagram expanded to show authorisation layer and CVS witness layer

**Removals:** Nothing removed.

---

### Changelog — v1.0

**Additions:** Initial document. Boundary position, frozen interface contract, invariant mapping table (simplified), caller/gate obligations, CVS relationship, failure modes, disambiguation table.

**Removals:** Nothing removed.
