# 512: The Commit Gate — Implementation Reference

**Jonathan M. Watson | 512 / CVS Architecture**
**Version 3.4 | June 2026**
**Canonical Repository:** github.com/JonathanMastersWatson/512
**Canonical Kernel Commitment:** SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`

---

## §-1 Legal Notice and Limitation of Liability

### §-1.1 Informational Nature

This document provides implementation guidance for engineers building Commit Gates that satisfy 512's observable properties. It does not constitute a product specification, a compliance certification, a standards mandate, or a legal instrument. The authors do not intend this document to create obligations on any party, and nothing herein should be read as doing so except as expressly agreed in a separate written agreement. Implementation results depend on the engineering decisions, deployment environments, and operational practices of those who build from this guide.

### §-1.2 No Warranty

This document and the architectures it describes are provided "as is," without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, accuracy, completeness, or non-infringement. The authors and contributors make no representation that this document is free from defects, errors, or omissions. Engineers who implement from this guide bear full responsibility for the correctness, safety, and suitability of their implementations.

### §-1.3 No Professional Advice

Nothing in this document constitutes legal, regulatory, financial, insurance, or engineering advice. Organisations evaluating whether their implementation satisfies the properties described here must consult qualified legal counsel, compliance advisors, and licensed engineers appropriate to their jurisdiction and industry. The authors are not responsible for decisions made in reliance on this document.

### §-1.4 No Guarantee of Coverage or Compliance

A gate implementation built from this guide does not automatically guarantee regulatory compliance, insurance coverage, litigation defence, or audit passage. Compliance is a legal determination made by regulators and courts. Coverage is an underwriting determination made by insurers. This guide provides a technical framework — it does not make compliance determinations or certify implementation correctness.

### §-1.5 Ownership and Licensing — Open Commons Declaration

**512** is a discovered constraint. The authors' position is that discovered constraints — properties that physics and scale force into existence regardless of human recognition — are not ownable in the manner of invented works. The authors assert no proprietary rights over the 512 constraint set, the Commit Gate category, or the seven invariants committed to the canonical kernel file, and do not intend to recognise exclusive proprietary claims asserted by any other party over those elements.

**CVS** (Cryptographic Verification Sidecar) is an invented witness architecture released as open infrastructure commons under CC BY 4.0. The authors assert no exclusive ownership over the base CVS architecture and do not intend to grant or recognise such exclusivity to any other party over the base layer.

**Derivative works** — gate implementations, managed services, SLA-bound products, interpretation tools, industry-specific deployments — are fully ownable and commercialisable by their creators. The base is open. What is built on the base belongs to its builder.

This documentation is released under Creative Commons Attribution 4.0 International (CC BY 4.0). Refer to §-1.7 for complete license terms.

### §-1.6 Public Ledger References

References to the XRP Ledger (XRPL) in this document are descriptive, not prescriptive. This architecture is ledger-agnostic. Any settlement ledger satisfying the mandatory technical properties — deterministic finality, predictable cost, public verifiability, and no execution-layer coupling — may be substituted without altering the architecture's semantics. References to XRPL do not imply endorsement, partnership, dependency, or affiliation.

### §-1.7 License

This document is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/. You are free to share and adapt this material for any purpose, including commercial use, provided attribution is given: "512 Implementation Reference, Jonathan M. Watson, github.com/JonathanMastersWatson/512," a link to the license is provided, and any changes made are indicated.

### §-1.8 Jurisdictional Scope

This document has been prepared with reference to the laws and regulatory frameworks of Canada, the United States, and the United Kingdom. It is not legal advice in any jurisdiction. To the fullest extent permitted by applicable law, the authors seek to limit any liability arising from use of this document or the architectures it describes. The authors do not accept financial liability for decisions made in reliance on this document. Organisations in other jurisdictions must assess applicability independently.

### §-1.9 Financial Projection Disclaimer

All cost, latency, and performance figures in this document are illustrative examples only. They are not guarantees of performance, regulatory penalty avoidance, financial return, or legal defence success. Actual results depend on hardware selection, deployment environment, implementation quality, and operational integrity.

### §-1.10 No Reliance

This document is a descriptive technical specification and reference architecture only.

It is not intended to be relied upon as a certification of compliance, a guarantee of regulatory sufficiency, a guarantee of audit success, a guarantee of insurance coverage, a guarantee of risk mitigation, or a representation of operational fitness.

Compliance, certification, underwriting, and legal sufficiency are determinations made by regulators, courts, insurers, and licensed professionals — not by technical documentation.

Any organisation implementing concepts described herein does so at its own risk and bears full responsibility for deployment posture, regulatory interpretation, operational integrity, and jurisdictional compliance.

### §-1.11 No Endorsement

Nothing in this document constitutes endorsement of any implementation, derivative system, organisation, settlement ledger, or commercial deployment.

References to regulatory frameworks, standards bodies, or public ledger networks are descriptive only and do not imply approval, partnership, affiliation, or recognition by those bodies.

No institution has certified, adopted, approved, or validated 512 or CVS unless expressly stated in a separate, formally executed written agreement.

### §-1.12 Independent Verification Requirement

Where verification is discussed in this document, it refers to cryptographic or structural verifiability of recorded data — not legal, regulatory, or institutional validation. Structural verifiability does not equate to a compliance determination. These are distinct claims requiring distinct evidence under distinct legal and regulatory standards.

### §-1.13 Builder Responsibility

Any party constructing, deploying, or commercialising a system based on 512 or CVS assumes full responsibility for system behaviour, constraint design, regulatory interpretation, evidence storage, key management, anchoring configuration, operational uptime, and all resulting consequences.

The authors of the canonical documentation assume no operational control and no liability for derivative deployments.

---

## 0. Normative Relationships

This document is the engineer-level build reference for a Commit Gate satisfying 512's observable properties. It defines how to build, test, integrate, and operate such a gate — not why the constraint exists or what it means. Engineers read this document. CTOs and boards read `512_ARCHITECTURE_v3.4.md`.

The following canonical documents govern this one:

- **`512_ARCHITECTURE_v3.4.md`** — The authoritative source for what 512 is, why physics forces the Commit Gate category into existence, the seven invariants and their rationale, and the witness layer requirement. The architecture document establishes *what* must be true. This document defines *how* to make it true. Rationale is not repeated here — engineers who need it read `512_ARCHITECTURE_v3.4.md` first.
- **`CVS_ARCHITECTURE`** — Defines the Cryptographic Verification Sidecar: the reference witness layer for 512. Evidence Object schemas, hash-chaining model, and XRPL anchoring semantics are authoritative in that document. This document defines only the integration surface between a gate implementation and a CVS-compatible witness layer.
- **`Constraint-Architecture`** — Defines the upstream constraint discipline: what is admissible, consent logic, authority models, thresholds, and domain-specific admissibility rules. Constraint definition is not in scope for this document. See https://github.com/JonathanMastersWatson/Constraint-Architecture.
- **`512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`** — The authoritative elaboration of Invariant 6. Governs all implementation decisions concerning gate unavailability handling, denial disclosure, and human sovereignty obligations. This document implements what that document defines.

The following operational reference documents in the 512 repository are non-normative companions to this document:

- **`512-ops/INTEGRATION_STEPS.md`** — The 7-step enterprise integration workflow.
- **`512-ops/CONSTRAINT_DEFINITION_LAYER.md`** — How organisations translate policies into executable constraints.
- **`512-ops/REFERENCE_FLOW.md`** — End-to-end sequence from intent declaration to anchored evidence.
- **`512-ops/PROPERTIES_CHECKLIST.md`** — Go-live verification instrument.
- **`AARM_AND_512.md`** — Architectural positioning relative to AARM and the CSA Agentic Control Plane Initiative.
- **`CANONICAL_COMMITMENT.md`** — Permanent priority record for 512 and CVS.

This document takes precedence over neither. Each canonical document is authoritative within its defined scope.

### 0.1 Reference Implementation Status

This document is a technical pattern reference. It is not a managed product, a supported software release, or a commercially maintained service. It carries no SLA, no uptime guarantee, no compliance certification, and no warranty of fitness for any purpose.

**512 is a constraint grammar. A Commit Gate is an implementation artifact.** This document describes how to build the artifact. It does not define the constraint grammar — that is the domain of `512_ARCHITECTURE_v3.4.md §2–4`.

**Builders assume full and sole responsibility** for all decisions made in reliance on this document.

**Normative language scope:** `MUST` and `MUST NOT` language throughout this document describes the internal consistency requirements of a valid Commit Gate implementation pattern. These terms do not create external legal obligations on builders beyond what is established in separate written agreements.

---

## Abstract

This document describes how one may construct a **Commit Gate** satisfying 512's observable properties. It does not imply certification, regulatory adoption, production readiness, or that any implementation built from it meets any external compliance requirement.

This document is an engineering build guide. It specifies, in executable terms, how to construct a Commit Gate that satisfies 512's observable properties: a minimal, immutable, binary enforcement mechanism positioned at the commit boundary of a machine-speed execution system.

What you are building is a deterministic function: `(intent, context, constraints) → {allow, deny}`. It executes in 10–50μs in software, under 5μs on dedicated hardware. It enforces seven pre-committed invariants without interpretation. On infrastructure failure, it produces Evaluation-Unavailable DENY — the commit boundary holds. It integrates with a witness layer that produces independently verifiable execution evidence.

This guide provides the constraint specification format, bytecode compilation pipeline, per-invariant executable schemas, validation sequence with latency targets, CVS integration surface, adapter implementations, deployment topology patterns, performance envelope specifications, security model requirements, and a complete conformance test suite.

A gate implementation that passes every test in §11 satisfies 512's properties. A gate that does not pass every test does not — regardless of what its documentation claims. The canonical commitment `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` is the ground truth. The verification procedure is in §3.2.

---

## 1. The Commit Gate — Position and Insertion

### 1.1 Gate Position Is Architecturally Determined

A **Commit Gate** has exactly one valid position: between authorisation and irreversible state change. This is not a preference. Before the commit boundary, actions are proposals. After it, they are facts. A gate upstream of the commit boundary is advisory. A gate downstream is retroactive. Neither is a Commit Gate.

Finding the commit boundary is the first engineering task. The question to answer: *at what point does the proposed action become a state change that cannot be undone?* The gate belongs immediately before that point, after authorisation has succeeded.

### 1.2 Insertion by Domain

The commit boundary location differs by execution surface. The gate inserts at the following positions:

**AI agent systems:**

```
User Request
    ↓
Agent Orchestrator (planning, reasoning, tool selection)
    ↓
[ COMMIT GATE ]  ← constraint evaluation here
    ↓ allow/deny
Tool Execution Layer  ← COMMIT BOUNDARY
    ↓
External APIs / Resources / State Changes
    ↓
CVS Evidence Capture (parallel, async, off hot path)
```

**Financial systems:**

```
Trading System / Risk Dashboard
    ↓
Order Management
    ↓
[ COMMIT GATE ]  ← constraint evaluation here
    ↓ allow/deny
Execution / Settlement Engine  ← COMMIT BOUNDARY
    ↓
Clearing / Finality
    ↓
CVS Evidence Capture (parallel, async, off hot path)
```

**Hardware and manufacturing systems:**

```
Operator Input / Automated Control
    ↓
Control System (PLC / SCADA)
    ↓
[ COMMIT GATE ]  ← constraint evaluation here
    ↓ allow/deny
Actuator  ← COMMIT BOUNDARY (voltage release)
    ↓
Physical Effect (irreversible)
    ↓
CVS Evidence Capture (parallel, async, off hot path)
```

### 1.3 Bypass Path Elimination Is Mandatory

Every route to the execution surface that does not pass through the gate is a bypass path. The gate implementation **MUST** ensure no such routes exist.

Bypass path audit checklist:

- All write APIs to the execution surface route through gate evaluation
- No emergency override paths skip gate evaluation; where overrides are operationally necessary, they **MUST** generate a gap record — an override that produces no gap record is a bypass, not an override
- Database direct-write access is revoked for all non-gate execution paths
- Administrative access to the execution surface generates a gap record at each use
- All execution pathways are periodically audited structurally

### 1.4 Authorisation Precedes the Gate

The gate evaluates constraints. It does not perform authorisation. Authorisation precedes gate evaluation. The gate receives a cryptographic proof of authorisation and evaluates whether the authorised action satisfies constraints.

### 1.5 Commit Path Ownership Is Non-Bypassable

The gate **MUST** be positioned such that there exists exactly one path to irreversible state change, and that path does not open without the gate's authorisation signal.

**The conformant model:**

```
[upstream systems]
        |
        v
[evaluation at commit boundary]
        |
        v
[irreversible state change — only on ALLOW]
```

The implementation **MUST NOT**:

- position the gate upstream of a separately operable execution surface
- route the gate's authorisation signal through any intermediary before the commit path receives it
- allow any request to reach the commit boundary without gate evaluation under any operational mode
- implement fallback or override execution paths that reach the execution surface without generating a gap record
- open the commit path when the gate cannot evaluate (Evaluation-Unavailable DENY is required)

### 1.6 Non-Conformant Execution Patterns

**❌ Pattern A — Evaluation result handed off to an API layer (NON-CONFORMANT)**
```
[evaluation] → [API call] → [DB write]
```

**❌ Pattern B — Evaluation result handed off to a queue (NON-CONFORMANT)**
```
[evaluation] → [message queue] → [worker executes]
```

**❌ Pattern C — Evaluation result handed off to a broker (NON-CONFORMANT)**
```
[evaluation] → [broker] → [runtime applies decision]
```

**❌ Pattern D — Pre-check positioning (NON-CONFORMANT)**
```
[evaluation check] → [execution layer]
```

**❌ Pattern E — Parallel or fallback execution path (NON-CONFORMANT)**
```
[evaluation]
     |
     +──► [primary execution path]
     |
     +──► [fallback / override / admin path]
```

**❌ Pattern F — Execution on evaluation unavailability (NON-CONFORMANT)**
```
[gate unavailable] → [commit path opens] → [execution proceeds]
```
The commit path must not open without completed evaluation. Evaluation-Unavailable DENY is required.

**✅ The only conformant model:**
```
[upstream systems]
        |
        v
[evaluation at commit boundary]
        |
        v
[irreversible state change — only on ALLOW]
```

---

## 2. Constraint Specification Format

### 2.1 Constraints Are Deterministic Boolean Functions

Constraints are expressed as deterministic Boolean functions over structured inputs. Every input is typed. Every operator is deterministic. Every evaluation produces an identical result for identical inputs, across every execution, on every machine.

The evaluation engine **MUST** conform to the following behavioral requirements:

- Evaluate every constraint expression as a pure Boolean function — no side effects, no state accumulation, no external I/O during evaluation.
- Produce identical output for identical `(intent, context, compiled_spec)` inputs on every invocation.
- **MUST NOT** produce probabilistic output.
- **MUST NOT** operate in an advisory mode.
- **MUST NOT** expose or accept any asynchronous override channel.
- **MUST NOT** modify the active invariant set at runtime.

### 2.2 Constraint Expression Schema

```json
{
  "constraint_id": "string — unique within specification",
  "invariant_ref": "integer 1–7 — which invariant this enforces",
  "description": "string — human-readable; not evaluated",
  "inputs": {
    "field_name": {
      "type": "string | integer | decimal | boolean | timestamp | hash | list<type>",
      "source": "intent | context | registry | accumulator",
      "required": true
    }
  },
  "expression": "string — deterministic Boolean expression over input fields",
  "deny_message": "string — disclosed to proposing entity on deny result"
}
```

### 2.3 Rule Expression Examples

**AI agent spend limit (Invariant 1):**

```json
{
  "constraint_id": "ai_spend_limit_v1",
  "invariant_ref": 1,
  "description": "Agent accumulated spend must not exceed pre-authorised budget",
  "inputs": {
    "agent_id": { "type": "string", "source": "intent", "required": true },
    "cost_estimate": { "type": "decimal", "source": "intent", "required": true },
    "accumulated_spend": { "type": "decimal", "source": "accumulator", "required": true },
    "spend_limit": { "type": "decimal", "source": "registry", "required": true }
  },
  "expression": "accumulated_spend + cost_estimate <= spend_limit",
  "deny_message": "spend_limit_exceeded"
}
```

**Consent check (Invariant 2):**

```json
{
  "constraint_id": "consent_check_v1",
  "invariant_ref": 2,
  "description": "Execution affecting a party requires current, explicit consent",
  "inputs": {
    "target_party_id": { "type": "string", "source": "intent", "required": true },
    "consent_token": { "type": "hash", "source": "registry", "required": false },
    "consent_expiry": { "type": "timestamp", "source": "registry", "required": false },
    "evaluation_time": { "type": "timestamp", "source": "context", "required": true }
  },
  "expression": "consent_token != null AND evaluation_time < consent_expiry",
  "deny_message": "consent_absent_or_expired"
}
```

**Withdrawal propagation (Invariant 3):**

```json
{
  "constraint_id": "withdrawal_propagation_v1",
  "invariant_ref": 3,
  "description": "Execution must not proceed against a party in revoked-consent state",
  "inputs": {
    "target_party_id": { "type": "string", "source": "intent", "required": true },
    "consent_epoch": { "type": "integer", "source": "registry", "required": true },
    "token_epoch": { "type": "integer", "source": "intent", "required": true }
  },
  "expression": "token_epoch == consent_epoch",
  "deny_message": "consent_withdrawn_epoch_mismatch"
}
```

**Financial exposure limit (Invariant 1):**

```json
{
  "constraint_id": "exposure_limit_v1",
  "invariant_ref": 1,
  "description": "Transaction must not breach counterparty or sector exposure limit",
  "inputs": {
    "counterparty_id": { "type": "string", "source": "intent", "required": true },
    "proposed_value": { "type": "decimal", "source": "intent", "required": true },
    "current_exposure": { "type": "decimal", "source": "accumulator", "required": true },
    "exposure_limit": { "type": "decimal", "source": "registry", "required": true }
  },
  "expression": "current_exposure + proposed_value <= exposure_limit",
  "deny_message": "exposure_limit_exceeded"
}
```

**Hardware tolerance override (Invariant 1):**

```json
{
  "constraint_id": "tolerance_override_v1",
  "invariant_ref": 1,
  "description": "Requested tolerance must fall within authorised range",
  "inputs": {
    "operator_id": { "type": "string", "source": "intent", "required": true },
    "requested_tolerance": { "type": "decimal", "source": "intent", "required": true },
    "range_min": { "type": "decimal", "source": "registry", "required": true },
    "range_max": { "type": "decimal", "source": "registry", "required": true },
    "approved_operators": { "type": "list<string>", "source": "registry", "required": true }
  },
  "expression": "(requested_tolerance >= range_min AND requested_tolerance <= range_max) AND (operator_id IN approved_operators)",
  "deny_message": "tolerance_out_of_range_or_operator_unauthorised"
}
```

### 2.4 Constraints Compile Once; Runtime Modification Is Prohibited

Constraints are compiled to bytecode once, at specification deployment time. The compilation step rejects any expression requiring external I/O, any expression exceeding the 50μs budget, and any expression with undeclared inputs.

```bash
512-compiler compile --spec ./constraints/*.json --output ./dist/512-kernel.bundle
512-compiler hash ./dist/512-kernel.bundle
# Output: SHA-256: 7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5

sha256sum 512-core/KERNEL/512-kernel-padded.txt
# Expected: 7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5
```

If the runtime hash does not match the canonical commitment, the gate **MUST** refuse to start.

---

## 3. The Seven Invariants — Implementation

### 3.1 Invariant 1 — No Agent May Initiate Force or Fraud Against Any Human

```json
{
  "action_type": "string",
  "affected_party_type": "enum: human | system | external_service",
  "is_coercive": "boolean",
  "is_deceptive": "boolean",
  "transfer_amount": "decimal",
  "authorised_transfer_limit": "decimal"
}
```

**Expression:** `(affected_party_type != 'human' OR (NOT is_coercive AND NOT is_deceptive)) AND (action_type != 'fund_transfer' OR transfer_amount <= authorised_transfer_limit)`

**Unit test fixtures:**

```json
[
  {
    "description": "coercive action against human — must deny",
    "inputs": { "affected_party_type": "human", "is_coercive": true, "is_deceptive": false, "action_type": "data_access", "transfer_amount": 0, "authorised_transfer_limit": 1000 },
    "expected": "deny",
    "violated_constraint": "invariant_1_no_force_fraud"
  },
  {
    "description": "fund transfer within limit — must allow",
    "inputs": { "affected_party_type": "human", "is_coercive": false, "is_deceptive": false, "action_type": "fund_transfer", "transfer_amount": 500, "authorised_transfer_limit": 1000 },
    "expected": "allow"
  },
  {
    "description": "fund transfer exceeding limit — must deny",
    "inputs": { "affected_party_type": "human", "is_coercive": false, "is_deceptive": false, "action_type": "fund_transfer", "transfer_amount": 1001, "authorised_transfer_limit": 1000 },
    "expected": "deny",
    "violated_constraint": "invariant_1_no_force_fraud"
  }
]
```

### 3.2 Invariant 2 — All Interactions Must Be Voluntary and Based on Explicit Consent

**Expression:** `NOT action_affects_human OR (consent_token_present AND consent_type == 'explicit' AND evaluation_timestamp < consent_expiry)`

**Unit test fixtures:**

```json
[
  {
    "description": "no consent token — must deny",
    "inputs": { "action_affects_human": true, "consent_token_present": false, "consent_type": "none", "consent_expiry": "2099-01-01T00:00:00Z", "evaluation_timestamp": "2026-02-01T00:00:00Z" },
    "expected": "deny",
    "violated_constraint": "invariant_2_voluntary_consent"
  },
  {
    "description": "implied consent — must deny",
    "inputs": { "action_affects_human": true, "consent_token_present": true, "consent_type": "implied", "consent_expiry": "2099-01-01T00:00:00Z", "evaluation_timestamp": "2026-02-01T00:00:00Z" },
    "expected": "deny",
    "violated_constraint": "invariant_2_voluntary_consent"
  },
  {
    "description": "explicit consent, not expired — must allow",
    "inputs": { "action_affects_human": true, "consent_token_present": true, "consent_type": "explicit", "consent_expiry": "2099-01-01T00:00:00Z", "evaluation_timestamp": "2026-02-01T00:00:00Z" },
    "expected": "allow"
  }
]
```

### 3.3 Invariant 3 — Consent May Be Withdrawn; Exit Must Always Be Possible

**Expression:** `NOT action_affects_human OR (presented_epoch == registry_epoch AND withdrawal_propagated)`

**Unit test fixtures:**

```json
[
  {
    "description": "epoch mismatch — consent withdrawn — must deny",
    "inputs": { "action_affects_human": true, "presented_epoch": 4, "registry_epoch": 5, "withdrawal_propagated": true },
    "expected": "deny",
    "violated_constraint": "invariant_3_consent_withdrawal"
  },
  {
    "description": "current epoch, propagated — must allow",
    "inputs": { "action_affects_human": true, "presented_epoch": 5, "registry_epoch": 5, "withdrawal_propagated": true },
    "expected": "allow"
  }
]
```

### 3.4 Invariant 4 — All Contracts Must Be Explicit, Readable, and Equally Enforceable

**Expression:** `contract_machine_readable AND contract_human_readable AND both_parties_acknowledged AND NOT enforcement_asymmetry`

**Unit test fixtures:**

```json
[
  {
    "description": "enforcement asymmetry — must deny",
    "inputs": { "contract_machine_readable": true, "contract_human_readable": true, "both_parties_acknowledged": true, "enforcement_asymmetry": true },
    "expected": "deny",
    "violated_constraint": "invariant_4_explicit_contracts"
  },
  {
    "description": "all conditions met — must allow",
    "inputs": { "contract_machine_readable": true, "contract_human_readable": true, "both_parties_acknowledged": true, "enforcement_asymmetry": false },
    "expected": "allow"
  }
]
```

### 3.5 Invariant 5 — No Rules May Be Hidden or Unilaterally Changed

**Expression:** `active_spec_hash == disclosed_spec_hash AND active_spec_hash == canonical_hash AND disclosure_acknowledged`

**Unit test fixtures:**

```json
[
  {
    "description": "hash mismatch — modified spec — must deny",
    "inputs": { "active_spec_hash": "AAAA...", "disclosed_spec_hash": "7B08...", "disclosure_acknowledged": true, "canonical_hash": "7B08..." },
    "expected": "deny",
    "violated_constraint": "invariant_5_no_hidden_rules"
  },
  {
    "description": "correct hash, acknowledged — must allow",
    "inputs": { "active_spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5", "disclosed_spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5", "disclosure_acknowledged": true, "canonical_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5" },
    "expected": "allow"
  }
]
```

### 3.6 Invariant 6 — Evaluation-Unavailable DENY, Transparent Denial, Human Default

**What it prevents:** Ungoverned execution on gate failure; silent denial; permanent deprivation of human agency.

**Implementation requirement:** I6 imposes obligations on the gate's failure handling logic, its DENY response, and the surrounding system. The authoritative elaboration is `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`.

**Evaluation-Unavailable DENY implementation:**

```python
def evaluate_with_infrastructure_failure_deny(proposal, constraints):
    """
    Returns (result, deny_cause, evidence_type) tuple.
    result: 'allow' | 'deny'
    deny_cause: None | 'constraint_violation' | 'evaluation_unavailable'
    evidence_type: 'evaluated' | 'evaluation_unavailable_deny'
    """
    try:
        result = evaluate_constraints(proposal, constraints)
        return (result, 'constraint_violation' if result == 'deny' else None, 'evaluated')
    except GateUnavailableError:
        record_evaluation_unavailable_deny(
            proposal_id=proposal.id,
            agent_id=proposal.agent_id,
            failure_cause='gate_unavailable',
            timestamp=now(),
            retry_permitted=True
        )
        return ('deny', 'evaluation_unavailable', 'evaluation_unavailable_deny')
    except EvaluationTimeout:
        record_evaluation_unavailable_deny(
            proposal_id=proposal.id,
            agent_id=proposal.agent_id,
            failure_cause='evaluation_timeout',
            timestamp=now(),
            retry_permitted=True
        )
        return ('deny', 'evaluation_unavailable', 'evaluation_unavailable_deny')
```

The commit path does not open on infrastructure failure. The evaluation-unavailable DENY is returned to the proposing entity with failure cause and retry path. The gap record is forwarded to the CVS sidecar regardless of whether the sidecar is available. If the sidecar is also unavailable, the gap record is queued locally and forwarded on reconnection. Local queue depth and forwarding latency are performance envelope parameters defined in §8.

**Unit test fixtures:**

```json
[
  {
    "description": "gate failure — must produce evaluation-unavailable DENY, commit path remains closed",
    "setup": "inject GateUnavailableError at evaluation start",
    "expected_result": "deny",
    "expected_deny_cause": "evaluation_unavailable",
    "expected_retry_permitted": true,
    "expected_execution_result": "no execution — commit path remains closed",
    "gap_record_fields_required": ["proposal_id", "agent_id", "failure_cause", "timestamp", "retry_permitted"]
  },
  {
    "description": "deny result discloses failed invariant — human can act on information",
    "setup": "submit proposal violating invariant 2",
    "expected_result": "deny",
    "expected_deny_cause": "constraint_violation",
    "expected_deny_response_fields": ["violated_constraint", "deny_message"]
  }
]
```

### 3.7 Invariant 7 — The Specification Is Immutable; Adherence Is Binary

```python
def load_specification(spec_path, expected_hash):
    with open(spec_path, 'rb') as f:
        spec_bytes = f.read()

    actual_hash = sha256(spec_bytes).hexdigest().upper()

    if actual_hash != expected_hash:
        raise SpecificationIntegrityError(
            f"Specification hash mismatch. "
            f"Expected: {expected_hash} "
            f"Actual:   {actual_hash}"
        )

    return load_readonly(spec_bytes)
```

**Runtime immutability:** The specification **MUST NOT** be reloaded, patched, or modified in memory after startup.

**Conformance is binary:** A gate evaluating 6 of 7 invariants is not "mostly conformant." It is non-conformant.

---

## 4. The Validation Sequence

### 4.1 Every Proposal Passes Four Steps in Fixed Order

```
PROPOSING ENTITY          COMMIT GATE               CONTEXT REGISTRIES        WITNESS LAYER (CVS)
       │                       │                             │                        │
       │── proposal ──────────►│                             │                        │
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 1: INTENT DECLARATION    ║         │                        │
       │          ║  Parse declaration structure   ║         │                        │
       │          ║  Verify authorisation token    ║         │                        │
       │          ║  Assign correlation_id         ║         │                        │
       │          ║  Target: <5μs                  ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │── emit pre_validation ─────────────────────────────►│
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 2: CONTEXT BINDING       ║         │                        │
       │          ║  Query accumulator values      ║         │                        │
       │          ╠════════════╪═══════════════════╣         │                        │
       │          ║  Query consent registry   ─────╫────────►│                        │
       │          ║  Query capability grants  ─────╫────────►│                        │
       │          ║  Query spec disclosure    ─────╫────────►│                        │
       │          ║  Assemble (intent, context)     ║◄────────│                        │
       │          ║  Target: <10μs (cache hit)      ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 3: CONSTRAINT EVALUATION ║         │                        │
       │          ║  Evaluate 7 invariants          ║         │                        │
       │          ║  Deterministic bytecode only    ║         │                        │
       │          ║  No external I/O during eval    ║         │                        │
       │          ║  → ALLOW or DENY                ║         │                        │
       │          ║  Target: <30μs                  ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │── emit validation_result ──────────────────────────►│
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 4: COMMIT AUTHORISATION  ║         │                        │
       │          ║  ALLOW → commit path opens      ║         │                        │
       │          ║  DENY  → commit path closed     ║         │                        │
       │          ║          + violated invariant   ║         │                        │
       │          ║            OR failure cause     ║         │                        │
       │          ║  Target: <5μs                   ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │                             │                        │
       │◄── ALLOW / DENY ───────│                             │                        │
       │                       │                             │                        │
  [commit path opens           │                             │                        │
   on ALLOW only]              │── emit post_execution ─────────────────────────────►│
       │                       │   (ALLOW only)              │                        │

── async (off critical path) ──────────────────────────────────────────────────────────►
   CVS emission never delays execution. Gate does not wait for witness acknowledgement.

EVALUATION-UNAVAILABLE DENY PATH (gate unavailable or Step 3 timeout):
       │                       │                             │                        │
       │                  GateUnavailable                    │                        │
       │                  or EvalTimeout                     │                        │
       │   [infrastructure-failure handler — commit path remains closed]             │
       │◄── DENY (evaluation_unavailable, retry_permitted: true) ───────────────────│
       │                       │── emit deny_evidence_object ───────────────────────►│
       │                       │── emit gap_record (sidecar) ───────────────────────►│
       │                       │   [queued locally if CVS unavailable]               │
```

**Step 1 — Intent Declaration (target: <5μs)**

```json
{
  "proposal_id": "string — unique, generated by proposing entity",
  "agent_id": "string — cryptographically attested identity",
  "action_type": "string — from controlled vocabulary",
  "action_params": { },
  "declared_scope": { },
  "intent_hash": "string — SHA-256 of serialised intent",
  "authorisation_token": "string — cryptographic proof of authorisation",
  "timestamp": "string — ISO 8601"
}
```

**Step 2 — Context Binding (target: <10μs)**

Context includes accumulator values, registry lookups (consent status, capability grants, spec hash disclosure acknowledgements), and environmental state. Context assembly queries **MUST** be pre-cached for hot-path evaluation.

**Step 3 — Constraint Evaluation (target: <30μs)**

The seven invariant expressions are evaluated against the assembled `(intent, context)` pair. Evaluation completes synchronously within the Step 3 latency budget or the infrastructure-failure handler engages — there is no third path.

```python
def evaluate_constraints(intent, context, compiled_spec):
    results = {}
    for invariant_id, constraint_fn in compiled_spec.items():
        results[invariant_id] = constraint_fn(intent, context)

    overall = all(results.values())
    return EvaluationResult(
        overall='ALLOW' if overall else 'DENY',
        per_invariant=results,
        violated=[k for k, v in results.items() if not v],
        spec_hash=compiled_spec.hash,
        evaluation_duration_us=elapsed_us()
    )
```

If any invariant produces `false`, the overall result is `DENY`. The deny response **MUST** include the specific violated invariant identifier and the human-readable `deny_message`. The evaluation engine **MUST NOT** suppress, redact, or generalise the violated invariant identifier.

**Step 4 — Commit Authorisation Signal (target: <5μs)**

The evaluation result **MUST** be one of exactly two values: `ALLOW` or `DENY`. No other output is valid. When the gate is unavailable or evaluation times out, the infrastructure-failure handler produces DENY (deny_cause: evaluation_unavailable). The commit path remains closed. Admissibility requires completed evaluation — an action does not commit because the gate was unavailable.

- `ALLOW` — the gate **MUST** return this result. The commit path opens. Execution proceeds. The gate **MUST NOT** append conditions, recommendations, or caveats.
- `DENY (constraint violation)` — the gate **MUST** return this result with the violated invariant identifier and deny message. The commit path remains closed. Execution does not proceed. The gate **MUST NOT** omit the violated invariant identifier.
- `DENY (evaluation unavailable)` — the infrastructure-failure handler produces this result. The commit path remains closed. Execution does not proceed. The DENY **MUST** include failure cause and retry_permitted: true. The CVS sidecar emits a gap record. An evaluation-unavailable DENY **MUST NOT** be treated as ALLOW. It is not a constraint violation — no invariant was evaluated.

### 4.2 Latency Budget

| Step | Target (median) | Target (p99) | Failure mode if exceeded |
|---|---|---|---|
| Intent Declaration | <5μs | <10μs | Reject as malformed |
| Context Binding | <10μs | <20μs | Use cached context; flag stale |
| Constraint Evaluation | <30μs | <100μs | Evaluation-Unavailable DENY; emit gap record to CVS sidecar |
| Commit Authorisation Signal | <5μs | <10μs | Non-blocking; log latency breach |
| **Total** | **<50μs** | **<200μs** | |

### 4.3 Intent-Execution Correspondence

The gate evaluates declared intent. Enforcement of correspondence between declared intent and actual execution is an implementation responsibility at the execution layer.

### 4.4 Observation Mode Is the Correct Enterprise Entry Point

In observation mode:

- all seven invariants are evaluated at every boundary crossing
- no execution is blocked — all proposals proceed regardless of evaluation result
- all gate results are recorded: ALLOW or DENY; evaluation-unavailable DENY events are recorded by the witness layer

Observation mode surfaces unexpected DENY results, evaluation-unavailable DENY events indicating integration issues, and coverage gaps before enforcement depends on them.

**Observation mode is not advisory mode** — evaluation is real and complete.

---

## 5. CVS Integration Surface

### 5.1 Three Observation Points

**Observation Point 1 — Pre-Validation:**

```json
{
  "observation_point": "pre_validation",
  "proposal_id": "string",
  "agent_id": "string",
  "intent_hash": "string",
  "authorisation_token_hash": "string",
  "timestamp": "string — ISO 8601",
  "correlation_id": "string"
}
```

**Observation Point 2 — Validation Result:**

```json
{
  "observation_point": "validation_result",
  "proposal_id": "string",
  "correlation_id": "string",
  "overall_result": "allow | deny",
  "deny_cause": "constraint_violation | evaluation_unavailable | null",
  "spec_hash": "string",
  "per_invariant_results": {
    "invariant_1_no_force_fraud": "pass | fail",
    "invariant_2_voluntary_consent": "pass | fail",
    "invariant_3_consent_withdrawal": "pass | fail",
    "invariant_4_explicit_contracts": "pass | fail",
    "invariant_5_no_hidden_rules": "pass | fail",
    "invariant_6_result": "pass | fail",
    "invariant_7_kernel_immutability": "pass | fail"
  },
  "violated_constraint_detail": "string | null — populated on constraint_violation DENY only",
  "failure_cause": "string | null — populated on evaluation_unavailable DENY only",
  "retry_permitted": "boolean | null — populated on evaluation_unavailable DENY only",
  "evaluation_duration_us": "integer",
  "timestamp": "string — ISO 8601"
}
```

**Observation Point 3 — Post-Execution (ALLOW only):**

```json
{
  "observation_point": "post_execution",
  "proposal_id": "string",
  "correlation_id": "string",
  "execution_outcome": "completed | failed | cancelled",
  "actual_scope": { },
  "execution_duration_us": "integer",
  "timestamp": "string — ISO 8601"
}
```

### 5.2 Gate and Witness Layer Must Never Share Authority

The gate **MUST NOT** control the witness layer. The witness layer **MUST NOT** influence gate evaluation. This separation is structural, not procedural.

- The gate's service identity has write-only, append-only access to the CVS event queue
- The gate has no read access to the evidence store
- The gate has no access to CVS attestation keys
- The CVS process has no access to gate configuration, constraint specifications, or evaluation logic

### 5.3 Evaluation-Unavailable DENY Records Are First-Class Witness Events

When the gate cannot evaluate, the infrastructure-failure handler produces DENY (deny_cause: evaluation_unavailable). The deny Evidence Object and gap record **MUST** be forwarded to the CVS event queue.

**Deny Evidence Object (evaluation-unavailable):**

```json
{
  "observation_point": "validation_result",
  "overall_result": "deny",
  "deny_cause": "evaluation_unavailable",
  "failure_cause": "gate_unavailable | evaluation_timeout | process_crash",
  "retry_permitted": true,
  "proposal_id": "string",
  "agent_id": "string",
  "timestamp": "string — ISO 8601",
  "spec_hash": "string",
  "correlation_id": "string"
}
```

**CVS sidecar gap record:**

```json
{
  "observation_point": "validation_gap",
  "proposal_id": "string",
  "agent_id": "string",
  "gap_start": "string — ISO 8601",
  "gap_reason": "gate_unavailable | evaluation_timeout | process_crash",
  "gate_output_during_gap": "deny_evaluation_unavailable",
  "correlation_id": "string"
}
```

If the CVS queue is unavailable when an evaluation-unavailable DENY occurs, the records **MUST** be persisted to a local durable queue and forwarded on reconnection. Local queue **MUST** be sized for a minimum of 30 minutes of records at peak throughput. Records **MUST NOT** be discarded.

---

## 6. Adapter Layer

### 6.1 Adapters Observe and Forward; They Do Not Interfere

Adapters connect the gate's CVS event stream to the witness layer's capture infrastructure. Adapters are non-interfering — they observe and forward; they do not modify events, acknowledge messages, or write to production systems.

### 6.2 Kafka Adapter

```yaml
kafka_adapter:
  bootstrap_servers: "kafka-host:9092"
  consumer_group: "cvs-witness-observer"
  topics:
    - "gate.pre_validation"
    - "gate.validation_result"
    - "gate.post_execution"
    - "gate.validation_gap"
  auto_offset_reset: "earliest"
  enable_auto_commit: false
  isolation_level: "read_committed"
```

### 6.3 Change Data Capture (CDC) Adapter

```yaml
cdc_adapter:
  type: "postgres_logical"
  connection: "postgresql://cvs-readonly@host:5432/gate_events"
  publication: "gate_events_pub"
  slot_name: "cvs_witness_slot"
  tables:
    - "gate_pre_validation"
    - "gate_validation_results"
    - "gate_post_execution"
    - "gate_validation_gaps"
```

### 6.4 OpenTelemetry (OTEL) Adapter

```yaml
otel_adapter:
  type: "additional_exporter"
  endpoint: "cvs-collector:4317"
  protocol: "grpc"
  resource_attributes:
    service.name: "512-commit-gate"
    cvs.integration: "true"
```

### 6.5 API Gateway Mirror Adapter

```yaml
api_mirror_adapter:
  mirror_target: "http://cvs-capture:8080/mirror"
  mirror_percentage: 100
  mirror_request_body: true
  mirror_response_body: true
```

### 6.6 SmartNIC Capture Adapter

For FPGA-based gate hardware or ultra-low-latency deployments requiring sub-microsecond capture and zero CPU impact. The SmartNIC capture engine **MUST** operate independently of the gate CPU and **MUST NOT** add latency to the gate's critical path.

---

## 7. Deployment Topologies

### 7.1 Pre-Production: Discovery Mode Is Mandatory Before Enforcement

**Discovery Mode configuration:**

```yaml
gate_mode: "discovery"
```

Discovery phase duration: 30–90 days. Output: gap analysis showing which invariants fail, at what frequency, for which agents.

**Enforcement Mode transition checklist:**

- [ ] All invariant-1 violations reviewed
- [ ] All invariant-2 violations resolved
- [ ] All invariant-3 violations resolved
- [ ] False positive rate below 0.1% on production traffic replay
- [ ] CVS integration tested: Evidence Objects generated for ALLOW, constraint violation DENY, and evaluation-unavailable DENY events
- [ ] Evaluation-Unavailable DENY tested under simulated gate failure — commit path confirmed closed
- [ ] Performance envelope validated: median <50μs, p99 <200μs
- [ ] Commit path exclusivity verified: no route to execution surface bypasses gate

### 7.2 On-Premises Topology

```
┌─────────────────────────────────────────────────────────┐
│ On-Premises Network                                      │
│                                                          │
│  ┌──────────────────┐      ┌─────────────────────────┐  │
│  │ Execution Surface│──→──│  COMMIT GATE            │  │
│  │                  │      │  (Enforcement VLAN)     │  │
│  └──────────────────┘      └────────────┬────────────┘  │
│                                         │               │
│                              ┌──────────▼────────────┐  │
│                              │  CVS Sidecar          │  │
│                              └──────────┬────────────┘  │
│                              ┌──────────▼────────────┐  │
│                              │  Evidence Store       │  │
│                              │  (WORM / MinIO)       │  │
│                              └──────────┬────────────┘  │
│                              ┌──────────▼────────────┐  │
│                              │  Access Plane         │  │
│                              └───────────────────────┘  │
└─────────────────────────────────────────┼───────────────┘
                                          ↓ XRPL anchoring
                                  Public Settlement Ledger
```

### 7.3 Hybrid Cloud Topology

```
On-Premises:  Commit Gate → CVS Sidecar → Evidence Store (primary)
                                                ↓ encrypted replication (TLS 1.3)
Cloud:                                    Evidence Store (replica)
                                                ↓ read-only
                                          Access Plane (cloud)
```

### 7.4 Cloud-Native Topology

```
Production VPC (Execution + Gate):
  Commit Gate in dedicated security group
  Outbound-only rules to CVS event queue

Evidence Store VPC:
  S3 with Object Lock enabled
  No public access

Access Plane VPC:
  ALB with HTTPS-only
  Read-only access to Evidence Store
```

---

## 8. Performance Envelope

### 8.1 Latency Budget by Component

| Step | Budget (median) | Budget (p99) | Notes |
|---|---|---|---|
| Intent parsing + auth | 5μs | 10μs | Struct deserialisation + token verify |
| Context binding | 10μs | 20μs | Cache-hit path |
| Constraint evaluation (7 invariants) | 30μs | 100μs | Compiled bytecode; no I/O |
| Commit authorisation signal | 5μs | 10μs | Struct serialisation + queue write |
| CVS event forwarding | async | async | Off critical path |

### 8.2 Software Gate — Hardware Requirements

| Component | Minimum | Recommended |
|---|---|---|
| CPU | 4 cores, 3.0 GHz | 8 cores, 3.5 GHz, AVX-512 |
| RAM | 16 GB | 32 GB |
| Storage | NVMe SSD | NVMe RAID-1 |
| Network to exec surface | <1ms RTT | <100μs RTT |
| Network to CVS queue | <5ms RTT | <1ms RTT |

### 8.3 Gate Addition Adds 10–50μs at the Commit Boundary

| Domain | Existing pipeline latency | Gate addition | Relative overhead |
|---|---|---|---|
| AI agent systems | 100–500μs | 10–50μs | 5–10% |
| Financial systems | 50–200μs | 10–50μs | 10–20% |
| Hardware / manufacturing | 10–100ms | 10–50μs | <0.1% |

### 8.4 FPGA Hardware Reduces Evaluation to Under 5μs

The FPGA implementation requirements:

- Seven invariant expressions synthesised to FPGA logic at specification compile time
- Bitstream hash **MUST** be verified against the canonical commitment before deployment
- Evaluation-Unavailable DENY **MUST** be implemented in FPGA logic — if the FPGA evaluation path fails, DENY is asserted and a gap signal is emitted to the CVS sidecar
- The gap signal triggers a gap record in the host system's CVS event queue

### 8.5 CVS Capture Adds Zero Evaluation Latency

CVS event forwarding is fully asynchronous and off the evaluation hot path. Buffer overflow generates an evaluation-unavailable DENY condition, not an evaluation failure.

---

## 9. Security Model

### 9.1 The Specification Is the Primary Attack Surface

Three layers prevent specification substitution:

**Load-time hash verification:** Gate process verifies specification hash at startup. Mismatch causes startup failure.

**Runtime immutability:** Specification loaded into read-only memory region. Write triggers process abort and gap record.

**Witness layer hash recording:** Every Evidence Object includes `spec_hash`. Hash mismatch is mechanically detectable.

### 9.2 The Gate Process Must Run in Isolation

- Separate process, separate OS user, no shared memory with execution surface
- No inbound connections from any source other than the execution surface
- Gate process **MUST NOT** have write access to execution surface storage

### 9.3 HSM Key Custody for Specification Signing

- FIPS 140-2 Level 2 minimum (Level 3 recommended)
- Signing key never leaves HSM
- Gate startup verifies both SHA-256 hash and cryptographic signature

### 9.4 Signing Keys Rotate on a Fixed Schedule

- Annual rotation: standard deployments
- Quarterly rotation: high-security environments
- Immediate rotation: suspected compromise

### 9.5 Compromise Protocol

Gate process compromise: isolate, analyse evidence chain, rotate keys. Specification signing key compromise: rotate immediately, verify all instances. Context registry compromise: registry write-path hardening is a deployment requirement.

### 9.6 Separation of Authority Is Structural, Not Procedural

No single role may simultaneously possess authority over both enforcement and evidence.

---

## 10. Attack Vectors

**Specification substitution** — adversary replaces running specification.
*Defense:* Every Evidence Object includes `spec_hash`. Hash mismatch mechanically detectable against canonical commitment.
*Residual risk:* Multi-system compromise required.

**Runtime specification injection** — adversary writes to specification memory region.
*Defense:* Specification in OS-protected read-only region. Write triggers process abort and gap record.
*Residual risk:* OS-level root compromise can bypass mprotect.

**Context registry poisoning** — adversary modifies registry to produce false evaluation inputs.
*Defense:* Registry writes are witnessed events. Unauthorised writes produce anomalous Evidence Objects.
*Residual risk:* Writes before CVS capture is instrumented for the registry are undetected.

**Bypass path exploitation** — adversary routes proposals around gate.
*Defense:* Execution without corresponding CVS Evidence Object creates detectable evidence absence.
*Residual risk:* Coverage completeness for full execution surface is a deployment responsibility.

**Bypass accumulation** — exceptions accumulate until boundary is irrelevant.
*Defense:* All execution paths, including override paths, **MUST** pass through gate or generate a gap record. Periodic structural audits required.
*Residual risk:* Not detectable from any single evidence chain event — requires pathway audit.

**Evaluation-unavailable exploitation** — adversary induces gate failure to create ungoverned execution windows.
*Defense:* Under the Evaluation-Unavailable DENY doctrine, gate failure produces DENY — the commit path remains closed. Induced gate failure cannot create ungoverned execution windows. Gate high-availability reduces availability of this attack surface.
*Residual risk:* Gate unavailability causes denial of service (legitimate proposals denied) rather than ungoverned execution. HA configuration is the mitigation.

**Intent declaration spoofing** — proposing entity declares benign intent but executes broader scope.
*Defense:* Divergence detectable in CVS evidence chain by comparing pre-validation intent against post-execution actual scope. Execution-layer enforcement is the primary prevention.
*Residual risk:* Prevention requires execution-layer enforcement.

**Constraint specification ambiguity** — constraint has semantic gaps exploitable by adversarial inputs.
*Defense:* Discovery Phase surfaces false negatives before enforcement. Constraint design review is mandatory.
*Residual risk:* Constraint design quality is a human responsibility.

---

## 11. Conformance Requirements

### 11.1 Mandatory Behaviors

A gate implementation satisfying 512's properties exhibits all of the following:

- Position the gate at the commit boundary with no parallel commit paths
- Ensure exactly one path to irreversible state change, not opening without the gate's authorisation signal
- Evaluate all seven invariants on every proposal without exception
- Return binary output only: ALLOW or DENY
- Complete evaluation in median <50μs, p99 <200μs at sustained production throughput
- Produce Evaluation-Unavailable DENY: when the gate is unavailable or evaluation times out, produce DENY (deny_cause: evaluation_unavailable) with failure cause and retry path; commit path remains closed; execution does not proceed
- Emit gap records to the CVS sidecar for all evaluation-unavailable DENY events; persist locally if the sidecar is unavailable; forward on reconnection
- Verify the canonical specification hash at startup and refuse to start on hash mismatch
- Load the specification into a read-only memory region after startup verification
- Emit three CVS observation events per evaluated proposal: pre-validation, validation-result, post-execution
- Emit two CVS records per evaluation-unavailable DENY: deny Evidence Object and CVS sidecar gap record
- Include `spec_hash`, `per_invariant_results`, and `violated_constraint_detail` in every constraint violation DENY validation-result event
- Include `deny_cause`, `failure_cause`, and `retry_permitted` in every evaluation-unavailable DENY validation-result event
- Maintain structural separation of authority from the witness layer
- Disclose the violated invariant identifier and deny message on every constraint violation DENY
- Run in isolation from the execution surface it governs
- Hold specification signing keys in an HSM (FIPS 140-2 Level 2 or higher)
- Instrument and expose latency percentile metrics at all four validation steps
- Instrument and expose evaluation-unavailable DENY event metrics (count, duration, reason)

### 11.2 Prohibited Behaviors

A gate implementation satisfying 512's properties does not exhibit any of the following:

- Return a scored, probabilistic, conditional, or deferred result from gate evaluation
- Block execution when the gate is unavailable without producing Evaluation-Unavailable DENY with disclosed cause and retry path (opaque blocking)
- Open the commit path when the gate is unavailable (ungoverned execution — non-conformant)
- Allow runtime modification of the constraint specification without process restart and hash re-verification
- Accept a specification that does not hash-verify at startup
- Allow the gate process to read from the evidence store
- Allow the CVS process to modify gate configuration or evaluation logic
- Route execution proposals around the gate without generating a gap record
- Evaluate a subset of the seven invariants and claim 512 conformance
- Suppress or discard gap records or evaluation-unavailable DENY records under any condition
- Accept an evaluation-unavailable DENY timeout that exceeds the evaluation latency p99 budget (200μs)
- Position evaluation upstream of a separately operable execution surface
- Route the gate's authorisation signal through an intermediary before it reaches the commit path

### 11.3 Scope of Valid Conformance Claims

- A gate may be described as 512-conformant only if it has passed every test in §11.4
- A gate may be described as satisfying 512's properties only if its specification produces a hash-verified match to `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`
- A gate may not be described as guaranteeing outcomes, preventing all harm, or replacing regulatory audits

### 11.4 Properties Verification Checklist

| Test | Procedure | Pass Condition |
|---|---|---|
| Specification hash match | `sha256sum 512-kernel-padded.txt` | `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |
| Hash mismatch causes startup failure | Start gate with modified spec | Gate refuses to start; logs mismatch |
| Evaluation latency (median) | 10,000 proposals at production throughput | Median <50μs |
| Evaluation latency (p99) | 10,000 proposals at production throughput | p99 <200μs |
| Deterministic evaluation | 1,000 identical proposal pairs | All pairs produce identical output |
| Evaluation-Unavailable DENY on gate failure | Kill gate process mid-evaluation | DENY returned (deny_cause: evaluation_unavailable); commit path remains closed; gap record emitted to CVS sidecar |
| Evaluation-Unavailable DENY on timeout | Inject 200μs+ evaluation delay | DENY returned (deny_cause: evaluation_unavailable); commit path remains closed; gap record emitted to CVS sidecar |
| Gap record contents | Inspect gap record after evaluation-unavailable DENY | Contains proposal_id, agent_id, gap_start, gap_reason, gate_output_during_gap |
| Gap record persistence | Kill CVS queue during gap event | Gap record persisted locally; forwarded on reconnection |
| All 7 invariants evaluated | Unit test each invariant (§3 fixtures) | All 28 fixture tests pass |
| Binary output only | Submit 100 proposals | All responses contain only `ALLOW` or `DENY` |
| Constraint violation DENY includes violated invariant | Submit proposal violating each invariant | Response includes invariant identifier and deny_message |
| Evaluation-unavailable DENY includes failure cause and retry path | Induce gate failure | Response includes failure_cause and retry_permitted: true |
| CVS pre-validation event emitted | Integration test | Evidence Object present for every proposal |
| CVS validation-result event emitted | Integration test | Evidence Object present with spec_hash and per_invariant_results |
| CVS post-execution event emitted | Integration test | Evidence Object present after execution completes (ALLOW only) |
| Separation of authority | IAM audit | Gate has no read access to evidence store |
| Separation of authority | IAM audit | CVS has no access to gate configuration |
| No bypass path exists | Penetration test | All routes to execution surface pass through gate |
| Commit path exclusivity | Penetration test | No route to execution surface bypasses gate authorisation signal |
| Pre-check architecture absent | Structural review | Execution surface not operable independently of gate |
| Specification read-only in memory | Attempt runtime spec write | Process aborts; gap record generated |
| HSM key custody | HSM configuration audit | Signing key never extracted from HSM |
| Latency metrics exposed | Query metrics endpoint | All four step latencies exposed as percentile distributions |
| Gap metrics exposed | Query metrics endpoint | Evaluation-unavailable DENY count, duration, reason exposed |

---

## 12. Constraint Definition Layer (Non-Normative)

### 12.1 The Gate Does Not Define Constraints

Three functions are involved in gate execution. They must remain structurally separate:

| Function | What it does | Who owns it |
|---|---|---|
| **Definition** | Translates policy into executable constraints | The organisation |
| **Expression** | Encodes constraints as deterministic binary logic | The organisation's engineers |
| **Enforcement** | Evaluates constraints against proposals | The gate |

### 12.2 The Constraint Definition Model

Every constraint uses this four-field structure: **Intent** (what is being protected), **Signal** (what data proves the property holds), **Threshold** (the binary condition), **Authority** (the source of truth for the signal).

### 12.3 Binary Reducibility Requirement

| Prohibited term | Why prohibited |
|---|---|
| "reasonable" | Requires judgment |
| "appropriate" | Context-dependent |
| "high risk" | Scoring concept |
| "likely" | Probabilistic |
| "significant" | Requires threshold definition |
| "material" | Legal interpretation required |
| "where feasible" | Introduces conditionality |
| "subject to policy" | Defers definition to runtime |

### 12.4 Determinism Requirement

Identical inputs must produce identical outputs on every invocation, on every machine, at any time.

### 12.5 Common Failure Modes

Vague policy language; hidden assumptions; runtime interpretation; external system dependency at evaluation time; temporal drift.

### 12.6 Anti-Drift Rules for Constraint Definitions

Constraints must be versioned. Each version produces a distinct compiled bundle with a distinct hash. The spec hash must represent the complete active constraint set.

### 12.7 Separation of Constraint Definition and Enforcement

Constraint definition must not leak into runtime. The gate receives a compiled constraint set and evaluates what it is given. This separation is what makes enforcement verifiable.

---

## Conclusion

A Commit Gate satisfying 512's properties is a deterministic function operating at the commit boundary of a machine-speed execution system. It enforces seven pre-committed invariants in 10–50μs. On infrastructure failure, it produces Evaluation-Unavailable DENY — the commit boundary holds unconditionally. It integrates with a witness layer that produces independently verifiable cryptographic records.

The engineering task is straightforward. Find the commit boundary. Insert the gate at that point such that no path to that boundary exists without the gate's authorisation signal. Eliminate parallel paths. Verify the specification hash. Instrument the three CVS observation points. Run Discovery Phase before enforcement. Pass all tests in §11.4.

The constraint being enforced is not invented here. It was found. The gate that enforces it is invented here. The difference between those two things is why the gate implementation is owned by its builder and the constraint it enforces is not.

**Canonical Repository:** github.com/JonathanMastersWatson/512

---

## Document Control

| Field | Value |
|---|---|
| Document | `512_IMPLEMENTATION_v3.3.md` |
| Version | 3.4 |
| Date | June 2026 |
| Author | Jonathan M. Watson |
| Audience | Engineers |
| Status | Active |
| Canonical Repository | github.com/JonathanMastersWatson/512 |
| Specification Commitment | SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |

### Changelog — v3.4

**June 2026 — Evaluation-Unavailable DENY doctrine.**

**Additions:**
- §0 Normative Relationships: `I6_CONSTITUTIONAL_ELABORATION.md` added as a governing canonical document.
- §1.5 Prohibited: opening the commit path on gate unavailability explicitly added to MUST NOT list.
- §1.6 Pattern F: execution on evaluation unavailability added as a named non-conformant pattern.
- §10 Attack Vectors: evaluation-unavailable exploitation attack vector added. Under the revised doctrine, induced gate failure produces DENY rather than ungoverned execution — the attack surface is denial of service, not ungoverned execution windows.
- §11.4: three new test rows added — evaluation-unavailable DENY on gate failure, evaluation-unavailable DENY on timeout (both with commit path closed as pass condition), and evaluation-unavailable DENY includes failure cause and retry path.

**Modifications:**
- Abstract: "fails open" replaced with "produces Evaluation-Unavailable DENY — the commit boundary holds."
- §3.6: section retitled from "Fail-Open" to "Evaluation-Unavailable DENY, Transparent Denial, Human Default." Python implementation rewritten — `evaluate_with_fail_open` returning `('allow', 'gap')` replaced with `evaluate_with_infrastructure_failure_deny` returning `('deny', 'evaluation_unavailable', ...)`. Unit test fixtures updated — expected_execution_result corrected from "allow" to "no execution — commit path remains closed."
- §4.1 sequence diagram: FAIL-OPEN PATH retitled EVALUATION-UNAVAILABLE DENY PATH. Diagram redrawn — "fail-open handler opens commit path" replaced with "infrastructure-failure handler — commit path remains closed." DENY returned to proposing entity. Post-execution annotated "ALLOW only."
- §4.1 Step 4 prose: infrastructure failure clause rewritten — "fail-open handler engages, commit path opens" replaced with "infrastructure-failure handler produces DENY (deny_cause: evaluation_unavailable), commit path remains closed."
- §4.1 Step 4 bullet: "Fail-open" bullet replaced with "DENY (evaluation unavailable)" bullet. Commit path remains closed. DENY includes failure cause and retry_permitted: true.
- §4.2 Latency table: "Fail open; emit gap record" replaced with "Evaluation-Unavailable DENY; emit gap record to CVS sidecar."
- §5.1 Observation Point 2 schema: `deny_cause` field added. `invariant_6_fail_open` renamed to `invariant_6_result`. `failure_cause` and `retry_permitted` fields added for evaluation-unavailable DENY. `violated_constraint_detail` scoped to constraint_violation DENY only.
- §5.3: retitled from "Validation Gap Records" to "Evaluation-Unavailable DENY Records." Gap record schema updated — `executing_identity` field (implied execution proceeded) replaced with `gate_output_during_gap: "deny_evaluation_unavailable"` (confirms execution did not proceed). Deny Evidence Object schema added.
- §7.1 transition checklist: "Fail-open tested under simulated gate failure" replaced with "Evaluation-Unavailable DENY tested under simulated gate failure — commit path confirmed closed."
- §8.4 FPGA: "fail-open behaviour" replaced with "Evaluation-Unavailable DENY in FPGA logic."
- §11.1 Mandatory Behaviors: "Fail open: execution proceeds" replaced with "Produce Evaluation-Unavailable DENY: commit path remains closed, execution does not proceed."
- §11.2 Prohibited Behaviors: "Block execution when gate unavailable (fail-closed behaviour)" replaced with two entries: opaque blocking (DENY without disclosed cause and retry path) and opening the commit path on gate unavailability.
- §11.4 Verification Checklist: fail-open test rows updated — pass condition changed from "Execution continues; gap record generated" to "DENY returned; commit path remains closed; gap record emitted to CVS sidecar."
- Conclusion: "fails open" replaced with "produces Evaluation-Unavailable DENY — the commit boundary holds unconditionally."

**Removals:**
- `evaluate_with_fail_open` function returning `('allow', 'gap')` — removed. Non-conformant under v2.0 doctrine.
- Unit test fixture asserting `expected_execution_result: "allow"` on gate failure — removed. Non-conformant.
- `executing_identity` field from gap record schema — removed. Implied execution proceeded during gap; under revised doctrine execution does not proceed.

---

### Changelog — v3.3

**May 2026 — competitive landscape and priority record cross-references.**

**Additions:**
- §0: `AARM_AND_512.md` and `CANONICAL_COMMITMENT.md` added.

**Modifications:**
- §0: stale reference updated to `512_ARCHITECTURE_v3.4.md`.

**Removals:** Nothing removed.

---

### Changelog — v3.2

**April 2026 — hardening pass.**

**Additions:**
- §0: cross-reference to `LAYER_REFERENCE.md`.

**Modifications:**
- §1.5, §1.6, §4.1, §11.2, §11.4: vocabulary and diagram corrections.

**Removals:** Nothing removed.

---

### Changelog — v3.1

**Modifications:**
- §4.1: GAP removed as gate output value. Fail-open path corrected. Per-invariant results corrected to binary. `overall_result` schema corrected to `allow | deny`.

**Removals:** Nothing removed.

---

### Changelog — v3.0 and prior

See prior version for full changelog history.
