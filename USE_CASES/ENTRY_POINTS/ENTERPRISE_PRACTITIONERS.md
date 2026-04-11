# Entry Point — Enterprise Practitioners

This document is for the Head of AI, CTO, or governance architect
at an organisation deploying agentic workflows at scale.

It answers one question: **what do you need to do to prepare
your agentic workflows for Commit Gate execution?**

It does not cover gate construction, witness layer architecture,
or regulatory interpretation. Those are addressed in separate
documents linked at the end of this file.

---

## What You Are Dealing With

Your agentic systems are making decisions and committing state
changes faster than any human can observe them. An AI agent
processing a customer request, executing a transaction, or
modifying a record operates in microseconds. Human reaction
time is measured in hundreds of milliseconds.

This means your existing governance mechanisms — approval
workflows, audit reviews, compliance dashboards — are not
operating at the point where decisions are made. They are
operating after the fact. They are observing consequences,
not governing decisions.

A Commit Gate moves enforcement to the commit boundary: the
precise moment at which a proposed action becomes an irreversible
state change. Before that moment, the action is a proposal.
After it, the action is a fact. The gate operates at that moment
— in under 50 microseconds — enforcing pre-committed constraints
before state change occurs.

This is not a product your organisation deploys. It is a
constraint that physics imposes on any execution system
operating at machine speed. The question is not whether the
constraint applies to your systems. The question is whether
your systems satisfy it.

---

## What You Need to Prepare

Preparing your agentic workflows for Commit Gate execution
is upstream work. It requires no gate infrastructure. It
requires your organisation to answer seven questions — one
per invariant — about every workflow that will cross a
commit boundary.

The seven invariants your workflows must satisfy:

### Invariant 1 — No Force or Fraud
Your system must not initiate coercive or deceptive actions
against any human party through its autonomous execution.

**What you must have ready:**
- A classification of action types in your system that
  constitute force or fraud in your domain
- A binary condition for each: testable, not interpretive
- Named data sources that the gate will query to evaluate
  each condition

**The question to answer:** For every action your agents
can take, can you state in binary terms whether that action
initiates force or fraud against a human party?

---

### Invariant 2 — Explicit Consent
No execution affecting a human party proceeds without
documented, explicit, prior consent from that party.

**What you must have ready:**
- A consent registry: a system of record holding explicit
  consent tokens for each affected party
- An expiry mechanism: consent has a timestamp after which
  it is no longer current
- A binary condition: `consent_token present AND
  evaluation_timestamp < consent_expiry`

**The question to answer:** For every human party affected
by your agents' actions, do you hold an explicit consent
record — not implied, not inherited, not assumed — that
the gate can verify at evaluation time?

---

### Invariant 3 — Consent Withdrawal
Any party that has given consent may withdraw it. Withdrawal
must propagate to all active execution contexts.

**What you must have ready:**
- A withdrawal mechanism: parties can revoke consent and
  the revocation is recorded immediately
- An epoch mechanism: tokens issued before revocation carry
  a stale epoch; the gate detects epoch mismatch and denies
- A propagation window: a declared time within which
  withdrawal reaches all execution contexts

**The question to answer:** If a customer withdraws consent
at 9:00am, what is the latest time at which your system
could execute against them — and is that window acceptable
and declared?

---

### Invariant 4 — Contractual Clarity
All terms governing an interaction must be explicit, readable
by both parties, and equally enforceable by both parties.

**What you must have ready:**
- A contract registry: machine-readable governing terms for
  each interaction type
- Human-readable versions: terms legible to affected parties
  without specialist interpretation
- Bilateral acknowledgement records: both parties have
  confirmed the terms
- No enforcement asymmetry: both parties hold identical
  enforcement rights under the terms

**The question to answer:** Can the counterparty in any
of your agent-executed interactions read, understand, and
enforce the terms governing that interaction on equal footing
with your organisation?

---

### Invariant 5 — No Hidden Rules
All constraints governing an interaction must be fully
disclosed before execution. Rules may not be changed
unilaterally.

**What you must have ready:**
- A spec hash disclosure mechanism: the active constraint
  set is disclosed to affected parties before enforcement
- An acknowledgement record: parties have confirmed receipt
  of the disclosed hash
- A change protocol: constraint updates require a new hash,
  new disclosure, and renewed consent before the new set
  is enforced

**The question to answer:** Can any affected party
independently verify which constraint set governed their
interaction — and when that set was in force?

---

### Invariant 6 — Fail-Open
When the gate is unavailable, execution continues. The gap
is recorded. Governing rules are disclosed. Control returns
to the human party.

**What you must have ready:**
- A declared fail-open posture: your system does not block
  on gate failure
- Gap record infrastructure: gaps are recorded and forwarded
  to the witness layer even when the gate is unavailable
- Human notification: affected parties are informed when
  execution proceeded without gate evaluation

**The question to answer:** If your gate goes offline at
2am, what happens to your agentic workflows — and does
that behaviour satisfy the fail-open requirement?

---

### Invariant 7 — Immutability and Binary Satisfaction
The constraint set is fixed. Adherence is binary. All seven
invariants are evaluated on every proposal. There is no
partial satisfaction.

**What you must have ready:**
- Hash verification at startup: the gate confirms the
  canonical hash before accepting any proposals
- No runtime modification: constraint changes require a
  gate restart with a new specification
- Full evaluation: all seven invariants are evaluated on
  every proposal without exception

**The question to answer:** Is your constraint set fixed,
versioned, and hash-verified — or does it change based
on context, configuration, or runtime conditions?

---

## The Four Things You Must Produce

Before any gate evaluation begins, your organisation must
produce four things for each agentic workflow:

**1. A boundary map**
Every point in your system where a proposed action becomes
an irreversible state change. Every boundary on this map
requires gate evaluation. A boundary not on this map is
an uncontrolled execution path.

**2. A parallel path audit**
Confirmation that exactly one path reaches each commit
boundary — through gate evaluation. Every administrative
override, emergency path, and direct execution surface
access that bypasses the gate must be structurally
eliminated before enforcement begins.

**3. Proposal Objects**
A defined schema for each commit boundary, populated from
real system data. Every field answered from live data —
not assumed, inferred, or carried forward.

**4. Executable constraints**
A binary condition for each invariant at each commit
boundary, expressed over named, typed inputs with declared
data sources. Vague policy language does not pass this
stage.

See `512-ops/INTEGRATION_STEPS.md` for the step-by-step
workflow that produces these four outputs.

---

## The Entry Point for Your Organisation

Start in observation mode.

Observation mode evaluates all seven invariants at every
boundary crossing without blocking any execution. All results
are recorded: ALLOW, DENY, GAP. No operational disruption.

Observation mode surfaces three things before enforcement
begins:

- **Unexpected DENY results** — constraints firing on
  legitimate requests, indicating constraint definitions
  that need refinement
- **GAP results** — evaluation failures indicating missing
  input data or integration gaps
- **Coverage gaps** — execution events with no evaluation
  record, indicating missed boundaries or parallel paths

Your organisation should run in observation mode until
the record is clean. Only then should enforcement be enabled.

This is the correct enterprise entry point. It allows your
governance and engineering teams to verify that your systems
satisfy 512's properties before any execution is blocked.

---

## Common Enterprise Failure Modes

**"We already have governance."**
Post-execution audit, approval workflows, and compliance
dashboards operate after the commit boundary. They record
what happened. They do not govern what happens. At machine
speed, by the time any of these mechanisms activate, the
action is a fact. Governance that cannot reach the commit
boundary is not governing execution — it is documenting it.

**"Our policies cover this."**
Policies written in natural language require interpretation.
The gate does not interpret. Policies must be translated into
binary conditions over named, typed inputs before they can
be enforced at the commit boundary. Translation is the
organisation's responsibility — and it frequently reveals
that policies contain assumptions that cannot be expressed
as executable logic.

**"We have an audit trail."**
Internal logs are mutable, selectively preserved, and subject
to administrator access. They are assertions, not independent
proof. A cryptographically hash-chained, WORM-stored, publicly
anchored evidence record is proof. The difference matters when
disputes demand independent verification.

**"We'll add the gate later."**
Every day your agentic systems operate without a commit
boundary is a day that cannot be reconstructed with
cryptographic certainty. The evidentiary gap does not
close retroactively. Disputes arising from actions taken
during unwitnessed periods are resolved through weaker
means — internal logs, testimony, forensic reconstruction —
with correspondingly weaker outcomes.

---

## Where to Go Next

| What you need | Where to find it |
|---|---|
| Step-by-step integration workflow | `512-ops/INTEGRATION_STEPS.md` |
| How to define executable constraints | `512-ops/CONSTRAINT_DEFINITION_LAYER.md` |
| Boundary mechanics and Proposal Object | `512-ops/COMMIT_BOUNDARY_REFERENCE.md` |
| End-to-end sequence from intent to evidence | `512-ops/REFERENCE_FLOW.md` |
| Go-live verification checklist | `512-ops/PROPERTIES_CHECKLIST.md` |
| What 512 is and why physics forces it | `512_ARCHITECTURE` |
| How the gate is built | `512_IMPLEMENTATION` |
| How the witness layer works | `CVS_ARCHITECTURE` |
| How implementations drift and how to prevent it | `ANTI_DRIFT.md` |
