gsap.registerPlugin(ScrollTrigger);

// ── NAV SCROLL ──
window.addEventListener('scroll', () => {
  document.getElementById('mainNav').classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

// ── EXPERIENCE STARTER & HERO TIMELINE ──
function startHeroAnimation() {
  // Set initial states for the animation
  gsap.set(['#hBadge', '#hSub', '#hBtns'], { autoAlpha: 0 });
  gsap.set('#typewriter', { autoAlpha: 0 });

  const heroTl = gsap.timeline({ delay: 0.2 });
  heroTl
    .to('#hBadge', { autoAlpha: 1, y: 0, duration: 0.55, ease: 'power2.out' })
    .call(() => { document.getElementById('whooshSfx')?.play().catch(e => console.error("Whoosh SFX failed:", e)); }, [], '-=0.15')
    .from('#line1 .h-word', { opacity: 0, x: -65, stagger: { each: 0.065 }, duration: 0.7, ease: 'power3.out' }, '<')
    .to('#typewriter', { autoAlpha: 1, duration: 0.01 }, "+=0.3")
    .call(() => { document.getElementById('typewriter')?.classList.add('animate'); })
    .call(() => { document.getElementById('glitchSfx')?.play().catch(e => console.error("Glitch SFX failed:", e)); }, [], '+=2.7')
    .from('#line3', { scale: 1.5, opacity: 0, duration: 0.8, ease: 'power2.out' }, "<")
    .to('#hSub',  { autoAlpha: 1, duration: 0.5, ease: 'power2.out' }, '-=0.2')
    .to('#hBtns', { autoAlpha: 1, duration: 0.45, ease: 'power2.out' }, '-=0.25');
}

const startPrompt = document.getElementById('start-prompt');
const heroElements = document.querySelectorAll('#hBadge, #hSub, #hBtns, .h-lines');

// Hide hero content initially, it will be revealed by the animation
gsap.set(heroElements, { autoAlpha: 0 });

if (startPrompt) {
  const startHandler = () => {
    // Fade out the prompt
    gsap.to(startPrompt, {
      opacity: 0,
      duration: 0.6,
      ease: 'power1.inOut',
      onComplete: () => {
        startPrompt.style.display = 'none';
        gsap.set('.h-lines', { autoAlpha: 1 }); // Make the lines container visible before animation
        startHeroAnimation();
      }
    });
    startPrompt.removeEventListener('click', startHandler);
  };
  startPrompt.addEventListener('click', startHandler);
}

// ── SCROLL REVEALS — individual .ry elements ──
gsap.utils.toArray('.ry').forEach(el => {
  gsap.to(el, {
    opacity: 1, y: 0,
    duration: 0.7, ease: 'power2.out',
    scrollTrigger: { trigger: el, start: 'top 82%' }
  });
});

// .rx elements (x-direction)
gsap.utils.toArray('.rx').forEach(el => {
  gsap.to(el, {
    opacity: 1, x: 0,
    duration: 0.7, ease: 'power2.out',
    scrollTrigger: { trigger: el, start: 'top 82%' }
  });
});

// ── STAGGERED GROUPS ──
// Step cards
ScrollTrigger.batch('.s-card', {
  onEnter: batch => gsap.to(batch, {
    opacity: 1, scale: 1,
    stagger: 0.16, duration: 0.7, ease: 'back.out(1.3)'
  }),
  start: 'top 78%'
});

// Bento boxes
ScrollTrigger.batch('.bb', {
  onEnter: batch => gsap.to(batch, {
    opacity: 1, y: 0,
    stagger: 0.1, duration: 0.65, ease: 'power2.out'
  }),
  start: 'top 80%'
});

// Pills
ScrollTrigger.batch('.pill', {
  onEnter: batch => gsap.to(batch, {
    opacity: 1, x: 0,
    stagger: 0.08, duration: 0.5, ease: 'power2.out'
  }),
  start: 'top 85%'
});

// Price cards
ScrollTrigger.batch('.pc', {
  onEnter: batch => gsap.to(batch, {
    opacity: 1, y: 0,
    stagger: 0.2, duration: 0.65, ease: 'power2.out'
  }),
  start: 'top 78%'
});

// ── MAGNETIC BUTTONS ──
document.querySelectorAll('.magnetic').forEach(btn => {
  btn.addEventListener('mousemove', e => {
    const r = btn.getBoundingClientRect();
    const x = (e.clientX - r.left  - r.width  / 2) * 0.26;
    const y = (e.clientY - r.top   - r.height / 2) * 0.26;
    gsap.to(btn, { x, y, duration: 0.4, ease: 'power2.out' });
  });
  btn.addEventListener('mouseleave', () => {
    gsap.to(btn, { x: 0, y: 0, duration: 0.75, ease: 'elastic.out(1, 0.4)' });
  });
});

// ── FORM SUBMIT ──
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  gsap.to(this, {
    opacity: 0, y: -10, duration: 0.3,
    onComplete: () => {
      this.style.display = 'none';
      const ok = document.getElementById('ok');
      ok.style.display = 'block';
      gsap.from(ok, { opacity: 0, y: 20, duration: 0.5, ease: 'power2.out' });
    }
  });
});

// ── SMOOTH NAV ANCHORS ──
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
  });
});