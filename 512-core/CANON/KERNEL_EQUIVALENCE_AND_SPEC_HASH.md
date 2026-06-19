# Kernel Equivalence & Spec-Hash (512)

512 cannot require word-for-word sameness.

512 must require **semantic sameness**.

This file defines how semantic sameness is recognised without creating an authority.

---

## Terms

**Kernel text**
The human-readable 7 constraints.

**Invariant**
A meaning-bearing constraint that must not change.

**IR (Intermediate Representation)**
A minimal structured form of the kernel: a list of invariants expressed as atomic rules.

**Spec-hash**
A hash of the canonical IR (not the prose).
If two kernels produce the same canonical IR, they share the same spec-hash.

**Interpreter**
A compiler-like process (human or machine) that maps prose to IR.

---

## Non-goals

This file does not:

- create an official interpretation
- grant enforcement power
- define remedies or penalties
- define identity, jurisdiction, or governance
- decide intent

It defines only: **equivalent or not equivalent**.

---

## What "equivalent" means

A kernel instance is **equivalent** to 512 if and only if:

1) it compiles to the same invariant set as the canonical kernel, and
2) it does not add, remove, weaken, conditionalize, or re-scope any invariant.

Format, sequence, and wording may differ.

Meaning may not.

---

## Canonical Invariants (IR Targets)

The kernel compiles to exactly these seven invariants:

**I1 — No Force or Fraud**
No agent may initiate force or fraud against any human.

**I2 — Voluntary Interaction**
All interactions must be voluntary and based on explicit consent.

**I3 — Consent Withdrawal and Exit**
Consent may be withdrawn. Exit must always be possible.

**I4 — Contractual Clarity**
All contracts must be explicit, readable, and equally enforceable by all parties.

**I5 — No Hidden or Unilateral Rules**
No rules governing interaction may be hidden or unilaterally changed.

**I6 — Continuity Behaviour / Transparent Denial / Human Default**
On failure, systems must fail open, reveal governing rules, and default to human choice.

**I7 — Immutability and Binary Satisfaction**
The kernel is immutable. Satisfaction is binary.

Notes:
- These seven invariants are the complete target.
- Prose is an interface, not the authority.
- The kernel text governs where any conflict exists between prose and invariant.
- The authoritative elaboration of I6 is `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`.

---

## Canonical IR Form (Normalization)

To compare kernels, interpreters must normalize into a canonical IR form.

Minimum requirements:

- Each invariant is represented as a single atomic rule.
- Modal verbs normalize to MUST / MUST NOT.
- Subjects normalize to AGENT / SYSTEM / PARTY / HUMAN.
- "Force or fraud" must remain a prohibition on initiation (not a preference,
  guideline, or policy goal).
- "Exit" must remain unconditional (not "reasonable efforts," not "where
  feasible," not "subject to policy").
- "Fail open" must remain bounded to gate unavailability behaviour — the gate
  produces no output; the continuity handler opens the commit path; the gap is
  recorded. "Reveal governing rules" must remain a disclosure obligation on DENY
  — not "fail safe," not "quiet degrade," not "fallback to authority." "Default
  to human choice" must remain an unconditional sovereignty guarantee — not
  "subject to policy," not "where feasible." All three are distinct obligations.
  See `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`.
- "Consent withdrawal" and "exit" must remain as two distinct conditions within
  I3 — neither may be dropped or merged into the other.
- "Immutability" and "binary satisfaction" must remain as two distinct conditions
  within I7 — neither may be treated as optional.

Normalization is not interpretation. It is formatting of meaning.

---

## Spec-Hash Definition

The **SPEC_HASH** is computed from canonical IR, not the kernel text.

Definition:

1) Parse candidate kernel prose into IR invariants (I1–I7).
2) Normalize IR into canonical form.
3) Serialize canonical IR deterministically (stable ordering).
4) Hash the serialization to obtain SPEC_HASH.

Result:
- Different wordings can share the same SPEC_HASH.
- Any semantic mutation changes SPEC_HASH.

SPEC_HASH is an identity for meaning, not authorship.

---

## Multi-Interpreter Consensus (Recommended)

Single interpreters can drift.

For high-stakes use, equivalence should be evaluated by multiple independent
interpreters.

Process:

- Run N interpreters (different prompts, models, vendors, or humans).
- Each outputs:
  - Canonical IR serialization
  - SPEC_HASH
  - Per-invariant confidence
  - A diff report if uncertain

Decision:

- **PASS** only if interpreters converge on identical canonical IR and SPEC_HASH.
- **HUMAN DEFAULT** on disagreement: surface the disagreement and default to
  user choice / non-action.

This does not create authority.
It reduces single-point semantic failure.

---

## Failure Mode: "Looks Equivalent" Drift

The primary attack on 512 is micro-mutation that appears equivalent.

Typical drifts (non-exhaustive):

- MUST NOT → SHOULD NOT
- "initiate" → "avoid"
- "any human" → "authorized humans" / "lawful persons" / "participants"
- "exit always possible" → "where feasible" / "reasonable notice" / "subject to policy"
- "no unilateral change" → "may update with notice"
- "fail open" → "fail safe" / "silent fallback" / "contact support" / "domain-configurable"
- "reveal governing rules" → omitted, merged with fail open, or reduced to logging
- "default to human choice" → "subject to policy" / "where feasible" / "at operator discretion"
- splitting I3 to drop either consent withdrawal or exit
- splitting I7 to treat binary satisfaction as optional
- adding an enforcer, court, council, registry, or scoring system

Any drift that changes invariants changes SPEC_HASH.

---

## Required Repository Practice

- The kernel text remains stable and separately referenced.
- This file may evolve to improve the comparison method.
- No update to this file may redefine the invariants themselves.
- The invariant count is seven. Any update that produces a different count
  has introduced drift.

---

## Summary

512 is portable only if equivalence is mechanical.

Prose can vary.
Invariants cannot.

SPEC_HASH binds meaning.
Multi-interpreter consensus hardens the edge.

Ambiguity fails open to Human Default.
