# Topology Diagrams

## Conformant Commit Gate Position

```mermaid
flowchart TD
    A[Upstream Caller] --> B[Authorisation Layer]
    B --> C[512 Commit Gate]
    C -->|ALLOW| D[Irreversible State Change]
    C -->|DENY inv_N| E[Commit Path Closed]
    C -. witness event async .-> F[CVS Witness Layer]
    F --> G[Evidence Object]
    G --> H[Merkle Batch]
    H --> I[Settlement Anchor / XRPL]
```

---

## Non-Conformant Pattern A — API Handoff

```mermaid
flowchart TD
    A[Upstream Caller] --> B[512 Evaluation]
    B -->|Result| C[API Layer]
    C --> D[DB Write]
    E[Direct DB Write] --> D

    X[NON-CONFORMANT: DB write reachable without evaluation] -.-> D
```

---

## Non-Conformant Pattern B — Queue Handoff

```mermaid
flowchart TD
    A[Upstream Caller] --> B[512 Evaluation]
    B -->|Result| C[Message Queue]
    C --> D[Worker Executes]
    E[Other Queue Sources] --> C

    X[NON-CONFORMANT: Worker can consume from sources other than evaluation path] -.-> D
```

---

## Non-Conformant Pattern C — Broker Handoff

```mermaid
flowchart TD
    A[Upstream Caller] --> B[512 Evaluation]
    B -->|Result| C[Broker]
    C -->|Decision applied| D[Runtime]
    D --> E[State Change]

    X[NON-CONFORMANT: Broker reintroduces interpretation layer] -.-> C
```

---

## Non-Conformant Pattern D — Pre-Check Positioning

```mermaid
flowchart TD
    A[Upstream Caller] --> B[512 Evaluation Check]
    B --> C[Execution Layer]
    C --> D[State Change]
    A -->|Direct path| C

    X[NON-CONFORMANT: Execution layer operable without evaluation result] -.-> C
```

---

## Non-Conformant Pattern E — Parallel Execution Path

```mermaid
flowchart TD
    A[Upstream Caller] --> B[512 Evaluation]
    B --> C[Primary Execution Path]
    C --> D[State Change]
    A --> E[Admin / Override / Fallback Path]
    E --> D

    X[NON-CONFORMANT: Any path reaching state change without evaluation] -.-> E
```

---

## Conformant Model — Structural Summary

```mermaid
flowchart TD
    A[Upstream Systems] --> B[Evaluation at Commit Boundary]
    B --> C[Irreversible State Change]

    note1[No alternate path exists] -.-> B
    note2[No reinterpretation between evaluation and commit] -.-> B
    note3[No execution outside this path under any operational mode] -.-> B
```
