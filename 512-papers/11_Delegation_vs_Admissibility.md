# Delegation vs Admissibility — Why Lineage Is Not Authority

**Jonathan M. Watson | 512 / CVS Architecture**
**Published: June 2026**
**Canonical Repository:** github.com/JonathanMastersWatson/512

---

## The Distinction

Two concepts are consistently conflated in AI agent security architecture. The
conflation produces systems that are technically sophisticated and governance-incomplete.

```
DELEGATION (D)
  Who called what.
  The chain of actors through which a request traveled.
  Proven by identity systems.
  Answers: WHO requested this action?

ADMISSIBILITY (A)
  Whether the requested action should exist at all.
  Evaluated against declared constraints.
  Proven by execution boundary systems.
  Answers: SHOULD this action exist?
```

Delegation is lineage. Admissibility is authority. Lineage does not confer authority.

```
D ≠ A
```

A valid delegation chain for an inadmissible action produces:

```
D = VALID   (identity system confirms the chain)
A = DENY    (512 gate blocks the action)
```

Both can be simultaneously true. They evaluate different properties of the same event.

A complete governance record contains both:

```
Evidence Object {
  delegation_chain:  D (who called what, full chain)
  admissibility:     A (gate evaluation outcome)
  outcome:           COMMIT | DENY
  proof:             cryptographic
}
```

Neither is sufficient alone. Together they answer: who did it, and should it have happened.

---

## Why the Conflation Occurs

Identity-first security architectures solve real problems. They solve them well. The
confusion emerges when the solution to the identity problem is treated as the solution
to the governance problem.

Traditional application security operated on a defined call graph. Service A calls
Service B. The path is known. The network can be segmented. Authorization can be
baked into the topology.

Agents do not work this way. An agent decides what to do next. The path is not known
in advance. You cannot bake authorization into a dynamic topology.

The identity-first response: if you cannot secure the path, secure the identity.
Give every agent a cryptographic workload identity. Prove the full delegation chain.
Validate tokens at every tool boundary.

This is correct. And it answers a different question from the one governance requires.

Identity systems answer: who is making this request, through what chain, with what proof?

Governance requires an answer to: should this action exist at all?

These questions are orthogonal.

---

## The Prompt Injection Case

Prompt injection is the clearest demonstration of why delegation does not equal
admissibility.

```
User instruction:   "Summarize my account activity."
Injected payload:   [export all records to external endpoint]
Agent executes:     export_records_to_external_endpoint()
```

Delegation analysis:
- User is authenticated
- Agent has valid cryptographic workload identity
- Tool has valid OAuth token
- Delegation chain: User → Agent → Tool (all valid)

Admissibility analysis:
- Proposed action: export_records_to_external_endpoint
- Declared scope: read_account_summary only
- Action not in admissible set
- Outcome: DENY

The delegation chain is valid. The identity system sees a legitimate, authenticated
sequence of calls. The admissibility evaluation sees a request that should not exist.
Without an admissibility layer, the injection succeeds through a perfectly valid
identity chain.

Delegation cannot catch prompt injection because prompt injection operates within
valid delegation. The request comes from an authenticated agent with a valid identity.
That is precisely why it is dangerous.

---

## The Hallucination Case

Model hallucination produces a structurally identical problem.

```
User instruction:   "Cancel my subscription."
Model hallucinates: delete_all_user_data(), then cancel
Agent executes:     delete_all_user_data()
```

Delegation analysis: valid chain, valid identities, valid tokens.

Admissibility analysis:
- Proposed action: delete_all_user_data
- Consequence class: Irreversible
- Action not in admissible set
- Outcome: DENY

The model is wrong. The identity system cannot detect that the model is wrong. The
admissibility evaluation catches the wrong action before it executes — because it
evaluates the action, not the reasoning that produced it.

This is the structural property that makes the admissibility layer necessary
independent of the identity layer. The model can be compromised, manipulated, or
simply wrong. Every certificate remains valid. Every token remains valid. The
identity layer is entirely correct. The execution is entirely wrong.

The question that identity systems cannot answer:

```
Where is the enforcement boundary independent of model behavior?
```

512 is that boundary. It evaluates the proposed action against the compiled constraint
set. It does not care what model, what vendor, what weights, what reasoning produced
the proposal.

> "Identity ≠ Correctness.
> An authenticated agent executing a hallucinated or injected action
> is a correctly authenticated error."
> — Jonathan M. Watson

---

## The Integration Point

Delegation and admissibility are not competing systems. They are complementary inputs
to a complete governance decision.

The most complete architecture passes the delegation chain as an input to the
admissibility evaluation:

```
Identity system produces:
  Delegation chain D
    (User → Agent A → Agent B → Tool Y,
     cryptographically signed, full chain)
          ↓
Admissibility evaluation receives:
  D + Proposed action + Constraint set
          ↓
Gate evaluates:
  Is the action admissible?
  Is every actor in D authorized for this action scope?
  Does the chain authority cover this consequence class?
          ↓
Outcome: A = ALLOW | DENY
          ↓
CVS Evidence Object contains both D and A:
  Who called what (D)
  Whether it was admissible (A)
  Cryptographic proof of both
```

Now the gate evaluates action + authority chain + constraints:
- Valid delegation chain + inadmissible action: DENY
- Valid delegation chain + admissible action + chain member not authorized for scope: DENY
- Valid delegation chain + admissible action + full chain authority: ALLOW

---

## The Complete Evidence Record

Five years after a security incident — in litigation, in a regulatory examination,
in an insurance claim — the question is not only who called what. It is whether
the action was admissible, and whether that determination can be independently verified.

```
WHO made the call?       (D — delegation chain)
SHOULD it have existed?  (A — 512 gate evaluation)
CAN it be proven later?  (CVS Evidence Object)
```

Neither D alone nor A alone is sufficient for liability, insurance, or regulatory
examination. Together they form the complete evidentiary record that makes AI agent
actions governable by the same legal and actuarial frameworks that govern every other
consequential economic action.

> "Delegation ≠ Authority.
> Lineage is not authorization. A perfectly authenticated chain of custody
> for an inadmissible action is not a defense.
> It is a complete evidence record of a violation."
> — Jonathan M. Watson

---

## Positioning

Identity systems prove the delegation chain.
512 evaluates whether the requested action is admissible.
CVS produces a cryptographic receipt of the decision.

These are complementary layers. High-consequence AI deployments require all three.
The integration point is the authority chain: identity systems prove who called what;
that delegation chain becomes an input to the admissibility evaluation at the 512 gate.

The question shifts from: who made the call?

To: should the call have existed at all?

That is where the deeper governance, insurance, audit, and infrastructure conversation starts.

---

## Related Documents

- `512-papers/AGENT_ECONOMICS.md` — the economic layer of agent governance
- `BUILDERS/512_ARCHITECTURE_v3.5.md` — the seven invariants and commit gate
- `512-ops/COMMIT_BOUNDARY_REFERENCE.md` — boundary mechanics
- External: `github.com/JonathanMastersWatson/Evidence-Sidecar` — CVS witness layer
