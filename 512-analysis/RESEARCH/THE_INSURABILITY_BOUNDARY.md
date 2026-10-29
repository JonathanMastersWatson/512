# The Insurability Boundary

**512 Research Archive — Analysis / Research**
**Document date:** 29 October 2026
**Evidence window:** 18 November 2025 – 22 October 2026
**Suggested placement:** `512-analysis/RESEARCH/THE_INSURABILITY_BOUNDARY.md`
**Status:** Draft for deployment in the 512 repository. Not a claim that 512 has been tested, accepted, or priced by any insurer, actuary, or underwriter.

> 512 describes a technical constraint on execution-time legitimacy. It does not prescribe policy, governance, or social outcomes. This document applies that constraint to one external problem — insurance — using dated, public evidence only.

---

## Thesis, tightened

Open-ended autonomous agents cannot yet obtain ordinary, scalable liability insurance on ordinary actuarial terms.

That is not the same as saying no insurance exists. Specialist coverage exists (see §5, dated 2025–2026). What does not yet exist is the underwriting infrastructure required for broad deployment:

- a standard exposure unit for delegated authority,
- a mature claims history,
- stable frequency and severity distributions,
- tested attribution models, and
- a reconstructable record of what was authorized, what was decided, and what was executed.

**The sharper wager:**

> Autonomous AI does not scale when the machine is capable of creating liabilities that neither the enterprise nor its insurer can bound, price, or reconstruct.

That is harder to dismiss than “agents need better governance,” because it names the party who will enforce the limit: the carrier who is asked to absorb the loss.

---

## 1. The actuarial problem, as stated by the field — 2026

**20 July 2026 — Szpruch et al., “Insuring AI: Incentivising Safe and Secure Deployment,” *Harvard Data Science Review* 8.3 (MIT Press), DOI 10.1162/99608f92.bd811034.**
Traditional actuarial practice estimates risk as frequency × severity. For AI, “both elements remain underspecified, as insurers lack validated loss experience data and probabilistic models for estimating the likelihood and severity of AI-caused harms.” The paper also argues insurers will require rigorous testing, monitoring, validation, and assurance artefacts — and that tying coverage to those artefacts is how insurance creates incentives for safer deployment.

*Note on attribution: the draft that prompted this document called this “MIT’s work.” The publisher is MIT Press; the authors are at the Alan Turing Institute, Oxford, Warwick, Imperial, Mila, NTU, and Sorbonne. The correction is recorded here rather than silently repeated.*

**13 July 2026 (v1; rev. 15 July 2026) — Trout et al., “Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack,” arXiv:2607.11999.**
Insurers’ exposure to AI agent risk “currently sits largely unpriced across existing insurance lines”; between silent coverage and growing exclusions, coverage is “not fit for purpose”; and “traditional actuarial modeling will struggle to keep pace with a technology evolving as rapidly as frontier AI.” The paper proposes building an entirely new, eight-component insurance stack: incident data collection, catastrophe modelling, standards, contract design, risk selection, pricing, monitoring, and claims management.

**March 2026 — Casualty Actuarial Society, *AI Primer: Practical Guidance for Actuaries*.**
The CAS treats agent underwriting as unsettled, highlighting thin audit trails, non-deterministic behaviour, cascading errors, and prompt-injection exposure, and advising underwriters to ask whether the path from prompt to production can be reconstructed after a loss — because logs and authorization records affect pricing, exclusions, and claims handling.

**21 October 2026 — Evan Greenberg, Chairman and CEO, Chubb, Q3 2026 earnings call (reported 22 October 2026, *Insurance Journal*).**
AI liability is “a growing and emerging exposure that is not contemplated in casualty underwriting really to date.” Greenberg predicted a combination of coverage clarifications, exclusions, and separate AI-related liability coverages, and said he could imagine model certification standards and best practices in the management and governance of AI and agentics emerging as tools to assist underwriting.

Three independent sources, in seven months, state the same core problem. That is confirmation of the premise, not commentary on it.

---

## 2. Why agents break the insurance model

A chatbot giving a bad answer is manageable. An agent can:

read → decide → transact → move money → modify records → enter commitments → call another agent → repeat, at machine speed.

### 2.1 The exposure unit is undefined

For a truck insurer, the exposure unit might be vehicle-miles. For workers’ compensation, payroll. For property, replacement value.

For an autonomous agent, there is no standard answer yet. Candidates include:

- API calls
- dollars under authority
- contracts executed
- records writable
- accounts accessible
- decisions per hour
- maximum transaction size
- number of downstream agents
- model version
- duration of the authority granted

### 2.2 The model is not the insured object. Delegated authority is.

The risk changes when the agent’s authority changes. The same model answering an employee’s question carries negligible liability compared with the same model holding credentials that permit it to transfer $10M.

An insurer is therefore not, in substance, underwriting a model. It is underwriting **delegated authority** — what the agent was permitted to do, by whom, within what limits, for how long.

### 2.3 There is no loss history to price from

An insurer needs a reasonable estimate of:

```
frequency × severity = expected loss
```

Agentic AI currently offers:

- no mature claims history,
- constant model changes,
- non-deterministic behaviour,
- changing prompts, tools, and context,
- changing delegated authority,
- uncertain legal attribution,
- potential correlated failure across millions of users of the same foundation model, and
- machine-speed loss propagation.

### 2.4 Correlation turns an error into a catastrophe exposure

Traditional insurance assumes substantial independence between insured losses. Agents break that assumption:

```
one model failure → 50,000 enterprises → correlated loss
```

That is catastrophe risk, not ordinary errors-and-omissions risk. Trout et al. (13 July 2026, §1) make the same point from the concentration side: concentration among a few foundation-model providers threatens correlated losses across the book.

---

## 3. Specialist insurance exists — the thesis must not overstate

**2024 / 30 April 2025 / January 2026 — Armilla (Lloyd’s).**
Armilla Insurance Services, a Lloyd’s coverholder dedicated to AI liability, launched a standalone affirmative AI liability policy underwritten at Lloyd’s in April 2025, covering algorithmic error, model drift, and hallucinations. In January 2026 its published limits rose to USD $25M or more per organization. In February 2026 Armilla and Chaucer launched a coordinated structure pairing cyber and technology E&O cover with the standalone AI policy.

**2018–2026 — Munich Re, aiSure.**
Munich Re offers specialist AI performance coverage (aiSure), using model evaluation and performance data to estimate risk and settling on measurable performance failure. On 26 February 2026, Mosaic Insurance partnered with Munich Re to write aiSure at an initial capacity of USD/EUR/CAD $15M. On 18 March 2026, HSB (Munich Re group) introduced AI liability cover for small and mid-sized businesses in the United States.

**2025–2026 — CFC.**
CFC states that traditional cyber/technology classifications do not fit autonomous AI neatly, and has been extending affirmative AI cover across its portfolio.

So, stated precisely:

- “Agents cannot be insured.” — **False.**
- “Unbounded autonomous agents cannot currently be commoditised, actuarially priced, and insured at enterprise scale like conventional operational risk.” — **Supported by the dated evidence above.**

That distinction is the document. Lose it, and the thesis is dismissible.

---

## 4. Deployment is running into the same wall — dated

Capability and deployment are accelerating. Authority is not being granted at the same rate.

- **April 2026 — Stanford HAI, *2026 AI Index Report*.** Agent task success on OSWorld rose from ~12% to ~66% in a year — while still failing roughly one task in three.
- **18 November 2025 — MIT Sloan Management Review / BCG, *The Emerging Agentic Enterprise*.** 35% of organizations had already adopted agentic AI; a further 44% planned to deploy it soon.
- **2026 (reported October 2026) — Gartner, 2026 CIO and Technology Executive Survey.** ~17% of organizations have deployed agents; more than 60% expect to within two years. Gartner separately forecasts that more than 40% of agentic AI projects will be cancelled by the end of 2027, on escalating costs, unclear business value, or inadequate risk controls.
- **April 2026 — Grant Thornton, *2026 AI Impact Survey* (950 senior executives).** Only **5%** of organizations allow agents to execute high-stakes decisions without human review; 60% limit agents to moderate-risk task automation; only 20% have a tested AI incident-response plan.
- **24 April 2026 — Deloitte, *State of AI in the Enterprise 2026* (3,235 leaders, 24 countries).** Only 21% report a mature governance model for agentic AI; approximately **80%** lack mature agent-governance capabilities — defined to include clear decision boundaries, real-time monitoring, and audit trails capturing the full chain of agent actions.
- **1 January 2026 — Verisk / ISO.** Optional generative-AI exclusion endorsements for commercial general liability took effect for carrier attachment — CG 40 47, CG 40 48, and CG 35 08 (edition 01 26), filed in mid-2025. By mid-2026, a nationwide review found 2,369 generative-AI exclusion records in force across 49 states.

The 5% figure is the tell. Companies are not necessarily afraid of agents performing work. They are afraid of agents possessing **unbounded consequential authority**.

There is a material difference between:

> “Prepare the invoice.”

and

> “Issue the invoice.”

and

> “Negotiate the amount, contract with the customer, issue the invoice, receive funds, and resolve disputes.”

The first is productivity software. The last is an economic actor. Insurance suddenly matters.

---

## 5. What insurers are beginning to ask for — and where 512 sits

This document does **not** claim that 512 solves insurance. 512 has not been tested by carriers or actuaries, and no such claim is made anywhere in this repository.

What can be claimed, on dated evidence, is that the requirements insurers and governance bodies are now publishing describe the same problem space 512 was defined for:

- **22 September 2026 — BCG, “The Authorization Gap: Why Yesterday’s Controls Won’t Work with Today’s Agents.”** Agents need purpose- and conduct-bound authorization, traceable delegation, and enforceable limits: which agents are operating, what they are authorized to do, who delegated that authority, and what stops an agent that pursues its goal by the wrong means.
- **26 May 2026 — World Economic Forum / Capgemini, *AI Agents in Action: A Playbook for Trusted Adoption, Authorization and Scaling*.** Introduces the Agent Capability and Authorization Profile (ACAP) — a deployment-level authorization instrument intended to make delegated decisions and actions auditable, enforceable, and accountable across the deployment life cycle.
- **20 July 2026 — Szpruch et al. (above).** Insurers will require rigorous testing, monitoring, validation, and assurance artefacts.
- **21 October 2026 — Greenberg, Chubb (above).** Certification and agent-governance standards will likely become underwriting tools.
- **March 2026 — Casualty Actuarial Society (above).** Underwriters should ask whether they can reconstruct the path from prompt to production after a loss.

Translated into underwriting language, an insurer does not primarily need to know:

> “Is this AI intelligent?”

It needs to know:

1. What was it permitted to do?
2. What could it not do?
3. Who gave it that authority?
4. Was that authority enforceable *before* execution?
5. What actually happened?
6. Can you prove it after the event?

512 addresses bounded admissibility **before** execution — whether a proposed action satisfies pre-declared constraints at the commit boundary, returning ALLOW or DENY and no third state.

An independent evidence witness (in this research line, the Evidence-Sidecar / CVS architecture, maintained separately from this repository) addresses the second half: independent evidence of what was authorized, decided, and executed.

From an insurance perspective, that changes the object being underwritten from:

> “Trust this probabilistic agent.”

to something closer to:

> “Insure the financial exposure created inside this provable execution envelope.”

That is a fundamentally easier underwriting problem. It is a statement about the *shape* of the problem, not a claim of a tested solution.

---

## 6. The deployment wall

Insurance may become one of the largest brakes on the productivity gains projected for agentic AI — not model capability, not tokens, not compute. **Liability.**

An enterprise will happily let an agent summarize documents, prepare reports, write draft code, and research suppliers. Those are large productivity gains, and they carry bounded exposure.

Then somebody says: “Let it execute.”

Legal asks who carries liability. Risk asks whether E&O covers it. The broker calls the carrier. The carrier asks what controls exist. The CTO answers: the agent has IAM permissions and an audit log.

The insurer asks:

> Can it take an unauthorized-but-technically-permitted action?

And the conversation stops. BCG named exactly this failure on 22 September 2026: an agent can remain inside its instructions and permissions and still cause harm, because yesterday’s controls governed access, not purpose and conduct.

That is the deployment wall.

---

## 7. The five signals, dated

These five conditions, all documented above, cannot coexist indefinitely:

1. **Capability accelerating** — OSWorld success ~12% → ~66% in one year (Stanford AI Index, April 2026).
2. **Deployment accelerating** — 35% adopted, 44% planning (MIT Sloan / BCG, 18 November 2025); 17% deployed, >60% expecting to within two years (Gartner, 2026).
3. **Governance lagging** — ~80% lack mature agent-governance capabilities (Deloitte, 24 April 2026); only 5% permit high-stakes decisions without human review (Grant Thornton, April 2026).
4. **Insurance retreating or separating the exposure** — ISO generative-AI exclusions effective 1 January 2026 (Verisk); separate AI liability products and certification predicted by Chubb’s CEO, 21 October 2026.
5. **Actuarial science without a loss history** — frequency and severity “underspecified” (Szpruch et al., 20 July 2026); agent risk “largely unpriced,” coverage “not fit for purpose” (Trout et al., 13 July 2026).

Something has to emerge between agent capability and capital willing to absorb agent liability.

The winning layer will probably not be another AI ethics dashboard. On the evidence above, it will look like risk infrastructure:

```
bounded authority → deterministic constraints → execution evidence
→ exposure measurement → underwriting → insurance capacity
```

That is where the economic bottleneck is forming — and it is the boundary 512 was defined to describe.

---

## Sources (all dates verified 29 October 2026)

1. Szpruch, L. et al. “Insuring AI: Incentivising Safe and Secure Deployment.” *Harvard Data Science Review* 8.3, MIT Press. Published 20 July 2026. DOI: 10.1162/99608f92.bd811034 — https://hdsr.mitpress.mit.edu/pub/f10qbic0/release/1
2. Trout, C. et al. “Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack.” arXiv:2607.11999. Submitted 13 July 2026; revised 15 July 2026. — https://arxiv.org/abs/2607.11999
3. Greenberg, E. Chubb Q3 2026 earnings call, 21 October 2026; reported in “Chubb CEO Greenberg: Industry Has to ‘Put Arms Around’ AI Liability,” *Insurance Journal*, 22 October 2026. — https://amp.insurancejournal.com/news/national/2026/10/22/889993.htm
4. Casualty Actuarial Society. *AI Primer: Practical Guidance for Actuaries*. March 2026. — https://www.casact.org/sites/default/files/2026-03/CAS-AI-Primer-Practical-Guidance-for-Actuaries.pdf
5. Nudelman, S. et al. “The Authorization Gap: Why Yesterday’s Controls Won’t Work with Today’s Agents.” BCG, 22 September 2026. — https://www.bcg.com/publications/2026/authorization-gap-ai-agent-governance
6. World Economic Forum / Capgemini. *AI Agents in Action: A Playbook for Trusted Adoption, Authorization and Scaling*. 26 May 2026. — https://www.weforum.org/publications/ai-agents-in-action-a-playbook-for-trusted-adoption-authorization-and-scaling
7. MIT Sloan Management Review / BCG. *The Emerging Agentic Enterprise*. 18 November 2025. — https://www.bcg.com/press/18november2025-agentic-ai-blurs-line-tool-teammate
8. Gartner. 2026 CIO and Technology Executive Survey; Hype Cycle for Agentic AI, October 2026 (17% deployed; >60% within two years; >40% of projects forecast cancelled by end of 2027).
9. Grant Thornton. *2026 AI Impact Survey*. April 2026. — https://www.grantthornton.com/services/advisory-services/artificial-intelligence/2026-ai-impact-survey
10. Deloitte. “Agentic AI is scaling faster than guardrails,” *State of AI in the Enterprise 2026*, 24 April 2026 (survey of 3,235 leaders). — https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html
11. Stanford Institute for Human-Centered AI. *2026 AI Index Report*. April 2026 (OSWorld ~12% → ~66%). — https://hai.stanford.edu/ai-index/2026-ai-index-report
12. Verisk / ISO. Generative-AI exclusion endorsements CG 40 47, CG 40 48, CG 35 08 (edition 01 26), filed mid-2025, available for carrier attachment from 1 January 2026.
13. Armilla Insurance Services (Lloyd’s coverholder). Standalone AI liability policy launched April 2025; limits raised to USD $25M+, January 2026; Armilla–Chaucer coordinated structure, February 2026.
14. Munich Re / Mosaic Insurance. aiSure partnership, 26 February 2026 ($15M initial capacity); HSB AI liability for SMBs, 18 March 2026.

---

*End of document. Prepared for the 512 research archive, 29 October 2026. No insurer, actuary, or underwriter has tested, endorsed, or priced 512; this document claims only that the dated public evidence in §1–§7 describes the problem 512 was defined for.*
