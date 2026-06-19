---
title: "facilitator_pooling_design"
type: "initiative"
initiative_name: "Shared Facilitator Pooling"
status: "active"
---

# facilitator_pooling_design

This document defines the functional specifications and database structures for the **Sovereign Facilitator Registry** and the shadow capacity allocation algorithms running on the Cosolvent/CommonContext stack [[wiki/pages/sources/source_bicultural_onboarding_prospectus#L20-L21|Source Onboarding Prospectus, §3.1]].

## 1. Tripartite System Architecture

The platform coordinates real-time interactions between three entities, ensuring that every placement is supported by a relational custodian.

```
                    +---------------------------+
                    |    Shared Facilitator     |
                    |   (Relational Custodian)  |
                    +---------------------------+
                     /                         \
                    /                           \
                   /                             \
                  v                               v
    +---------------------------+   +---------------------------+
    |         Candidate         |   |         Employer          |
    |    (Narrative Profile)    |   |    (Readiness Profile)    |
    +---------------------------+   +---------------------------+
```

### 1.1 Facilitator Registry Schema
Facilitators register via secure local OCAP nodes. The schema tracks:
*   **Affiliation Bounding**: Validated Treaty 7 community membership (e.g. Siksika, Tsuut'ina, Stoney Nakoda).
*   **Capacity Slot availability**: Weekly hours allocated for shadowing (default: 5 hours per active candidate, max 4 candidates per facilitator).
*   **Skill Specializations**: Traditional language skills, dispute resolution experience, and industry familiarity.

### 1.2 Capacity Allocation & Matching
When a candidate placement is confirmed:
1.  **Geographic Bounding check**: The system filters the registry to identify facilitators in the candidate's home Treaty area.
2.  **Capacity Check**: Identifies facilitators with at least 1 free capacity slot.
3.  **Ontology Match**: Matches the candidate's background and the employer's industry with the facilitator's expertise.

---

## 2. Tripartite Checkpoint Protocol

To maintain onboarding alignment, the system manages a automated checkpoint loop:

### 2.1 Micro-Surveys (Weekly Tokens)
*   **Candidate Token**: A 2-question survey checking comfort level and workload equity.
*   **Employer Token**: A 2-question survey checking process quality and scheduling alignment.
*   If either token records a negative response, a **Resolution Alert** is sent to the Facilitator.

### 2.2 Milestone Reviews
Facilitators lead reviews at Day 15, Day 30, and Day 90:
*   **Verification**: Reviewing the candidate's comfort with the Dual-Register Playbooks.
*   **Feedback Integration**: Gathering operational notes from the shop supervisor.
*   **Sign-off**: Recording milestone completion in the ledger.

---

## 3. Financial Settlement & Honoraria

To bypass institutional payment delays that alienate participants:
*   **Immediate Honoraria Bridge**: The platform matches facilitator hours and issues payments immediately upon checkpoint completion, bridging university or corporate invoice lags [[wiki/pages/sources/source_manyguns_roadmap#L21-L21|Source Manyguns Roadmap, §4.1]].
*   **B2B Service Fee Integration**: The platform collects a pooled service fee from employers (e.g. 15% of placement wages) to fund the facilitator pool.

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
