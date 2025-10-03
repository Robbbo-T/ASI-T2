# Technical Security Requirements

**Version:** 1.0.0  
**Effective Date:** 2025-01-01  
**Owner:** INFRANET TSC  
**Security Team:** security@ideale-eu.example

---

## Purpose

This document defines technical security requirements for IDEALE-EU artifacts, complementing the root [SECURITY.md](../SECURITY.md) vulnerability reporting policy.

---

## Supply Chain Security (SLSA Framework)

### SLSA Levels

**SLSA Level 1: Documented Build** (Minimum for all IDEALE-EU)
- [ ] Build process documented
- [ ] Version control system used (Git)
- [ ] Build scripts in repository

**SLSA Level 2: Hosted Build** (Required for PAx releases)
- [ ] Hosted build platform (GitHub Actions, GitLab CI)
- [ ] Build provenance generated
- [ ] Source and build platform authenticated

**SLSA Level 3: Hardened Build** (Required for safety-critical)
- [ ] Hermetic builds (isolated, reproducible)
- [ ] Provenance signed (Sigstore, GPG)
- [ ] Non-falsifiable (tamper-evident)

**SLSA Level 4: Two-Party Review** (Aspirational)
- [ ] Two-person review required
- [ ] Hermetic + reproducible
- [ ] All dependencies reviewed

**Implementation:**
```yaml
# .github/workflows/release.yml
name: SLSA L3 Release
on:
  push:
    tags: ['v*']
permissions:
  id-token: write  # For Sigstore
  contents: write  # For release assets
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v1.9.0
```

---

## SBOM (Software Bill of Materials)

### Requirements

**All PAx releases must include SBOM:**
- Format: SPDX 2.3+ or CycloneDX 1.5+
- Depth: Include transitive dependencies
- License info: All components identified with SPDX license ID
- Vulnerabilities: Known CVEs listed

### Generation

**Python:**
```bash
pip-audit --format cyclonedx --output sbom.json
# Or
pip install sbom4python
sbom4python -m <module> -o sbom.spdx.json --format spdx
```

**Node.js:**
```bash
npx @cyclonedx/cyclonedx-npm --output-file sbom.json
```

**Container:**
```bash
syft <image> -o spdx-json > sbom.json
# Or
docker sbom <image> --format spdx > sbom.json
```

**Validation:**
```bash
# SPDX validation
java -jar tools-java-1.1.3-jar-with-dependencies.jar Verify sbom.spdx.json

# CycloneDX validation
cyclonedx-cli validate --input-file sbom.json
```

---

## Provenance & Attestations

### Sigstore Integration

**Signing Artifacts:**
```bash
# Sign with Sigstore (OIDC-based, no long-term keys)
cosign sign <artifact>

# Verify
cosign verify \
  --certificate-identity=<expected-identity> \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  <artifact>
```

**In-toto Attestation:**
```bash
# Generate attestation with predicate (SBOM, test results, etc.)
cosign attest \
  --predicate=sbom.json \
  --type https://cyclonedx.org/bom/v1.4 \
  <artifact>

# Verify attestation
cosign verify-attestation \
  --type https://cyclonedx.org/bom/v1.4 \
  --certificate-identity=... \
  --certificate-oidc-issuer=... \
  <artifact>
```

### GPG Signing (Legacy)

For contributors without Sigstore access:
```bash
# Sign
gpg --detach-sign --armor <artifact>

# Verify
gpg --verify <artifact>.asc <artifact>
```

**Key Management:**
- 4096-bit RSA or Ed25519
- Expires within 2 years
- Published to keyserver (keys.openpgp.org)

---

## Dependency Management

### Approved Package Registries

- ✅ PyPI (Python)
- ✅ npm registry (JavaScript)
- ✅ Maven Central (Java)
- ✅ crates.io (Rust)
- ✅ Docker Hub / GitHub Container Registry (Containers)
- ⚠️ Private registries (require security audit)
- ❌ Unofficial mirrors (forbidden)

### Dependency Pinning

**Python (requirements.txt):**
```txt
# Pin exact versions
numpy==1.24.3
requests==2.31.0

# Pin with hash verification
--require-hashes
numpy==1.24.3 \
    --hash=sha256:ab344f1bf21f140adab1e9cc6ab0d123...
```

**Node.js (package-lock.json):**
```json
{
  "lockfileVersion": 3,
  "packages": {
    "node_modules/example": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/example/-/example-1.0.0.tgz",
      "integrity": "sha512-..."
    }
  }
}
```

### Vulnerability Scanning

**Automated (CI/CD):**
```yaml
# .github/workflows/security.yml
- name: Python vulnerability scan
  run: |
    pip install pip-audit
    pip-audit --format=json --output=vulnerabilities.json

- name: Node.js vulnerability scan
  run: npm audit --audit-level=moderate

- name: Container scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'my-image:latest'
    severity: 'CRITICAL,HIGH'
```

**Manual (Development):**
```bash
# Python
pip-audit

# Node.js
npm audit

# Container
trivy image <image>
```

**Response:**
- Critical/High: Fix within 7 days
- Medium: Fix within 30 days
- Low: Address in next release

---

## Secrets Management

### Never Commit Secrets

**Forbidden:**
- API keys, tokens
- Passwords, SSH keys
- TLS certificates (private keys)
- Encryption keys
- Database credentials

**Detection:**
```bash
# Pre-commit hook (use gitleaks, detect-secrets)
pre-commit install
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

### Secrets in CI/CD

**GitHub Actions:**
```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
  # Masked in logs automatically
```

**Best Practices:**
- Use short-lived tokens (OIDC, STS)
- Rotate secrets every 90 days
- Audit access logs quarterly

---

## Access Control

### Least Privilege

**Repository Access:**
- **Read**: Public (OPEN classification)
- **Triage**: Labeled contributors (can triage issues)
- **Write**: Working group members (can push branches, not main)
- **Maintain**: Domain leads (can manage issues, projects, not settings)
- **Admin**: TSC chairs, Council (full access)

### Multi-Factor Authentication (MFA)

**Required for:**
- Admin/Maintain roles
- RESTRICTED repository access
- Export control reviews

**Supported Methods:**
- TOTP apps (Authy, Google Authenticator)
- Hardware keys (YubiKey, Titan)
- Passkeys (FIDO2)

---

## Cryptography Standards

### Algorithms (Approved)

**Symmetric:**
- AES-256-GCM
- ChaCha20-Poly1305

**Asymmetric:**
- RSA-4096 (legacy)
- ECDSA P-384
- Ed25519 (preferred)

**Hashing:**
- SHA-3-512
- BLAKE3
- Argon2id (passwords)

**Post-Quantum (Experimental):**
- Dilithium (signatures)
- Kyber (key encapsulation)

### Key Management

**Storage:**
- Production: Hardware Security Module (HSM)
- Development: OS keychain (Keychain Access, KeePass)
- Never: Source code, config files, environment variables

**Rotation:**
- Signing keys: Annual
- TLS certificates: 90-day validity (Let's Encrypt)
- API tokens: 30-day validity

---

## Container Security

### Base Images

**Approved:**
- ✅ `distroless/static` (Google)
- ✅ `alpine:latest` (minimal)
- ✅ `ubuntu:22.04` (LTS)
- ⚠️ Custom images (require security review)
- ❌ `latest` tag (forbidden in production)

**Minimal Example:**
```dockerfile
FROM gcr.io/distroless/static-debian12:nonroot
COPY --chown=nonroot:nonroot /app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

### Security Best Practices

- [ ] Run as non-root user
- [ ] Read-only root filesystem
- [ ] Drop all capabilities
- [ ] No privileged mode
- [ ] Scan for vulnerabilities (Trivy, Clair)

```yaml
# Kubernetes deployment
securityContext:
  runAsNonRoot: true
  runAsUser: 65534  # nobody
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```

---

## Network Security

### TLS/HTTPS

**Requirements:**
- TLS 1.3 (preferred) or TLS 1.2 (minimum)
- Strong cipher suites (AEAD only)
- Certificate from trusted CA
- HSTS headers enabled

**Configuration (Nginx):**
```nginx
ssl_protocols TLSv1.3 TLSv1.2;
ssl_ciphers 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256';
ssl_prefer_server_ciphers on;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

### Firewall Rules

**Default Deny:**
```bash
# Allow only necessary ports
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # HTTPS
iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # SSH (restricted IPs)
```

---

## Audit Logging

### What to Log

**Security Events:**
- Authentication (success, failure)
- Authorization (access granted, denied)
- Data access (RESTRICTED, CONTROLLED)
- Configuration changes
- Secrets access

**Format:**
```json
{
  "timestamp": "2025-01-01T12:00:00Z",
  "event": "authentication_success",
  "user": "alice@example.org",
  "ip": "203.0.113.42",
  "resource": "RESTRICTED/AAA/cad/wing_model.step",
  "action": "download",
  "result": "allowed"
}
```

### Retention

- Security logs: 1 year
- Audit logs (RESTRICTED): 5 years
- Legal hold: Indefinite (until released)

### Integrity

- Logs forwarded to SIEM (Splunk, ELK)
- Write-once storage (append-only)
- Cryptographic sealing (UTCS/QS)

---

## Incident Response

### Detection

**Automated:**
- SIEM alerts (failed logins, privilege escalation)
- Vulnerability scanner findings
- Secrets leaked (GitHub Advanced Security)

**Manual:**
- Security researcher reports
- User reports (suspicious activity)

### Response (24h)

1. **Triage**: Severity (Critical, High, Medium, Low)
2. **Contain**: Disable accounts, revoke tokens, block IPs
3. **Investigate**: Root cause, scope, affected systems
4. **Remediate**: Patch, rotate secrets, restore from backup
5. **Notify**: Users (if personal data breach), authorities (NIS2)

### Post-Mortem

- Document timeline, root cause, lessons learned
- Update runbooks, improve detection
- Share with community (transparency)

---

## Compliance Audits

### Third-Party Audits

- **Penetration Testing**: Annual (by accredited firm)
- **Code Review**: Quarterly (safety-critical)
- **SLSA Conformance**: Per release
- **SBOM Validation**: Automated (CI/CD)

### Self-Assessment

- **NIS2 Checklist**: Quarterly
- **Export Control Review**: Before RESTRICTED releases
- **Privacy Impact Assessment**: When processing changes

---

## References

- [../SECURITY.md](../SECURITY.md) - Vulnerability reporting
- [DATA_CLASSIFICATION.md](./DATA_CLASSIFICATION.md) - Classification levels
- [EXPORT_CONTROL.md](./EXPORT_CONTROL.md) - Export control compliance
- [SLSA Framework](https://slsa.dev/)
- [SBOM Guidance](https://www.ntia.gov/sbom)
- [Sigstore](https://www.sigstore.dev/)

---

**Questions?**
- Security team: security@ideale-eu.example
- Vulnerability reporting: See [../SECURITY.md](../SECURITY.md)

**Version History:**
- **1.0.0** (2025-01-01): Initial technical security requirements
