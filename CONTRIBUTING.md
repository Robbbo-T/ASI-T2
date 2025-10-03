# Contributing to IDEALE-EU

Thank you for your interest in contributing to the IDEALE-EU federation! This guide will help you get started and ensure your contributions align with our standards, policies, and certification requirements.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Contribution Process](#contribution-process)
- [Repository Structure](#repository-structure)
- [Development Standards](#development-standards)
- [Testing & Validation](#testing--validation)
- [Documentation Requirements](#documentation-requirements)
- [Compliance & Policies](#compliance--policies)
- [Code Review](#code-review)
- [Community Guidelines](#community-guidelines)

---

## Getting Started

### Prerequisites

1. **GitHub Account**: Create an account at [github.com](https://github.com)
2. **Git**: Install Git on your local machine
3. **Contributor License Agreement (CLA)**: Sign the CLA (instructions below)
4. **Development Environment**: See [INSTALLATION.md](./INSTALLATION.md) for setup

### Sign the Contributor License Agreement (CLA)

Before your first contribution can be merged, you must sign our CLA:

**Individual Contributors:**
- Review the CLA: [link to CLA document]
- Sign electronically: [link to CLA signing service]

**Corporate Contributors:**
- Have your employer's legal team review the Corporate CLA
- Obtain authorized signature
- Email signed document to: legal@ideale-eu.example

### Find Something to Work On

- **Good First Issues**: Look for issues tagged `good-first-issue`
- **Help Wanted**: Check issues tagged `help-wanted`
- **Working Groups**: Join a working group (see [GOVERNANCE.md](./GOVERNANCE.md))
- **RFC Process**: Propose new features via Request for Comments

---

## Contribution Process

### 1. Fork and Clone

```bash
# Fork the repository via GitHub UI, then:
git clone https://github.com/YOUR-USERNAME/ASI-T2.git
cd ASI-T2
git remote add upstream https://github.com/Robbbo-T/ASI-T2.git
```

### 2. Create a Branch

Use descriptive branch names:

```bash
# Feature branches
git checkout -b feature/aaa-wing-optimization

# Bug fixes
git checkout -b fix/pax-manifest-validation

# Documentation
git checkout -b docs/update-bwb-q100-readme
```

### 3. Make Changes

Follow our [coding standards](#development-standards) and ensure:
- Changes are minimal and focused on a single issue
- All tests pass locally
- Documentation is updated if behavior changes
- Commit messages are clear and reference issues

### 4. Commit

Use conventional commit format:

```bash
git commit -m "feat(AAA): add wing optimization algorithm

- Implements topology optimization using QAIM
- Reduces weight by 12% in validation runs
- Adds S1000D data module DMC-BWB-AAA-57-001

Refs: #123
Evidence: UTCS-MI:v5.0:BWB-Q100:QOX:AAA:ATA-57:wing-opt-001
```

**Commit Message Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** feat, fix, docs, style, refactor, test, chore  
**Scopes:** Domain codes (AAA, IIS, etc.) or component names  
**Footer:** Issue references, evidence IDs, breaking changes

### 5. Test Locally

```bash
# Run relevant tests
python -m pytest PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/

# Validate manifests
python scripts/derive_struct_from_readmes.py --check

# Run linting
pre-commit run --all-files
```

### 6. Push and Create Pull Request

```bash
git push origin feature/aaa-wing-optimization
```

Then create a pull request via GitHub UI:
- Fill out the PR template completely
- Reference related issues
- Add screenshots/diagrams if applicable
- Request review from CODEOWNERS

---

## Repository Structure

IDEALE-EU follows a strict domain-based structure:

```
PRODUCTS/<LINE_OF_EFFORT>/<PRODUCT>/domains/<DOMAIN>/
├── ata/ATA-xx/           # S1000D documentation
├── cax/<DISCIPLINE>/     # Classical engineering (CAD, CFD, etc.)
├── qox/<PHASE>/          # Quantum optimization
├── pax/                  # Packaging & applications
│   ├── OB/               # On-board (embedded)
│   └── OFF/              # Off-board (cloud/edge)
├── index.extracted.yaml  # Domain manifest
└── README.md             # Domain overview
```

**Key Directories:**
- `FIELDS/`: Cross-cutting disciplines and curricula
- `ENVIRONMENTS/`: Physical and digital contexts
- `PRODUCTS/`: Deliverable systems and platforms
- `policies/`: Compliance and governance policies
- `Shared/_templates/`: Reusable templates and schemas

---

## Development Standards

### Code Quality

**Python:**
- PEP 8 compliance (enforced by `black`, `flake8`)
- Type hints for public APIs (`mypy` checked)
- Docstrings (Google style)
- Test coverage >80% for new code

**C/C++ (for embedded systems):**
- DO-178C coding standards (enforced by static analyzers)
- MISRA C compliance for safety-critical code
- Unit tests via CppUnit or Google Test

**MATLAB/Simulink:**
- MAAB style guidelines
- Model Advisor checks passing
- Code generation settings documented

### CAX Artifacts

**CAD Models:**
- Native format + STEP AP242 exchange
- Assembly structure documented
- PMI (Product Manufacturing Information) included
- Naming conventions: `<product>_<domain>_<component>_v<version>`

**CFD/FEA:**
- Mesh independence study included
- Solver settings documented
- Validation against experimental data (if available)
- Reproducible workflows via scripts

### QOX Artifacts

**Problem Definitions:**
- JSON format (see `/Shared/_templates/qox_problem_template.json`)
- Cost function clearly defined
- Constraints documented
- Baseline classical solution for comparison

**Runs:**
- Timestamped directories: `runs/<ISO8601>/`
- Input, output, and metrics captured
- UTCS evidence generated automatically
- Energy consumption logged (QPU or simulator)

### PAX Packaging

**Manifests:**
- JSON or YAML format
- Schema validation required (`index.extracted.schema.json`)
- All dependencies listed with versions
- Classification and export control fields mandatory

**SBOM (Software Bill of Materials):**
- SPDX or CycloneDX format
- Generated automatically via CI/CD
- Includes transitive dependencies
- Signed with Sigstore/Cosign

**Signatures & Attestations:**
- GPG or Sigstore signatures for all releases
- In-toto attestations for build provenance
- SLSA Level 3+ for production artifacts

---

## Testing & Validation

### Test Requirements

All code changes must include tests:

**Unit Tests:**
- Test individual functions/classes
- Mock external dependencies
- Fast execution (<1s per test)

**Integration Tests:**
- Test component interactions
- Use test fixtures for setup
- Validate against schemas

**System Tests:**
- End-to-end workflows (CAX → QOX → PAX → ATA)
- Performance benchmarks
- Stress testing for production code

### CI/CD Validation

Pull requests automatically run:
1. **Linting**: Code style, security scans
2. **Unit Tests**: All relevant test suites
3. **Manifest Validation**: Schema compliance, BREX rules
4. **SBOM Generation**: Dependency analysis
5. **Build**: Compilation (if applicable)

**Required Gates:**
- All CI checks must pass (green)
- No unresolved security vulnerabilities
- Test coverage ≥80% (new code)
- Documentation updated

---

## Documentation Requirements

### Code Documentation

**Python:**
```python
def optimize_wing_topology(mesh: Mesh, constraints: Dict[str, Any]) -> Topology:
    """Optimize wing topology using quantum annealing.
    
    Args:
        mesh: Input wing mesh with material properties
        constraints: Load cases and design constraints
        
    Returns:
        Optimized topology with weight/stiffness objectives
        
    Raises:
        ValueError: If mesh has no material definition
        
    Evidence:
        UTCS-MI:v5.0:BWB-Q100:QOX:AAA:ATA-57:wing-opt-001
    """
```

**C/C++:**
```c
/**
 * @brief Initialize ARINC-653 partition scheduler
 * 
 * @param config Partition configuration from XML
 * @return 0 on success, -1 on error
 * 
 * @safety DO-178C DAL-A
 * @certification CS-25 § 25.1309
 */
int init_partition_scheduler(const PartitionConfig* config);
```

### README Files

Every domain requires a README.md with:
- **Purpose**: What this domain covers
- **Structure**: Directory layout
- **Quick Start**: How to run/build/test
- **Standards**: Applicable ATA chapters, S1000D conventions
- **Contacts**: Maintainers and working group

### S1000D Documentation

All certification artifacts use S1000D:
- **DMRL**: Data Module Requirements List
- **BREX**: Business Rules Exchange (validation rules)
- **DMs**: Data Modules (individual documents)
- **ICN**: Illustrations/graphics
- **PM**: Publication Modules (assemblies)

**Naming Convention:**
```
DMC-<MODEL>-<DOMAIN>-<SYSTEM>-<SUBSYSTEM>-<DISASSCODE>-<INFOCODE>-<ITEMLOCATION>-<LANG>-<COUNTRY>
Example: DMC-BWB-AAA-57-10-01-00A-040A-A-EN-US.xml
```

---

## Compliance & Policies

### Data Classification

All artifacts must be tagged with classification level:

```yaml
classification: OPEN | SHARED | RESTRICTED | CONTROLLED
```

**OPEN**: Public internet, no restrictions  
**SHARED**: Registered federation members, NDA  
**RESTRICTED**: Vetted organizations, bilateral agreements  
**CONTROLLED**: Off-repo references only, export-controlled  

### Export Control

If your contribution involves export-controlled content:

1. **Do NOT commit CONTROLLED artifacts** to the repository
2. Tag in manifest:
```yaml
export_control:
  itar: true | false
  ear: "NLR" | "EAR99" | "ECCN-XXXXX"
  eu_dual_use: "none" | "ML-XX" | "dual-use-category"
```
3. Contact export-control@ideale-eu.example for guidance
4. Use off-repo pointers (hash references) for sensitive files

### Privacy & Data Protection

When handling personal data:
- Minimize data collection (only what's necessary)
- Document lawful basis (GDPR Article 6)
- Use EU-U.S. Data Privacy Framework for transatlantic transfers
- Implement privacy-by-design (anonymization, encryption)
- Honor data subject rights (access, deletion, portability)

### Security

Follow secure development practices:
- **Dependency scanning**: Automated vulnerability checks
- **Secrets management**: Never commit credentials, keys, tokens
- **Code signing**: Sign all releases with GPG or Sigstore
- **Incident response**: Report vulnerabilities to security@ideale-eu.example

---

## Code Review

### Review Process

1. **Automated Checks**: CI/CD runs automatically
2. **CODEOWNERS Review**: Assigned reviewers notified
3. **Technical Review**: TSC or working group members review
4. **Approval**: At least 1 approval from CODEOWNERS required
5. **Merge**: Squash merge preferred (clean history)

### What Reviewers Look For

- **Correctness**: Does it solve the problem?
- **Quality**: Follows coding standards, well-tested
- **Documentation**: Clear explanations, updated README
- **Compliance**: Meets classification, export control, privacy requirements
- **Evidence**: UTCS/QS traceability for CAX/QOX/PAX artifacts

### Addressing Feedback

- Respond to all comments (even if just "acknowledged")
- Push new commits (don't force-push during review)
- Re-request review after addressing feedback
- Be patient and professional

---

## Community Guidelines

### Communication Channels

- **GitHub Discussions**: Technical Q&A, brainstorming
- **Mailing Lists**: [ideale-air@lists.example.org], [ideale-council@...]
- **TSC Meetings**: Monthly, open to observers
- **Working Groups**: Domain-specific meetings (see GOVERNANCE.md)

### Be a Good Citizen

- **Search before asking**: Check existing issues, docs, discussions
- **Be respectful**: Follow our [Code of Conduct](./CODE_OF_CONDUCT.md)
- **Give credit**: Acknowledge prior work, cite sources
- **Help others**: Answer questions, review PRs, share knowledge

### Recognition

Active contributors are recognized through:
- Listed in `CONTRIBUTORS.md`
- Acknowledgment in release notes
- Invitation to working groups
- Annual contributor awards

---

## Questions?

- **General**: discussions@ideale-eu.example
- **Technical**: Relevant TSC or working group
- **Legal/IP**: legal@ideale-eu.example
- **Security**: security@ideale-eu.example
- **Conduct**: conduct@ideale-eu.example

---

**Thank you for contributing to a more sustainable, collaborative aerospace future!**

**Version:** 1.0.0  
**Last Updated:** 2025-01-01
