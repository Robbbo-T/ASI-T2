# Interchangeability / Replaceability (IRQ)

This directory contains interchangeability and replaceability rules for parts.

## Structure

- **tuples/** — IRQ tuples (CO-3.18) — Part interchange pairs with classifications
- **constraints/** — Qualified alternate constraints (CO-3.19) — Performance, weight, software limits
- **classes/** — Interchangeability class definitions (CI-2.18) — Full/Backward/Forward/None

## IRQ Classes

- **FULL** — Parts are fully interchangeable in both directions
- **BACKWARD** — New part can replace old part, but not vice versa
- **FORWARD** — Old part can replace new part, but not vice versa
- **NONE** — No interchangeability (separate, distinct parts)

## Validation

All IRQ tuples must:
1. Pass `irq.tuple.schema.json` validation
2. Have proper approval documentation
3. Include constraint analysis where applicable
4. Reference MRB cases for non-standard interchanges

---

*Part of 360IPCirq — Configuration controlled under UTCS/QS v5.0*
