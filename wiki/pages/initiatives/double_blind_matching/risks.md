---
title: "double_blind_matching_risks"
type: "initiative"
initiative_name: "Double-Blind Bicultural Matching"
status: "active"
---

# double_blind_matching_risks

This risk register outlines the operational, technical, and privacy risks associated with the Double-Blind Bicultural Matching initiative [[wiki/pages/sources/source_bicultural_onboarding_prospectus#L20-L21|Source Onboarding Prospectus, §3.1]].

## 1. Risk Register Matrix

| Risk ID | Description | Severity | Probability | Mitigation Protocol |
|---|---|---|---|---|
| **MR-01** | **Deanonymization Leak**: Candidate identity or community membership is inadvertently exposed via unique details in the anonymous match narrative. | High | Medium | **Entity Scrubbing Filter**: The translation pipeline strips all specific geographical names, family markers, and distinct local landmarks, replacing them with generic regional tokens (e.g. "Local Treaty 7 river system") [[wiki/pages/sources/source_manyguns_roadmap#L18-L18|Source Manyguns Roadmap, §1.3]]. |
| **MR-02** | **Capability Over-Translation**: The AI mapping engine translates narrative stewardship too loosely, matching candidates with roles that exceed their technical training. | High | Low | **Vector Distance Bounding**: The Cosolvent matching algorithm enforces strict capability boundaries. Any match requires a baseline of verified hands-on operational tasks, not just conceptual alignment. |
| **MR-03** | **Readiness Checklist Gaming**: Employers misrepresent their readiness or support programs to access candidate pools without making actual structural accommodations. | Critical | Medium | **Facilitator Post-Placement Audit**: If a Shared Facilitator logs that an employer fails to honor scheduling flexibility, the employer's readiness rating is downgraded, and matching is paused. |
| **MR-04** | **Unbalanced Opt-in Friction**: The progressive disclosure steps create too many friction points, leading to dropouts before the reveal occurs. | Medium | High | **Interactive Story Delivery**: Keep match stories short (under 300 words) and allow simple one-click approvals to proceed to the next stage. |

---

## 2. Validation Metrics

Before deploying the matching loop in a live environment, the Cosolvent algorithms must pass:
1.  **Calibration Match Accuracy**: The AI-generated capability translations must align with manual evaluations from cultural HR specialists in at least 85% of test cases.
2.  **Privacy Leak Audit**: Automated red-teaming checks must confirm that zero personal identifier tokens (names, addresses, band registry IDs) escape the local OCAP boundary.
3.  **Simulated Matching Success**: ClientSynth digital twin simulations must demonstrate that bicultural match stories reduce pre-interview dropouts by 20% compared to typical resume exchanges [[wiki/pages/sources/source_bicultural_onboarding_prospectus#L20-L21|Source Onboarding Prospectus, §3.3]].

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
