---
title: "Architecture Specification"
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
date: 2024-09-30
---

# Architecture Specification

## Microkernel Design

The AQUA-OS implements a microkernel architecture with minimal functionality in the kernel:

- Process/partition management
- Memory management
- Inter-process communication
- Low-level I/O
- Scheduling

All other functionality is implemented in user-space services.

## Separation Kernel

The separation kernel enforces:

1. **Spatial Separation**: Memory protection between partitions
2. **Temporal Separation**: Time-sliced CPU allocation
3. **Information Flow Control**: Regulated inter-partition communication
4. **Fault Containment**: Partition failures isolated

## Memory Architecture

### Address Space Layout

Each partition has a dedicated address space:

```
0xFFFFFFFF  ┌─────────────────┐
            │  Kernel Space   │  (accessible in supervisor mode only)
0xC0000000  ├─────────────────┤
            │  I/O Devices    │  (memory-mapped I/O)
0x80000000  ├─────────────────┤
            │  Partition Code │  (read-only, executable)
0x40000000  ├─────────────────┤
            │  Partition Data │  (read-write, non-executable)
0x20000000  ├─────────────────┤
            │  Partition Stack│  (read-write, non-executable, grows down)
0x10000000  ├─────────────────┤
            │  Partition Heap │  (read-write, non-executable, grows up)
0x00000000  └─────────────────┘
```

### Memory Protection

- **MMU-based Protection**: Hardware-enforced page-level protection
- **Execute-Never (XN)**: Data pages cannot be executed
- **Write-Never (WN)**: Code pages cannot be modified
- **Guard Pages**: Detect stack overflow

## Scheduling Architecture

### Cyclic Scheduling

```
Major Frame (8ms)
┌──────┬──────┬─────┬──────┬──────┐
│P-NAV │P-FBW │P-SEC│P-DISP│P-MAINT│
│ 2ms  │ 2ms  │ 1ms │ 2ms  │ 1ms  │
└──────┴──────┴─────┴──────┴──────┘
   ↑                              ↑
   └──────── repeats ─────────────┘
```

### Scheduler Properties

- **Fixed Priority**: Partitions execute in configured order
- **Non-Preemptive**: Partitions execute to completion of window
- **Deterministic**: Exact execution timing guaranteed
- **Low Overhead**: < 1μs context switch overhead

## Communication Architecture

### Sampling Ports

```
Partition A                Partition B
┌─────────┐               ┌─────────┐
│  Write  │──────────────▶│  Read   │
│  Port   │  Latest Value │  Port   │
└─────────┘               └─────────┘
```

- Non-blocking read/write
- Latest value semantics
- No message queueing

### Queuing Ports

```
Partition A                Partition B
┌─────────┐               ┌─────────┐
│  Send   │──────────────▶│ Receive │
│  Port   │  FIFO Queue   │  Port   │
└─────────┘               └─────────┘
```

- FIFO message queue
- Configurable depth
- Blocking/non-blocking options

## I/O Architecture

### Device Drivers

All device drivers run in kernel space:

- AFDX network interface
- ARINC 429 interface
- Serial ports
- Discrete I/O
- Timers and clocks

### I/O Access Control

Partitions access I/O through:

1. **Sampling/Queuing Ports**: For inter-partition data
2. **System Calls**: For direct I/O (if permitted)
3. **Shared Memory**: For DMA buffers (if configured)

## Health Monitoring Architecture

### Error Detection

- **Partition Errors**: Window overrun, illegal instruction, memory fault
- **System Errors**: Hardware faults, watchdog timeout
- **Communication Errors**: Port overflow, invalid message

### Error Response

```
Error Detected
     │
     ▼
Classify Error
     │
     ├─── Partition Error ──▶ Partition-Level Action
     │                        (restart, halt, etc.)
     │
     └─── System Error ────▶ System-Level Action
                             (switch redundant, safe mode, etc.)
```

### Health Monitoring Table

Configured per-partition and per-error-type:

| Error Type | Action | Recovery Time |
|------------|--------|---------------|
| Window Overrun | Halt Partition | Immediate |
| Illegal Instruction | Restart Partition | Next Major Frame |
| Memory Fault | Halt Partition | Immediate |
| Watchdog Timeout | Switch Redundant | < 50ms |

## Related Documents

- [OS Overview](./os_overview.md)
- [Security Model](./security_model.md)
- [Configuration Management](../S1000D/dmodule/DMC-Q100-A-42-12-00-00A-012A-D-EN-US.xml)
