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

The system behaviour that engages when the gate cannot complete
evaluation — due to crash, timeout, network partition, or any
condition that prevents evaluation from occurring. On a Fail Open
event: the gate produces no output; the commit path remains
available; execution proceeds; the witness layer records the
ungoverned period as an evidence chain gap.

Fail Open is not a gate output. It is not equivalent to ALLOW.
Constraint satisfaction was not established.

Fail Open governs gate unavailability only. It does not govern
what a system must do when the gate evaluates and produces DENY.
Those obligations — disclosure of the governing rule and return
of authority to the human party — are defined in the kernel
clauses "reveal governing rules" and "default to human choice"
and elaborated in `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`.

---

## Kernel

The canonical text contained in `512-kernel.txt`.

The kernel is immutable.
