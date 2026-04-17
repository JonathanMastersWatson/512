# CHANGELOG
## Purpose
This file records **structural and documentary changes** to the 512 research archive.
It exists to:
- preserve historical integrity
- prevent silent revisionism
- allow reviewers to track evolution
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
