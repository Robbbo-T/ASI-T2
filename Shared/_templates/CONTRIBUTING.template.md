# Contributing to {DOMAIN_NAME} ({DOMAIN_CODE})

Thank you for your interest in contributing to the **{DOMAIN_NAME}** domain of **{PRODUCT_NAME}**!

This guide supplements the main [CONTRIBUTING.md](../../../CONTRIBUTING.md) with domain-specific requirements.

---

## Domain Overview

**Domain Code:** {DOMAIN_CODE} (e.g., AAA, IIS, LCC)  
**Classification:** {CLASSIFICATION}  
**Working Group:** {WG_NAME}  
**Maintainers:** {MAINTAINER_NAMES}

**Scope:**
{Brief description of domain scope, e.g.:
- Airframes & Aerodynamics: Wing/fuselage structures, aerodynamic analysis
- Integrated Intelligence & Software: Avionics software, ML models, data processing
}

---

## Domain Structure

```
domains/{DOMAIN_CODE}/
├── ata/ATA-xx/           # S1000D documentation
│   ├── DMRL.xml          # Data Module Requirements List
│   ├── BREX.xml          # Business Rules Exchange
│   └── DMs/              # Data Modules
├── cax/{DISCIPLINE}/     # Classical engineering
│   ├── CAD/              # Native CAD + STEP AP242
│   ├── CAE/              # FEA/MBSE
│   ├── CFD/              # Meshes, setup, post
│   └── manifests/        # Dataset manifests
├── qox/{PHASE}/          # Quantum optimization
│   ├── problems/         # Problem definitions (JSON)
│   ├── runs/             # Timestamped run logs
│   └── benchmarks/       # Baselines
├── pax/                  # Packaging & applications
│   ├── OB/               # On-board (embedded)
│   └── OFF/              # Off-board (cloud/edge)
├── index.extracted.yaml  # Domain manifest
└── README.md             # This file
```

---

## Getting Started

### 1. Set Up Development Environment

```bash
# Clone repository
git clone https://github.com/Robbbo-T/ASI-T2.git
cd ASI-T2/PRODUCTS/{PRODUCT}/{PLATFORM}/domains/{DOMAIN_CODE}/

# Install domain-specific tools
{installation-commands}

# Verify setup
{verification-commands}
```

### 2. Review Domain Standards

**Required Reading:**
- [ ] ATA chapter mapping (see `ata/README.md`)
- [ ] S1000D BREX rules (see `ata/ATA-xx/BREX.xml`)
- [ ] CAX naming conventions (see `cax/README.md`)
- [ ] Export control guidance (see `policies/EXPORT_CONTROL.md`)

---

## Contribution Workflow

### Step 1: Find or Create an Issue

- Browse [existing issues](https://github.com/Robbbo-T/ASI-T2/issues?q=is%3Aissue+label%3A{DOMAIN_CODE})
- Look for `good-first-issue` or `help-wanted` tags
- If proposing new work, create an issue with `[{DOMAIN_CODE}]` prefix

### Step 2: Create a Branch

```bash
git checkout -b feature/{domain-code}-{short-description}
# Example: feature/aaa-wing-optimization
```

### Step 3: Make Changes

**Follow Domain Standards:**

#### ATA (Documentation)
```bash
# Create new data module
cp ata/ATA-xx/DMs/DMC-TEMPLATE.xml ata/ATA-xx/DMs/DMC-{your-dm}.xml
# Edit with XML editor (oXygen, Arbortext)
# Validate against BREX
```

#### CAX (Engineering)
```bash
# Add CAD model
# - Native format: {tool-specific}
# - Exchange: STEP AP242 (mandatory)
cax/CAD/{component}/model.step

# Add analysis
cax/CFD/{analysis}/
  ├── setup.json         # Solver settings
  ├── mesh.msh           # Mesh file
  ├── results/           # Post-processing
  └── manifest.yaml      # Dataset manifest
```

#### QOX (Quantum)
```bash
# Define problem
qox/{PHASE}/problems/{problem-name}.json

# Run optimization (generates timestamped directory)
python scripts/run_qox.py --problem {problem-name}

# Results appear in:
qox/{PHASE}/runs/{ISO8601-timestamp}/
```

#### PAX (Packaging)
```bash
# Create package manifest
pax/OFF/{package-name}/manifest.yaml

# Generate SBOM
{sbom-generation-command}

# Sign artifact
cosign sign {artifact}
```

### Step 4: Update Domain Manifest

Edit `index.extracted.yaml` to reflect your changes:

```yaml
schema_version: 1.0.0
product: {PRODUCT}
platform: {PLATFORM}
domain: {DOMAIN_CODE}
classification: {CLASSIFICATION}
standards:
  - S1000D
  - STEP-AP242
  - SPDX
artifacts:
  - type: "cax:cad"
    path: "cax/CAD/{your-component}/model.step"
    description: "{Brief description}"
    hash_sha256: "{sha256sum}"
licenses:
  code: Apache-2.0
  docs: CC-BY-4.0
  hardware: CERN-OHL-S-2.0
export_control:
  itar: false
  ear: "NLR"
  eu_dual_use: "none"
contacts:
  - "{your-email}"
```

### Step 5: Test Locally

```bash
# Validate manifest
python scripts/derive_struct_from_readmes.py --check

# Run domain-specific tests
{test-commands}

# Lint
pre-commit run --all-files
```

### Step 6: Submit Pull Request

```bash
git add .
git commit -m "feat({domain-code}): {concise description}

- {bullet point 1}
- {bullet point 2}

Refs: #{issue-number}
Evidence: UTCS-MI:v5.0:{PRODUCT}:{domain-code}:{artifact-id}"

git push origin feature/{domain-code}-{description}
```

Then create PR via GitHub UI:
- Title: `[{DOMAIN_CODE}] {Description}`
- Reference issue(s)
- Fill out PR template
- Request review from `@{domain-maintainers}`

---

## Domain-Specific Requirements

### {DOMAIN_CODE}-Specific Standards

{Insert domain-specific technical requirements, e.g.:

**AAA (Airframes & Aerodynamics):**
- CAD models: CATIA V5 or NX native + STEP AP242
- CFD: Mesh independence study required
- Loads: Reference CS-25 § 25.301-25.341

**IIS (Software):**
- Code: DO-178C DAL-{level} coding standards
- Tests: 80% coverage minimum (MC/DC for DAL-A)
- Security: Static analysis with no critical findings

**LCC (Controls):**
- Models: MATLAB/Simulink R2021b+
- Code gen: MISRA C compliance
- V&V: Closed-loop simulation required
}

---

## Review Process

### Automatic Checks (CI/CD)
- [ ] Manifest schema validation
- [ ] BREX compliance (S1000D)
- [ ] SBOM generation
- [ ] Security scans
- [ ] Export control markers

### Human Review
- [ ] Domain maintainer approval (CODEOWNERS)
- [ ] TSC review (if cross-domain impact)
- [ ] Export control officer (if RESTRICTED/CONTROLLED)

**Timeline:**
- Initial review: Within 7 days
- Follow-up: Within 3 days of updates
- Merge: After all checks pass + 1+ approval

---

## Communication Channels

### Domain-Specific
- **Mailing List:** {domain-code}-wg@ideale-eu.example
- **Meetings:** {schedule}
- **Chat:** [Discord/Slack channel]

### General IDEALE-EU
- **Issues:** GitHub Issues with `[{DOMAIN_CODE}]` tag
- **Discussions:** GitHub Discussions
- **RFCs:** Submit to `rfcs/` directory

---

## Recognition

Active contributors to this domain are recognized through:
- Listed in `domains/{DOMAIN_CODE}/CONTRIBUTORS.md`
- Acknowledgment in release notes
- Domain badge on member profile
- Invitation to working group meetings

---

## Questions?

- **Domain maintainers:** {maintainer-emails}
- **Working group lead:** {wg-lead-email}
- **TSC:** {tsc-email}
- **General:** discussions@ideale-eu.example

---

**Version:** 1.0.0  
**Last Updated:** {DATE}  
**Domain:** {DOMAIN_CODE} - {DOMAIN_NAME}
