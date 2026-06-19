---
title: "dynamic_scheduling_design"
type: "initiative"
initiative_name: "Dynamic Scheduling Rotation"
status: "active"
---

# dynamic_scheduling_design

This document defines the technical design and data structures for the **Transient Memory** scheduling engine running on the Cosolvent platform to coordinate peer-to-peer capacity rotations [[wiki/pages/sources/source_bicultural_onboarding_prospectus#L20-L21|Source Onboarding Prospectus, §3.1]].

## 1. Capacity Pool & Shift Aggregation Architecture

Rather than scheduling individual workers to fixed, rigid contracts, the system aggregates worker availability into a pooled model:

```
            +-------------------------------------------+
            |      Corporate Operational Shift Slot     |
            |     (e.g., 2 FTE Precision Machining)     |
            +-------------------------------------------+
                                  ^
                                  |
            +-------------------------------------------+
            |        Dynamic Sourcing Scheduler         |
            +-------------------------------------------+
              /                   |                   \
             v                    v                    v
+-----------------------+ +-----------------------+ +-----------------------+
|    Peer Worker A      | |    Peer Worker B      | |    Peer Worker C      |
| (Certified Machine Op)| | (Certified Machine Op)| | (Certified Machine Op)|
+-----------------------+ +-----------------------+ +-----------------------+
```

### 1.1 Capacity Pool Schema
Each pool tracks:
*   **Operational Certification Vector**: A list of certified machinery types, QA procedures (e.g. AS-9100), and site safety credentials.
*   **Availability Windows**: Declared seasonal obligations, preferred hours, and minimum weekly hours.
*   **Status Ledger**: Active schedules, historical rotation frequency, and peer-to-peer swap logs.

### 1.2 Transient Memory Engine
The scheduling calculations are managed within a transient memory space that:
1.  Stores active worker schedules.
2.  Monitors upcoming harvest alerts and ceremony windows.
3.  Computes optimal rotation matches within the capacity pool when a swap is requested.

---

## 2. Peer-to-Peer Rotation Workflow

```
[Worker A requests leave] -> [System checks Pool Certs] -> [Worker B confirms swap] -> [Ledger updates]
```

### 2.1 Step 1: Rotation Request
A worker submits a leave window (e.g. 5 days for seasonal harvest) via their local node.

### 2.2 Step 2: Peer Query
The system filters the local Capacity Pool to identify peers who:
1.  Hold the exact required **Certification Vector** for the target machine or assembly line.
2.  Are currently off-shift or have complementary availability.
3.  Have not exceeded maximum weekly shift hours.

### 2.3 Step 3: Peer-to-Peer Opt-In
The system sends a notification to qualified peers. Once a peer accepts the shift, the schedule is locked.

### 2.4 Step 4: ERP/Timesheet Synch
The system updates the corporate ERP timesheet via an API connector, ensuring safety audits see a qualified operator assigned to the slot.

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
