# 512 Runtime — Submit Spec

submit(request) → ALLOW | DENY

---

## Request shape

{
  "intent": {},
  "constraints": {},
  "context": {}
}

---

## Required fields

intent.action  
intent.target  
context.identity  
context.consent  
context.timestamp  
context.system_state  
constraints.max_amount  

---

## Rules

Missing or null required field → DENY  
No defaults  
No inference  
No mutation  

---

## Output

ALLOW  

or  

DENY <invariant_id>  

or  

DENY invalid_request
