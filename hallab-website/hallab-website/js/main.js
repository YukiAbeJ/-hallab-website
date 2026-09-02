/* ============================================================
   HAL Lab. — Main JavaScript v2
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {


  /* --- Navigation scroll effect --- */
  const nav = document.querySelector('.nav');
  const onScroll = () => {
    nav?.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* --- Hamburger / Mobile overlay --- */
  const hamburger = document.querySelector('.hamburger');
  const overlay   = document.querySelector('.nav-overlay');

  hamburger?.addEventListener('click', () => {
    const isOpen = hamburger.getAttribute('aria-expanded') === 'true';
    hamburger.setAttribute('aria-expanded', String(!isOpen));
    hamburger.classList.toggle('open', !isOpen);
    overlay?.classList.toggle('open', !isOpen);
    overlay?.setAttribute('aria-hidden', String(isOpen));
    document.body.style.overflow = !isOpen ? 'hidden' : '';
  });

  overlay?.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      hamburger?.setAttribute('aria-expanded', 'false');
      hamburger?.classList.remove('open');
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    });
  });

  /* --- Scroll reveal animation (CSS expects .in class) --- */
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.10, rootMargin: '0px 0px -30px 0px' });

    reveals.forEach(el => observer.observe(el));
  }

  /* --- Smooth scroll for anchor links --- */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        const navH = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-h')) || 72;
        const top = target.getBoundingClientRect().top + window.scrollY - navH - 16;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

});
