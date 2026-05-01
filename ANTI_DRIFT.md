This is the architectural equivalent of bypass accumulation, but
it is a design error rather than an operational one. The execution
surface is reachable independently of the evaluation result. The
evaluation is structurally advisory — it runs before execution
but does not own the commit path. **Exclusive commit authority**
does not exist. The **non-bypassable commit path** is absent.

Common forms:

> A middleware component that evaluates proposals and passes results
> to a downstream service that performs the actual state change
>
> An API gateway that checks constraints and forwards requests to
> a database layer that writes independently
>
> A compliance check that runs before a transaction engine that
> executes regardless of evaluation outcome

In each case, the evaluation and the commit boundary are separate
systems. The evaluation result is a message, not a gate. Any
implementation where the execution surface can operate without
receiving — or can ignore — the evaluation result is not satisfying
512's properties.

The conformant model requires that the gate's authorisation signal
is the structural prerequisite for the commit path to open. Not a
prior step. Not an upstream check. The gate on the path — holding
**exclusive commit authority** over the **non-bypassable commit path**.

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
- `LAYER_REFERENCE.md` — three-layer semantic firewall: what each
  layer owns and must not claim
- `TERMS.md` — canonical definitions for exclusive commit authority,
  non-bypassable commit path, and all boundary vocabulary
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — what the boundary looks
  like in practice, including non-conformant patterns
- `https://github.com/JonathanMastersWatson/Constraint-Architecture`
  — upstream constraint definition discipline
