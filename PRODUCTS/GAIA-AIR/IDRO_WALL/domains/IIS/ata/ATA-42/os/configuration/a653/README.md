# ARINC-653 Configuration

ARINC-653 partition and schedule definitions for IMA system.

## Files

- **partition.xml** — Partition definitions, APEX ports, resource budgets
- **schedule.xml** — Major frame and window assignments

## partition.xml

Defines IMA partitions following ARINC-653 specifications:

### Partitions
- `IIS.SwarmCore` — Swarm coordination and resilient consensus (DAL B)
- `IIS.MAL-EEM` — Ethics gate with fail-closed pre-action assessment (DAL A)
- `IIS.MissionPlanner` — Planning, tasking, and replanning (DAL B)
- `IIS.CMSAdapter` — Health/telemetry export to CMS (DAL C)

### APEX Ports
Each partition defines:
- **Sampling ports** — Latest value semantics
- **Queueing ports** — FIFO message queues
- **Port direction** — Source (SRC) or Destination (DST)
- **Port names** — Following `domain.function.version` convention

### Resource Budgets
- **CPU percentage** — Computational allocation
- **Memory (KB)** — RAM allocation
- **I/O bandwidth** — If applicable

## schedule.xml

Defines temporal partitioning:

### Major Frame
- Duration: 100 ms (baseline)
- Cycle rate: 10 Hz

### Windows
- W1: MAL-EEM (0-20 ms)
- W2: SwarmCore (20-60 ms)
- W3: MissionPlanner (60-100 ms)
- CMSAdapter: Best-effort in remaining slots

## Validation

Configuration validated for:
- Schedule feasibility (all partitions fit in major frame)
- Budget sufficiency (CPU/memory adequate for partition needs)
- Port connectivity (all ports have valid endpoints)
- Safety constraints (DAL A partitions isolated)
