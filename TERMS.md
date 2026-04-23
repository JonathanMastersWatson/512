# TERMS AND DEFINITIONS

## Purpose

This document defines terms **as they are used in this repository**.

Definitions are:
- operational
- context-specific
- non-normative

No external definitions are implied.

---

## Core Terms

### 512
A **minimal execution-time constraint layer** that governs how legitimacy may be witnessed.

512 is:
- non-ownable
- voluntary
- enforcement-free
- ideology-free

512 is not a system, protocol, or authority.

---

### Commit Boundary
The exact point at which a proposed action becomes an irreversible state change.

Before the commit boundary: the action is a proposal. It can be modified,
withdrawn, or cancelled.

After the commit boundary: the action is a fact. State has changed.
Reversal requires a new action with its own boundary crossing.

The commit boundary is not the moment a request arrives. It is the moment
state becomes irreversible.

---

### Exclusive Commit Authority
The property of a correctly positioned gate whereby there exists exactly one
path to irreversible state change, and that path does not open without the
gate's authorisation signal.

A system that allows execution to proceed to the commit boundary without
passing through gate evaluation does not exhibit exclusive commit authority.

---

### Non-Bypassable Commit Path
The structural requirement that no route to the execution surface exists
outside gate evaluation.

Procedural controls — access policies, documented prohibitions, contractual
restrictions — do not satisfy this requirement. The path must not exist,
not merely be restricted.

---

### Proposal Object
A structured record of a proposed action, constructed before the commit
boundary is crossed and submitted to the gate for evaluation.

The Proposal Object is the gate's only input from the proposing entity.
It is constructed before evaluation begins and is not reconstructed after
the fact.

Required fields: `proposal_id`, `agent_id`, `action_type`, `action_params`,
`declared_scope`, `consent_evidence`, `contract_reference`, `exit_available`,
`rules_disclosed`, `spec_hash`, `authorisation_token`, `intent_hash`,
`timestamp`.

---

### Compiled Constraint Set
The machine-evaluable form of the constraint definitions for a given deployment,
produced by translating policy into deterministic Boolean expressions over
named, typed inputs.

The compiled constraint set is hashed to produce the spec hash. It is loaded
at gate startup, hash-verified against the canonical commitment, and thereafter
immutable for the process lifetime.

---

### Spec Hash
The SHA-256 hash of the compiled constraint set active at the moment of
evaluation.

The spec hash is embedded in every Evidence Object produced by the witness
layer. It binds each evidence record to the exact constraint specification
that was in force — enabling independent verification that the declared rules
were the rules evaluated against.

The canonical kernel commitment:
`7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

---

### Gate Output
The result produced by the gate upon completing evaluation of a Proposal Object.

The gate produces exactly two output values:

- **ALLOW** — all seven invariants are satisfied; the commit path opens
- **DENY** — one or more invariants are not satisfied; the commit path remains closed

There is no third output value. When the gate cannot complete evaluation,
it produces no output. Execution proceeds under the fail-open posture
required by Invariant 6. The witness layer records the resulting ungoverned
period as an evidence chain gap.

---

### Evidence Chain Gap
A witness layer classification applied to an ungoverned period in the evidence
chain — a period during which execution proceeded without gate evaluation.

An evidence chain gap is produced by the witness layer, not the gate. It is
not a gate output. It records that evaluation did not occur, not that
evaluation produced a particular result.

---

### Witness Layer
An independent evidence-capture system that observes execution events
out-of-band, records cryptographic evidence, and produces independently
verifiable records of what occurred.

The witness layer does not influence execution. It does not enforce
constraints. It does not produce gate outputs. It records what the gate
decided and what execution produced.

CVS (Cryptographic Verification Sidecar) is the reference witness layer
architecture for 512.

---

### Constraint
A limitation imposed by **physics, irreversibility, or system scale**, not by policy or preference.

Constraints are descriptive, not prescriptive.

---

### Legitimacy
The ability to **verify that an execution occurred as claimed**, without asserting correctness, truth, or value.

Legitimacy does not imply approval.

---

### Execution
A real-time action performed by a system that produces an effect.

Execution is local, autonomous, and irreversible once completed.

---

### Settlement
The irreversible recording of a completed execution or commitment.

Settlement does not control execution.

---

### Witnessing
The act of recording evidence that an execution occurred, without influencing the execution itself.

Witnessing is passive.

---

### Fail-Open
The behaviour required by Invariant 6 when a system cannot complete
evaluation at the commit boundary.

On fail-open:
- the gate produces no output
- execution proceeds — blocking execution on gate failure would itself
  violate Invariant 6
- governing rules are disclosed
- control returns to the human party
- the witness layer records the ungoverned period as an evidence chain gap

Fail-open is not a gate output. It is a system behaviour. The resulting
ungoverned period is classified by the witness layer as an evidence chain gap.

---

### Governance
Any mechanism that:
- enforces behavior
- applies rules
- imposes penalties
- requires compliance

Governance is explicitly out of scope for 512.

---

### Identity
Any construct that binds actions to a person, entity, or reputation.

512 does not require or process identity.

---

### Ideology
A system of beliefs, values, or normative claims.

512 contains none.

---

## Definition Rule

If a term is not defined in this document, its meaning is:
- implementation-specific
- external to 512
- not canonical

---

## Status

This document defines the **canonical vocabulary** for the 512 research archive.
