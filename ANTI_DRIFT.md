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

512 does not make decisions. It enforces decisions that have already
been committed into constraints.

---

## The Temporal Constraint

512 exists because of a physical fact:

Execution occurs faster than human oversight.
Post-execution governance is structurally late.

When AI agents execute in microseconds and human reaction requires
hundreds of milliseconds, governance cannot function at runtime.
It must function before runtime — at the constraint definition layer —
and at the boundary — where 512 enforces.

Therefore:

- enforcement MUST occur at execution
- not before execution (advisory)
- not after execution (audit)

Systems that attempt to govern through post-execution audit,
dashboards, or workflow reviews are not satisfying 512's properties.
They are observing the absence of governance, not providing it.

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

## What 512 Is Not

512 is not:

- a compliance system
- a policy engine
- a monitoring tool
- an observation or logging system
- a risk scoring engine
- an AI governance layer
- an advisory system
- a certification body
- a standards organisation
- a control plane

512 is a deterministic execution boundary constraint.

It enforces pre-committed constraints at the moment of irreversible
state change. That is its complete function. Nothing more is claimed.

---

## Separation of Constraint Definition and Enforcement

Constraint definition occurs outside the commit boundary.
Enforcement occurs at it. These are different functions.

The commit boundary:

- receives compiled constraint specifications
- evaluates them deterministically
- produces binary outcomes: allow / deny / gap

The commit boundary does NOT:

- define constraints
- modify constraints at runtime
- interpret constraint intent
- resolve ambiguity in constraint definitions
- perform risk scoring or weighting

The boundary enforces constraints. It does not decide what they
should be.

Any system that collapses constraint definition and enforcement
into a single component has eliminated the independence that makes
enforcement verifiable.

### Upstream Reference

The formation of constraint boundaries is addressed by the
Constraint Architecture discipline, maintained separately at:

https://github.com/JonathanMastersWatson/Constraint-Architecture

Governance is not achieved by observing behaviour. It is achieved
by constructing the boundaries within which behaviour is possible.

---

## 512 Is Not a Policy Engine

The commit boundary does NOT:

- define policy
- interpret policy
- resolve policy ambiguity
- perform risk scoring
- adapt behaviour dynamically based on context
- weight constraints against each other

The boundary executes pre-committed constraints only.

Any system that evaluates policies dynamically, uses scoring or
weighting, or introduces interpretation at runtime is not satisfying
512's properties. It is a policy engine. Policy engines are not
commit boundaries.

Without this distinction, vendors turn 512 into a "smart compliance
engine" and determinism is lost.

---

## Observation Mode

A system satisfying 512's properties MAY operate in observation mode.

In observation mode:

- all seven constraints are evaluated at every boundary crossing
- no execution is blocked
- all results are recorded: allow / deny / gap

Observation mode is not a simulation. It is real evaluation without
enforcement. The mechanism is unchanged. Only the enforcement
posture differs.

Observation mode is the correct entry point for institutional
adoption. It allows an organisation to verify that its systems
satisfy 512's properties before enabling enforcement.

### What Observation Mode Is Not

Observation mode is NOT:

- advisory mode
- a recommendation engine
- a partial evaluation
- a bypass of the boundary

Valid outputs in observation mode remain: allow / deny / gap.
No advisory or conditional outputs are produced.

---

## No Advisory Operation

The commit boundary MUST NOT operate in advisory mode.

Advisory outputs are non-conformant. The boundary MUST NOT:

- return recommendations
- produce conditional outcomes
- suggest alternative actions
- score or rank proposals

Valid outputs are exactly three: allow / deny / gap.

Any output that is not one of these three is not a commit boundary
output. A system that produces advisory outputs is not satisfying
512's properties regardless of what it is called.

---

## Intent-Execution Correspondence

The commit boundary evaluates declared intent.

The execution system MUST ensure that execution does not exceed
declared intent.

Any divergence between declared intent and actual execution:

- MUST be detectable
- MUST be recorded in evidence
- MUST be treated as a gap or denial, not an allow

A system where agents declare one intent and execute another has
broken the fundamental property that makes boundary enforcement
meaningful. The boundary becomes a gate on claims, not on actions.

---

## Single Authority Path

All execution paths MUST pass through the commit boundary.

The following are explicitly non-conformant:

- admin bypass paths that skip boundary evaluation
- emergency override mechanisms without gap recording
- direct execution surface access that bypasses the boundary
- parallel execution paths not subject to evaluation

Any parallel path invalidates enforcement. A boundary that can be
bypassed is not a boundary. It is a suggestion.

This is the most common real-world failure mode. Systems are built
with the boundary in the primary path and exceptions accumulate
over time until the boundary is structurally irrelevant.

---

## Deterministic Execution

The commit boundary MUST:

- produce identical outputs for identical inputs
- perform no external I/O during evaluation
- use no probabilistic or heuristic logic
- use no machine learning models in evaluation
- use no scoring systems or weighted logic

Determinism is not a performance property. It is a trust property.

A boundary that produces different outputs for identical inputs
cannot be independently verified. Evidence produced against a
non-deterministic boundary cannot be relied upon.

Any system that introduces probabilistic, heuristic, or ML-based
logic into boundary evaluation is not satisfying 512's properties.

---

## Gap Semantics

A gap is not an evaluation result. It is a failure of evaluation.

**A gap means:** the system could not determine whether the property holds.

**A gap is not:** an allow. It is not a pass condition.

**A gap means:** execution proceeds only because availability is
prioritised over blocking — not because the constraint was satisfied.

Gap behaviour:

- MUST be recorded explicitly
- MUST NOT be treated as allow
- MUST NOT be concealed or smoothed
- MUST be detectable by any verifier

A system that treats gaps as allows has broken the binary property.
A system that conceals gaps has broken independent verifiability.

---

## Binary Satisfaction

Satisfaction of 512's properties is binary.

A system either satisfies all seven properties at every execution
boundary, or it does not. There is no spectrum.

The following claims are non-conformant:

- "partial conformance"
- "512-inspired"
- "512-aligned"
- "mostly satisfying"
- "roadmap to full satisfaction"
- "spirit of 512"

These claims do not exist within 512's property framework.
They are marketing language applied to systems that do not satisfy
512's properties.

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

### Pattern 6 — Policy Engine Substitution

A system replaces deterministic constraint evaluation with dynamic
policy interpretation and calls the result 512-conformant.

> Weighted scoring instead of binary evaluation
> ML models assessing constraint satisfaction
> Risk-based thresholds replacing fixed constraints

Any system that introduces interpretation, weighting, or probabilistic
logic at the boundary is a policy engine. It is not satisfying
512's properties.

### Pattern 7 — Bypass Accumulation

A system builds the boundary correctly but accumulates exceptions
over time.

> Emergency admin paths
> Operator override mechanisms
> Direct database writes bypassing the boundary

Each bypass is a hole. Enough holes and the boundary is
structurally irrelevant regardless of what documentation says.

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
| "Evaluate risk" | 512 evaluates constraints. It does not evaluate risk. |
| "Assess" | Replace with: evaluate constraints / enforce / allow / deny. |
| "Monitor" | Replace with: record / observe. 512 does not monitor. |

---

## What Does Not Constitute Drift

The following do not constitute drift:

- Different kernel wording that produces the same SPEC_HASH
- Different witness architectures observing the same boundary
- Different enforcement mechanisms satisfying the same properties
- Different programming languages or hardware implementations
- Domain-specific constraint definitions upstream of the boundary
- Commercial layers built on top of a satisfying implementation
- Operating in observation mode before enabling enforcement

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
- `https://github.com/JonathanMastersWatson/Constraint-Architecture` — upstream
  constraint definition discipline
