/* Velacore Health — interactivity */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Year in footer
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
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        links.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

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

  // Scroll reveal (safe: content visible by default; CSS animates on .is-visible)
  if ('IntersectionObserver' in window && !reduce) {
    var revealEls = document.querySelectorAll('.tcard, .pillar, .step');
    revealEls.forEach(function (el) { el.classList.add('reveal'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  // Sticky mobile CTA: hide while the intake section is on screen
  var mobileCta = document.getElementById('mobileCta');
  var intakeSec = document.getElementById('intake');
  if (mobileCta && intakeSec && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      mobileCta.classList.toggle('is-hidden', entries[0].isIntersecting);
    }, { threshold: 0.05 }).observe(intakeSec);
  }

  // Hero molecular node field (Canvas — innovative ambient motion)
  var canvas = document.getElementById('molecule');
  if (canvas && canvas.getContext) {
    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var nodes = [];
    var W = 0, H = 0, raf = null;

    function size() {
      var rect = canvas.getBoundingClientRect();
      W = rect.width; H = rect.height;
      canvas.width = W * dpr; canvas.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function build() {
      var count = Math.max(22, Math.min(56, Math.round(W / 26)));
      nodes = [];
      for (var i = 0; i < count; i++) {
        nodes.push({
          x: Math.random() * W,
          y: Math.random() * H,
          vx: (Math.random() - 0.5) * 0.32,
          vy: (Math.random() - 0.5) * 0.32,
          r: Math.random() * 1.8 + 1.1
        });
      }
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        a.x += a.vx; a.y += a.vy;
        if (a.x < 0 || a.x > W) a.vx *= -1;
        if (a.y < 0 || a.y > H) a.vy *= -1;
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j];
          var dx = a.x - b.x, dy = a.y - b.y;
          var d = Math.sqrt(dx * dx + dy * dy);
          if (d < 130) {
            ctx.globalAlpha = (1 - d / 130) * 0.22;
            ctx.strokeStyle = '#57D9B6';
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
      }
      ctx.globalAlpha = 0.85;
      for (var k = 0; k < nodes.length; k++) {
        var n = nodes[k];
        ctx.fillStyle = '#57D9B6';
        ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2); ctx.fill();
      }
      ctx.globalAlpha = 1;
      raf = requestAnimationFrame(draw);
    }

    function start() { size(); build(); if (!reduce) { if (raf) cancelAnimationFrame(raf); draw(); } else { draw(); cancelAnimationFrame(raf); } }
    start();
    var t;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(start, 200); });
    // Pause when hero is offscreen (perf)
    if ('IntersectionObserver' in window && !reduce) {
      new IntersectionObserver(function (e) {
        if (e[0].isIntersecting) { if (!raf) draw(); }
        else { if (raf) { cancelAnimationFrame(raf); raf = null; } }
      }, { threshold: 0 }).observe(canvas);
    }
  }
})();
