# Invariant Diagrams

## K1–K7 Canonical Invariants — Evaluation Order

```mermaid
flowchart TD
    A[Proposal Received] --> B{K1 — No force or fraud}
    B -->|FAIL| R1[DENY inv_1]
    B -->|PASS| C{K2 — Voluntary explicit consent}
    C -->|FAIL| R2[DENY inv_2]
    C -->|PASS| D{K3 — Consent withdrawal / exit rights}
    D -->|FAIL| R3[DENY inv_3]
    D -->|PASS| E{K4 — Explicit enforceable contracts}
    E -->|FAIL| R4[DENY inv_4]
    E -->|PASS| F{K5 — No hidden or unilateral rules}
    F -->|FAIL| R5[DENY inv_5]
    F -->|PASS| G{K6 — Fail open / disclose rules}
    G -->|FAIL| R6[DENY inv_6]
    G -->|PASS| H{K7 — Immutable spec / binary adherence}
    H -->|FAIL| R7[DENY inv_7]
    H -->|PASS| ALLOW[ALLOW]
```

---

## Runtime Proxy Mapping — inv_1 through inv_7

```mermaid
flowchart LR
    subgraph Runtime ["Runtime Proxy Conditions"]
        I1[inv_1: context.identity not null]
        I2[inv_2: context.consent == true]
        I3[inv_3: intent.action not null]
        I4[inv_4: amount ≤ max_amount]
        I5[inv_5: context.timestamp not null]
        I6[inv_6: intent.target not null]
        I7[inv_7: system_state == healthy]
    end

    subgraph Canonical ["Canonical Invariants"]
        K1[K1 — No force or fraud]
        K2[K2 — Voluntary explicit consent]
        K3[K3 — Exit rights]
        K4[K4 — Enforceable contracts]
        K5[K5 — No hidden rules]
        K6[K6 — Fail open]
        K7[K7 — Immutable specification]
    end

    I1 -->|proxies| K1
    I2 -->|proxies| K2
    I3 -->|proxies| K3
    I4 -->|proxies| K4
    I5 -->|proxies| K5
    I6 -->|proxies| K6
    I7 -->|proxies| K7
```

---

## K6 and K7 — Gate-Behaviour Invariants

K6 and K7 are not per-request field checks. They constrain gate
implementation. The proxy conditions in the reference runtime are
placeholders only.

```mermaid
flowchart TD
    subgraph K6 ["K6 — Fail Open"]
        A[Gate cannot evaluate] --> B[Fail-open handler engages]
        B --> C[Commit path opens]
        B --> D[Gap record emitted to witness]
        C --> E[Execution continues]
    end

    subgraph K7 ["K7 — Immutable Specification"]
        F[Gate startup] --> G[Load specification]
        G --> H{SHA-256 matches canonical hash?}
        H -->|NO| I[Gate refuses to start]
        H -->|YES| J[Specification locked in memory]
        J --> K[No runtime modification permitted]
    end
```

---

## Proxy Completeness — What Each Proxy Enforces vs What Full Enforcement Requires

```mermaid
flowchart LR
    subgraph inv2 ["inv_2 — consent proxy"]
        A[context.consent == true] -->|checks| B[boolean field present]
        C[Full K2 enforcement] -->|requires| D[cryptographic consent token]
        C -->|requires| E[consent type == explicit]
        C -->|requires| F[expiry not exceeded at evaluation time]
    end

    subgraph inv3 ["inv_3 — exit rights proxy"]
        G[intent.action not null] -->|checks| H[declared action present]
        I[Full K3 enforcement] -->|requires| J[token epoch matches registry epoch]
        I -->|requires| K[withdrawal propagated]
    end

    subgraph inv5 ["inv_5 — no hidden rules proxy"]
        L[context.timestamp not null] -->|checks| M[timestamp present]
        N[Full K5 enforcement] -->|requires| O[active spec hash == disclosed hash]
        N -->|requires| P[disclosure acknowledged by all parties]
    end
```

---

## Canonical Kernel Commitment

```mermaid
flowchart TD
    A[512-kernel-padded.txt] --> B[SHA-256]
    B --> C[7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5]
    C --> D{Gate startup hash check}
    D -->|MATCH| E[Gate starts — specification locked]
    D -->|MISMATCH| F[Gate refuses to start — critical alert logged]
```
