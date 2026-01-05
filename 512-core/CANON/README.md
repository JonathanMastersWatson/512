# 512 — Execution-Time Legitimacy Under Scale

512 documents a **discovered constraint** governing legitimacy at execution time in large-scale, distributed systems.

It is not a product, protocol, platform, governance framework, political ideology, or enforcement system.

512 defines a **minimal, immutable kernel** that allows actions, interactions, and automated systems to be evaluated for legitimacy **at the moment they execute**, without creating new authorities.

---

## What 512 Is

512 is a research archive that records:

- observed failures of legitimacy under scale
- constraints imposed by physics (latency, irreversibility, distribution)
- the identification of a minimal execution-time constraint (the 512 kernel)
- mechanisms for determining **semantic equivalence** without centralized interpretation

512 makes no prescriptions about outcomes.
It defines only whether execution aligns with declared constraints.

---

## The Kernel

The 512 kernel consists of a small set of invariants governing voluntary interaction, consent, exit, symmetry, transparency, and failure behavior.

- The kernel is **immutable**.
- Adherence is **binary**.
- The kernel does not evolve.
- No interpretation is authoritative.

Kernel text is human-readable.
Kernel meaning is invariant.

---

## Semantic Equivalence (Critical)

512 does **not** require word-for-word sameness.

It requires **semantic equivalence**.

Different phrasings, sequences, or languages may express the same kernel meaning.
Semantic mutation is not permitted.

To enable equivalence without authority, this repository defines:

- a **Canonical Intermediate Representation (IR)** of kernel invariants
- a **SPEC_HASH** computed from canonical IR, not prose
- a **multi-interpreter consensus model** that fails open on disagreement

These mechanisms allow equivalence to be evaluated mechanically rather than argued socially.

See:
- `512-core/CANON/KERNEL_EQUIVALENCE_AND_SPEC_HASH.md`
- `512-core/CANON/CANONICAL_IR.json`
- `512-core/CANON/SPEC_HASH.md`

---

## What This Repository Is Not

This repository does not:

- define enforcement mechanisms
- grant authority or certification
- provide governance, identity, incentives, or safety logic
- prescribe legal, political, or moral outcomes
- adjudicate disputes or intent

Those concerns are explicitly out of scope.

---

## Evidence Sidecars (Related, Separate)

512 is compatible with external evidence-capture systems (often referred to as sidecars or CVS architectures) that independently observe and record execution events.

These systems are not part of the kernel.
They are optional infrastructure that may use 512 constraints to evaluate execution consistency.

---

## Design Principles

- Meaning over wording
- Execution over explanation
- Verification over interpretation
- Constraint over control
- Fail open on ambiguity
- No hidden rules
- No silent authority

---

## Status

- Kernel: **Frozen**
- Equivalence mechanism: **Defined**
- Implementations: **Out of scope**
- Adoption: **Voluntary**

512 spreads by usefulness, not mandate.

---

## License / Use

This repository documents a constraint.
It may be referenced, implemented, or ignored.

No permission is required.
No endorsement is implied.

---

## For Engineers

512 treats natural language as an interface, not an authority.

Equivalence is determined mechanically, not socially.

### How equivalence works

1. Kernel prose (any wording / language) is parsed into a **Canonical Intermediate Representation (IR)**.
2. The IR is normalized into a fixed invariant set (`CANONICAL_IR.json`).
3. A deterministic hash is computed:

   **SPEC_HASH = HASH( JCS( CANONICAL_IR.json ) )**

4. If two kernel texts produce the same SPEC_HASH, they are semantically equivalent.
5. Any semantic mutation changes SPEC_HASH.

### Interpreter model

- Interpreters may be human or machine.
- No interpreter is authoritative.
- High-stakes use SHOULD require multiple independent interpreters.
- Disagreement MUST fail open and default to non-action / human choice.

### What this avoids

- word-for-word matching
- centralized interpretation
- silent drift through paraphrase
- “looks equivalent” attacks
- governance by explanation

### What this enables

- paraphrase tolerance
- language portability
- deterministic equivalence checks
- adversarial review
- execution-time legitimacy at scale

Implementations are intentionally out of scope.

---

**If this function cannot be implemented deterministically, the kernel is not portable.**

text
function compute_spec_hash(kernel_text):
    ir_list = parse_to_ir(kernel_text)          // extract invariants
    canonical_ir = normalize(ir_list)            // I1..I9, fixed semantics
    canonical_ir = sort_by_id(canonical_ir)      // deterministic ordering
    json = serialize_canonical(canonical_ir)     // stable keys, UTF-8
    json = json_canonicalize(json)               // RFC 8785 (JCS) or equivalent
    return hash(json)                             // e.g. SHA-256

function equivalent(kernel_a, kernel_b):
    return compute_spec_hash(kernel_a) ==
           compute_spec_hash(kernel_b)



