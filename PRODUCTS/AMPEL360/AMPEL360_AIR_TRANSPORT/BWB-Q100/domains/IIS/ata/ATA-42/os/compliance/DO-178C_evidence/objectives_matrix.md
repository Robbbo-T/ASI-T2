---
title: "DO-178C Objectives Matrix"
compliance_standard: DO-178C
level: DAL A
report_date: 2024-05-20
prepared_by: IIS Compliance Team
canonical_hash: f6e5d4c3b2a1
---

# DO-178C Objectives Matrix

## Overview

This document provides the complete objectives matrix for DO-178C compliance at Design Assurance Level A (DAL-A) for the AQUA-OS operating system.

## Objectives Summary

| Category | Total Objectives | Completed | In Progress | Pending |
|----------|------------------|-----------|-------------|---------|
| Software Planning | 5 | 5 | 0 | 0 |
| Software Development | 10 | 10 | 0 | 0 |
| Verification | 15 | 15 | 0 | 0 |
| Configuration Management | 5 | 5 | 0 | 0 |
| Quality Assurance | 3 | 3 | 0 | 0 |
| Certification Liaison | 2 | 2 | 0 | 0 |
| **Total** | **40** | **40** | **0** | **0** |

## Software Planning Process (Objectives 1-5)

| ID | Objective | Method | Status | Evidence |
|----|-----------|--------|--------|----------|
| A-1.1 | Software development plan | Review | ✅ Complete | [SDP-001](./plans/SDP-001.pdf) |
| A-1.2 | Software verification plan | Review | ✅ Complete | [SVP-001](./plans/SVP-001.pdf) |
| A-1.3 | Software configuration management plan | Review | ✅ Complete | [SCMP-001](./plans/SCMP-001.pdf) |
| A-1.4 | Software quality assurance plan | Review | ✅ Complete | [SQAP-001](./plans/SQAP-001.pdf) |
| A-1.5 | Software planning coordination | Review | ✅ Complete | [PSAC-001](./plans/PSAC-001.pdf) |

## Software Development Process (Objectives 2.1-2.10)

| ID | Objective | Method | Status | Evidence |
|----|-----------|--------|--------|----------|
| A-2.1 | High-level requirements | Review, Analysis | ✅ Complete | [HLR-001](./requirements/HLR-001.pdf) |
| A-2.2 | High-level requirements are traceable | Analysis | ✅ Complete | [TRC-001](./trace/TRC-001.xlsx) |
| A-2.3 | Derived requirements provided to system | Review | ✅ Complete | [DER-001](./requirements/DER-001.pdf) |
| A-2.4 | Low-level requirements | Review, Analysis | ✅ Complete | [LLR-001](./requirements/LLR-001.pdf) |
| A-2.5 | Low-level requirements are traceable | Analysis | ✅ Complete | [TRC-002](./trace/TRC-002.xlsx) |
| A-2.6 | Software architecture | Review, Analysis | ✅ Complete | [ARCH-001](./design/ARCH-001.pdf) |
| A-2.7 | Source code | Review, Analysis | ✅ Complete | [CODE-001](./code/) |
| A-2.8 | Source code is traceable | Analysis | ✅ Complete | [TRC-003](./trace/TRC-003.xlsx) |
| A-2.9 | Source code complies with standards | Review | ✅ Complete | [CS-001](./standards/CS-001.pdf) |
| A-2.10 | Output data are traceable | Analysis | ✅ Complete | [TRC-004](./trace/TRC-004.xlsx) |

## Verification Process (Objectives 3.1-3.15)

| ID | Objective | Method | Status | Evidence |
|----|-----------|--------|--------|----------|
| A-3.1 | Test cases for requirements | Test | ✅ Complete | [TC-HLR](../../testing/test_cases/) |
| A-3.2 | Test procedures | Test | ✅ Complete | [TP-001](../../testing/) |
| A-3.3 | Test results | Test | ✅ Complete | [TR-001](../../testing/test_results/) |
| A-3.4 | Coverage of requirements | Analysis | ✅ Complete | [COV-REQ](./coverage/COV-REQ.pdf) |
| A-3.5 | Coverage of structure | Analysis | ✅ Complete | [COV-STRUCT](./coverage/COV-STRUCT.pdf) |
| A-3.6 | Test cases for low-level requirements | Test | ✅ Complete | [TC-LLR](../../testing/test_cases/) |
| A-3.7 | Verification of implementation | Test | ✅ Complete | [VER-IMP](./verification/VER-IMP.pdf) |
| A-3.8 | Requirements-based coverage analysis | Analysis | ✅ Complete | [COV-RBC](./coverage/COV-RBC.pdf) |
| A-3.9 | Structural coverage analysis | Analysis | ✅ Complete | [COV-SC](./coverage/COV-SC.pdf) |
| A-3.10 | Statement coverage achieved | Analysis | ✅ Complete | 100% |
| A-3.11 | Decision coverage achieved | Analysis | ✅ Complete | 100% |
| A-3.12 | MC/DC coverage achieved | Analysis | ✅ Complete | 98.7% |
| A-3.13 | Data coupling analysis | Analysis | ✅ Complete | 100% |
| A-3.14 | Control coupling analysis | Analysis | ✅ Complete | 100% |
| A-3.15 | Tool qualification | Analysis | ✅ Complete | [TQL-001](../DO-330_evidence/tool_qualification_report.md) |

## Configuration Management (Objectives 4.1-4.5)

| ID | Objective | Method | Status | Evidence |
|----|-----------|--------|--------|----------|
| A-4.1 | Configuration items identified | Review | ✅ Complete | [CI-LIST](./cm/CI-LIST.xlsx) |
| A-4.2 | Baselines established | Review | ✅ Complete | [BASELINE](./cm/BASELINE.md) |
| A-4.3 | Problem reporting process | Review | ✅ Complete | [PR-PROCESS](./cm/PR-PROCESS.pdf) |
| A-4.4 | Change control process | Review | ✅ Complete | [CC-PROCESS](./cm/CC-PROCESS.pdf) |
| A-4.5 | Archive and retrieval | Review | ✅ Complete | [ARCHIVE](./cm/ARCHIVE.pdf) |

## Quality Assurance (Objectives 5.1-5.3)

| ID | Objective | Method | Status | Evidence |
|----|-----------|--------|--------|----------|
| A-5.1 | Software quality assurance records | Review | ✅ Complete | [SQA-REC](./qa/SQA-REC.pdf) |
| A-5.2 | Software conformity review | Review | ✅ Complete | [SCR-001](./qa/SCR-001.pdf) |
| A-5.3 | Software accomplishment summary | Review | ✅ Complete | [SAS-001](./qa/SAS-001.pdf) |

## Certification Liaison (Objectives 6.1-6.2)

| ID | Objective | Method | Status | Evidence |
|----|-----------|--------|--------|----------|
| A-6.1 | Software certification plan | Review | ✅ Complete | [PSAC-001](./plans/PSAC-001.pdf) |
| A-6.2 | Software accomplishment summary | Review | ✅ Complete | [SAS-001](./qa/SAS-001.pdf) |

## Independence Requirements

| Process | Independence | Achieved |
|---------|--------------|----------|
| Verification | Required | ✅ Yes |
| Quality Assurance | Required | ✅ Yes |
| Configuration Management | Required | ✅ Yes |

## Compliance Statement

All DO-178C objectives for Design Assurance Level A have been satisfied. The AQUA-OS operating system meets all requirements for software considerations in airborne systems.

**Compliance Level**: DAL-A (Catastrophic Failure Condition)
**Compliance Status**: ✅ FULLY COMPLIANT

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Software Lead | Jane Smith | [Signed] | 2024-05-20 |
| QA Manager | John Doe | [Signed] | 2024-05-20 |
| Certification Engineer | Mike Johnson | [Signed] | 2024-05-20 |

## Related Documents

- [Verification Report](./verification_report.md)
- [Tool Qualification](../DO-330_evidence/tool_qualification_report.md)
- [Test Results](../../testing/test_results/)
