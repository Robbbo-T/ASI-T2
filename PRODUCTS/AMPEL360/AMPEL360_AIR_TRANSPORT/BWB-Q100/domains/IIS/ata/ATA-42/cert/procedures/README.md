# Certification Procedures

This directory contains detailed certification procedures for all applicable standards.

## Purpose

Provides step-by-step procedures for:
- Software certification (DO-178C)
- Hardware certification (DO-254)
- IMA certification (DO-297)
- Tool qualification (DO-330)
- System development (ARP4754B)
- Safety assessment (ARP4761A)
- Security certification (DO-326A/356A/355)
- Evidence collection and management

## Available Procedures

| Procedure File | Standard | Scope |
|----------------|----------|-------|
| `do178c_procedures.yaml` | DO-178C | Software certification covering all 9 objectives |
| `do254_procedures.yaml` | DO-254 | Hardware development lifecycle |
| `do297_procedures.yaml` | DO-297 | IMA-specific certification procedures |
| `do330_procedures.yaml` | DO-330 | Tool qualification procedures |
| `arp4754b_procedures.yaml` | ARP4754B | System development procedures |
| `arp4761a_procedures.yaml` | ARP4761A | Safety assessment procedures (FHA/PSSA/SSA) |
| `airworthiness_security.yaml` | DO-326A/356A/355 | Complete security lifecycle procedures |
| `evidence_collection.yaml` | Multiple | Evidence collection and management procedures |

## Procedure Structure

Each procedure file contains:
- **Procedure name**: Clear identification
- **Description**: Purpose and scope
- **Steps**: Sequential actions to perform
- **Deliverables**: Expected outputs
- **Evidence location**: Where results are stored

## Usage

Procedures are referenced during:
- Certification planning
- Development activities
- Verification and validation
- Evidence collection
- Authority audits

## Validation

Procedures can be validated using:
```bash
make validate-plans
```

## See Also

- [Plans](../plans/README.md) - Certification plans
- [Evidence](../evidence/README.md) - Evidence generated per procedures
- [Standards References](../references/README.md) - Standard requirements
