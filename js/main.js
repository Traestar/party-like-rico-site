/* ============================================================
   PARTY LIKE RICO PROMOTIONS LLC – Main JavaScript
   ============================================================ */

/* ── Scroll Progress Bar ── */
function initProgressBar() {
  const bar = document.getElementById('progress-bar');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
    bar.style.width = pct + '%';
  });
}

/* ── Sticky Header ── */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── Mobile Navigation ── */
function initMobileNav() {
  const toggle = document.querySelector('.menu-toggle');
  const nav    = document.querySelector('.main-nav');
  const overlay = document.querySelector('.nav-overlay');
  if (!toggle || !nav) return;

  const open = () => {
    toggle.classList.add('open');
    nav.classList.add('open');
    overlay && overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  };
  const close = () => {
    toggle.classList.remove('open');
    nav.classList.remove('open');
    overlay && overlay.classList.remove('active');
    document.body.style.overflow = '';
  };

  toggle.addEventListener('click', () => toggle.classList.contains('open') ? close() : open());
  overlay && overlay.addEventListener('click', close);

  // Close on nav link click
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', close));
}

/* ── Active Nav Link ── */
function setActiveNav() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });
}

/* ── Scroll Animations ── */
function initScrollAnimations() {
  const els = document.querySelectorAll('[data-animate]');
  if (!els.length) return;
  const obs = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        const delay = (e.target.dataset.animateDelay || e.target.dataset.delay || 0) * 100;
        setTimeout(() => e.target.classList.add('visible'), delay);
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  els.forEach(el => obs.observe(el));
}

/* ── FAQ Accordion ── */
function initFAQ() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', () => {
      const open = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      if (!open) item.classList.add('open');
    });
  });
}

/* ── Event Filters (Events Page) ── */
function initEventFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn[data-filter]');
  const filterMonth = document.getElementById('filter-month');
  const cards = document.querySelectorAll('.event-card');
  if (!filterBtns.length && !filterMonth) return;

  let activeType = 'all';
  let activeMonth = 'all';

  function applyFilters() {
    cards.forEach(card => {
      const type  = card.dataset.type  || '';
      const month = card.dataset.month || '';
      const featured = card.dataset.featured || '';

      const typeMatch  = activeType === 'all' || activeType === type || (activeType === 'featured' && featured === 'true');
      const monthMatch = activeMonth === 'all' || activeMonth === month;

      card.hidden = !(typeMatch && monthMatch);
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeType = btn.dataset.filter;
      applyFilters();
    });
  });

  filterMonth && filterMonth.addEventListener('change', () => {
    activeMonth = filterMonth.value;
    applyFilters();
  });
}

/* ── Newsletter Form ── */
function initNewsletterForm() {
  const form = document.getElementById('newsletter-form');
  if (!form) return;
  form.addEventListener('submit', e => {
    e.preventDefault();
    const input = form.querySelector('input[type="email"]');
    if (!input || !input.value) return;
    const btn = form.querySelector('button');
    if (btn) {
      btn.textContent = '✓ Subscribed!';
      btn.style.background = 'var(--green)';
      btn.disabled = true;
    }
  });
}

/* ── Contact / Vendor Form Success ── */
function initFormSuccess() {
  document.querySelectorAll('form[data-netlify]').forEach(form => {
    form.addEventListener('submit', e => {
      // NOTE: For actual Netlify forms, remove the e.preventDefault()
      // Netlify handles the submission automatically.
      // This is just a front-end preview state.
      const successEl = form.parentElement.querySelector('.form-success');
      if (successEl) {
        // e.preventDefault(); // Remove this line for actual Netlify deployment
        // successEl.classList.add('show');
        // form.style.display = 'none';
      }
    });
  });
}

/* ── Calendar ── */
function initCalendar() {
  const calGrid = document.getElementById('calendar-grid');
  const calTitle = document.getElementById('cal-title');
  const prevBtn = document.getElementById('cal-prev');
  const nextBtn = document.getElementById('cal-next');
  if (!calGrid) return;

  // Events data
  // REPLACE: Add your actual events here
  const events = [
    { date: '2026-04-18', title: '420 AC Bud Crawl', type: 'green', url: 'event-detail.html' },
    { date: '2026-05-25', title: 'Memorial Day Bash', type: 'gold', url: '#' },
    { date: '2026-06-20', title: 'Summer Kickoff', type: 'green', url: '#' },
    { date: '2026-07-04', title: '4th of July Party', type: 'gold', url: '#' },
    { date: '2026-08-15', title: 'Summer Crawl', type: 'green', url: '#' },
  ];

  let current = new Date(2026, 3, 1); // April 2026

  function render() {
    const year = current.getFullYear();
    const month = current.getMonth();
    calTitle.textContent = current.toLocaleString('default', { month: 'long', year: 'numeric' });

    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const daysInPrev  = new Date(year, month, 0).getDate();
    const today = new Date();

    calGrid.innerHTML = '';
    // Day names
    ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].forEach(d => {
      calGrid.innerHTML += `<div class="cal-day-name">${d}</div>`;
    });

    // Prev month tail
    for (let i = 0; i < firstDay; i++) {
      calGrid.innerHTML += `<div class="cal-cell other-month"><span class="cal-num">${daysInPrev - firstDay + 1 + i}</span></div>`;
    }

    // Current month
    for (let d = 1; d <= daysInMonth; d++) {
      const dateStr = `${year}-${String(month+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
      const dayEvents = events.filter(e => e.date === dateStr);
      const isToday = today.getFullYear() === year && today.getMonth() === month && today.getDate() === d;
      const hasEvent = dayEvents.length > 0;

      let evHtml = dayEvents.map(ev =>
        `<a href="${ev.url}" class="cal-event ${ev.type}">${ev.title}</a>`
      ).join('');

      calGrid.innerHTML += `
        <div class="cal-cell${isToday ? ' today' : ''}${hasEvent ? ' has-event' : ''}">
          <span class="cal-num">${d}</span>
          ${evHtml}
        </div>`;
    }

    // Next month fill
    const total = firstDay + daysInMonth;
    const remaining = total % 7 === 0 ? 0 : 7 - (total % 7);
    for (let i = 1; i <= remaining; i++) {
      calGrid.innerHTML += `<div class="cal-cell other-month"><span class="cal-num">${i}</span></div>`;
    }
  }

  prevBtn && prevBtn.addEventListener('click', () => { current.setMonth(current.getMonth() - 1); render(); });
  nextBtn && nextBtn.addEventListener('click', () => { current.setMonth(current.getMonth() + 1); render(); });
  render();
}

/* ── Gallery Lightbox (simple) ── */
function initGallery() {
  document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', () => {
      const label = item.querySelector('.gallery-placeholder')?.textContent || 'Image';
      // For a real lightbox, replace this with your preferred lightbox library
      console.log('Open lightbox for:', label);
    });
  });
}

/* ── Smooth Scroll for anchor links ── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id === '#') return;
      const el = document.querySelector(id);
      if (el) {
        e.preventDefault();
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

/* ── Init ── */
document.addEventListener('DOMContentLoaded', () => {
  initProgressBar();
  initStickyHeader();
  initMobileNav();
  setActiveNav();
  initScrollAnimations();
  initNavDropdown();
  initImageFallbacks();
  initHeroFlyer();
  initFAQ();
  initEventFilters();
  initNewsletterForm();
  initFormSuccess();
  initCalendar();
  initGallery();
  initSmoothScroll();
});

/* ── Nav Dropdown — keyboard + hover support ── */
function initNavDropdown() {
  const drops = document.querySelectorAll('.has-dropdown');
  drops.forEach(item => {
    const link = item.querySelector(':scope > a');
    const menu = item.querySelector('.nav-dropdown');
    if (!link || !menu) return;
    // Keyboard toggle
    link.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const open = menu.style.display === 'block';
        menu.style.display = open ? '' : 'block';
      }
    });
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!item.contains(e.target)) {
        menu.style.display = '';
      }
    });
  });
}

/* ── Image Error Fallback — hide broken img, show sibling placeholder ── */
function initImageFallbacks() {
  document.querySelectorAll('img[src]').forEach(img => {
    if (img.hasAttribute('data-fallback-init')) return;
    img.setAttribute('data-fallback-init', '1');
    img.addEventListener('error', function() {
      this.style.display = 'none';
      // Show next sibling ph-layer if exists
      const ph = this.parentElement && this.parentElement.querySelector('.ph-layer, .gallery-ph, .g-ph');
      if (ph) ph.style.display = 'flex';
    });
  });
}

/* ── Hero flyer placeholder visibility ── */
function initHeroFlyer() {
  const img = document.querySelector('.hero-flyer-img img');
  const ph  = document.getElementById('flyer-ph');
  if (!img || !ph) return;
  if (img.complete && (img.naturalWidth === 0 || img.naturalHeight === 0)) {
    ph.style.display = 'flex';
  } else {
    img.addEventListener('load',  () => { ph.style.display = 'none'; });
    img.addEventListener('error', () => { ph.style.display = 'flex'; });
  }
}


/* ── Dropdown Nav ── */
function initDropdowns() {
  const dropItems = document.querySelectorAll('.nav-item-dropdown');
  dropItems.forEach(item => {
    // Mobile: toggle on click
    const trigger = item.querySelector('.nav-dropdown-trigger');
    if (trigger) {
      trigger.addEventListener('click', (e) => {
        if (window.innerWidth <= 1024) {
          e.preventDefault();
          item.classList.toggle('open');
        }
      });
    }
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!item.contains(e.target)) item.classList.remove('open');
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initDropdowns();
});
