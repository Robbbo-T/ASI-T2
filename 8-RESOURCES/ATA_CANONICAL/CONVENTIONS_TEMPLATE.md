# ATA <ATA_NUMBER> Conventions

**Domain:** <DOMAIN>  
**Version:** 0.1.0  
**Last Updated:** <DATE>

---

## 1) File Naming

* **Data Modules (S1000D):** Follow DMC pattern: `DMC-<MODEL>-<SNS>-<...>.xml`
* **Assets:** Descriptive names with version suffix: `asset_name_v1.0.ext`
* **Documents:** Use kebab-case: `design-review-v1.md`
* **Manifests:** Include domain and ATA: `<DOMAIN>-<ATA>-manifest.yaml`

## 2) Version Control

* **Semantic Versioning:** MAJOR.MINOR.PATCH for all artifacts
* **Git Commit Messages:** Follow conventional commits:
  - `feat(ata-<ATA>): description` for new features
  - `fix(ata-<ATA>): description` for bug fixes
  - `docs(ata-<ATA>): description` for documentation
  - `chore(ata-<ATA>): description` for maintenance

## 3) Documentation Standards

* **README files:** Use YAML front matter with UTCS metadata
* **S1000D Data Modules:** Follow project BREX rules
* **Diagrams:** Store source in `assets/`, export to PNG/SVG/WebCGM
* **Code Comments:** Explain "why", not "what"

## 4) Quality & Compliance

* **Reviews:** All changes require peer review via PR
* **Baselines:** Tag formal releases: `<DOMAIN>-<ATA>-BL-<N>`
* **Evidence:** Store in `governance/audits/` with QS hashes
* **Testing:** Document test results in `os/testing/`

## 5) Cross-References

* **Internal:** Use relative paths from this ATA root
* **External:** Reference via `governance/cross_references.yaml`
* **Product Links:** Products use symlinks, not copies

## 6) Artifacts & Outputs

* **SBOM:** Generated in `os/configuration/manifests/`
* **Build Outputs:** Reference, don't store (use CI artifacts)
* **Binary Files:** Store with manifest and QS hash
* **CAD/CAE:** Store native format + neutral export (STEP/IGES)

## 7) Change Control

* **Baseline Changes:** Require CAR/PAR in `governance/audits/`
* **Risk Assessment:** Update `governance/risk_management/` for safety-critical changes
* **Traceability:** Link requirements → design → verification

## 8) Security

* **Sensitive Data:** Mark classification in front matter
* **Credentials:** Never commit (use secrets management)
* **Hashes:** QS/UTCS hashes for all critical artifacts
* **Sanitization:** Document in `sustainment/recycling_disposal/data_sanitization/`

## 9) Collaboration

* **Issues:** File in GitHub with `<DOMAIN>/<ATA>` label
* **Discussions:** Use project communication channels
* **External Partners:** Coordinate via `governance/change_control/`

## 10) Automation

* **CI/CD:** Validate on every PR (see §6 in README)
* **Scripts:** Place in `scripts/`, document usage
* **Linting:** YAML, XML, JSON validated before merge
