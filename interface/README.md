# Interface

This folder defines how external systems interact with the 512 execution boundary.

The core contract:

submit(action, constraints, state) → ALLOW | DENY

## Purpose

- Define the structure of requests
- Provide a clear integration entry point
- Ensure all required data is explicit at execution time

## Key Principles

- No hidden state
- No implicit inputs
- No interpretation inside the interface layer

## Next

See `/interface/request.schema.json` (to be added) for the formal request structure.
