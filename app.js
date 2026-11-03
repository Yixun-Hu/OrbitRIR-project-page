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
