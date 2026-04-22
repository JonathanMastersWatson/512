# CHANGELOG
## Purpose
This file records **structural and documentary changes** to the 512 research archive.
It exists to:
- preserve historical integrity
- prevent silent revisionism
- allow reviewers to track evolution
---
## [2026-04-22] — Canonical IR Correction and Execution Boundary Hardening Pass

### Objective
Two independent issues identified and corrected in this pass.

**Issue 1 — CANONICAL_IR.json contained 9 rules instead of 7.**
The March 2026 hardening pass corrected INVARIANTS.md but did not
correct CANONICAL_IR.json. The file split Invariant 3 (withdrawal
and exit — one kernel statement) into two rules (I3 + I4), and
split Invariant 7 (immutability and binary satisfaction — one kernel
statement) into two rules (I8 + I9), producing a 9-rule IR that
misrepresents the 7-statement kernel. The SPEC_HASH computed via
JCS(CANONICAL_IR.json) therefore did not correctly represent the
canonical kernel structure. The canonical commitment hash
(7b08c024...) is unaffected — it is computed from
512-kernel-padded.txt, not from this file.

**Issue 2 — Gate output model ambiguity in ops docs.**
COMMIT_BOUNDARY_REFERENCE.md and REFERENCE_FLOW.md listed
Fail-Open as a third sub-heading alongside ALLOW and DENY,
visually implying a third gate output value. This contradicted
the established binary model and created a surface for
misinterpretation. The gate produces exactly two outputs:
ALLOW or DENY. Fail-open is a system behaviour (Invariant 6),
not a gate output.

### Files Modified
- `512-core/CANON/CANONICAL_IR.json`
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md`
- `512-ops/REFERENCE_FLOW.md`

### Changes Applied

**CANONICAL_IR.json:**
- I3 (Withdrawal) + I4 (Exit) merged into I3 (Withdrawal and exit)
- I8 (Immutability) + I9 (Binary adherence) merged into I7
  (Immutability and binary satisfaction)
- Rules renumbered: former I5→I4, I6→I5, I7→I6
- Ordering comment updated from I1..I9 to I1..I7
- Notes added to I3 and I7 documenting the merged conditions

**COMMIT_BOUNDARY_REFERENCE.md:**
- §4 opening hardened: "The gate is binary. Every completed
  evaluation produces exactly one of two outputs: ALLOW or DENY.
  There is no third output value."
- Fail-Open moved to §4.1 as a named sub-section (system behaviour,
  not gate output)
- Quick Reference table updated: outputs row hardened to
  "ALLOW or DENY — binary, always"; fail-open added as separate row
- Diagrams reformatted as fenced code blocks

**REFERENCE_FLOW.md:**
- Stage 4 opening hardened to two values only
- Fail-Open moved to Stage 4.1
- Stage 3 witness layer note updated: validation-result absent on
  fail-open; gap_record replaces it
- Stage 6 Evidence Object tree annotated accordingly
- All diagrams reformatted as fenced code blocks

### Invariant Mapping Restored

| Kernel statement | CANONICAL_IR rule |
|---|---|
| No agent may initiate force or fraud against any human | I1 |
| All interactions must be voluntary and based on explicit consent | I2 |
| Consent may be withdrawn. Exit must always be possible | I3 |
| All contracts must be explicit, readable, and equally enforceable | I4 |
| No rules governing interaction may be hidden or unilaterally changed | I5 |
| On failure, systems must fail open, reveal governing rules, and default to human choice | I6 |
| The kernel is immutable. Adherence is binary | I7 |

---
## [2026-04-17] — GAP Attribution Hardening Pass
### Objective
Correct all instances where GAP was attributed to the Commit Gate
as an output or evaluation result. 512 is binary. The gate produces
exactly two outputs: ALLOW or DENY. GAP is a CVS witness layer
classification applied to ungoverned periods in the evidence chain.
It is not a gate output under any operational state.
### Files Modified
- `ANTI_DRIFT.md`
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md`
- `512-ops/REFERENCE_FLOW.md`
- `512-ops/INTEGRATION_STEPS.md`
- `512-ops/PROPERTIES_CHECKLIST.md`
- `USE_CASES/ENTRY_POINTS/ENTERPRISE_PRACTITIONERS.md`
### Changes Applied Across All Files
- Removed GAP from gate output lists (ALLOW / DENY / GAP → ALLOW or DENY)
- Output counts corrected from "three" to "two" wherever they appeared
- "GAP results" and "### GAP" subsections reframed as
  "Fail-open events" and "### Fail-Open (Gate Unavailable)"
- Sequence diagrams: ALLOW/DENY/GAP gate signal → ALLOW or DENY;
  ALLOW (GAP) fail-open arrow removed — gate produces no signal
  when unavailable; gap_record emits from fail-open handler to
  witness layer only
- Evidence Object schema: overall_result ALLOW / DENY / GAP
  → ALLOW or DENY (absent on fail-open events — see gap_record)
- Quick Reference tables updated to reflect two gate outputs;
  GAP row replaced with fail-open behaviour row
### Correct Separation Established
- 512 produces: ALLOW or DENY
- CVS records: the ALLOW or DENY result from 512, AND classifies
  any ungoverned execution periods as evidence chain gaps
### Notes
- Gap Semantics section in ANTI_DRIFT.md was correct as written
  and is unchanged: "A gap is not an evaluation result. It is a
  failure of evaluation."
- Fail-Open Properties checklist items in PROPERTIES_CHECKLIST.md
  were correctly scoped to the witness layer and are unchanged
---
## [2025-12-26] — Initial Canonical Archive Freeze
### Added
- Full `/512-papers/` canonical sequence
- README.md (repository orientation)
- PROVENANCE.md
- INTERPRETATION_GUIDE.md
- CITATION_POLICY.md
- FAILURE_MODES.md
- TERMS.md
- REVIEWER_FAQ.md
### Defined
- Canonical paper numbering
- Discovery timeline (log-derived)
- Explicit non-goals and exclusions
### Notes
- Research identified as descriptive, not prescriptive
- No ownership or authority claims asserted
---
## Change Policy
- Substantive conceptual changes require a new dated entry
- Clarifications may be added, but original text is not retroactively altered
- Historical discovery documents are immutable
---
## Versioning Note
This repository does not follow semantic versioning.
Changes are historical, not product-based.
---
## Status
This changelog marks the **first frozen public research state** of the 512 archive.
