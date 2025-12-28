# Scope and Non‑Goals (Read This First)

512 is a **minimal constraint kernel**: a small set of invariants that bound how
digital systems may claim **execution-time legitimacy** under scale.

It is intentionally incomplete.

## What 512 Is

512 defines the minimum conditions under which a third party can **audit**
whether a system’s **declared rules** were consistent with its **observed execution**
— without relying on hidden authorities.

In 512, **legitimacy is a technical term**:

- **Legitimacy (512):** verifiable consistency between declared rules and observed execution.
- It is **not** a claim about justice, fairness, ethics, or legal validity.

## What 512 Is Not

512 is **not** a protocol suite, product, platform, identity system, incentive system,
governance model, certification program, legal framework, or AI alignment theory.

## Explicit Non‑Goals

512 does **not** attempt to solve:

1. **Adoption / coordination** — it does not force adoption.
2. **Enforcement / consequences** — it makes deviation *observable*, not punishable.
3. **Correctness / “truth”** — it does not prove outcomes are correct, only auditable.
4. **Identity / attribution** — it does not bind actions to real‑world identities.
5. **Safety engineering** — it does not prescribe fail‑closed/fail‑safe control logic.

## Relationship to Implementations

512 does not prescribe an implementation.

**Evidence-Sidecar** (maintained separately) is one example of an external witness
architecture designed to satisfy 512 constraints. It is an existence proof, not a dependency.

## Reading Order

1. `SCOPE_AND_NON_GOALS.md`
2. `README.md`
3. `FAILURE_MODES.md`
4. `512-core/`
