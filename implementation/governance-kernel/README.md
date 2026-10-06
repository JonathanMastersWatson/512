# governance-kernel

**Status:** Placeholder — code to be exported from the reference build.

---

The web application: the 512 interface panel. It presents the governance
kernel model, collects declarations, and calls `kernel-512`. It does not
re-implement the kernel.

## Expected layout

| Area | Responsibility |
|---|---|
| Worksheet | The seven question panels (I accountability, II participation, III exit, IV terms, V change notice, VI human escalation, VII binding), one per invariant. Page-local draft state; three field states surfaced honestly (answered / declined / unanswered). |
| Domain profiles | Label/copy packs mapped onto the canonical question spine (generic default; VEX commercial as a selectable profile). Profiles supply wording only — they cannot reorder or replace core questions. |
| Binding flow | The separate, explicit bind action: compiles the declaration, emits the canonical hashed `BindRecord`, and only then enables the gate. Consent is optional; binding is explicit. |
| Commit Gate UI | Builds the action proposal (action type, actor/declaration reference, delegation chain, object and terms descriptors, live inputs) and displays the gate decision with the failed check named. |
| Observation events | Builds CVS observation-event descriptors (bind, evaluation, outcome, withdrawal, obligation creation) for the publisher seam. Transport is configured separately; unwitnessed state is shown honestly, never implied. |
| Training replays | Scripted walkthroughs (worked example, fault catalog). Fictional only: a replay cannot bind a record or create a gate receipt, observation event, or CVS receipt — stated in the UI. |

## Rules the UI must keep

- Draft answers stay page-local; nothing is sent anywhere until explicit bind.
- Undeclared fields are draft-only and unbindable: binding requires every
  field answered or explicitly declined.
- Sensitive identifiers are verify-and-discard: the raw value never enters
  the bound record.
- The UI never implies witnessing it cannot prove. If the CVS transport is
  unconfigured, the interface says so.
