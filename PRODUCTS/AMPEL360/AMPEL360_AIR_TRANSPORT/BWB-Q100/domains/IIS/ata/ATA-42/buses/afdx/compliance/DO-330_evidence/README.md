# DO-330 Tool Qualification Evidence

This directory contains evidence for tool qualification per DO-330 "Software Tool Qualification Considerations."

## Purpose

Documents the qualification of software tools used in the development and verification of the AFDX implementation. DO-330 ensures that tools do not introduce errors or fail to detect errors in the software development process.

## Contents

| Document | Description |
|----------|-------------|
| `afdx_tool_qualification_report.md` | Complete tool qualification report for all tools used |

## Tool Categories

Tools are classified based on their potential impact:

### TQL-1 (Verification Tools)
Tools that can fail to detect errors:
- **Static Analysis Tool**: Coverity (qualified)
- **Coverage Analysis Tool**: VectorCAST (qualified)

### TQL-5 (No Qualification Required)
Tools whose output is independently verified:
- **Compiler**: GCC/Green Hills (output verified through testing)
- **Build Tool**: CMake (builds verified)
- **Version Control**: Git (configuration management)

## Qualification Activities

For each TQL-1 tool:
- ✅ Tool Operational Requirements (TOR) defined
- ✅ Tool Qualification Plan (TQP) developed
- ✅ Tool validation performed with known test cases
- ✅ Tool operational environment documented
- ✅ Lifecycle data captured

## Validation Results

### Static Analysis Tool
- Test Cases: 50 known defects
- Detection Rate: 100%
- Status: ✅ Qualified

### Coverage Analysis Tool
- Test Cases: 100 coverage scenarios
- Accuracy: 100% (verified against reference)
- Status: ✅ Qualified

## Configuration Management

All qualified tools maintained under configuration control:
- Version numbers locked
- Installation packages archived
- Configuration files under version control

## Related Standards

- **DO-330**: Software Tool Qualification Considerations
- **DO-178C**: Software Considerations (see [../DO-178C_evidence/](../DO-178C_evidence/))

## Related Files

- Parent Documentation: [../../README.md](../../README.md)
- DO-178C Evidence: [../DO-178C_evidence/](../DO-178C_evidence/)
- Verification Report: [../DO-178C_evidence/afdx_verification_report.md](../DO-178C_evidence/afdx_verification_report.md)
