---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-QAFBW-DO297
llc: SYSTEMS
maintainer: OOO (OS), LCC (Control Laws), EDI (Avionics/Net), IIS (Software), MEC
  (Actuation)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
release_date: 2024-09-23
utcs_mi: 'scope: DO-297_IMA_responsibilities

  stakeholders: platform_supplier, application_supplier, system_integrator

  lifecycle_coverage: full

  '
version: 1.0
---

# QAFbW DO-297 Roles & Responsibilities (RACI Matrix)

## Overview

This document defines the roles and responsibilities for the QAFbW Control Stack component following DO-297 Integrated Modular Avionics (IMA) guidelines. The RACI matrix clarifies accountability across Platform Supplier (AQUA OS), Application Supplier (QAFbW Team), and System Integrator (BWB-Q100 Team).

**RACI Legend:**
- **R**esponsible: Performs the work
- **A**ccountable: Ultimately answerable for completion
- **C**onsulted: Input sought before decisions/actions
- **I**nformed: Kept informed of progress/decisions

## RACI Matrix

| Responsibility | Platform Supplier (AQUA OS Team) | Application Supplier (QAFbW Team) | System Integrator (BWB-Q100 Team) |
| :--- | :--- | :--- | :--- |
| **Provide ARINC-653 Runtime Environment** | **Accountable** | Informed | Informed |
| **Develop Core OS Services (Time/Sync/Network)** | **Responsible** | Consulted | Informed |
| **Provide Partition Schedule Management** | **Responsible** | Consulted | Consulted |
| **Implement Security Framework (KMS/Boot)** | **Responsible** | Consulted | Informed |
| **Develop QAFbW Application Software** | Informed | **Responsible** | Consulted |
| **Define QAFbW Requirements (SRD)** | Consulted | **Responsible** | Consulted |
| **Implement Flight Control Laws** | - | **Responsible** | Consulted |
| **Provide Component Interface Spec (ICD)** | Consulted | **Responsible** | Consulted |
| **Perform Component Unit Testing** | - | **Responsible** | Informed |
| **Provide Component Conformance Evidence**| - | **Responsible** | - |
| **Integrate App onto Platform** | Consulted | Consulted | **Responsible** |
| **Define Product-Specific Bindings (ICDs)**| - | Consulted | **Responsible** |
| **Perform HIL/Iron Bird Integration Tests**| Consulted | Consulted | **Responsible** |
| **Overall Aircraft Safety Case** | Informed | Informed | **Accountable** |
| **Obtain Aircraft-Level Certification** | - | - | **Accountable** |
| **Partition Schedule Authority (PSSC)** | Consulted | Responsible | **Accountable** |
| **Network VL Admission Control** | **Responsible** | Consulted | Accountable |
| **Key Management (KMS/QKD ingest)** | **Responsible** | Informed | Consulted |
| **Secure Boot / Attestation Policy** | **Responsible** | Consulted | Informed |
| **Configuration Management (CM/CCB)** | Responsible | Responsible | **Accountable** |
| **Problem Reporting & CARs** | Responsible | Responsible | **Accountable** |
| **Assurance Case (GSn/ARG)** | Informed | Responsible | **Accountable** |
| **Evidence Sealing (UTCS/QS)** | Responsible | Responsible | **Accountable** |

## Interface Management

### Technical Interfaces
- **OS-to-App Interface**: Platform Supplier defines APIs; Application Supplier implements against them
- **App-to-Product Interface**: Application Supplier defines generic interface; System Integrator binds to specific product
- **Cross-Partition Interface**: All parties coordinate through System Integrator as integrator

### Process Interfaces
- **Requirements Flow**: System Integrator → Application Supplier → Platform Supplier
- **Evidence Flow**: Platform/Application Suppliers → System Integrator → Certification Authority
- **Change Control**: System Integrator maintains overall CCB with supplier participation

## Verification Responsibilities

### Platform Verification (AQUA OS Team)
- OS service conformance testing
- Partition isolation validation
- Resource management verification
- Security framework validation

### Application Verification (QAFbW Team)
- Functional requirements testing
- Component-level safety analysis
- Performance characterization
- Interface conformance testing

### Integration Verification (BWB-Q100 Team)
- System-level integration testing
- Aircraft-specific validation
- Certification evidence coordination
- Final airworthiness demonstration

## Risk & Issue Management

### Risk Ownership
- **Platform Risks**: AQUA OS Team accountable for OS-related risks
- **Application Risks**: QAFbW Team accountable for component-related risks  
- **Integration Risks**: BWB-Q100 Team accountable for system-level risks

### Issue Resolution
- **Technical Issues**: Resolved at appropriate supplier level with System Integrator coordination
- **Schedule Issues**: System Integrator manages overall schedule impact
- **Certification Issues**: System Integrator leads resolution with supplier support

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*