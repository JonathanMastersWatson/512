# 512 Reference Implementation

**Status:** Scaffold — placeholder framework. Implementation code to be
exported from the reference build into the folders below.

---

## What this is

The reference implementation of the 512 governance kernel: the worksheet,
the binding flow, the Commit Gate, and the obligation fold — as runnable
TypeScript. It exists so future developers can run the checks, not just
read about them.

## What this is not

- Not the specification. The normative specification is `512-core/`
  (canonical kernel, canon, genesis records). Where code and spec disagree,
  the spec governs.
- Not the frozen minimal gate. `runtime/` holds the earlier Python
  reference gate under `INTERFACE_LOCK.md` — its interface is frozen and
  it is left untouched. This folder is the full governance platform;
  `runtime/` is the minimal evaluator. They serve different readers.

## Structure

| Folder | Contents |
|---|---|
| `kernel-512/` | The shared TypeScript kernel library: canonical schema, worksheet definition, draft and gate checks, binding and record compilation, canonical JSON hashing, Commit Gate evaluator, obligation creation and fold. The load-bearing code. |
| `governance-kernel/` | The web application (the interface panel): the seven-question worksheet, draft state, explicit binding flow, Commit Gate UI, training/scripted replays. Imports `kernel-512` directly. |
| `api-server/` | The service layer in front of the kernel. Currently a health route; not the kernel's evaluation service or a CVS adapter. |

See each folder's README for the expected module layout and public boundary.

## License

The repository's `LICENSE` (CC BY 4.0) covers written documentation only.
All code in this folder is released under the **Apache License 2.0**.
See `LICENSE-APACHE.md`. The full license text ships with the code drop;
the notice file is already in place.

## Sealing

This folder is included in the repository's sealed archive state. The
December 5, 2026 final seal covers whatever implementation code is present
at that date. See `LIVING_DOCUMENTS.md`.
