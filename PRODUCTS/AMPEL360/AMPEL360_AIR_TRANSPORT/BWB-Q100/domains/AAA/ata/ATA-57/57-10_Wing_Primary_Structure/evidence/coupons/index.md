# Coupon Test Index

**Path:** `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-10_Wing_Primary_Structure/evidence/coupons/`

## Purpose

This index references all coupon-level test results used to establish material and joint allowables for wing primary structure.

## Test Categories

### Material Characterization
- **Tension:** 0°, 45°, 90° fiber orientations
- **Compression:** 0°, 45°, 90° fiber orientations
- **Shear:** In-plane shear, interlaminar shear
- **Bearing:** Pin bearing, bolt bearing

### Joint Testing
- **Open-Hole Tension (OHT):** Notch sensitivity
- **Filled-Hole Tension (FHT):** Fastener interference fit effects
- **Bearing/Bypass:** Combined bearing and bypass loads
- **Pull-Through:** Fastener pull-through resistance
- **Bolted Lap Joints:** Single-lap, double-lap configurations

### Bonded Joint Testing
- **Lap Shear:** Adhesive shear strength
- **Peel:** Mode I fracture toughness
- **Mixed-Mode:** Combined shear and peel
- **Durability:** Hot/wet aging, thermal cycling

### Environmental Effects
- **Hot/Wet Conditioning:** Elevated temperature + moisture
- **Cold Temperature:** -55°C performance
- **UV Exposure:** Weathering effects
- **Chemical Exposure:** Fluids, hydraulics, deicing

## Coupon Test Matrix

| Test Series ID | Description | Sample Size | Temperature | Status |
|----------------|-------------|-------------|-------------|--------|
| CT-57-10-001 | Laminate tension 0° | n=18 | RTD, ETW, CTD | Complete |
| CT-57-10-002 | Laminate compression 0° | n=18 | RTD, ETW, CTD | Complete |
| CT-57-10-003 | Open-hole tension | n=12 | RTD, ETW | Complete |
| CT-57-10-004 | Filled-hole tension | n=12 | RTD, ETW | Complete |
| CT-57-10-005 | Bearing/bypass | n=24 | RTD, ETW | In-work |
| CT-57-10-006 | Bonded lap shear | n=18 | RTD, ETW, HW | Complete |

**Legend:** RTD=Room Temperature Dry, ETW=Elevated Temperature Wet, CTD=Cold Temperature Dry, HW=Hot Wet

## Statistical Analysis

All coupon test results are statistically analyzed to establish:
- **A-Basis:** 99% probability with 95% confidence (critical structure)
- **B-Basis:** 90% probability with 95% confidence (redundant structure)
- **S-Basis:** Specification minimum (where applicable)

## References

Detailed test reports and data are maintained in:
- `../../../cax/testing/coupons/` (raw data, test reports)
- Material specifications (ATA-20-30)
- Allowables database (compliance/allowables/)

## Traceability

Each coupon test must have:
1. Test plan and procedure
2. Material certification (batch traceability)
3. Environmental conditioning log
4. Test data and photos
5. Statistical analysis
6. Approval signatures

---
*Coupon test results are the foundation for structural allowables and require M&P approval.*
