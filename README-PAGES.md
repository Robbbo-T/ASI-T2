# GitHub Pages — CAD & S1000D

This repo publishes a static site with:

* **/CAD** — WebXR (A-Frame) viewer + `<model-viewer>` fallback for local `.gltf/.glb`
* **/S1000D** — browsable index for S1000D XML (with a lightweight client-side viewer)

**Enable Pages** → *Settings* → *Pages* → **Source: GitHub Actions**.
On push to `main`/`master`, the site builds and deploys automatically.

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
```

## How it works

* The build script scans the repo, copies assets into `_site/`, and writes minimal HTML/JS to browse/view them.
* `_site/` is ignored by git and produced by CI (or locally via the script).
* Script: `scripts/ghpages_build.py`

## CAD

**Where to put models**

Any of these locations are discovered (recursive by pattern):

```
PRODUCTS/*/*/domains/*/cax/CAD/wing_baseline_model/surface_geometry/
CAD/wing_baseline_model/surface_geometry/
```

**What's supported**

* `.glb` — single self-contained file (copied as-is).
* `.gltf` — **sidecars supported**. External `buffers[].uri` (e.g. `.bin`) and `images[].uri` (textures) are copied, **preserving relative paths**.
* Each model is published in its **own bucket** to avoid name collisions:

```
/CAD/assets/<model-stem>/<model-file>
# e.g. /CAD/assets/wing_oml_left/wing_oml_left.gltf
#      /CAD/assets/wing_oml_left/wing_data.bin
```

**Hero model (optional)**

Declare a preferred first/"hero" model in `pages.manifest.yaml`:

```yaml
cad.hero: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/surface_geometry/wing_oml_left.gltf
```

Paths are repo-relative; forward/back slashes are normalized.

## S1000D

**Where to put XML**

Any of these roots are discovered:

```
PRODUCTS/*/*/domains/*/ata/*/S1000D
PRODUCTS/*/*/ata/*/S1000D
PRODUCTS/*/*/ata/*/s1000d
ata/57/s1000d
ata/*/S1000D
```

**Path preservation & collisions**

* Each discovered root is published under `/S1000D/dm/rootN/` (**N** starts at 1).
* The **entire original subpath is preserved**, so identically named files from different trees no longer clash.

Example published paths:

```
/S1000D/dm/root1/data_modules/descriptive/DMC-...xml
/S1000D/dm/root2/publication_modules/PMC-...xml
```

**Viewer URLs**

* Index page: `/S1000D/`
* Viewer page: `/S1000D/viewer.html?dm=rootN/<subpath>/<file>.xml`
* Raw XML: `/S1000D/dm/rootN/<subpath>/<file>.xml`

*Basic `..` sanitization is applied to the `dm` query param.*

## Local build & preview

```bash
python scripts/ghpages_build.py
# Optional preview:
python -m http.server -d _site 8080
# Then open http://localhost:8080/
```

## CI / Deployment

* Workflow in `.github/workflows/` builds `_site/` and deploys via GitHub Pages.
* Triggers on push to `main` or `master`.

## Notes & limits

* Only local repo files are indexed; no external network fetches occur at runtime.
* For `.gltf`, make sure sidecar URIs are relative paths (non-`data:` URIs get copied).
* `_site/` is ephemeral; don't commit it.