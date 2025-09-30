---
id: BWBQ100-IIS-ATA42-AFDX-INDEX
project: ASI-T2
artifact: ATA-42 AFDX Bus Implementation
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: 2025-09-30
maintainer: IIS (Integrated Information Systems)
language_default: en-US
enterprise_code: IIS
brex_dmref: DMC-Q100-A-42-79-00-00A-022A-D-EN-US
dmrl_file: ./S1000D/dmrl/ATA-42-AFDX.dmrlexchange.xml
canonical_hash: pending
ethics_guard: MAL-EEM
---

# ATA-42 — AFDX Bus Implementation (BWB-Q100)

S1000D-conformant documentation for the ARINC 664 (AFDX) bus implementation in the BWB-Q100 IMA system, including architecture, configuration, testing, and compliance.

## 📋 Quick Navigation

- [S1000D Data Modules](#s1000d-data-modules)
- [Configuration Files](#configuration-files)
- [Test Results](#test-results)
- [Compliance Evidence](#compliance-evidence)
- [Standard References](#standard-references)
- [Validation Tools](#validation-tools)
- [CAUiX Templates](#cauix-templates)

## 🗂️ S1000D Data Modules

| DM Code | Description | File |
|---------|-------------|------|
| `DMC-Q100-A-42-70-00-00A-010A-D-EN-US.xml` | General AFDX description | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-70-00-00A-010A-D-EN-US.xml) |
| `DMC-Q100-A-42-71-00-00A-010A-D-EN-US.xml` | AFDX network architecture | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-71-00-00A-010A-D-EN-US.xml) |
| `DMC-Q100-A-42-72-00-00A-012A-D-EN-US.xml` | Virtual Links configuration | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-72-00-00A-012A-D-EN-US.xml) |
| `DMC-Q100-A-42-73-00-00A-030A-D-EN-US.xml` | AFDX security implementation | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-73-00-00A-030A-D-EN-US.xml) |
| `DMC-Q100-A-42-74-00-00A-020A-P-EN-US.xml` | AFDX integration procedures | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-74-00-00A-020A-P-EN-US.xml) |
| `DMC-Q100-A-42-75-00-00A-020A-P-EN-US.xml` | AFDX test procedures | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-75-00-00A-020A-P-EN-US.xml) |
| `DMC-Q100-A-42-79-00-00A-022A-D-EN-US.xml` | AFDX compliance documentation | [📄 View](./S1000D/dmodule/DMC-Q100-A-42-79-00-00A-022A-D-EN-US.xml) |

### Supporting S1000D Files
- **DMRL**: [📄 ATA-42-AFDX.dmrlexchange.xml](./S1000D/dmrl/ATA-42-AFDX.dmrlexchange.xml)
- **BREX**: [📄 BREX-ATA42-AFDX.xml](./S1000D/brex/BREX-ATA42-AFDX.xml)
- **Schemas**: [📁 View](./S1000D/schemas/6.0/)

## ⚙️ Configuration Files

| File | Description | Link |
|------|-------------|------|
| `virtual_links.schema.json` | JSON schema for VL configuration | [📄 View](./configuration/virtual_links.schema.json) |
| `virtual_links.yaml` | Virtual Links definitions | [📄 View](./configuration/virtual_links.yaml) |
| `switch_configuration.json` | Switch configuration | [📄 View](./configuration/switch_configuration.json) |
| `bandwidth_allocation.yaml` | Bandwidth allocation | [📄 View](./configuration/bandwidth_allocation.yaml) |
| `vl_scheduling.yaml` | VL scheduling parameters | [📄 View](./configuration/vl_scheduling.yaml) |
| `redundancy_config.yaml` | Redundancy configuration | [📄 View](./configuration/redundancy_config.yaml) |
| `gateway_config.yaml` | Gateway configuration | [📄 View](./configuration/gateway_config.yaml) |

## 🧪 Test Results (Markdown)

| Test | Report | File |
|------|--------|------|
| Bandwidth Test | Bandwidth and jitter test results | [📄 View](./testing/test_results/tr_bandwidth_test_20240515.md) |
| Frame Integrity | Frame integrity test results | [📄 View](./testing/test_results/tr_frame_integrity_20240520.md) |
| Redundancy | Redundancy management test results | [📄 View](./testing/test_results/tr_redundancy_20240525.md) |
| Error Handling | Error handling test results | [📄 View](./testing/test_results/tr_error_handling_20240530.md) |

## ✅ Compliance Evidence (Markdown)

| Standard | Evidence | File |
|----------|----------|------|
| DO-178C | Objectives Matrix | [📄 View](./compliance/DO-178C_evidence/afdx_objectives_matrix.md) |
| DO-178C | Verification Report | [📄 View](./compliance/DO-178C_evidence/afdx_verification_report.md) |
| DO-330 | Tool Qualification | [📄 View](./compliance/DO-330_evidence/afdx_tool_qualification_report.md) |
| ARINC 664 | Compliance Report | [📄 View](./compliance/ARINC664_compliance/arinc664_compliance_report.md) |

## 📚 Standard References (Markdown Summaries)

| Standard | Summary | File |
|----------|---------|------|
| ARINC 664 | Aircraft Data Network, Part 7 | [📄 View](./references/ARINC664_spec.md) |
| Implementation Guide | AFDX implementation guidelines | [📄 View](./references/AFDX_implementation_guide.md) |
| Ethernet Comparison | Comparison with standard Ethernet | [📄 View](./references/ethernet_comparison.md) |

## 🔧 Validation Tools

### Makefile Commands
```bash
# Validate S1000D data modules
make validate-s1000d

# Validate BREX rules
make validate-brex

# Validate configuration files
make validate-config

# Validate Markdown files
make validate-md

# Run all validations
make validate-all
```

### Pre-commit Hooks
The repository includes pre-commit hooks for automatic validation:
- YAML linting
- JSON schema validation
- Markdown linting
- S1000D XML validation

## 🧩 CAUiX Templates

| Template | Purpose | Manifest |
|----------|---------|----------|
| `index-s1000d@v1.0.0` | Index S1000D artifacts | [📄 View](./CAUiX/manifests/index-s1000d@v1.0.0.manifest.yaml) |
| `validate-afdx@v1.0.0` | Validate AFDX configuration | [📄 View](./CAUiX/manifests/validate-afdx@v1.0.0.manifest.yaml) |
| `refactor-segregate@v1.0.0` | Domain segregation | [📄 View](./CAUiX/templates/refactor-segregate@v1.0.0.yaml) |

## 🔗 Cross-domain Links

- **ARINC 429**: Link to [ATA-42 A429](../a429/) bus documentation
- **System Integration**: Link to [ATA-42 OS](../../os/) integration procedures
- **Physical Layer**: Link to [EWIS · ATA-20](../../../AAA/ata/ATA-20/) wiring documentation
- **Cabin Systems**: Link to [ATA-46 CabinNet](../../../AAA/ata/ATA-46/CabinNet/) (domain segregation)

## 📊 Project Status

| Component | Status | Last Updated |
|-----------|--------|--------------|
| S1000D DMs | ✅ Complete | 2025-09-30 |
| Configuration | ✅ Complete | 2025-09-30 |
| Testing | ✅ Complete | 2025-09-30 |
| Compliance | ✅ Complete | 2025-09-30 |
| Validation | ✅ Complete | 2025-09-30 |
| CAUiX Integration | ✅ Complete | 2025-09-30 |

## ⚠️ Domain Segregation Notice

**Passenger_Information** has been moved to [ATA-46 CabinNet](../../../AAA/ata/ATA-46/CabinNet/) to ensure domain segregation. Non-critical cabin systems do not share failure domains with certified DAL-A/B systems. Data exchange occurs only via a secure gateway with whitelisted signals.

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial AFDX directory README |
| 0.2.0 | 2025-09-30 | IIS | Quality pass: S1000D structure, CAUiX integration |
