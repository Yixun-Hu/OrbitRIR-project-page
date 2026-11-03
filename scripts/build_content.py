"""Generate the standalone static page; no third-party dependencies."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>OrbitRIR | Frame-Averaged Few-Shot RIR Synthesis</title>
<meta name="description" content="A geometry-conditioned generative model that uses forward acoustic knowledge to solve inverse localization problems. Frame Averaging for few-shot RIR synthesis and 3D sound source localization.">
<meta name="theme-color" content="#173d39">
<meta property="og:title" content="OrbitRIR: Frame-Averaged Few-Shot RIR Synthesis">
<meta property="og:description" content="A geometry-conditioned generative model that uses forward acoustic knowledge to solve inverse localization problems.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://yixun-hu.github.io/OrbitRIR-project-page/">
<meta property="og:image" content="https://yixun-hu.github.io/OrbitRIR-project-page/assets/pipeline.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://yixun-hu.github.io/OrbitRIR-project-page/">
<link rel="icon" type="image/svg+xml" href="./favicon.svg">
<link rel="stylesheet" href="./style.css"><script src="./app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="nav-row wrap">
<a class="brand" href="#top" aria-label="OrbitRIR, back to top"><img src="./favicon.svg" width="28" height="28" alt="">OrbitRIR</a>
<nav aria-label="Main navigation"><a href="#abstract">Abstract</a><a href="#method">Method</a><a href="#results">Results</a></nav>
</div></header>
<main id="main">
<section class="hero wrap" id="top" aria-labelledby="title">
<p class="eyebrow">NeurIPS 2026 · ESR Workshop</p>
<h1 id="title"><span class="wordmark">Orbit<span>RIR</span></span><span class="paper-title">Frame-Averaged Few-Shot RIR Synthesis<br class="desktop-break"> for 3D Sound Source Localization</span></h1>
<p class="hero-copy">A geometry-conditioned generative model that uses forward acoustic knowledge to solve inverse localization problems.</p>
<div class="authors-scroll"><p class="authors"><a href="https://yixun-hu.github.io/" target="_blank" rel="noopener noreferrer">Yixun Hu</a><span aria-hidden="true">·</span><a href="https://fourierlaplace124-design.github.io/" target="_blank" rel="noopener noreferrer">Zhixuan Zhao</a><span aria-hidden="true">·</span><a href="https://taozhong.info/" target="_blank" rel="noopener noreferrer">Tao Zhong</a><span aria-hidden="true">·</span><a href="https://cablanc.github.io/" target="_blank" rel="noopener noreferrer">Christine Allen-Blanchette</a></p></div>
<p class="affiliation">Princeton University</p>
<div class="release-badges" aria-label="Release status"><span>arXiv <small>Coming soon</small></span><span>Code <small>Coming soon</small></span></div>
</section>

<section class="section abstract-section" id="abstract" aria-labelledby="abstract-title"><div class="wrap">
<div class="section-heading"><h2 id="abstract-title">Abstract</h2></div>
<div class="prose">
<p>Room impulse responses (RIRs) capture how sound interacts with the geometry of a room, making acoustics a rich signal for spatial reasoning. Few-shot acoustic models can predict RIRs from geometry and sparse room observations, but they do not necessarily respect known physical symmetries.</p>
<p>We introduce <strong>OrbitRIR</strong>, a geometry-conditioned generative acoustic model that incorporates receiver-yaw invariance through <strong>Frame Averaging</strong>. By averaging conditioning features over equivalent coordinate frames, OrbitRIR builds this symmetry into the model. The trained generator can then be frozen and inverted for <strong>3D sound source localization</strong> through analysis-by-synthesis, without localization-specific training or fine-tuning. Experiments on AcousticRooms show improved few-shot RIR synthesis and downstream localization relative to the unconstrained FLAC baseline.</p>
</div></div></section>

<section class="section wrap" id="method" aria-labelledby="method-title">
<div class="section-heading"><h2 id="method-title">Method</h2></div>
<p class="section-intro">Learn a room’s acoustic response from panoramic geometry and a few context RIRs. Then use the same forward model to infer where an observed sound originated.</p>
<figure class="figure"><a class="fig-link" href="./assets/pipeline.png" aria-label="Enlarge the OrbitRIR pipeline"><img src="./assets/pipeline.png" width="4000" height="1852" loading="lazy" alt="OrbitRIR training and localization pipeline. Frame-averaged geometry conditions RIR generation; at inference, candidate source positions are scored against an observed response."></a><figcaption><strong>One model, two uses.</strong> Train for few-shot acoustic synthesis, then freeze the generator for source localization.</figcaption></figure>
<div class="method-steps">
<article><span class="step-no">01</span><h3>Condition on the room</h3><p>A panoramic depth map, source coordinates, and sparse acoustic context describe the scene. A latent flow-matching model generates plausible RIRs for a queried source position.</p></article>
<article><span class="step-no">02</span><h3>Average over frames</h3><p>Transform geometry and source coordinates consistently across a finite receiver-yaw orbit. A shared encoder processes each frame, and averaging its features yields invariant conditioning.</p></article>
<article><span class="step-no">03</span><h3>Localize by synthesis</h3><p>Query the frozen generator at candidate 3D positions. Compare synthesized and observed RIRs in the frozen AGREE audio embedding space, and select the most compatible position.</p></article>
</div>
<div class="method-detail"><h3>Frame Averaging: different frames, the same scene</h3>
<p>For an omnidirectional monaural RIR, re-expressing the same scene in a different receiver-yaw coordinate frame should not change its acoustics. Frame Averaging makes the geometry representation invariant to the chosen finite yaw group: a frame change simply reorders the features being averaged.</p>
<figure class="figure"><a class="fig-link" href="./assets/frame-averaging.png" aria-label="Enlarge the Frame Averaging diagram"><img src="./assets/frame-averaging.png" width="4000" height="1791" loading="lazy" alt="Four yaw-aligned panoramic geometry and source-coordinate frames pass through a shared ViT and projection. Their encoded features are averaged into one conditioning representation."></a><figcaption><strong>Frame-averaged conditioning.</strong> The same encoder and projection are applied across the yaw orbit before feature averaging.</figcaption></figure>
<p class="scope-note">The invariance is defined over a finite yaw group, illustrated here with C<sub>4</sub>. It concerns coordinate changes of the same acoustic scene, rather than arbitrary physical rotations of directional sound sources.</p>
</div></section>

<section class="section results-section" id="results" aria-labelledby="results-title"><div class="wrap">
<div class="section-heading"><h2 id="results-title">Results</h2></div>
<p class="section-intro">We evaluate both the forward task—few-shot RIR synthesis—and the inverse task—3D sound source localization in unseen rooms.</p>
<article class="result-block"><h3>Few-shot acoustic synthesis</h3>
<p>OrbitRIR improves all reported synthesis metrics over FLAC in both sparse and dense context settings. Its synthesis quality also stays stable across the evaluated receiver-yaw frames, while FLAC varies with the coordinate frame. Compared with yaw augmentation, the methods exhibit metric-dependent trade-offs: OrbitRIR improves clarity and early-decay errors, while yaw augmentation achieves lower reverberation-time error.</p>
<figure class="figure"><a class="fig-link" href="./assets/yaw-robustness.png" aria-label="Enlarge synthesis results across receiver-yaw frames"><img src="./assets/yaw-robustness.png" width="3338" height="1461" loading="lazy" alt="Six synthesis metrics across four yaw frames, comparing FLAC and OrbitRIR with sparse and dense context. OrbitRIR's curves remain nearly constant across frames."></a><figcaption><strong>Stable across receiver-yaw frames.</strong> Synthesis errors and retrieval recalls on unseen AcousticRooms. Error bars show the standard deviation over evaluation seeds.</figcaption></figure>
</article>
<article class="result-block"><h3>3D sound source localization</h3>
<p>The frozen acoustic generator supports localization without task-specific training. OrbitRIR improves localization over FLAC and achieves the strongest resolution-aware success rate among the compared methods. Results vary by metric: yaw-augmented FLAC has a lower median localization error.</p>
<figure class="figure"><a class="fig-link" href="./assets/localization-results.jpeg" aria-label="Enlarge localization examples in unseen rooms"><img src="./assets/localization-results.jpeg" width="3300" height="1993" loading="lazy" alt="Qualitative OrbitRIR source-localization predictions across six unseen room layouts. Blue circles indicate predicted positions, red crosses indicate ground-truth sources, and dark markers indicate receivers."></a><figcaption><strong>Localization in unseen rooms.</strong> Blue circles: predictions. Red crosses: ground-truth source positions. Dark markers: receivers.</figcaption></figure>
<p class="scope-note">These results use AcousticRooms, registered geometry, sparse acoustic context, and omnidirectional monaural RIRs. Localization searches a finite candidate grid.</p>
</article></div></section>
<section class="release-section wrap" aria-labelledby="release-title"><p class="eyebrow">Stay tuned</p><h2 id="release-title">arXiv and code will be released soon.</h2><p>Links to the paper and research code will appear here when available.</p></section>
</main>
<footer class="site-footer"><div class="wrap"><span>OrbitRIR · Princeton University · 2026</span><a href="https://github.com/Yixun-Hu/OrbitRIR-project-page" target="_blank" rel="noopener noreferrer">Website source ↗</a></div></footer>
<dialog class="figure-dialog" aria-label="Enlarged research figure"><button class="dialog-close" aria-label="Close enlarged figure">Close ×</button><img alt=""><p class="dialog-caption"></p></dialog>
</body>
</html>
'''
(ROOT / 'index.html').write_text(HTML, encoding='utf-8')
