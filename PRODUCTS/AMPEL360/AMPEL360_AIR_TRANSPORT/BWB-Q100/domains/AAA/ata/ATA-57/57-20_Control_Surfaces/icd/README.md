# Interface Control Documents (ICDs)

This directory contains Interface Control Documents defining interfaces between ATA-57-20 Control Surfaces and other systems/chapters.

## Purpose

ICDs provide:
- Clear interface definitions and boundaries
- Mechanical and functional requirements
- Validation and acceptance criteria
- Cross-system coordination
- Change management procedures

## ICD Documents

### ICD-57-20-27_Flight_Control_System.md
Interface with ATA-27 Flight Controls:
- **Scope**: Kinematics, hinge moments, actuator interfaces
- **Key Topics**:
  - Angular range of motion and deflection limits
  - Hinge moment sign conventions
  - Actuator attachment points and forces
  - Position accuracy requirements
  - Clearance envelopes

### ICD-57-20-29_Hydraulic_System.md
Interface with ATA-29 Hydraulic Systems:
- **Scope**: Hydraulic actuator interfaces
- **Key Topics**:
  - Actuator specifications (pressure, flow)
  - Mounting provisions and load paths
  - Cleanliness requirements (ISO 4406)
  - Seal specifications
  - Installation and preload requirements

### ICD-57-20-57-10_Wing_Structure.md
Interface with ATA-57-10 Wing Primary Structure:
- **Scope**: Hinge attachments, load transfer
- **Key Topics**:
  - Hinge attachment locations and tolerances
  - Fastener specifications and patterns
  - Load transfer mechanisms
  - Bonding and sealing requirements
  - Corrosion protection

### ICD-57-20-57-30_High_Lift.md
Interface with ATA-57-30 High-Lift Devices:
- **Scope**: Gap management, seal interfaces
- **Key Topics**:
  - Gap dimensions and variations
  - Seal specifications and attachment
  - Motion envelope clearances
  - Combined deflection constraints
  - Maintenance access

## ICD Structure

Each ICD includes:
1. **Interface Scope**: Systems covered and boundaries
2. **Mechanical Interfaces**: Physical interfaces and requirements
3. **Functional Requirements**: Performance and operational requirements
4. **Validation & Acceptance**: Test and acceptance criteria
5. **References**: Related documents and specifications

## Change Management

ICD changes require:
- Review by both systems/chapters
- Impact assessment
- Configuration control approval
- Update of affected specifications
- Notification to stakeholders

## Bidirectional References

ICDs are cross-referenced:
- ATA-57-10 references ICD-57-10-57-20
- ATA-27 references ICD-27-57-20
- Ensures consistency across systems

## Related Directories

- **../contracts/** - JSON schemas and contracts
- **../S1000D/DMC/** - Technical data modules
- **../compliance/** - Interface verification evidence

---
*Part of ATA-57-20 Control Surfaces interface framework.*
