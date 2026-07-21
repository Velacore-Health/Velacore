/* Velacore Health — light interactivity */
(function () {
  'use strict';

  // Current year in footer
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile nav toggle
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });
    // Close menu after choosing a link
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        links.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // FAQ: keep only one item open at a time
  var faq = document.getElementById('faqList');
  if (faq) {
    var items = faq.querySelectorAll('details');
    items.forEach(function (item) {
      item.addEventListener('toggle', function () {
        if (item.open) {
          items.forEach(function (other) {
            if (other !== item) other.open = false;
          });
        }
      });
    });
  }

  // Lead form (demo handler — replace with your intake provider)
  var form = document.getElementById('leadForm');
  var success = document.getElementById('formSuccess');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      // TODO: send `new FormData(form)` to your CRM / intake endpoint.
      if (success) success.hidden = false;
      form.querySelector('button[type="submit"]').textContent = 'Request received ✓';
      form.querySelectorAll('input, select, button').forEach(function (el) {
        el.disabled = true;
      });
    });
  }

  // Subtle reveal on scroll. Handled purely in CSS via the `.reveal` class so
  // content is ALWAYS visible by default — the class only adds an entrance
  // animation when it scrolls into view, and can never leave a section blank.
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var revealEls = document.querySelectorAll('.step, .prog, .pillar, .stat');
    revealEls.forEach(function (el) { el.classList.add('reveal'); });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });

    revealEls.forEach(function (el) { io.observe(el); });
  }
})();
