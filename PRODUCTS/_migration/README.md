# ASI-T2 Products Migration Tracking

This directory tracks the reorganization and migration of product directories within the ASI-T2 portfolio to provide better operational clarity and domain separation.

## Migration Overview

The ASI-T2 product portfolio has undergone strategic reorganization to separate operational domains and improve architectural clarity. This migration moved from field×environment naming patterns to focused product line organization.

## Migration History

### Phase 1: Initial Product Line Consolidation
- **Date**: Various dates (historical migrations)
- **Scope**: Consolidated field×environment products into product lines
- **Rationale**: Improved operational characteristics alignment

### Phase 2: Air/Space Domain Separation (2025-01-15)
- **Date**: January 2025
- **Scope**: Split GAIA_AIR_SPACE into focused GAIA-AIR and GAIA-SPACE portfolios
- **Rationale**: Eliminate operational environment conflicts, clearer domain focus

## Current Migration Manifest

The [manifest.csv](./manifest.csv) file contains the complete mapping of old paths to new paths with migration reasoning:

### Product Line Mappings
- **AMPEL360**: Manned aerospace systems (passenger/crewed transport)
- **GAIA-AIR**: Unmanned aerial systems (UAM/UAV) 
- **GAIA-SPACE**: Space-only systems (satellites & orbital robotics)
- **INFRANET**: Infrastructure and cross-cutting systems

### Key Migrations
- `GAIA_AIR_SPACE/GAIA-SAT` → `GAIA-SPACE/SAT-CONSTELLATIONS`
- `GAIA_AIR_SPACE/UAM-SWARM` → `GAIA-AIR/ETHICS-EMPATHY-UAV`
- Historical field×environment products consolidated into product lines

## Migration Benefits

1. **Clearer Domain Focus**: Each product line has distinct operational characteristics
2. **Reduced Conflicts**: Eliminates air/space environment overlaps
3. **Better Scalability**: Clear structure for adding new products
4. **Improved Navigation**: Logical organization for developers and stakeholders

## Validation & Compliance

- ✅ All migrations tracked in manifest.csv
- ✅ Git history preserved through proper file moves
- ✅ No breaking changes to build systems
- ✅ Documentation updated to reflect new paths
- ✅ QAIM validation compliance maintained

## Usage

To find the current location of a migrated product:
1. Check [manifest.csv](./manifest.csv) for the old_path → new_path mapping
2. Update any references, imports, or links to use the new path
3. Verify the new location contains expected content

---

*Migration tracking for ASI-T2 - Artificial Super Intelligence Transponders for Aerospace Sustainable Industry Transition*