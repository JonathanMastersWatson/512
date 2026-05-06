# Architectural Layer Diagrams

## The 512 / CVS Layer Stack

```mermaid
flowchart TD
    A[Constraint Architecture] -->|defines what is admissible| B
    B[Physics — Commit Boundary] -->|forces gate into existence| C
    C[512 — Commit Gate] -->|enforces pre-committed constraints| D
    D[CVS — Cryptographic Verification Sidecar] -->|makes enforcement provable| E
    E[Derivatives — Managed Services / SLA Products / Domain Deployments]

    style A fill:#f5f5f5
    style B fill:#f5f5f5
    style C fill:#d4e8ff
    style D fill:#d4f7d4
    style E fill:#fff8d4
```

---

## Layer Responsibilities

```mermaid
flowchart LR
    subgraph CA ["Constraint Architecture"]
        A1[Consent logic]
        A2[Authority models]
        A3[Thresholds]
        A4[Domain constraints]
        A5[Admissibility rules]
    end

    subgraph Gate ["512 Commit Gate"]
        B1[Evaluates constraints]
        B2[Produces ALLOW or DENY]
        B3[Enforces at commit boundary]
        B4[Operates at sub-50μs]
        B5[Immutable specification]
    end

    subgraph Witness ["CVS Witness Layer"]
        C1[Observes gate decisions]
        C2[Constructs Evidence Objects]
        C3[Hash chains events]
        C4[Anchors to settlement ledger]
        C5[Enables independent verification]
    end

    CA -->|upstream definition| Gate
    Gate -->|boundary events| Witness
```

---

## What Each Layer Does Not Do

```mermaid
flowchart TD
    subgraph NotCA ["Constraint Architecture does NOT"]
        A1[Enforce constraints]
        A2[Produce evidence]
        A3[Operate at machine speed]
    end

    subgraph Not512 ["512 Commit Gate does NOT"]
        B1[Define constraints]
        B2[Capture evidence]
        B3[Interpret rules]
        B4[Store logs]
    end

    subgraph NotCVS ["CVS does NOT"]
        C1[Enforce constraints]
        C2[Block execution]
        C3[Define admissibility]
        C4[Store payload content]
        C5[Interpret evidence meaning]
    end
```

---

## Layer Independence

```mermaid
flowchart TD
    A[512 Commit Gate] -->|operates without| B[CVS]
    B -->|operates without| A

    A -->|enforcement continues| C[No witness = unverifiable]
    B -->|witnessing continues| D[No gate = ungoverned execution]

    E[Both required for: enforcement AND auditability] -.-> A
    E -.-> B
```

---

## Open Commons Model

```mermaid
flowchart TD
    subgraph T1 ["Tier 1 — Discovered Constraint"]
        A[512 / Commit Gate category]
        A1[Not ownable]
        A2[Not commercialisable at base]
    end

    subgraph T2 ["Tier 2 — Invented Witness Layer"]
        B[CVS base architecture]
        B1[Not ownable at base]
        B2[Apache 2.0 / open commons]
    end

    subgraph T3 ["Tier 3 — Derivatives"]
        C[Implementations / SLA products / managed services / domain deployments]
        C1[Fully ownable]
        C2[Freely commercialisable]
    end

    T1 --> T2 --> T3
```

---

## Deployment Sequence — Constraint to Evidence

```mermaid
flowchart LR
    A[Policy] -->|translated by| B[Constraint Architecture]
    B -->|binary-reducible constraints| C[512 Commit Gate]
    C -->|ALLOW or DENY at commit boundary| D[Execution Surface]
    C -. boundary event async .-> E[CVS Capture Plane]
    E -->|Evidence Object| F[CVS Access Plane]
    F -->|read-only APIs| G[CVS Interpretation Plane]
    G -->|findings| H[Regulator / Insurer / Auditor]
```
