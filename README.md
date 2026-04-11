# 512 — The Commit Gate

This repository documents **512**, a discovered constraint that physics
forces into existence at the execution boundary of any machine-speed
system operating at scale.

512 is **not** a product, protocol, platform, governance system, or
political program. It is a **minimal, non-ownable constraint** identified
through applied systems research conducted in late 2025.

---

## START HERE

Choose your entry point:

| I am... | Start here |
|---|---|
| **An engineer building a gate** | [`512-ops/COMMIT_BOUNDARY_REFERENCE.md`](./512-ops/COMMIT_BOUNDARY_REFERENCE.md) |
| **An enterprise practitioner preparing workflows** | [`USE_CASES/ENTRY_POINTS/ENTERPRISE_PRACTITIONERS.md`](./USE_CASES/ENTRY_POINTS/ENTERPRISE_PRACTITIONERS.md) |
| **A CTO or board member** | [`512_ARCHITECTURE`](./512_ARCHITECTURE_v3.0.md) |
| **A regulator or legal reviewer** | [`USE_CASES/ENTRY_POINTS/REGULATORS.md`](./USE_CASES/ENTRY_POINTS/REGULATORS.md) |
| **An economist or researcher** | [`USE_CASES/ENTRY_POINTS/ECONOMISTS.md`](./USE_CASES/ENTRY_POINTS/ECONOMISTS.md) |

---

## The Canonical Kernel

The kernel text is the authority.
Path:   512-core/KERNEL/512-kernel-padded.txt
Size:   512 bytes (exact, UTF-8, no BOM)
SHA-256: 7b08c024b77a24830c15e7952d6e54bed383aa960f4c74a71ff95ce51f4d80f5

XRPL anchor transaction:
`378536A3CB75DECF90B6AE57F75292BDFF716285B01946870CAC158F8152D100`

The kernel is immutable. It is not redefined anywhere else in this
repository. Commentary, analysis, and interpretation documents are
subordinate to it. The 512-byte padded artifact is implementation-oriented
and must not be edited in-browser.

---

## What 512 Is

512 is a **discovered constraint** — not a product, system, or invention.

When execution systems operate at machine speed — AI agents deciding
in microseconds, autonomous systems committing thousands of state changes
per second — the moment between intent and irreversible consequence
collapses below the threshold of human intervention. Governance
mechanisms designed for human-speed execution do not slow down.
They become structurally irrelevant.

The response to this is not a product. It is a constraint that physics
makes inevitable: a **Commit Gate** — a minimal, immutable, binary
mechanism positioned at the execution boundary, enforcing pre-committed
constraints before state change occurs, at speeds that make
interpretation physically impossible.

512 defines seven invariants that any Commit Gate satisfying its
properties must enforce. Systems either satisfy these properties or
they do not. There is no partial satisfaction.

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
- a policy engine
- a product to be deployed

512 does not determine truth, correctness, or morality.
It defines only whether execution aligns with declared constraints.

---

## The Seven Invariants

No agent may initiate force or fraud against any human.
All interactions must be voluntary and based on explicit consent.
Consent may be withdrawn. Exit must always be possible.
All contracts must be explicit, readable, and equally
enforceable by all parties.
No rules governing interaction may be hidden or unilaterally changed.
On failure, systems must fail open, reveal governing rules,
and default to human choice.
The kernel is immutable. Adherence is binary.


Full definitions: [`512-core/KERNEL/INVARIANTS.md`](./512-core/KERNEL/INVARIANTS.md)

---

## Operational Reference — 512-ops

The `512-ops/` folder contains the working reference for organisations
preparing agentic workflows for Commit Gate execution:

| File | What it covers |
|---|---|
| [`INTEGRATION_STEPS.md`](./512-ops/INTEGRATION_STEPS.md) | 7-step workflow from boundary identification to verified evidence chain |
| [`COMMIT_BOUNDARY_REFERENCE.md`](./512-ops/COMMIT_BOUNDARY_REFERENCE.md) | Boundary mechanics, Proposal Object, evaluation outputs, non-conformant patterns |
| [`CONSTRAINT_DEFINITION_LAYER.md`](./512-ops/CONSTRAINT_DEFINITION_LAYER.md) | How to translate policies into executable constraints |
| [`REFERENCE_FLOW.md`](./512-ops/REFERENCE_FLOW.md) | End-to-end sequence from intent to anchored evidence |
| [`PROPERTIES_CHECKLIST.md`](./512-ops/PROPERTIES_CHECKLIST.md) | Go-live verification checklist |

---

## Repository Structure

**Core:**
- `/512-core/KERNEL/` — canonical kernel text and invariants
- `/512-core/CANON/` — spec hash mechanism and equivalence model
- `/512-ops/` — operational reference for builders and enterprise practitioners

**Research record:**
- `/512-papers/` — discovery history, problem definition, technical
  constraints, economic implications, explicit non-goals
- `/512-analysis/` — economics, philosophy, history

**Reference:**
- `ANTI_DRIFT.md` — how implementations drift from 512's properties
  and how to prevent it
- `PROVENANCE.md` — origin and authorship
- `TERMS.md` — terminology
- `FAILURE_MODES.md` — explicit non-solutions
- `INTERPRETATION_GUIDE.md` — how not to misread this repository
- `LEGAL_NOTE.md` — legal posture
- `SCOPE_AND_NON_GOALS.md` — what 512 defines and what it does not

**Entry points by audience:**
- `/USE_CASES/ENTRY_POINTS/` — engineers, enterprise practitioners,
  regulators, economists

**Non-canonical:**
- `/DERIVATIVES/` — commercial and exploratory material
- `/512-interpretation/` — interpretation variants (non-authoritative)
- `/PROMPTS/` — optional LLM workspace loaders (UX helpers only)

---

## Scope

512 defines the minimum constraint surface for enforcing execution-time
properties at the commit boundary — without creating new authorities.

512 does **not** provide:
- constraint definition (see [`Constraint-Architecture`](https://github.com/JonathanMastersWatson/Constraint-Architecture))
- evidence persistence or ledger anchoring (see CVS)
- identity, governance, or enforcement logic
- implementation prescriptions

**On witness architectures:** 512 does not prescribe a witness layer.
The CVS (Cryptographic Verification Sidecar) repository is the reference
witness architecture. Others may exist. None are canonical to 512.

**On constraint definition:** 512 does not define domain constraints.
Constraint definition is upstream work — the organisation's
responsibility. See `512-ops/CONSTRAINT_DEFINITION_LAYER.md`.

---

## Status

This repository is a **descriptive research record**.

The kernel is frozen. The hardening pass covering this repository
was completed April 2026. New material may be added only through
append-only updates tracked in `CHANGELOG.md`.

---

## Licensing

512 and its constraint set are non-ownable. Discovered constraints
are not subject to proprietary ownership.

Written documentation in this repository is released under Creative
Commons Attribution 4.0 (CC BY 4.0) unless otherwise specified.

---

## One-Sentence Summary

> 512 is a discovered constraint — the minimal set of properties any
> execution system operating at machine speed must satisfy at the
> commit boundary, or bear the consequences that physics and scale impose.
