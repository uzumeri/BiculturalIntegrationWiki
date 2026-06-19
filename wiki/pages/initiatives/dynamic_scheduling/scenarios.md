---
title: "dynamic_scheduling_scenarios"
type: "initiative"
initiative_name: "Dynamic Scheduling Rotation"
status: "active"
---

# dynamic_scheduling_scenarios

This document records worked rotation case studies and validation tests for the Dynamic Scheduling engine [[wiki/pages/sources/source_bicultural_integration_exchange_system#L22-L22|Source BCI System, §2.4]].

## 1. Case Study: CNC Shop Sundance Ceremony Rotation

### The Setup
*   **Employer**: Apex Aerospace Components (Ontario).
*   **Capacity Pool**: POOL-CNC-CAL-01 (4 pre-certified CNC machine operators).
*   **Target Slot**: Slot CNC-02 (Day Shift, Monday–Thursday).
*   **Scheduled Operator**: Worker A (Siksika Nation member).
*   **Trigger**: Worker A requests 4 days off to attend and participate in the annual Sundance ceremony.

### System Rotation Execution
1.  **Request Logging**: Worker A logs the request via their local OCAP-compliant interface.
2.  **Peer Query**: The system queries the pool and identifies Worker B, who is currently assigned to a weekend rotation (Friday–Sunday) and has a clean safety audit record on Apex CNC lathes.
3.  **Swap Offer & Opt-in**: The system offers the Monday-Thursday slot to Worker B. Worker B accepts.
4.  **Schedule Update**: The system updates the Apex ERP workspace. The supervisor receives a notice that a qualified, certified operator is assigned to Slot CNC-02, preventing any safety anomalies or production pauses.

---

## 2. Case Study: Shared-FTE Autumn Harvest Block

### The Setup
*   **Employer**: Boreal Precision Fabricators.
*   **Capacity Pool**: POOL-ASSY-CAL-03 (3 pre-certified Assembly Technicians).
*   **Target Slots**: Slots ASSY-01 and ASSY-02 (2 Full-Time Equivalent slots).
*   **Scheduled Operators**: Worker X and Worker Y.
*   **Trigger**: The autumn moose harvest season begins, requiring members to take rotational blocks on the land.

### System Rotation Execution
1.  **Pre-planning Alert**: The system flags the upcoming seasonal harvest window.
2.  **Rotational Schedule Proposal**: The system compiles a three-way rotation plan for the three assembly technicians (Worker X, Worker Y, and Worker Z):
    *   *Block 1 (Days 1–5)*: Worker X and Worker Z work. Worker Y is on the land.
    *   *Block 2 (Days 6–10)*: Worker Y and Worker Z work. Worker X is on the land.
    *   *Block 3 (Days 11–15)*: Worker X and Worker Y work. Worker Z is on the land.
3.  **Approval & Commitment**: The three workers approve the plan via their local nodes. The system uploads the schedule to Boreal's HR portal, maintaining continuous double-occupancy on the assembly line.

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
