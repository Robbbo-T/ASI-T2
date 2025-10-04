# Data Classification Policy

**Version:** 1.0.0  
**Effective Date:** 2025-01-01  
**Owner:** IDEALE Council  
**Review Cycle:** Annual

---

## Purpose

This policy establishes a consistent data classification scheme for the IDEALE-EU federation, ensuring appropriate handling of artifacts based on sensitivity, export control requirements, and data protection obligations.

---

## Classification Levels

### OPEN 🌍

**Definition:** Information that can be freely shared with the public.

**Characteristics:**
- No confidentiality requirements
- No export control restrictions
- May be published on public internet
- No access controls required

**Examples:**
- Published research papers
- Open-source software (Apache-2.0, MIT)
- Public documentation (CC-BY-4.0)
- Marketing materials
- Public APIs and standards

**Handling:**
- Store in public GitHub repositories
- No encryption required (HTTPS for transport)
- No access logs required
- May be cached by CDNs

**Marking:**
```yaml
classification: OPEN
```

---

### SHARED 🤝

**Definition:** Information shared with registered IDEALE-EU members under NDA.

**Characteristics:**
- Limited to federation members
- Requires signed Non-Disclosure Agreement (NDA)
- May include pre-release features, designs, or data
- No export control restrictions (but may have partner-specific terms)

**Examples:**
- Early-stage designs (before public release)
- Member-contributed datasets (with sharing permissions)
- Draft RFCs and proposals
- Meeting minutes (non-public sessions)
- Beta releases and test builds

**Handling:**
- Private GitHub repositories (member access only)
- TLS 1.3 encryption for transport
- Access control lists (ACLs) enforced
- Audit logging enabled
- May be time-limited (e.g., embargo until public release)

**Marking:**
```yaml
classification: SHARED
data_sharing:
  nda_required: true
  members_only: true
  embargo_until: "2025-06-01"  # Optional
```

**Access Request:**
- Submit to access-control@ideale-eu.example
- Provide: name, affiliation, intended use
- Approval by working group lead or TSC

---

### RESTRICTED 🔒

**Definition:** Sensitive information requiring bilateral agreements and vetted access.

**Characteristics:**
- Requires formal agreement beyond NDA (e.g., BPRA, MTA, DUA)
- Limited to vetted organizations (government, research, certified industry)
- May include proprietary methods, unpublished research, or competition-sensitive data
- Subject to audit and compliance checks

**Examples:**
- Proprietary CAD models (before STEP export available)
- Unpublished certification test data
- Confidential business information (CBI)
- Government-funded research under publication restrictions
- Third-party licensed components (redistribution prohibited)

**Handling:**
- Off-repo or private repo with strict ACLs
- Encryption at rest (AES-256-GCM) and in transit (TLS 1.3)
- Multi-factor authentication (MFA) required
- Audit logging with tamper-evident seals
- Data Loss Prevention (DLP) monitoring
- Access reviews every 90 days

**Marking:**
```yaml
classification: RESTRICTED
access_control:
  agreement_type: "BPRA"  # Bilateral Partnership and Research Agreement
  authorized_orgs:
    - "OrgA"
    - "OrgB"
  expiration: "2026-12-31"
  audit_required: true
```

**Access Request:**
- Submit to legal@ideale-eu.example
- Requires: executed agreement, justification, compliance attestation
- Approval by Council or TSC chair

---

### CONTROLLED 🚫

**Definition:** Export-controlled or highly sensitive information not stored in the repository.

**Characteristics:**
- Subject to ITAR, EAR, or EU Dual-Use Regulation
- **Never committed to any repository** (even private)
- Referenced by cryptographic hash only
- Requires government authorization for access (e.g., export license)

**Examples:**
- ITAR-controlled defense articles
- EAR-controlled encryption software (>1024-bit RSA, AES-256)
- EU Dual-Use Category 5 (cryptography, cybersecurity tools)
- Classified government data
- Nuclear-related designs or materials
- Biological/chemical hazard information

**Handling:**
- **Off-repo storage only** (secure file transfer, escrow, HSM)
- Hash pointer in manifest:
  ```yaml
  classification: CONTROLLED
  export_control:
    itar: true
    eccn: "9E991"
    license_required: true
  storage:
    location: "off-repo"
    hash_sha256: "a3f8b7c6d9e4..."
    access_procedure: "contact export-control@ideale-eu.example"
  ```
- Air-gapped systems preferred
- Access restricted to cleared personnel
- Full audit trail (who, what, when, why)

**Access Request:**
- Contact export-control@ideale-eu.example
- Requires: export license (if applicable), security clearance, need-to-know justification
- Approval by Council + government authority (if applicable)

---

## Classification Guidelines

### How to Classify New Artifacts

**Step 1: Sensitivity Assessment**
- Is this information already public? → OPEN
- Does it contain proprietary or unpublished work? → SHARED or RESTRICTED
- Is it export-controlled? → CONTROLLED

**Step 2: Export Control Review**
- Check US EAR CCL (Commerce Control List)
- Check EU Dual-Use Annex I
- Check ITAR USML (if defense-related)
- If uncertain, consult export-control@ideale-eu.example

**Step 3: Personal Data Check**
- Does it contain personal data (names, emails, biometrics)?
- If yes, apply GDPR/privacy requirements (see [PRIVACY.md](./PRIVACY.md))
- Consider anonymization or pseudonymization

**Step 4: Partner Agreements**
- Are there third-party license restrictions?
- Does a contributor's employer require NDA?
- Are there confidentiality obligations from funded research?

**Step 5: Document in Manifest**
```yaml
classification: OPEN | SHARED | RESTRICTED | CONTROLLED
rationale: "Brief explanation of classification"
classified_by: "Name <email>"
classification_date: "2025-01-01"
declassification_date: "2027-01-01"  # Optional
```

---

## Classification Tags in Code

### YAML Front-Matter (Markdown/Documentation)
```yaml
---
classification: SHARED
data_sharing:
  nda_required: true
  embargo_until: "2025-06-01"
---
```

### JSON Manifest (CAX/QOX/PAX)
```json
{
  "metadata": {
    "classification": "OPEN",
    "export_control": {
      "itar": false,
      "ear": "NLR",
      "eu_dual_use": "none"
    }
  }
}
```

### Source Code Comments
```python
# Classification: SHARED
# Data Sharing: Member NDA required
# Embargo: 2025-06-01
```

---

## Declassification Process

Artifacts may be downgraded (e.g., RESTRICTED → SHARED → OPEN) when:
- Embargo periods expire
- Technology becomes publicly available elsewhere
- Export control restrictions are lifted
- Research is published in peer-reviewed venues

**Procedure:**
1. Author/maintainer submits declassification request to TSC
2. TSC reviews export control status, partner agreements, and confidentiality
3. If approved, update classification tags and move to appropriate repo
4. Document in changelog and issue tracker

---

## Penalties for Misclassification

**Under-classification** (marking CONTROLLED as OPEN):
- Immediate removal from repositories
- Incident report to Council and authorities
- Possible legal liability (export control violations)
- Contributor access suspended pending investigation

**Over-classification** (marking OPEN as CONTROLLED):
- Hinders collaboration and slows development
- May be challenged by TSC
- Author must justify classification or downgrade

---

## Data Residency Requirements

### EU Data Residency
For GDPR compliance, personal data of EU data subjects must:
- Be stored in EU/EEA or adequacy-approved countries
- Use EU-U.S. Data Privacy Framework for transatlantic transfers
- Implement Standard Contractual Clauses (SCCs) where needed

See [PRIVACY.md](./PRIVACY.md) for details.

### US Government Data
Data generated under US government contracts may require:
- Storage in US-based systems
- FedRAMP-certified cloud services
- Compliance with FAR 52.204-21 (Basic Safeguarding of Covered Contractor Information Systems)

---

## Automated Classification Checks

CI/CD pipelines enforce classification rules:

```yaml
# .github/workflows/classification-check.yml
name: Classification Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check for CONTROLLED markers
        run: |
          if grep -r "CONTROLLED\|ITAR\|SECRET" --include="*.md" --include="*.yaml" .; then
            echo "ERROR: CONTROLLED content detected in public repo"
            exit 1
          fi
      
      - name: Validate classification tags
        run: |
          python scripts/validate_classification.py --strict
```

**Automated Actions:**
- **FAIL builds** if CONTROLLED content detected
- **WARN** if classification tag missing
- **REQUIRE** export-control team review for RESTRICTED changes

---

## References

- [EXPORT_CONTROL.md](./EXPORT_CONTROL.md) - Export control lanes
- [PRIVACY.md](./PRIVACY.md) - Personal data protection
- [SECURITY.md](./SECURITY.md) - Information security requirements
- [CHARTER.md](../CHARTER.md) - Federation principles

**Regulatory Sources:**
- US: [EAR § 734](https://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear)
- EU: [Dual-Use Regulation (EU 2021/821)](https://eur-lex.europa.eu/eli/reg/2021/821/oj/eng)
- ITAR: [22 CFR Parts 120-130](https://www.pmddtc.state.gov/?id=ddtc_public_portal_itar_landing)

---

**Questions?**
- Policy interpretation: governance@ideale-eu.example
- Export control: export-control@ideale-eu.example
- Data privacy: privacy@ideale-eu.example

**Version History:**
- **1.0.0** (2025-01-01): Initial data classification policy
