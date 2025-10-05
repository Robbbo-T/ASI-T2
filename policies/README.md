# Policies

Compliance policies and policy-as-code framework for the IDEALE-EU Federation.

## Overview

This directory contains the **federation-wide compliance policies** that govern data classification, export control, privacy, and security practices. These policies are **enforced as code** through CI/CD workflows and automated validation.

## Policy Documents

### 1. Data Classification

**File**: [DATA_CLASSIFICATION.md](./DATA_CLASSIFICATION.md)

Four-tier classification system for federation artifacts.

**Classification Levels**:
- **OPEN** 🌍: Public, no restrictions
- **SHARED** 🤝: Federation members only, NDA required
- **RESTRICTED** 🔒: Vetted organizations, bilateral agreements
- **CONTROLLED** 🚫: Export-controlled (ITAR/EAR/Dual-Use), off-repo

**Key Requirements**:
- All artifacts must declare `classification` in manifest
- CONTROLLED content cannot be committed to repository (hash references only)
- Classification changes require change control approval
- Automated enforcement via `.github/workflows/validate-manifests.yml`

**Usage**:
```yaml
# In index.extracted.yaml
classification: INTERNAL–EVIDENCE-REQUIRED
```

---

### 2. Export Control

**File**: [EXPORT_CONTROL.md](./EXPORT_CONTROL.md)

Compliance framework for ITAR, EAR, and EU Dual-Use regulations.

**Regulatory Frameworks**:
- **ITAR** (22 CFR 120-130): U.S. defense articles and services
- **EAR** (15 CFR 730-774): Dual-use items and emerging technologies
- **EU Dual-Use** (Regulation 2021/821): European dual-use export controls

**Required Declarations**:
```yaml
# In index.extracted.yaml
export_control:
  itar: false              # ITAR-controlled?
  ear: "NLR"               # EAR: NLR, EAR99, or ECCN (e.g., 9E003)
  eu_dual_use: "none"      # EU: none, or annex code (e.g., 9E003.a)
```

**Compliance Requirements**:
- Export control review required for RESTRICTED artifacts
- Empowered Export Control Officer approval for CONTROLLED
- Training mandatory for contributors handling controlled content
- Automated checks prevent CONTROLLED content in public repos

---

### 3. Privacy

**File**: [PRIVACY.md](./PRIVACY.md)

GDPR compliance and EU-U.S. Data Privacy Framework implementation.

**Key Topics**:
- **GDPR Compliance**: Legal basis, consent, data subject rights
- **EU-U.S. DPF**: Lawful transatlantic data transfers
- **Standard Contractual Clauses (SCCs)**: Alternative transfer mechanism
- **Privacy by Design**: Minimize, anonymize, pseudonymize
- **Data Subject Rights**: Access, rectification, erasure, portability

**Personal Data Handling**:
```yaml
# Mark artifacts containing personal data
metadata:
  contains_personal_data: true
  data_subjects: ["contributors", "testers"]
  legal_basis: "consent"  # or legitimate_interest, contract, etc.
  retention_period: "2_years"
```

**Privacy Requirements**:
- Privacy Impact Assessment (PIA) for high-risk processing
- Data Protection Officer (DPO) consultation
- Breach notification within 72 hours
- Anonymize/pseudonymize by default

---

### 4. Security

**File**: [SECURITY.md](./SECURITY.md)

Supply chain security, SLSA framework, and NIS2 cybersecurity requirements.

**Security Frameworks**:
- **SLSA Level 3+**: Build provenance and integrity
- **SBOM**: Software Bill of Materials (SPDX/CycloneDX)
- **Sigstore**: Keyless signing with OIDC
- **NIS2**: EU cybersecurity directive compliance

**Security Requirements**:
```yaml
# PAx packages must include
pax/
  ├── sbom/
  │   └── package.spdx.json      # SBOM required
  └── signatures/
      └── package.sig             # Sigstore signature
```

**Mandatory Practices**:
- Vulnerability scanning (Grype, Trivy) before release
- Cryptographic signing of all releases
- Dependency pinning and SBOM generation
- Incident response plan (see [SECURITY.md](../SECURITY.md))
- NIS2 incident reporting within 24 hours

---

## Policy Enforcement

### Automated Validation

Policies are enforced through CI/CD workflows:

| Policy | Workflow | Enforcement |
|--------|----------|-------------|
| Data Classification | `validate-manifests.yml` | FAIL if CONTROLLED in public repo |
| Export Control | `validate-manifests.yml` | WARN if missing declarations |
| Privacy | Manual review | REQUIRE DPO approval for personal data |
| Security | `sbom-attest.yml` | FAIL if missing SBOM/signatures |

### Manual Gates

Some policies require human review:

- **Export Control**: Empowered Officer approval for RESTRICTED/CONTROLLED
- **Privacy**: DPO consultation for high-risk processing
- **Security**: Incident Commander for security breaches
- **Classification**: Change Control Board for reclassification

---

## Policy-as-Code

Policies are implemented as executable checks:

### Example: Classification Check

```python
# In .github/workflows/validate-manifests.yml
def check_classification(manifest):
    classification = manifest.get("classification")
    
    if not classification:
        return "ERROR: Missing classification field"
    
    if classification == "CONTROLLED":
        # Check if in public repo
        if repo.visibility == "public":
            return "FAIL: CONTROLLED content in public repo"
    
    return "PASS"
```

### Example: Export Control Check

```python
def check_export_control(manifest):
    export = manifest.get("export_control", {})
    
    if export.get("itar") == True:
        # Require off-repo with hash reference
        if "hash_reference" not in manifest:
            return "FAIL: ITAR content requires hash reference"
    
    if export.get("ear") not in ["NLR", "EAR99"] and not export.get("ear", "").startswith("ECCN"):
        return "WARN: EAR classification unclear"
    
    return "PASS"
```

---

## Compliance Monitoring

### Audit Trail

All policy-relevant events are logged:

- Classification changes (with Change Control Board ticket)
- Export control reviews (with officer approval)
- Privacy assessments (with DPO sign-off)
- Security incidents (with IR case number)

### Compliance Dashboard

Track policy adherence across federation:

| Metric | Target | Current |
|--------|--------|---------|
| Artifacts with classification | 100% | [Auto-updated by CI] |
| Export control declarations | 100% | [Auto-updated by CI] |
| SBOM coverage (releases) | 100% | [Auto-updated by CI] |
| Vulnerability scan (weekly) | 100% | [Auto-updated by CI] |
| Security incidents (MTTD) | <24h | [Manual tracking] |

---

## Policy Updates

### Proposing Changes

To update a policy:

1. **RFC Process**: Open issue with `[RFC]` and `policy:` labels
2. **Impact Assessment**: Evaluate effects on existing artifacts
3. **Legal Review**: Consult with Legal Working Group
4. **TSC Approval**: Requires 2/3 majority vote
5. **Migration Period**: Minimum 6 months for breaking changes
6. **Documentation**: Update policy doc and CI workflows

### Version History

| Policy | Version | Date | Changes |
|--------|---------|------|---------|
| DATA_CLASSIFICATION.md | 1.0.0 | 2025-01-01 | Initial version |
| EXPORT_CONTROL.md | 1.0.0 | 2025-01-01 | Initial version |
| PRIVACY.md | 1.0.0 | 2025-01-01 | Initial version |
| SECURITY.md | 1.0.0 | 2025-01-01 | Initial version |

---

## Training & Certification

### Required Training

Contributors must complete training based on their role:

| Role | Training | Frequency |
|------|----------|-----------|
| All Contributors | Data Classification | Annually |
| RESTRICTED access | Export Control Basics | Annually |
| CONTROLLED access | ITAR/EAR Compliance | Quarterly |
| Data Processors | GDPR & Privacy | Annually |
| Security Team | Incident Response | Semi-annually |

### Certification

Empowered roles require certification:

- **Export Control Officer**: NCBFAA Export Compliance Certification
- **Data Protection Officer**: IAPP CIPP/E certification
- **Security Officer**: CISSP, CEH, or equivalent
- **Compliance Manager**: Regulatory compliance experience

---

## Regulatory References

### United States

- ITAR: 22 CFR 120-130 (https://www.pmddtc.state.gov/ddtc_public?id=ddtc_public_portal_itar_landing)
- EAR: 15 CFR 730-774 (https://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear)
- NIST SP 800-218: SSDF (https://csrc.nist.gov/publications/detail/sp/800-218/final)

### European Union

- GDPR: Regulation (EU) 2016/679 (https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- NIS2: Directive (EU) 2022/2555 (https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- Dual-Use: Regulation (EU) 2021/821 (https://eur-lex.europa.eu/eli/reg/2021/821/oj)

### International

- EU-U.S. Data Privacy Framework: https://www.dataprivacyframework.gov/
- FAA-EASA Bilateral: https://www.easa.europa.eu/en/document-library/bilateral-agreements/eu-usa
- SLSA Framework: https://slsa.dev/

---

## Support

### Policy Questions

- **Classification**: classification@ideale-eu.example
- **Export Control**: export-control@ideale-eu.example
- **Privacy/GDPR**: privacy@ideale-eu.example (DPO)
- **Security/NIS2**: security@ideale-eu.example (CISO)
- **General Compliance**: compliance@ideale-eu.example

### Incident Reporting

- **Security Incidents**: security@ideale-eu.example (24/7)
- **Privacy Breaches**: privacy@ideale-eu.example (within 72h)
- **Export Violations**: export-control@ideale-eu.example (immediate)
- **Non-Compliance**: compliance@ideale-eu.example

---

**Directory Version**: 1.0.0  
**Last Updated**: 2025-01-01  
**Maintained By**: IDEALE-EU Compliance Working Group

For policy questions, open a [GitHub Discussion](https://github.com/Robbbo-T/ASI-T2/discussions) or contact the appropriate functional contact above.
