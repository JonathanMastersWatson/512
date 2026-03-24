# Anti-Drift

This document defines what 512 is not, and how implementations drift
from its properties.

It exists because the most common failure mode is not outright rejection
of 512's properties — it is gradual reinterpretation that preserves
the name while abandoning the constraint.

---

## What 512 Is

512 is a **discovered constraint**. It was not invented.

Physics and scale force it into existence: when systems execute at
machine speed, when human reaction latency is fixed, when state changes
are irreversible, a minimal constraint layer at the execution boundary
is not optional. It emerges from necessity.

512 identifies what that constraint layer must satisfy. It does not
prescribe how to build it.

A system either satisfies 512's seven properties at every execution
boundary, or it does not.

---

## The Seven Properties

A system satisfies 512's properties if and only if it exhibits all
of the following at every execution boundary:

1. No agent initiates force or fraud against any human
2. All interactions are voluntary and based on explicit consent
3. Consent may be withdrawn and exit is always possible
4. All contracts are explicit, readable, and equally enforceable
5. No rules are hidden or unilaterally changed
6. On failure, the system fails open, reveals governing rules,
   and defaults to human choice
7. The constraint set is immutable and satisfaction is binary

If any single property is not exhibited, the system does not satisfy
512's properties. There is no partial satisfaction.

---

## How Drift Happens

Drift is rarely intentional. It follows predictable patterns.

### Pattern 1 — Softening

Hard constraints become recommendations.

> "No agent may initiate force" → "Agents should avoid initiating force"
> "Exit must always be possible" → "Exit should be available where feasible"
> "Adherence is binary" → "Systems may be partially aligned"

Any softening of a MUST into a SHOULD changes the property.
SPEC_HASH changes. The system no longer satisfies 512's properties.

### Pattern 2 — Scope Narrowing

Universal constraints become conditional.

> "Any human" → "authorized users" / "lawful persons" / "participants"
> "Always possible" → "subject to policy" / "with reasonable notice"
> "All contracts" → "primary agreements" / "material terms"

Scope narrowing is semantic mutation. It looks like clarification.
It is not.

### Pattern 3 — Authority Insertion

A system introduces an interpreter, authority, or enforcer.

> Adding a governance council
> Adding a compliance scoring system
> Adding a certification body
> Adding a registry of approved implementations

512 creates no authority. Any system that adds one has drifted.
The inserted authority will eventually redefine the constraint.

### Pattern 4 — Layer Conflation

Enforcement and witness functions are merged.

> A system that enforces constraints and controls its own evidence record
> A system that monitors execution and blocks it
> A system that logs events and interprets them at the boundary

These are different systems. Merging them breaks the independence
that makes 512's properties verifiable.

### Pattern 5 — Name Retention Without Property Satisfaction

A system drops one or more properties but retains the 512 name.

> "We follow the spirit of 512"
> "We are 512-aligned"
> "We implement 512's principles"

There is no spirit of 512. There is no alignment spectrum.
A system either satisfies all seven properties or it does not.

---

## Prohibited Terms and Framings

The following framings indicate drift and must not appear in
documentation claiming to describe 512:

| Prohibited | Reason |
|---|---|
| "512-compliant" | Compliance implies an authority. 512 has none. |
| "512-compatible" | Compatibility implies partial satisfaction. There is none. |
| "Adopt 512" | 512 is not adopted. Systems satisfy its properties or they do not. |
| "Deploy 512" | 512 is not deployed. It is a discovered constraint. |
| "Implement 512" | 512 is not implemented. Systems are built that satisfy its properties. |
| "Spirit of 512" | There is no spirit. Properties are binary. |
| "Partial alignment" | There is no partial alignment. |
| "512-inspired" | Acceptable only for systems that do not claim property satisfaction. |

---

## What Does Not Constitute Drift

The following do not constitute drift:

- Different kernel wording that produces the same SPEC_HASH
- Different witness architectures observing the same boundary
- Different enforcement mechanisms satisfying the same properties
- Different programming languages or hardware implementations
- Domain-specific constraint definitions upstream of the boundary
- Commercial layers built on top of a satisfying implementation

512 does not prescribe implementation. It prescribes properties.
Any implementation that satisfies all seven properties at every
execution boundary is valid — regardless of how it is built.

---

## The SPEC_HASH Test

The mechanical test for drift is SPEC_HASH comparison.

If a candidate kernel text compiles to the same canonical IR as the
512 kernel and produces the same SPEC_HASH, it satisfies 512's
semantic properties regardless of wording.

If it produces a different SPEC_HASH, it does not — regardless of
how similar it appears.

See `512-core/CANON/KERNEL_EQUIVALENCE_AND_SPEC_HASH.md` for the
full equivalence mechanism.

---

## Relationship to Other Documents

- `512-core/KERNEL/INVARIANTS.md` — the seven invariants defined precisely
- `512-core/CANON/KERNEL_EQUIVALENCE_AND_SPEC_HASH.md` — SPEC_HASH mechanism
- `512-interpretation/FORBIDDEN_MUTATIONS.md` — specific prohibited mutations
- `INTERPRETATION_GUIDE.md` — how not to misread this repository
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — what the boundary looks like in practice
