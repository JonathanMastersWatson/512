# Proposal Object

This document defines the canonical Proposal Object — the structured
record of a proposed action submitted to the gate for evaluation at
the commit boundary.

This is the gate's only input from the proposing entity. Every field
must be populated before evaluation begins. No field is derived,
inferred, or reconstructed after the fact.

All other documents in this repository that reference the Proposal
Object point here. This is the single authoritative definition.

---

## Definition

A **Proposal Object** is a complete, immutable, structured record
of a proposed action, constructed by the proposing entity before
the commit boundary is crossed and submitted to the gate for
deterministic evaluation against the compiled constraint set.

A Proposal Object is not:
- a log entry assembled after execution
- a partial record completed during evaluation
- a request object reused from an upstream API layer
- a mutable structure updated as evaluation proceeds

If any field is populated during or after evaluation, the object
is not a Proposal Object. It is an audit artifact.

---

## Required Fields

All fields are required before evaluation begins. No field is optional
for gate evaluation purposes. Fields tagged *witness-side* are
included in the object but populated by the witness layer after
execution — they are not evaluated by the gate.

### `proposal_id`
**Type:** String — UUID or equivalent collision-resistant identifier
**Source:** Proposing entity, generated at construction time
**Purpose:** Unique identifier for this proposal across all systems.
Links the pre-validation, validation-result, and post-execution
Evidence Objects in the witness layer via correlation ID.

Must be generated before the Proposal Object is submitted. Must not
be reused across proposals.

---

### `agent_id`
**Type:** String — cryptographically attested identity token
**Source:** Identity system upstream of the gate
**Purpose:** Identifies the proposing entity. Must be attested —
not self-declared. The gate does not resolve identity; it receives
an attested token and evaluates whether it satisfies the consent
and authorisation constraints.

---

### `action_type`
**Type:** String — from controlled vocabulary
**Source:** Proposing entity, classification applied before construction
**Purpose:** Classifies the proposed action against a declared
vocabulary of action types. The gate evaluates constraints scoped
to this action type. An action type not in the controlled vocabulary
cannot be evaluated — the gate produces DENY.

---

### `action_params`
**Type:** Object — typed parameters scoped to `action_type`
**Source:** Proposing entity
**Purpose:** The specific parameters of the proposed action. Must
not exceed `declared_scope`. The witness layer compares actual
execution scope against declared scope at Observation Point 3.

---

### `declared_scope`
**Type:** Object — explicit bounds on what the proposing entity
declares it will not exceed
**Source:** Proposing entity
**Purpose:** The proposing entity's declaration of execution bounds.
The gate evaluates declared intent. If execution exceeds declared
scope, the gate's ALLOW has been exploited — this is an
intent-execution correspondence failure, not a gate failure.

---

### `affected_parties`
**Type:** Array of party identifiers
**Source:** Proposing entity, with verification against consent registry
**Purpose:** All parties affected by the proposed action — not
only the initiating party. Required for I1 (no force or fraud) and
I2 (voluntary interaction) evaluation. If affected parties cannot
be enumerated, the action cannot be evaluated for consent.

---

### `consent_evidence`
**Type:** Object — consent token per affected party
**Source:** Consent registry
**Purpose:** Explicit, current consent from each affected party.
Not assumed. Not inherited from a prior action. Each token must
reference the specific action type and must not be expired at
evaluation time.

Required for I2 evaluation. If any affected party lacks a current
consent token, I2 fails.

---

### `contract_reference`
**Type:** String — identifier of the governing contract or terms
**Source:** Contract registry
**Purpose:** The explicit terms governing this action. Must be
readable by affected parties without specialist interpretation.
Must be equally enforceable by all parties.

Required for I4 evaluation. If the contract cannot be resolved
from the registry at evaluation time, I4 fails.

---

### `exit_available`
**Type:** Boolean
**Source:** Proposing entity, confirmed against system state before
construction
**Purpose:** Confirms that departure from the system, interaction,
or obligation remains structurally possible for all parties at the
moment of proposal construction. Must be `true` before the commit
boundary is crossed.

Required for I3 evaluation. If `false`, I3 fails.

---

### `rules_disclosed`
**Type:** Boolean
**Source:** Proposing entity, confirmed against disclosure registry
**Purpose:** Confirms that the active constraint set has been
disclosed to all affected parties and acknowledgement has been
recorded. Must be `true` before the commit boundary is crossed.

Required for I5 evaluation. If `false`, I5 fails.

---

### `spec_hash`
**Type:** String — SHA-256 hex
**Source:** Gate, from loaded compiled constraint set
**Purpose:** The cryptographic commitment to the constraint set
active at evaluation time. Must match the canonical kernel
commitment:
`7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

Required for I7 evaluation. If the spec hash does not match the
gate's loaded constraint set hash, the gate refuses evaluation.
This field is embedded in every Evidence Object by the witness
layer — it binds each evidence record to the exact constraint
specification that was evaluated against.

---

### `authorisation_token`
**Type:** String — cryptographic proof of authorisation
**Source:** Authorisation system upstream of the gate
**Purpose:** Cryptographic proof that the proposing entity is
authorised to propose this action type for this affected party set.
Verified by the gate before evaluation begins. If verification
fails, the gate produces DENY without evaluating invariants.

---

### `intent_hash`
**Type:** String — SHA-256 hex
**Source:** Computed by the proposing entity at construction time
**Purpose:** SHA-256 of the canonical serialisation of the proposed
action (action_type + action_params + declared_scope). Captured
before evaluation begins. Included in the pre-validation Evidence
Object at Observation Point 1.

This is Element 1 of the Proof Object. It creates a cryptographic
commitment to declared intent at the moment of proposal — not
reconstructed from execution outcomes.

---

### `timestamp`
**Type:** String — ISO 8601 UTC
**Source:** Gate clock — not the proposing entity's clock
**Purpose:** The time at which the gate received and accepted the
Proposal Object. The gate's clock governs. The proposing entity
may include a submission timestamp for its own records; the gate's
timestamp is the authoritative record.

---

## Fields Required Before Evaluation Begins

The following fields must be fully populated before the gate begins
invariant evaluation. If any of these fields is absent, null, or
unresolvable, the gate produces DENY without evaluating invariants:

- `proposal_id`
- `agent_id`
- `action_type`
- `action_params`
- `declared_scope`
- `affected_parties`
- `consent_evidence` (one token per affected party)
- `contract_reference` (must resolve from registry)
- `exit_available` (must be `true`)
- `rules_disclosed` (must be `true`)
- `spec_hash` (must match gate's loaded hash)
- `authorisation_token` (must verify)
- `intent_hash`
- `timestamp` (set by gate)

---

## Construction Rules

**Construct before submission.** The Proposal Object is assembled
completely before it is submitted to the gate. The gate receives
a complete object. It does not participate in construction.

**No field may be deferred.** A field that cannot be populated
at construction time indicates a missing upstream dependency —
a consent registry unavailable, a contract reference unresolvable,
an identity system offline. These are integration failures, not
acceptable partial states. The proposal must not be submitted until
all fields are populated.

**No field is carried forward from a prior proposal.** Each
proposal is independently constructed from live system data.
Consent evidence, contract references, and scope declarations
from prior proposals are not inherited.

**Intent hash is computed from canonical serialisation.** The
hash is computed from the action_type, action_params, and
declared_scope fields in their canonical serialised form before
any other processing. It is not computed from the full Proposal
Object — only from the declared intent fields.

---

## Non-Conformant Construction Patterns

**❌ Partial construction — submitting with unpopulated fields**
The gate receives a Proposal Object with null or placeholder values.
The gate produces DENY. The proposal is not evaluated.

**❌ Post-hoc field population — populating fields during or after
evaluation**
Fields populated during evaluation are not part of the evaluated
Proposal Object. Evidence Objects produced from such a proposal
do not represent the evaluated state.

**❌ Inherited consent — carrying consent evidence from a prior
proposal**
Consent evidence must be current at evaluation time. Inherited
tokens may be expired or revoked. I2 requires current explicit
consent.

**❌ Proposer-set timestamp**
The gate sets the timestamp. A proposer-set timestamp enables
temporal fabrication. If the gate does not set the timestamp,
the Evidence Object's temporal record is unreliable.

**❌ Self-attested agent_id**
Agent identity must be externally attested. A self-declared identity
cannot be verified. I1 and I2 evaluation depends on knowing who
is proposing the action.

---

## Relationship to Evidence Objects

The Proposal Object is the input to the gate. The Evidence Object
is the witness layer's record of what the gate received and decided.

At Observation Point 1 (pre-validation), the witness layer records:
- `proposal_id`
- `agent_id`
- `intent_hash`
- `authorisation_token_hash`
- `timestamp`

At Observation Point 2 (validation-result), the witness layer records:
- overall gate result (ALLOW or DENY)
- `spec_hash`
- per-invariant results
- violated constraint detail (on DENY)
- evaluation duration

The `proposal_id` links all three observation points into a single
verifiable chain. No Proposal Object field containing personal data,
contract content, or payload data is stored in the Evidence Object.

---

## Related Files

- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — boundary mechanics and
  non-conformant execution patterns
- `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — how constraints that
  evaluate Proposal Object fields are defined
- `512-ops/REFERENCE_FLOW.md` — how the Proposal Object moves
  through the full evaluation sequence
- `512-ops/PROPERTIES_CHECKLIST.md` — checklist items covering
  Proposal Object field population requirements
- `TERMS.md` — canonical definitions for all Proposal Object terms
- `LAYER_REFERENCE.md` — layer separation governing what the gate
  may and may not do with the Proposal Object
