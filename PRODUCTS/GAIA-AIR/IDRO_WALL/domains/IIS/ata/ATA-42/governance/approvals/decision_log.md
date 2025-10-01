# Decision Log — ATA-42 IIS

Human-readable record of key architectural and configuration decisions.

## Format

### DECISION-XXX: Title (YYYY-MM-DD)

**Context:** What situation prompted this decision?

**Decision:** What was decided?

**Rationale:** Why was this the best choice?

**Consequences:** What are the implications?

**Approvers:** Who signed off?

---

## Decisions

<!-- Add decision entries below -->

<!-- Example:
### DECISION-001: ARINC-653 Major Frame Selection (2025-10-01)

**Context:** Initial IMA schedule design required major frame duration selection.

**Decision:** Selected 100 ms major frame with three windows for partitions.

**Rationale:** Provides adequate time slots for SwarmCore (40ms), MissionPlanner (40ms), and MAL-EEM (20ms) while maintaining 10 Hz system cycle rate.

**Consequences:** All partitions must complete their critical operations within assigned windows. Window overruns trigger health monitoring alerts.

**Approvers:** System Lead (J.Smith), Safety Lead (M.Johnson)
-->
