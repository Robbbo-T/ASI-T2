# Repair & Reuse Routes

This directory contains repair operations, acceptance limits, and reuse decision logic for circular economy lifecycle management.

## Structure

- **operations/** — Repair operations (CO-3.13) — Inspect/repair/overhaul procedures
- **limits/** — Acceptance limits (CO-3.14) — Post-repair verification thresholds
- **rules/** — Reuse decision rules (CO-3.15) — R-score formulas and criteria

## Shop Visit Routes

Parts are routed through maintenance levels based on condition and requirements:

### L1 — Line Maintenance
- Quick inspections
- Minor repairs
- Cosmetic work
- Preventive maintenance
- Typical turnaround: hours to days

### L2 — Base Maintenance
- Intermediate repairs
- Component replacements
- Non-destructive testing
- Detailed inspections
- Typical turnaround: days to weeks

### L3 — Depot/Heavy Maintenance
- Major overhauls
- Structural repairs
- Complete refurbishment
- Life extension work
- Typical turnaround: weeks to months

## Operation Codes

Standard operation codes include:
- **INSPECT** — Visual and instrumented inspection
- **CLEAN** — Cleaning and preparation
- **REPAIR** — Corrective repair work
- **OVERHAUL** — Complete refurbishment
- **TEST** — Functional and performance testing
- **CERTIFY** — Final certification and release

## Acceptance Limits (CO-3.14)

Post-repair verification thresholds for key metrics:

### Structural Metrics
- Dimensional tolerance
- Straightness/flatness
- Surface finish
- Crack growth limits

### Functional Metrics
- Leak rate (pressure systems)
- Bond resistance (electrical bonding)
- Bond void area (adhesive bonding)
- Performance parameters

### Methods
- Visual inspection
- NDT (ultrasonic, eddy current, X-ray)
- Dimensional measurement
- Functional testing
- Pressure/leak testing

## Reuse Decision Logic (CO-3.15)

**R-Score Formula**: Weighted assessment of repairability and reusability

Factors considered:
1. **Condition Score** (0-100): Current physical condition
2. **Life Remaining** (0-100): Remaining useful life percentage
3. **Repair Cost** (0-100): Cost vs. new part value
4. **Repair Feasibility** (0-100): Technical feasibility
5. **Criticality** (0-100): Safety/mission criticality

### Decision Thresholds
- **R-Score ≥ 80**: Reuse without repair
- **R-Score 50-79**: Repair and reuse (route to appropriate level)
- **R-Score 30-49**: Repair only if critical shortage
- **R-Score < 30**: Scrap (non-repairable)

### Overrides
- Safety-critical items may have higher thresholds
- Economic factors (new part availability, lead time)
- Fleet-wide considerations
- Regulatory requirements
- Customer requirements

## Provenance Tracking

All repair/reuse decisions are tracked with:
- **Unit State Transitions** (CO-3.21): From/to state changes
- **Provenance Edges** (CO-3.22): Complete history of events
- **Evidence** (CO-3.23): Supporting documentation
- **QS Sealing** (CO-3.29): Cryptographic integrity

## Integration with ATA-20

All repair work follows **ATA-20 Standard Practices**:
- Use approved procedures
- Document with appropriate forms
- Maintain complete evidence packages
- Apply QS/UTCS sealing

---

*Part of 360IPCirq — Configuration controlled under UTCS/QS v5.0*
