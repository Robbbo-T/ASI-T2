# ATA-22 — Autoflight (BWB-Q100)

Autopilot, Flight Director, Yaw Damper, and mode management for BWB-Q100. Scope covers **software & intelligence** (IIS domain) with interfaces to:
- **ATA-27 Flight Controls (AAP domain)** — actuator commands & mode status
- **ATA-34 Nav/Air Data** — ADC/IRS/GPS/FMS data
- **ATA-46 Information Systems** — MFD/EFIS annunciations & crew control
- **AAA Airframes** — control-effect mapping (via 27/AAP)

> Development aligned to **DO-178C DAL A** (safety-critical). This repo provides structure, ICDs, unit tests, SIL harness, and CI.

## Features (initial)
- Lateral: **HDG HOLD, TRK HOLD, ROLL HOLD, LNAV (stub)**
- Vertical: **ALT HOLD, VS HOLD (stub VNAV)**
- Stability: **Yaw Damper**
- **Flight Director** command bars
- **Mode Manager** with engage/disengage & interlock logic

## Layout
- `architecture/` — system architecture, safety patterns
- `requirements/HLR.md` — high-level requirements
- `requirements/LLR/` — low-level requirements (per module)
- `icd/` — interface control docs (to ATA-27/34/46)
- `config/` — mode configs & gain schedules
- `software/` — source, tests, packaging
- `sitl/` — simple Software-In-The-Loop harness
- `qox/` — quantum optimization hooks (gain set selection, mode graph)

## Build & test
```bash
cd PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22/IIS/ata/ATA-22/software
python -m pip install -e ".[dev]"
pytest -q
```

## Notes

* **Autothrottle**: coordinated via engine control domain; commands exposed but not implemented here.
* **BWB specifics**: elevon-dominated pitch/roll; differential spoilers optional; yaw via split surfaces + YD.