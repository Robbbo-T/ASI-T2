# Material Allowables Index

**Path:** `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-10_Wing_Primary_Structure/compliance/allowables/`

## Purpose

This index references material and joint allowables used in wing primary structure design and substantiation.

## Referenced Allowables

### Composite Materials
- **Material Basis:** S-Basis, A-Basis, B-Basis per MMPDS
- **Temperature Effects:** Room temperature, elevated temperature (up to 180°C), cold temperature (-55°C)
- **Environmental Knockdowns:** Humidity, UV exposure, chemical exposure

### Metallic Materials
- **Aluminum Alloys:** 7075-T6, 7050-T7451, 2024-T3
- **Titanium Alloys:** Ti-6Al-4V for high-load fittings
- **Steel:** 300M, 15-5PH for fasteners and bushings

### Joint Allowables
- **Bolted Joints:** Bearing/bypass interaction, open-hole tension, filled-hole tension
- **Bonded Joints:** Lap shear, peel, mixed-mode
- **Hybrid Joints:** Combined mechanical and adhesive

## References

Allowable data is maintained in CAX/FEA tools and referenced via:
- `../../../cax/FEA/allowables/` (detailed allowable datasets)
- Material specifications per ATA-20-30

## Traceability

All allowables must be traceable to:
1. Test reports (coupons, elements)
2. Statistical analysis (basis values)
3. Environmental conditioning records
4. Approval signatures (M&P, Stress)

---
*Allowables are version-controlled and require M&P approval for changes.*
