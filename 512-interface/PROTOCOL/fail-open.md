# Transparent Denial and Human Default Protocol

## Purpose

This document specifies how systems adhering to the 512 Kernel implement
the disclosure and human sovereignty obligations of Invariant 6 — without
exposing private data, security-sensitive internals, or exploitable system
logic.

This document governs two of the three obligations derived from I6:

- **Transparent Denial** — when the gate evaluates and produces DENY,
  the governing rule must be disclosed and the decision must be inspectable.
- **Human Default** — on any adverse outcome, authority returns to the
  human party; exit, revocation, and contest remain structurally available.

This document does not govern Fail Open (gate unavailability behaviour).
Fail Open — the behaviour that engages when the gate cannot complete
evaluation — is defined in `512-core/KERNEL/DEFINITIONS.md` and elaborated
in `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`.

The authoritative constitutional elaboration of all three I6 obligations
is `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md`. This document
provides the operational protocol for implementing Transparent Denial
and Human Default.

---

## Principle

Transparent Denial means:

When the gate evaluates and produces DENY, the system must:
- reveal the governing rule that produced the denial, and
- make the decision inspectable by the affected party.

Human Default means:

On any adverse outcome — denial, restriction, or system failure —
the system must:
- return authority to the human party, and
- default to user choice to exit, revoke, or contest.

Neither obligation requires disclosure of secrets.

---

## Scope of Disclosure

Transparent Denial requires disclosure of what is necessary for accountability.

It does not require disclosure of what would enable exploitation.

---

## Required Disclosures

On a Transparent Denial event, a system must disclose:

1. **Decision Outcome**  
   The action taken or denied (e.g., allow, deny, restrict, flag).

2. **Kernel Reference**  
   The specific kernel line(s) invoked.

3. **Policy Reference**  
   The policy module, contract clause, or rule-set applied, identified by
   name and version or hash.

4. **Reason Codes**  
   A concise description of the decision grounds expressed as categories,
   not raw data or thresholds.

5. **User Options**  
   Clear paths to:
   - exit the interaction,
   - revoke consent,
   - export the user's own data,
   - or initiate review.

---

## Prohibited Disclosures

Transparent Denial must not disclose:

- private data belonging to other parties,
- credentials, keys, or secrets,
- model weights or embeddings,
- internal thresholds or detection heuristics,
- infrastructure topology or attack surfaces,
- proprietary logic that enables circumvention.

---

## Proof Without Disclosure

Where relevant information cannot be safely disclosed, the system must
provide verifiable proof that the governing rules were applied correctly.

Acceptable proof mechanisms include:
- signed execution receipts,
- policy and model hashes,
- trusted execution environment attestations,
- reproducible policy identifiers,
- cryptographic commitments.

Proof replaces disclosure where disclosure would cause harm.

---

## Two-Channel Transparency

Transparent Denial operates across two channels:

1. **Public Accountability Channel**  
   Discloses rules, policy identifiers, and decision grounds.

2. **Private User Channel**  
   Provides the affected user with access to their own data, logs, and
   evidence bundles, encrypted to that user.

---

## Degraded Operation

On any adverse outcome, systems must reduce risk by:

- disabling non-essential actions,
- rate-limiting sensitive operations,
- freezing high-impact automated decisions,
- preserving evidence for review.

Adverse outcome handling does not imply full operational continuity.

---

## Dispute and Review

If a human party contests a decision:

- the system must provide a reproducible rule path, or
- offer escalation to an independent reviewer or auditor.

Disclosure to reviewers may occur under controlled conditions.

---

## Exit Guarantee

If Transparent Denial obligations cannot be satisfied without violating
privacy or security constraints, the system must default to exit.

Human parties must be able to:
- terminate participation,
- revoke consent,
- and retrieve their own data.

This is the structural expression of Human Default.

---

## Non-Compliance

A system that:
- hides governing rules on denial,
- traps human parties after an adverse outcome,
- or claims secrecy to avoid accountability,

is not adhering to the 512 Kernel.
