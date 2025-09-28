---
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-BWB-Q100-LCC-ATA27-QAFBW-BINDING
llc: SYSTEMS
maintainer: LCC (Control Laws), EDI (Avionics Integration)
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
release_date: 2024-09-23
utcs_mi: 'binding_scope: BWB-Q100_product_specific

  aqua_os_component: QAFbW_Control_Stack

  ata_chapter: ATA-27_Flight_Controls

  '
version: 1.0
---

# QAFbW BWB-Q100 Product Binding

## Overview

This document defines the product-specific binding of the generic [AQUA OS QAFbW Control Stack](../../../../../../INFRANET/AQUA_OS_AIRCRAFT/components/QAFbW/) to the **AMPEL360 BWB-Q100** aircraft.

The binding transforms the generic AQUA OS component specification into BWB-Q100-specific implementation through:
1. **Physical Interface Mapping**: Logical topics → physical sensors/actuators
2. **Control Law Tuning**: Generic algorithms → BWB-Q100 flight characteristics  
3. **Envelope Parameters**: Generic limits → BWB-Q100 certified flight envelope
4. **Integration Testing**: HIL/Iron Bird validation for BWB-Q100 configuration

## Physical Interface Mapping

### Sensor Mapping
| Logical Topic | Physical Sensor | Bus/Location | Sample Rate |
|:---|:---|:---|:---|
| `aqua.fcl.sensor.imu` | Honeywell HG4930 | ARINC-429 Bus A/B | 500 Hz |
| `aqua.fcl.sensor.airdata` | Rosemount 1151 | Analog/Digital | 200 Hz |
| `aqua.fcl.surface_fb` | Parker EMAs | CAN Bus | 500 Hz |

### Actuator Mapping  
| Logical Command | Physical Actuator | Type | Authority |
|:---|:---|:---|:---|
| `pos_cmd_deg[0-3]` | Elevon EMAs 1-4 | Parker Hannifin | ±25° |
| `pos_cmd_deg[4-5]` | Rudder EMAs 1-2 | Liebherr | ±30° |

## BWB-Q100 Flight Control Laws

### Control Modes & Envelope
- **Normal Mode**: Full BWB stability augmentation + envelope protection
- **Alternate Mode**: Reduced augmentation, relaxed envelope limits  
- **Direct Mode**: Minimal augmentation, pilot authority preserved
- **Reversionary Mode**: Hardwired backup, basic stability only

### BWB-Specific Parameters
```yaml
flight_envelope:
  alpha_max_deg: 18.0        # BWB-Q100 specific AoA limit
  alpha_min_deg: -5.0
  nz_max_g: 2.5             # Load factor limits for transport category
  nz_min_g: -1.0
  bank_max_deg: 67.0        # Bank angle limit
  
control_gains:
  pitch_rate_kp: 0.85       # Tuned for BWB-Q100 inertia
  roll_rate_kp: 1.2         # BWB span-specific tuning
  yaw_rate_kp: 0.65         # BWB stability characteristics
```

## Integration Evidence

### HIL Test Campaign Reference
- **Test Facility**: BWB-Q100 Iron Bird (LCC Domain)
- **Evidence Location**: `domains/LCC/cax/VP/HIL_results/QAFbW_validation/`
- **UTCS Seal**: Links to AQUA OS component VCRM

### Configuration Management
- **Baseline Control**: BWB-Q100 CCB authority
- **Change Process**: Generic AQUA OS changes → product impact assessment
- **Evidence Chain**: AQUA OS UTCS/QS ↔ BWB-Q100 product evidence

## Cross-Reference

### AQUA OS Component
- **Generic Specification**: [QAFbW Component Spec](../../../../../../INFRANET/AQUA_OS_AIRCRAFT/components/QAFbW/QAFbW_Component_Spec.md)
- **Interface Contract**: [QAFbW ICD](../../../../../../INFRANET/AQUA_OS_AIRCRAFT/components/QAFbW/QAFbW_ICD.yaml)
- **Verification Matrix**: [QAFbW VCRM](../../../../../../INFRANET/AQUA_OS_AIRCRAFT/components/QAFbW/QAFbW_VCRM.csv)

### BWB-Q100 Integration
- **System Architecture**: [BWB-Q100 README](../../../../README.md)
- **Network Integration**: [EDI/ATA-22](../../EDI/ata/ATA-22/)
- **OS Integration**: [OOO/ATA-22](../../OOO/ata/ATA-22/)

---

*BWB-Q100 product binding for INFRANET AQUA OS QAFbW component*