---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-MXDIAG-COMP-README
llc: SYSTEMS
maintainer: OOO (OS), IIS (Integration)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
release_date: 2024-09-26
utcs_mi: 'component: MX_DIAG Maintenance & Diagnostics

  certification_level: DO-178C DAL-B

  quantum_boundary: out-of-loop-assistive-only

  '
version: 1.0
---

# MX_DIAG Maintenance & Diagnostics Component

Maintenance & Diagnostics service providing system health monitoring and fault reporting.

## Component Overview

**Purpose**: Maintenance & Diagnostics service providing system health monitoring and fault reporting.

**Certification Level**: DO-178C DAL-B (Design Assurance Level B)

**Architecture**: ARINC-653 partitioned application running on AQUA OS kernel services

## Document Structure

### Core Specifications
- **[Component Specification](./MX_DIAG_Component_Spec.md)**: Complete technical specification
- **[System Requirements (SRD)](./MX_DIAG_SRD.md)**: MoSCoW requirements matrix
- **[Interface Control Document (ICD)](./MX_DIAG_ICD.yaml)**: Message formats and protocols (if available)
- **[Partition & Schedule Spec (PSSC)](./MX_DIAG_PSSC.json)**: Resource allocation and scheduling (if available)

### Verification & Validation
- **[Verification Matrix (VCRM)](./MX_DIAG_VCRM.csv)**: Requirements traceability matrix (if available)
- **[Test Plan](./MX_DIAG_Test_Plan.md)**: Comprehensive test strategy and procedures

## Integration Points

### AQUA OS Platform Integration
The MX_DIAG component integrates with the AQUA OS platform through:
- **OOO Domain**: Operating system services and partition management
- **IIS Domain**: Software integration and verification framework
- **EDI Domain**: Avionics and network integration (where applicable)

### Cross-Component Dependencies
- Integration with other AQUA OS components through standardized ARINC-653 interfaces
- Participation in platform-wide health monitoring and fault management
- Compliance with AQUA OS timing and resource allocation policies

## Verification Strategy

### Test Requirements
- Requirements traceability through VCRM matrix
- Unit testing with appropriate coverage for DAL-B certification
- Integration testing with AQUA OS platform services
- System-level validation in target aircraft environment

### Evidence Requirements
- All test artifacts sealed via UTCS/QS evidence service
- Configuration management through formal change control
- Compliance verification for DO-178C DAL-B requirements

## Development Status

**Current Status**: SPECIFICATION COMPLETE

**Next Steps**:
1. Stakeholder review and baseline approval
2. Detailed design and implementation  
3. Unit testing and component verification
4. Integration testing with AQUA OS platform
5. System-level validation and certification evidence

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*
