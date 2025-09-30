# AFDX Test Results

This directory contains test reports documenting the verification and validation of the AFDX implementation.

## Purpose

Provides comprehensive test results demonstrating that the AFDX implementation meets all requirements per ARINC 664 Part 7. Test reports are in Markdown format for easy review and traceability.

## Contents

| Test Report | Test Date | Description | Status |
|-------------|-----------|-------------|--------|
| `tr_bandwidth_test_20240515.md` | 2024-05-15 | Bandwidth and jitter testing | ✅ All Pass |
| `tr_frame_integrity_20240520.md` | 2024-05-20 | Frame integrity and CRC validation | ✅ All Pass |
| `tr_redundancy_20240525.md` | 2024-05-25 | Dual-active redundancy and failover | ✅ All Pass |
| `tr_error_handling_20240530.md` | 2024-05-30 | Error detection and recovery | ✅ All Pass |

## Test Summary

### Bandwidth and Jitter Test
- **Virtual Links Tested**: 6 (VL-1001 through VL-1006)
- **Result**: All VLs within specification
- **Total Utilization**: 8.14 Mbps (9.1% of capacity)
- **Average Jitter**: 197 µs (well within limits)
- **Frame Loss**: 0%

### Frame Integrity Test
- **Duration**: 24 hours
- **Frames Transmitted**: 43,200,000
- **CRC Errors**: 0
- **Sequence Errors**: 0
- **Result**: 100% frame integrity maintained

### Redundancy Test
- **Test Scenarios**: Branch A failure, Branch B failure, dual-active operation
- **Failover Time**: 95ms (Branch A), 92ms (Branch B)
- **Frame Loss**: 0.05% (Branch A), 0.04% (Branch B)
- **Requirement**: < 100ms failover, < 0.1% frame loss
- **Result**: ✅ All requirements met

### Error Handling Test
- **Scenarios Tested**: Link failures, traffic overflow, switch failures, end system errors
- **Error Detection Rate**: 100%
- **Automatic Recovery**: < 100ms (all scenarios)
- **Alarm Generation**: 100% success rate
- **Result**: ✅ All error handling mechanisms working correctly

## Test Environment

- **Hardware**: BWB-Q100 AFDX Test Network v1.0
- **Switches**: 4x AFDX switches (dual-redundant configuration)
- **Test Equipment**:
  - AFDX Analyzer: AIM AC-664
  - Traffic Generator: Spirent TestCenter
  - Network Analyzer: Wireshark with AFDX plugin

## Compliance Evidence

Test results support compliance with:
- **ARINC 664 Part 7**: Full compliance demonstrated
- **DO-178C**: Verification objectives satisfied
- See [../compliance/](../compliance/) for complete evidence

## Related Files

- Parent Documentation: [../../README.md](../../README.md)
- Test Cases: [../test_cases/](../test_cases/)
- Compliance Evidence: [../../compliance/](../../compliance/)
- Configuration: [../../configuration/](../../configuration/)
