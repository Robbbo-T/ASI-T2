# Configuration

IMA system configuration artifacts for ATA-42.

## Structure

- **manifests/** — Evidence manifests with hashes, SBOM references, QS anchors
- **a653/** — ARINC-653 partition and schedule definitions
- **rtos/** — Real-time operating system and board configuration

## ARINC-653 Configuration (a653/)

### partition.xml
Defines IMA partitions with:
- Partition identifiers and names
- Resource budgets (CPU, memory, I/O)
- APEX port definitions (sampling, queuing)
- Access control lists
- Health monitoring parameters

### schedule.xml
Defines temporal partitioning:
- Major frame duration
- Partition windows (start time, duration)
- Window to partition mapping
- Schedule validation rules

## Manifests (manifests/)

### manifest.yaml
Evidence bundle with:
- Configuration file hashes (SHA-256)
- SBOM references (dependencies, versions)
- Test result references
- Approval sign-offs
- QS/UTCS anchor for immutability

## RTOS Configuration (rtos/)

Board support and RTOS configuration:
- Processor and memory layout
- Device drivers configuration
- Boot sequence parameters
- System initialization
- Platform-specific settings
