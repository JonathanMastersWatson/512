# Invariants of the 512 Kernel

This document defines the seven invariants expressed by the 512 Kernel.

The kernel text is the authority. This document maps each kernel
statement to its precise meaning. Where any conflict exists between
this document and the kernel text, the kernel text governs.

An invariant is a condition that holds at every execution boundary.
If an invariant is not satisfied, the system does not exhibit
512's properties.

These invariants are descriptive, not aspirational.
They describe constraints, not outcomes.

---

## Invariant 1 — No Force or Fraud

**Kernel statement:**
> No agent may initiate force or fraud against any human.

Force includes physical coercion, digital coercion, and economic
coercion through undisclosed constraints.

Fraud includes misrepresentation, omission of material facts,
and deceptive interface or system behaviour.

This invariant applies to agents, systems, and automated processes
acting on behalf of any party.

---

## Invariant 2 — Voluntary Interaction

**Kernel statement:**
> All interactions must be voluntary and based on explicit consent.

Consent must be explicit. Silence does not imply consent.
Assumed consent is not consent.

Interactions initiated without explicit consent do not satisfy
this invariant regardless of intent.

---

## Invariant 3 — Consent Withdrawal and Exit

**Kernel statement:**
> Consent may be withdrawn. Exit must always be possible.

These are two conditions, not one.

Consent withdrawal: a party may revoke consent at any point.
A system that makes revocation difficult, costly, or impossible
does not satisfy this invariant.

Exit: departure from any system, interaction, or obligation must
always be structurally possible. Exit that requires permission
from the system being exited does not satisfy this invariant.

---

## Invariant 4 — Contractual Clarity

**Kernel statement:**
> All contracts must be explicit, readable, and equally enforceable
> by all parties.

Three conditions, all required:

**Explicit** — terms are stated, not implied or embedded in behaviour.

**Readable** — terms are legible to the affected parties without
specialist interpretation.

**Equally enforceable** — all parties hold the same enforcement
rights. Asymmetric enforcement, hidden terms, or unilateral
modification violate this invariant.

---

## Invariant 5 — No Hidden Rules

**Kernel statement:**
> No rules governing interaction may be hidden or unilaterally changed.

All rules affecting an interaction must be visible and inspectable
before the interaction occurs.

Hidden rules include: undisclosed moderation logic, opaque scoring
systems, and decision processes that affect outcomes without
disclosure.

Unilateral change: rules may not be changed by one party without
the knowledge and ability to exit of all affected parties.

Authority must be declared or it does not exist.

---

## Invariant 6 — Fail-Open

**Kernel statement:**
> On failure, systems must fail open, reveal governing rules,
> and default to human choice.

Three conditions on failure:

**Fail open** — default to the least restrictive state, not the
most restrictive.

**Reveal governing rules** — the rules in force at the moment
of failure must be exposed, not concealed.

**Default to human choice** — control returns to the human
party, not to the system or its operator.

Fail-closed systems, silent failures, and failures that increase
system control do not satisfy this invariant.

---

## Invariant 7 — Immutability and Binary Satisfaction

**Kernel statement:**
> The kernel is immutable. Adherence is binary.

The kernel text does not change. Any modification to the kernel
text constitutes a fork, not an update. Silent modification is
non-satisfaction.

Satisfaction is binary. A system either satisfies all seven
invariants at every execution boundary or it does not.
There is no partial satisfaction. There is no phased alignment.
There is no "spirit of 512."

---

## Closing Note

These seven invariants are the complete constraint set.

Nothing may be added. Nothing may be softened. Nothing may be
qualified with "where feasible," "to the extent possible," or
"in most cases."

Any system that satisfies all seven at every execution boundary
exhibits 512's properties. Any system that does not satisfy all
seven does not — regardless of naming, documentation, or intent.
