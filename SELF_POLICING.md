# Self-policing

**Document:** `512-self-policing` · **Version:** 1.0 · **Date:** 2026-10-06
**Author:** Jonathan M. Watson
**Status:** Architectural specification. Describes how the seven invariants
enforce themselves through detectability. Does not modify the canonical 512 kernel.

---

## 1. The claim

The seven constraints police themselves.

Every marketplace has rules; they are enforced by whoever holds power, which is
why nobody trusts them. 512 replaces enforcement-with-power by
enforcement-with-structure: each violation is structurally visible through the
system's own rules. No watcher is required. Nobody needs to watch the
marketplace — watch it try to cheat.

The historical analogue is double-entry bookkeeping: it did not prevent
embezzlement; it made the books balance-or-not a mechanical fact, and that
changed commerce.

## 2. Detectability, not prevention

Enforcement is detectability, not prevention. Prevention-by-force would itself
violate Invariant I — a system that restrains people by force commits the force
it prohibits. Every attempt to govern by control, stop, prevent, and review
reproduces the same failure: a control mindset that offloads responsibility
onto whoever holds the controls.

So 512 does not prevent violations. It makes them visible:

- **V** makes hiding detectable. No hidden rules means a hidden action has
  nowhere to stand — its absence from the declared record is itself the evidence.
- **VII** makes silent change detectable. The bound record is content-hashed,
  so any silent change is a hash mismatch — mechanical, not judgmental.
- **II×IV** makes stale consent detectable. Consent references the exact
  terms_hash it was given under; consent to version N does not silently carry
  to version N+1.
- **VI×I** makes fabrication detectable. Where verification fails, the system
  emits an honest null naming the failed check instead of a fabricated result.
  I prohibits fraud; VI supplies the honest alternative.

## 3. The cross-action matrix

Each pair names how one invariant constrains the operation of another. The
constraints do not merely coexist; they check each other.

| Cross-action | What it makes visible |
|---|---|
| **VII×V** | A rule change is either declared — new version, new hash, renewed consent — or it is a hash mismatch. There is no third option. VII gives V teeth: "no hidden rules" holds because any rule change alters the hash. |
| **II×IV** | Consent is bound to the exact terms hash it was given under. Stale consent — consent invoked under terms that have since changed — is detectable because the hashes differ. New terms require renewed consent. |
| **III×II** | Consent that cannot be withdrawn is not consent. The exit path is what makes II's voluntariness real rather than nominal: a system that holds you after you withdraw has converted your past yes into present force. |
| **VI×I** | At the point of failure, I's fraud prohibition meets VI's honest-null requirement: the system must emit a named null rather than fabricate a passing result. Fabrication would be fraud; the honest null is the lawful alternative. |
| **V×VI** | The null must name the failed check. A null that does not say why is itself a hidden rule — V constrains VI's nulls. Silence about the reason violates V even when the outcome is honest. |
| **VII×III** | Withdrawal is forward-only. It stops future distribution and access, but it never mutates receipts — the witnessed past stays verifiable. Exit changes what happens next, not what happened. |
| **II×VII** | Binding is the highest-stakes act in the system: it makes the record immutable. Therefore bind requires explicit consent — no silent binding, no implied binding, no binding by continued use. |
| **I×PLATFORM** | The platform is not above the kernel. Coercive onboarding — walls before value, dark patterns, forced declarations — is itself a force/fraud violation by the platform, and it is structurally visible as such. The kernel constrains the operator, not just the participants. |

## 4. The hinge

Stated plainly: the self-policing claim has one hinge. It holds given
tamper-evident receipts plus external anchoring. The cross-actions make
violations visible *in the record*; the record itself must be tamper-evident,
and tamper-evidence must be anchored outside the operator's control.

Until the anchor is real, there is exactly one unpoliced party: whoever
controls the receipt store. That is not a refutation — it is the next thing to
build, and now the doctrine names what it is for. The anchor is not a feature;
it is what closes the loop.

## 5. Witness, not warden

The self-check runs as witness-not-warden: canonical, content-hashed check
functions — pure deterministic Booleans over the bound record plus live inputs —
evaluated event-driven and on a rolling heartbeat, with check receipts written
into CVS. The checker declares failures and honest nulls. It never mutates
records or receipts. A warden prevents; a witness declares.

## 6. What this answers

- *"Why seven constraints instead of seventy pages of Terms of Service?"* —
  because the seven check each other; seventy pages need a reader with power.
- *"Who watches the marketplace?"* — nobody needs to. The structure is the
  watcher; the participants are the verifiers.

## 7. Demonstration

The doctrine is demonstrable, not just statable. Each beat is a cross-action
firing live:

- Tamper with a price without a new version → hash mismatch → DENY. (VII×V)
- Leave a field undeclared → bind refuses; undeclared is draft-only, unbindable. (V)
- Consent invoked under changed terms → DENY, stale consent named. (II×IV)
- Verification fails → honest null naming the failed check; nothing served. (VI×I, V×VI)
- Actor withdraws → future access stops; past receipts remain verifiable. (VII×III)

A demo of 512 is not a feature tour. It is violations getting caught by the
system's own rules.

## 8. What self-policing is not

- Not prevention. The system does not stop you from acting; it withholds its
  attestation and records what happened.
- Not punishment. Detection carries no penalty inside the system; consequences
  are priced by the market and judged at human speed.
- Not trust in the operator. The operator is constrained by I×PLATFORM like
  any participant.
