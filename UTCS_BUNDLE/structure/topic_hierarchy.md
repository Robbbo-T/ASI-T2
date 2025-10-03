# ASI-T2 MAP Topic ↔ TFA Path ↔ S1000D DMC Crosswalk

## BWB-Q100 Program Mappings

This document provides the canonical crosswalk between:
- **MAP Topics** — ASI-T2 MAP contract topic paths
- **TFA Paths** — Physical repository paths following ATA/S1000D grammar
- **S1000D DMCs** — Data Module Codes for structured documentation

### Topic Hierarchy Format

```
map/<major>/<contract>/<program>/<domain>/<component>/<stream>/<layer>
```

Where:
- `<major>` = Contract major version (e.g., 1)
- `<contract>` ∈ {control, telemetry, health, log, advisory}
- `<program>` = Program identifier (e.g., BWB-Q100, GAIA-SAT)
- `<domain>` = Three-letter domain code (e.g., AAA, AAP)
- `<component>` = Component identifier (e.g., STATES, WAVES, SYSTEMS)
- `<stream>` = Data stream identifier (e.g., SI, ECS, THRUST)
- `<layer>` = TFA bridge layer (e.g., QS, FWD, CB, QB)

## BWB-Q100 AAA Domain (Airframe, Aerodynamics, Avionics)

### QS Layer — State Logging

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/log/BWB-Q100/AAA/STATES/QS/QS | domains/AAA/ATA-57/57-10_Wing/S1000D/QS/PAx/OB/ | DMC-BWB-Q100-A-57-10-00-00A-QS0A-D | Wing state logging and evidence capture |
| map/1/log/BWB-Q100/AAA/STATES/QS/QS | domains/AAA/ATA-53/53-00_Fuselage/S1000D/QS/PAx/OB/ | DMC-BWB-Q100-A-53-00-00-00A-QS0A-D | Fuselage state logging |
| map/1/log/BWB-Q100/AAA/DECISIONS/QS/QS | domains/AAA/ATA-22/22-10_Autopilot/S1000D/QS/PAx/OB/ | DMC-BWB-Q100-A-22-10-00-00A-QS0A-D | Autopilot decision logging |

### FWD Layer — Nowcast & Prediction

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/telemetry/BWB-Q100/AAA/WAVES/FWD/FWD | domains/AAA/ATA-57/57-10_Wing/S1000D/FWD/CAx/CFD/ | DMC-BWB-Q100-A-57-10-00-00A-FWD0A-D | Wing aerodynamic nowcast |
| map/1/telemetry/BWB-Q100/AAA/PRESSURE/FWD/FWD | domains/AAA/ATA-30/30-00_IceRainProtect/S1000D/FWD/CAx/CAE/ | DMC-BWB-Q100-A-30-00-00-00A-FWD0A-D | Pressure and ice protection forecast |
| map/1/telemetry/BWB-Q100/AAA/THERMAL/FWD/FWD | domains/AAA/ATA-21/21-00_AirConditioning/S1000D/FWD/CAx/CAE/ | DMC-BWB-Q100-A-21-00-00-00A-FWD0A-D | Thermal management prediction |

### UE Layer — Unit Element / Measurement

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/telemetry/BWB-Q100/AAA/SENSORS/UE/UE | domains/AAA/ATA-34/34-00_Navigation/S1000D/UE/PAx/OB/ | DMC-BWB-Q100-A-34-00-00-00A-UE0A-D | Navigation sensor measurements |
| map/1/telemetry/BWB-Q100/AAA/ACTUATORS/UE/UE | domains/AAA/ATA-27/27-00_FlightControls/S1000D/UE/PAx/OB/ | DMC-BWB-Q100-A-27-00-00-00A-UE0A-D | Flight control actuator states |

### FE Layer — Federation & Contracting

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/control/BWB-Q100/AAA/FEDERATION/FE/FE | domains/AAA/ATA-42/42-00_IMA/S1000D/FE/CAx/CAD/ | DMC-BWB-Q100-A-42-00-00-00A-FE0A-D | Integrated Modular Avionics federation |
| map/1/control/BWB-Q100/AAA/CONTRACTS/FE/FE | domains/AAA/ATA-45/45-00_CMS/S1000D/FE/PAx/OB/ | DMC-BWB-Q100-A-45-00-00-00A-FE0A-D | Central Maintenance System contracts |

### CB Layer — Classical Control & Computation

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB | domains/AAA/ATA-57/57-10_Wing/S1000D/CB/QOx/OPT/ | DMC-BWB-Q100-A-57-10-00-00A-CB0A-D | Wing system classical optimization |
| map/1/control/BWB-Q100/AAA/FCS/PRIMARY/CB | domains/AAA/ATA-27/27-00_FlightControls/S1000D/CB/CAx/CAD/ | DMC-BWB-Q100-A-27-00-00-00A-CB0A-D | Primary flight control system |
| map/1/control/BWB-Q100/AAA/ECS/THERMAL/CB | domains/AAA/ATA-21/21-00_AirConditioning/S1000D/CB/CAx/CAE/ | DMC-BWB-Q100-A-21-00-00-00A-CB0A-D | Environmental control classical solver |

### QB Layer — Advisory & Decision Support

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/advisory/BWB-Q100/AAA/CUBIC/QB/QB | domains/AAA/ATA-22/22-10_Autopilot/S1000D/QB/QOx/ANNEAL/ | DMC-BWB-Q100-A-22-10-00-00A-QB0A-D | Autopilot quantum-inspired advisory |
| map/1/advisory/BWB-Q100/AAA/ROUTING/QB/QB | domains/AAA/ATA-34/34-00_Navigation/S1000D/QB/QOx/OPT/ | DMC-BWB-Q100-A-34-00-00-00A-QB0A-D | Route optimization advisory |
| map/1/advisory/BWB-Q100/AAA/MAINTENANCE/QB/QB | domains/AAA/ATA-45/45-00_CMS/S1000D/QB/QOx/ANNEAL/ | DMC-BWB-Q100-A-45-00-00-00A-QB0A-D | Predictive maintenance advisory |

## GAIA-SAT Program Mappings

### Space Systems (AAP Domain)

| MAP Topic | TFA Path | S1000D DMC | Description |
|-----------|----------|------------|-------------|
| map/1/telemetry/GAIA-SAT/AAP/ORBIT/FWD/FWD | domains/AAP/ATA-00/00-00_General/S1000D/FWD/CAx/CAE/ | DMC-GAIA-SAT-P-00-00-00-00A-FWD0A-D | Orbit propagation and prediction |
| map/1/control/GAIA-SAT/AAP/ADCS/CB/CB | domains/AAP/ATA-00/00-00_General/S1000D/CB/CAx/CAD/ | DMC-GAIA-SAT-P-00-00-00-00A-CB0A-D | Attitude determination and control |
| map/1/advisory/GAIA-SAT/AAP/COLLISION/QB/QB | domains/AAP/ATA-00/00-00_General/S1000D/QB/QOx/OPT/ | DMC-GAIA-SAT-P-00-00-00-00A-QB0A-D | Collision avoidance advisory |

## Validation Requirements

### Crosswalk Completeness

UTCS bundles **MUST** ensure:

1. **Topic Coverage:** All active MAP topics are mapped to TFA paths
2. **Path Validity:** All TFA paths conform to grammar in `tfa_grammar.md`
3. **DMC Format:** All S1000D DMCs follow the pattern:
   ```
   DMC-<PROGRAM>-<DOMAIN_LETTER>-<ATA>-<SUBATA>-<VARIANT>-<INFOCODE>-<LAYER><ITEM>-<TYPE>
   ```
4. **Bidirectional Mapping:** Topics ↔ Paths ↔ DMCs must be bidirectionally resolvable

### CI Enforcement

The following checks are enforced at CI:

```bash
# Validate crosswalk completeness
utcs validate --manifest manifest.utcs.yaml --check-crosswalk

# Verify topic grammar
map contracts.check --crosswalk structure/topic_hierarchy.md

# Verify path grammar
tfa path.check --grammar structure/tfa_grammar.md
```

## Usage Notes

### Adding New Mappings

When adding new systems or components:

1. Choose appropriate ATA chapter for the component
2. Select TFA bridge layer based on function (QS/FWD/UE/FE/CB/QB)
3. Select pack (CAx/QOx/PAx) and valid subpack
4. Generate S1000D DMC following naming convention
5. Add entry to this crosswalk table
6. Update manifest.utcs.yaml with new files
7. Run validation: `utcs validate --manifest manifest.utcs.yaml`

### Historical Notes

- **v5.0:** Introduced UiX Threading model (Context/Content/Cache & Structure/Style/Sheet)
- **v4.x:** Legacy "Universal Traceability & Crypto Signatures" semantics
- **v3.x and earlier:** Pre-UTCS bundling models (deprecated)

## References

- [Master Whitepaper #1](../context/MASTER_WHITEPAPER_1.md) — TFA V2 Architecture
- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — QS/UTCS Provenance Framework
- [TFA Grammar](tfa_grammar.md) — Path validation rules
- [ATA Spec 2200](https://www.ata.org/resources/specifications) — ATA chapter definitions
- [S1000D](http://www.s1000d.org/) — International specification for technical publications
