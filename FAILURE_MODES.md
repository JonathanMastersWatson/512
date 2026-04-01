# Failure Modes and Non-Solutions 

## Purpose

This document enumerates **problems 512 does not attempt to solve**.

It exists to prevent scope creep and misattribution of responsibility.

These are **boundary conditions**, not defects: they are the limits of what 512 can guarantee on its own.

> **Pre-hardening phase in progress.** See [`PRE_HARDENING_NOTICE.md`](./PRE_HARDENING_NOTICE.md).

---

## 512 Does Not Solve

### 1. Truth Determination

512 does not determine:
- truth
- accuracy
- correctness
- intent

It evaluates whether a proposed action satisfies declared constraints.
It does not determine whether those constraints are correct, complete,
or whether the declared intent is truthful.

---

### 2. Ethical Judgment

512 does not evaluate:
- morality
- fairness
- harm
- benefit

It contains no ethical logic.

---

### 3. Behavioral Enforcement

512 does not:
- penalize actions that have already occurred
- reward compliant behaviour
- modify how agents behave over time
- enforce consequences beyond the boundary decision

At the commit boundary, 512 produces one of three outputs: allow,
deny, or gap. What happens to an agent as a result of a denial —
sanctions, reputation effects, legal consequences — is outside
512's scope. 512 controls the boundary. It does not control
what follows from a boundary decision.

---

### 4. Identity Resolution

512 does not:
- verify identity
- manage credentials
- assign reputation
- enforce accountability

Any system doing so is external to 512.

---

### 5. Governance Outcomes

512 does not:
- improve governance
- reform institutions
- guarantee compliance
- ensure trust

It constrains legitimacy witnessing only.

---

### 6. Social or Political Stability

512 does not address:
- inequality
- democracy
- authoritarianism
- social cohesion

Such outcomes are outside its scope.

---

## Known Limitations

512 cannot prevent:
- misuse of systems
- malicious actors
- bad incentives
- institutional capture

It is not designed to.

---

## Boundary Statement

If a problem requires:
- ethics
- enforcement of consequences
- identity
- values
- authority

It is **out of scope** for 512.

---

## Status

This document defines the **explicit limits** of the 512 constraint layer.
