# OrbitRIR project website

English research project page for **OrbitRIR: Frame-Averaged Few-Shot RIR Synthesis for 3D Sound Source Localization**, accepted to the NeurIPS 2026 ESR Workshop.

This standalone repository contains the website only: HTML, CSS, JavaScript, five manuscript figures, and the result tables displayed on the page. It does not contain the research implementation, model weights, raw experiment data, internal review notes, or a provisional manuscript PDF.

## Local preview

```bash
python3 -m http.server 8000
```

Open http://localhost:8000. No package installation or build step is required.

## Files and editing

- `index.html`: complete research page with semantic tables.
- `style.css`, `app.js`, `favicon.svg`: styling, interactive controls, and icon.
- `assets/`: manuscript figures (Figures 1, 2, 3, 4, and 10).
- `results.json`: the paper values displayed in the tables (Tables 1 and 2).
- `scripts/build_content.py`: content and table generator. Edit this file for page text, resource links, citations and results, then run `python3 scripts/build_content.py`.

Edit CSS and JavaScript directly. The site uses relative asset paths and works under a repository subpath.

## Deployment

Publish the repository root as a static site; leave the build command empty. For GitHub Pages, select **Settings → Pages → Deploy from a branch → main → /(root)**. Creating this public source repository does not itself enable GitHub Pages.

## Research content

The page distinguishes finite yaw-group invariance from arbitrary continuous rotation invariance, and reports all comparison baselines without claiming every metric is best. The interactive frame permutation is conceptual; it is not an acoustic simulation.

The paper and research-code resource links are pending. Add verified public URLs when available. The displayed citation is provisional and should be updated against the final public paper.

Figures and research content remain subject to their respective rights. No research-code license or release is implied by publishing this website source.
