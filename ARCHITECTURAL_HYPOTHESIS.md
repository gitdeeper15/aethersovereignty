# AetherSovereignty — Architectural Hypothesis

**Status:** Phase 0 — Architectural Hypothesis (Complete)
**Version:** 1.0.0
**Date:** 2026-11-22
**Author:** Samir Baladi
**ORCID:** [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029)
**License:** CC-BY-4.0
**Position in the Aether family:** Eleventh candidate
**Decision:** (E) Undetermined (interim)

---

## 0. Status of this document

This document states a **hypothesis**. It does not state a result.

- It does **not** claim that AetherSovereignty is an independent architectural dimension.
- It does **not** claim that the gap it describes is genuine.
- It does **not** claim that the boundaries with the existing Aether dimensions are sufficient.
- It does **not** authorize implementation.

The next steps are: independent review of this hypothesis, execution of the falsification conditions, and a decision on architectural independence. Only after that decision may specification or implementation begin.

---

## 1. Position in the Aether family

The Aether family currently has **seven foundational dimensions**, **three candidates** (Identity, Policy, Audit), and **this candidate** (Sovereignty, eleventh).

| # | Project | Status |
|---|---|---|
| 1 | AetherGit | Foundational |
| 2 | AetherFlow | Foundational |
| 3 | AetherProof | Foundational |
| 4 | AetherMesh | Foundational |
| 5 | AetherGovern | Foundational (boundary unresolved) |
| 6 | AetherRuntime | Foundational |
| 7 | AetherOrchestrate | Foundational |
| 8 | AetherIdentity | Candidate (unresolved) |
| 9 | AetherPolicy | Candidate |
| 10 | AetherAudit | Candidate |
| 11 | **AetherSovereignty** | **Candidate (this document; Phase 0)** |

AetherSovereignty is the **eleventh project**. It is **not** a replacement for AetherGovern, AetherIdentity, or any other dimension.

### 1.1 Structural dependency

AetherSovereignty is **structurally dependent** on the resolution of AetherGovern and AetherIdentity. Both are currently unresolved.

- If AetherGovern absorbs the sovereignty question, the boundary between governance and sovereignty must be redrawn.
- If AetherIdentity absorbs the sovereignty question, the boundary between identity and sovereignty must be redrawn.

This dependency is treated as a threat to validity (T7), not as a detail.

---

## 2. Central question

> **Does sovereignty — the structural responsibility that organizes authority, normative reference, and veto relations within an autonomous agent system — constitute an independent architectural dimension, or is it merely an emergent descriptive label for the interaction of existing dimensions?**

The question has four clauses, each mapped to a failure condition:

| Clause | Condition |
|---|---|
| (i) Not already covered by Govern / Identity / Runtime | **AS-F1** |
| (ii) Does not decompose into Govern + Identity + Runtime | **AS-F2** |
| (iii) No central sovereignty authority required | **AS-F3** (embedded in H3) |
| (iv) No irreducible epistemic or architectural addition missing | **AS-F5** |

A positive answer needs all four. A negative answer on any one is sufficient to reject the candidate as a separate dimension.

---

## 3. Four-level functional stratification

The investigation distinguishes four analytical levels:

1. **Psychological Decision-Making.** The cognitive, affective, and motivational processes through which decisions are generated.
2. **Decision Authority.** The mechanism or process that resolves direct conflicts between competing behavioral options.
3. **Normative Authority.** The source of the criteria, priorities, and evaluative standards by which options are judged.
4. **Sovereignty Architecture.** The structural organization, connection, and governance of the relations among the first three levels.

**Methodological guardrail.** The existence of these four distinctions does *not* constitute evidence of an independent architectural entity. They serve strictly as analytical coordinates to test a core structural dilemma.

---

## 4. Testing dichotomy

Two competing hypotheses:

- **H1 — Emergent Reducibility:** What is called "sovereignty" is an emergent descriptive label for the interaction of established psychological and architectural processes. It adds no independent structural responsibility.
- **H2 — Irreducible Architectural Responsibility:** There exists a structural responsibility that governs the relation among the lower three levels and cannot be fully reconstructed from their interaction.

These hypotheses are exhaustive within the investigation's scope.

**Asymmetry.** H1 can be supported by demonstrating that the four-level description collapses into a three-level description without loss. H2 cannot be supported by the mere absence of such a demonstration; it requires a positive specification of what level 4 adds.

---

## 5. Falsification conditions (AS-F1 to AS-F5)

| ID | Condition under test | Status |
|:-:|---|---|
| **AS-F1** | Functional Duplication: the sovereignty functions are not already covered by AetherGovern, AetherIdentity, or AetherRuntime. | NOT FALSIFIED (untested) |
| **AS-F2** | Reconstructability: the four-level stratification does not fully decompose into levels 1–3; a remainder survives. | NOT FALSIFIED (untested) |
| **AS-F5** | Emergent Epistemic Reducibility: the sovereignty architecture adds an irreducible structural responsibility beyond existing dimensions. | NOT FALSIFIED (untested) |

All three conditions are **untested**. The decision rule: a positive answer requires all three to be tested with none falsified.

---

## 6. What this document does not claim

- That AetherSovereignty is an independent architectural dimension.
- That the four-level stratification is evidence of four independent components.
- That the boundaries with the existing dimensions are sufficient.
- That the gap is genuine.
- That implementation should begin.

This document claims only that the hypothesis is worth investigating under the stated methodology.

---

## 7. Threats to validity

| # | Threat | Description |
|:-:|---|---|
| **T1** | Author-on-author reasoning | The hypothesis and the decision are written by the same author. |
| **T2** | No independent review | Phase 2 (independent review) has not started. |
| **T3** | Structural dependency on AetherGovern and AetherIdentity | Both are unresolved; any conclusion is conditional. |
| **T4** | Cooperative-human assumption | The investigation assumes cooperative human principals. |
| **T5** | Irreducible trust anchor | An irreducible trust anchor may exist that the four-level stratification does not cover. |
| **T6** | No measurement | AS-F1, AS-F2, AS-F5 are untested; no evaluation has been run. |
| **T7** | Unresolved Govern and Identity | Boundaries with these dimensions cannot be drawn until they are stabilized. |

---

## 8. Falsification-first methodology

AetherSovereignty follows the falsification-first methodology:

1. **Architectural Hypothesis** (this document).
2. **Conceptual Genesis and Methodological Reconstruction** (bracketing, not replacement).
3. **Four-Level Stratification** (analytical coordinates).
4. **Testing Dichotomy** (H1 vs. H2).
5. **Falsification Design** (AS-F1, AS-F2, AS-F5).
6. **Independence Decision** (currently: E — Undetermined, interim).
7. **Specification** — only if the independence decision is positive.
8. **Implementation** — only after specification.

**No implementation begins before step 6.**

Stopping after step 5 is a legitimate outcome. So is a negative decision.

---

## 9. Next steps

In order:

1. **Independent review** of this hypothesis and the boundaries.
2. **Falsification execution** for AS-F1, AS-F2, AS-F5.
3. **Independence decision**: is AetherSovereignty a separate dimension, a feature of AetherGovern, a feature of AetherIdentity, or a bounded extension of one of them?
4. **If independent**: specification (`SPECIFICATION.md`).
5. **If not independent**: report the result, and do not proceed to implementation.

---

## 10. Open questions (initial)

- **Q1.** Is "sovereignty" a property of the decision, the agent, or the delegation?
- **Q2.** Can sovereignty be expressed as a policy in AetherGovern, or does it require a new primitive?
- **Q3.** Can the four-level stratification be reduced to three levels without loss?
- **Q4.** Does the veto structure introduce a new attack surface?
- **Q5.** What is the minimal interface between AetherSovereignty and AetherGovern?
- **Q6.** What is the minimal interface between AetherSovereignty and AetherIdentity?
- **Q7.** Can sovereignty be decentralized, or does it require a central authority?
- **Q8.** How is structural independence distinguished from analytical convenience?
- **Q9.** What is the difference between "sovereignty" and "governance"?
- **Q10.** Is AetherSovereignty a dimension, a feature, or a bounded extension of an existing dimension?

These are initial questions. They are not final.

---

**AetherSovereignty v2.0.0 — Architectural Hypothesis (Complete)**
© 2026 Samir Baladi — Ronin Institute / Rite of Renaissance
DOI: 10.5281/zenodo.24433970
