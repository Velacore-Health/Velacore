/* Velacore Health — interactivity */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Learn page: peptide walk-through
  Array.prototype.forEach.call(document.querySelectorAll('[data-pepwalk]'), function (w) {
    var steps = w.querySelectorAll('.pw-step');
    var btns = w.querySelectorAll('[data-go]');
    var cap = w.querySelector('.pw-cap');
    Array.prototype.forEach.call(btns, function (b, i) {
      b.addEventListener('click', function () {
        Array.prototype.forEach.call(steps, function (s, k) { s.classList.toggle('is-on', k === i); });
        Array.prototype.forEach.call(btns, function (x, k) { x.setAttribute('aria-pressed', String(k === i)); });
        cap.textContent = b.getAttribute('data-cap');
      });
    });
  });

  // Year in footer
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Slide-in menu, Nov 17 2026. One panel on every page; nothing stored, nothing sent.
  (function () {
    var btn = document.getElementById('menuBtn'), panel = document.getElementById('sidePanel'), overlay = document.getElementById('panelOverlay'), closeBtn = document.getElementById('panelClose');
    if (!btn || !panel || !overlay || !closeBtn) return;
    var timer = null;
    function focusables() { return Array.prototype.filter.call(panel.querySelectorAll('a[href], button'), function (el) { return el.offsetParent !== null; }); }
    function open() {
      clearTimeout(timer); panel.hidden = false; overlay.hidden = false;
      panel.setAttribute('aria-hidden', 'false'); btn.setAttribute('aria-expanded', 'true'); document.body.classList.add('panel-open');
      requestAnimationFrame(function () { panel.classList.add('is-open'); overlay.classList.add('is-open'); });
      closeBtn.focus();
    }
    function close(returnFocus) {
      panel.classList.remove('is-open'); overlay.classList.remove('is-open');
      panel.setAttribute('aria-hidden', 'true'); btn.setAttribute('aria-expanded', 'false'); document.body.classList.remove('panel-open');
      timer = setTimeout(function () { panel.hidden = true; overlay.hidden = true; }, reduce ? 0 : 320);
      if (returnFocus) btn.focus();
    }
    btn.addEventListener('click', function () { panel.classList.contains('is-open') ? close(true) : open(); });
    closeBtn.addEventListener('click', function () { close(true); });
    overlay.addEventListener('click', function () { close(true); });
    panel.addEventListener('click', function (e) { if (e.target.closest('a')) close(false); });
    document.addEventListener('keydown', function (e) {
      if (!panel.classList.contains('is-open')) return;
      if (e.key === 'Escape') { close(true); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(); if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  })();

  // Stepper on How it works, Nov 17 2026: the word for the step nearest the middle of the screen is lit
  var stepper = document.querySelector('[data-stepper]');
  if (stepper && 'IntersectionObserver' in window) {
    var words = [].slice.call(stepper.children), stepEls = [].slice.call(document.querySelectorAll('.hw-step'));
    var light = function (i) { words.forEach(function (w, k) { w.classList.toggle('is-on', k === i); if (k === i) w.querySelector('a').setAttribute('aria-current', 'step'); else w.querySelector('a').removeAttribute('aria-current'); }); };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) light(stepEls.indexOf(e.target)); });
    }, { rootMargin: '-40% 0px -40% 0px', threshold: 0 });
    stepEls.forEach(function (el) { io.observe(el); });
  }

  // Phone footer as an accordion, Nov 17 2026: the script adds the class, so links stay visible without it
  var fgrid = document.querySelector('.footer-grid');
  if (fgrid && window.matchMedia('(max-width:640px)').matches) {
    fgrid.classList.add('footer-acc');
    fgrid.querySelectorAll('.footer-col h4').forEach(function (h) {
      var col = h.parentNode; h.setAttribute('role', 'button'); h.tabIndex = 0; h.setAttribute('aria-expanded', 'false');
      var flip = function () { var open = col.classList.toggle('is-open'); h.setAttribute('aria-expanded', open ? 'true' : 'false'); };
      h.addEventListener('click', flip);
      h.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); flip(); } });
    });
  }

  // Treatments dropdown: tap to open on phones, keyboard friendly everywhere
  document.querySelectorAll('.has-mega > a').forEach(function (trigger) {
    trigger.addEventListener('click', function (e) {
      var narrow = window.matchMedia('(max-width: 780px)').matches;
      var item = trigger.parentNode;
      if (narrow || !item.classList.contains('open') && e.detail === 0) {
        e.preventDefault();
        e.stopPropagation();
        var open = item.classList.toggle('open');
        trigger.setAttribute('aria-expanded', String(open));
      }
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.has-mega.open').forEach(function (item) {
      if (!item.contains(e.target)) { item.classList.remove('open'); item.querySelector('a').setAttribute('aria-expanded', 'false'); }
    });
  });

  // FAQ: one open at a time
  var faq = document.getElementById('faqList');
  if (faq) {
    var items = faq.querySelectorAll('details');
    items.forEach(function (item) {
      item.addEventListener('toggle', function () {
        if (item.open) items.forEach(function (o) { if (o !== item) o.open = false; });
      });
    });
  }

  // Treatment filter
  var filterBtns = document.querySelectorAll('.filter');
  var cards = document.querySelectorAll('#tgrid .tcard');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.getAttribute('data-filter');
      filterBtns.forEach(function (b) { b.classList.toggle('is-active', b === btn); });
      cards.forEach(function (card) {
        var cat = card.getAttribute('data-cat');
        var show = f === 'all' || cat === f || cat === 'all';
        card.style.display = show ? '' : 'none';
      });
    });
  });

  // Program row that slides, Nov 17 2026: drag with a mouse, swipe with a thumb, the two arrows, or arrow keys on the row.
  document.querySelectorAll('[data-prow]').forEach(function (root) {
    var track = root.querySelector('.prow-track'), prev = root.querySelector('[data-prev]'), next = root.querySelector('[data-next]');
    if (!track) return;
    function step() { var c = [].filter.call(track.querySelectorAll('.tcard'), function (x) { return x.offsetParent; })[0]; return c ? c.getBoundingClientRect().width + 18 : 300; }
    function sync() {
      var max = track.scrollWidth - track.clientWidth;
      if (prev) prev.disabled = track.scrollLeft <= 2;
      if (next) next.disabled = track.scrollLeft >= max - 2;
      root.classList.toggle('at-end', track.scrollLeft >= max - 2);
    }
    function by(dx) { track.scrollBy({ left: dx, behavior: reduce ? 'auto' : 'smooth' }); }
    if (prev) prev.addEventListener('click', function () { by(-step()); });
    if (next) next.addEventListener('click', function () { by(step()); });
    track.addEventListener('scroll', sync); window.addEventListener('resize', sync); window.addEventListener('load', sync); sync();
    track.addEventListener('keydown', function (e) {
      if (e.target !== track) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); by(step()); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); by(-step()); }
    });
    // Mouse drag. Touch scrolls natively. A drag never counts as a click on a card.
    var x0 = null, s0 = 0, moved = false;
    track.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse' || e.button !== 0) return;
      x0 = e.clientX; s0 = track.scrollLeft; moved = false;
    });
    track.addEventListener('pointermove', function (e) {
      if (x0 === null) return;
      var dx = e.clientX - x0;
      if (!moved && Math.abs(dx) > 6) { moved = true; track.classList.add('is-dragging'); track.setPointerCapture(e.pointerId); }
      if (moved) track.scrollLeft = s0 - dx;
    });
    function end() {
      if (x0 === null) return;
      x0 = null;
      if (moved) {
        track.classList.remove('is-dragging');
        var block = function (ev) { ev.preventDefault(); ev.stopPropagation(); };
        track.addEventListener('click', block, true);
        setTimeout(function () { track.removeEventListener('click', block, true); }, 60);
      }
    }
    track.addEventListener('pointerup', end); track.addEventListener('pointercancel', end);
    track.addEventListener('dragstart', function (e) { e.preventDefault(); });
    filterBtns.forEach(function (b) { b.addEventListener('click', function () { track.scrollTo({ left: 0, behavior: 'auto' }); setTimeout(sync, 30); }); });
  });

  // Find your program chooser, Nov 17 2026. Two answers, then the matching program cards, cloned from the
  // program list so prices and wording exist in one place. Nothing is stored or sent anywhere.
  (function () {
    var root = document.querySelector('[data-chooser]');
    if (!root) return;
    var MAP = {
      weight: { inject: ['tirzepatide', 'semaglutide', 'microdosing'], noneedle: ['semaglutide', 'microdosing'] },
      vitality: { inject: ['nad', 'glutathione'], noneedle: ['nad', 'glutathione'] },
      hormone: { inject: ['sermorelin'], noneedle: ['sermorelin'] }
    };
    var NOTE = {
      'weight|inject': 'Three GLP-1 programs. Tirzepatide is an injection. Semaglutide comes as an injection or an oral form. Microdosing GLP-1 is a lower dose, as an oral form or an injection. The clinician decides which program, if any, is appropriate for you.',
      'weight|noneedle': 'Semaglutide and Microdosing GLP-1 both come in an oral form. Tirzepatide is an injection only. The clinician decides the program and the form.',
      'vitality|inject': 'Two programs. NAD+ comes as an injection, a nasal spray or an oral dropper. Glutathione comes in the form the clinician prescribes.',
      'vitality|noneedle': 'NAD+ comes as a nasal spray or an oral dropper as well as an injection. Glutathione comes in the form the clinician prescribes. The clinician decides the form.',
      'hormone|inject': 'One program. Sermorelin is an injection. The clinician decides whether it is appropriate for you.',
      'hormone|noneedle': 'Sermorelin is an injection only. There is no spray, dropper or tablet option for this program today. The clinician decides whether it is appropriate for you.'
    };
    var TITLE = { weight: 'Weight programs that may fit', vitality: 'Vitality programs that may fit', hormone: 'The hormone support program' };
    var goal = null;
    function show(n) {
      root.querySelectorAll('.ch-step').forEach(function (s) { s.hidden = s.getAttribute('data-step') !== String(n); });
      root.querySelectorAll('.ch-track li').forEach(function (li) {
        var k = +li.getAttribute('data-track');
        li.classList.toggle('is-on', k === n); li.classList.toggle('is-done', k < n);
      });
      var top = root.getBoundingClientRect().top + window.pageYOffset - 96;
      window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
      var q = root.querySelector('.ch-step:not([hidden]) .ch-q');
      if (q) { q.setAttribute('tabindex', '-1'); q.focus({ preventScroll: true }); }
    }
    root.querySelectorAll('.goal-tile[data-goal]').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); goal = a.getAttribute('data-goal'); show(2); });
    });
    // the hero menu rows pick a goal from anywhere on the page
    document.querySelectorAll('[data-pick-goal]').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); goal = a.getAttribute('data-pick-goal'); show(2); });
    });
    root.querySelectorAll('[data-form]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (!goal) { show(1); return; }
        var form = b.getAttribute('data-form');
        var out = document.getElementById('chResults'); out.innerHTML = '';
        MAP[goal][form].forEach(function (slug) {
          var src = document.querySelector('.tcard [data-start="' + slug + '"]');
          if (!src) return;
          var card = src.closest('.tcard').cloneNode(true);
          
          card.removeAttribute('data-d'); card.removeAttribute('style'); card.removeAttribute('aria-hidden');
          card.querySelectorAll('img').forEach(function (i) { i.loading = 'eager'; });
          card.querySelectorAll('a, button').forEach(function (el) { el.removeAttribute('tabindex'); });
          // needle-free answer: where the program has an oral tile, the card shows the oral form, its photo and its price, read from that tile
          var oral = form === 'noneedle' && document.querySelector('[data-oral="' + slug + '"]');
          if (oral) {
            var oimg = oral.querySelector('img'), oline = oral.querySelector('p').textContent, oprice = (oline.match(/\$\d+/) || [''])[0];
            var cimg = card.querySelector('.tcard-photo'); if (cimg) { cimg.src = oimg.src; cimg.alt = oimg.alt; }
            card.querySelector('.tcard-mech').textContent = oline.replace(/\s*\$\d+ a month\.?$/, '');
            card.querySelector('.tcard-price').innerHTML = oprice + ' <small>a month, oral form</small>';
            var cplan = card.querySelector('.tcard-plan'); if (cplan) cplan.remove();
            var clink = card.querySelector('.tcard-link'); if (clink) clink.href = oral.querySelector('a').getAttribute('href');
          }
          out.appendChild(card);
        });
        document.getElementById('chTitle').textContent = TITLE[goal];
        document.getElementById('chNote').textContent = NOTE[goal + '|' + form];
        show(3);
      });
    });
    // arriving from the menu on another page: #goals-weight opens step 2 with that goal picked
    var m = /^#goals-(weight|vitality|hormone)$/.exec(window.location.hash);
    if (m) { goal = m[1]; show(2); if (history.replaceState) history.replaceState(null, '', '#goals'); }
    root.querySelectorAll('[data-ch-back]').forEach(function (b) {
      b.addEventListener('click', function () { var n = +b.getAttribute('data-ch-back'); if (n === 1) goal = null; show(n); });
    });
  })();

  // Funnel, Nov 13 2026. Goal tiles open the matching filter in the program list.
  Array.prototype.forEach.call(Array.prototype.filter.call(document.querySelectorAll('a[data-goal][href="#treatments"]'), function (a) { return !a.closest('[data-chooser]'); }), function (a) {
    a.addEventListener('click', function (e) {
      var btn = document.querySelector('.filter[data-filter="' + a.getAttribute('data-goal') + '"]');
      var sec = document.getElementById('treatments');
      if (!btn || !sec) return;
      e.preventDefault();
      btn.click();
      sec.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      if (history.replaceState) history.replaceState(null, '', '#treatments');
    });
  });

  // Start pages: carry the ad's UTM tags into the partner's intake link.
  (function () {
    var q = window.location.search;
    if (!q || q.indexOf('utm_') === -1) return;
    var keep = q.slice(1).split('&').filter(function (kv) { return kv.indexOf('utm_') === 0; }).join('&');
    if (!keep) return;
    Array.prototype.forEach.call(document.querySelectorAll('a[data-intake], a[data-start]'), function (a) {
      var href = a.getAttribute('href');
      if (!href || href === '#') return;
      a.setAttribute('href', href + (href.indexOf('?') === -1 ? '?' : '&') + keep);
    });
  })();

  // Intake links: placeholders stay put until the hosted intake URLs are set; real links fire a GA4 event
  document.querySelectorAll('a[data-intake]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (a.getAttribute('aria-disabled') === 'true' || a.getAttribute('href') === '#') {
        e.preventDefault();
        return;
      }
      if (typeof gtag === 'function') {
        gtag('event', 'start_visit_click', { product: a.getAttribute('data-intake'), link_url: a.href });
      }
    });
  });

  // Program pages: plan selector updates the price box
  var planInputs = document.querySelectorAll('.plan-option input');
  if (planInputs.length) {
    var priceEl = document.getElementById('planPrice');
    var unitEl = document.getElementById('planUnit');
    var noteEl = document.getElementById('planNote');
    planInputs.forEach(function (inp) {
      inp.addEventListener('change', function () {
        if (!inp.checked) return;
        priceEl.childNodes[0].nodeValue = inp.getAttribute('data-price');
        unitEl.textContent = inp.getAttribute('data-unit');
        noteEl.textContent = inp.getAttribute('data-note');
      });
    });
  }

  // Sticky mobile CTA: shown only after the hero scrolls away, hidden again on the start section
  var mobileCta = document.getElementById('mobileCta');
  var heroSec = document.querySelector('.hero, .hub, .prog-hero');
  var intakeSec = document.getElementById('intake') || document.getElementById('start');
  if (mobileCta && 'IntersectionObserver' in window) {
    var heroVisible = !!heroSec, intakeVisible = false, carVisible = false; // pages without a hero show the bar at once
    var carSec = document.querySelector('[data-prow]');
    var update = function () {
      var show = !heroVisible && !intakeVisible && !carVisible;
      mobileCta.classList.toggle('is-shown', show);
      mobileCta.classList.toggle('is-hidden', !show);
    };
    if (heroSec) new IntersectionObserver(function (e) { heroVisible = e[0].isIntersecting; update(); }, { threshold: 0.1 }).observe(heroSec);
    if (intakeSec) new IntersectionObserver(function (e) { intakeVisible = e[0].isIntersecting; update(); }, { threshold: 0.05 }).observe(intakeSec);
    if (carSec) new IntersectionObserver(function (e) { carVisible = e[0].isIntersecting; update(); }, { threshold: 0.05 }).observe(carSec);
    update();
  }

})();
