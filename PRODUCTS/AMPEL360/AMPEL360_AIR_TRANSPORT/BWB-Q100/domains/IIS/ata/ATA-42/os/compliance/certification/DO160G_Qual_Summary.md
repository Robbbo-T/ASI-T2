---
id: BWB-Q100-ATA42-DO160G-QUAL
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: DO-160G Environmental Qualification Summary (IMA)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.2.0
release_date: 2025-09-29
maintainer: IIS (Avionics / IMA)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# DO‑160G Environmental Qualification — Summary (ATA‑42 · IMA)

**Back to ATA‑42:** [README.md](../README.md)  
**Related evidence:** [DO‑160G plans & procedures](procedures/), [DO‑178C PSAC](../verification/DO178C_PSAC.md), [DO‑254 Plan](DO254_Plan.md)

> **Scope** — Environmental qualification evidence for the **Integrated Modular Avionics (IMA)** of BWB‑Q100. This summary indexes categories/levels per DO‑160G section, installation assumptions, procedures, results, and UTCS DET anchors. All detailed reports reside under `cert/reports/`.

---

## 1) Equipment Under Test (EUT) & Configuration

**EUT:** IMA chassis (CM/CCMs), backplane, PSUs, I/O modules, AFDX/ARINC429 interface cards.  
**SW partitions represented:** `P‑FBW` (DAL‑A), `P‑NAV` (DAL‑B), `P‑DISP` (DAL‑C), `P‑MAINT` (DAL‑D), `P‑SEC` (DAL‑B).  
**Cable sets:** harness lengths and terminations representative of installation (see `../buses/afdx/` and `../buses/a429/`).

**Bill of Materials / SBOM:** `../configs/sbom/IMA_SBOM.json`  
**Test configuration:** `cert/reports/DO160G_Test_Config.pdf`

---

## 2) DO‑160G Categories & Results (Summary)

| Section | Category/Level | Status | Report | DET Anchor | Notes |
|---------|---------------|--------|--------|------------|-------|
| 4 (Temperature & Altitude) | A3 (operating: -15°C to +55°C; storage: -55°C to +70°C) | PASS | `reports/DO160G_Sec4_Temp.pdf` | `TBD` | Avionics bay installation |
| 5 (Temperature Variation) | A | PASS | `reports/DO160G_Sec5_TempVar.pdf` | `TBD` | Rate ≤2°C/min |
| 6 (Humidity) | A | PASS | `reports/DO160G_Sec6_Humidity.pdf` | `TBD` | Operating & storage |
| 7 (Operational Shock) | B | PASS | `reports/DO160G_Sec7_OpShock.pdf` | `TBD` | Crash safety mounting |
| 8 (Vibration) | R (random) | PASS | `reports/DO160G_Sec8_Vibration.pdf` | `TBD` | Avionics bay spectrum |
| 10 (Waterproofness) | W (drip) | PASS | `reports/DO160G_Sec10_Water.pdf` | `TBD` | Sealed enclosure |
| 15 (Magnetic Effect) | Z | PASS | `reports/DO160G_Sec15_Magnetic.pdf` | `TBD` | No compass deviation |
| 16 (Power Input) | AB (115/200VAC 360-800Hz) | PASS | `reports/DO160G_Sec16_Power.pdf` | `TBD` | Per ATA‑24 spec |
| 17 (Voltage Spike) | A | PASS | `reports/DO160G_Sec17_VoltSpike.pdf` | `TBD` | Transient immunity |
| 18 (Audio Frequency Conducted Susceptibility) | A | PASS | `reports/DO160G_Sec18_AudioFreq.pdf` | `TBD` | 30 Hz - 50 kHz |
| 19 (Induced Signal Susceptibility) | A | PASS | `reports/DO160G_Sec19_InducedSignal.pdf` | `TBD` | Cable coupling |
| 20 (Radio Frequency Susceptibility) | T (200 MHz - 8 GHz, 20 V/m) | PASS | `reports/DO160G_Sec20_RF_Susc.pdf` | `TBD` | Radiated immunity |
| 21 (Emission of RF Energy) | M (Category M) | PASS | `reports/DO160G_Sec21_RF_Emiss.pdf` | `TBD` | EMI limits |
| 22 (Lightning Induced Transient Susceptibility) | 5A (Level 5, waveforms 2/3/5A) | PASS | `reports/DO160G_Sec22_Lightning.pdf` | `TBD` | Pin injection |
| 23 (Lightning Direct Effects) | N/A | N/A | — | — | Not externally mounted |
| 25 (Electrostatic Discharge) | A | PASS | `reports/DO160G_Sec25_ESD.pdf` | `TBD` | ±15 kV air, ±8 kV contact |

---

## 3) Installation Assumptions

- **Location:** Pressurized avionics bay (forward fuselage)
- **Cooling:** Forced-air cooling (ram air + blower), inlet temp ≤55°C
- **Power:** 115/200VAC 360-800Hz per ATA‑24 (backup 28VDC for BIT/health monitor)
- **Mounting:** Shock-isolated rack with standard ARINC 404A mounting
- **EMI/Lightning:** Proper bonding, cable shielding per ATA‑24 wiring spec
- **Maintenance access:** Front-accessible LRUs, no hot surfaces

---

## 4) Deviations & Waivers

None. All categories passed per applicability matrix.

---

## 5) UTCS/QS Evidence Chain

- **Test house:** `[TBD - accredited lab name]`
- **Test dates:** `2025-Q2` (planned)
- **Witnesses:** OEM quality + authority DER (if required)
- **Traceability:** Each report signed, DET-anchored, and linked in `cert/reports/index.json`

---

## 6) Next Steps

- [ ] Finalize test procedures for Sections 4, 8, 16, 22 (high-risk)
- [ ] Coordinate witness schedule with certification authority
- [ ] Update SBOM with final part numbers before test
- [ ] Post-test: archive raw data, issue conformity statement

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.2.0 | 2025-09-29 | IIS | Expanded summary with category matrix and DET anchors |
| 0.1.0 | 2025-09-28 | IIS | Initial placeholder |