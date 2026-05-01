# Unauthorized by Design
## Why Federal AI Authorization Fails at the Point of Execution

**Jonathan M. Watson | 512 / CVS Architecture**
**Mark Gomez | AGICOMPLY · Founder & CEO · Federal AI Compliance & Authorization**
**Version 4.0 | May 2026**
**Classification:** Public — Institutional Readership
**Audience:** Federal Agency CIOs · Procurement Officers · GovCon Primes · Risk and Authorization Leads

---

*512 / CVS Architecture · White Paper · May 2026*

---

*For federal agency CIOs, procurement officers, GovCon primes, and risk and authorization leads evaluating AI system posture under current and emerging federal AI policy.*

---

## The Authorization Problem Exists Now, Before Autonomy Arrives

Federal AI governance conversations are dominated by a future framing: autonomous agents operating at machine speed, systems executing thousands of consequential actions per second, decision velocity that outpaces any human review cycle. The implication is that authorization is a preparation problem — something to be designed before the technology matures to that point.

That framing obscures a failure that is already operating, in production, at human speed.

AI-assisted federal procurement, adjudication, and benefits systems run deliberately. Analysts review outputs. Supervisors authorize overrides. Program offices produce audit trails. The process is staffed, governed, and subject to a framework of authorization controls refined over decades. And yet, the evidentiary record produced by those processes is structurally insufficient to satisfy the requirements those frameworks mandate — not because the systems are too fast for oversight, but because authorization practice certifies systems before deployment and has no mechanism to verify execution after it.

The gap between what is declared in an Authorization to Operate and what occurs at the execution boundary is not a compliance gap. It is an architectural one. When autonomous systems arrive and decision velocity increases by four orders of magnitude, this gap does not become a new problem. It becomes an irrecoverable one.

The time to address the evidence architecture is now, while federal systems still operate at a speed that allows the gap to be examined.

```
Current authorization model — certification precedes execution, evidence does not follow it

System Design -> Control Mapping -> Assessment -> ATO Granted -> Deployment -> Execution -> Post-hoc Audit
                                                                                              ^
                                                                                   Evidence reconstructed here
```

---

## Authorization Certifies Configuration. It Does Not Witness Execution.

The Authorization to Operate is the federal government's primary mechanism for confirming that an AI system meets the security and control requirements necessary for operation. A System Security Plan documents the control environment. A Security Assessment Report tests it against defined requirements. An Authorizing Official signs the ATO on the basis of that record. The record is accurate at the moment of assessment.

Execution begins after the ATO is granted. The system that operates in production is not frozen at the configuration the assessment captured. Models drift. Data distributions shift. Control implementations that passed assessment degrade in operation. None of these changes require a new ATO unless they breach defined significant-change thresholds — thresholds that are themselves defined by the system operator and documented in the same plan the ATO certified.

The ATO record contains what the system declared it would do. The execution record, where it exists, contains what the system produced. The gap between declaration and execution — where drift occurs, where judgment is exercised, where admissibility assumptions break down — is not recorded anywhere. The ATO audits the plan. Nothing audits the gap between the plan and its execution.

---

## Meaningful Human Oversight Is Documented in Controls. It Is Absent from the Execution Record.

Federal AI policy has converged on a requirement for meaningful human oversight of high-impact automated decisions. OMB Memorandum M-25-21 mandates that agencies maintain human oversight mechanisms capable of detecting and correcting AI errors before they cause harm. The language is precise on intent: oversight must be meaningful — not procedural, not a rubber-stamp, not a change-log entry that records an approval without documenting what was reviewed.

In production federal AI environments, human oversight takes a recognizable form. An analyst is assigned to review AI-flagged cases. The analyst reviews, reaches a judgment, and approves or rejects. The approval event is recorded. The system log shows: AI flagged, analyst approved, timestamp recorded. The control is satisfied.

What is absent from the record is the substance of the oversight: what information the analyst examined, what gave them confidence that the AI output was accurate, what reasoning they applied to convert machine uncertainty into a human decision. The oversight requirement is documented in the control framework. Its exercise at any specific decision point is structurally absent from the evidentiary record. If that decision is later contested — in litigation, OIG review, or congressional inquiry — the agency demonstrates that oversight was procedurally present. It cannot demonstrate that it was substantively exercised.

---

## Continuous Monitoring Records Telemetry. It Does Not Record Decisions.

Continuous monitoring under FedRAMP and FISMA captures the operational condition of a system over time: patch levels, configuration state, vulnerability findings, access log anomalies. This is necessary infrastructure. It is not evidentiary infrastructure for AI decision governance.

When an AI system produces a consequential output — a procurement recommendation, a benefits determination, a threat classification — the continuous monitoring record confirms the system was running, that it was in its authorized configuration, and that no flagged vulnerabilities were active at the time. It does not confirm that the specific decision was made within the declared scope of the system's authorized behavior, by an actor whose delegated authority covered that specific action category, against an AI model whose calibration had been validated within the required timeframe.

Those are not telemetry questions. They are decision-level evidence questions. They require a record created at the moment the decision was made — not a system health record that can be correlated to the approximate time the decision occurred. Correlation is not evidence. It is inference, and inference under adversarial scrutiny does not hold.

---

## Degraded Operation Is Classified in the CONOPS. It Is Invisible in the Evidence Chain.

Federal systems operate under Continuity of Operations Plans that define authorized fallback procedures when primary AI systems are unavailable. Manual processing, legacy system routing, and human-driven exception handling are documented, tested, and authorized. The plan is sound. The execution of the plan — which decisions were affected, over what period, against what standard — leaves no trace in the evidence record beyond the classification of a processing pathway.

The gap is precise: knowing that a decision was made in manual fallback mode is not the same as knowing whether the manual process was accurate, authorized, and within the declared scope of the fallback procedure. A regulatory examiner or OIG reviewing a contested decision determines that the system was in degraded operation. It cannot determine whether the decision made during that degraded operation met any specific standard of correctness, authority, or process compliance. The pathway is declared. The execution inside it is invisible.

---

## Control Mappings Are Assertions. No Mechanism Verifies Them at Runtime.

The Security Assessment Report is the authorization record's most detailed technical artifact. It documents, control by control, how the system satisfies each applicable requirement. The mapping is reviewed by an independent assessor, validated by the Authorizing Official, and remains in force until the next assessment cycle or a significant-change trigger. It is a snapshot of a declared control environment.

Execution is continuous. Control implementations that satisfied assessment degrade in operation without triggering a significant-change threshold. A logging control that passed assessment becomes inconsistently applied as system updates accumulate. An access control mapped to AC-3 is technically present but operationally bypassed through a fallback code path no assessment examined. A model governance control mapped to AI-specific overlays was valid at assessment time and invalid six months later when the underlying model was retrained without a corresponding authorization event.

The mapping says the control is present. Nothing confirms whether it was present — and functioning — at the moment a specific decision executed. That is not the assessor's failure. It is an architectural limit of assessment-based authorization: it verifies a declared state, but it cannot verify a running one.

---

## Fraud Does Not Occur After Execution. It Commits at the Boundary.

Current federal AI systems detect fraud after execution. Evidence is reconstructed after the fact, authority violations are identified through audit sampling, and anomalies surface in review cycles that run weeks or months behind the decisions they examine. By the time fraud is detected, it has committed. The state has changed. The record — where one exists — shows an output, not the decision that produced it.

---

## Regulatory Frameworks Require What Current Authorization Practice Cannot Produce

Every major federal AI governance framework now mandates proof of execution — not documentation of intent. Current authorization practice produces the latter.

The NIST AI Risk Management Framework (AI RMF 1.0) treats the inability to reconstruct decisions under audit conditions as a governance posture failure regardless of measured system accuracy. Traceability is a foundational property without which AI risk cannot be managed. OMB Memorandum M-25-21 mandates that agencies deploying high-impact AI maintain mechanisms capable of demonstrating that human oversight was not only procedurally present but substantively exercised — a standard that requires a reasoning record created at the moment of decision, not reconstructed from outcome logs afterward. Executive Order 14110 and its successors require auditable records of AI system behavior in security and safety-critical applications, with traceability sufficient to support independent review.

FedRAMP's continuous authorization model moves toward ongoing verification rather than point-in-time assessment — but its monitoring infrastructure captures system health telemetry, not decision-level evidence. The framework recognizes the need for continuous verification. The evidence layer required to satisfy it does not exist in standard federal AI deployments.

Each framework assumes the decision record was created at execution time. Each of the five structural gaps documented above demonstrates that it was not — not through negligence, but because the architecture places the recording boundary after the decision boundary. Closer monitoring, more frequent assessments, and richer system logs do not close this gap. They produce more detailed records of the same structural absence.

The procurement consequence is direct and growing. AI systems that cannot produce independent execution-bound evidence face increasing resistance in federal authorization processes as agencies implement AI RMF-aligned controls. Systems that produce that evidence — with proof independent of the vendor, verifiable without operator cooperation — change the authorization conversation from risk management to risk elimination.

---

## Compliance Platforms Cannot Independently Verify Themselves

The federal AI compliance market is expanding rapidly. Platforms offer control mapping, audit trail generation, model monitoring, and risk dashboard capabilities. Each addresses a real need. None resolves the foundational problem, and one creates a new one.

The problem is evidentiary independence. A compliance platform monitors the AI system it is deployed alongside. Its logs, dashboards, and audit exports are produced by the same operational environment they are documenting. Under federal regulatory examination, an Inspector General review, or GAO audit, that evidence carries the weakest possible evidentiary standing: it is assertion by the interested party. The agency cannot ask the compliance vendor's platform to verify the compliance vendor's platform. The regulator cannot accept as independent evidence a record whose independence cannot be demonstrated.

This is not a criticism of compliance platforms. It is a structural property of any evidentiary system that is part of the environment it observes. Providing independent evidence of system behavior requires a component that is architecturally separate from every system it observes — not integrated, not co-deployed in the same stack, not relying on the same infrastructure. Purpose-built AI observability platforms accurately identify execution anomalies and model drift — after those anomalies have already produced decisions, already created regulatory exposure, already entered the case record. They explain what happened. They do not prevent it, and they do not produce evidence of it that is independent of their own operation.

---

## 512 and CVS Are Not AI. That Is Precisely the Point.

Every AI compliance platform in the federal market has a confidence problem. 512 and CVS do not.

AI systems are probabilistic. They optimize for statistical outcomes, express confidence without guaranteed accuracy, and drift as their operating environments diverge from their training data. Governing AI with AI compounds the problem — the governance layer inherits the same failure modes it is supposed to detect.

512 and CVS are not AI. They are deterministic constraint infrastructure — the layer that operates below AI systems and beside governance platforms, enforcing what those platforms declare and producing proof that is independent of everyone in the room.

A **Commit Gate** is positioned at the execution boundary — the precise point at which a proposed action becomes an irreversible state change. It carries an immutable constraint set. It evaluates each proposed action against that set simultaneously across every applicable invariant and produces one of two outputs: allow or deny. It does not learn, drift, weight, or interpret. It enforces declared policy before execution proceeds, at speeds between 10 and 50 microseconds — 6,000 to 80,000 times faster than human cognition, without relying on human cognition to function.

**CVS** — the Cryptographic Verification Sidecar — is the independent witness layer. It operates in parallel with any execution surface without touching the execution path. Every observed event produces an Evidence Object: a structured, cryptographically signed record, hash-chained to its predecessor, anchored to a public ledger every 30 to 60 seconds at approximately $1.08 per month. Retroactive alteration of any Evidence Object breaks every subsequent link in the chain — detectable through independent verification without operator cooperation. The system that produced the decision cannot alter the record of it.

The architecture is agnostic to upstream governance platforms and downstream compliance systems. It enforces declared constraints and produces independent evidence regardless of which AI system, which model, or which authorization framework is in use. Whatever federal compliance platform an agency selects, it still requires independent proof that the platform operated as declared. No vendor provides that proof about their own system. 512 and CVS provide it about any system.

---

## Execution at the Commit Boundary

Every execution system has a commit boundary: the precise point at which a proposed action becomes an irreversible state change. Before that boundary, actions are proposals — they can be evaluated, modified, or denied. After it, they are facts. In a federal procurement environment, that moment is the approval of a contract action, the execution of a delegated purchasing authority, or the routing of an adjudication to automatic settlement. Once committed, the state has changed.

```
The commit boundary

Proposed Action  ->  [COMMIT GATE]  ->  Commit
                           |
                          CVS

Before [COMMIT GATE]: proposal. After Commit: irreversible fact.
CVS records what was proposed, what was evaluated, and what was decided.
```

When a proposed action reaches the boundary, the gate evaluates the constraint set simultaneously across every applicable invariant: Is this action within the declared admissible set? Does the executing party hold attested authority for this specific action category? Are all required inputs present — authority attestation, model calibration certification, structured reasoning record? Is the system in a valid operational state? Each invariant returns a binary result. No reasoning, no interpretation, no weighting. If all invariants return true, execution proceeds. If any return false, execution is denied. The evaluation completes in 10 to 50 microseconds.

CVS operates in parallel throughout this sequence, never on the execution path. The Evidence Object records the proposed action, the constraint evaluation results for each invariant, the binary outcome, and the timestamp — all cryptographically signed and chained before the next event arrives. Evidence Objects accumulate in Merkle batches anchored to the public ledger every 30 to 60 seconds. The record of what the gate evaluated and what it decided exists permanently, independently, before any downstream system has processed the result.

| Stage | Current Federal System | With 512 / CVS |
|---|---|---|
| Decision basis | AI output, analyst judgment — implicit | Proposed action evaluated against declared, committed constraints |
| Evaluation method | Interpretive; reconstructed post-hoc if contested | Deterministic, simultaneous, binary — at execution time |
| Record produced | Outcome only; control mappings asserted separately | Full boundary record: inputs, constraint results, authority attestation, outcome |
| Evidence independence | Vendor-internal; operator cooperation required to read | Public ledger anchored; verifiable without operator cooperation |
| ATO relationship | ATO certifies declared configuration | ATO commitment verified against every execution event |

---

## From Observation to Authorization: Three Operational States

### State 1 — Observation Mode: CVS in a Human-Speed Federal System

```
Observation Mode — CVS beside the workflow, not in it

Request -> AI Analysis -> Analyst Review -> Authorization -> Execution -> Record
   |            |               |               |              |            |
  CVS          CVS             CVS             CVS            CVS         CVS

CVS observes state transitions at each stage. Execution is unchanged.
CVS does not intercept, block, or influence any step.
```

What CVS records at each stage is precise: input events, override actions, authority delegations exercised, system state classifications, approvals, and degraded mode transitions. Each observation produces an Evidence Object — a structured, cryptographically signed record of what occurred, when it occurred, and in what system state. Gaps in the evidence chain are themselves recorded. Nothing is inferred. The absence of a record is the record.

### State 2 — Pre-Enforcement Evaluation Mode: 512 Without Blocking

Operational risk is the primary barrier to enforcement adoption in federal systems. No agency accepts a gate that could block critical execution before the constraint definitions have been validated against real transaction volumes and real authority patterns. Pre-enforcement evaluation mode removes this barrier entirely.

In this state, the 512 boundary is present at the execution boundary. It evaluates every proposed action against the declared constraint set — authority scope, model calibration state, required input presence, operational status. It records the result of each evaluation: which actions would have been allowed, which would have been denied, which invariant would have triggered the denial. Execution is not blocked. The results are recorded as if enforcement were active.

```
Pre-Enforcement Evaluation Mode

Proposed Action  ->  [512 BOUNDARY — EVALUATING, NOT BLOCKING]  ->  Execution proceeds
                                    |
                              Result: ALLOW / DENY
                                    |
                          CVS records evaluation result
                          CVS records ungoverned periods as evidence chain gaps

Execution continues regardless of evaluation result.
Record shows exactly what enforcement would have produced.
```

The output of this phase is a readiness signal: the precise distribution of allow, deny, and gap results across the agency's actual transaction volume. Before a single action is blocked, the agency has a complete, evidence-backed picture of which constraint definitions are calibrated correctly, which upstream systems need to produce attestations they are not currently producing, and what the enforcement failure rate would be on day one.

### State 3 — Enforcement Mode: 512 + CVS at Full Deployment

Humans define the constraints upstream — what constitutes a valid delegated authority attestation, what a structured analyst reasoning record requires, what model calibration recency standards apply. At the moment of execution, constraint evaluation is deterministic. Human cognition is not in the loop at the boundary.

```
Enforcement Mode — human upstream, gate at the boundary, CVS beside it

Policy / Authority Registry / Model Validation / Control Definitions
                              |
                    [Declared Constraints]
                              |
Proposed Action  ->  [COMMIT GATE]  ->  Commit  ->  Execution
                           |
                          CVS

Humans operate upstream. No human decision occurs at the boundary.
Gate evaluates constraints. CVS records at evaluation. Binary outcome only.
```

| Capability | CVS Only | 512 + CVS |
|---|---|---|
| Visibility into execution | Yes | Yes |
| Independent evidence | Yes | Yes |
| Prevent unauthorized actions | No | Yes |
| Hidden decisions | Visible | Eliminated |
| Execution speed support | Human-speed | Machine-speed |
| ATO-defensible evidence | Partial | Structural |

---

## What the Federal Authorization Workflow Looks Like Under This Architecture

Each failure mode maps to a gate condition and to an upstream system of responsibility. The boundary does not resolve authorization gaps in real time. It exposes them precisely, at the moment they would otherwise have been absorbed through human intervention.

| Failure Mode | Gap in Current Architecture | Gate Condition (512 / CVS) | Upstream System |
|---|---|---|---|
| ATO certifies configuration, not execution | Runtime drift not captured between assessment cycles | Constraint set derived from committed specification; drift conditions produce denial and gap record | Authorization Management / Configuration Control |
| Human oversight undocumented at decision point | Analyst approval recorded; reasoning absent | Without structured reasoning input, the approval does not commit | Agency Review Process / AI Governance |
| Continuous monitoring records telemetry, not decisions | Decision-level evidence requires reconstruction from correlated logs | Evidence Object created at execution time; no reconstruction required | IT Operations / ISSO |
| Degraded operation invisible in evidence chain | Fallback processing classified but not witnessed | Degraded state recorded explicitly; gap bounded and timestamped | COOP / Continuity Planning |
| Control mappings asserted, not runtime-verified | SSP mapping valid at assessment; no mechanism verifies it at execution | Control attestation evaluated at each execution event; failed attestation produces denial | Security Engineering / Authorizing Official |

---

## Boundary Failures Are Authorization Intelligence, Not Authorization Risk

When a proposed action fails at the execution boundary — authority not attested, model calibration expired, reasoning record absent — the failure does not originate in the execution system. It originates in a dependent upstream system that was not ready when execution was attempted. The boundary does not create the problem. It exposes it precisely.

Each failure is resolved at the source — authority governance, model validation, review process design. What was previously interpreted into compliance at execution is now required before execution. As the boundary extends across connected systems, the upstream functions align: authority registries attest scope before actions execute, model governance certifies calibration before models authorize straight-through processing, policy owners define constraint sets for every authorized decision category.

In the early phase, this produces visible friction. More actions fail than the current model permits. That friction is accurate — it reflects the actual gap between declared authorization and live execution. Each failure identifies a specific upstream gap. Each gap, resolved at its origin, removes a future failure permanently. The friction is front-loaded and finite.

---

## The Constraint Architect: A New Role and a New Professional Services Category

The primary failure point is not enforcement. It is constraint definition.

512 enforces precisely what it is declared to enforce. Bad constraint definitions produce perfectly wrong outcomes — denied actions that should proceed, admitted actions that should not, authority scopes that do not reflect actual delegation structures, model calibration requirements that do not correspond to real model risk profiles. The gate is deterministic. The quality of what it enforces is entirely a function of how the constraint set was defined.

This points to a function most federal agencies and GovCon primes do not yet have a name for: the **Constraint Architect** — the practitioner who translates governance intent into machine-enforceable constraint sets, closing the gap between what policy declares and what the gate enforces. In a federal context, this means specifying, in machine-enforceable terms, what delegated purchasing authority scope looks like as a cryptographic attestation, what an AI model reliability certification must contain before it authorizes straight-through processing, and what a structured analyst reasoning record must include before human oversight of a flagged decision is considered evidenced.

The Constraint Architect is both a new role and a new professional services category. The analogy is direct: when organizations undertook major operational transitions — process reengineering, ERP adoption, post-Sarbanes-Oxley control redesign — they did not attempt to develop the required expertise internally from scratch. They engaged specialist firms. Constraint architecture is the same category of engagement: a scoped, deliverable professional services function that produces a machine-enforceable constraint set the gate runs against — without requiring the agency to develop or permanently staff that capability internally before deployment begins.

This is a necessary global macro transition. The shift from interpretive to determinative execution systems does not happen without upfront friction — constraint definitions to write, upstream systems to align, authority registries to formalize, model governance cadences to establish. That friction is real, front-loaded, and finite. What it produces on the other side is authorization that is structural rather than administrative: a system where compliance is not constructed after the fact but verified at the moment of action, where audit is retrieval rather than reconstruction, and where the cost of exception handling, rework, and regulatory exposure declines continuously as the constraint surface matures.

---

## Path to Implementation

**Phase 1 — Observation.** CVS deploys as an independent witness of the existing federal AI system. No system changes. No workflow interruption. The output is the first accurate baseline of execution conformance: which decisions route automatically, which require human review, which involve override authority, where evidence chain gaps appear, and how frequently each failure mode occurs. This record has immediate ATO utility and defines the constraint surface precisely before any enforcement is designed.

**Phase 2 — Passive Evaluation.** The 512 boundary deploys in pre-enforcement evaluation mode. Every proposed action is evaluated against the declared constraint set. Execution is not blocked. The output is a readiness signal: the distribution of allow and deny results across actual transaction volume, with CVS recording any ungoverned periods as evidence chain gaps — before a single action is affected. Constraint definitions are hardened against real behavior. Upstream systems are identified and aligned.

**Phase 3 — Selective Enforcement.** The gate activates on the highest-risk execution surfaces first: delegated authority overrides, AI-flagged exception approvals, high-value contract actions. Full deployment follows as constraint definitions mature and upstream systems align. At each phase, the evidentiary record is complete for governed surfaces and explicitly bounded for surfaces not yet enrolled.

**Phase 4 — Full Enforcement.** The entire execution surface operates inside the gate boundary. Authority registries attest scope before overrides execute. Model governance certifies calibration before models authorize straight-through processing. Policy owners have defined constraint sets for every authorized decision category. Authorization is no longer a certification that precedes the system. It is a property that every execution event carries.

---

## Authorization Cannot Be Achieved After Execution

The five structural gaps documented in this paper exist in production federal AI environments — systems that are well-resourced, actively maintained, and operating under the same authorization frameworks that mandate the records they cannot produce. The conditions that produce those gaps are architectural properties shared by most federal AI deployments currently in operation.

The regulatory enforcement trajectory makes the consequence concrete. Agencies that deploy AI systems without execution-bound evidence face growing exposure under AI RMF-aligned authorization requirements, OMB M-25-21 implementation guidance, and the expanding oversight posture of Inspector General and GAO functions developing AI-specific audit methodologies. The question is not whether these frameworks will require execution-bound evidence. They already require it in principle. The question is when the enforcement posture catches up with the architectural gap — and whether the agency's authorization record is ready when it does.

Adding more frequent assessments, enhanced telemetry, or richer compliance platforms to a system that records outcomes but not decisions produces a more detailed record of the same structural absence. The authorization boundary remains in the wrong place. The evidence remains reconstructed. The compliance platform still cannot independently verify itself.

Authorization constructed before execution — enforced at the commit boundary, witnessed independently by CVS — is not a stronger version of current authorization practice. It is a different category, operating at the only moment when the question of what was authorized still has a determinable answer.

This architecture does not improve authorization. It replaces it at the point where authorization becomes real.

---

## Regulatory Alignment

| Framework | Core Requirement | Gap in Current Architecture |
|---|---|---|
| NIST AI RMF 1.0 | End-to-end traceability; decision reconstruction under audit | ATO certifies declared configuration; runtime execution produces no independent decision record |
| OMB M-25-21 | Meaningful human oversight for high-impact AI decisions | Analyst approval recorded; reasoning structurally absent at point of highest regulatory exposure |
| FedRAMP Continuous Authorization | Ongoing control verification beyond point-in-time assessment | Continuous monitoring captures telemetry; decision-level evidence requires reconstruction |
| FISMA / NIST SP 800-53 | Unbroken audit trail; non-repudiation; access enforcement | Control mappings asserted at assessment time; no mechanism verifies them at execution |
| EO 14110 (and successors) | Auditable records of AI behavior in safety-critical applications | Degraded mode operation classified but not independently witnessed in evidence chain |

---

*Unauthorized by Design | Version 4.0 | May 2026*
*Authors: Jonathan M. Watson · Mark Gomez (AGICOMPLY)*
*512 / CVS Architecture Series*
*Released under CC BY 4.0 consistent with 512 repository licensing.*
*Canonical kernel SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`*
