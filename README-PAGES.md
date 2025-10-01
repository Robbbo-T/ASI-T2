# GitHub Pages — CAD & S1000D

This repository publishes a static site with:

* **/CAD** — WebXR (A‑Frame) viewer with `<model-viewer>` fallback for local `.gltf/.glb`
* **/S1000D** — Browsable index for S1000D XML (with a lightweight client-side viewer)

> **Enable Pages** → *Settings* → *Pages* → **Source: GitHub Actions**. On push to `main`/`master`, the site builds and deploys automatically.

---

## Installation & Dependencies

The repository includes comprehensive Python dependency management:

* **`requirements.txt`** — Traditional pip-installable requirements for all Python components
* **`pyproject.toml`** — Modern Python project configuration with optional dependency groups
* **`INSTALLATION.md`** — Complete installation guide with troubleshooting
* **`verify_installation.py`** — Verification script to test all dependencies

**Quick setup:**

```bash
pip install -r requirements.txt
python verify_installation.py
python scripts/verify_structure.py  # Validate repository structure
```

---

## Quantum Computing Support

The repository includes quantum optimization capabilities for QUBO (Quadratic Unconstrained Binary Optimization) problems.

* **`pennylane >= 0.33.0`** — Quantum circuit simulation and QAOA/VQE algorithms
* **`numpy >= 1.24.0`** — Numerical computations for quantum optimization

**SICOCA QUBO Implementation** (`PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/qox/qubo/`):

* Supply chain optimization for logistic lane selection
* PennyLane integration for quantum algorithms (QAOA, VQE)
* Compatible with D‑Wave quantum annealers and classical solvers
* Complete test suite and JSON artifacts for UTCS‑MI traceability

**Run SICOCA optimization:**

```bash
cd PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/qox/qubo
python aqua_qubo_sicoca.py       # Execute QUBO model
python test_aqua_qubo_sicoca.py  # Run test suite (5/5 tests)
```

See `PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/qox/qubo/SICOCA_README.md` for detailed documentation.

---

## Optional Dependency Groups

Install feature groups as needed (defined in `pyproject.toml`):

* **`dev`** — Development & testing tools (pytest, httpx)
* **`docs`** — Documentation generation (mkdocs, mkdocs-material)
* **`xml`** — High‑performance XML parsing (lxml)
* **`optimization`** — MILP optimization framework (pyomo) for AQUA OS resource planning

**Install with optional dependencies:**

```bash
pip install -e ".[optimization]"  # For AQUA MILP optimization module
pip install -e ".[dev,docs]"      # Multiple groups
```

---

## Figure Generation

Automated technical diagram generation for publications:

* **`scripts/generate_publication_figures.py`** — Generates blueprint‑style technical diagrams from text placeholders
* **Dependencies:** `matplotlib`, `pillow` (included in `requirements.txt`)

**Generate figures for a publication:**

```bash
python3 scripts/generate_publication_figures.py path/to/publication.md
```

This tool extracts `[FIGURE PLACEHOLDER: "..."]` descriptions and generates professional technical diagrams with a consistent blueprint aesthetic.

---

## How it works

* The build script scans the repo, copies assets into `_site/`, and writes minimal HTML/JS to browse/view them.
* `_site/` is ignored by git and produced by CI (or locally via the script).
* Script: `scripts/ghpages_build.py`

---

## Repository Structure

The repository follows a strict **ENVIRONMENTS/FIELDS/PRODUCTS** taxonomy:

* **ENVIRONMENTS/DIGITAL/CONTEXT/** and **ENVIRONMENTS/PHYSICAL/CONTEXT/** — Operational deployment contexts
* **FIELDS/** — Technology domains and specialized capabilities
* **PRODUCTS/** — Strategic product lines (source for CAD/S1000D content)

Structure validation is automated via `scripts/verify_structure.py` and CI workflows.

---

## Documentation & Whitepapers

### Master Whitepaper #1

The repository includes comprehensive technical documentation in the **WHITEPAPERS/** directory:

* **[Master Whitepaper #1](WHITEPAPERS/MASTER_WHITEPAPER_1.md)** — Complete system-of-systems specification covering:
  - All 7 ecosystem products (AMPEL360 BWB, GAIA SPACE, GAIA AIR, Digital Platform, AMPEL 360PLUS, H₂/LH₂ Airport, Sustainable Finance)
  - TFA V2 architecture (CB→QB→UE/FE→FWD→QS)
  - MAL (Master Application Layer) specification
  - Evidence & provenance pipeline (QS/UTCS)
  - V&V and safety methodology
  - Compliance and ethics (MAL-EEM)
  - Roadmap with FCR-1/FCR-2 gates

* **[Product Specification Template](WHITEPAPERS/schemas/PRODUCT_SPEC_TEMPLATE.yaml)** — Reusable YAML template for defining new products with MAL interfaces, standards tracking, and gate requirements

### Sustainable Finance Framework

The **FINANCE/** directory contains the anti-speculative economic design:

* **[Finance Overview](FINANCE/README.md)** — Framework emphasizing service-aligned economics with SLO-based rewards, operational credits, and quadratic funding
* **[Finance Principles](FINANCE/PRINCIPLES.md)** — Detailed mechanisms including demurrage, lock-ups, slashing, and treasury governance

### Citation

The repository includes **CITATION.cff** for proper academic citation (CFF 1.2.0 compliant).

---

## CAD

### Where to put models

Any of these locations are discovered (recursive by pattern):

```
PRODUCTS/*/*/domains/*/cax/CAD/wing_baseline_model/surface_geometry/
CAD/wing_baseline_model/surface_geometry/
```

### What's supported

* `.glb` — single self‑contained file (copied as‑is)
* `.gltf` — **sidecars supported**. External `buffers[].uri` (e.g. `.bin`) and `images[].uri` (textures) are copied, **preserving relative paths**
* Each model is published in its **own bucket** to avoid name collisions:

```
/CAD/assets/<model-stem>/<model-file>
# e.g. /CAD/assets/wing_oml_left/wing_oml_left.gltf
#      /CAD/assets/wing_oml_left/wing_data.bin
```

### Hero model (optional)

Declare a preferred first/"hero" model in `pages.manifest.yaml`:

```yaml
cad.hero: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/surface_geometry/wing_oml_left.gltf
```

Paths are repo‑relative; forward/back slashes are normalized.

---

## S1000D

### Where to put XML

Any of these roots are discovered:

```
PRODUCTS/*/*/domains/*/ata/*/S1000D
PRODUCTS/*/*/ata/*/S1000D
PRODUCTS/*/*/ata/*/s1000d
ata/57/s1000d
ata/*/S1000D
```

### Path preservation & collisions

* Each discovered root is published under `/S1000D/dm/rootN/` (**N** starts at 1)
* The **entire original subpath is preserved**, so identically named files from different trees no longer clash

**Example published paths:**

```
/S1000D/dm/root1/data_modules/descriptive/DMC-...xml
/S1000D/dm/root2/publication_modules/PMC-...xml
```

### Viewer URLs

* Index page: `/S1000D/`
* Viewer page: `/S1000D/viewer.html?dm=rootN/<subpath>/<file>.xml`
* Raw XML: `/S1000D/dm/rootN/<subpath>/<file>.xml`

> Basic `..` sanitization is applied to the `dm` query param.

---

## AQUA Optimization Module

**Location:** `PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/optimization/`

Comprehensive Mixed Integer Linear Programming (MILP) optimization framework for hybrid classical‑quantum resource planning in the **AQUA OS Aircraft** system.

**Key components:**

* `aqua_milp_pyomo.py` — Complete MILP model using Pyomo framework
* `test_aqua_milp.py` — Automated test suite for model validation
* `README.md` — Detailed documentation and usage guide

**Features:**

* Multi‑criteria optimization (Cost, Emissions, Reliability, Synchronization)
* Hybrid classical‑quantum subsystem modeling
* Linearized synchronization constraints (Big‑M method)
* Quantum quality certification (Fidelity/Latency thresholds)
* UTCS‑MI v5.0 compliant traceability with SHA‑256 hashing
* Automatic solver detection (CBC, GLPK, Gurobi, CPLEX)

**Installation:**

```bash
pip install -e ".[optimization]"  # Install pyomo dependency
sudo apt-get install glpk-utils     # Install GLPK solver (Linux)
```

**Usage:**

```bash
cd PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/optimization
python aqua_milp_pyomo.py        # Run optimization
python test_aqua_milp.py         # Run tests
```

See the module's README for detailed documentation and customization options.

---

## Local build & preview

```bash
python scripts/ghpages_build.py
# Optional preview:
python -m http.server -d _site 8080
# Then open http://localhost:8080/
```

---

## CI / Deployment

* **Pages workflow** (`.github/workflows/pages.yml`) builds `_site/` and deploys via GitHub Pages
* **Structure guard** (`.github/workflows/structure-guard.yml`) validates repository structure and prevents regressions
* Triggers on push to `main` or `master`

### Minimal `pages.yml` example

```yaml
name: GitHub Pages
on:
  push:
    branches: [ main, master ]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt
      - run: python scripts/ghpages_build.py
      - uses: actions/upload-pages-artifact@v3
        with: { path: _site }
  deploy:
    needs: build
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

---

## Notes & limits

* Only local repo files are indexed; no external network fetches occur at runtime
* For `.gltf`, make sure sidecar URIs are relative paths (non‑`data:` URIs get copied)
* `_site/` is ephemeral; don't commit it
* For large CAD assets, prefer `.glb` to reduce path complexity and I/O round‑trips

---

## Troubleshooting

* **No models found**: confirm paths match the discovery patterns and file extensions are `.gltf` or `.glb`
* **Textures missing**: verify relative paths in `images[].uri` are correct and within the source tree
* **Viewer 404s**: ensure `_site/` was rebuilt and that CI uploaded the artifact
* **MILP solver not found**: install GLPK (`glpsol`) or set `GUROBI_HOME`/`CPLEX_HOME` for commercial solvers

---

## Verification

Run all guards locally:

```bash
python verify_installation.py
python scripts/verify_structure.py
pytest -q  # if dev group installed
```
