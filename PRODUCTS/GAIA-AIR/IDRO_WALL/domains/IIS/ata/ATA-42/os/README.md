# OS Package — ATA-42 (GAIA-AIR IDRO_WALL / IIS)

Operating system and software configuration artifacts for ATA-42 Integrated Modular Avionics.

## Structure

- **S1000D/** — IETP/IETM data modules for technical publications
- **configuration/** — IMA configuration files (manifests, ARINC-653, RTOS)
- **testing/** — Test plans, procedures, coverage reports
- **compliance/** — DO-178C, DO-297, DO-326A/356A artifacts

## Configuration Files

### ARINC-653 Configuration
- `configuration/a653/partition.xml` — Partition definitions, APEX ports, resource budgets
- `configuration/a653/schedule.xml` — Major frame definition and window assignments

### Manifests
- `configuration/manifests/manifest.yaml` — Evidence hashes, SBOM references, QS anchor

### RTOS
- `configuration/rtos/*` — Board support package and RTOS configuration

## Testing

Test artifacts include:
- Unit and integration test plans
- Test procedures and cases
- Coverage reports (MC/DC where applicable)
- Health monitoring test results
- APEX interface validation

## Compliance

Certification evidence for:
- **DO-178C** — Software development lifecycle
- **DO-297** — IMA-specific objectives
- **DO-326A/356A** — Security development and methods

## Related Work Packages

See parent README.md for complete work package list and status.
