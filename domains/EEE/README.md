# EEE · Renewable Energy, Harvesting & Circulation

**Description:** Energy generation, harvesting, and distribution systems

## Structure

This domain follows the standard ASI-T2 domain architecture:

```
EEE/
├── PLM/            # Product Lifecycle Management (CAx processes)
│   ├── CAO/        # Computer Aided Kick-Off (CON/REQ/SYS)
│   ├── CAD/        # Computer Aided Design (ASSY/PRT/DRW)
│   ├── CAE/        # Computer Aided Engineering (FEM/CFD/MBD/EMI)
│   ├── CAM/        # Computer Aided Manufacturing (NC/APT/OPR/FIX/TOOL/SET)
│   ├── CAV/        # Quality Verification & Validation (QIP/QIF/DMIS/MEAS/MSA/CERT)
│   ├── CAI/        # Computer Aided Installation & Integration (INS/INT/FIT)
│   ├── CAS/        # Services in Operation (AMM/SRM/IPD/EIS)
│   ├── CAP/        # Computer Aided Processes (overlay + domain)
│   └── CMP/        # CAMPost - Services Post Operations (EoL/Recycling/ESG)
├── QUANTUM_OA/     # Quantum Optimization & Approximation
│   ├── QOX/        # Quantum Optimization (generic)
│   ├── MILP/       # Mixed Integer Linear Programming
│   ├── LP/         # Linear Programming
│   ├── QP/         # Quadratic Programming
│   ├── QUBO/       # Quadratic Unconstrained Binary Optimization
│   ├── QAOA/       # Quantum Approximate Optimization Algorithm
│   ├── SA/         # Simulated Annealing
│   └── GA/         # Genetic Algorithms
├── PAx/            # Packaging (artifacts)
├── DELs/           # Final Check & Deliveries
├── policy/
│   ├── lints/      # Naming convention validators
│   └── schematron/ # S1000D validation rules
└── tests/          # Test suites
```

## CAx Process Definitions

### CAO — Computer Aided Kick-Off
**What it is:** Pre-design and program start-up: concept, requirements, architecture, baselines.
- **Inputs:** needs, constraints, trade-off studies
- **Outputs:** Concept docs, specifications, system architecture
- **DISC types:** CON, REQ, SYS
- **Extensions:** pdf, docx, req, xml, json
- **Example:** `CON-BWQ1-CAO5710-FWD-SPAR-CONFIG-GA-r001.pdf`

### CAD — Computer Aided Design
**What it is:** 3D modeling, assemblies and drawings.
- **Inputs:** CON/REQ/SYS; geometric specs
- **Outputs:** parts, assemblies, drawings
- **DISC types:** ASSY, PRT, DRW
- **Extensions:** step, stp, sldprt, sldasm, ipt, iam, dwg, dxf, pdf
- **Example:** `ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step`

### CAE — Computer Aided Engineering
**What it is:** Analysis and simulation (structures, fluids, multibody, EMC/EMI).
- **Inputs:** CAD; loads; boundary conditions
- **Outputs:** solver models and results
- **DISC types:** FEM, CFD, MBD, EMI
- **Extensions:** inp, cdb, cas, dat, fem, nas, pdf
- **Example:** `FEM-BWQ1-CAE5710-FS-BOX-STAT-r006.inp`

### CAM — Computer Aided Manufacturing
**What it is:** Manufacturing planning and programming.
- **Inputs:** CAD; routes; tooling
- **Outputs:** NC code, process sheets, tooling
- **DISC types:** NC, APT, OPR, FIX, TOOL, SET
- **Extensions:** nc, eia, apt, cl, cls, csv, pdf, step, stp
- **Example:** `NC-BWQ1-CAM5710-FWD-SPAR-OP30-DRILL-r002.nc`

### CAV — Quality Verification & Validation
**What it is:** V&V plans, execution and certifications.
- **Inputs:** CAD/CAE; acceptance criteria
- **Outputs:** QIF/DMIS programs, measurements, COCs, MSA
- **DISC types:** QIP, QIF, DMIS, MEAS, MSA, CERT
- **Extensions:** qif, dmis, csv, xml, pdf
- **Example:** `QIF-BWQ1-CAV5710-FWD-SPAR-GDTPMI-r003.qif`

### CAI — Computer Aided Installation & Integration
**What it is:** Assembly installation and integration into higher-level systems.
- **Inputs:** CAD/CAE/CAM; tooling; interfaces
- **Outputs:** instructions, fit checks, integration models
- **DISC types:** INS, INT, FIT
- **Extensions:** pdf, step, dwg, json
- **Example:** `INS-BWQ1-CAI5710-FWD-SPAR-INSTALL-GA-r001.pdf`

### CAS — Services in Operation
**What it is:** In-service support and Technical Publications.
- **Inputs:** S1000D DMRL; service feedback
- **Outputs:** AMM, SRM, IPD, EIS, bulletins
- **DISC types:** AMM, SRM, IPD, EIS
- **Extensions:** xml, sgml, pdf
- **Example:** `IPD-BWQ1-CAS5710-FWD-SPAR-IPD-941A-r003.xml`

### CAP — Computer Aided Processes
**What it is:** Cross-functional processes (DevOps, CI/CD, QA/Testing, Schema/BREX, Security/Observability).

**Two usage modes:**
1. **Optional overlay** on any CAx file: `-CAP.[CI|CD|QA|TEST|UNIT|E2E|PERF|HIL|SIL|LINT|SCHEMA|BREX|SEC|TRACE|LOG|MON].[DEV|INT|STG|PROD]`
2. **Own domain** for pipelines/evidence: DISC `PIPE, JOB, TESTSET, EVID, RPT`

- **Extensions:** yml, yaml, json, xml, csv, pdf
- **Examples:**
  - Overlay: `FEM-BWQ1-CAE5710-FS-BOX-STAT-CAP.TEST.STG-r006.inp`
  - Domain: `PIPE-BWQ1-CAP5710-FWD-SPAR-CI-PIPELINE-r001.yaml`

### CMP — CAMPost (Services Post Operations)
**What it is:** Post-operation services (disassembly, recycling, treatment, ESG compliance).
- **Inputs:** BOM/trace; regulations
- **Outputs:** EoL reports, traceability, certificates
- **DISC types:** EPR, RECY, TREAT, DISP, MATREC, CERT
- **Extensions:** pdf, csv, xml, json
- **Example:** `RECY-BWQ1-CMP5710-FWD-SPAR-MATREC-AL7050-98PCT-r003.csv`

**Note:** CAS is in-service operation; CMP is post-operation (EoL). CAP never replaces other domains: it annotates them (overlay) or captures process artifacts.

## Naming Conventions

### PLM (CAx++) Pattern
```
<DISC>-<MIC>-<DOMAIN><ATA>-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```
- ATA default: **5710**
- See `policy/lints/lint_names.py` for full regex

### QUANTUM_OA Pattern
```
<ALG>-<MIC>-QOA<ATA>-<SCOPE>-<DATASET?>-<STAGE?>-r<REV>.<EXT>
```
- Examples: `MILP-BWQ1-QOA5710-FWD-SPAR-OPT-DS-BENCH01-DEV-r003.lp`

### PAx Pattern
```
PAX-<MIC>-PKG<ATA>-<SCOPE>-<TYPE>-r<REV>.<EXT>
```
- Examples: `PAX-BWQ1-PKG5710-FWD-SPAR-DOCS-r001.zip`

### DELs Pattern
```
<DISC>-<MIC>-REL<ATA>-<SCOPE>-<TAG>-r<REV>.<EXT>
```
- Examples: `DLV-BWQ1-REL5710-FWD-SPAR-PKG-r001.zip`

## Compliance

- **Linter:** `policy/lints/lint_names.py` validates filenames per tree
- **Schematron:** `policy/schematron/dmc-ata-align.sch` validates S1000D DMCs
- **CI:** `.github/workflows/domains-filename-policy.yml` runs automated checks

## Testing

Run domain-specific tests:
```bash
python3 -m pytest domains/EEE/tests/test_lint_names.py -v
```

Or test the linter directly:
```bash
python3 domains/EEE/policy/lints/lint_names.py domains/EEE
```

## Contributing

Follow the standard naming conventions and ensure all files are placed in the correct process folder (PLM, QUANTUM_OA, PAx, or DELs). Run the linter before committing.

---

**Classification:** INTERNAL–EVIDENCE-REQUIRED  
**Maintainer:** ASI-T Architecture Team  
**UTCS-MI:** v5.0
