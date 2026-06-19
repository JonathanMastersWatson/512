# Constraint Definition Layer

This document defines how organisations translate policies into
executable constraints for evaluation at the commit boundary.

This is upstream work. The gate does not define constraints.
The gate evaluates them. Constraint definition is the
organisation's responsibility and must be complete before
gate evaluation begins.

---

## What This Document Is

A non-normative operational guide for the constraint definition
layer — the work that occurs upstream of the gate, before any
proposal reaches the commit boundary.

## What This Document Is Not

This document is not:
- part of the 512 kernel
- a policy engine or governance framework
- a compliance system
- a certification instrument
- a definition of what constraints organisations must use

512 does not prescribe domain constraints. It prescribes the
properties that any constraint must satisfy to be evaluable
at the commit boundary.

---

## The Separation That Must Be Maintained

Three functions are involved in gate execution. They must remain
structurally separate.

| Function | What it does | Who owns it |
|---|---|---|
| **Definition** | Translates policy into executable constraints | The organisation |
| **Expression** | Encodes constraints as deterministic binary logic | The organisation's engineers |
| **Enforcement** | Evaluates constraints against proposals | The gate |

Constraint definition must not leak into runtime. The gate
receives a compiled constraint set. It does not receive policy
intent, natural language rules, or interpretive guidance.
It evaluates what it is given.

Any system that requires the gate to interpret, adapt, or apply
judgment to constraints at evaluation time is not a Commit Gate.
It is a policy engine.

---

## The Constraint Definition Model

Every constraint must be defined using this structure before
it can be expressed as executable logic.

### Required Fields

**Intent** — what is being protected.

State the property the constraint enforces in one sentence.
Not the rule. The property.

> "No execution may transfer funds from a party without their
> current explicit authorisation."

**Signal** — what data proves the property holds.

Name the specific data field or record that the gate will
evaluate. If you cannot name a specific data source, the
constraint is not ready for expression.

> `consent_token` present in consent registry for
> `target_party_id`, with `consent_expiry` greater than
> `evaluation_timestamp`.

**Threshold** — the binary condition.

Express the signal as a deterministic true/false condition.
This is the expression the gate will evaluate. It must be
reducible to a single Boolean without interpretation.

> `consent_token != null AND evaluation_timestamp < consent_expiry`

**Authority** — the source of truth for the signal.

Name the system that holds the data the threshold evaluates
against. The gate will query this system during context binding.

> Consent registry — append-only, write-audited, accessible
> to the gate at evaluation time.

---

## Translation Requirement — Binary Reducibility

Every constraint must be reducible to a binary evaluation before
it reaches the gate.

The gate produces exactly two evaluation outputs per constraint:
pass or fail. It produces no scores, no weights, no risk
assessments, no conditional results.

If a constraint cannot be expressed as a binary condition over
named, typed inputs, it is not ready for expression.

### Prohibited Language

The following terms indicate a constraint that is not yet
binary-reducible. Do not submit constraints containing these
terms to the expression stage.

| Prohibited | Reason |
|---|---|
| "reasonable" | Requires judgment to evaluate |
| "appropriate" | Context-dependent; not deterministic |
| "high risk" | A scoring concept, not a binary condition |
| "likely" | Probabilistic; not deterministic |
| "significant" | Requires threshold definition before use |
| "material" | Legal interpretation required |
| "where feasible" | Introduces conditionality |
| "subject to policy" | Defers definition to runtime |

Replace each prohibited term with a measurable, testable condition.

### Translation Examples

**❌ Not binary-reducible:**
> "Transactions must not be high risk."

**✅ Binary-reducible:**
> `current_exposure + proposed_value <= exposure_limit`
> where `exposure_limit` is sourced from the counterparty
> registry and `current_exposure` is sourced from the
> accumulator.

---

**❌ Not binary-reducible:**
> "Consent must be reasonably current."

**✅ Binary-reducible:**
> `consent_expiry > evaluation_timestamp`
> where `consent_expiry` is sourced from the consent registry
> and `evaluation_timestamp` is the gate's clock at evaluation.

---

**❌ Not binary-reducible:**
> "The agent should not take actions that seem coercive."

**✅ Binary-reducible:**
> `affected_party_type != 'human' OR (NOT is_coercive AND
> NOT is_deceptive)`
> where `is_coercive` and `is_deceptive` are boolean fields
> computed from action classification upstream of the gate.

---

## Determinism Requirement

Identical inputs must produce identical outputs on every
invocation, on every machine, at any time.

A constraint is deterministic if:
- every input is typed and sourced from a named registry
- the threshold expression uses only deterministic operators
- no runtime state outside the declared input schema affects
  the result
- no external I/O occurs during evaluation
- no human judgment is applied at evaluation time

A constraint is not deterministic if:
- it relies on a model, heuristic, or scoring system
- it produces different results for the same inputs under
  different conditions
- it requires context that is not declared in the input schema
- it defers any part of its evaluation to a downstream component

Non-deterministic constraints cannot be evaluated by a Commit Gate.

---

## Common Failure Modes

### Vague Policy Language

Policy is written in natural language intended for human
interpretation. It reaches the expression stage without
translation to binary logic.

> "Agents must act in the customer's best interest."

This is a principle, not a constraint. It cannot be evaluated
deterministically. It requires translation into specific,
measurable conditions before it can be expressed.

Resolution: identify the specific observable signal that
indicates the principle is satisfied in a given execution
context. Express that signal as a binary threshold.

---

### Hidden Assumptions

A constraint references data that is assumed to exist without
being explicitly declared in the input schema.

> `transfer_amount <= authorised_limit`

If `authorised_limit` is not declared as a named input sourced
from a specific registry, the gate cannot evaluate this
constraint. The assumption must become an explicit declaration.

Resolution: for every variable in the threshold expression,
name the source system, the field name, and the data type.
No undeclared dependencies.

---

### Runtime Interpretation

A constraint is expressed in a form that requires the gate
to apply judgment at evaluation time.

> "Deny if the request appears unusual for this agent."

Appearance of unusual behaviour is not a binary condition.
It is a pattern-matching task requiring context the gate
does not hold and cannot evaluate deterministically.

Resolution: define what "unusual" means in terms of specific,
measurable deviations from declared parameters. If the
deviation cannot be expressed as a binary threshold, it
cannot be enforced at the commit boundary.

---

### Dependency on External Systems at Evaluation Time

A constraint requires the gate to call an external system
during evaluation — a model, a scoring API, a risk engine —
to resolve its inputs.

External I/O during evaluation breaks the latency budget
and introduces non-determinism. If the external system is
unavailable, the constraint cannot be evaluated.

Resolution: all inputs must be pre-fetched and bound before
evaluation begins. The gate queries registries during context
binding (before evaluation), not during constraint evaluation.
Any input that cannot be pre-fetched is not a valid gate input.

---

### Temporal Drift

The constraint set in force at evaluation does not match
the constraint set disclosed to affected parties.

This occurs when constraints are updated without updating
the spec hash, or when the spec hash disclosed to parties
does not match the hash the gate is evaluating against.

Resolution: every constraint set change produces a new
compiled bundle with a new hash. The new hash must be
disclosed to and acknowledged by affected parties before
enforcement of the new set begins. The spec hash recorded
in Evidence Objects is the ground truth — it must match
the hash disclosed to parties.

---

## Anti-Drift Rules for Constraint Definitions

These rules apply to all constraint definitions in this layer.

- Constraints must be versioned. Each version produces a
  distinct compiled bundle with a distinct hash.

- The spec hash must represent the complete active constraint
  set. A partial hash — covering some but not all active
  constraints — is non-conformant.

- Changes to any constraint require a new spec hash. A gate
  evaluating against a modified constraint set without a
  new hash is not evaluating against a disclosed specification.

- The spec hash disclosed to affected parties must match the
  spec hash recorded in Evidence Objects. Any divergence is
  detectable by verifiers and constitutes a violation of
  Invariant 5.

- Constraints must not be modified at runtime. Constraint
  changes require: producing a new compiled bundle, computing
  the new hash, disclosing the new hash to affected parties,
  obtaining consent to the new constraint set, and restarting
  the gate process with the new specification.

---

## Per-Invariant Definition Checklist

Use this checklist when defining constraints for each invariant.

| Invariant | Definition complete when... |
|---|---|
| I1 — No force or fraud | You have named the specific action types that constitute force or fraud in your domain, and each is expressed as a binary condition over typed inputs |
| I2 — Explicit consent | You have named the consent registry, the consent token structure, and the expiry field, and the threshold evaluates currency without inference |
| I3 — Consent withdrawal | You have defined the propagation window, the epoch mechanism, and the binary condition that detects stale tokens |
| I4 — Contractual clarity | You have named the contract registry, defined what machine-readable and human-readable mean for your contract format, and confirmed both parties have acknowledged the terms |
| I5 — No hidden rules | You have defined how the active spec hash is disclosed, to whom, and how acknowledgement is recorded |
| I6 — Continuity Behaviour / Transparent Denial / Human Default | You have defined what your system does when the gate is unavailable and confirmed the continuity handler generates a gap record; you have confirmed DENY results include the violated invariant ID and constraint reference; you have confirmed exit and contest paths are structurally available on any adverse outcome |
| I7 — Immutability | You have confirmed the gate verifies the canonical hash at startup and refuses to start on mismatch |

A constraint definition is complete only when all fields in the
definition model are populated and the threshold expression is
binary-reducible without any prohibited language.

---

## Related Files

- `512-ops/INTEGRATION_STEPS.md` — Step 4 covers constraint
  definition in the integration workflow
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — boundary mechanics
  and Proposal Object structure
- `512-ops/REFERENCE_FLOW.md` — how defined constraints flow
  through evaluation to anchored evidence
- `512-core/KERNEL/INVARIANTS.md` — the seven invariants each
  constraint set must address
- `ANTI_DRIFT.md` — how constraint definitions drift and how
  to prevent it
