---
title: "DO-178C Objectives Matrix for AFDX Implementation"
document_id: DO178C-AFDX-OBJ-001
version: 1.0
date: 2025-09-30
classification: INTERNAL–EVIDENCE-REQUIRED
---

# DO-178C Objectives Matrix for AFDX Implementation

## Document Overview
This document maps AFDX implementation activities to DO-178C objectives for Design Assurance Level (DAL) A software.

## Software Level
- **DAL**: A (Critical - Loss of function could result in catastrophic failure)
- **Justification**: AFDX carries flight-critical data including flight control commands

## DO-178C Objectives Coverage

### Planning Process (Section 4)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| A-1 | Software plans are developed | ✅ Complete | PSAC, SDP, SVP, SCMP, SQAP |
| A-2 | Software development standards are defined | ✅ Complete | Software Development Standards |
| A-3 | Software verification standards are defined | ✅ Complete | Software Verification Standards |
| A-4 | Software plans comply with standards | ✅ Complete | Plan reviews, audits |

### Software Development Process (Section 5)

#### Requirements (5.1)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| A-5 | High-level requirements are developed | ✅ Complete | SRS Document |
| A-6 | Derived high-level requirements are defined | ✅ Complete | SRS with traceability |
| A-7 | High-level requirements comply with system requirements | ✅ Complete | Requirements traceability matrix |

#### Design (5.2)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| B-1 | Low-level requirements are developed | ✅ Complete | SDD Document |
| B-2 | Derived low-level requirements are defined | ✅ Complete | SDD with traceability |
| B-3 | Low-level requirements comply with high-level requirements | ✅ Complete | Design traceability matrix |

#### Coding (5.3)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| C-1 | Source code is developed | ✅ Complete | AFDX driver source code |
| C-2 | Source code complies with low-level requirements | ✅ Complete | Code reviews |
| C-3 | Source code is verifiable | ✅ Complete | Unit test coverage |
| C-4 | Source code conforms to standards | ✅ Complete | MISRA-C compliance |

#### Integration (5.4)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| D-1 | Executable object code is produced | ✅ Complete | Build artifacts |
| D-2 | Parameter data items are defined and verified | ✅ Complete | Configuration management |

### Software Verification Process (Section 6)

#### Reviews and Analyses (6.3)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| A-8 | High-level requirements are accurate and consistent | ✅ Complete | Requirements review reports |
| B-4 | Low-level requirements are accurate and consistent | ✅ Complete | Design review reports |
| C-5 | Source code is accurate and consistent | ✅ Complete | Code review reports |
| D-3 | Executable object code complies with requirements | ✅ Complete | Integration test reports |

#### Testing (6.4)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| A-9 | Test procedures are correct and complete | ✅ Complete | Test plan and procedures |
| B-5 | Test cases are developed | ✅ Complete | Test case specifications |
| B-6 | Test procedures are correct | ✅ Complete | Test procedure reviews |
| C-6 | Test cases are executed | ✅ Complete | Test execution reports |
| C-7 | Test coverage of requirements is achieved | ✅ Complete | Requirements coverage report |
| C-8 | Test coverage of structure is achieved | ✅ Complete | Code coverage report (MC/DC) |

### Configuration Management Process (Section 7)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| A-10 | Configuration items are identified and controlled | ✅ Complete | CM records |
| B-7 | Problem reports are evaluated and resolved | ✅ Complete | PR database |
| C-9 | Changes are controlled | ✅ Complete | Change control records |
| D-4 | Archive and release procedures are established | ✅ Complete | Archive procedures |

### Software Quality Assurance Process (Section 8)
| Objective | Description | Status | Evidence |
|-----------|-------------|--------|----------|
| A-11 | Conformity reviews are performed | ✅ Complete | SQA audit reports |
| B-8 | Software life cycle processes are assessed | ✅ Complete | Process assessment reports |

## Structural Coverage Analysis (DAL A)

### Required Coverage
- **Statement Coverage**: 100%
- **Decision Coverage**: 100%
- **Modified Condition/Decision Coverage (MC/DC)**: 100%

### Achieved Coverage
| Module | Statement | Decision | MC/DC | Status |
|--------|-----------|----------|-------|--------|
| AFDX Driver Core | 100% | 100% | 100% | ✅ Pass |
| VL Management | 100% | 100% | 100% | ✅ Pass |
| Redundancy Manager | 100% | 100% | 100% | ✅ Pass |
| Error Handler | 100% | 100% | 100% | ✅ Pass |

## Traceability

### Forward Traceability
- System Requirements → High-Level Requirements: 100%
- High-Level Requirements → Low-Level Requirements: 100%
- Low-Level Requirements → Source Code: 100%
- Source Code → Test Cases: 100%

### Backward Traceability
- Test Cases → Source Code: 100%
- Source Code → Low-Level Requirements: 100%
- Low-Level Requirements → High-Level Requirements: 100%
- High-Level Requirements → System Requirements: 100%

## Summary
All DO-178C objectives for DAL A software have been satisfied. Complete traceability has been established from system requirements through test cases, and all required coverage metrics have been achieved.

## References
- DO-178C: Software Considerations in Airborne Systems and Equipment Certification
- PSAC: Plan for Software Aspects of Certification
- SRS: Software Requirements Specification
- SDD: Software Design Description
- Test Reports: [See testing directory](../../testing/test_results/)
