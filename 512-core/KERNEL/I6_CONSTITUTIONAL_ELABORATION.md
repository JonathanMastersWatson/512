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

When the system cannot evaluate — when it genuinely fails — it must default to the least restrictive state. It must not weaponise its own inability to function as a mechanism of restriction. A gate that blocks execution because it crashed has concentrated authority in its own failure. I6 prohibits that. This clause is failure-triggered. It applies to Continuity Behaviour only.

**"reveal governing rules" — a permanent obligation.**

This clause is not conditioned on failure in the same way. Governing rules are not revealed only when the system malfunctions. They are revealed always — on DENY, on ALLOW, on any outcome in which a governing rule was applied. The kernel expresses this in the context of failure because failure is the moment when concealment is most tempting and most harmful. But the obligation is not limited to failure events. It applies to every gate output. This is the basis for Transparent Denial — and Transparent Denial fires on correct DENY outcomes, not on gate malfunction.

**"and default to human choice" — a permanent constitutional floor.**

Human choice is not the default only when the system fails. It is the default always. The system does not accumulate authority over the human party through its operation. Exit, contest, and revocation remain available regardless of what the system determines. The kernel states this in the failure context because failure is when systems are most likely to trap human parties — but the obligation is unconditional. This is Human Default. It fires on every adverse outcome and every operational state.

**The structural reading:**

The kernel sentence opens with "on failure" and lists three obligations. Only the first — fail open — is exclusively failure-triggered. The other two are permanent obligations that the failure scenario makes most urgent to state, but whose scope is not limited to failure events. The BOSUN examples — credit denied, speech moderated, agent blocked — are correctly applications of I6, not because denial is "failure," but because "reveal governing rules" is a permanent obligation that applies to every governed outcome including denial.

---

## 5. Why Elaboration Is Required

The elaboration layer drifted in a specific and predictable way.

The kernel phrase "fail open" exists as an established engineering term. Engineering fail-open means: gate unavailable → allow execution. That meaning is valid in its own context and exists correctly in the 512 ops documents. But the elaboration layer imported that engineering definition as the primary reading of I6, and treated the transparency and sovereignty clauses as adjuncts to an availability behaviour.

This is constitutionally inverted. Availability continuity — the gate behaviour on unavailability — is a downstream consequence of I6's logic, not its primary obligation. A gate that blocks execution on its own failure concentrates authority in itself; I6 prohibits that, which is why availability continuity is required. But availability continuity is not what I6 was written to mandate.

The primary obligation of I6 is transparency on adverse outcomes. The structural floor is human sovereignty. The availability behaviour of the gate is the engineering expression of the constitutional principle in the specific case of gate unavailability.

The elaboration layer must be built on the constitutional reading — not on the engineering convention it inherited by default.

---

## 6. Constitutional Decomposition of I6

I6 contains three obligations. They are triggered by different events and produce different outputs. They are named separately from this document forward.

The constitutional hierarchy is:

| Priority | Obligation | Named Term | Trigger |
|---|---|---|---|
| Primary | Basis for adverse outcome must be visible and inspectable | **Transparent Denial** | Any adverse outcome — denial, restriction, rejection |
| Floor | Human party retains agency; exit and contest remain available | **Human Default** | Any adverse outcome |
| Architectural expression | Gate unavailable → continue → record gap | **Continuity Behaviour** | Gate technical unavailability only |

These three obligations are not alternatives. They are cumulative. Human Default fires on every adverse outcome without exception. Transparent Denial fires when a governing rule produced the outcome. Continuity Behaviour fires when the gate cannot evaluate.

---

## 7. Obligation One — Transparent Denial

**Term:** Transparent Denial

**Constitutional priority:** Primary. This is the obligation I6 was written to mandate.

**Trigger:** Any adverse outcome in which a governing rule was applied. Gate evaluates and produces DENY. System restricts, modulates, rejects, or denies a human party under a declared constraint.

**Behaviour:**

The governing rule is disclosed. The basis for authority is declared. The failed constraint is identified. The decision is inspectable by the affected party and by independent verifiers. The human party can see what rule applied, why it applied, and on what basis.

**What this obligation is not:**

Transparent Denial is not triggered by gate unavailability. If the gate could not evaluate, there is no denial to disclose — there is only a gap. Transparent Denial fires when the gate operated correctly and produced an adverse result.

Transparent Denial is not total disclosure. The kernel says "reveal governing rules" — not "reveal everything." Rules are not mechanisms. The obligation is to reveal what governed the decision, not how the system executes that governance internally.

**The constitutional boundary — what ruled versus how it works:**

The boundary between required and prohibited disclosure is drawn by a single question applied to any candidate disclosure:

*Does this information help the affected human party understand what rule governed their specific situation — or does it help any party circumvent the rule's future application?*

If the former: required. If the latter: prohibited. If both: the minimum disclosure that serves understanding without enabling circumvention is required; the remainder is prohibited.

**The three-question test — what Transparent Denial must answer:**

The affected human party must be able to answer three questions from the disclosure alone:

1. **What rule applied?** The specific invariant or constraint that produced the denial. Not a category. Not a department. The actual rule. "Invariant 2 — explicit consent was not established for this interaction" is disclosure. "Policy violation" is not.

2. **Why did it apply to this specific act?** The factual basis connecting the rule to the proposal. Not the detection mechanism — the factual determination. "The proposed action affected a party for whom no consent record exists at evaluation time" satisfies this. "Our system determined a violation occurred" does not.

3. **How can the human party contest or exit?** The structural path to challenge the determination, withdraw consent, or exit. Not a promise. A structural path. This question is answered jointly by Transparent Denial and Human Default.

A denial that cannot answer all three questions does not satisfy Transparent Denial regardless of how much other information is disclosed.

**Constitutional basis for the disclosure boundary:**

The prohibition on implementation disclosure is not a general security exception. It derives from I1 and I5.

I1 prohibits force and fraud against any human — including third parties. Disclosing detection heuristics or security logic enables circumvention, which enables harm to third parties those mechanisms protect. A transparency obligation to one party does not override a protection obligation to others. Where full disclosure would enable harm to third parties, the disclosure boundary is set by I1.

I5 prohibits hidden rules and unilateral change. Revealing security implementation details forces the system to change its detection mechanisms to maintain effectiveness — producing exactly the unilateral rule mutation I5 prohibits. The disclosure obligation and the stability obligation resolve together: disclose the rule, not the mechanism that enforces it.

**Required and prohibited disclosure table:**

| Information | Status | Constitutional basis |
|---|---|---|
| Which invariant was violated (I1–I7) | **Required** | The rule itself — "reveal governing rules" |
| Factual basis connecting the rule to this specific proposal | **Required** | Human party must understand why their act triggered the rule |
| Constraint reference — policy ID, version, specification hash | **Required** | I5 — rules must be inspectable; rule identity is not a secret |
| What the rule prohibits in general terms | **Required** | The rule is public; only its detection mechanism is protected |
| Contest and exit path | **Required** | Human Default — "default to human choice" |
| How the system detects rule violations | **Prohibited** | Implementation, not rule; enables circumvention — I1 |
| Scoring thresholds or confidence values | **Prohibited** | Implementation; reveals exploit path — I1 |
| Model weights or embeddings | **Prohibited** | Implementation; not a rule |
| Data belonging to third parties | **Prohibited** | I2 and I3 rights of those parties |
| Infrastructure or deployment topology | **Prohibited** | Not a rule; reveals attack surface — I1 |
| Specific signals that triggered detection | **Prohibited** | Detection mechanism, not the rule — I1 |

**Proof without disclosure:**

A class of cases exists where the minimum required disclosure would itself reveal prohibited information. The factual basis for a denial sometimes cannot be stated without revealing detection logic or third-party data.

Example: fraud detection under I1. The rule is clear — no fraud against any human. The factual determination is: this transaction matches a known fraud pattern. Stating which pattern reveals the detection heuristic. Not stating it leaves the human party unable to understand why their specific act was denied.

The constitutional resolution is proof without disclosure. The system provides cryptographic evidence that the governing rule was correctly applied — without revealing the mechanism of application.

Acceptable proof mechanisms:
- Signed execution receipt confirming which invariant was evaluated and the result
- Specification hash confirming which constraint set was in force at evaluation time
- Trusted execution environment attestation confirming evaluation occurred correctly under the canonical specification
- Reproducible policy identifier — the human party can verify the rule exists and applies to their category of action, without the system revealing how it detects violations

This mechanism is structurally present in CVS. The Evidence Object provides cryptographic proof of which invariant was evaluated, under which specification, at what time. It does not reveal detection logic. It satisfies "reveal governing rules" — the rule is identified and its application is proven — without requiring disclosure of implementation.

Proof without disclosure is the constitutional resolution wherever full factual disclosure would violate I1 or expose third-party data. It is not an escape from Transparent Denial. It is Transparent Denial satisfied by a different evidentiary path.

**The BOSUN examples:**

Every stress-test application of K6 in the repository is an application of Transparent Denial: credit denied — rule disclosed; speech moderated — policy identifier disclosed; agent blocked — constraint category disclosed; account frozen — rule invoked disclosed. In none of these cases did the gate fail technically. In all of them, the gate operated correctly and produced an adverse outcome that I6 requires be made visible. In all of them, the rule is disclosable without revealing the detection mechanism.

**Architectural expression:**

```
Gate evaluates → DENY
  → failed invariant identified (I1–I7)
  → governing rule disclosed (rule identity, not detection mechanism)
  → factual basis stated (what the proposal lacked, not how detection worked)
  → contest and exit path disclosed
  → decision recorded in witness layer
  → Evidence Object: violated invariant ID, constraint reference, proposal hash, spec hash
  → where factual basis cannot be stated without revealing prohibited information:
      → proof-without-disclosure mechanism engaged
      → cryptographic attestation replaces factual statement
```

**Relationship to CVS:**

Every Transparent Denial event produces a CVS Evidence Object. The Evidence Object includes the violated invariant identifier, the specification hash confirming which constraint set was in force, and the proposal correlation ID. The denial is independently verifiable by any party with access to the public ledger and the canonical repository — without any implementation detail being exposed in the evidence record.

---

## 8. Obligation Two — Human Default

**Term:** Human Default

**Constitutional priority:** Structural floor. Fires on every adverse outcome without exception.

**Trigger:** Any adverse outcome — denial, restriction, gate unavailability, constraint conflict, system failure. Human Default does not fire only on gate evaluation events. It fires on every condition in which the human party experiences an adverse outcome from the system.

**Behaviour:**

The 512 system does not permanently and opaquely remove a human party's standing to contest, understand, or exit. The system does not use an adverse outcome as a mechanism to further concentrate its own authority over the human party.

**The essential distinction — human agency versus immediate operational control:**

The kernel says "default to human choice." It does not say "default to this specific human's immediate operational control in this specific moment."

These are not the same thing. Human Default guarantees one unconditionally. The other may be legitimately suspended by external authority.

**Human agency** is the permanent constitutional condition Human Default protects. It includes: the right to know what rule applied, the right to contest through appropriate mechanisms, the right to exit the 512 system itself, the right to be treated as an agent rather than a subject. Human agency cannot be suspended by the 512 system on its own authority. It is inalienable within the 512 constitutional framework.

**Immediate operational control** is the ability to act, transact, move, or exit in this specific moment. This can be legitimately suspended by external lawful authority — courts, regulators, emergency safety systems, medical protocols — operating at a layer above the 512 commit boundary. When that suspension occurs, the 512 system records it transparently and executes it. The system is not the source of the deprivation. The external authority is.

**The constitutional test for any edge case:**

*Is the deprivation of operational control generated by the 512 system on its own authority, opaquely, without recourse — or is it generated by an external authority whose basis is disclosed and whose exercise is contestable through an appropriate mechanism?*

If the former: Human Default violation.
If the latter: Human Default satisfied — the external authority, not the system, is the constitutional source of the constraint.

**What qualifies as external authority — the constitutional rule:**

The constitutional rule is a single question:

*Could the system operator produce a different outcome without violating a constraint that exists independently of the operator's own will?*

If yes: system authority. Transparent Denial and Human Default apply in full.

If no: external authority — the 512 system records and executes the constraint transparently; it did not generate it.

This question holds constitutional authority. It is self-contained. It does not depend on the authority's label, its formal status, or how it is presented. An operator cannot launder system authority into external authority by routing a decision through a nominally external source if the operator could, without violating any independently existing constraint, have produced a different outcome.

**The authority laundering pattern:**

*"The system did not make this decision. The policy did."*

The constitutional question defeats this directly: could the operator have written a different policy? Could they have applied the policy differently? Could they have chosen not to apply it? If yes to any of these — system authority. The policy is the operator's own instrument. The decision is the operator's own act.

**Diagnostic indicators:**

The following three indicators assist in answering the constitutional question. They are not an independent parallel test. They are not each individually necessary. They are evidence — when all three are present, the constitutional question is almost certainly answered no; when any is absent, the question requires direct examination.

**Indicator 1 — Origin.** Was the authority constituted by a process outside the operator's control? An authority the operator wrote, commissioned, or determined is strong evidence that the operator could have produced a different outcome.

**Indicator 2 — Modification.** Can the operator unilaterally change the authority? If yes, the operator can produce a different outcome in future cases — strong evidence of system authority. If no, the constraint exists independently of the operator's ongoing will.

**Indicator 3 — Enforcement.** Is the authority enforced by a body that does not derive its mandate from the operator? Operator-controlled enforcement means the operator determines how the authority is applied — strong evidence that a different application was within the operator's power.

When all three indicators point toward independence, the constitutional question is answered no: the operator could not alone have produced a different outcome. When any indicator points toward operator control, the constitutional question must be asked directly — the answer may still be no in specific cases (a collectively bargained agreement the operator co-authored but cannot unilaterally exit), but the indicators no longer provide presumptive evidence.

**Authority classification:**

The following classifications apply the constitutional question directly. The indicators are shown for diagnostic transparency.

| Authority | Indicators | Constitutional question | Classification |
|---|---|---|---|
| Court order | All independent | Operator cannot produce different outcome | External |
| Emergency statute / regulation | All independent | Operator cannot produce different outcome | External |
| Statute directly mandating outcome | All independent | Operator cannot produce different outcome | External |
| Clinical safety protocol (standards body) | All independent | Operator cannot produce different outcome | External |
| Industrial safety standard (independent body) | All independent | Operator cannot produce different outcome | External |
| Government agency guidance (non-binding) | Partial — operator interprets and applies | Operator chooses whether and how to apply it | **System authority** |
| University conduct board | Partial — board may be operator-controlled | Operator controls enforcement | **System authority** |
| Private arbitration | Partial — clause is operator-drafted | Operator drafted clause and selected forum | **System authority** |
| Insurance underwriting criteria | Operator-negotiated | Operator negotiated the criteria | **System authority** |
| Employer policy | None independent | Operator wrote, modifies, and enforces | **System authority** |
| Platform moderation policy | None independent | Operator wrote, modifies, and enforces | **System authority** |
| Corporate policy | None independent | Operator wrote, modifies, and enforces | **System authority** |
| Bank / financial institution policy | None independent | Operator wrote and applies its own policy | **System authority** |
| Bank's interpretation of statute | None independent | Operator determines interpretation | **System authority** |

**The regulatory overlay resolution:**

A regulated operator presents a distinctive case. Banking, healthcare, and financial services operators are subject to statute — genuinely external authority. But operators also write internal policies that implement, interpret, and extend that statute. The statute is external. The operator's application of the statute is system authority.

The constitutional resolution: *the law itself, where it directly and unambiguously mandates the outcome, is external authority. The operator's interpretation and application of law is system authority.*

A bank that freezes an account because a court order requires it: external authority — Transparent Denial records the court order, Human Default is satisfied through the court system.

A bank that freezes an account under its own AML procedures because it determined this account triggered a reporting threshold: system authority — Transparent Denial requires disclosure of the specific basis for the bank's determination, Human Default requires that contest and exit remain available. The AML statute is external. The bank's determination that this account triggered it is the bank's own act.

An operator who says "we're required to do this by regulation" must be able to identify a specific statutory provision that directly mandated this specific outcome — not a general regulatory framework within which the operator made its own interpretive choice. General regulatory context does not convert operator decisions into external authority.

**Government agency guidance:**

Agency guidance is not statute. It is not binding law. The operator chooses whether and how to apply it. That interpretive choice is the operator's — it is system authority. An operator who denies a user under agency guidance must disclose the specific guidance applied and the factual basis for its application. The operator cannot invoke regulatory guidance as a shield from Transparent Denial.

**Edge case resolution:**

*Court order* — the operator could not produce a different outcome without violating the court's mandate. External authority. The 512 system executes and records transparently. Transparent Denial fires: the court order is the governing rule. Human Default is satisfied through the court's own contest mechanism.

*National security restriction* — where the restriction is statutory and enforced by a state body, the operator could not produce a different outcome without violating statute. External authority. Transparent Denial is satisfied by proof without disclosure where the basis cannot be named. Human Default is satisfied through available legal challenge mechanisms.

*Fraud prevention hold* — if the hold is executed under the operator's own AML procedures: the operator determined that this account triggered the threshold. That determination is the operator's own act. System authority — Transparent Denial and Human Default apply. If the hold is executed under a direct court or regulatory freeze order: the operator could not produce a different outcome. External authority. The distinction is whether the operator made the determination or an independent body did.

*Industrial emergency shutdown* — if governed by an independently constituted safety standard the operator cannot unilaterally modify or override: the operator could not produce a different outcome. External authority. If governed by the operator's own safety procedures: system authority — Transparent Denial and Human Default apply, with immediate operational control appropriately suspended where third-party safety is implicated.

*Medical safety lockout* — if the protocol derives from independently constituted clinical standards the operator cannot modify: external authority. If the protocol is the operator's own clinical policy: system authority. Human Default requires that the patient know what rule applied and retain access to a contest mechanism.

*Platform moderation policy* — system authority in all cases. The operator wrote the policy, can modify it, and enforces it. The operator could have produced a different outcome by writing a different policy or applying the existing policy differently. Transparent Denial applies: the specific rule within the policy that produced the denial must be disclosed. Human Default applies: exit must remain structurally available. "Our Community Standards policy" is not external authority — it is the operator's own rule.

*Employer policy* — system authority. The employer wrote, modifies, and enforces its own policy. The employer could produce a different outcome by changing the policy. Full Transparent Denial and Human Default obligations apply.

*Private arbitration* — system authority. The operator drafted the arbitration clause and selected the forum. The arbitration process derives its mandate from the operator's contract. The operator could have drafted a different clause. Routing a denial through an arbitration clause does not convert system authority into external authority.

**Duration and recourse — the two operative variables:**

Human Default prohibits permanent opaque deprivation generated by the system on its own authority. It does not prohibit temporary suspension of operational control under genuine external authority.

Temporary suspension with disclosed basis and available recourse: Human Default can be satisfied.

Permanent deprivation without disclosed basis and without contestable mechanism: Human Default cannot be satisfied regardless of what authority asserts it — including external authority, if that authority cannot itself be contested through any mechanism.

**What this obligation is not:**

Human Default is not a technical mode. It is a constitutional guarantee about what the 512 system must not become — a mechanism of permanent, opaque, uncontestable authority over human parties.

Human Default is not a guarantee of winning a contest. The human party may contest and lose. The court order may be upheld. The fraud hold may be confirmed. Human Default does not determine outcomes — it guarantees standing.

Human Default is not satisfied by providing a complaints form or a stated appeals process. Exit from the system must be structurally possible — not procedurally promised. A system where exit requires permission from the system being exited does not satisfy this obligation.

Human Default is not contingent on Transparent Denial. A system that discloses its governing rules but removes exit paths after denial satisfies Transparent Denial and violates Human Default. Both are required and independent.

Human Default does not govern courts, regulators, law enforcement, or emergency safety systems. It governs the 512 system and any system built on it. External authorities operate at a layer above the commit boundary. The 512 system's obligation is to record their exercise transparently — not to override them and not to replicate their authority on its own.

**Why this is the structural floor:**

I1 through I5 govern the conditions of valid interaction. I6 governs what must be preserved when those conditions are not met. Human Default is the guarantee that no system satisfying 512's properties can become — on its own authority — an instrument of permanent, opaque human subjugation. External legal authority may constrain human parties. The 512 system records that constraint transparently. It does not generate it.

**Architectural expression:**

```
Any adverse outcome (Transparent Denial event OR Continuity Behaviour event)
  → apply constitutional question:
      could the operator produce a different outcome without violating
      a constraint that exists independently of the operator's own will?
  → if yes (system authority):
      → Transparent Denial fires in full
      → governing rule disclosed — the operator's rule, not a nominal external source
      → exit from system structurally available
      → contest path available and disclosed
      → system does not increase its control as consequence of adverse outcome
      → authority laundering prohibited: nominal external source does not insulate
         operator from Transparent Denial or Human Default
  → if no (external authority):
      → external mandate recorded transparently
      → basis disclosed to extent external authority permits
      → where basis cannot be disclosed: proof-without-disclosure engaged
      → human party's legal standing to contest external authority preserved
      → exit from 512 system available after external constraint resolves
  → in all cases:
      → human party treated as agent, not subject
      → deprivation is temporary and bounded, or external authority is independently contestable
      → permanent opaque deprivation by system's own authority: prohibited
```

---

## 9. Obligation Three — Continuity Behaviour

**Term:** Continuity Behaviour

**Constitutional status:** Derived constitutional obligation. Continuity Behaviour is not a co-equal primary obligation alongside Transparent Denial and Human Default. It is what I6's constitutional purpose — no concealed authority, human agency preserved — necessarily requires when applied to the specific case of gate technical failure. Its authority is constitutionally binding. Its source is the primary principles, not independent constitutional standing.

**Trigger:** Gate unavailable. Evaluation timeout. Gate crash. Network partition. Any condition under which the gate cannot complete evaluation.

**Behaviour:**

The gate produces no output. Evaluation did not complete. The continuity handler engages. The commit path remains available. Execution proceeds. The witness layer records the ungoverned period as an evidence chain gap.

**The constitutional necessity proof:**

Remove Continuity Behaviour. Transparent Denial and Human Default still exist. The gate fails. Two failure modes are now possible:

*Gate blocks on failure.* The system halts because the gate is down. No execution proceeds. No authority is visibly exercised — and that is precisely the problem. The gate's failure state has become a concealed governing rule: *"when the gate is unavailable, nothing executes."* That rule was never declared. It was never committed to the specification. It was never consented to by the human party. The gate operator now controls all execution through the simple act of taking the gate down. Transparent Denial does not cover this — there is no DENY to disclose. Human Default does not fully resolve it — the human party cannot distinguish between a DENY and a gate failure; both produce the same visible outcome. The constitutional purpose of I6 — no concealed authority — is violated by a mechanism the primary obligations do not reach.

*Gate allows silently on failure.* Execution proceeds without evaluation. No record exists that evaluation did not occur. Every execution during the failure period appears governed when it was not. The human party, an auditor, a regulator, a court — none can distinguish evaluated execution from ungoverned execution. This is authoritative concealment in its most complete form: the absence of governance is itself concealed. I5 is violated — a hidden rule operates: *"when the gate is down, constraints do not apply."* I6 is violated — the governing condition at execution time is concealed. Human Default cannot be satisfied because the condition that would trigger it is invisible.

Continuity Behaviour is the only resolution that avoids both failure modes simultaneously. Execution continues — the gate's failure state does not become a concealed governing rule. The gap is recorded — the absence of evaluation is disclosed, not concealed. The human party can see that their execution proceeded ungoverned — the condition is visible and contestable.

Without Continuity Behaviour, I6 cannot satisfy its constitutional purpose under gate failure. The primary obligations are necessary but not sufficient. Continuity Behaviour is what they entail in this scenario. That entailment is constitutionally binding.

**The derivation:**

```
Primary principle: no system may exercise authority while concealing the basis for that authority.
Scenario: gate cannot evaluate.
  → gate blocks on failure
      → gate's availability state becomes concealed governing rule
      → authoritative concealment — I6 violated
  → gate allows silently on failure
      → absence of governance concealed as governed execution
      → authoritative concealment — I5 and I6 violated
  → therefore: execution must continue AND the gap must be recorded
      → continuation: prevents gate availability from becoming concealed authority
      → gap record: prevents silent execution from concealing absence of governance
      → both are required — neither alone satisfies the primary principle
      → Continuity Behaviour = continuation + gap record = derived constitutional obligation
```

**The relationship to engineering implementation:**

Continuity Behaviour is not an engineering implementation choice. An engineering implementation choice is one where the constitutional principle is satisfied by multiple available designs and the implementer selects among them. Continuity Behaviour admits no such choice: within the constitutional framework of I6, gate-blocks-on-failure and gate-allows-silently-on-failure are both constitutional violations. Continuation with gap recording is the only constitutionally permissible behaviour. That is a constitutional obligation, not a design preference.

What is an engineering implementation choice is *how* continuation and gap recording are achieved — the specific handler architecture, the gap record schema, the anchoring interval. Those are implementation decisions. The requirement that they exist is not.

**What this obligation is not:**

Continuity Behaviour is not a primary obligation of I6. It does not stand independently of Transparent Denial and Human Default. If the primary principles did not exist, Continuity Behaviour would have no constitutional grounding. Its authority is derived, not original.

Continuity Behaviour is not an ALLOW output. The gate produced no output. The continuity handler opened the commit path. Constraint satisfaction was not established. Execution proceeded because the alternative — blocking — is itself a constitutional violation. Not because the constraints passed.

Continuity Behaviour is not silent continuation. A system that continues execution without generating a gap record is not exhibiting Continuity Behaviour — it is exhibiting the second failure mode: silent execution that conceals the absence of governance. Silent continuation violates I5 and I6. It is what Continuity Behaviour exists to prevent, not what it permits.

**Architectural expression:**

```
Gate unavailable or evaluation timeout
  → gate produces no output
  → continuity handler opens commit path        [prevents concealed blocking authority]
  → witness layer records gap                   [prevents concealed ungoverned execution]
  → gap record anchored to public ledger        [makes absence of governance independently verifiable]
  → gap record is not ALLOW                     [records absence of evaluation, not positive evaluation]
  → gap record is not DENY                      [no constraint was violated; evaluation did not occur]
```

---

## 10. Relationship Between the Three Obligations

The three obligations are not alternatives. They are cumulative.

**On a Continuity Behaviour event** (gate unavailable):
- Continuity Behaviour fires — execution continues, gap recorded
- Human Default fires — exit remains available
- Transparent Denial does not fire — there is no denial to disclose

**On a Transparent Denial event** (gate evaluates → DENY):
- Transparent Denial fires — governing rule disclosed, reason exposed
- Human Default fires — exit remains available
- Continuity Behaviour does not fire — the gate did not fail

**Human Default fires on every adverse outcome without exception.**

No adverse outcome satisfies I6 unless Human Default is also satisfied. Human Default is the constitutional floor. Transparent Denial and Continuity Behaviour are the event-specific obligations that sit above it.

```
Gate unavailable
  → Continuity Behaviour (execution continues, gap recorded)
  → Human Default (exit remains available)
  → Transparent Denial: does NOT fire

Gate evaluates → DENY
  → Transparent Denial (governing rule disclosed, reason exposed)
  → Human Default (exit remains available)
  → Continuity Behaviour: does NOT fire
```

---

## 11. Architectural Consequences

**Gate design:**

The gate must identify the failed invariant on every DENY. A gate that returns DENY without invariant identification violates Transparent Denial regardless of whether Continuity Behaviour and Human Default are correctly implemented.

**Continuity handler design:**

The continuity handler must generate a gap record on every gate unavailability event. A handler that opens the commit path without generating a gap record violates the recording requirement that makes Continuity Behaviour distinguishable from silent bypass.

**Witness layer design:**

CVS must produce Evidence Objects for all three event types:
- ALLOW — per-invariant results, spec hash, proposal hash, timestamp
- DENY — violated invariant ID, constraint reference, spec hash, proposal hash, timestamp
- Gap record — gap duration, gap reason, executing identity, spec hash, timestamp

The DENY Evidence Object must include the violated invariant ID. A DENY Evidence Object without this field does not satisfy Transparent Denial.

**System design:**

Exit paths, consent revocation mechanisms, and contest paths are not gate responsibilities. They are system responsibilities. The gate enforces constraints at the commit boundary. Human Default requires that the system surrounding the gate preserve human agency regardless of gate output.

---

## 12. Implementation Consequences

**Prohibited implementations:**

A system that:
- blocks execution on gate technical failure (violates Continuity Behaviour)
- produces DENY without disclosing the failed invariant (violates Transparent Denial)
- produces DENY and removes exit options (violates Human Default)
- generates no gap record on gate unavailability (violates Continuity Behaviour recording requirement)
- treats a continuity event as equivalent to ALLOW (violates the semantic distinction between evaluation and continuation)
- conceals the governing rule on any adverse outcome (violates the constitutional intent of I6)

does not satisfy Invariant 6.

**Required Evidence Object fields on DENY:**

```json
{
  "event_type": "deny",
  "violated_invariant": "I[1-7]",
  "constraint_reference": "<governing constraint identifier>",
  "proposal_id": "<correlation ID>",
  "spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5",
  "timestamp": "<ISO 8601>"
}
```

**Required gap record fields on Continuity Behaviour:**

```json
{
  "event_type": "validation_gap",
  "gap_start": "<ISO 8601>",
  "gap_reason": "<unavailability cause>",
  "executing_identity": "<agent or system ID>",
  "spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5",
  "timestamp": "<ISO 8601>"
}
```

**JSON field naming:**

The Evidence Object field previously named `invariant_6_fail_open` is a misnomer. It records the per-invariant evaluation result for I6 — a binary pass/fail outcome of successful gate evaluation. It is not a gap indicator. It does not fire on gate unavailability. Rename this field to `invariant_6_result` in all schema definitions and implementations.

---

## 13. CVS Implications

CVS is the reference witness layer for 512. Its Evidence Object schema must reflect the three-obligation decomposition of I6.

**Continuity Behaviour events:** CVS records a `validation_gap` record. This is not an ALLOW. It is not a DENY. It is a distinct event type indicating that evaluation did not occur and execution proceeded.

**Transparent Denial events:** CVS records a DENY Evidence Object including the violated invariant ID and constraint reference. The violated invariant field is mandatory on every DENY. A DENY Evidence Object without a violated invariant ID does not satisfy Transparent Denial.

**Human Default:** CVS does not enforce Human Default directly — that is a system obligation. CVS provides the evidentiary record that makes Human Default verifiable: the Evidence Object proves what outcome was produced, which invariant was violated, and when. Independent verifiers can determine from the evidence chain whether the system preserved exit options following an adverse outcome.

---

## 14. Patent and Standards Implications

The three-obligation decomposition of I6 is the authoritative structure for any IP filing that references I6 or fail-open behaviour.

**Claims must specify which obligation is claimed:**

- Claims about gate unavailability handling reference Continuity Behaviour.
- Claims about denial disclosure reference Transparent Denial.
- Claims about human control preservation reference Human Default.

A claim that references "fail-open behaviour" without specifying which obligation is a claim against an ambiguous term. Post this document, that ambiguity is a known defect — not a prior art shield.

**For standards submissions:**

The three terms — Transparent Denial, Human Default, Continuity Behaviour — are the vocabulary for any standards body engagement. Submissions that use "fail-open" as a composite term invite conflation with the engineering convention. Precise terms eliminate that conflation.

**For regulatory citations:**

DORA, NIST AI RMF, EU AI Act, and similar frameworks reference operational continuity, explainability, and human oversight as distinct obligations. The three I6 terms map to those categories:

- Continuity Behaviour → operational continuity (DORA alignment)
- Transparent Denial → explainability / logging (EU AI Act Article 12 alignment)
- Human Default → human oversight (NIST AI RMF Govern function alignment)

Single-term "fail-open" references in regulatory submissions obscure these mappings. Precise terms make them explicit.

---

## 15. Terminology Governance

**Transparent Denial** — the primary obligation of I6. Applies to all DENY events and all adverse outcomes produced by governing rule application. Every DENY must produce a Transparent Denial. There are no silent denials in a 512-conforming system.

**Human Default** — the structural floor of I6. Applies to all adverse outcomes without exception. Not contingent on Transparent Denial. Not contingent on Continuity Behaviour. Fires always.

**Continuity Behaviour** — the architectural expression of I6's principle in the specific case of gate technical unavailability. Previously labelled "fail-open" in ops and implementation documents. That label is retained in existing ops documents where its scope is already correctly bounded to gate unavailability. New documents use Continuity Behaviour.

**"Fail open" as a phrase:**

The phrase "fail open" is not prohibited. It remains valid as a shorthand in contexts where its scope is unambiguously bounded to gate unavailability (Continuity Behaviour). It is prohibited as a label for Transparent Denial or Human Default. Any document using "fail-open" to describe denial disclosure or human control obligations is using the term incorrectly from this document's effective date.

**Prohibited usages:**

- "fail-open" used to mean disclosure on DENY → Transparent Denial
- "fail-open" used to mean return of human control → Human Default
- "fail-open event" used to describe a DENY outcome → incorrect; DENY is a gate output, not a continuity event
- treating gap records as equivalent to ALLOW → prohibited

---

## 16. Authority Over Future Documents

This document governs all future elaborations of Invariant 6 across:

- the 512 repository
- the Evidence Sidecar (CVS) repository
- the 512-canon repository
- the Constraint Architecture repository
- all derivative documents, technical papers, whitepapers, and implementation guides

Any future document that introduces a usage of these terms inconsistent with the definitions in this document is in constitutional error.

Any future document that reintroduces the conflation of these three obligations under a single label is in constitutional error.

The kernel remains the highest authority. This document is the second authority for all matters concerning the elaboration of Invariant 6.

---

## Document Control

| Field | Value |
|---|---|
| Document | `I6_CONSTITUTIONAL_ELABORATION.md` |
| Version | 1.7 |
| Date | June 2026 |
| Author | Jonathan M. Watson |
| Status | Constitutional Authority |
| Canonical Repository | github.com/JonathanMastersWatson/512 |
| Kernel Commitment | SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |

### Changelog — v1.7

**Modifications:**
- §8 Human Default: confirmed that the single constitutional question — *could the system operator produce a different outcome without violating a constraint that exists independently of the operator's own will?* — holds constitutional authority, not the three indicators. The three indicators (Origin, Modification, Enforcement independence) are correctly framed as diagnostic evidence that assists in answering the single question, not as an independent parallel test with constitutional standing. This distinction matters: a case can satisfy the single question while failing an indicator (collectively bargained agreement the operator co-authored but cannot exit); and a case can satisfy all three indicators but still require direct examination. The single question is self-contained and handles novel authority types the indicators were not designed to anticipate.
- Changelog v1.6: corrected — prior description incorrectly stated the three conditions were "the constitutional test" and that "all three conditions are required." That framing has been superseded. The constitutional rule is the single question; the three indicators are evidence.

**Removals:** Nothing removed.

---

### Changelog — v1.6

**Modifications:**
- §8 Human Default: added external authority analysis. Constitutional rule: single question — could the operator produce a different outcome without violating an independently existing constraint? Three diagnostic indicators introduced (Origin, Modification, Enforcement independence) as evidence assisting the single question — not as an independent parallel test. Authority laundering pattern identified and defeated by the single question. Authority classification table added. Regulatory overlay resolution added: statute is external authority; operator interpretation of statute is system authority. Government agency guidance classified as system authority. Nine edge cases resolved. Architectural expression updated to incorporate the constitutional question and laundering test as structural steps.

**Removals:** Nothing removed.

---

### Changelog — v1.5

**Modifications:**
- §9 Continuity Behaviour: fully revised. Reframed constitutional status from "architectural expression" to "derived constitutional obligation" — binding but derived from the primary principles rather than holding independent constitutional standing. Added the constitutional necessity proof in full: removes Continuity Behaviour, applies the two failure modes (gate-blocks-on-failure, gate-allows-silently-on-failure), demonstrates that both are constitutional violations that Transparent Denial and Human Default do not individually reach, and derives Continuity Behaviour as the only constitutionally permissible resolution. Added formal derivation chain. Added the engineering-implementation-choice distinction: what Continuity Behaviour requires (continuation + gap recording) is constitutionally obligated; how it is achieved is an engineering decision. Revised architectural expression to annotate each step with its constitutional function.

**Removals:** Nothing removed.

---

### Changelog — v1.4

**Modifications:**
- §8 Human Default: substantially expanded. Added the human agency versus immediate operational control distinction — the kernel guarantees the former unconditionally; the latter may be legitimately suspended by external lawful authority. Added the constitutional test for edge cases: deprivation generated by the system on its own authority is prohibited; deprivation generated by external authority and recorded transparently is not. Added edge case resolution for six scenarios: criminal investigation / court order, national security restriction, fraud prevention hold, industrial emergency shutdown, medical safety lockout — each resolved against the constitutional test without relaxing the doctrine. Added duration and recourse as the two operative variables distinguishing permissible temporary suspension from prohibited permanent deprivation. Expanded architectural expression to distinguish system-authority outcomes from external-authority outcomes. Clarified that Human Default governs the 512 system, not courts, regulators, or emergency safety systems — those operate at a layer above the commit boundary.

**Removals:** Nothing removed.

---

### Changelog — v1.3

**Modifications:**
- §7 Transparent Denial: substantially expanded. Added the constitutional boundary definition — "what ruled versus how it works." Added the three-question test: what rule applied, why did it apply to this specific act, how can the human party contest or exit. Added the required/prohibited disclosure table with constitutional basis for each row. Added constitutional basis for the disclosure prohibition — derived from I1 (circumvention enables harm to third parties) and I5 (revealing detection mechanisms forces unilateral rule mutation). Added proof-without-disclosure mechanism as the constitutional resolution for cases where minimum required disclosure would reveal prohibited information — defines acceptable proof mechanisms and establishes that this is Transparent Denial satisfied by a different evidentiary path, not an escape from it. Expanded architectural expression to include proof-without-disclosure path.

**Removals:** Nothing removed.

---

### Changelog — v1.2

**Modifications:**
- §4 Constitutional Intent of I6: surgical revision. Removed the claim that "on failure" means any adverse outcome — that reading is indefensible against ordinary meaning in legal, regulatory, and standards contexts. Restored "failure" to its ordinary meaning: malfunction, inability to evaluate. Established that "fail open" is the malfunction clause only. Established that "reveal governing rules" and "default to human choice" are permanent obligations — not failure-triggered — whose scope extends to all governed outcomes including correct DENY results. This is the basis on which the BOSUN examples are correctly applications of I6 without requiring redefinition of "failure."

**Removals:** Nothing removed.

---

### Changelog — v1.1

**Modifications:**
- §4 Constitutional Intent of I6: added as new primary section. Establishes that I6's purpose is prevention of authoritative concealment, not engineering availability. Defines "on failure" as any adverse outcome against a human party, not technical gate failure. Corrects the constitutional reading of "fail open" from availability instruction to directional instruction.
- §5 Why Elaboration Is Required: rewritten to identify the specific inversion in the elaboration layer — engineering "fail-open" imported as primary reading, transparency and sovereignty clauses treated as adjuncts.
- §6 Constitutional Decomposition: hierarchy table added. Transparent Denial elevated to primary. Human Default identified as structural floor. Continuity Behaviour repositioned as architectural expression, not primary obligation.
- §7–§9: obligations reordered to reflect constitutional hierarchy (Transparent Denial first, Human Default second, Continuity Behaviour third).
- §15 Terminology Governance: "fail open" retained as valid shorthand for Continuity Behaviour where scope is unambiguously bounded; prohibited only as label for the other two obligations.

### Changelog — v1.0

**Additions:**
- Initial document. Three obligations named and defined.
- Architectural, implementation, CVS, patent, standards, and regulatory consequences documented.
- Terminology governance and authority over future documents established.

**Removals:** Nothing removed.
