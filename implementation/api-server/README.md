# api-server

**Status:** Placeholder — code to be exported from the reference build.

---

The service layer in front of the kernel.

## Current scope

A health route. It is not the kernel's evaluation service and not a CVS
adapter. Evaluation stays in `kernel-512` as a pure library call; this
server exists so deployers have a place to put transport, authentication,
and rate limiting without touching the kernel.

## Rules

- The server never re-implements gate logic. It calls the kernel and
  reports what the kernel returned.
- The server never mints CVS receipts. Observation events go through the
  publisher seam to the independent CVS Capture Plane; this server does
  not stand in for it.
- Any future evaluation endpoint must preserve the kernel's contract:
  pure evaluation over (bound record, action proposal, live inputs),
  ALLOW/DENY with the failed check named, honest nulls on missing evidence.
