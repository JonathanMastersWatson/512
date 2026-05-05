# 512 Runtime — Quick Start

Run:

cd runtime
./run_512 request.json

Expected:

DENY inv_2

---

Fix request.json until:

ALLOW

---

## Contract

See:

submit_spec.md

---

## Tests

Run:

./run_tests

---

## Rules

Missing or invalid input → DENY  
No retries  
No fetching  
No interpretation  

---

## Output

ALLOW  

or  

DENY <invariant_id>  

or  

DENY invalid_request  

---

Nothing becomes real unless the boundary allows it.
