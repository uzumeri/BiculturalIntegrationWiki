---
title: "double_blind_matching_design"
type: "initiative"
initiative_name: "Double-Blind Bicultural Matching"
status: "active"
---

# double_blind_matching_design

This document defines the architectural specifications and vector representation mechanics for the **Progressive trust-intermediated** matching engine built on the Cosolvent framework [[wiki/pages/sources/source_bicultural_onboarding_prospectus#L20-L21|Source Onboarding Prospectus, §3.1]].

## 1. Matching Engine Architecture

The platform translates narrative experiences into industrial capacities, bypassing keyword resume filters.

```
       Candidate Data                               Employer Data
+-------------------------+                 +---------------------------+
| Narrative Work History  |                 | Workplace Readiness Check |
| (Stewardship, Harvesting)|                 |  (Culture & Support Plan) |
+-------------------------+                 +---------------------------+
             |                                            |
             v (AI Mapping Layer)                         v (AI Mapping Layer)
+-------------------------+                 +---------------------------+
|  Auditable Capability   |                 | Structured Accommodation  |
|      Vector Space       |                 |        Vector Space       |
+-------------------------+                 +---------------------------+
             \                                           /
              \                                         /
               v                                       v
         +---------------------------------------------------+
         |  Cosolvent Bicultural Match Optimization Engine   |
         +---------------------------------------------------+
                                   |
                                   v
                     +---------------------------+
                     |    Bicultural Match Story  |
                     +---------------------------+
```

### 1.1 Narrative-to-Expository Capability Mapping
The mapping layer translates narrative-register statements into standard operational terms:
*   *Narrative Input*: "Coordinated multi-family seasonal fish camp operations at Bow River weir, managing equipment allocations, safety briefings, and youth mentorship."
*   *Expository Output*: "Multi-domain logistics management, process safety governance, personnel onboarding orchestration (equivalent to Shop Lead/Foreman)."

### 1.2 Structured Accommodation Mapping
Employers must declare concrete support plans in their readiness profiles:
*   *Flexibility Allocation*: Allotted paid days for seasonal harvesting or traditional ceremonies.
*   *Mentorship Bindings*: Assigned internal buddy and connection to local Shared Facilitators.

---

## 2. Progressive Disclosure States

To mitigate bias and prevent strategic exposure, profiles go through three gated states:

### 2.1 State 1: Double-Blind Match (Decoupled)
*   **Employer View**: Candidate is represented only by capability vectors and anonymous summary profiles (e.g. "Candidate #TB-702 - Experienced Shop Floor Coordinator").
*   **Candidate View**: Employer is represented only by operational readiness metrics and cultural support ratings.

### 2.2 State 2: Bicultural Match Story (Blended)
*   The system generates a custom **Bicultural Match Story** for each party.
    *   *Candidate Story*: Tells how the company's team and culture will support their integration.
    *   *Employer Story*: Illustrates how the candidate's capabilities will solve concrete operational bottlenecks (such as shipping delays or tool-room audits).

### 2.3 State 3: Decrypted Reveal (Mutual Consent)
*   Only after *both* the candidate and the employer approve the Bicultural Match Story does the system exchange cryptographic keys to reveal names, contact details, and locations.

---

## 3. Sovereign Storage & OCAP

To align with Ostrom commons principles and data sovereignty (OCAP):
1.  **Distributed Node Ingestion**: Candidate narrative data is stored on community-hosted local databases.
2.  **Encrypted Token Vectors**: Only anonymous vector tokens are transmitted to the central Cosolvent matching node.
3.  **Local Access Control**: Any decrypt requests require approval from the community facilitator's local node key [[wiki/pages/sources/source_manyguns_roadmap#L18-L18|Source Manyguns Roadmap, §1.3]].

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
