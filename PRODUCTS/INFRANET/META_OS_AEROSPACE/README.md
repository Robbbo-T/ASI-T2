---
id: ASIT2-INFRANET-METAOS-README
project: ASI-T2
artifact: Meta-OS Aeroespacial/Defensa — Operating System of Systems
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-24
maintainer: OOO (OS), IIS (Integration), EDI (Avionics/Net)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  component: Meta-OS Aeroespacial/Defensa
  level: Meta-sistémico (DO-178C DAL-A/B, DO-326A, ISO-26262)
  bridges: CB→QB→UE→FE→FWD→QS
  status: BASELINED
canonical_hash: pending
---

# Meta-OS Aeroespacial/Defensa — Stack y Skeleton

Este repositorio es un **Meta-OS** federado para coordinar activos aeroespaciales (aeronaves, satélites, sondas, UAM/UAV, robótica, defensa/ciber).
Integra **plano de control seguro** (L1–L3), **plano de datos/decisiones** (L2/L5) y **digital thread** (L4), con puentes **CB→QB→UE→FE→FWD→QS**.

## Diagrama de stack por capas (conceptual)

```mermaid
flowchart TB
  L0[HW/Plataformas\nSoC, FPGA, GPU, QPU stub, radios, buses ARINC, 1553, CAN, SpaceWire]
  L1[Núcleo & Orquestación\nseL4/QNX/VxWorks | Linux-PREEMPT_RT/LSM\nHypervisor/ARINC-653 | Orquestador Federado | Planificador Heterogéneo]
  L2[Middleware & Interop\nDDS/ROS2, Gateways ARINC/1553/CAN/SpaceWire\nQoS determinista, TimeSync GNSS/PTP]
  L3[Certificación, Seguridad & Resiliencia\nPKI, Zero-Trust, MLS, FDIR, OTA firmado, Policy-as-Code]
  L4[Digital Thread & Gemelos\nMBSE/PLM/ALM, SIL/HIL, Twin Operativo]
  L5[Inteligencia & Optimización\nML en el borde, planificación autónoma, QOx QAOA/annealing]
  L6[Aplicaciones de Misión & Cockpit\nUI/UX, Mission Control, APIs de terceros]
  L0-->L1-->L2-->L3-->L4-->L5-->L6
  L2--telemetría-->L4
  L5--órdenes/planes-->L2
  L3--atestado/auditoría-->L4
```

> **Plano de control vs. plano de datos**: L1–L3 forman el **plano de control seguro** (aislamiento, políticas, certificación); L2 y L5 mueven **datos/decisiones** entre borde y tierra; L4 garantiza trazabilidad ciclo-de-vida (digital thread).

## Estructura principal

```
meta-os/
├─ platforms/
│  ├─ uav/                 # BSP, drivers, particiones ARINC-653 (UAV)
│  ├─ satellite/           # SpaceWire, RTEMS targets, ventanas de contacto
│  └─ ground/              # Estación terrestre (Linux endurecido)
├─ kernels/
│  ├─ rtos/                # seL4, VxWorks, RTEMS (configs y proofs/refs)
│  ├─ linux/               # PREEMPT_RT, LSM/SELinux, cgroups, IMA/EVM
│  └─ hypervisor/          # Jailhouse/Xen, particionado temporal/espacial
├─ orchestrator/
│  ├─ control-plane/       # scheduler, placement, reconciler, admission
│  ├─ edge-agents/         # agentes en UAV/SAT/GROUND (telemetría+comandos)
│  └─ manifests/           # mission/*.yaml (políticas por misión)
├─ middleware/
│  ├─ dds/                 # perfiles, qos_policies.yaml, IDL
│  ├─ ros2/                # paquetes, bridges, launchers
│  └─ gateways/            # arinc1553/, can/, spacewire/, radio/
├─ security/
│  ├─ pki/                 # raíces, intermedias, CRL, perfilar hardware
│  ├─ attestation/         # TPM/TEE, evidencias, mediciones
│  ├─ policies/            # OPA/Rego, SELinux, MLS, sandbox perfiles
│  ├─ ota/                 # firmador, manifiestos, rollback
│  └─ fdir/                # reglas y acciones (Fault Detection/Isolation/Recovery)
├─ certification/
│  ├─ do-178c/             # DAL A/B artefactos y trazabilidad
│  ├─ do-326a/             # amenazas, mitigaciones, pruebas de intrusión
│  └─ iso-26262/           # si aplica (UAM/UAV automoción aérea)
├─ digital-thread/
│  ├─ connectors/          # PLM/MBSE (SysML), ALM, trazas
│  └─ twin/                # modelos de estado, sims, SIL/HIL
├─ ai/
│  ├─ edge-runtime/        # ONNX/TensorRT pipelines deterministas
│  └─ models/              # visión, planificación, salud de flota
├─ qox/
│  ├─ optimizers/          # QAOA, annealing; wrappers para planners
│  └─ simulators/          # qpu_stub/ (interfaces locales)
├─ observability/
│  ├─ telemetry/           # protobuf/avro schemas; time-sync
│  └─ logging/             # logs firmados, cadenas de custodia
├─ tooling/
│  ├─ cli/                 # metaosctl (despliegue, diagnóstico, atestado)
│  └─ sdk/                 # APIs, codegen, emuladores
├─ examples/
│  └─ uav_sat_demo/        # misión ejemplo extremo a extremo
└─ docs/
   ├─ architecture/        # ADRs, diagramas, perfiles DAL
   └─ runbooks/            # operación, incidentes, MRO
```

## Artefactos de ejemplo incluidos

- **Manifiesto de misión**: `orchestrator/manifests/mission/uav_sat_demo.yaml`
- **QoS DDS determinista**: `middleware/dds/qos_policies.yaml`
- **OTA firmado**: `security/ota/update-manifests/uav01_2025-09-24.json`
- **Reglas FDIR**: `security/fdir/rules/uav_fdir.yaml`
- **Mapa ARINC-653**: `platforms/uav/partitions.map`
- **Política OPA/Rego (DAL-A)**: `security/policies/placement.rego`
- **Esquema de salud (telemetría)**: `observability/telemetry/schemas/health.proto`

## CLI de operación (stub)

En `tooling/cli/metaosctl.py` hay un CLI mínimo para:

```bash
# Despliegue con atestado
python tooling/cli/metaosctl.py deploy orchestrator/manifests/mission/uav_sat_demo.yaml --require-attestation

# Auditoría de QoS activos
python tooling/cli/metaosctl.py qos audit --profile crit-telemetry --asset UAV-01

# Simular FDIR y verificar plan de recuperación
python tooling/cli/metaosctl.py fdir test security/fdir/rules/uav_fdir.yaml --inject LOST_GNSS
```

## Ejemplo en acción

Una misión conjunta UAV + satélite + estación terrestre:

1. **UAV con FreeRTOS/ROS2** detecta anomalía
2. **Middleware** traduce y comunica al satélite con RTEMS sobre MIL-STD-1553
3. **Orquestador central** activa plan de contingencia definido bajo DO-178C
4. **Digital Twin** en tierra actualiza estado y recalcula misión con QAOA (optimización cuántica)
5. **Estación terrestre** aplica parche OTA seguro al UAV antes de la siguiente pasada

## Integración con AQUA OS

Este Meta-OS extiende y complementa los componentes existentes de INFRANET/AQUA_OS_AIRCRAFT:

- **A653_PM**: Base para hypervisor/particionado temporal-espacial
- **NET_STACK**: Fundación para middleware determinista DDS/ROS2
- **TIME_SYNC**: Sincronización PTP/TTE entre activos heterogéneos
- **SEC_KMS**: PKI y gestión de claves para zero-trust federado
- **QAFbW**: Ejemplo de aplicación DAL-A sobre Meta-OS

> **Notas**: 
> * Prioridad `0x0E` (hex) = `1110₂` (binario).  
> * Major frame ARINC-653 de `20 ms` con minor `[5,5,5,5]` garantiza determinismo temporal.
> * **Meta-OS federado** integra SoSE (System of Systems Engineering) + CPS (Cyber-Physical Systems) + Mission-Centric OS frameworks.

---

*Part of INFRANET Meta-OS Aerospace Extension under ASI-T2 portfolio*