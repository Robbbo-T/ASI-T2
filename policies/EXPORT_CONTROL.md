# Export Control Policy

**Version:** 1.0.0  
**Effective Date:** 2025-01-01  
**Owner:** IDEALE Council  
**Export Control Officer:** export-control@ideale-eu.example

---

## Purpose

This policy ensures IDEALE-EU compliance with export control regulations across US, EU, and international jurisdictions. Export controls restrict transfer of certain technologies, software, and data to foreign nationals or countries.

---

## Regulatory Framework

### United States

**International Traffic in Arms Regulations (ITAR)**
- Authority: US State Department, Directorate of Defense Trade Controls (DDTC)
- Scope: Defense articles and services (USML Categories I-XXI)
- Licensing: Required for export, re-export, or deemed export
- **IDEALE-EU Policy**: No ITAR content in public repositories

**Export Administration Regulations (EAR)**
- Authority: US Commerce Department, Bureau of Industry and Security (BIS)
- Scope: Dual-use items (CCL Categories 0-9)
- Classification: ECCN (Export Control Classification Number)
- Licensing: Depends on destination, end-use, end-user
- **IDEALE-EU Policy**: EAR items tagged with ECCN, licensed distribution tracked

### European Union

**Dual-Use Regulation (EU 2021/821)**
- Scope: Items usable for civilian and military purposes
- Categories: 0-9 (aligned with Wassenaar Arrangement)
- Controls: Export, transit, brokering, technical assistance
- **IDEALE-EU Policy**: EU Dual-Use items tagged, export authorizations documented

### International

**Wassenaar Arrangement**
- Multilateral export control regime (42 participating states)
- Covers conventional arms and dual-use goods/technologies

**Missile Technology Control Regime (MTCR)**
- Restricts missiles, drones, and related technology

---

## IDEALE-EU Export Control Lanes

### Lane 1: No License Required (NLR) ✅

**Criteria:**
- Not on ITAR USML
- EAR99 or specifically exempted ECCN
- Not on EU Dual-Use Annex I
- Published, publicly available, or fundamental research

**Examples:**
- Open-source software (Apache, MIT licenses)
- Published academic papers
- Basic aerodynamics theory
- Non-proprietary CAD models (STEP AP242 exchange)

**Marking:**
```yaml
export_control:
  itar: false
  ear: "NLR"
  eu_dual_use: "none"
```

**Distribution:** Public repositories, no restrictions

---

### Lane 2: EAR-Controlled / EU Dual-Use 📋

**Criteria:**
- Specific ECCN (e.g., 9E991, 3E001, 5A992)
- EU Dual-Use Annex I category
- License **may** be required depending on:
  - Destination country (Country Group D:1, E:1, E:2)
  - End-use (military, WMD, terrorist)
  - End-user (denied parties list)

**Examples:**
- High-performance computing software (ECCN 4E001)
- Encryption software >1024-bit (ECCN 5D002)
- CFD software (ECCN 9D004)
- Avionics software (ECCN 7D003)
- Composite materials technology (EU Cat 1C010)

**Marking:**
```yaml
export_control:
  itar: false
  ear: "9D004"  # Specific ECCN
  ear_note: "See 15 CFR 774 Supplement No. 1"
  eu_dual_use: "1C010"
  license_exceptions:
    - "TSU"  # Technology and Software Unrestricted
```

**Distribution:**
- SHARED or RESTRICTED classification
- Export destination tracked
- License exception applicability documented
- If no exception applies, obtain export license before transfer

---

### Lane 3: ITAR-Controlled (Defense Articles) 🚫

**Criteria:**
- Listed on USML (United States Munitions List)
- Categories: I (firearms), VIII (aircraft), X (spacecraft), XV (spacecraft)
- **Specific to IDEALE-EU:**
  - Category VIII(h): Military aircraft engines, parts
  - Category VIII(i): Military flight control systems
  - Category XI(c): Military electronics (radar, targeting)
  - Category XV: Spacecraft and related articles

**IDEALE-EU Policy:** **ITAR content NEVER enters the repository.**

**Examples:**
- Military aircraft weapon systems
- Classified propulsion technology
- Secure communications (government-specific)
- Anti-tamper mechanisms

**Marking:**
```yaml
export_control:
  itar: true
  usml_category: "VIII(h)"
  classification: CONTROLLED
  storage:
    location: "off-repo"
    hash_sha256: "a3f8b7c6d9e4..."
    access: "export-control@ideale-eu.example"
```

**Access:**
- Requires DDTC-authorized export license
- US Person restriction (citizenship/permanent residency check)
- Cleared facility required

---

### Lane 4: Cryptography (Special Rules) 🔐

**Regulatory Complexity:**
- US: EAR Category 5 Part 2 (encryption items)
- EU: Dual-Use Annex I, Category 5A002/5D002
- Varies by key length, algorithm, and use case

**Common Scenarios:**

| Technology | US EAR | EU Dual-Use | License Required? |
|------------|--------|-------------|-------------------|
| AES-256 (general use) | 5D002 | 5A002 | License exception (TSU) |
| RSA >1024 bit | 5D002 | 5A002 | Notification + exception |
| Post-quantum (Dilithium, Kyber) | 5D002 | 5A002 | Case-by-case |
| Custom military crypto | ITAR Cat XIII | Not dual-use | Always ITAR |

**IDEALE-EU Requirements:**
- **Notification**: File BIS "Encryption Registration Number" (ERN) for products with encryption
- **Documentation**: Maintain crypto inventory with key lengths, algorithms
- **Export**: Use license exception (TSU, ENC) where applicable, obtain license otherwise

**Marking:**
```yaml
export_control:
  cryptography: true
  algorithms:
    - "AES-256-GCM"
    - "Ed25519"
  ear: "5D002"
  eu_dual_use: "5A002"
  license_exception: "TSU"
  bis_notification: "ERN-XXXXXX"  # If applicable
```

---

## Deemed Export Rules

**Definition:** Release of controlled technology to foreign nationals **within the same country** is considered an export.

**Examples:**
- Sharing ITAR-controlled data with non-US person in US facility
- Allowing EU national to access EAR-controlled software in US without license

**IDEALE-EU Policy:**
- Contributor nationality tracked for ITAR/RESTRICTED access
- Multi-factor authentication for RESTRICTED repositories
- Training required for contributors accessing controlled content

---

## End-Use and End-User Screening

Before releasing controlled technology, verify:

### Destination Country
- **Red flags**: Embargoed countries (Cuba, Iran, North Korea, Syria, Russia, Belarus)
- **Caution**: Country Groups D:1, E:1, E:2 (restricted destinations)

### End-Use
- Military application? → License likely required
- Nuclear, chemical, biological weapons? → Denied
- Missile/drone technology? → MTCR restrictions apply

### End-User
- Check denied parties lists:
  - BIS Denied Persons List
  - BIS Entity List
  - OFAC SDN (Specially Designated Nationals)
  - EU Consolidated Sanctions List

**Automated Screening:**
- CI/CD pipeline checks contributor affiliations
- Denied party screening for RESTRICTED access requests

---

## Contributions from Non-US/EU Nationals

**Open Contributions (Lane 1: NLR):**
- No restrictions, all nationalities welcome

**Controlled Contributions (Lane 2-4):**
- **ITAR**: US Person only (citizen, permanent resident, protected person)
- **EAR/Dual-Use**: Case-by-case, depends on ECCN and destination
- **Process:**
  1. Contributor discloses nationality
  2. Export Control Officer reviews applicability
  3. If license required, contributor or sponsor obtains authorization
  4. Access granted after approval

---

## Export Authorization Requests

**When Required:**
- Distributing EAR/dual-use items to restricted destinations
- Providing technical assistance (training, consulting) involving controlled tech
- Re-exporting items received from US or EU

**Procedure:**
1. Submit export control questionnaire to export-control@ideale-eu.example
2. Include: item description, ECCN/USML, destination, end-use, end-user
3. Export Control Officer determines licensing requirement
4. If license needed, assist with application to BIS, DDTC, or EU authority
5. Do NOT proceed with export until license granted

**Timeline:**
- BIS (EAR): 4-6 weeks
- DDTC (ITAR): 60-120 days
- EU Member State: Varies (2-8 weeks)

---

## Technical Assistance and Training

Providing technical support to non-US/EU persons may be an export:
- Live training on controlled software
- Debugging sessions involving ITAR data
- Consulting on export-controlled designs

**Best Practices:**
- Use NLR/OPEN materials for training when possible
- Document nationality of trainees
- Obtain licenses if controlled tech discussed

---

## Penalties for Violations

Export control violations carry severe penalties:
- **Civil**: Up to $1.2M per violation (BIS), €500K (EU)
- **Criminal**: Up to 20 years imprisonment (ITAR), 10 years (EAR)
- **Administrative**: Denied export privileges, debarment

**IDEALE-EU Consequences:**
- Immediate suspension of access
- Reporting to authorities (mandatory for ITAR)
- Permanent ban from federation

---

## Compliance Program

### Training
- Annual export control training for all contributors (RESTRICTED access)
- Specialized training for TSC, working group leads
- Onboarding module for new members

### Audits
- Quarterly review of CONTROLLED artifact references
- Annual third-party export control audit
- Post-violation forensics and remediation

### Documentation
- Export Control Manual (internal, RESTRICTED)
- Decision logs for classification determinations
- License applications and approvals archive

---

## Contacts

**Export Control Officer:**
- Email: export-control@ideale-eu.example
- PGP: 3FA5 1C2D 7B8E 9A0C 4D2F  8E1A 6B7C 2D1E 5F6A 9B3C
- Phone: +32 2 555 1234

**Regulatory Authorities:**
- **US BIS**: publicaffairs@bis.doc.gov, https://www.bis.doc.gov
- **US DDTC**: DDTCPublicAffairs@state.gov, https://www.pmddtc.state.gov
- **EU**: Contact your Member State's export control authority

---

## References

- [DATA_CLASSIFICATION.md](./DATA_CLASSIFICATION.md) - Classification levels
- [SECURITY.md](./SECURITY.md) - Security controls for CONTROLLED data
- US EAR: https://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear
- ITAR: https://www.pmddtc.state.gov/?id=ddtc_public_portal_itar_landing
- EU Dual-Use: https://eur-lex.europa.eu/eli/reg/2021/821/oj/eng

---

**Version History:**
- **1.0.0** (2025-01-01): Initial export control policy
