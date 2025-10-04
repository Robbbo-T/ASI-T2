# IDEALE-EU Federation: Quick Start Guide

Welcome to the IDEALE-EU open federation! This guide helps you navigate the governance, policies, and standards implemented in this repository.

---

## 📚 Essential Reading (Priority Order)

### 1. Start Here
- [**CHARTER.md**](./CHARTER.md) - Understand our mission, principles, and founding values (5 min)
- [**README.md**](./README.md#-ideale-eu-federation) - Federation overview and technical architecture (10 min)

### 2. Before Contributing
- [**CODE_OF_CONDUCT.md**](./CODE_OF_CONDUCT.md) - Community standards and expectations (5 min)
- [**CONTRIBUTING.md**](./CONTRIBUTING.md) - How to contribute code, documentation, or designs (15 min)

### 3. Security & Compliance
- [**SECURITY.md**](./SECURITY.md) - Report vulnerabilities and understand our incident response (10 min)
- [**policies/DATA_CLASSIFICATION.md**](./policies/DATA_CLASSIFICATION.md) - OPEN/SHARED/RESTRICTED/CONTROLLED levels (10 min)
- [**policies/EXPORT_CONTROL.md**](./policies/EXPORT_CONTROL.md) - ITAR/EAR/EU dual-use compliance (15 min)

### 4. Governance & Decision-Making
- [**GOVERNANCE.md**](./GOVERNANCE.md) - How decisions are made, who decides what (15 min)
- [**ROADMAP.md**](./ROADMAP.md) - Development phases 2025-2028 (10 min)

---

## 🚀 Quick Actions

### I want to...

**Contribute Code**
1. Sign CLA (required) – The CLA signing service is not yet live. Please contact a project admin for instructions or check back soon.
2. Read [CONTRIBUTING.md](./CONTRIBUTING.md)
3. Fork repo, create branch, submit PR
4. Ensure CI passes (validate-manifests, sbom-attest)

**Report a Security Issue**
- Email: security@ideale-eu.example
- See [SECURITY.md](./SECURITY.md) for coordinated disclosure

**Join a Working Group**
- Browse [PRODUCTS/](./PRODUCTS/) for active groups
- Email relevant WG (listed in domain README)
- Attend monthly meetings (see GOVERNANCE.md)

**Propose a New Feature (RFC)**
- Create issue with `[RFC]` prefix
- Follow template in `rfcs/` (to be created)
- TSC reviews and votes

**Use Federation Templates**
- Product README: [Shared/_templates/README.product.md](./Shared/_templates/README.product.md)
- Domain manifest: [Shared/_templates/index.extracted.schema.json](./Shared/_templates/index.extracted.schema.json)
- Contribution guide: [Shared/_templates/CONTRIBUTING.template.md](./Shared/_templates/CONTRIBUTING.template.md)

---

## 🔐 Classification Quick Reference

| Level | Description | Storage | Access |
|-------|-------------|---------|--------|
| **OPEN** 🌍 | Public | GitHub public repos | Anyone |
| **SHARED** 🤝 | Members only, NDA | Private repos | Signed NDA |
| **RESTRICTED** 🔒 | Vetted orgs, bilateral agreements | Off-repo with ACLs | Executed agreement |
| **CONTROLLED** 🚫 | Export-controlled (ITAR/EAR/Dual-Use) | Off-repo, hash refs only | Export license |

**Rule:** Never commit CONTROLLED content to any repository. Use hash pointers.

See [policies/DATA_CLASSIFICATION.md](./policies/DATA_CLASSIFICATION.md) for full details.

---

## 📋 Checklist Before Submitting

Before opening a pull request, ensure:

- [ ] **Classification declared** in manifest (`classification: OPEN|SHARED|RESTRICTED|CONTROLLED`)
- [ ] **Export control reviewed** (`export_control.itar`, `export_control.ear`, `export_control.eu_dual_use`)
- [ ] **SBOM generated** for software/firmware (if PAx artifact)
- [ ] **Tests pass** locally (`pytest`, `npm test`, etc.)
- [ ] **Linting clean** (`pre-commit run --all-files`)
- [ ] **Documentation updated** if behavior changes
- [ ] **Commit message follows convention** (`feat(domain): description`)
- [ ] **CODEOWNERS approval** requested

CI will automatically check most of these.

---

## 🛠️ CI/CD Workflows

Our automated checks enforce federation policies:

### Always Run
- **validate-manifests.yml** - Schema compliance, classification checks
- **struct-and-brex.yml** - Repository structure validation

### On Release (tags)
- **sbom-attest.yml** - Generate SBOM, sign with Sigstore
- **s1000d-checks.yml** - Validate S1000D data modules

### Policy Gates
- ❌ **FAIL** if CONTROLLED content detected in public repos
- ⚠️ **WARN** if classification or contacts missing
- ⚠️ **WARN** if SBOM not found for PAx artifacts

See [.github/workflows/](./.github/workflows/) for details.

---

## 📞 Contacts

### General Inquiries
- **Discussions:** discussions@ideale-eu.example
- **GitHub:** https://github.com/Robbbo-T/ASI-T2/discussions

### Specialized
- **Security:** security@ideale-eu.example (24/7)
- **Privacy:** privacy@ideale-eu.example
- **Export Control:** export-control@ideale-eu.example
- **Code of Conduct:** conduct@ideale-eu.example
- **Legal/IP:** legal@ideale-eu.example

### Technical Steering Committees
- **AIR TSC:** air-tsc@ideale-eu.example
- **SEA TSC:** sea-tsc@ideale-eu.example
- **SPACE TSC:** space-tsc@ideale-eu.example
- **INFRANET TSC:** infranet-tsc@ideale-eu.example

---

## 🌟 Recognition

Active contributors are recognized through:
- Listing in domain `CONTRIBUTORS.md`
- Acknowledgment in release notes
- Annual contributor awards
- Invitation to working group leadership

---

## 📖 Standards Reference

| Domain | Primary Standards |
|--------|-------------------|
| Documentation | S1000D Issue 5.0, ATA iSpec 2200 |
| CAD/CAM | STEP AP242, QIF |
| Software | SPDX 2.3+, CycloneDX 1.5+, DO-178C |
| Security | SLSA, Sigstore, NIS2 |
| Privacy | GDPR, EU-U.S. DPF |
| Export | ITAR 22 CFR 120-130, EAR 15 CFR 730-774, EU 2021/821 |

---

## 🔄 Migration to Federation Schema v1.0.0

If you maintain an existing domain with legacy `index.extracted.yaml`:

1. **Add new required fields:**
   ```yaml
   schema_version: "1.0.0"
   classification: "OPEN"  # or SHARED/RESTRICTED/CONTROLLED
   export_control:
     itar: false
     ear: "NLR"
     eu_dual_use: "none"
   licenses:
     code: "Apache-2.0"
     docs: "CC-BY-4.0"
     hardware: "CERN-OHL-S-2.0"
   contacts:
     - "your-email@example.org"
   ```

2. **Optionally convert to artifacts list:**
   ```yaml
   artifacts:
     - type: "cax:cad"
       path: "cax/CAD/model.step"
       description: "Baseline geometry"
   ```

3. **Keep legacy fields for now** (backward compatibility)

4. **Validate:** Run `validate-manifests.yml` workflow

See [PRODUCTS/AMPEL360/.../AAA/index.extracted.EXAMPLE.yaml](./PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/index.extracted.EXAMPLE.yaml) for complete example.

---

## ✅ Next Steps

1. **Read** [CHARTER.md](./CHARTER.md) to understand our mission
2. **Sign** the Contributor License Agreement (CLA)
3. **Join** a working group or domain of interest
4. **Explore** [PRODUCTS/](./PRODUCTS/) to see active projects
5. **Contribute** your first PR!

**Welcome to the IDEALE-EU community!** 🚀

---

**Version:** 1.0.0  
**Last Updated:** 2025-01-01  
**Status:** Production-ready

For questions, open a [GitHub Discussion](https://github.com/Robbbo-T/ASI-T2/discussions) or contact governance@ideale-eu.example
