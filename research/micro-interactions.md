# Micro-Interactions & Scroll-Driven Animations Research (2025–2026)

## 1. Scroll-Driven Animations

### CSS Native: `animation-timeline`

The CSS `animation-timeline` property (Baseline 2024+, now widely supported in 2025–2026) enables scroll-linked animations without JavaScript:

```css
/* Scroll progress timeline — animation tied to scroll position */
.progress-bar {
  animation: grow linear;
  animation-timeline: scroll();        /* anonymous: nearest scroller */
}

/* View progress timeline — triggers when element enters/leaves viewport */
.reveal-on-scroll {
  animation: fadeSlideIn linear;
  animation-timeline: view();
  animation-range: entry 0% entry 100%; /* animate during entry */
}
```

**Key functions:**
- `scroll()` — binds animation to scroll position of a container
- `view()` — binds animation to element visibility within scroller
- Named timelines via `scroll-timeline-name` / `view-timeline-name` for complex choreography

**Best for:** Simple parallax, progress indicators, fade-in reveals. Pure CSS, zero JS overhead.

### GSAP ScrollTrigger (Power User Choice)

GSAP's ScrollTrigger remains the gold standard for complex scroll choreography:

```js
gsap.to(".parallax-bg", {
  scrollTrigger: {
    trigger: ".hero",
    start: "top top",
    end: "bottom top",
    scrub: true,           // smooth scrub tied to scroll
    pin: true,             // pin element during animation
  },
  y: -200,
  scale: 1.2,
});
```

**Key features for portfolio use:**
- `scrub: true` — animation progress = scroll progress (smooth, feels native)
- `pin` — lock sections in place while content animates around them
- `snap` — snap to keyframes/sections for discrete page-flip feel
- `batch()` — stagger animations across multiple elements as they enter
- `getVelocity()` — measure scroll speed for velocity-responsive effects

### Scroll-Snapping for Page-Flip Feel

```css
.container {
  scroll-snap-type: y mandatory;
}
.section {
  scroll-snap-align: start;
  height: 100vh;
}
```

Combined with GSAP ScrollTrigger `snap`, this creates a "flip book" feel where each scroll gesture lands on a defined section.

---

## 2. Cursor Effects

### Custom Cursor

```css
body { cursor: none; }
.cursor-dot {
  position: fixed;
  width: 8px; height: 8px;
  background: #fff;
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  mix-blend-mode: difference;
  transition: transform 0.1s;
}
.cursor-ring {
  position: fixed;
  width: 40px; height: 40px;
  border: 1px solid rgba(255,255,255,0.5);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9998;
  transition: transform 0.15s ease-out, width 0.3s, height 0.3s;
}
```

### Magnetic Buttons

```js
document.querySelectorAll('.magnetic').forEach(el => {
  el.addEventListener('mousemove', (e) => {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    gsap.to(el, { x: x * 0.3, y: y * 0.3, duration: 0.3, ease: 'power2.out' });
  });
  el.addEventListener('mouseleave', () => {
    gsap.to(el, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.5)' });
  });
});
```

### Cursor Trail

```js
const trail = [];
for (let i = 0; i < 20; i++) {
  const dot = document.createElement('div');
  dot.className = 'trail-dot';
  document.body.appendChild(dot);
  trail.push({ el: dot, x: 0, y: 0 });
}

document.addEventListener('mousemove', (e) => {
  trail[0].x = e.clientX;
  trail[0].y = e.clientY;
});

function animateTrail() {
  for (let i = trail.length - 1; i > 0; i--) {
    trail[i].x += (trail[i-1].x - trail[i].x) * 0.3;
    trail[i].y += (trail[i-1].y - trail[i].y) * 0.3;
    trail[i].el.style.transform = `translate(${trail[i].x}px, ${trail[i].y}px)`;
  }
  requestAnimationFrame(animateTrail);
}
animateTrail();
```

### Cursor as Page-Flip Trigger

The cursor can serve as the "finger" that initiates the flip — on click/hold near page edge, show a curl preview following cursor position, release to flip.

---

## 3. Text Animations

### GSAP SplitText (v3.13+ — Major Rewrite)

```js
// Split into characters with masking for reveal effects
SplitText.create(".title", {
  type: "chars, words",
  mask: "chars",          // wrap each char in overflow:hidden container
  autoSplit: true,        // re-split on resize
  onSplit(self) {
    return gsap.from(self.chars, {
      duration: 0.8,
      y: 80,
      rotateX: -90,
      opacity: 0,
      stagger: 0.03,
      ease: "back.out(1.7)",
    });
  }
});
```

**Key features:**
- `.chars`, `.words`, `.lines` arrays for granular control
- `mask: "lines"` — creates reveal-from-behind effect (overflow hidden per line)
- `autoSplit: true` — responsive re-splitting on viewport changes
- Screen reader accessibility built-in (aria attributes)

### Character-by-Character Scramble Effect

```js
function scrambleText(element, finalText, duration = 1.5) {
  const chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const iterations = Math.ceil(duration / 0.03); // ~33fps
  let frame = 0;

  const interval = setInterval(() => {
    element.textContent = finalText
      .split('')
      .map((char, i) => {
        if (i < frame / iterations * finalText.length) return finalText[i];
        return chars[Math.floor(Math.random() * chars.length)];
      })
      .join('');

    frame++;
    if (frame > iterations) {
      clearInterval(interval);
      element.textContent = finalText;
    }
  }, 30);
}
```

### Morphing Text (Crossfade Between Strings)

```js
function morphText(element, fromText, toText, duration = 1000) {
  const maxLen = Math.max(fromText.length, toText.length);
  const start = performance.now();

  function update(now) {
    const progress = Math.min((now - start) / duration, 1);
    const visible = Math.floor(progress * maxLen);

    let result = '';
    for (let i = 0; i < maxLen; i++) {
      if (i < visible) {
        result += toText[i] || '';
      } else {
        result += fromText[i] || '';
      }
    }
    element.textContent = result;

    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}
```

### Text During Page Flip

- **Phase 1 (0–30% flip):** Characters scatter outward from center with random velocities
- **Phase 2 (30–70% flip):** Scramble/morph text through random characters
- **Phase 3 (70–100% flip):** New title characters assemble with stagger + bounce

---

## 4. Particle Systems & Background Effects

### Canvas Particle System

```js
class Particle {
  constructor(x, y, color) {
    this.x = x; this.y = y;
    this.vx = (Math.random() - 0.5) * 8;
    this.vy = (Math.random() - 0.5) * 8;
    this.life = 1;
    this.decay = 0.01 + Math.random() * 0.02;
    this.size = 2 + Math.random() * 4;
    this.color = color;
  }
  update() {
    this.x += this.vx;
    this.y += this.vy;
    this.vy += 0.05; // gravity
    this.life -= this.decay;
    this.size *= 0.99;
  }
  draw(ctx) {
    ctx.globalAlpha = this.life;
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

// Burst 200 particles at page-flip origin
function burstParticles(x, y) {
  const colors = ['#ff6b35', '#f7c948', '#ff4081', '#00e5ff'];
  for (let i = 0; i < 200; i++) {
    particles.push(new Particle(x, y, colors[i % colors.length]));
  }
}
```

### Background Gradient Morphing

```css
.gradient-bg {
  background: linear-gradient(135deg, #0a0a0a, #1a1a2e, #16213e);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

**During page flip:** Morph gradient from section A colors to section B colors over the flip duration using GSAP:

```js
gsap.to('.gradient-bg', {
  backgroundImage: 'linear-gradient(135deg, #newColor1, #newColor2, #newColor3)',
  duration: 0.8,
  ease: 'power2.inOut',
});
```

### Noise/Grain Overlay

```css
.noise-overlay::after {
  content: '';
  position: fixed;
  inset: 0;
  background: url('data:image/svg+xml,...'); /* inline noise SVG */
  opacity: 0.03;
  pointer-events: none;
  animation: noiseShift 0.5s steps(10) infinite;
}
```

---

## 5. Sound Design Integration

### Web Audio API — Programmatic Sounds

```js
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playClickSound() {
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.connect(gain);
  gain.connect(audioCtx.destination);

  osc.type = 'sine';
  osc.frequency.setValueAtTime(800, audioCtx.currentTime);
  osc.frequency.exponentialRampToValueAtTime(400, audioCtx.currentTime + 0.1);

  gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);

  osc.start(audioCtx.currentTime);
  osc.stop(audioCtx.currentTime + 0.1);
}

function playFlipSound() {
  // Whoosh: white noise burst + pitch sweep
  const bufferSize = audioCtx.sampleRate * 0.3;
  const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < bufferSize; i++) {
    data[i] = (Math.random() * 2 - 1) * (1 - i / bufferSize); // decaying noise
  }

  const source = audioCtx.createBufferSource();
  source.buffer = buffer;

  const filter = audioCtx.createBiquadFilter();
  filter.type = 'bandpass';
  filter.frequency.setValueAtTime(2000, audioCtx.currentTime);
  filter.frequency.exponentialRampToValueAtTime(200, audioCtx.currentTime + 0.3);
  filter.Q.value = 1;

  const gain = audioCtx.createGain();
  gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);

  source.connect(filter).connect(gain).connect(audioCtx.destination);
  source.start();
}
```

### Sound Cues for Page Flip

| Moment | Sound | Implementation |
|--------|-------|----------------|
| Flip starts | Paper lift / soft whoosh | Decaying white noise + bandpass sweep |
| Mid-flip | Air / swoosh | Filtered noise with volume curve |
| Page lands | Paper snap / thud | Short sine burst + low-pass filter |
| New section reveals | Subtle chime | Two-tone sine (C5 → E5) with reverb |
| Hover on interactive | Soft tick | Very short sine blip (10ms) |
| Click/confirm | Crisp click | Square wave burst (5ms) |

### Ambient Background Sound

```js
// Optional: low ambient hum that changes per section
function setAmbient(frequency, volume) {
  if (!ambientOsc) {
    ambientOsc = audioCtx.createOscillator();
    ambientGain = audioCtx.createGain();
    ambientOsc.connect(ambientGain).connect(audioCtx.destination);
    ambientOsc.type = 'sine';
    ambientOsc.start();
  }
  ambientOsc.frequency.linearRampToValueAtTime(frequency, audioCtx.currentTime + 1);
  ambientGain.gain.linearRampToValueAtTime(volume, audioCtx.currentTime + 1);
}
```

### Important: Audio UX

- **Always require user interaction** before starting AudioContext (browser autoplay policy)
- Provide a mute toggle — some users hate sound
- Keep volumes low (0.1–0.3 gain max)
- Preload all audio buffers on first interaction
- Use `linearRampToValueAtTime` for smooth transitions, never abrupt stops

---

## 6. Loading Sequences & Entrance Animations

### Cinematic Loading Sequence

```js
const loadTimeline = gsap.timeline();

loadTimeline
  .set('.loader', { display: 'flex' })
  .from('.loader-logo', { scale: 0, rotation: -180, duration: 1, ease: 'back.out(1.7)' })
  .from('.loader-text', { y: 30, opacity: 0, duration: 0.5 }, '-=0.3')
  .to('.loader-bar-fill', { width: '100%', duration: 2, ease: 'power1.inOut' })
  .to('.loader', { opacity: 0, duration: 0.5, ease: 'power2.in' })
  .set('.loader', { display: 'none' })
  .from('.hero-title', { y: 100, opacity: 0, duration: 1, ease: 'power3.out' }, '-=0.2')
  .from('.hero-subtitle', { y: 50, opacity: 0, duration: 0.8 }, '-=0.5')
  .from('.hero-cta', { scale: 0, duration: 0.5, ease: 'back.out(2)' }, '-=0.3');
```

### Staggered Section Entrance

```js
ScrollTrigger.batch('.portfolio-card', {
  onEnter: (elements) => {
    gsap.from(elements, {
      y: 60,
      opacity: 0,
      stagger: 0.15,
      duration: 0.8,
      ease: 'power2.out',
    });
  },
  start: 'top 85%',
  once: true,
});
```

### Page Transition (Flip) Entrance

```js
function flipToSection(fromEl, toEl) {
  const tl = gsap.timeline();

  tl
    // Phase 1: Lift off
    .to(fromEl, {
      rotateY: -90,
      transformOrigin: 'left center',
      duration: 0.4,
      ease: 'power2.in',
      onStart: () => playFlipSound(),
    })
    // Phase 2: Burst particles at spine
    .call(() => burstParticles(window.innerWidth / 2, window.innerHeight / 2))
    // Phase 3: New page lands
    .fromTo(toEl,
      { rotateY: 90, transformOrigin: 'right center', display: 'none' },
      { rotateY: 0, display: 'block', duration: 0.4, ease: 'power2.out' },
      '-=0.1'
    )
    // Phase 4: Reveal content
    .from(toEl.querySelectorAll('.reveal'), {
      y: 40, opacity: 0, stagger: 0.1, duration: 0.6, ease: 'power2.out'
    }, '-=0.2');

  return tl;
}
```

---

## 7. Dramatic Page-Flip Transition — Detailed Breakdown

### What Happens to Elements DURING the Flip

| Phase | Timing | Elements | Behavior |
|-------|--------|----------|----------|
| Pre-flip | -0.5s to 0s | Page edge | Subtle curl shadow appears on hover/click near edge |
| Lift | 0–20% | Current page | `rotateY` begins, shadow deepens, slight `scale(0.98)` |
| Curl | 20–50% | Current page | Full 3D perspective, `transform-origin: left`, shadow casts right |
| Cross-over | 40–60% | Both pages | New page begins rotating in from `rotateY(90)` |
| Land | 60–90% | New page | Decelerates, bounce ease, shadow fades |
| Settle | 90–100% | New page | Subtle scale bounce (1.02 → 1.0), content fades in |

### Particle Effects During Transition

```
Timeline:
0%   ─── Particles spawn along the spine (center line)
20%  ─── Particles burst outward (fan pattern, ~200 particles)
50%  ─── Peak spread, gravity takes hold
80%  ─── Most particles fade out (life < 0.2)
100% ─── Canvas cleared
```

**Particle types for flip:**
- **Sparks:** Small, bright, fast — gold/white, short life
- **Confetti:** Larger, slower, rotating — section accent colors
- **Dust:** Tiny, subtle, brownish — adds realism to the paper feel
- **Light streaks:** Thin lines that arc across the flip path

### Text Scramble During Flip

```
iHackAudio → !@#ckA*dio → ih##auD!o → iHackAudio (new section)
```

The title text goes through:
1. Characters replaced with random symbols (scramble)
2. Characters briefly show new section's title mixed with old
3. Final text resolves to new title with bounce easing

### Background Gradient Morphing

```js
const sectionGradients = {
  hero:       ['#0a0a0a', '#1a1a2e', '#16213e'],
  portfolio:  ['#0d1117', '#161b22', '#21262d'],
  about:      ['#1a0a2e', '#2d1b4e', '#16213e'],
  contact:    ['#0a1a0a', '#1b2d1b', '#163e21'],
};

// During flip: interpolate between old and new gradients
gsap.to('.bg-gradient', {
  '--color-1': sectionGradients[newSection][0],
  '--color-2': sectionGradients[newSection][1],
  '--color-3': sectionGradients[newSection][2],
  duration: 0.8,
  ease: 'power2.inOut',
});
```

### Sound Cues for the Flip

```
[0ms]    User clicks/scrolls → trigger flip
[50ms]   Paper lift whoosh (bandpass noise sweep 2kHz → 200Hz, 300ms)
[200ms]  Air swoosh (volume peak at mid-flip)
[400ms]  Page lands — paper thud (low sine burst 80Hz, 50ms)
[450ms]  Subtle reverb tail (convolver, 500ms decay)
[500ms]  New section chime (two-tone: C5→E5, 200ms, sine)
[600ms]  Content reveal sounds (optional: soft ticks per element)
```

---

## 8. Performance Considerations

- **`will-change`** — Apply to animated elements (`transform`, `opacity`) but remove after animation
- **Canvas for particles** — Don't use DOM elements for 200+ particles; canvas is 10× faster
- **`requestAnimationFrame`** — Always use for JS animations, never `setInterval`
- **Debounce scroll handlers** — Use GSAP ScrollTrigger's built-in debouncing
- **Audio lazy-init** — Create AudioContext on first user interaction only
- **GPU compositing** — Stick to `transform` and `opacity` for 60fps animations
- **Reduce motion** — Respect `prefers-reduced-motion: reduce`:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 9. Recommended Libraries

| Library | Use Case | Size |
|---------|----------|------|
| **GSAP 3** | All animations, ScrollTrigger, SplitText | ~30KB core |
| **Three.js** | WebGL particle systems, 3D page flip | ~150KB |
| **Howler.js** | Audio playback with fallbacks | ~10KB |
| **Lenis** | Smooth scroll (butter-smooth, pairs with ScrollTrigger) | ~5KB |
| **Motion One** | CSS-native animation API (lightweight alternative) | ~6KB |
| **Anime.js** | Simple timeline animations | ~17KB |

---

## 10. Implementation Priority for iHackAudio

1. **Phase 1 (Core):** Page-flip CSS 3D transform + GSAP ScrollTrigger snap
2. **Phase 2 (Polish):** SplitText title animation + scramble effect during flip
3. **Phase 3 (Particles):** Canvas particle burst at flip spine
4. **Phase 4 (Sound):** Web Audio API flip sounds + hover ticks
5. **Phase 5 (Cursor):** Custom cursor + magnetic buttons
6. **Phase 6 (Ambient):** Gradient morphing + noise overlay + ambient sound

---

*Research compiled 2026-08-03. Sources: MDN Web Docs, GSAP documentation, Web Audio API spec, CSS Scroll-driven Animations spec.*
