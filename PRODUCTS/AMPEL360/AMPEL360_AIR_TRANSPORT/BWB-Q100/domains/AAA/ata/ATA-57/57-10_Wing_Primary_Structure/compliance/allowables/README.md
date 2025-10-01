# Material Allowables

This directory contains material and joint allowables data used in wing primary structure design and substantiation.

## Purpose

Provides reference to:
- Material property databases (strength, stiffness, environmental effects)
- Joint allowables (bearing, bypass, shear, peel)
- Statistical basis values (A-Basis, B-Basis, S-Basis)
- Environmental knockdown factors

## Contents

- **index.md** — Master index of allowables with references to detailed datasets

## Allowable Categories

### Composite Materials
- Laminate properties (tension, compression, shear)
- Temperature and moisture effects
- Environmental aging factors

### Metallic Materials
- Aluminum alloys (7075, 7050, 2024)
- Titanium alloys (Ti-6Al-4V)
- Steel alloys (300M, 15-5PH)

### Joints
- Bolted joint allowables (bearing/bypass)
- Bonded joint allowables (lap shear, peel)
- Hybrid joint allowables

## References

Detailed allowables data maintained in:
- `../../../cax/FEA/allowables/` — Computational datasets
- Material specifications per ATA-20-30

## Traceability

All allowables are traceable to:
- Coupon test reports (see evidence/coupons/)
- Statistical analysis methods
- Material certifications
- Approval signatures (M&P, Stress)

---

*Part of ATA-57-10 Wing Primary Structure — Configuration controlled under UTCS/QS v5.0*
