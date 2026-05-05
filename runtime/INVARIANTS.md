# 512 Runtime — Invariants

All invariants must evaluate TRUE at execution time.

Evaluation is deterministic and stateless.

---

## Invariants

inv_1 — identity_present  
context.identity must exist

inv_2 — consent_valid  
context.consent must be true

inv_3 — action_defined  
intent.action must exist

inv_4 — within_limit  
intent.amount ≤ constraints.max_amount

inv_5 — timestamp_present  
context.timestamp must exist

inv_6 — target_defined  
intent.target must exist

inv_7 — system_healthy  
context.system_state must equal "healthy"

---

## Evaluation

- Evaluated in order  
- First failure → DENY  
- All TRUE → ALLOW  

---

## Non-negotiable

- No partial pass  
- No weighting  
- No scoring  
- No interpretation  

All must pass.
