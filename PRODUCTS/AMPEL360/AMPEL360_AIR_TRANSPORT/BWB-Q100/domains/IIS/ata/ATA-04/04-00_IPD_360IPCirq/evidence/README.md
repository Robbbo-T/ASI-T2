# Evidence & QA Forms

This directory contains evidence file references and links to ATA-20 QA forms.

## Structure

- **file_refs/** — Evidence file references (CO-3.23) — Pointers to evidence packages
- **qa_forms/** — QA form links (CO-3.24) — References to ATA-20 canonical forms
- **logs/** — OOC, torque, cure logs (CI-2.26) — Detailed records

## ATA-20 Form References (Canonical)

All physical work must reference appropriate ATA-20 forms:

1. **FORM-QA-20-10-01** — Composite Fastening
   - Path: `../../../../AAA/ata/ATA-20/20-10_Structural_Practices/forms/`

2. **FORM-QA-20-10-02** — Adhesive Bonding
   - Path: `../../../../AAA/ata/ATA-20/20-10_Structural_Practices/forms/`

3. **FORM-QA-20-20-01** — Cabin Integrity / Leak Test
   - Path: `../../../../AAA/ata/ATA-20/20-20_Sealing_and_Pressurization/forms/`

4. **FORM-QA-20-30-01** — Material Handling & OOC Log
   - Path: `../../../../AAA/ata/ATA-20/20-30_Material_Handling/forms/`

5. **FORM-QA-20-40-01** — Bonding / EMI Continuity
   - Path: `../../../../AAA/ata/ATA-20/20-40_Electrical_Bonding/forms/`

## Evidence Types

Evidence files include:
- OOC (Out-of-Cold) logs
- Torque records
- Cure logs
- NDT results
- Pressure test traces
- Bond test results
- EMI continuity measurements
- Leak test data
- Visual inspection photos
- Dimensional verification

## Validation

All evidence must:
1. Pass `evidence.file.schema.json` validation
2. Include SHA-256 checksums for integrity
3. Reference appropriate QA forms
4. Be sealed with QS/UTCS anchor (CO-3.29)

---

*Part of 360IPCirq — Configuration controlled under UTCS/QS v5.0*
