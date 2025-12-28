# Fail-Open Protocol

## Purpose

This document specifies how systems adhering to the 512 Kernel implement
fail-open behavior without exposing private data, security-sensitive
internals, or exploitable system logic.

Fail-open is a transparency and freedom guarantee, not a disclosure mandate.

---

## Principle

Fail-open means:

When a system cannot proceed normally, it must:
- reveal the governing rule path that led to the outcome, and
- default to user choice to exit, revoke, or contest.

Fail-open does not require disclosure of secrets.

---

## Scope of Disclosure

Fail-open requires disclosure of what is necessary for accountability.

It does not require disclosure of what would enable exploitation.

---

## Required Disclosures

On a fail-open event, a system must disclose:

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
   - export the user’s own data,
   - or initiate review.

---

## Prohibited Disclosures

Fail-open must not disclose:

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

Fail-open operates across two channels:

1. **Public Accountability Channel**  
   Discloses rules, policy identifiers, and decision grounds.

2. **Private User Channel**  
   Provides the affected user with access to their own data, logs, and
   evidence bundles, encrypted to that user.

---

## Safe-Open Mode

On entering fail-open, systems must reduce risk by:

- disabling non-essential actions,
- rate-limiting sensitive operations,
- freezing high-impact automated decisions,
- preserving evidence for review.

Fail-open does not imply full operational continuity.

---

## Dispute and Review

If a user contests a decision:

- the system must provide a reproducible rule path, or
- offer escalation to an independent reviewer or auditor.

Disclosure to reviewers may occur under controlled conditions.

---

## Exit Guarantee

If fail-open obligations cannot be satisfied without violating privacy or
security constraints, the system must default to exit.

Users must be able to:
- terminate participation,
- revoke consent,
- and retrieve their own data.

---

## Non-Compliance

A system that:
- hides governing rules,
- traps users during failure,
- or claims secrecy to avoid accountability,

is not adhering to the 512 Kernel.
