---
id: ASIT2-PORTFOLIO-PRODUCTS-OV
rev: 4
field: portfolio
environment: cross-environment
configuration: n/a
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.1.1"
release_date: 2025-09-25
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: "MAL-EEM"
---

# ASI-T2 Product Portfolio

The ASI-T2 product portfolio, organized by a **Field × Environment** matrix. Each product represents a specific implementation and deployment of the ASI-T2 architecture, designed to accelerate the aerospace sustainable industry transition.

All products within this portfolio adhere to a unified development framework, ensuring consistency, reusability, and auditable compliance across the entire ASI-T2 ecosystem.

---

## Quick Nav

*   [Overview](#overview)
*   [Product Matrix](#product-matrix)
*   [Unified Product Development Framework](#unified-product-development-framework)
*   [QAIM-2 Integration Framework](#qaim-2-integration-framework)
*   [Portfolio Architecture & Cross-References](#portfolio-architecture--cross-references)
*   [Glossary & Acronyms](#glossary--acronyms)

---

## Overview

The ASI-T2 portfolio encompasses a range of advanced aerospace systems, each developed under a strict set of governing principles to ensure safety, sustainability, and performance.

**Core Governance & Architecture Principles:**

*   **TFA (Top Federation Algorithm / Threading Final Assembly):** A federated architecture that provides a single, auditable thread from design to certification for every product.
*   **UIX (Universal Injection Prompt):** Mandatory pre-flight rules enforced on all human and AI agents before executing tasks.
*   **MAL-EEM (Ethics & Empathy Module):** A fail-closed ethics and safety guardrail active across all systems and processes.
*   **UTCS / QS (Universal Traceability & Configuration System / Quantum Seal):** A mandatory evidence standard, generating deterministic provenance anchors for every significant engineering action.

---

## Product Matrix

Products are organized into three main product lines based on operational characteristics:

### Product Lines

**AMPEL360** - Manned aerospace (certified passenger transport) - 360° full circularity for all aerospace products that transport human passengers, including aircraft, space stations, and shuttles.

**GAIA-AIR** - Unmanned Air (UAM/UAV) - Autonomous unmanned aerial systems for commercial and defense applications.

**GAIA-SPACE** - Space-only (satellites & orbital robotics) - Autonomous space systems including satellite constellations and orbital servicing.

**GAIA-SEA** - Marine & Ocean Systems - Autonomous marine and oceanic systems for environmental monitoring, scientific research, and sustainable ocean operations.

**INFRANET** - Infrastructure and network systems, encompassing cross-cutting intelligence and ground physical infrastructures.

**MISCELLANEOUS** - Legacy and transitional products being evaluated for integration into appropriate product lines.

### Product Directory

| Product Line | Field | Environment | Product Name | Primary Domains | Description |
| ------------ | ----- | ----------- | ------------ | --------------- | ----------- |
| **AMPEL360** |       |             |              |                 |             |
|  | [`transport-civil`](../FIELDS/transport-civil/) | [`air`](../ENVIRONMENTS/air/) | [`BWB-Q100`](./AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/) | AAA, PPP, MEC, EEE, CQH | Blended Wing Body 100-passenger aircraft |
|  | [`space-tourism`](../FIELDS/space_tourism/) | [`space`](../ENVIRONMENTS/space/) | [`AMPEL360PLUS`](./AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/) | CCC, EDI, IIS, LCC, LIB, MEC, PPP, CQH | Suborbital/orbital tourism vehicle |
| **GAIA-AIR** |       |             |              |                 |             |
|  | [`cyberdefense`](../FIELDS/cyberdefense/) | [`air`](../ENVIRONMENTS/air/) | [`HYDROBOTS`](./GAIA-AIR/HYDROBOTS/) | EEE, CQH, IIS, AAA | Hydrogen UAM retail (logistics, delivery, inspection) |
|  | [`defense`](../FIELDS/defense/) | [`air`](../ENVIRONMENTS/air/) | [`ETHICS-EMPATHY-UAV`](./GAIA-AIR/ETHICS-EMPATHY-UAV/) | IIS, OOO, LCC, EDI, DDD | Ethical SHARM (STOP HARMFUL) logic for defense |
| **GAIA-SPACE** |       |             |              |                 |             |
|  | [`cyberdefense`](../FIELDS/cyberdefense/) | [`space`](../ENVIRONMENTS/space/) | [`SAT-CONSTELLATIONS`](./GAIA-SPACE/SAT-CONSTELLATIONS/) | DDD, IIS, EDI, LCC | Earth observation, communications & quantum satellites |
|  | [`cyberdefense`](../FIELDS/cyberdefense/) | [`space`](../ENVIRONMENTS/space/) | [`ORBITAL-MACHINES`](./GAIA-SPACE/ORBITAL-MACHINES/) | IIS, MEC, AAA, LCC | Debris removal, assembly & servicing |
| **GAIA-SEA** |       |             |              |                 |             |
|  | [`EER`](../FIELDS/EER/) | [`sea`](../ENVIRONMENTS/sea/) | [`GAIA-SOUND`](./GAIA-SEA/GAIA-SOUND/) | EER, IIS, EDI, LCC, LIB | Sea Organisms and Universal Nature Diagnostics |
| **INFRANET** |       |             |              |                 |             |
|  | [`cross`](../FIELDS/cross/) | [`cross`](../ENVIRONMENTS/cross/) | [`LH2-CORRIDOR`](./INFRANET/LH2_CORRIDOR/) | LIB, CQH, IIF, EEE, IIS | End-to-end green liquid hydrogen (LH2) value chain |
|  | [`quantum-intelligence`](../FIELDS/quantum-intelligence/) | [`digital`](../ENVIRONMENTS/digital/) | [`QAIM`](./INFRANET/QAIM/) | IIS, CQH, OOO, DDD | Core quantum-classical optimization & AI engine |
|  | Shared Templates | All | [`Templates`](./INFRANET/Shared/_templates/) | All | Shared boilerplates and templates |
| **MISCELLANEOUS** |       |             |              |                 |             |
|  | [`cyberdefense`](../FIELDS/cyberdefense/) | [`deep_space`](../ENVIRONMENTS/deep_space/) | [`LIGHTVIBES`](./MISCELLANEOUS/LIGHTVIBES/) | IIS, CQH, DDD | Quantum key management (migrated from root directory) |


---

## Migration Information

The ASI-T2 product portfolio has been reorganized into four strategic product portfolios for better operational clarity and management. For historical tracking and migration details, see:

- [`_migration/manifest.csv`](./_migration/manifest.csv) - Complete mapping of old to new paths
- Migration rationale follows operational characteristics:
  - **Passenger/crewed systems** → AMPEL360 (360° lifecycle management)
  - **Unmanned air systems** → GAIA-AIR (autonomous air operations)
  - **Space-only systems** → GAIA-SPACE (satellites & orbital robotics)
  - **Infrastructure/shared intelligence** → INFRANET (cross-cutting support)

### Recent Migration (2025-01-15)

The former GAIA_AIR_SPACE product line has been split into two focused portfolios:
- **GAIA-AIR**: All unmanned aerial systems (UAM/UAV)
- **GAIA-SPACE**: All space-only systems (satellites & orbital robotics)

This separation provides clearer domain focus and eliminates operational environment conflicts.

---

## Unified Product Development Framework

Every ASI-T2 product directory is structured identically to ensure seamless navigation, interoperability, and process standardization. This is achieved through the mandatory **Domain → Process → ATA** model.

### Standard Product Directory Structure

```
{field}_{environment}_{product-name}/
└── domains/
    ├── <DOMAIN_CODE_1>/
    │   ├── cax/
    │   │   ├── <PROCESS_1>/  // e.g., CAD, CAE, CFD
    │   │   └── <PROCESS_2>/
    │   ├── qox/
    │   │   ├── <PROCESS_1>/
    │   │   └── <PROCESS_2>/
    │   └── ata/
    │       ├── <ATA_CHAPTER_1>/
    │       └── <ATA_CHAPTER_2>/
    └── <DOMAIN_CODE_2>/
        └── ...
```

### Framework Components

*   **`domains/`**: The primary decomposition of engineering work into areas of subject matter expertise (e.g., `AAA` for Aerodynamics, `PPP` for Propulsion). This organizes all data and models by technical function.
*   **`cax/` (Computer-Aided X):** The home for all **classical** engineering artifacts. This includes models, simulations, and data from processes like CAD, CAE, CFD, CAM, and SCM.
*   **`qox/` (Quantum-Optimized X):** The quantum counterpart to `cax/`. This is where classical optimization problems are encoded into quantum-compatible formats (QUBO/BQM), solved using quantum or hybrid algorithms, and analysed.
*   **`ata/` (ATA Spec 100):** The home for all formal, certifiable documentation. Each folder corresponds to an ATA chapter (e.g., `ATA-32` for Landing Gear), providing a single source of truth for design rationale, test evidence, and compliance.

---

## QAIM-2 Integration Framework

The **Quantum AI Model for Quantum Augmented/Accelerated Industrial Management (QAIM-2)** is the core optimization framework for the ASI-T2 portfolio. It provides the methodology for translating complex classical problems into quantum computations to drive measurable sustainability and performance improvements.

**The QAIM-2 Process Flow:**

1.  **Identify Classical Problem (in `cax/`)**: An engineering challenge is identified (e.g., optimizing a wing's topology for weight and drag).
2.  **Encode with QAIM-2 (to `qox/`)**: The problem is mathematically formulated as a QUBO/BQM, mapping engineering objectives to a cost function.
3.  **Solve with Quantum/Hybrid Methods**: The QUBO is solved using quantum annealing or gate-based algorithms (QAOA, VQE).
4.  **Analyze & Integrate (back to `cax/`)**: The optimized solution is decoded, validated, and fed back into classical engineering tools (e.g., updating the CAD model).
5.  **Measure Sustainability Impact (SIM)**: The impact of the optimization is quantified against the **Sustainable Industry Model (SIM)** levers (e.g., fuel burn reduction, material waste reduction).
6.  **Document with Evidence (in `ata/`)**: The entire process, including the QS/UTCS-sealed run, is documented in the relevant ATA chapter.

This closed-loop process is applied consistently across all products to ensure that quantum optimization delivers tangible, auditable benefits.

---

## Portfolio Architecture & Cross-References

### Fields

*   [`FIELDS/transport-civil/`](../FIELDS/transport-civil/): Civil mobility and aviation.
*   [`FIELDS/cyberdefense/`](../FIELDS/cyberdefense/): Aerospace and cyber defense.
*   [`FIELDS/defense/`](../FIELDS/defense/): Ethically-constrained defense systems.
*   [`FIELDS/quantum-intelligence/`](../FIELDS/quantum-intelligence/): The foundational science of quantum systems for aerospace.
*   [`FIELDS/cross/`](../FIELDS/cross/): Cross-cutting initiatives and frameworks.

### Environments

*   [`ENVIRONMENTS/air/`](../ENVIRONMENTS/air/): Manned and unmanned airborne platforms.
*   [`ENVIRONMENTS/ground/`](../ENVIRONMENTS/ground/): Ground-based systems and infrastructure.
*   [`ENVIRONMENTS/sea/`](../ENVIRONMENTS/sea/): Maritime platforms and operations.
*   [`ENVIRONMENTS/space/`](../ENVIRONMENTS/space/): Space-based platforms and orbital operations.
*   [`ENVIRONMENTS/cross/`](../ENVIRONMENTS/cross/): Systems spanning multiple operational environments.
*   [`ENVIRONMENTS/digital/`](../ENVIRONMENTS/digital/): Abstract computational and software environments.

### Core Optimization Framework

*   [`FIELDS/cross/QAIM-2/`](../FIELDS/cross/QAIM-2/): **Quantum AI Model for Quantum Augmented/Accelerated Industrial Management** — the central optimization methodology supporting all products.

---

## Glossary & Acronyms

*   **ASI-T2**: Artificial Super Intelligence Transponders for Aerospace Sustainable Industry Transition.
*   **ATA**: Air Transport Association; refers to the standard for technical documentation in aviation.
*   **CAx**: Computer-Aided X; refers to classical engineering processes (CAD, CAE, etc.).
*   **QOx**: Quantum-Optimized X; the quantum-augmented counterpart to a CAx process.
*   **Domain**: A primary area of engineering expertise.
    *   **AAA — Aerodynamics & Airframes Architectures**
    *   **AAP — Airport Adaptable Platforms**
    *   **CCC — Cockpit, Cabin & Cargo**
    *   **CQH — Cryogenics, Quantum & H₂**
    *   **DDD — Digital & Data Defense**
    *   **EDI — Electronics & Digital Instruments**
    *   **EEE — Ecological Efficient Electrification**
    *   **EER — Environmental, Emissions & Remediation**
    *   **IIF — Industrial Infrastructure & Facilities**
    *   **IIS — Integrated Intelligence & Software**
    *   **LCC — Linkages, Control & Communications**
    *   **LIB — Logistics, Inventory & Blockchain**
    *   **MEC — Mechanical Systems Modules**
    *   **OOO — OS, Ontologies & Office Interfaces**
    *   **PPP — Propulsion & Fuel System**
*   **EE-US**: Ethics-Empathy Unmanned-Swarm.
*   **LH2**: Liquid Hydrogen.
*   **MAL-EEM**: Ethics & Empathy Module; the portfolio's safety and ethics guardrail.
*   **QAIM-2**: **Quantum AI Model for Quantum Augmented/Accelerated Industrial Management**; the framework for applying quantum and hybrid AI optimization to industrial processes.
*   **SIM**: Sustainable Industry Model; the framework for measuring sustainability impact.
*   **TFA**: Top Federation Algorithm / Threading Final Assembly; the core architectural principle.
*   **UAV**: Unmanned Aerial Vehicle.
*   **UTCS/QS**: Universal Traceability & Configuration System / Quantum Seal; the evidence standard.

---
*Part of ASI-T2 - Artificial Super Intelligence Transponders for Aerospace Sustainable Industry Transition*
