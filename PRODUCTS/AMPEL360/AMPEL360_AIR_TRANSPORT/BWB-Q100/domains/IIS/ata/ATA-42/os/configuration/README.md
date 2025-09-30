# Configuration Files

This directory contains configuration files for the AQUA-OS operating system.

## Configuration Files

| File | Format | Description |
|------|--------|-------------|
| kernel_parameters.conf | Config | OS kernel parameters for DAL-A operation |
| resource_allocation.json | JSON | CPU, memory, and I/O resource allocation |
| [security_policies/](./security_policies/) | Directory | Security policy configuration files |

## Kernel Parameters

The `kernel_parameters.conf` file defines:

- Time management (8ms major frame, TAI time base)
- Scheduling (cyclic, non-preemptive)
- Memory protection (MMU, execute-never, stack guards)
- Health monitoring (watchdog, error logging)
- Security (secure boot, quantum crypto, audit logging)
- Performance settings

## Resource Allocation

The `resource_allocation.json` file specifies:

- **CPU**: 4 cores @ 1.2GHz, allocation per partition
- **Memory**: 512MB total, allocation per partition
- **I/O**: AFDX and ARINC 429 channel assignments

## Security Policies

See [security_policies/README.md](./security_policies/README.md) for:

- Access control configuration
- Data protection policies
- Multi-level security settings

## Usage

Configuration files are loaded at system initialization:

```bash
# Validate configuration
config_validate --all

# Apply configuration
config_apply
```

## Related Documents

- [Partition Configuration](../installation/partition_config.yaml)
- [Security Model](../descriptive/security_model.md)
- [Main README](../README.md)
