# GitHub Pages — CAD & S1000D

This repo publishes a static site with:
- **/CAD** — WebXR (A-Frame) viewer + `<model-viewer>` fallback for local `.gltf/.glb`
- **/S1000D** — browsable index for DM XML

**Enable Pages** → Settings → Pages → Source: **GitHub Actions**.

Add assets to:
- CAD: `PRODUCTS/*/*/domains/*/cax/CAD/wing_baseline_model/surface_geometry/` or `CAD/wing_baseline_model/surface_geometry/`
- S1000D: `PRODUCTS/*/*/ata/57/s1000d/` or `ata/57/s1000d/`

On push to `main`/`master`, the site deploys automatically.