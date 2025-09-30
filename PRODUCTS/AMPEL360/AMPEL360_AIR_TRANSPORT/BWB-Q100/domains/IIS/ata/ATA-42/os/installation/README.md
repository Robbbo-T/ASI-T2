# Installation & Configuration

This directory contains installation and configuration documentation for the AQUA-OS operating system.

## Files

| File | Format | Description |
|------|--------|-------------|
| partition_config.yaml | YAML | ARINC 653 partition configuration |
| health_monitoring.md | Markdown | Health monitoring configuration guide |

## Partition Configuration

The `partition_config.yaml` file defines:

- **System Configuration**
  - Major frame: 8ms
  - Time base: TAI (International Atomic Time)

- **Partition Definitions** (5 partitions)
  - P-NAV: Navigation (DAL-B, 2ms window)
  - P-FBW: Fly-by-Wire (DAL-A, 2ms window)
  - P-SEC: Security Services (DAL-B, 1ms window)
  - P-DISP: Display Management (DAL-C, 2ms window)
  - P-MAINT: Maintenance (DAL-D, 1ms window)

- **Resource Allocation**
  - CPU percentage per partition
  - Memory regions (code, data, stack)
  - Communication ports (sampling, queuing)

- **Health Monitoring Rules**
  - Error detection and response actions
  - Partition-level and system-level error handling

## Health Monitoring

The `health_monitoring.md` document provides:

- Health monitoring architecture
- Error classification (partition and system errors)
- Recovery actions (restart, halt, switch redundant)
- Configuration details
- Testing procedures

## Usage

```bash
# Validate partition configuration
config_validate partition_config.yaml

# Apply partition configuration
config_apply partition_config.yaml
```

## Related Documents

- [Configuration](../configuration/)
- [Test Results](../testing/test_results/)
- [Main README](../README.md)
