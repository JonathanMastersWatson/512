# Integration Steps

This document defines the steps an organisation takes to integrate
an agentic workflow with a Commit Gate satisfying 512's properties.

Work through these steps in order. Each step is a prerequisite for
the next. Do not proceed to enforcement mode until all steps are
complete and verified.

---

## Step 1 — Identify Your Commit Boundaries

Find every point in your system where a proposed action becomes
an irreversible state change.

A commit boundary is not:
- the moment a user submits a request
- the moment an agent produces an output
- the moment a decision is logged

A commit boundary is:
- the moment a financial transaction finalises
- the moment a record is written that another party relies on
- the moment an obligation is created that cannot be undone
- the moment a communication is sent that cannot be recalled

**Output:** A documented list of every commit boundary in your
system, mapped to the specific execution event that crosses it.

Every boundary on this list requires gate evaluation. A boundary
not on this list is an uncontrolled execution path.

---

## Step 2 — Audit for Parallel Execution Paths

For each commit boundary identified in Step 1, identify every
route that can reach it.

Common parallel paths that must be found and eliminated:

- administrative API endpoints that write directly to the
  execution surface
- emergency override mechanisms that skip evaluation
- direct database write access held by non-gate service accounts
- background jobs or scheduled tasks that commit state without
  passing through the gate
- internal tooling or scripts used by engineering or operations teams

**Output:** For each boundary, a confirmed statement that exactly
one path reaches it — through gate evaluation — or a list of
parallel paths requiring structural elimination before proceeding.

Procedural controls (access policies, documented prohibitions)
do not satisfy this step. The parallel paths must not exist.

---

## Step 3 — Build Your Proposal Objects

For each commit boundary, define the Proposal Object that will
be evaluated at that boundary.

A Proposal Object answers seven questions before the boundary
is crossed:

| Field | Question |
|---|---|
| `action` | What is being proposed? |
| `proposing_party` | Who is proposing it? |
| `affected_parties` | Who does it affect? |
| `consent_evidence` | Is consent explicit and current? |
| `contract_reference` | What terms govern this? |
| `exit_available` | Can any party still exit? |
| `rules_disclosed` | Are all governing rules visible? |

**Output:** A defined Proposal Object schema for each commit
boundary. Every field must be populated from real system data —
not assumed, inferred, or carried forward from a prior action.

See `512-ops/COMMIT_BOUNDARY_REFERENCE.md §2` for the full
Proposal Object specification.

---

## Step 4 — Define Your Constraints

Translate your policies into executable constraints.

This step occurs upstream of the gate. The gate does not define
constraints. The gate evaluates them. Constraint definition is
your responsibility.

For each invariant, define the specific binary condition your
system will evaluate:

| Invariant | What you must define |
|---|---|
| I1 — No force or fraud | What constitutes a coercive or deceptive action in your domain |
| I2 — Explicit consent | Where consent records live and how currency is verified |
| I3 — Consent withdrawal | How withdrawal propagates and within what time window |
| I4 — Contractual clarity | Which contract governs each action and how readability is confirmed |
| I5 — No hidden rules | How the active constraint set is disclosed and to whom |
| I6 — Fail-open | What your system does when the gate is unavailable |
| I7 — Immutability | How the canonical hash is verified at startup |

**Each constraint must be reducible to a binary condition.**
Vague policy language does not pass this step.

- ❌ "transactions must not be high risk"
- ✅ "transaction value must not exceed counterparty_exposure_limit"

- ❌ "consent must be reasonably current"
- ✅ "consent_expiry timestamp must be greater than evaluation_timestamp"

**Output:** A constraint definition for each invariant at each
commit boundary, expressed as a testable binary condition with
a named data source for each input.

See `512-ops/CONSTRAINT_DEFINITION_LAYER.md` for the full
constraint definition model and failure mode reference.

---

## Step 5 — Run in Observation Mode

Before enabling enforcement, operate the gate in observation mode.

In observation mode:
- all seven invariants are evaluated at every boundary crossing
- no execution is blocked
- all results are recorded: ALLOW / DENY / GAP

Observation mode surfaces three categories of problem:

**Unexpected DENY results** — constraints that fire on legitimate
requests. These indicate constraint definitions that are too narrow
or input data that is not being assembled correctly.

**GAP results** — evaluation failures caused by missing input data,
registry unavailability, or timeout. These indicate integration
gaps that must be resolved before enforcement.

**Coverage gaps** — execution events that do not produce any
evaluation record. These indicate commit boundaries that were
missed in Step 1 or parallel paths that were missed in Step 2.

**Output:** An observation period of sufficient duration to capture
a representative sample of your execution traffic, with a resolution
log showing how each DENY and GAP was addressed.

Do not proceed to Step 6 until the observation record is clean:
no unexpected DENYs, no unresolved GAPs, no uncovered boundaries.

---

## Step 6 — Enable Enforcement

Switch the gate from observation mode to enforcement mode.

At this point:
- ALLOW results open the commit path
- DENY results close the commit path and record the violated invariant
- GAP results open the commit path under fail-open and record the gap

No constraint changes are required between observation and
enforcement mode. Only the enforcement posture changes.

**Confirm before switching:**

- [ ] All commit boundaries are covered
- [ ] No parallel execution paths exist
- [ ] All Proposal Object fields are populated from live data
- [ ] All constraints produce expected results against test inputs
- [ ] Observation period is complete with no unresolved issues
- [ ] Gate specification hash matches canonical commitment:
      `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`
- [ ] Witness layer is capturing all three observation points
- [ ] Gap records are being forwarded and stored

---

## Step 7 — Verify the Evidence Chain

After enforcement is live, verify that the evidence chain is
operating correctly.

For a sample of recent ALLOW results, confirm:
- a pre-validation evidence record exists for each proposal
- a validation-result evidence record exists, containing the
  spec hash and per-invariant results
- a post-execution evidence record exists, with the actual
  execution outcome
- the three records are linked by a common correlation ID
- evidence is anchored to the public ledger within the
  declared anchoring window

For a sample of DENY results, confirm:
- the denial record identifies the specific violated invariant
- the deny message is present and human-readable

For any GAP records, confirm:
- the gap duration and reason are recorded
- all executions during the gap window are identifiable

**Output:** A verified evidence chain sample confirming that
enforcement records are complete, linked, and anchored.

---

## Quick Reference

| Step | What you produce | Gate dependency |
|---|---|---|
| 1 — Identify boundaries | Boundary map | None |
| 2 — Audit parallel paths | Structural elimination confirmation | None |
| 3 — Build Proposal Objects | Proposal Object schema per boundary | None |
| 4 — Define constraints | Binary constraint per invariant | None |
| 5 — Observation mode | Clean observation record | Gate live, enforcement off |
| 6 — Enable enforcement | Confirmed pre-enforcement checklist | Gate live, enforcement on |
| 7 — Verify evidence chain | Verified evidence sample | Witness layer live |

Steps 1–4 are upstream preparation. They require no gate
infrastructure. Complete them before any gate is built or deployed.

---

## Related Files

- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — boundary mechanics,
  Proposal Object, non-conformant patterns
- `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — constraint definition
  model, failure modes, binary reducibility requirement
- `512-ops/REFERENCE_FLOW.md` — end-to-end sequence from intent
  to anchored evidence
- `512-ops/PROPERTIES_CHECKLIST.md` — go-live verification checklist
- `512-core/KERNEL/INVARIANTS.md` — the seven invariants defined precisely
- `ANTI_DRIFT.md` — how implementations drift from 512's properties
