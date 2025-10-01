# Effectivity & Options

This directory contains effectivity rules and option/variant management for aircraft configuration control.

## Structure

- **rules/** — Effectivity rules (CO-3.16) — MSN ranges, blocks, date-based effectivity
- **options/** — Option/variant flags (CO-3.17) — Configuration options and dependencies

## Effectivity Management

Effectivity rules define when parts, procedures, or configurations apply to specific aircraft:

### By Manufacturing Serial Number (MSN)
- **Start**: First MSN where effectivity begins
- **End**: Last MSN where effectivity applies (or "OPEN" for ongoing)
- **Exclude**: Specific MSNs or ranges to exclude

### By Block
- Block numbers for production batches
- Modification blocks
- Software/hardware configuration blocks

### By Date
- Effective from date
- Expiration date (if applicable)

### By Options
- Required option codes
- Excluded option codes
- Conditional logic (AND/OR/NOT/XOR)

## Option/Variant Management

Options define aircraft configuration choices:
- **Option Code**: Unique identifier (e.g., OPT-WX100 for weather radar)
- **Dependencies**: Required options for this option to be valid
- **Exclusions**: Options that cannot coexist
- **Impact**: Downstream effects on parts, procedures, systems

## Validation

All effectivity rules must:
1. Pass `effectivity.rule.schema.json` validation
2. Have clear start conditions
3. Include proper approval documentation
4. Link to relevant service bulletins, mods, or engineering changes

## Integration

Effectivity is checked at multiple points:
- Part selection (IPD items)
- Procedure applicability (R/I tasks)
- Interchangeability rules (IRQ tuples)
- Evidence requirements (QA forms)
- Maintenance scheduling

---

*Part of 360IPCirq — Configuration controlled under UTCS/QS v5.0*
