---
title: "ARINC 653 Standard Summary"
standard: ARINC 653
version: Part 1-5
issue_date: 2021-06
maintainer: IIS Team
---

# ARINC 653 Standard Summary

## Overview
ARINC 653 defines the Avionics Application Software Standard Interface, which specifies the requirements for partitioning and communication in Integrated Modular Avionics (IMA) systems.

## Key Concepts

### 1. Partitioning
- **Time Partitioning**: Fixed schedule for CPU allocation
- **Space Partitioning**: Protected memory areas for each partition
- **Health Monitoring**: Fault detection and recovery mechanisms

### 2. Communication
- **Sampling Ports**: Unbuffered, latest-value communication
- **Queuing Ports**: Buffered, FIFO communication
- **Virtual Channels**: Logical communication paths

### 3. Core Services
- Process management
- Time management
- I/O management
- Error handling

## Compliance Requirements for BWB-Q100

1. **Partition Schedule**: Must guarantee deterministic execution
2. **Memory Protection**: No inter-partition memory access
3. **Health Monitoring**: Must detect and handle faults within 50ms
4. **Communication**: Must support AFDX and ARINC 429

## Implementation Notes

- Our AQUA-OS implementation follows ARINC 653 Part 1
- Extensions for quantum-ready security are documented in ATA-42-20
- Partition configuration is managed via `partition_config.yaml`

## ARINC 653 API

### Partition Management
```c
GET_PARTITION_STATUS()
SET_PARTITION_MODE()
```

### Process Management
```c
CREATE_PROCESS()
START()
STOP()
SUSPEND()
RESUME()
```

### Time Management
```c
PERIODIC_WAIT()
GET_TIME()
TIMED_WAIT()
```

### Communication
```c
// Sampling ports
CREATE_SAMPLING_PORT()
WRITE_SAMPLING_MESSAGE()
READ_SAMPLING_MESSAGE()

// Queuing ports
CREATE_QUEUING_PORT()
SEND_QUEUING_MESSAGE()
RECEIVE_QUEUING_MESSAGE()
```

### Health Monitoring
```c
REPORT_APPLICATION_MESSAGE()
CREATE_ERROR_HANDLER()
RAISE_APPLICATION_ERROR()
```

## Partition States

```
┌─────────┐
│  IDLE   │ ── START → ┌────────┐
└─────────┘            │ NORMAL │
                       └────────┘
                            │
            HALT ←──────────┼───────→ ERROR
                            │
                       ┌─────────┐
                       │ RESTART │
                       └─────────┘
```

## Scheduling Example

```yaml
# 8ms major frame
major_frame: 8000000  # nanoseconds

partitions:
  - id: P-NAV
    window: 2000000    # 2ms
    offset: 0
  - id: P-FBW
    window: 2000000    # 2ms
    offset: 2000000
  - id: P-DISP
    window: 2000000    # 2ms
    offset: 4000000
  - id: P-MAINT
    window: 2000000    # 2ms
    offset: 6000000
```

## Health Monitoring Example

```c
// Error handler
void error_handler(ERROR_CODE error, MESSAGE_ADDR_TYPE msg_addr, ERROR_MESSAGE_SIZE_TYPE length) {
    switch(error) {
        case DEADLINE_MISSED:
            // Log and continue
            log_error(error, msg_addr);
            break;
        case APPLICATION_ERROR:
            // Restart partition
            RESTART_PARTITION();
            break;
        case MEMORY_VIOLATION:
            // Halt partition
            HALT_PARTITION();
            break;
    }
}
```

## References

- [Official ARINC 653 Standard](https://www.arinc.com/cf/store/catalog.cfm?prod_group_id=1) (PDF)
- [ARINC 653 Training Materials](https://www.arinc.com/cf/store/catalog.cfm?prod_group_id=2)
- [Implementation Guide](../S1000D/publications/PUB-A42-OS-DES-00000-00.md)

## Related Documents

- [Architecture Specification](../descriptive/architecture_spec.md)
- [Partition Configuration](../installation/partition_config.yaml)
- [Health Monitoring](../installation/health_monitoring.md)
