'use strict';
document.body.classList.add('js');
const dialog = document.querySelector('.figure-dialog');
document.querySelectorAll('.fig-link').forEach(link => {
  link.addEventListener('click', event => {
    if (!dialog || typeof dialog.showModal !== 'function') return;
    event.preventDefault();
    const original = link.querySelector('img');
    const image = dialog.querySelector('img');
    image.src = link.href;
    image.alt = original.alt;
    dialog.querySelector('.dialog-caption').textContent =
      link.closest('figure').querySelector('figcaption').textContent;
    dialog.showModal();
  });
});
dialog?.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog?.addEventListener('click', event => {
  if (event.target !== dialog) return;
  const bounds = dialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right ||
      event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
});
if ('IntersectionObserver' in window) {
  const links = document.querySelectorAll('nav a');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      links.forEach(link => {
        if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    });
  }, {rootMargin: '-15% 0px -65% 0px'});
  document.querySelectorAll('section[id]').forEach(section => observer.observe(section));
}

const angleButtons = [...document.querySelectorAll('[data-angle]')];
const subscripts = ['₀', '₁', '₂', '₃'];
angleButtons.forEach(button => button.addEventListener('click', () => {
  const offset = Number(button.dataset.angle) / 90;
  angleButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  document.querySelectorAll('.frame-token').forEach((token, index) => {
    const frame = (index + offset) % 4;
    token.querySelector('strong').textContent = 'F' + subscripts[frame];
    token.querySelector('small').textContent = (frame * 90) + '°';
  });
  document.getElementById('orbit-status').textContent =
    button.dataset.angle + '° frame change: the same four features in a different order. Their average is unchanged.';
}));

/* Source images are unchanged; clipping only selects a panel from the paper. */
const localizationMethods = {
  "orbitrir": {
    "label": "OrbitRIR",
    "src": "./assets/localization-results.jpeg",
    "width": 3300,
    "height": 1993,
    "figure": 10,
    "color": "#167dab",
    "rows": [
      83,
      1011
    ],
    "columns": [
      21,
      1109,
      2198
    ]
  },
  "flac": {
    "label": "FLAC",
    "src": "./assets/localization/flac.jpeg",
    "width": 3300,
    "height": 1985,
    "figure": 12,
    "color": "#b98117",
    "rows": [
      75,
      1003
    ],
    "columns": [
      21,
      1109,
      2198
    ]
  },
  "yaw-flac": {
    "label": "Yaw-Augmented FLAC",
    "src": "./assets/localization/yaw-flac.jpeg",
    "width": 3300,
    "height": 1981,
    "figure": 13,
    "color": "#7951ac",
    "rows": [
      71,
      1000
    ],
    "columns": [
      22,
      1109,
      2198
    ]
  },
  "fewshotrir": {
    "label": "Few-ShotRIR (AR-adapted)",
    "src": "./assets/localization/fewshotrir.jpeg",
    "width": 3300,
    "height": 1990,
    "figure": 11,
    "color": "#21866e",
    "rows": [
      79,
      1008
    ],
    "columns": [
      21,
      1109,
      2198
    ]
  },
  "fem": {
    "label": "FEM-Based Localization",
    "src": "./assets/localization/fem.jpeg",
    "width": 3300,
    "height": 1972,
    "figure": 9,
    "color": "#b98117",
    "rows": [
      62,
      991
    ],
    "columns": [
      21,
      1109,
      2198
    ]
  }
};
const localizationRooms = [
  {
    "id": "apartment",
    "label": "Apartment · idx 42"
  },
  {
    "id": "bathroom",
    "label": "Bathroom · idx 18"
  },
  {
    "id": "bedroom",
    "label": "Bedroom · idx 33"
  },
  {
    "id": "living-room",
    "label": "Living room with hallway · idx 25"
  },
  {
    "id": "meeting-room",
    "label": "Meeting room · idx 20"
  },
  {
    "id": "restaurant",
    "label": "Restaurant · idx 24"
  }
];
const comparison = document.getElementById('localization-comparison');
if (comparison) {
  const roomSelect = document.getElementById('comparison-room');
  const methodSelects = ['a', 'b'].map(side => document.getElementById('method-' + side));
  const refreshComparison = () => {
    const roomIndex = localizationRooms.findIndex(room => room.id === roomSelect.value);
    const room = roomIndex < 0 ? null : localizationRooms[roomIndex];
    ['a', 'b'].forEach((side, index) => {
      const method = localizationMethods[methodSelects[index].value];
      const panel = comparison.querySelector('[data-comparison-side="' + side + '"]');
      const viewport = panel.querySelector('.comparison-viewport');
      const image = panel.querySelector('img');
      const row = Math.floor(roomIndex / 3);
      const crop = room
        ? {x: method.columns[roomIndex % 3], y: method.rows[row], w: 1082, h: row === 0 ? 807 : 806}
        : {x: 0, y: 0, w: method.width, h: method.height};
      viewport.style.aspectRatio = crop.w + ' / ' + crop.h;
      image.src = method.src;
      image.alt = method.label + ' — ' + (room ? room.label : 'all six rooms') +
        '. Colored circle: prediction; red cross: ground-truth source; dark marker: receiver.';
      image.style.width = (100 * method.width / crop.w) + '%';
      image.style.height = (100 * method.height / crop.h) + '%';
      image.style.left = (-100 * crop.x / crop.w) + '%';
      image.style.top = (-100 * crop.y / crop.h) + '%';
      panel.querySelector('.prediction-marker').style.setProperty('--prediction-color', method.color);
      panel.querySelector('.prediction-method').textContent = method.label;
      panel.querySelector('.comparison-original').href = method.src;
      panel.querySelector('.comparison-original').setAttribute('aria-label',
        'Open Figure ' + method.figure + ': ' + method.label + ', all six rooms');
    });
    const femSelected = methodSelects.some(select => select.value === 'fem');
    document.getElementById('comparison-query-note').hidden =
      !(femSelected && (roomSelect.value === 'apartment' || roomSelect.value === 'all'));
    document.getElementById('comparison-status').textContent =
      localizationMethods[methodSelects[0].value].label + ' versus ' +
      localizationMethods[methodSelects[1].value].label + ' — ' +
      (room ? room.label : 'all six rooms') + '.';
  };
  roomSelect.addEventListener('change', refreshComparison);
  methodSelects.forEach(select => select.addEventListener('change', refreshComparison));
  document.getElementById('comparison-swap').addEventListener('click', () => {
    const previousA = methodSelects[0].value;
    methodSelects[0].value = methodSelects[1].value;
    methodSelects[1].value = previousA;
    refreshComparison();
  });
  refreshComparison();
}
