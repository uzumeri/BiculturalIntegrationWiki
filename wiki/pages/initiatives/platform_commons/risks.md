---
title: "platform_commons_risks"
type: "initiative"
initiative_name: "Ostrom-Based Platform Commons"
status: "active"
---

# platform_commons_risks

This risk register outlines potential governance, security, and structural failure modes for the Ostrom-Based Platform Commons initiative [[wiki/pages/sources/source_bicultural_integration_exchange_system#L23-L23|Source BCI System, §2.5]].

## 1. Risk Register Matrix

| Risk ID | Description | Severity | Probability | Mitigation Protocol |
|---|---|---|---|---|
| **CR-01** | **Custodian Key Loss**: A local Shared Facilitator loses or compromises their cryptographic custodian key, locking candidates out of matching pools. | High | Medium | **Multi-Signature Recovery**: Implement a 2-of-3 secret-sharing recovery scheme. The key can be reconstructed with signatures from (1) the candidate, (2) the local Band Council administration, and (3) the regional exchange coordinator. |
| **CR-02** | **Aggregator Capture**: A commercial partner attempts to migrate candidate data to a centralized commercial cloud to reduce operational latency. | Critical | Low | **Hardcoded Hosting Rules**: The matching engine's codebase includes strict verification logic that rejects database queries to servers that fail OCAP sovereignty validation [[wiki/pages/sources/source_manyguns_roadmap#L18-L18|Source Manyguns Roadmap, §1.3]]. |
| **CR-03** | **Local Node Isolation**: A local community node goes offline, preventing candidates from receiving match notifications. | Medium | Medium | **Failover Routing**: Temporarily route encrypted notifications through the Treaty 7 regional coordination hub, ensuring candidates do not miss opportunities. |
| **CR-04** | **Monitor Capture**: A facilitator is co-opted by an employer and fails to report workplace safety or cultural alignment issues. | High | Low | **Double-Loop Audit**: Candidates can submit feedback anonymously directly to the community elders' council, bypassing the facilitator. |

---

## 2. Validation Metrics

Prior to launching the multi-node pilot:
1.  **OCAP Separation Audit**: Automated test scripts must run daily to verify that zero candidate identifiers exist in the shared central matching database.
2.  **Key Recovery Success**: 100% of recovery coordinators must pass a quarterly multi-signature recovery drill.
3.  **Governance Transparency Ledger**: 100% of platform parameter votes (wages, standards) must be cryptographically recorded in the log ledger.

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
