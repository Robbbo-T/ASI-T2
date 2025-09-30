# ATA-42 IMA — CI Templates (Quick Reference)

**Scope:** Minimal entry point for CI checks guarding ATA‑42 (IMA). Each validator exits **non‑zero** on failure.

## Validators

* **AFDX VL table** — `validate_afdx.py` → checks schema, BAG set, L2 size, per‑net BW, headroom.
  Data: [`../../buses/afdx/vl_table.csv`](../../buses/afdx/vl_table.csv)
* **ARINC‑429 channels/labels** — `validate_a429.py` → channel schema, 12.5/100 kbps, octal labels cross‑ref.
  Data: [`../../buses/a429/channel_map.csv`](../../buses/a429/channel_map.csv), `../../buses/a429/label_dict.csv`
* **ARINC‑653 schedule** — `validate_schedule.py` → windows sum ≤ major frame, no overlap, NAV→FBW order.
  Data: [`../../os/schedule.xml`](../../os/schedule.xml)
* **Safety links/trace** — `validate_safety.py` → link integrity, FHA↔PSSA↔SSA trace no‑orphans.
  Data: [`../../safety/FHA_PSSA_SSA.md`](../../safety/FHA_PSSA_SSA.md)
* **Security plans** — `validate_security.py` → link integrity, required sections present, key inventory present.
  Data: [`../../security/SEC_Plans.md`](../../security/SEC_Plans.md)
* **SBOM/provenance** — `validate_sbom.py` → SBOM present, signed builds, provenance fields set.
  Data: `../../configs/sbom/`

> Only `validate_afdx.py` is mandatory today; others may be added incrementally.

## GitHub Actions

* **AFDX:** `.github/workflows/afdx.yml` — runs AFDX validator on push/PR.
* **A429 (optional):** `.github/workflows/a429.yml` — runs A429 validator.

## Local usage

```bash
# From repo root
python3 PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-42/tools/ci/validate_afdx.py
```

## Conventions

* **Return code:** 0 = pass, ≠0 = fail.
* **Warnings:** printed with `::warning ::` but do not fail the job.
* **Paths:** this README assumes relative navigation from `tools/ci/` up to ATA‑42 root.

## Adding New Validators

1. Create `validate_<topic>.py` in this directory
2. Follow pattern: parse data, check rules, print `::error ::` on fail
3. Update this README with new validator entry
4. Add GitHub Actions workflow if needed

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.2.0 | 2025-09-29 | IIS | Expanded CI README with validator details |
| 0.1.0 | 2025-09-28 | IIS | Initial CI templates |