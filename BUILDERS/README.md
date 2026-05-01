# BUILDERS

This folder contains the reference documents for organisations and engineers
building on top of the 512 Commit Gate specification.

512 is a discovered constraint. The documents here define what it is, why it
exists, how to build a system that satisfies its properties, and how it relates
to the broader AI governance landscape.

---

## Contents

| Document | Audience | Purpose |
|---|---|---|
| `EXECUTION_BOUNDARY_PRINCIPLE.md` | CTO / Architect / Regulator | Why physics forces the Commit Gate into existence — the first-principles case for boundary governance at machine speed |
| `512_ARCHITECTURE_v3.4.md` | CTO / Board | What 512 is, the seven invariants, the open commons model |
| `512_IMPLEMENTATION_v3.3.md` | Engineer | How to build a system satisfying 512's observable properties |
| `AARM_AND_512.md` | CTO / Architect | Architectural positioning — AARM governs the orchestration layer, 512 governs the commit boundary; complementary, not competing |
| `512_CVS_ENTERPRISE_v1_0.md` | CTO / CFO / Board | Enterprise executive brief — the execution boundary problem and what 512/CVS resolves |

---

## Where to Start

**If you are a CTO or board member:** Read `EXECUTION_BOUNDARY_PRINCIPLE.md`
first for the physical and structural case. Then `512_ARCHITECTURE_v3.4.md`
for the full specification. Then `512_CVS_ENTERPRISE_v1_0.md` for the
financial and operational case.

**If you are an engineer:** Read `512_ARCHITECTURE_v3.4.md` §1–4 for the
constraint rationale, then `512_IMPLEMENTATION_v3.3.md` for the build reference.

**If you are evaluating 512 relative to AARM or the CSA initiative:**
Read `AARM_AND_512.md` first.

**If you are a regulator or insurer:** Read `EXECUTION_BOUNDARY_PRINCIPLE.md`
and `512_CVS_ENTERPRISE_v1_0.md`.

---

## What Is Not Here

The kernel itself — the seven invariants, the canonical hash, the XRPL genesis
anchor — lives in `512-core/`. The documents in this folder reference the kernel
but do not define it.

Constraint definition and operational workflows are in `512-ops/`.

The priority record establishing 512's prior art status is `CANONICAL_COMMITMENT.md`
at repo root.

---

*512 BUILDERS reference documents | github.com/JonathanMastersWatson/512*
*CC BY 4.0 — open commons. Build freely. Own what you build.*
