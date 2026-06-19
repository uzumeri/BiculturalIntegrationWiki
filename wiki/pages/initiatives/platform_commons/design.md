---
title: "platform_commons_design"
type: "initiative"
initiative_name: "Ostrom-Based Platform Commons"
status: "active"
---

# platform_commons_design

This document defines the technical architecture and governance protocols required to enforce data sovereignty (OCAP) and apply Ostrom's commons principles to the platform's hosting and matching layer [[wiki/pages/sources/source_bicultural_integration_exchange_system#L23-L23|Source BCI System, §2.5]].

## 1. Decentralized OCAP Database Architecture

The platform separates matching logic from personal identity data to ensure community sovereignty:

```
               Sovereign Community Layer (OCAP)
+-------------------------------------------------------------+
|               Local Community Custodian Node                |
|  - Encrypted candidate records                              |
|  - Custodian Cryptographic Key (held by local facilitator)  |
+-------------------------------------------------------------+
                              |
                     (Opt-In Match Approval)
                              |
                              v (Anonymous Token Vector)
+-------------------------------------------------------------+
|               Central Matching Layer (Cosolvent)            |
|  - Runs vector search algorithms                            |
|  - Generates double-blind match stories                     |
+-------------------------------------------------------------+
```

### 1.1 Physical Separation
All personal information, work history narrative logs, and contact details are hosted exclusively on local, community-owned servers. Only anonymous vector tokens are transmitted to the central matching nodes.

### 1.2 Custodian Cryptographic Key Schema
Decryption of any narrative data requires two signatures:
1.  **Candidate Signature**: Confirms consent for a specific employer's match story.
2.  **Custodian Signature**: Cryptographic key held by the local **Shared Facilitator** verifying employer readiness [[wiki/pages/sources/source_manyguns_roadmap#L18-L18|Source Manyguns Roadmap, §1.3]].

---

## 2. Elinor Ostrom's Commons Design Principles Mapping

To prevent platform capture, governance parameters conform to Ostrom's design rules:

| Principle | Technical / Platform Implementation |
|---|---|
| **1. Group Boundaries** | Clear definitions of who is eligible to match. Verified Treaty 7 candidates and pre-vetted corporate employers. |
| **2. Local Rules** | Minimum wage thresholds, ceremonial leave buffers, and work-cycle parameters are set by local node voting, not central managers. |
| **3. Collective Choice** | Platform updates, service fees, and routing parameters require majority consensus from participating community nodes. |
| **4. Monitoring** | Community-approved **Shared Facilitators** audit workplace environments and check-in logs [[wiki/pages/sources/source_bicultural_integration_exchange_system#L21-L21|Source BCI System, §2.3]]. |
| **5. Graduated Sanctions** | Employers who fail audits face: (1) Warning, (2) Rating drop, (3) Suspended access to candidate pools. |
| **6. Conflict Resolution** | Tripartite mediation (Candidate, Employer, Facilitator/Elder) occurs prior to any formal termination or legal escalations. |
| **7. Self-Determination** | The system is structured so that any local community can copy their data state and run an independent node at any time. |
| **8. Nested Enterprise** | Local community databases are nested within the Treaty 7 regional coordination hub, which connects to the national procurement marketplace [[wiki/pages/sources/source_manyguns_roadmap#L20-L20|Source Manyguns Roadmap, §1.2]]. |

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
