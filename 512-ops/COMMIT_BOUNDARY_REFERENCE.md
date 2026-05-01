# Commit Boundary Reference

This document is a developer reference for building systems that
satisfy 512's properties at the execution boundary.

It answers four questions:
1. Where is the boundary?
2. What crosses it?
3. What gets evaluated?
4. What comes out?

No philosophy. No history. Start here, build from here.

---

## 1. Where Is the Boundary?

The commit boundary is the exact point at which a proposed action
becomes an irreversible state change.

Before the boundary: the action is a proposal. It can be modified,
withdrawn, or cancelled. Nothing is committed.

After the boundary: the action is a fact. State has changed.
Reversal requires a new action with its own boundary crossing.

**The boundary is not:**
- the moment a user clicks a button
- the moment a request hits an API
- the moment a decision is logged
- the moment an AI model outputs a result

**The boundary is:**
- the moment state becomes irreversible
- the moment an obligation is created that another party relies on
- the moment a transfer of ownership, authority, or rights completes
- the moment a payment finalises

If reversal would impose harm on another party or create enforceable
obligations — that is the boundary.

---

## 2. What Crosses the Boundary — The Proposal Object

Every action that crosses the boundary is represented as a
**Proposal Object** before evaluation begins.

A Proposal Object answers:

| Field | Question | Notes |
|---|---|---|
| `action` | What is being proposed? | Human-readable description |
| `proposing_party` | Who is proposing it? | Identifiable party |
| `affected_parties` | Who does it affect? | All parties, not just initiator |
| `consent_evidence` | Is consent explicit and current? | Not assumed, not inherited |
| `contract_reference` | What terms govern this? | Must be explicit and readable |
| `exit_available` | Can any party still exit? | Must be true before boundary |
| `rules_disclosed` | Are all governing rules visible? | No hidden rules permitted |
| `spec_hash` | Which constraint set is active? | Hash of the declared constraints |
| `timestamp` | When is this proposed? | Before boundary crossing |

The Proposal Object is constructed **before** the boundary is crossed.
It is not reconstructed after the fact.

---

## 3. What Gets Evaluated — The Seven Invariants

Each Proposal Object is evaluated against all seven invariants.
Evaluation is per-invariant. All seven must be satisfied.
There is no weighting, scoring, or partial credit.

### I1 — No Force or Fraud
**Check:** Does this action initiate force or fraud against any human?

Force: physical coercion, digital coercion, economic coercion
through undisclosed constraints.

Fraud: misrepresentation, omission of material facts, deceptive
interface or system behaviour.

**Pass:** No force or fraud is initiated.
**Fail:** Any force or fraud is present.

---

### I2 — Voluntary Interaction
**Check:** Is this interaction voluntary and based on explicit consent?

Consent must be explicit. Silence is not consent.
Assumed consent is not consent.

**Pass:** Explicit consent is present and current.
**Fail:** Consent is absent, assumed, or inherited from a prior action.

---

### I3 — Consent Withdrawal and Exit
**Check:** Can consent be withdrawn? Can any party exit?

These are two separate checks.

Withdrawal: the proposing party and affected parties can revoke
consent before the boundary is crossed.

Exit: departure from the system, interaction, or obligation remains
structurally possible. Exit that requires permission from the system
being exited fails this invariant.

**Pass:** Both withdrawal and exit are structurally available.
**Fail:** Either withdrawal or exit is blocked, costly, or requires
permission from the system.

---

### I4 — Contractual Clarity
**Check:** Are the governing terms explicit, readable, and equally
enforceable by all parties?

Three sub-checks:
- Explicit: terms are stated, not implied
- Readable: legible to affected parties without specialist interpretation
- Equally enforceable: all parties hold identical enforcement rights

**Pass:** All three sub-checks pass.
**Fail:** Any term is hidden, unreadable, or asymmetrically enforceable.

---

### I5 — No Hidden or Unilateral Rules
**Check:** Are all governing rules visible? Have any been changed
unilaterally?

All rules affecting this action must be visible and inspectable
before the boundary is crossed.

Unilateral change: rules changed by one party without the knowledge
and exit opportunity of all affected parties fail this invariant.

**Pass:** All rules are disclosed and unchanged since last consent.
**Fail:** Any rule is hidden, or any rule changed without disclosure
and exit opportunity.

---

### I6 — Fail-Open
**Check:** If this system fails at or after this boundary, will it
fail open?

Fail-open means:
- default to least restrictive state
- reveal governing rules
- return control to the human party

**Pass:** Failure mode is structurally fail-open.
**Fail:** Failure mode is fail-closed, silent, or increases system
control over the human party.

---

### I7 — Immutability and Binary Satisfaction
**Check:** Is the constraint set immutable? Is evaluation binary?

The constraint set in force at evaluation must be the canonical
512 kernel — unmodified, referenced by hash.

Satisfaction is binary per invariant. No scoring. No partial credit.

**Pass:** Constraint set matches canonical hash. All seven invariants
evaluated. Each produces pass or fail.
**Fail:** Constraint set is modified. Any invariant is skipped.
Any invariant produces a non-binary output.

---

## 4. What Comes Out — Gate Outputs

The gate is binary. Every completed evaluation produces exactly
one of two outputs: ALLOW or DENY. There is no third output value.

### ALLOW
All seven invariants are satisfied.
The action may cross the boundary and become irreversible state change.

### DENY
One or more invariants are not satisfied.
The action does not cross the boundary.
State does not change.
The denial is recorded with the specific invariant(s) that failed.

---

## 4.1 Fail-Open — When the Gate Cannot Evaluate

Fail-open is not a gate output. It is a system behaviour that
engages when the gate cannot complete evaluation.

When the gate is unavailable or evaluation times out:

- the gate produces **no output** — evaluation did not complete
- execution proceeds because Invariant 6 requires fail-open behaviour;
  blocking execution on gate failure would itself be a violation
- the fail-open handler emits a **gap record** to the witness layer
- the witness layer records the ungoverned period as an evidence
  chain gap — not an ALLOW, not a DENY

**A gap record is not an ALLOW.** Constraint satisfaction was not
established. Execution proceeded because availability is prioritised
over blocking — not because the constraints passed.

**Silent execution — proceeding without a gate output and without
a gap record — is non-satisfaction of 512's properties.**

---

## 5. What Gets Anchored to XRPL

Every gate evaluation produces ALLOW or DENY and generates a witness
record. Fail-open events produce no gate output but generate a witness
layer gap record. The witness layer batches these records and anchors
a Merkle root to the XRP Ledger on a fixed interval (every 30 seconds
under standard configuration).

| Event | What is anchored |
|---|---|
| ALLOW | Hash of Proposal Object, per-invariant results, spec hash, timestamp, execution outcome |
| DENY | Hash of Proposal Object, per-invariant results, violated invariant identifier, spec hash, timestamp |
| Fail-open (gap record) | Gap duration, gap reason, executing identity during gap window, spec hash, timestamp |

**What is never anchored:**
- private data
- personal information
- content of contracts
- identity information beyond what is required for consent evidence

The ledger records proof of evaluation. It does not record content.
DENY and gap records are anchored with the same integrity guarantees
as ALLOW records. A DENY is not a lesser event — it is evidence that
the constraint enforced correctly. A gap record is not a lesser event
— it is evidence that evaluation did not occur and execution proceeded
under fail-open.

**Why XRPL:**
- Deterministic finality
- Low, predictable transaction cost (~$0.000025 per transaction)
- Public auditability — no operator cooperation required to verify
- Conservative protocol governance
- Long-term operational stability

XRPL is used as a neutral public witness. It is not used to execute
rules, enforce behaviour, store documents, or manage identities.

---

## 6. Canonical Kernel Reference

**Kernel text:**
No agent may initiate force or fraud against any human.
All interactions must be voluntary and based on explicit consent.
Consent may be withdrawn. Exit must always be possible.
All contracts must be explicit, readable, and equally enforceable
by all parties.
No rules governing interaction may be hidden or unilaterally changed.
On failure, systems must fail open, reveal governing rules, and
default to human choice.
The kernel is immutable. Adherence is binary.

**Canonical artifact:** `512-core/KERNEL/512-kernel-padded.txt`
**Encoding:** UTF-8, no BOM, exactly 512 bytes
**SHA-256:** `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

**XRPL anchor transaction:**
`378536A3CB75DECF90B6AE57F75292BDFF716285B01946870CAC158F8152D100`

---

## 7. Quick Reference

| Concept | Answer |
|---|---|
| Where is the boundary? | Point of irreversible state change |
| What is a Proposal Object? | Structured record of a proposed action, built before boundary |
| How many invariants? | Seven — all must be satisfied |
| What are the gate outputs? | ALLOW or DENY — binary, always |
| What is fail-open? | System behaviour when gate cannot evaluate — not a gate output; witness layer records a gap |
| What gets anchored? | Hashes only — no private data |
| Why XRPL? | Public, final, cheap, no operator trust required |
| Is partial satisfaction valid? | No. Binary. All seven or none. |
| Can I build my own witness layer? | Yes. The witness layer is external to 512. |
| Is a pre-check architecture conformant? | No. See §9. |
| Can execution proceed via a parallel path? | No. See §8. |

---

## 8. Commit Path Ownership

There exists exactly one path to irreversible state change.
That path does not open without a passing evaluation result.

This is not a recommendation. It is a structural requirement.

The commit boundary must be the gate on the commit path — not a
check that runs before an independently operable execution surface.
A system where the execution surface can be reached without passing
through evaluation does not satisfy 512's properties, regardless of
how rarely that path is used.

**The conformant model:**
[upstream systems]
|
v
[evaluation at commit boundary]
|
v
[irreversible state change]

- no alternate path exists
- no reinterpretation occurs between evaluation and commit
- no execution proceeds outside this path under any operational mode

**Procedural controls do not satisfy this requirement.**
Access policies, documentation, and contractual prohibitions on
bypass are not structural controls. The absence of any reachable
path to the execution surface that bypasses evaluation is the
requirement.

**The existence of a bypass path — not its frequency of use —
is the disqualifying condition.**

---

## 9. Non-Conformant Patterns

The following patterns do not satisfy 512's properties.
Each introduces a structural separation between evaluation and
the commit boundary, creating a path to irreversible state change
that is not controlled by the evaluation result.

---

**❌ Pattern A — Evaluation result handed off to an API layer**
[evaluation] → [API call] → [DB write]
The DB write is reachable independently of evaluation.
The evaluation result is advisory to the API layer.

---

**❌ Pattern B — Evaluation result handed off to a queue**
[evaluation] → [message queue] → [worker executes]
The worker can consume from sources other than the evaluation path.
The queue is an independently operable execution surface.

---

**❌ Pattern C — Evaluation result handed off to a broker**
[evaluation] → [broker] → [runtime applies decision]
The broker reintroduces an interpretation layer.
The runtime may apply the decision differently from the evaluation output.

---

**❌ Pattern D — Pre-check positioning**
[evaluation check] → [execution layer]
Decision and execution are structurally separate.
The execution layer is operable without the evaluation result.
This is the most common misinterpretation of 512's boundary model.

---

**❌ Pattern E — Parallel or fallback execution path**
[evaluation]
|
+──► [primary execution path]
|
+──► [fallback / override / admin path]
Any path that reaches the execution surface without evaluation
is a bypass. The existence of the path is the disqualifying
condition — not whether it is used.

---

**The only conformant model:**
[upstream systems]
|
v
[evaluation at commit boundary]
|
v
[irreversible state change]

---

## Related Files

- `512-core/KERNEL/INVARIANTS.md` — full invariant definitions
- `512-core/KERNEL/512-kernel.txt.txt` — canonical kernel text
- `512-core/CANON/KERNEL_EQUIVALENCE_AND_SPEC_HASH.md` — SPEC_HASH mechanism
- `512-interface/BLOCKCHAIN/COMMIT_BOUNDARY.md` — boundary mechanics detail
- `512-interface/BLOCKCHAIN/WHY_XRPL.md` — ledger selection rationale
- `ANTI_DRIFT.md` — how implementations drift from 512's properties
- `512-ops/CONSTRAINT_DEFINITION_LAYER.md` — upstream constraint definition
- `512-ops/INTEGRATION_STEPS.md` — end-to-end integration workflow
