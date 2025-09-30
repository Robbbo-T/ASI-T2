# AFDX Configuration Files

This directory contains machine-parseable configuration files for the AFDX network implementation.

## Purpose

Provides YAML and JSON configuration files with proper AFDX semantics and machine-parseable units. All configuration files use separate number and unit fields (e.g., `bag_ms: 2` instead of "2ms") to enable automated validation and processing.

## Contents

| File | Format | Description |
|------|--------|-------------|
| `virtual_links.schema.json` | JSON Schema | Schema for Virtual Links validation |
| `virtual_links.yaml` | YAML | Virtual Links definitions (6 VLs) |
| `switch_configuration.json` | JSON | Switch configuration (4 switches) |
| `bandwidth_allocation.yaml` | YAML | Bandwidth allocation groups |
| `vl_scheduling.yaml` | YAML | VL scheduling parameters |
| `redundancy_config.yaml` | YAML | Dual-active redundancy configuration |
| `gateway_config.yaml` | YAML | Domain segregation gateway |

## Virtual Links Summary

| VL ID | Name | BAG | Priority | Redundancy |
|-------|------|-----|----------|------------|
| 1001 | Flight_Control_Data | 2ms | 7 | A+B |
| 1002 | Navigation_Data | 20ms | 6 | A+B |
| 1003 | Air_Data | 10ms | 7 | A+B |
| 1004 | Engine_Parameters | 50ms | 5 | A+B |
| 1005 | System_Status | 100ms | 3 | A |
| 1006 | Maintenance_Data | 1000ms | 2 | A |

## Network Utilization

- **Total Capacity**: 100 Mbps per network
- **Reserved**: 10 Mbps for management
- **Available**: 90 Mbps
- **Current Usage**: 8.14 Mbps (9.1%)
- **Headroom**: 81.86 Mbps (90.9%)

## Validation

All configuration files can be validated using:
```bash
make validate-config
```

This validates:
- JSON syntax and schema compliance
- YAML syntax
- BAG values (must be in {1,2,4,8,16,32,64,128} ms)
- Frame sizes (64-1518 bytes)
- Bandwidth utilization (< 100%)

## Key Features

### Machine-Parseable Units
All timing and size values use separate fields:
- `bag_ms: 2` (not "2ms")
- `jitter_us: 50` (not "50µs")
- `max_frame_size_bytes: 1518` (not "1518 bytes")

### AFDX Semantics
- Dual-active redundancy (A+B) for critical VLs
- BAG values from ARINC 664 standard set
- Priority-based QoS (0-7)
- Domain segregation via gateway

## Related Files

- Parent Documentation: [../README.md](../README.md)
- Architecture Spec: [../descriptive/architecture_spec.md](../descriptive/architecture_spec.md)
- Test Results: [../testing/test_results/](../testing/test_results/)
