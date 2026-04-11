# Properties Checklist

This checklist defines the minimum observable properties a system
must exhibit to satisfy 512's constraints at the execution boundary.

Satisfaction is binary. A system that does not exhibit all properties
does not satisfy 512's properties — regardless of naming, intent,
or documentation.

This checklist is a go-live verification instrument, not a
certification document. Passing this checklist does not constitute
regulatory certification, legal sufficiency, or insurance coverage.

---

## Pre-Enforcement Checklist

Complete this checklist before switching from observation mode
to enforcement mode. Every item must be confirmed. There is no
partial passage.

### Boundary and Path Properties

- [ ] Every commit boundary in the system is identified and
      documented — the point at which each proposed action
      becomes an irreversible state change

- [ ] Exactly one path reaches each commit boundary — through
      gate evaluation. No parallel paths, admin overrides,
      emergency routes, or direct execution surface access
      exists without generating a gap record

- [ ] Structural elimination of bypass paths is confirmed —
      not procedural restriction. The paths must not exist,
      not merely be restricted by policy or access control

- [ ] The gate's authorisation signal is the structural
      prerequisite for the commit path to open — not a
      prior check, not advisory input to an independently
      operable execution surface

### Proposal Object Properties

- [ ] A Proposal Object schema is defined for each commit
      boundary

- [ ] Every field in every Proposal Object is populated from
      live system data — not assumed, inferred, or carried
      forward from a prior action

- [ ] The `spec_hash` field in every Proposal Object matches
      the canonical commitment:
      `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

### Constraint Properties

- [ ] A binary constraint is defined for each invariant at
      each commit boundary

- [ ] Every constraint is expressed as a deterministic Boolean
      over named, typed inputs with declared data sources

- [ ] No constraint contains prohibited language: reasonable,
      appropriate, high risk, likely, significant, material,
      where feasible, subject to policy

- [ ] Every constraint input has a named source system and
      is pre-fetched during context binding — no external
      I/O occurs during constraint evaluation

- [ ] The compiled constraint bundle hash has been computed
      and committed to the specification file

- [ ] The active spec hash has been disclosed to all affected
      parties and acknowledgement has been recorded

### Evaluation Properties

- [ ] All seven invariants are evaluated on every proposal
      without exception — no selective evaluation, no skipped
      invariants

- [ ] Evaluation produces exactly three output values:
      ALLOW, DENY, or GAP. No scored, probabilistic,
      conditional, or deferred outputs are produced

- [ ] Median evaluation latency is below 50μs at sustained
      production throughput — verified by load test

- [ ] 99th percentile evaluation latency is below 200μs —
      verified by load test

- [ ] The gate verifies the canonical specification hash at
      startup and refuses to start on hash mismatch

- [ ] The specification is loaded into read-only memory after
      startup verification — no runtime modification is possible

### Fail-Open Properties

- [ ] The gate fails open when unavailable — execution
      continues; execution is never blocked by gate failure

- [ ] Gap records are generated for all fail-open events

- [ ] Gap records are forwarded to the witness layer and
      persisted locally if the witness layer is unavailable

- [ ] Gap records identify the gap duration, reason, and
      the executing identity during the gap window

### Witness Layer Properties

- [ ] The witness layer captures all three observation points
      for every evaluation: pre-validation, validation-result,
      post-execution

- [ ] Every validation-result event contains: overall result,
      spec hash, per-invariant results, violated constraint
      detail (on DENY), and evaluation duration

- [ ] The three observation point events for each proposal
      are linked by a common correlation ID

- [ ] Evidence Objects are hash-chained — each includes the
      hash of the prior Evidence Object

- [ ] Evidence is stored in WORM-compliant append-only storage

- [ ] Evidence is anchored to the public ledger within the
      declared anchoring window

- [ ] The gate does not have read access to the evidence store

- [ ] The witness layer does not have access to gate
      configuration, constraint specifications, or evaluation
      logic

### Authority Separation Properties

- [ ] The gate process runs in isolation from the execution
      surface: separate process, separate OS user, no shared
      memory

- [ ] No single operator account holds both gate administrative
      access and evidence store access

- [ ] Specification signing keys are held in an HSM at
      FIPS 140-2 Level 2 or higher

---

## Post-Enforcement Verification

Run this verification after enforcement has been live for a
representative period.

### Evidence Chain Verification

- [ ] For a sample of ALLOW results: confirm a pre-validation,
      validation-result, and post-execution record exists for
      each, linked by correlation ID

- [ ] For a sample of DENY results: confirm the denial record
      identifies the specific violated invariant and includes
      the deny message

- [ ] For any GAP records: confirm the gap duration, reason,
      and executing identity during the gap window are recorded

- [ ] Evidence anchoring is confirmed against the public ledger
      for the sample period — Merkle roots are present and
      Evidence Objects validate against them

### Bypass Path Verification

- [ ] Penetration test confirms no path to the execution
      surface exists without gate evaluation or a gap record

- [ ] All execution events in the sample period have a
      corresponding pre-validation Evidence Object — no
      execution without a witness record

### Specification Integrity Verification

- [ ] The spec hash recorded in witness Evidence Objects
      matches the canonical commitment:
      `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

- [ ] The disclosed spec hash matches the hash in Evidence
      Objects — no divergence between what parties were shown
      and what was evaluated

---

## What This Checklist Does Not Cover

This checklist does not address:

- correctness of upstream constraint definitions — whether
  constraints capture the right policy is a design question,
  not a properties question
- regulatory or legal sufficiency in any jurisdiction
- insurance underwriting requirements
- witness layer construction
- gate construction

Those are outside 512's scope or addressed in separate documents.

---

## Related Files

- `512-ops/INTEGRATION_STEPS.md` — the step-by-step workflow
  that produces the outputs this checklist verifies
- `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — constraint
  definition requirements
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — boundary mechanics
  and non-conformant patterns
- `512-ops/REFERENCE_FLOW.md` — end-to-end sequence this
  checklist verifies against
- `ANTI_DRIFT.md` — drift patterns this checklist guards against
