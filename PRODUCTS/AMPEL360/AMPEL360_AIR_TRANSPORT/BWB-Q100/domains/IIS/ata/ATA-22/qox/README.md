# QOx hooks for ATA-22

Targets for quantum/hybrid optimization:
- **Gain-set selection** across envelopes (discrete candidate sets → QUBO)
- **Mode transition graph** pruning (minimize undesired transitions subject to safety constraints)

Artifacts:
- `problem_definitions/` (TBD) with JSON/QUBO encodings
- Fitness from SIL runs (tracking error, overshoot, capture time)