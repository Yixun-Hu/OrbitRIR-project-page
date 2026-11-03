# OrbitRIR project website

English project page for **OrbitRIR: Frame-Averaged Few-Shot RIR Synthesis for 3D Sound Source Localization**, accepted to the NeurIPS 2026 ESR Workshop.

Website: https://yixun-hu.github.io/OrbitRIR-project-page/

This standalone repository contains only the website and manuscript figures. The research implementation, model weights, raw experiment data, internal notes, and manuscript PDF are not included. **arXiv and code will be released soon.**

## Local preview

```bash
python3 -m http.server 8000
```

Open http://localhost:8000. No package installation or build step is required.

## Files and editing

- `index.html`: generated static page organized as Abstract, Method, and Results.
- `scripts/build_content.py`: page content source; run `python3 scripts/build_content.py` after editing.
- `style.css`, `app.js`, `favicon.svg`: presentation, accessible figure enlargement, and icon.
- `assets/`: manuscript figures. Figures 2, 3, 4, and 9–13 appear on the page; the conceptual teaser is retained as an asset.
- `results.json`: previously transcribed manuscript tables for reference; not loaded or displayed by the page.

The four author names stay on a single row. On narrow screens, the author row can scroll horizontally without making the page overflow. Figures open in a dialog and can be closed with the Close button or Escape.

## Deployment

GitHub Pages serves `main` → `/(root)` from this public website repository. The `.nojekyll` file bypasses Jekyll processing. Asset paths are relative and work under the repository subpath. Commit regenerated `index.html` together with content-source changes.

The private research repository is independent of this deployment.

## Research content

The page summarizes manuscript findings without numerical highlight cards. Frame Averaging enforces invariance over a finite yaw group; localization uses the frozen generator and requires no localization-specific training. The qualitative figures and synthesis plots are original manuscript figures.

Add verified public arXiv and research-code links when those releases are available. Figures and research content remain subject to their respective rights; publishing this website does not release or license the research implementation.

## Interactive localization comparison

Choose Method A, Method B, and one of six rooms, or show all rooms. Swap A/B to exchange the panels. The five available methods are OrbitRIR, FLAC, Yaw-Augmented FLAC, Few-ShotRIR (AR-adapted), and FEM-Based Localization. The original manuscript JPEGs are preserved; the browser clips a room viewport without redrawing predictions. Full-figure links retain the original context.

`assets/localization/sources.json` records figure numbers, dimensions, and crop coordinates. The FEM apartment source panel uses different receiver/source positions from the other apartment panels, and the interface explicitly labels that combination. Random Selection has no qualitative figure in the manuscript and is not offered as a visual option. The existing Frame Averaging interaction remains in Method.
