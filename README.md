# 512 — Execution-Time Legitimacy Under Scale

This repository documents **512**, a discovered constraint governing
**legitimacy at execution time** in large-scale, distributed systems.

512 is **not** a product, protocol, platform, governance system, or
political program. It is a **minimal, non-ownable constraint**
identified through applied systems research conducted in late 2025.

> **Pre-hardening phase in progress.** Language and normative framework
> are being tightened. See [`PRE_HARDENING_NOTICE.md`](./PRE_HARDENING_NOTICE.md).

---

## ⚡ START HERE — Developers

If you are building a system against 512, start with these three files
in this order:

| Step | File | What it gives you |
|---|---|---|
| 1 | [`512-core/KERNEL/512-kernel.txt.txt`](./512-core/KERNEL/512-kernel.txt.txt) | The 7 invariants — the actual constraint text |
| 2 | [`512-core/KERNEL/INVARIANTS.md`](./512-core/KERNEL/INVARIANTS.md) | Each invariant defined precisely |
| 3 | [`512-ops/COMMIT_BOUNDARY_REFERENCE.md`](./512-ops/COMMIT_BOUNDARY_REFERENCE.md) | What the boundary looks like in practice — Proposal Objects, evaluation, output |

The verified 512-byte canonical artifact:
[`512-core/KERNEL/512-kernel-padded.txt`](./512-core/KERNEL/512-kernel-padded.txt)
SHA-256: `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

Everything else in this repository is context, history, or commentary.
Those three files are what you need to build.

---

## What 512 Is

512 is a **discovered constraint** — not a product, system, or invention.

It consists of seven invariants defining the minimum conditions under
which execution at machine speed can be considered legitimate.

Systems either satisfy these properties or they do not.
There is no partial satisfaction.

512 does not determine truth, correctness, or morality.
It defines only whether execution aligns with declared constraints.

---

## What 512 Is Not

512 is not:
- a manifesto
- a constitution
- a governance framework
- a protocol suite
- a standards body
- a movement or ideology
- a compliance system
- a monitoring tool

A system that enforces behavior, requires identity, or embeds ideology
does not satisfy 512's properties.

---

## The Canonical Kernel

The kernel text is the authority. It lives here:
[`512-core/KERNEL/512-kernel.txt.txt`](./512-core/KERNEL/512-kernel.txt.txt)

The kernel is **immutable**. It is not redefined anywhere else in this
repository. Commentary, analysis, and interpretation documents are
subordinate to it.

The 512-byte padded artifact is implementation-oriented and
MUST NOT be edited in-browser. Canonical meaning is defined by
the unpadded kernel text.

- Encoding: UTF-8 (no BOM)
- Size: 512 bytes (exact)
- SHA-256: `7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5`

---

## Scope

512 defines the minimum constraint surface for making execution-time
legitimacy auditable — without creating new authorities.

512 does **not** provide:
- coordination or incentives
- enforcement or identity
- governance or safety logic
- implementation prescriptions

Those are explicitly out of scope. See `SCOPE_AND_NON_GOALS.md`.

**On terminology:** in 512, *legitimacy* means verifiable consistency
between declared rules and observed execution — not moral, legal,
or political legitimacy.

**On witness architectures:** 512 does not prescribe a witness layer.
External witness architectures that observe and record execution
against 512's properties are compatible but independent.
The Evidence-Sidecar repository is one such architecture.
Others may exist. None are canonical to 512.

---

## Repository Structure

**Core — start here:**
- `/512-core/KERNEL/` — the canonical kernel text and invariants
- `/512-ops/` — operational reference, including the developer boundary worksheet

**Research record:**
- `/512-papers/` — discovery history, problem definition, technical constraints,
  economic implications, explicit non-goals

**Reference:**
- `PROVENANCE.md` — origin and authorship
- `INTERPRETATION_GUIDE.md` — how not to misread this repository
- `TERMS.md` — terminology
- `FAILURE_MODES.md` — explicit non-solutions
- `ANTI_DRIFT.md` — what 512 is not, and how implementations drift
- `LEGAL_NOTE.md` — legal posture
- `CITATION_POLICY.md` — citation rules

**Status documents:**
- `PRE_HARDENING_NOTICE.md` — current hardening phase status
- `LIVING_DOCUMENTS.md` — which documents are dynamic and subject to revision

**Non-canonical:**
- `/PROMPTS/` — optional LLM workspace loaders (UX helpers only)
- `/DERIVATIVES/` — commercial and exploratory material
- `/512-interpretation/` — interpretation variants (non-authoritative)

---

## Status

This repository is a **descriptive research record**.

The kernel is frozen. Historical documents are immutable.
New material may be added only through append-only updates
tracked in `CHANGELOG.md`.

See `PRE_HARDENING_NOTICE.md` for current hardening phase status.

---

## Licensing

512 and its constraint set are non-ownable.
Written documentation in this repository is released under
Creative Commons Attribution 4.0 (CC BY 4.0) unless otherwise specified.
The constraint category itself remains unowned.

---

## One-Sentence Summary

> 512 documents a minimal execution-time constraint required to witness
> legitimacy in distributed systems without identity, enforcement, or ideology.
