# 512 Runtime — Quick Start

Run:

cd runtime
./run_512 request.json

Expected:

DENY inv_2

Fix request.json until:

ALLOW

Rules:
- Missing or invalid input → DENY
- No retries
- No fetching
- No interpretation

Nothing becomes real unless the boundary allows it.
