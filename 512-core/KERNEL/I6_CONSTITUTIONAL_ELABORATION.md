# I6 Constitutional Elaboration

**Jonathan M. Watson | 512 / CVS Architecture**
**Status: Constitutional Authority**
**Canonical Repository:** github.com/JonathanMastersWatson/512

---

## 1. Purpose

This document is the authoritative elaboration of Invariant 6 of the 512 Kernel.

It exists because a vocabulary audit identified a terminology defect in the elaboration layer. The phrase "fail open" accumulated multiple meanings across repository documents. Those meanings are not wrong within their individual contexts. They are incompatible as a shared term — and that incompatibility is a constitutional defect.

This document resolves the defect by establishing the constitutional intent of I6 and naming each of its constituent obligations precisely.

The kernel is not defective. The kernel statement of I6 is a constitutional compression — three distinct obligations expressed in one sentence at maximum density. The defect is in the elaboration layer, which inherited the parent phrase without decomposing its constituent parts, and which imported the engineering definition of "fail open" in place of the constitutional one.

This document corrects that. It does not change the kernel.

---

## 2. Authority

This document is authoritative over:

- all repository documents that reference Invariant 6 or "fail-open" behaviour
- all implementation documents describing gate unavailability, denial disclosure, or human control obligations
- all CVS documents describing evidence requirements on failure or denial events
- all derivative documents, standards submissions, and IP filings that cite I6

Where any conflict exists between this document and a prior elaboration of I6 in any repository document, this document governs.

Where any conflict exists between this document and the kernel statement of I6, the kernel governs.

The kernel always governs.

---

## 3. Kernel Statement

The kernel statement of Invariant 6 is:

> On failure, systems must fail open, reveal governing rules, and default to human choice.

This statement is unchanged. Its SHA-256 commitment is unchanged:

```
7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5
```

No word in this statement is modified by this document. No word is reinterpreted. No word is replaced.

This document explains the statement. It does not supersede it.

---

## 4. Constitutional Intent of I6

I6 was created to solve one problem: authoritative concealment.

The problem is a system that exercises authority — through rule application, enforcement, or denial — while concealing the basis for that authority. The rule that produced the outcome is invisible. The authority behind it is undeclared. The decision is uncontestable.

512 was discovered as a response to the observation that control was being exercised at the semantic layer — rules hidden, authority undisclosed, decisions presented as neutral process rather than the exercise of power. I6 is the invariant that makes authoritative concealment structurally impossible in any system satisfying 512's properties.

I6 in one sentence: *No system may exercise authority while concealing the basis for that authority.*

The kernel sentence expresses this through three clauses. They do not all carry the same trigger. Reading the sentence as though "on failure" conditions all three clauses is the error that produced the elaboration drift.

**"On failure" — failure means malfunction.**

Failure carries its ordinary meaning: the system cannot function as intended. Gate crash. Evaluation timeout. Network partition. Inability to determine. This is the trigger for the first clause only. It is not a restatement of "adverse outcome." A credit denial is not a failure. A moderation decision is not a failure. These are the system working correctly. Stretching "failure" to cover correct adverse outcomes is indefensible against ordinary reading — by a regulator, a patent examiner, or a court.

**"systems must fail open" — the malfunction clause.**

When the system cannot evaluate — when it genuinely fails — it must not weaponise its own inability to function as a mechanism of restriction. This clause governs gate behaviour on infrastructure failure. Its constitutional meaning is resolved in §9 below, where the $50,000 / $500,000 transfer test establishes that "fail open" in the context of gate failure means: the commit boundary holds, the reason is disclosed, and the human party retains the ability to retry. It does not mean execution proceeds without admissibility being established.

**"reveal governing rules" — a permanent obligation.**

This clause is not conditioned on failure in the same way. Governing rules are not revealed only when the system malfunctions. They are revealed always — on DENY, on any outcome in which a governing rule was applied. The kernel expresses this in the context of failure because failure is the moment when concealment is most tempting and most harmful. But the obligation is not limited to failure events. It applies to every gate output. This is the basis for Transparent Denial.

**"and default to human choice" — a permanent constitutional floor.**

Human choice is not the default only when the system fails. It is the default always. The system does not accumulate authority over the human party through its operation. Exit, contest, and revocation remain available regardless of what the system determines. This is Human Default. It fires on every adverse outcome and every operational state.

**The structural reading:**

The kernel sentence opens with "on failure" and lists three obligations. Only the first — fail open — is exclusively failure-triggered. The other two are permanent obligations that the failure scenario makes most urgent to state, but whose scope is not limited to failure events.

---

## 5. Why Elaboration Is Required

The elaboration layer drifted in two distinct ways, both of which required correction.

**First drift — Def B contamination:**

The kernel phrase "fail open" was imported with its engineering definition — gate unavailable → allow execution — and applied to all three I6 obligations simultaneously. Transparency obligations and human sovereignty guarantees were labelled "fail-open" by proximity, producing three incompatible meanings under one term. This drift is documented in the vocabulary audit and corrected by naming the three obligations separately.

**Second drift — Continuity Behaviour as gate-output doctrine:**

The elaboration layer established "Continuity Behaviour" as the gate-output doctrine for infrastructure failure: gate unavailable → no gate output → continuity handler opens commit path → execution proceeds → gap recorded. This doctrine was constitutionally challenged by the $50,000 / $500,000 transfer test: if a proposed transfer of $500,000 reaches the commit boundary against a manifest limit of $50,000, and at that moment infrastructure fails, the Continuity Behaviour doctrine permits the $500,000 transfer to commit — ungoverned, without admissibility established, with only a gap record as evidence of the ungoverned period.

That outcome is constitutionally wrong. The transfer was not authorised. Admissibility was not established. The gap record is honest but does not undo an irreversible state change. A governance architecture that permits unauthorised high-consequence actions because the gate was unavailable does not satisfy I6's constitutional purpose.

**The resolution — Evaluation-Unavailable DENY:**

DENY means permission to commit not granted. Two causes produce DENY:
1. Constraint violation — invariant evaluated and failed
2. Evaluation unavailability — infrastructure failure, evaluation could not complete

In both cases the commit path remains closed. The causes differ. The outcome does not. The disclosure differs — constraint violation DENY identifies the violated invariant; evaluation-unavailable DENY identifies the infrastructure failure and permits retry. Both satisfy Transparent Denial. Both hold the commit boundary.

Continuity Behaviour is retired as a gate-output doctrine. The term "continuity" remains available at the CVS sidecar and transport layers where it retains its correct meaning: evidence capture continues even when upstream components fail.

---

## 6. Constitutional Decomposition of I6

I6 contains three obligations. They are named separately from this document forward.

The constitutional hierarchy is:

| Priority | Obligation | Named Term | Trigger |
|---|---|---|---|
| Primary | Basis for any gate output must be visible and inspectable | **Transparent Denial** | Any DENY — whether constraint violation or evaluation unavailability |
| Floor | Human party retains agency; exit, retry, and contest remain available | **Human Default** | Any adverse outcome without exception |
| Gate-output doctrine on infrastructure failure | Commit boundary holds; reason disclosed; retry permitted | **Evaluation-Unavailable DENY** | Gate technical unavailability only |

These three obligations are not alternatives. They are cumulative. Human Default fires on every adverse outcome without exception. Transparent Denial fires on every DENY regardless of cause. Evaluation-Unavailable DENY fires when the gate cannot complete evaluation.

---

## 7. Obligation One — Transparent Denial

**Term:** Transparent Denial

**Constitutional priority:** Primary. This is the obligation I6 was written to mandate.

**Trigger:** Any DENY output. Gate evaluates and produces DENY (constraint violation). Or gate cannot evaluate and produces DENY (evaluation unavailability). In both cases: the basis for the DENY must be disclosed.

**Behaviour:**

The governing rule or infrastructure failure is disclosed. The basis for the outcome is declared. The decision is inspectable by the affected party and by independent verifiers. The human party can see what produced the DENY and on what basis.

**What this obligation is not:**

Transparent Denial does not require disclosure of implementation internals, detection heuristics, model weights, or security-sensitive logic. It requires disclosure of what governed the decision — the rule, or the infrastructure failure — not how the system executes governance internally.

**The constitutional boundary — what ruled versus how it works:**

The boundary between required and prohibited disclosure is drawn by a single question applied to any candidate disclosure:

*Does this information help the affected human party understand what produced the DENY — or does it help any party circumvent the rule's future application?*

If the former: required. If the latter: prohibited. If both: the minimum disclosure that serves understanding without enabling circumvention is required; the remainder is prohibited.

**The three-question test — what Transparent Denial must answer:**

The affected human party must be able to answer three questions from the disclosure alone:

1. **What produced the DENY?** Either: the specific invariant or constraint that failed (constraint violation DENY), or: the infrastructure failure that prevented evaluation (evaluation-unavailable DENY). Not a category. Not a department. The actual cause.

2. **Why did it apply to this specific proposal?** The factual basis connecting the cause to the proposal. For constraint violation: "The proposed action exceeded the manifest limit of $50,000." For evaluation unavailability: "Evaluation could not complete due to power loss at timestamp X. No admissibility determination was made."

3. **How can the human party contest, retry, or exit?** The structural path forward. For evaluation-unavailable DENY: retry is explicitly permitted when the gate is available. For constraint violation DENY: contest path and exit path are disclosed.

A DENY that cannot answer all three questions does not satisfy Transparent Denial regardless of how much other information is disclosed.

**Constitutional basis for the disclosure boundary:**

The prohibition on implementation disclosure is not a general security exception. It derives from I1 and I5.

I1 prohibits force and fraud against any human — including third parties. Disclosing detection heuristics or security logic enables circumvention, which enables harm to third parties those mechanisms protect. A transparency obligation to one party does not override a protection obligation to others. Where full disclosure would enable harm to third parties, the disclosure boundary is set by I1.

I5 prohibits hidden rules and unilateral change. Revealing security implementation details forces the system to change its detection mechanisms to maintain effectiveness — producing exactly the unilateral rule mutation I5 prohibits. The disclosure obligation and the stability obligation resolve together: disclose the rule, not the mechanism that enforces it.

**Required and prohibited disclosure table:**

| Information | Status | Constitutional basis |
|---|---|---|
| Which invariant was violated (I1–I7) | **Required** (constraint violation DENY) | The rule itself — "reveal governing rules" |
| Infrastructure failure cause and timestamp | **Required** (evaluation-unavailable DENY) | Basis for the DENY must be disclosed |
| Factual basis connecting the cause to this specific proposal | **Required** | Human party must understand why their proposal was denied |
| Constraint reference — policy ID, version, specification hash | **Required** | I5 — rules must be inspectable |
| What the rule prohibits in general terms | **Required** | The rule is public; only its detection mechanism is protected |
| Retry path (evaluation-unavailable DENY) | **Required** | Human Default — retry is the human party's right |
| Contest and exit path | **Required** | Human Default — "default to human choice" |
| How the system detects rule violations | **Prohibited** | Implementation, not rule; enables circumvention — I1 |
| Scoring thresholds or confidence values | **Prohibited** | Implementation; reveals exploit path — I1 |
| Model weights or embeddings | **Prohibited** | Implementation; not a rule |
| Data belonging to third parties | **Prohibited** | I2 and I3 rights of those parties |
| Infrastructure or deployment topology | **Prohibited** | Not a rule; reveals attack surface — I1 |
| Specific signals that triggered detection | **Prohibited** | Detection mechanism, not the rule — I1 |

**Proof without disclosure:**

A class of cases exists where the minimum required disclosure would itself reveal prohibited information. The factual basis for a denial sometimes cannot be stated without revealing detection logic or third-party data.

The constitutional resolution is proof without disclosure. The system provides cryptographic evidence that the governing rule was correctly applied — without revealing the mechanism of application.

Acceptable proof mechanisms:
- Signed execution receipts confirming which invariant was evaluated and the result
- Specification hash confirming which constraint set was in force at evaluation time
- Trusted execution environment attestation confirming evaluation occurred correctly under the canonical specification
- Reproducible policy identifier — the human party can verify the rule exists and applies to their category of action, without the system revealing how it detects violations

This mechanism is structurally present in CVS. The Evidence Object provides cryptographic proof of which invariant was evaluated, under which specification, at what time. It does not reveal detection logic. It satisfies "reveal governing rules" — the rule is identified and its application is proven — without requiring disclosure of implementation.

Proof without disclosure is the constitutional resolution wherever full factual disclosure would violate I1 or expose third-party data. It is not an escape from Transparent Denial. It is Transparent Denial satisfied by a different evidentiary path.

**Architectural expression:**

```
Gate evaluates → DENY (constraint violation)
  → failed invariant identified (I1–I7)
  → governing rule disclosed (rule identity, not detection mechanism)
  → factual basis stated (what the proposal lacked, not how detection worked)
  → contest and exit path disclosed
  → decision recorded in witness layer
  → Evidence Object: violated invariant ID, constraint reference, proposal hash, spec hash

Gate cannot evaluate → DENY (evaluation unavailability)
  → infrastructure failure cause disclosed
  → timestamp of failure disclosed
  → no admissibility determination was made — stated explicitly
  → retry path disclosed
  → decision recorded in witness layer
  → Evidence Object: evaluation-unavailable indicator, failure cause, proposal hash, spec hash
  → where factual basis cannot be stated without revealing prohibited information:
      → proof-without-disclosure mechanism engaged
      → cryptographic attestation replaces factual statement
```

**Relationship to CVS:**

Every DENY event — whether constraint violation or evaluation unavailability — produces a CVS Evidence Object. The Evidence Object includes the DENY type, the specification hash confirming which constraint set was in force, and the proposal correlation ID. The DENY is independently verifiable by any party with access to the public ledger and the canonical repository.

---

## 8. Obligation Two — Human Default

**Term:** Human Default

**Constitutional priority:** Structural floor. Fires on every adverse outcome without exception.

**Trigger:** Any adverse outcome — constraint violation DENY, evaluation-unavailable DENY, restriction, system failure. Human Default does not fire only on one DENY type. It fires on every condition in which the human party experiences an adverse outcome from the system.

**Behaviour:**

The 512 system does not permanently and opaquely remove a human party's standing to contest, understand, retry, or exit. The system does not use an adverse outcome as a mechanism to further concentrate its own authority over the human party.

**The essential distinction — human agency versus immediate operational control:**

The kernel says "default to human choice." It does not say "default to this specific human's immediate operational control in this specific moment."

**Human agency** is the permanent constitutional condition Human Default protects. It includes: the right to know what produced the DENY, the right to contest through appropriate mechanisms, the right to retry when conditions permit, the right to exit the 512 system itself, the right to be treated as an agent rather than a subject. Human agency cannot be suspended by the 512 system on its own authority.

**Immediate operational control** is the ability to act, transact, or commit in this specific moment. This can be legitimately suspended — by a constraint violation, by infrastructure failure, by external lawful authority.

**The constitutional test for any edge case:**

*Is the deprivation of operational control generated by the 512 system on its own authority, opaquely, without recourse — or is it generated by a disclosed constraint or external authority whose basis is declared and whose exercise is contestable through an appropriate mechanism?*

If the former: Human Default violation.
If the latter: Human Default satisfied.

**What qualifies as external authority — the single constitutional question:**

*Could the system operator produce a different outcome without violating a constraint that exists independently of the operator's own will?*

If yes: system authority. Transparent Denial and Human Default apply in full.
If no: external authority — the 512 system records and executes the constraint transparently.

**The three diagnostic indicators** (evidence assisting the single question, not an independent parallel test):

**Indicator 1 — Origin.** Was the authority constituted by a process outside the operator's control?

**Indicator 2 — Modification.** Can the operator unilaterally change the authority?

**Indicator 3 — Enforcement.** Is the authority enforced by a body that does not derive its mandate from the operator?

When all three indicators point toward independence, the constitutional question is almost certainly answered no. When any indicator points toward operator control, the constitutional question must be asked directly.

**Authority laundering:**

The authority laundering pattern: *"The system did not make this decision. The policy did."*

The constitutional question defeats this directly: could the operator have written a different policy? Could they have applied it differently? If yes — system authority. The policy is the operator's own instrument. The decision is the operator's own act.

**Authority classification:**

| Authority | Constitutional question | Classification |
|---|---|---|
| Court order | Operator cannot produce different outcome | External |
| Emergency statute / regulation | Operator cannot produce different outcome | External |
| Statute directly mandating outcome | Operator cannot produce different outcome | External |
| Clinical safety protocol (standards body) | Operator cannot produce different outcome | External |
| Industrial safety standard (independent body) | Operator cannot produce different outcome | External |
| Government agency guidance (non-binding) | Operator chooses whether and how to apply it | **System authority** |
| Platform moderation policy | Operator wrote, modifies, and enforces | **System authority** |
| Employer policy | Operator wrote, modifies, and enforces | **System authority** |
| Corporate policy | Operator wrote, modifies, and enforces | **System authority** |
| Bank / financial institution policy | Operator wrote and applies its own policy | **System authority** |
| Bank's interpretation of statute | Operator determines interpretation | **System authority** |
| Private arbitration | Operator drafted clause and selected forum | **System authority** |

**The regulatory overlay resolution:**

The statute itself, where it directly and unambiguously mandates the outcome, is external authority. The operator's interpretation and application of statute is system authority.

**Duration and recourse:**

Human Default prohibits permanent opaque deprivation generated by the system on its own authority. Temporary deprivation with disclosed basis and available recourse — including retry on evaluation-unavailable DENY — satisfies Human Default.

**What this obligation is not:**

Human Default is not a technical mode. It is a constitutional guarantee about what the 512 system must not become.

Human Default is not satisfied by providing a complaints form. Exit and retry must be structurally possible — not procedurally promised.

Human Default does not govern courts, regulators, law enforcement, or emergency safety systems. It governs the 512 system. External authorities operate at a layer above the commit boundary.

**Architectural expression:**

```
Any adverse outcome (constraint violation DENY OR evaluation-unavailable DENY)
  → apply constitutional question: could operator alone have produced a different outcome?
  → if system authority:
      → Transparent Denial fires in full
      → basis for DENY disclosed
      → retry / exit / contest structurally available
      → system does not increase its control as consequence of adverse outcome
  → if external authority (all indicators satisfied AND operator could not alone modify outcome):
      → external mandate recorded transparently
      → basis disclosed to extent external authority permits
      → where basis cannot be disclosed: proof-without-disclosure engaged
      → human party's legal standing to contest external authority preserved
  → in all cases:
      → human party treated as agent, not subject
      → deprivation is temporary and bounded, or external authority is independently contestable
      → permanent opaque deprivation by system's own authority: prohibited
      → authority laundering — system authority presented as external authority: prohibited
```

---

## 9. Obligation Three — Evaluation-Unavailable DENY

**Term:** Evaluation-Unavailable DENY

**Constitutional status:** Derived gate-output doctrine for infrastructure failure. This is what I6's constitutional purpose — no concealed authority, human agency preserved, admissibility required for ALLOW — necessarily requires when applied to the specific case of gate technical failure.

**Note on prior terminology:** "Continuity Behaviour" was the prior term for this obligation. It is retired as a gate-output doctrine following the $50,000 / $500,000 transfer test (documented below). The term "continuity" remains available at the CVS sidecar and transport layers where it retains its correct meaning.

**Trigger:** Gate unavailable. Evaluation timeout. Gate crash. Network partition. Any condition under which the gate cannot complete evaluation.

**Behaviour:**

The gate produces DENY. The DENY reason is: evaluation unavailable. The commit path remains closed. The cause of unavailability is disclosed. Retry is explicitly permitted when the gate is available. The witness layer records the evaluation-unavailable event.

**The $50,000 / $500,000 transfer test — why prior doctrine was wrong:**

The prior doctrine — gate cannot evaluate → continuity handler opens commit path → execution proceeds → gap recorded — was challenged by a concrete governance scenario:

- Manifest limit: $50,000
- Agent proposal: transfer $500,000
- At the moment the proposal reaches the commit boundary: DPU power loss / network partition / evaluation timeout

Under the prior doctrine: the $500,000 transfer commits. The gap record proves it was ungoverned. The transfer is irreversible.

The constitutional analysis of that outcome:
- Who authorised the $500,000 transfer? Nobody. The continuity handler is not an authority. No admissibility determination was made.
- Was admissibility established? No. "We recorded that it was ungoverned" does not justify permitting an unauthorised irreversible transfer.
- Was the transfer governed? No. Ungoverned. The gap record is honest but does not undo the transfer.

This outcome is constitutionally wrong. The prior doctrine failed on all five governance criteria: machine-speed commerce, agentic systems, authority transparency, governance integrity, and insurability. The $500,000 transfer was not authorised. The commit boundary did not hold.

**The resolution — DENY = permission to commit not granted:**

DENY means permission to commit not granted. Two causes:
1. Constraint violation — invariant evaluated and failed. Commit path remains closed.
2. Evaluation unavailability — infrastructure failure, evaluation could not complete. Commit path remains closed.

In both cases the commit boundary holds. The causes differ. The outcome does not.

Under the Evaluation-Unavailable DENY model:
- The $500,000 transfer does not commit.
- The DENY is disclosed: evaluation unavailable, infrastructure failure at timestamp X, retry permitted.
- The human party is returned to a position where they can retry when the gate is available.
- No irreversible state change occurred without admissibility being established.

**Why this satisfies I6:**

"Fail open" in the kernel means: the system must not weaponise its own failure as a mechanism of concealed restriction. Evaluation-Unavailable DENY is not silent blocking — it is disclosed, reasoned, and retry-permitted. The basis is declared. The human party knows what happened and what to do next. No authority is concealed. The commit boundary held because admissibility requires evaluation — not because the gate operator took the gate down to control outcomes.

"Reveal governing rules" is satisfied: the admissibility requirement — that no action may commit without evaluation — is the governing rule. It is disclosed in the DENY reason.

"Default to human choice" is satisfied: retry is structurally available. The human party chooses whether to retry, escalate, or abandon.

**What this obligation is not:**

Evaluation-Unavailable DENY is not a constraint violation. No invariant failed. The violated invariant field is absent from the Evidence Object. The disclosure is the infrastructure failure, not a failed invariant.

Evaluation-Unavailable DENY is not permanent denial. It is temporary — retry is permitted when the gate is available. A system that produces permanent Evaluation-Unavailable DENY without retry path violates Human Default.

Evaluation-Unavailable DENY is not equivalent to constraint violation DENY for disclosure purposes. The three-question test applies differently: the "what rule applied" answer is the admissibility requirement itself, not a specific invariant.

**CVS sidecar fail-open — unaffected:**

The CVS sidecar must never block execution. The sidecar is a witness, not a gate. Sidecar fail-open means: if the sidecar fails, evidence capture continues as best it can and gaps are recorded; the sidecar does not block the gate. This is an evidence-layer principle. It does not govern commit authority. "Continuity" at the sidecar layer retains its prior meaning.

**Gap records — revised semantics:**

Gap records are CVS witness layer records. Under the revised model they document the period of gate unavailability — that evaluation was attempted, infrastructure failed, DENY was produced, and the commit path remained closed. They are evidence of the unavailability event and the DENY that resulted. They are not evidence that execution proceeded. Under the revised model, execution does not proceed during gate unavailability.

**The derivation:**

```
Constitutional principle: ALLOW = admissibility established.
                          DENY = permission to commit not granted.
Scenario: gate cannot evaluate.
  → prior doctrine: continuity handler opens commit path → execution proceeds → gap recorded
      → $500,000 transfer commits without admissibility established
      → ungoverned irreversible state change
      → constitutional failure
  → revised doctrine: gate produces DENY (evaluation unavailable) → commit path remains closed
      → $500,000 transfer does not commit
      → basis disclosed: evaluation unavailable, cause, retry path
      → human party retains agency: retry, escalate, or abandon
      → constitutional purpose satisfied
  → therefore: infrastructure failure → Evaluation-Unavailable DENY
      → commit boundary holds unconditionally
      → disclosure satisfies Transparent Denial
      → retry path satisfies Human Default
      → Evaluation-Unavailable DENY = derived constitutional obligation
```

**Architectural expression:**

```
Gate unavailable or evaluation timeout
  → gate produces DENY (reason: evaluation unavailable)    [commit boundary holds]
  → failure cause disclosed                                  [Transparent Denial]
  → timestamp of failure recorded                           [evidence integrity]
  → no admissibility determination was made — stated        [honesty of record]
  → retry path disclosed and structurally available         [Human Default]
  → witness layer records evaluation-unavailable event      [CVS evidence]
  → Evidence Object: evaluation-unavailable indicator,
                     failure cause, proposal hash, spec hash,
                     timestamp, retry path
  → gap record: documents period of gate unavailability     [CVS sidecar layer]
  → DENY is not a constraint violation                      [violated invariant field absent]
  → DENY is not permanent                                   [retry explicitly permitted]
```

---

## 10. Relationship Between the Three Obligations

The three obligations are not alternatives. They are cumulative.

**On an Evaluation-Unavailable DENY event** (gate unavailable):
- Evaluation-Unavailable DENY fires — commit path remains closed, reason disclosed, retry permitted
- Transparent Denial fires — the basis for the DENY (evaluation unavailable, infrastructure failure) is disclosed
- Human Default fires — retry, contest, and exit remain available

**On a constraint violation DENY event** (gate evaluates → DENY):
- Transparent Denial fires — violated invariant disclosed, governing rule exposed
- Human Default fires — contest, exit, and retry remain available
- Evaluation-Unavailable DENY does not fire — the gate evaluated; this is a constraint violation, not infrastructure failure

**Human Default fires on every adverse outcome without exception.**

No adverse outcome satisfies I6 unless Human Default is also satisfied. Human Default is the constitutional floor. Transparent Denial and Evaluation-Unavailable DENY are the event-specific obligations that sit above it.

```
Gate unavailable
  → Evaluation-Unavailable DENY (commit path remains closed, reason disclosed, retry permitted)
  → Transparent Denial (infrastructure failure disclosed)
  → Human Default (retry and exit available)

Gate evaluates → DENY (constraint violation)
  → Transparent Denial (violated invariant disclosed, governing rule exposed)
  → Human Default (contest, exit, and retry available)
  → Evaluation-Unavailable DENY: does NOT fire

Gate evaluates → ALLOW
  → Transparent Denial: fires (basis for ALLOW: all seven invariants satisfied — this is the
    governing record, not a denial disclosure)
  → Human Default: fires (human party retains agency throughout)
  → Evaluation-Unavailable DENY: does NOT fire
```

---

## 11. Architectural Consequences

**Gate design:**

The gate produces exactly two outputs: ALLOW or DENY. No third value. No continuation path. No output on infrastructure failure — the gate is unavailable; DENY is produced by the system's infrastructure-failure handler, not by gate evaluation.

On constraint violation DENY: the gate must identify the failed invariant. A DENY without invariant identification violates Transparent Denial.

On evaluation-unavailable DENY: the infrastructure-failure handler produces DENY with cause and retry path. No invariant identification — evaluation did not occur.

**Infrastructure-failure handler design:**

The infrastructure-failure handler must:
- produce DENY with reason: evaluation unavailable
- record the failure cause and timestamp
- disclose the retry path
- emit an Evidence Object to the witness layer recording the evaluation-unavailable event
- never open the commit path without completed evaluation

**Witness layer design:**

CVS must produce Evidence Objects for all gate output types:
- ALLOW — per-invariant results, spec hash, proposal hash, timestamp
- DENY (constraint violation) — violated invariant ID, constraint reference, spec hash, proposal hash, timestamp
- DENY (evaluation unavailable) — evaluation-unavailable indicator, failure cause, spec hash, proposal hash, timestamp, retry path

CVS must also produce gap records at the sidecar layer documenting periods of gate unavailability. Gap records are sidecar-layer evidence. They do not imply execution proceeded.

**System design:**

Exit paths, retry mechanisms, and contest paths are system obligations — not gate obligations. The gate enforces constraints at the commit boundary. Human Default requires that the system surrounding the gate preserve human agency regardless of gate output.

---

## 12. Implementation Consequences

**Prohibited implementations:**

A system that:
- opens the commit path when the gate cannot evaluate (violates Evaluation-Unavailable DENY doctrine)
- produces DENY (constraint violation) without disclosing the failed invariant (violates Transparent Denial)
- produces any DENY and removes retry, exit, or contest options (violates Human Default)
- produces DENY (evaluation unavailable) without disclosing failure cause and retry path (violates Transparent Denial)
- treats infrastructure failure as ALLOW (violates admissibility requirement)
- treats a gap record as evidence that execution was permitted (misreads CVS evidence)
- makes gate unavailability a permanent denial without retry path (violates Human Default)

does not satisfy Invariant 6.

**Required Evidence Object fields on constraint violation DENY:**

```json
{
  "event_type": "deny",
  "deny_cause": "constraint_violation",
  "violated_invariant": "I[1-7]",
  "constraint_reference": "<governing constraint identifier>",
  "proposal_id": "<correlation ID>",
  "spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5",
  "timestamp": "<ISO 8601>"
}
```

**Required Evidence Object fields on evaluation-unavailable DENY:**

```json
{
  "event_type": "deny",
  "deny_cause": "evaluation_unavailable",
  "failure_cause": "<infrastructure failure description>",
  "retry_permitted": true,
  "proposal_id": "<correlation ID>",
  "spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5",
  "timestamp": "<ISO 8601>"
}
```

**Required gap record fields (CVS sidecar layer):**

```json
{
  "event_type": "validation_gap",
  "gap_start": "<ISO 8601>",
  "gap_end": "<ISO 8601>",
  "gap_reason": "<gate unavailability cause>",
  "gate_output_during_gap": "deny_evaluation_unavailable",
  "spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5",
  "timestamp": "<ISO 8601>"
}
```

**JSON field naming:**

The Evidence Object field previously named `invariant_6_fail_open` is a misnomer. It records the per-invariant evaluation result for I6 — a binary pass/fail outcome of successful gate evaluation. It is not a gap indicator. It does not fire on gate unavailability. Rename this field to `invariant_6_result` in all schema definitions and implementations.

---

## 13. CVS Implications

CVS is the reference witness layer for 512. Its Evidence Object schema must reflect the revised gate-output doctrine.

**Constraint violation DENY events:** CVS records a DENY Evidence Object with `deny_cause: constraint_violation`. The violated invariant field is mandatory. A DENY Evidence Object without a violated invariant ID does not satisfy Transparent Denial for constraint violation events.

**Evaluation-Unavailable DENY events:** CVS records a DENY Evidence Object with `deny_cause: evaluation_unavailable`. The failure cause and retry-permitted fields are mandatory. No violated invariant field is present — evaluation did not occur.

**Gap records:** CVS records gap records at the sidecar layer documenting periods of gate unavailability. Gap records are evidence of the unavailability period. Under the revised model they document the period during which the gate was unavailable and evaluation-unavailable DENYs were produced. The `gate_output_during_gap` field confirms no execution proceeded.

**ALLOW events:** CVS records an ALLOW Evidence Object with per-invariant results. All seven invariants must be present and passing.

**CVS sidecar fail-open:** CVS must never block gate operation. If the sidecar fails, evidence capture gaps are recorded. The sidecar does not gate the gate. Sidecar continuity — evidence capture resuming after sidecar recovery — is a sidecar-layer concern and retains its prior meaning.

**Human Default:** CVS does not enforce Human Default directly — that is a system obligation. CVS provides the evidentiary record that makes Human Default verifiable: the Evidence Object proves what outcome was produced, what caused it, and when. Independent verifiers can determine from the evidence chain whether the system preserved retry and exit options following an adverse outcome.

---

## 14. Patent and Standards Implications

The three-obligation decomposition of I6 is the authoritative structure for any IP filing that references I6 or fail-open behaviour.

**Claims must specify which obligation is claimed:**

- Claims about gate unavailability handling reference Evaluation-Unavailable DENY.
- Claims about denial disclosure reference Transparent Denial.
- Claims about human control preservation reference Human Default.

A claim that references "fail-open behaviour" without specifying which obligation is a claim against an ambiguous term. Post this document, that ambiguity is a known defect — not a prior art shield.

**For standards submissions:**

The three terms — Transparent Denial, Human Default, Evaluation-Unavailable DENY — are the vocabulary for any standards body engagement.

**For regulatory citations:**

DORA, NIST AI RMF, EU AI Act, and similar frameworks reference operational continuity, explainability, and human oversight as distinct obligations. The three I6 terms map to those categories:

- Evaluation-Unavailable DENY → operational resilience (DORA alignment — gate unavailability is documented, commit boundary holds, retry path is preserved)
- Transparent Denial → explainability / logging (EU AI Act Article 12 alignment)
- Human Default → human oversight (NIST AI RMF Govern function alignment)

---

## 15. Terminology Governance

**Transparent Denial** — the primary obligation of I6. Applies to all DENY events regardless of cause. Every DENY must produce a Transparent Denial disclosure. There are no silent denials in a 512-conforming system.

**Human Default** — the structural floor of I6. Applies to all adverse outcomes without exception. Fires always. Requires retry path on evaluation-unavailable DENY.

**Evaluation-Unavailable DENY** — the gate-output doctrine for infrastructure failure. Gate unavailable → DENY with disclosed cause and retry path. Commit boundary holds. Replaces "Continuity Behaviour" as gate-output doctrine.

**Continuity Behaviour** — retired as gate-output doctrine. Term remains available at CVS sidecar and transport layers where it describes evidence-capture continuity, not commit-path behaviour.

**"Fail open" as a phrase:**

The phrase "fail open" is not prohibited. It remains valid in contexts where its constitutional meaning is unambiguous — the I6 principle that the system must not weaponise its own failure as concealed restriction. In those contexts it is shorthand for the Evaluation-Unavailable DENY doctrine: the commit boundary holds with disclosed reason and retry path, not silent blocking. "Fail open" is prohibited as a label for Transparent Denial or Human Default.

**Prohibited usages:**

- "fail-open" used to mean disclosure on DENY → Transparent Denial
- "fail-open" used to mean return of human control → Human Default
- "fail-open" used to mean execution continues on gate failure → Evaluation-Unavailable DENY is the correct doctrine; execution does not continue
- treating gap records as evidence that execution was permitted → gap records document the unavailability period; under revised doctrine execution did not proceed
- treating evaluation-unavailable DENY as equivalent to constraint violation DENY → the causes and disclosures differ; the commit-boundary-holds outcome does not

---

## 16. Authority Over Future Documents

This document governs all future elaborations of Invariant 6 across:

- the 512 repository
- the Evidence Sidecar (CVS) repository
- the 512-canon repository
- the Constraint Architecture repository
- all derivative documents, technical papers, whitepapers, and implementation guides

Any future document that introduces a usage of these terms inconsistent with the definitions in this document is in constitutional error.

Any future document that reintroduces the prior Continuity Behaviour gate-output doctrine — execution proceeds on gate failure — is in constitutional error.

The kernel remains the highest authority. This document is the second authority for all matters concerning the elaboration of Invariant 6.

---

## Document Control

| Field | Value |
|---|---|
| Document | `I6_CONSTITUTIONAL_ELABORATION.md` |
| Version | 2.0 |
| Date | June 2026 |
| Author | Jonathan M. Watson |
| Status | Constitutional Authority |
| Canonical Repository | github.com/JonathanMastersWatson/512 |
| Kernel Commitment | SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |

### Changelog — v2.0

**Additions:**
- §5 Why Elaboration Is Required: second drift identified and documented — Continuity Behaviour as gate-output doctrine. $50,000 / $500,000 transfer test documented as the constitutional challenge that overturned prior doctrine. Evaluation-Unavailable DENY introduced as the replacement gate-output doctrine. DENY redefined as permission to commit not granted (two causes: constraint violation / evaluation unavailability).
- §9 Evaluation-Unavailable DENY: full replacement of prior §9 Continuity Behaviour. New obligation named and defined. $50,000 / $500,000 transfer test documented in full with constitutional analysis. Prior doctrine's constitutional failure demonstrated. Revised doctrine derived from constitutional principle: ALLOW = admissibility established; DENY = permission not granted. CVS sidecar fail-open explicitly separated as unaffected. Gap record semantics revised: gap records document the unavailability period and the DENY that resulted; they do not imply execution proceeded. Formal derivation chain updated.
- §10 Relationship Between the Three Obligations: fully revised. Evaluation-Unavailable DENY replaces Continuity Behaviour in the relationship model. ALLOW event added to the relationship diagram — Human Default and Transparent Denial fire on ALLOW (as the governed record) as well as on DENY.
- §11 Architectural Consequences: revised. Infrastructure-failure handler design replaces continuity handler design. Gate design clarified: gate produces ALLOW or DENY only; infrastructure-failure handler (not the gate) produces evaluation-unavailable DENY.
- §12 Implementation Consequences: revised. Evidence Object schemas updated — constraint violation DENY and evaluation-unavailable DENY have separate schemas with distinct required fields. Gap record schema updated: `gate_output_during_gap` field added. Prohibited implementations updated.
- §13 CVS Implications: revised. Gap record semantics updated. Sidecar continuity explicitly separated from gate-output doctrine.
- §14 Patent and Standards Implications: Continuity Behaviour → Evaluation-Unavailable DENY in claims and regulatory mapping.
- §15 Terminology Governance: Evaluation-Unavailable DENY added. Continuity Behaviour formally retired as gate-output doctrine with note that the term remains available at sidecar/transport layers.

**Modifications:**
- §4 Constitutional Intent of I6: "fail open" malfunction clause revised — no longer states execution continues; states the commit boundary holds with disclosed reason and retry path.
- §6 Constitutional Decomposition table: Continuity Behaviour row replaced with Evaluation-Unavailable DENY row. Transparent Denial trigger expanded to include evaluation-unavailable DENY.
- §7 Transparent Denial: trigger expanded — fires on both constraint violation DENY and evaluation-unavailable DENY. Three-question test updated for evaluation-unavailable DENY. Required disclosure table updated — infrastructure failure cause and retry path added as required fields.

**Removals:**
- Prior §9 Continuity Behaviour gate-output doctrine: retired. Gate unavailable → execution proceeds → gap recorded is no longer the constitutional doctrine for infrastructure failure.

---

### Changelog — v1.7

**Modifications:**
- §8 Human Default: confirmed that the single constitutional question holds constitutional authority, not the three indicators. The three indicators are correctly framed as diagnostic evidence.
- Changelog v1.6: corrected.

**Removals:** Nothing removed.

---

### Changelog — v1.6

**Modifications:**
- §8 Human Default: added external authority analysis. Constitutional rule: single question. Three diagnostic indicators introduced as evidence. Authority laundering pattern identified. Authority classification table added. Regulatory overlay resolution added. Nine edge cases resolved.

**Removals:** Nothing removed.

---

### Changelog — v1.5

**Modifications:**
- §9 Continuity Behaviour: reframed as derived constitutional obligation. Constitutional necessity proof added. Formal derivation chain added.

**Removals:** Nothing removed.

---

### Changelog — v1.4

**Modifications:**
- §8 Human Default: agency vs operational control distinction added. Six edge cases resolved. Duration and recourse variables added.

**Removals:** Nothing removed.

---

### Changelog — v1.3

**Modifications:**
- §7 Transparent Denial: three-question test added. Required/prohibited disclosure table added. Proof-without-disclosure mechanism added.

**Removals:** Nothing removed.

---

### Changelog — v1.2

**Modifications:**
- §4: "on failure" restored to ordinary meaning. "Reveal governing rules" and "default to human choice" established as permanent obligations.

**Removals:** Nothing removed.

---

### Changelog — v1.1

**Modifications:**
- §4 added. §5 rewritten. §6 hierarchy table added. §7–§9 reordered.

**Removals:** Nothing removed.

---

### Changelog — v1.0

**Additions:**
- Initial document. Three obligations named and defined.

**Removals:** Nothing removed.
