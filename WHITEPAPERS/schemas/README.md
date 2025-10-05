---
id: ASIT2-WHITEPAPERS-SCHEMAS
project: ASI-T2
artifact: Product Specification Templates and Schemas
llc: GENESIS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: "2025-10-01"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
canonical_hash: pending
---

# Product Specification Schemas

This directory contains templates and schemas for defining ASI-T2 products according to the Master Whitepaper #1 specifications.

---

## Contents

### [PRODUCT_SPEC_TEMPLATE.yaml](./PRODUCT_SPEC_TEMPLATE.yaml)

**Purpose:** Reusable YAML template for product specifications following Master Whitepaper #1 guidelines (Appendix A).

**Use this template when:**
- Creating a new product in the ASI-T2 portfolio
- Updating existing product documentation
- Defining product interfaces and compliance requirements
- Planning gates and milestones (FCR-1/FCR-2)

**Includes:**
- Product metadata (name, TRL, maturity)
- MAL interface specifications:
  - `MAL.v1.control` - Control bus interface
  - `MAL.v1.telemetry` - Telemetry bus interface
  - Data schemas for product-specific messages
- Standards compliance tracking:
  - ARP4754A (System development)
  - ARP4761 (Safety assessment)
  - DO-178C (Software certification)
  - DO-254 (Hardware certification)
  - ECSS (Space standards)
  - AS9100-lite (Quality management)
- Artifacts and evidence requirements:
  - System Requirements Specification (SRS)
  - System Design Document (SDD)
  - V&V plan
  - Safety case
  - SBOM (Software Bill of Materials)
  - Demo videos and logs
- TFA V2 bridge status (CB→QB→UE→FE→FWD→QS)
- Compliance checklist (MAL-EEM, export control, DAL)
- Dependencies on other products
- FCR-1 and FCR-2 gate requirements
- Team and contact information

---

## Usage

### 1. Copy the Template

```bash
cp WHITEPAPERS/schemas/PRODUCT_SPEC_TEMPLATE.yaml \
   PRODUCTS/<PRODUCT_LINE>/<PRODUCT_NAME>/product_spec.yaml
```

### 2. Fill in Product Details

Edit the copied file and replace placeholders:
- `<PRODUCT_NAME>` - Your product name
- `<TECHNOLOGY_READINESS_LEVEL>` - Current TRL (1-9)
- `<product_name>` - Lowercase product identifier for schemas
- `TBD` fields - Complete with actual values

### 3. Define Product-Specific Metrics

Uncomment and customize the metrics section based on your product type:

**For Aircraft (BWB, AMPEL360PLUS):**
- `tracking_error` - Control accuracy
- `energy_efficiency` - MJ per passenger-km
- `stability_margins` - Flight envelope

**For Satellites (GAIA SPACE):**
- `downlink_latency` - Communication delay
- `packet_integrity` - Data quality
- `mission_success_rate` - Operational reliability

**For Swarms (GAIA AIR):**
- `mean_pairwise_distance` - Coordination metric
- `collision_count` - Safety metric
- `mission_completion_rate` - Effectiveness

**For Infrastructure (H₂/LH₂ Airport):**
- `turnaround_time` - Operational efficiency
- `boil_off_losses` - Resource efficiency
- `capacity_per_hour` - Throughput

### 4. Update TFA V2 Status

Track progress through the TFA V2 bridge:
- **CB (Conceptual Baseline):** Vision and constraints defined
- **QB (Qualified Baseline):** Specifications and interfaces validated
- **UE (User Evidence):** Minimal useful evidence demonstrated
- **FE (Federation Entanglement):** Interoperability established
- **FWD (Forward Design):** Iterative design with metrics
- **QS (Quantum Superposition State):** Signed/auditable release

### 5. Plan Gates

**FCR-1 Requirements:**
- SBOM generated (`syft` or equivalent)
- Demo videos/logs published with hashes
- DOI obtained (Zenodo or similar)
- Git tag signed (`git tag -s`)
- UTCS anchor created

**FCR-2 Requirements:**
- Reproducibility verified (one-click scripts)
- Coverage targets met (line/branch)
- Attestations generated (in-toto/SLSA-lite)
- 2 external validations obtained

---

## Validation

Before committing your product specification:

```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('product_spec.yaml'))"

# Check required fields
grep -E "^product:|^trl:|^maturity:" product_spec.yaml

# Verify MAL interfaces
grep -E "control_bus|telemetry_bus|data_schema" product_spec.yaml
```

---

## Examples

Product specifications using this template can be found in:

- `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/` - Blended-wing-body aircraft
- `PRODUCTS/GAIA-SPACE/SAT-CONSTELLATIONS/` - Satellite constellation
- `PRODUCTS/GAIA-AIR/IDRO_WALL/` - Swarm defense system
- `PRODUCTS/INFRANET/LH2_CORRIDOR/` - Hydrogen infrastructure

---

## Related Documentation

### Master Whitepaper
* [Master Whitepaper #1](../MASTER_WHITEPAPER_1.md) - Complete technical specification
* [Whitepaper Section 4](../MASTER_WHITEPAPER_1.md#4-products-vision-state-interfaces-evidence) - Product specifications
* [Appendix A](../MASTER_WHITEPAPER_1.md#a-template-specproductyaml) - Template reference

### Standards & Compliance
* [Section 6](../MASTER_WHITEPAPER_1.md#6-vv-and-safety) - V&V and safety methodology
* [Section 7](../MASTER_WHITEPAPER_1.md#7-compliance-ethics--export) - Compliance and ethics

### Evidence & Gates
* [Section 5](../MASTER_WHITEPAPER_1.md#5-evidence--provenance-qsutcs) - Evidence pipeline
* [Section 8](../MASTER_WHITEPAPER_1.md#8-roadmap--gates) - Roadmap and gates

---

## Support

For questions or clarifications:
- Review the [Master Whitepaper #1](../MASTER_WHITEPAPER_1.md)
- Check the [Whitepapers README](../README.md) for usage guidelines
- Open an issue in the repository

---

*Last Updated: 2025-10-01*  
*Version: 0.1.0*  
*UTCS Anchor: TBD*
