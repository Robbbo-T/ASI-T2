# Security Policy

**Version:** 1.0.0  
**Last Updated:** 2025-01-01  
**Contact:** security@ideale-eu.example

---

## Overview

IDEALE-EU takes security seriously across all layers:
- **Safety-critical systems**: Aviation, space, marine platforms
- **Supply chain integrity**: SBOM, provenance, attestations
- **Infrastructure**: CI/CD, build systems, artifact repositories
- **Data protection**: Privacy, encryption, access control
- **Export control**: Compliance with ITAR, EAR, EU dual-use regulations

---

## Supported Versions

Security updates are provided for:

| Product/Component | Version | Security Support |
|-------------------|---------|------------------|
| BWB-Q100 (all domains) | 0.x.x (pre-release) | ✅ Active development |
| AQUA-OS | 0.x.x | ✅ Active development |
| QAIM | 0.x.x | ✅ Active development |
| Legacy scripts | <1.0 | ⚠️ Best-effort |

**End-of-Life Policy:**
- Active development: Full security support
- Maintenance mode: Critical vulnerabilities only
- Archived: No security updates (migration guidance provided)

---

## Reporting a Vulnerability

### Coordinated Disclosure

We follow a **90-day coordinated disclosure** policy:

1. **Report privately** to security@ideale-eu.example
2. We acknowledge within **48 hours**
3. We provide status updates every **7 days**
4. We aim to release a fix within **90 days** (or explain why not)
5. **Public disclosure** after fix is released or 90 days, whichever comes first

### How to Report

**Email:** security@ideale-eu.example

**PGP Key:** 3A94 1F2B 7C8E 5D6A 9B1C  2F3E 8A7D 4C5B 1E2F 3A9C

**Include in Your Report:**
- Description of the vulnerability
- Steps to reproduce (or proof-of-concept)
- Affected versions/components
- Potential impact (confidentiality, integrity, availability)
- Suggested remediation (optional)
- Whether you plan to publish independently

**Do NOT:**
- File public issues for security vulnerabilities
- Share exploit details publicly before disclosure date
- Exploit vulnerabilities beyond proof-of-concept testing

### What to Expect

**Within 48 hours:**
- Acknowledgment of receipt
- Initial severity assessment (Critical, High, Medium, Low)
- Assignment of CVE identifier (if applicable)

**Within 7 days:**
- Detailed analysis and validation
- Proposed remediation plan
- Estimated timeline for fix

**Ongoing:**
- Weekly status updates
- Coordination on disclosure date
- Credit in security advisory (if desired)

---

## NIS2 Incident Reporting

For incidents affecting EU entities or critical infrastructure, we comply with **NIS2 Directive (EU 2022/2555)**:

**Reporting Thresholds:**
- **Early warning** (24h): Incident under investigation, significant impact suspected
- **Incident notification** (72h): Confirmed incident, detailed assessment
- **Final report** (1 month): Root cause, remediation, lessons learned

**Contact:**
- Primary: security@ideale-eu.example
- NIS2 Coordinator: nis2@ideale-eu.example
- Phone (24/7): [hotline to be established]

**Reportable Incidents:**
- Unauthorized access to CONTROLLED artifacts
- Data breaches involving personal information
- Ransomware or destructive attacks
- Supply chain compromises (e.g., malicious dependencies)
- Denial of service affecting critical operations

---

## Security Requirements

### For Contributors

**Before Submitting Code:**
- [ ] No hardcoded secrets (keys, passwords, tokens)
- [ ] Dependencies scanned for known vulnerabilities
- [ ] Input validation for all external data
- [ ] Proper error handling (no sensitive info in logs)
- [ ] Security-relevant changes reviewed by @security-team

**Sensitive Areas (Extra Review Required):**
- Authentication/authorization logic
- Cryptographic implementations
- Network protocols and APIs
- File uploads and processing
- SQL/database queries
- ARINC-653 partition isolation (AQUA-OS)

### For Deployments

**Production Systems:**
- [ ] SLSA Level 3+ provenance for all artifacts
- [ ] SBOM (SPDX or CycloneDX) attached to every release
- [ ] Artifacts signed with Sigstore or GPG
- [ ] No DEBUG/TEST code in production builds
- [ ] Least privilege (containers run as non-root)
- [ ] Read-only filesystems where possible
- [ ] Network segmentation (partitions, namespaces)
- [ ] Audit logging enabled

**CI/CD Pipelines:**
- [ ] Branch protection (require reviews, status checks)
- [ ] Secret scanning (GitHub Advanced Security or equivalent)
- [ ] Dependency updates (Dependabot or Renovate)
- [ ] Container scanning (Trivy, Clair, Snyk)
- [ ] Code scanning (CodeQL, Semgrep, SonarQube)

---

## Supply Chain Security

### SBOM (Software Bill of Materials)

**Required for all releases:**
- Format: SPDX 2.3+ or CycloneDX 1.4+
- Depth: Include transitive dependencies
- License info: All components identified
- Vulnerabilities: Known CVEs listed

**Generation:**
```bash
# Python
pip-audit --format=cyclonedx > sbom.json

# Node.js
npm run sbom:generate  # uses @cyclonedx/cyclonedx-npm

# Container
syft <image> -o spdx-json > sbom.json
```

### Provenance & Attestations

**SLSA Framework:**
- **Level 1**: Documented build process
- **Level 2**: Hosted build service (GitHub Actions)
- **Level 3**: Hermetic, reproducible builds
- **Level 4**: Two-party review (required for safety-critical code)

**Sigstore Integration:**
```bash
# Sign artifact
cosign sign <artifact>

# Generate attestation
cosign attest --predicate=sbom.json <artifact>

# Verify
cosign verify --certificate-identity=... <artifact>
```

### Dependency Management

**Approved Registries:**
- PyPI (Python)
- npm registry (JavaScript)
- Maven Central (Java)
- crates.io (Rust)
- Docker Hub / GHCR (Containers)

**Prohibited Actions:**
- Using dependencies from untrusted sources
- Vendoring without license review
- Downgrading dependencies to avoid vulnerability fixes
- Ignoring security advisories without documented risk acceptance

---

## Cryptography

### Approved Algorithms

**Symmetric Encryption:**
- AES-256-GCM (preferred)
- ChaCha20-Poly1305 (lightweight/embedded)

**Asymmetric Encryption:**
- RSA-4096 (legacy compatibility)
- ECDSA P-384 (elliptic curve)
- Ed25519 (signing)

**Hashing:**
- SHA-3-512 (general purpose)
- BLAKE3 (high performance)
- Argon2id (password hashing)

**Post-Quantum (Experimental):**
- Dilithium (signatures)
- Kyber (key encapsulation)

**Deprecated/Forbidden:**
- ❌ MD5, SHA-1 (collision attacks)
- ❌ DES, 3DES (weak key size)
- ❌ RSA <2048 bits
- ❌ Random number generators without CSPRNG

### Key Management

**Storage:**
- Hardware Security Modules (HSM) for production
- Operating system keystores (Keychain, KeePass) for development
- Never in source code, config files, or environment variables

**Rotation:**
- Signing keys: Annual rotation (or after suspected compromise)
- TLS certificates: 90-day validity (automated renewal)
- API tokens: 30-day validity (revocable)

**Export Control:**
Cryptographic software may be subject to export regulations:
- **US EAR**: Encryption Registration Number (ERN) required for some algorithms
- **EU Dual-Use**: Category 5 Part 2 (cryptography)
- Contact export-control@ideale-eu.example before implementing crypto

---

## Vulnerability Disclosure

### Security Advisories

Published vulnerabilities include:

- **CVE ID**: Common Vulnerabilities and Exposures identifier
- **Severity**: CVSS 3.1 score (0.0-10.0)
- **Affected Versions**: Specific releases impacted
- **Fixed Versions**: Releases containing the fix
- **Workarounds**: Mitigations if fix not yet available
- **Credits**: Reporter acknowledgment (if desired)

**Publication Channels:**
- GitHub Security Advisories (https://github.com/Robbbo-T/ASI-T2/security/advisories)
- Mailing list: security-announce@ideale-eu.example
- NVD (National Vulnerability Database)

### Hall of Fame

We recognize security researchers who report vulnerabilities responsibly:
- Listed in `SECURITY_HALL_OF_FAME.md`
- Acknowledgment in security advisories
- Swag/rewards for critical findings (TBD)

---

## Compliance & Audits

### Standards Alignment

**Aviation Safety:**
- DO-178C (Software Considerations in Airborne Systems)
- DO-254 (Hardware Assurance)
- DO-326A / ED-202A (Airworthiness Security Process)
- ARP4754B (Development Assurance for Civil Aircraft)

**Cybersecurity:**
- NIS2 Directive (EU 2022/2555)
- NIST Cybersecurity Framework
- ISO/IEC 27001 (Information Security Management)
- ISO/SAE 21434 (Automotive Cybersecurity, adapted for aerospace)

**Supply Chain:**
- NIST SP 800-161 (Supply Chain Risk Management)
- Executive Order 14028 (Improving the Nation's Cybersecurity)
- SLSA Framework (Supply-chain Levels for Software Artifacts)

### Third-Party Audits

We undergo periodic security assessments:
- **Penetration Testing**: Annual (by accredited firm)
- **Code Review**: Quarterly (internal + external for safety-critical)
- **Dependency Scanning**: Continuous (automated)
- **Compliance Audits**: As required by certification authorities

**Reports Available Upon Request:**
- SOC 2 Type II (Service Organization Control)
- ISO 27001 certificate
- Penetration test executive summaries (non-sensitive findings)

---

## Contact Information

### Security Team

**General Inquiries:**
- Email: security@ideale-eu.example
- PGP Key: [fingerprint]

**Incident Response (24/7):**
- Phone: [hotline]
- Signal: [number]

**NIS2 Coordinator:**
- Email: nis2@ideale-eu.example

**Export Control:**
- Email: export-control@ideale-eu.example

### TSC Security Leads

- **AIR**: [name] <email>
- **SEA**: [name] <email>
- **SPACE**: [name] <email>
- **INFRANET**: [name] <email>

---

## Version History

- **1.0.0** (2025-01-01): Initial security policy

---

## References

- [CHARTER.md](./CHARTER.md) - Federation charter
- [GOVERNANCE.md](./GOVERNANCE.md) - Governance model
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - Community conduct
- [policies/SECURITY.md](./policies/SECURITY.md) - Technical security requirements
- [NIS2 Directive](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng)
- [SLSA Framework](https://slsa.dev/)
