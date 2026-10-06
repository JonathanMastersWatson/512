# Obligation

**Document:** `512-obligation` · **Version:** 1.0 · **Date:** 2026-10-06
**Author:** Jonathan M. Watson
**Status:** Architectural specification. This document specifies the obligation
layer of the 512/CVS architecture. It does not modify the canonical 512 kernel.

---

## 1. The gap

The 512/CVS model runs declaration → gate → witness: declarations are bound,
actions are evaluated (ALLOW or DENY), and events are witnessed into
tamper-evident receipts.

What it did not specify is the durable layer between evidence and settlement:
who owes whom, under which terms, how much — and whether the amount is unpaid,
disputed, or settled. The obligation is that layer.

## 2. Position in the pipeline

```
Execution → Evidence → Obligation → Settlement → Enforcement
```

Each stage is a separate function:

- **Execution** is governed by 512 at the commit boundary (ALLOW/DENY).
- **Evidence** is produced by CVS, which witnesses events and never judges them.
- **Obligation** records what is owed as a result of an authorized action.
- **Settlement** moves value against obligations.
- **Enforcement** is human-speed: arbitration and courts.

A receipt may establish an economic fact and create an obligation without being
a payment and without participating in collection. Witnessing an economic fact
is not collecting on it. This separation resolves the coupling objection:
evidence, obligation, settlement, and enforcement are distinct functions, and a
system may implement any subset without collapsing them into one.

## 3. What an obligation is

The obligation is the IOU: a content-addressed, tamper-evident statement that
the governing agreements and checks were green and that one party owes another
for an exchange.

- **Content-addressed.** `obligation_id` is the SHA-256 of the canonical
  obligation object. The identifier *is* the content hash.
- **Tamper-evident, not mutable.** Creation is witnessed into the chain.
  Transitions are appended as new witnessed events; the IOU is never silently
  rewritten or deleted.
- **Amount-agnostic.** Amounts are decimal strings with arbitrary precision —
  never floating point. An obligation for $0.0003 and an obligation for $333.00
  are the same kind of object.
- **Canonical form.** Every obligation object and every lifecycle event is
  canonical JSON (JCS), SHA-256 hashed and chained.

## 4. The obligation object

Each obligation identifies:

- **obligor** — the party who owes. This is the legal principal resolved through
  the carried delegation chain: the agent acts; the named human or enterprise owes.
- **obligee** — the party owed.
- **amount / currency** — decimal string, arbitrary precision, never float.
- **terms reference / hash** — the bound terms under which the obligation
  was created.
- **due condition** — when the obligation becomes overdue, as defined by
  the terms.
- **evidence_ref** — the hash of the evaluation core that authorized the action
  (see §5).

## 5. Creation

- An obligation is created **per priced ALLOW**, at machine speed, inside the
  ALLOW artifact. DENY creates no obligation; the honest null names the failed
  check instead.
- **Construction order** (resolving the self-reference): the canonical evaluation
  core — declaration, frozen evidence, kernel version/checksum, the seven check
  results, decision and reason codes — is hashed first to produce `core_hash`.
  The obligation carries `evidence_ref = core_hash`. The outer artifact contains
  the evaluation plus the obligation, producing `artifact_hash`. The witness
  creation event references the full outer artifact hash. The IOU is therefore
  self-contained and cryptographically bound to the exact decision that created it.
- The gate **emits** the creation; it does not store it (see §10).

## 6. Authorized is not happened

At ALLOW, the obligation means exactly one thing: *agreements green, transfer
authorized.* It does not mean the transfer happened.

- The transfer-happened half of the story arrives via the witness: execution
  reports — attempted, returned, retry — linked to the obligation by `evidence_ref`.
- If the authorized action never executes, the obligation transitions to `voided`
  by a witnessed event. Never silent deletion.

The handoff line is the ALLOW at the execution boundary: the good, service, or
data is exchanged for the obligation — not necessarily for immediate payment.
Settlement is a later consequence and produces its own witnessed receipt.

## 7. Lifecycle

States: `open → settled | overdue | disputed | voided`.

- **open** — authorized and within the terms' settlement window. Open means
  current; it does not block subsequent machine-speed actions.
- **settled** — netted within the settlement window (see §8).
- **overdue** — past the window, unpaid.
- **disputed** — contested through a human-speed process. Disputes are visible
  but tracked separately from arrears: the gate does not prejudge a human-speed
  dispute.
- **voided** — authorized but never executed. Witnessed, never deleted.

Every transition is a witnessed event. A later settlement receipt references one
or many obligation IDs; batched or net settlement may close many micropayment
obligations at once while preserving per-obligation traceability.

## 8. Settlement

Obligations are settled by netting per (obligor, obligee, currency) over the
terms' settlement window. Settlement rails report settlement as witnessed events;
the obligation layer itself moves no value.

## 9. Arrears

`arrears_clear` is a Boolean computed over the obligation fold: it is false if
and only if the fold finds at least one `overdue` obligation in the terms-defined
scope.

- `open` is current and never counts against arrears.
- `disputed` is tracked separately and never counts as arrears.
- The terms define when `open → overdue`. The kernel does not adjudicate lateness.

## 10. Ledger placement

- **Not in the gate.** The gate is stateless. It creates the obligation inside
  the ALLOW artifact and emits it; it keeps no ledger.
- **Not a third platform.** The witness chain already records every transition —
  creation, settlement reports, disputes, voids. The ledger is a deterministic
  fold: a projection over the chain. No new system of record is required.
- **Writers of transitions:** the gate (creation), settlement rails (settlement
  reports), human-speed processes (disputes, voids). CVS only witnesses.
- **Deterministic evaluation:** evidence bundles carry `witness_head` — the
  chain-head hash against which the obligation fold and the `arrears_clear`
  Boolean were computed — so state-dependent checks stay re-executable.

## 11. What the obligation is not

- Not a payment. Creating an obligation moves no value.
- Not collection. The obligation layer does not collect or enforce.
- Not a fact about the world. Like everything in 512, it binds declarations:
  *this transfer was authorized under these terms*, attributable and witnessed.
  Whether the transfer happened, and whether the debt is paid, is established
  by further witnessed events — and ultimately judged at human speed.
