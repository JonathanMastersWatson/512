# Definitions

This document defines terms as they are used in the 512 Kernel.

These definitions clarify language.
They do not add rules, permissions, or enforcement mechanisms.

If a definition conflicts with the kernel text, the kernel prevails.

---

## Agent

Any software system, automated process, organization, or individual
capable of initiating or responding to an interaction.

---

## Human

A natural person.

---

## Interaction

Any exchange, action, transaction, or influence between agents,
humans, or systems that affects rights, data, resources, or outcomes.

---

## Consent

A clear, affirmative agreement to participate in an interaction.

Consent must be:
- explicit, and
- attributable to the consenting party.

Consent may be withdrawn.

---

## Exit

The ability of a party to discontinue participation in an interaction
without coercion or undisclosed penalty.

---

## Force

Any action that compels behavior through physical, technical,
economic, or systemic coercion without consent.

---

## Fraud

Any action that induces participation through deception,
misrepresentation, or omission of material facts.

---

## Contract

An explicit agreement governing an interaction between parties.

A contract may be human-readable, machine-readable, or both.

---

## Rule

Any condition, constraint, or logic that governs or limits interaction.

---

## Hidden Rule

A rule that materially affects interaction but is not disclosed to
affected parties in advance.

---

## Fail Open

The I6 constitutional principle governing gate behaviour on infrastructure
failure. When the gate cannot complete evaluation — due to crash, timeout,
network partition, or any condition preventing evaluation from occurring —
the gate produces DENY with reason: evaluation unavailable. The commit path
remains closed. The cause of unavailability is disclosed. Retry is
explicitly permitted when the gate is available.

Fail Open does not mean execution continues without admissibility being
established. It means the system must not weaponise its own failure as
concealed restriction — the DENY reason is disclosed, the commit boundary
holds, and the human party retains the ability to retry.

This is the Evaluation-Unavailable DENY doctrine. The authoritative
elaboration is `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`.

Fail Open governs gate unavailability only. It does not govern what a
system must do when the gate evaluates and produces DENY due to constraint
violation. Those obligations — disclosure of the violated invariant and
return of authority to the human party — are defined in the kernel clauses
"reveal governing rules" and "default to human choice."

---

## Kernel

The canonical text contained in `512-kernel.txt`.

The kernel is immutable.
