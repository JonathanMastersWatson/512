# Compiled Constraint Format

This document defines the canonical format for a compiled constraint
— the machine-evaluable form of a single invariant constraint as it
exists inside the gate at evaluation time.

This is the output of constraint definition work. It is the input
to gate evaluation. The gate receives compiled constraints. It does
not receive policy intent, natural language rules, or interpretive
guidance.

All documents in this repository that reference compiled constraints
or the compiled constraint set point here for format definition.

---

## Definition

A **compiled constraint** is a deterministic Boolean expression over
named, typed inputs with declared data sources, produced by
translating a domain-specific policy into a form the gate can
evaluate without interpretation, judgment, or external I/O during
evaluation.

A compiled constraint is not:
- a policy statement
- a natural language rule
- a scoring function
- a probabilistic threshold
- a model output
- a runtime interpretation of intent

If a constraint requires judgment to evaluate, it is not compiled.
It is a policy draft.

---

## Canonical Compiled Rule Shape

Every compiled constraint MUST declare the following fields before
it is admitted to the compiled constraint set:

### `invariant_id`
**Type:** String — one of I1, I2, I3, I4, I5, I6, I7
**Purpose:** The kernel invariant this constraint enforces. Every
compiled constraint is bound to exactly one invariant. A constraint
not bound to an invariant cannot be evaluated by the gate.

---

### `rule_id`
**Type:** String — unique identifier within the compiled constraint set
**Purpose:** Unique identifier for this rule within the deployment's
constraint set. Used in per-invariant evaluation results and in DENY
messages to identify the specific rule that failed.

---

### `description`
**Type:** String — one sentence, plain language
**Purpose:** Human-readable statement of what property this
constraint enforces. Not evaluated by the gate. Used in DENY
messages and audit records.

Example:
> "No execution may transfer funds from a party without their
> current explicit authorisation."

---

### `input_fields`
**Type:** Array of field references
**Purpose:** The exact Proposal Object fields this constraint
evaluates. Every field referenced in the predicate must be declared
here. Undeclared dependencies are non-conformant.

Example:
```json
["consent_evidence.party_id", "consent_evidence.expiry", "timestamp"]
```

---

### `data_sources`
**Type:** Object — field name to source system mapping
**Purpose:** For each input field not sourced directly from the
Proposal Object, the named system that provides the value during
context binding. The gate queries these systems during context
binding (before evaluation begins), not during evaluation.

Example:
```json
{
  "consent_expiry": "consent_registry.tokens[party_id].expiry",
  "exposure_limit": "counterparty_registry.limits[agent_id].max_exposure"
}
```

No data source may be queried during evaluation. All inputs must
be pre-fetched during context binding. A data source that is
unavailable at context binding time produces an unevaluated result
for that constraint — not a DENY, not a pass.

---

### `predicate`
**Type:** String — deterministic Boolean expression
**Purpose:** The exact condition the gate evaluates. Must be
reducible to a single Boolean without interpretation. Must use
only the operators listed in `allowed_operators`.

The predicate is the constraint. Everything else in this format
is metadata about the predicate.

Example:
consent_evidence[party_id].expiry > timestamp
AND consent_evidence[party_id].token != null
AND consent_evidence[party_id].action_type == action_type

---

### `allowed_operators`
**Type:** Array of strings
**Purpose:** The complete set of operators permitted in the
predicate. Operators not in this list are non-conformant.

Permitted operators:
==  !=  >  <  >=  <=  AND  OR  NOT  IN  NOT_IN  IS_NULL  IS_NOT_NULL

Prohibited operators and constructs:
- any function call to an external system
- any model inference or scoring call
- any probabilistic operator
- any operator whose result depends on state outside the declared
  input schema
- any natural language construct

---

### `failure_mode_on_missing_input`
**Type:** Enum — one of: `DENY` | `UNEVALUATED`
**Purpose:** Declares the gate's behaviour when a required input
field cannot be resolved during context binding.

- `DENY` — treat missing input as constraint failure; the gate
  produces DENY for this invariant
- `UNEVALUATED` — record the constraint as unevaluated; this is
  a per-constraint state distinct from pass or fail; it does not
  produce an overall ALLOW

An unevaluated constraint is recorded in the per-invariant results
of the Evidence Object. If any constraint is unevaluated and the
overall evaluation cannot complete, the gate produces no output
and the fail-open handler engages.

No constraint may declare a missing-input behaviour that silently
passes. A missing input is never a pass.

---

### `witness_emission_fields`
**Type:** Array of field names
**Purpose:** The fields from this constraint's evaluation that the
witness layer includes in the validation-result Evidence Object.
Defines what evidence is produced about this constraint's evaluation.

Minimum required emission fields:
- `rule_id`
- `invariant_id`
- `result` (pass / fail / unevaluated)
- `predicate_inputs` (the resolved values evaluated against)
- `failure_detail` (on fail — the specific condition that failed)

No witness emission field may contain payload data, personal
identifiers beyond what is required for consent evidence, or
contract content.

---

## Compiled Constraint Set

A **compiled constraint set** is the complete collection of compiled
constraints active for a given deployment, versioned and hashed as
a unit.

### Set Requirements

- Every invariant (I1 through I7) must have at least one compiled
  constraint in the set. A set with no constraint for any invariant
  is incomplete and must not be loaded by the gate.

- The set is versioned. Each change to any constraint — including
  whitespace — produces a new version with a new hash.

- The set hash (spec hash) is the SHA-256 of the canonical
  serialisation of the complete set. It is computed after all
  constraints are finalised and before the set is loaded.

- The spec hash is disclosed to all affected parties before
  enforcement begins. Enforcement against an undisclosed spec hash
  violates I5.

- The set is immutable at runtime. No constraint may be added,
  removed, or modified after the gate has loaded the set. Changes
  require: producing a new compiled set, computing the new hash,
  disclosing the new hash to affected parties, obtaining consent,
  and restarting the gate process with the new set.

### Set Loading Sequence

1. Gate reads compiled constraint set from configuration
2. Gate computes SHA-256 of canonical serialisation of the set
3. Gate compares computed hash against the canonical commitment
4. If hashes match: set is loaded into read-only memory; gate starts
5. If hashes do not match: gate refuses to start; error is logged;
   no evaluation occurs

The gate verifies the hash at startup and never again at runtime.
The set is in read-only memory after verification. No runtime
modification is possible.

---

## Prohibited Content

The following must not appear in any compiled constraint:

| Prohibited | Reason |
|---|---|
| Model inference calls | Non-deterministic; not reproducible |
| Scoring functions | Produces gradations, not binary result |
| Probabilistic operators | Not deterministic |
| Natural language conditions | Requires interpretation |
| External I/O during evaluation | Breaks latency budget; introduces non-determinism |
| Undefined input references | Hidden dependency; cannot be pre-fetched |
| `reasonable`, `appropriate`, `high risk`, `likely`, `significant`, `material`, `where feasible`, `subject to policy` | Require judgment to evaluate — see `CONSTRAINT_DEFINITION_LAYER.md` |

---

## Example: Complete Compiled Constraint

```json
{
  "invariant_id": "I2",
  "rule_id": "consent.current.v1",
  "description": "Consent must be explicit and current for each affected party at evaluation time.",
  "input_fields": [
    "consent_evidence",
    "affected_parties",
    "action_type",
    "timestamp"
  ],
  "data_sources": {
    "consent_evidence": "consent_registry.tokens"
  },
  "predicate": "ALL(party IN affected_parties: consent_evidence[party].token IS_NOT_NULL AND consent_evidence[party].expiry > timestamp AND consent_evidence[party].action_type == action_type)",
  "allowed_operators": ["ALL", "IN", "IS_NOT_NULL", "AND", ">", "=="],
  "failure_mode_on_missing_input": "DENY",
  "witness_emission_fields": [
    "rule_id",
    "invariant_id",
    "result",
    "predicate_inputs",
    "failure_detail"
  ]
}
```

---

## Relationship to Other Documents

- `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — upstream process for
  translating policy into compiled constraint format
- `512-ops/PROPOSAL_OBJECT.md` — the input the compiled constraint
  evaluates against
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — how compiled constraints
  are evaluated at the gate
- `512-ops/PROPERTIES_CHECKLIST.md` — checklist items covering
  compiled constraint set requirements
- `TERMS.md` — canonical definitions: Compiled Constraint Set,
  Spec Hash, Gate Output
- `LAYER_REFERENCE.md` — layer separation: constraint definition
  is upstream; gate evaluates; witness layer records
