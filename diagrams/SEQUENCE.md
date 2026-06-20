# Sequence Diagrams

## The Four-Step Validation Sequence

```mermaid
sequenceDiagram
    participant P as Proposing Entity
    participant G as 512 Commit Gate
    participant R as Context Registries
    participant C as Commit Target

    P->>G: Step 1 — Intent Declaration
    Note over P,G: action type, parameters, scope

    G->>R: Step 2 — Context Binding
    R-->>G: timestamp, identity, environment, resource state

    G->>G: Step 3 — Constraint Evaluation
    Note over G: Seven invariants evaluated in order (K1–K7)
    Note over G: First failure → DENY. All pass → ALLOW.

    G->>C: Step 4 — Commit Authorisation Signal
    Note over G,C: ALLOW — commit path opens
    Note over G,C: DENY inv_N — commit path stays closed
```

---

## Early-Exit Evaluation Flow

```mermaid
sequenceDiagram
    participant G as 512 Commit Gate
    participant C as Commit Target

    G->>G: Validate required fields
    Note over G: Missing or null → DENY invalid_request

    G->>G: Evaluate K1 proxy (inv_1)
    Note over G: Fail → DENY inv_1

    G->>G: Evaluate K2 proxy (inv_2)
    Note over G: Fail → DENY inv_2

    G->>G: Evaluate K3 proxy (inv_3)
    Note over G: Fail → DENY inv_3

    G->>G: Evaluate K4 proxy (inv_4)
    Note over G: Fail → DENY inv_4

    G->>G: Evaluate K5 proxy (inv_5)
    Note over G: Fail → DENY inv_5

    G->>G: Evaluate K6 proxy (inv_6)
    Note over G: Fail → DENY inv_6

    G->>G: Evaluate K7 proxy (inv_7)
    Note over G: Fail → DENY inv_7

    G->>C: All pass → ALLOW
```

---

## Evaluation-Unavailable DENY — Gate Cannot Evaluate
```mermaid
sequenceDiagram
    participant P as Proposing Entity
    participant G as 512 Commit Gate
    participant F as Infrastructure-Failure Handler
    participant C as Commit Target
    participant W as CVS Sidecar
    P->>G: Submit proposal
    G->>G: Attempt constraint evaluation
    G--xG: Gate unavailable or evaluation timeout
    G->>F: Engage infrastructure-failure handler
    F->>P: DENY (evaluation_unavailable, retry_permitted: true)
    Note over F,C: Commit path remains closed — execution does not proceed
    F-->>W: Emit deny evidence object (async)
    F-->>W: Emit gap record (async)
    W->>W: Record evaluation-unavailable DENY evidence
    W->>W: Record gap record (gate_output_during_gap: deny_evaluation_unavailable)
    Note over W: Gap and DENY permanently observable in evidence chain
```

---

## Proposal to Evidence — Full Path

```mermaid
sequenceDiagram
    participant P as Proposing Entity
    participant G as 512 Commit Gate
    participant C as Commit Target
    participant W as CVS Witness
    participant M as Merkle Batcher
    participant A as Settlement Layer

    P->>G: Submit proposal
    G->>G: Evaluate K1–K7
    G->>C: ALLOW or DENY inv_N
    G-->>W: Emit witness event (async)
    W->>W: Construct Evidence Object
    W->>W: Calculate evidence_hash
    W->>W: Sign witness_attestation via HSM
    W->>M: Emit merkle_leaf_hash
    M->>M: Batch leaves — build Merkle root
    M->>A: Anchor Merkle root
    A-->>M: Anchor receipt + ledger timestamp
    Note over A: Timestamp set by ledger — not operator
    Note over W,A: Evidence anchored within 30–60 seconds
