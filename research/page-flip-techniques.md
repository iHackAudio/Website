# Page Flip & Page Turn Animation Techniques — Research

**Context:** Portfolio site with two sides — "The Human" (warm gold, storytelling) and "The Architect" (cold blue, technical). A pivot card in the middle triggers a dramatic page-turn animation that flips the ENTIRE viewport from one theme to the other.

---

## 1. CSS 3D Transforms for Page Flip

### Core Properties

```css
/* The 3D scene container */
.flip-scene {
  perspective: 1200px;           /* Creates the 3D space — higher = less distortion */
  perspective-origin: center center;
}

/* The page that flips */
.flip-page {
  transform-style: preserve-3d;  /* CRITICAL: keeps children in 3D space */
  backface-visibility: hidden;   /* Hide the back face when rotated past 90° */
  transform-origin: left center; /* Hinge point — left edge for book-style flip */
  transition: transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
}

.flip-page.flipped {
  transform: rotateY(-180deg);
}

/* The back face (hidden by default, revealed on flip) */
.flip-page-back {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  transform: rotateY(180deg);   /* Pre-rotated so it shows when parent flips */
}
```

### Key Gotchas (from CSS-Tricks / Ana Tudor)

1. **`overflow: hidden` breaks `preserve-3d`** — Any element with `overflow` other than `visible` forces `transform-style: flat`. Use a wrapper for clipping and keep 3D children outside it.

2. **3D Rendering Context** — Elements must share the same 3D rendering context to intersect/z-order properly. Nest them inside a `preserve-3d` container.

3. **`perspective` goes on the PARENT, not the element** — `perspective: 1000px` on `.container` applies to `.container`'s children, not `.container` itself.

4. **`backface-visibility` and Safari** — Safari has known quirks; test thoroughly. Use `-webkit-backface-visibility: hidden` as well.

### Full-Viewport Page Flip (CSS Only)

```css
/* Two full-screen pages stacked */
.page {
  position: fixed;
  inset: 0;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  transition: transform 1.2s cubic-bezier(0.645, 0.045, 0.355, 1);
  transform-origin: 50% 50%; /* Center hinge — flips like a card */
}

/* OR for book-style: hinge on left/right edge */
.page {
  transform-origin: left center;  /* "The Human" page — hinges from left */
}

.page--back {
  transform: rotateY(180deg);
  transform-origin: left center;
}

/* Triggered state */
.page--flipped {
  transform: rotateY(-180deg);
}

/* Container needs perspective */
.viewport {
  perspective: 2000px; /* Higher for full-viewport — less "fisheye" distortion */
  overflow: hidden;
  height: 100vh;
  width: 100vw;
}
```

### CSS View Transitions API (Modern Approach)

The View Transitions API can handle cross-document page flips, but **3D transforms don't work on view transition pseudo-elements** due to flattening issues (as of mid-2026). The snapshot pseudo-elements (`::view-transition-old`, `::view-transition-new`) lose their 3D context.

**Workaround:** Use JavaScript-based FLIP (GSAP) instead of pure CSS View Transitions for 3D effects.

---

## 2. GSAP-Based Page Flip Animations

### GSAP Flip Plugin (Recommended for this use case)

The FLIP technique (First, Last, Invert, Play) by Paul Lewis, implemented in GSAP:

```js
import { gsap } from "gsap";
import { Flip } from "gsap/Flip";

gsap.registerPlugin(Flip);

// Capture current state
const state = Flip.getState(".page-content");

// Swap classes (change theme, layout, content)
document.body.classList.toggle("architect-mode");

// Animate the transition
Flip.from(state, {
  duration: 1.2,
  ease: "power2.inOut",
  absolute: true,        // Use position:absolute during flip
  onComplete: () => { /* theme swap complete */ }
});
```

**Key features for our use case:**
- `absolute: true` — elements use `position: absolute` during flip (solves flex/grid layout jumps)
- `nested: true` — compensates for nested transforms (parent + child both flipping)
- `onEnter` / `onLeave` — animate elements entering/leaving the DOM
- `fade: true` — cross-fade between two different elements (perfect for theme swap)
- Full GSAP easing, timeline integration, ScrollTrigger compatibility

### GSAP Timeline — Full Page Flip Sequence

```js
const tl = gsap.timeline({ paused: true });

// Phase 1: Pivot card "lifts" and starts rotation
tl.to(".pivot-card", {
  scale: 1.05,
  boxShadow: "0 25px 60px rgba(0,0,0,0.4)",
  duration: 0.3,
  ease: "power2.out"
});

// Phase 2: Full page flips (viewport rotation)
tl.to(".viewport", {
  rotateY: -180,
  duration: 1.2,
  ease: "power3.inOut",
  transformOrigin: "center center",
  transformPerspective: 2000,
}, 0.1);

// Phase 3: Theme transition (colors morph during flip)
tl.to(":root", {
  "--bg-primary": "#0a1628",      // Cold blue
  "--text-primary": "#e8f0ff",
  "--accent": "#4a9eff",
  duration: 0.6,
  ease: "power1.inOut",
}, 0.4); // Starts mid-flip

// Phase 4: Content fades in on other side
tl.fromTo(".architect-content", 
  { opacity: 0, y: 30 },
  { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" },
  0.9 // Starts near end of flip
);

document.querySelector(".pivot-card").addEventListener("click", () => {
  tl.play(); // or tl.reverse() to flip back
});
```

### GSAP + ScrollTrigger (Scroll-Driven Flip)

```js
gsap.registerPlugin(ScrollTrigger);

// Scroll-driven page flip — the page turns as user scrolls
gsap.to(".page-human", {
  rotateY: -180,
  transformOrigin: "center center",
  transformPerspective: 2000,
  scrollTrigger: {
    trigger: ".pivot-section",
    start: "top center",
    end: "bottom center",
    scrub: 1,           // Smooth 1-second catch-up
    pin: true,          // Pin the section during flip
    snap: [0, 1],       // Snap to start/end positions
  }
});
```

---

## 3. Full-Page Transition Effects (ENTIRE Viewport)

### Approach A: Two Full-Screen Layers (Recommended)

The most reliable approach for dramatic full-viewport flips:

```html
<div class="flip-viewport">
  <!-- Front: "The Human" (warm gold) -->
  <div class="page page--front">
    <div class="page-content human-theme">
      <!-- Full content here -->
    </div>
  </div>
  
  <!-- Back: "The Architect" (cold blue) -->
  <div class="page page--back">
    <div class="page-content architect-theme">
      <!-- Full content here -->
    </div>
  </div>
</div>
```

```css
.flip-viewport {
  perspective: 2000px;
  perspective-origin: 50% 50%;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
}

.page {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  will-change: transform;
}

.page--front {
  z-index: 2;
}

.page--back {
  transform: rotateY(180deg);
}

/* Shadow/gradient overlay during flip for depth */
.page::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to left, rgba(0,0,0,0.3), transparent);
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}
```

### Approach B: CSS `clip-path` Morph (No 3D)

A 2D alternative that avoids 3D rendering issues:

```css
.page-transition {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  transition: clip-path 0.8s cubic-bezier(0.77, 0, 0.175, 1);
}

.page-transition.flipped {
  clip-path: polygon(50% 0, 50% 0, 50% 100%, 50% 100%);
}
```

### Approach C: Split-Page Reveal

The page splits in half (like opening a book), revealing the other side:

```js
const tl = gsap.timeline();

tl.to(".split-left", {
  xPercent: -100,
  rotateY: -90,
  transformOrigin: "right center",
  duration: 0.8,
  ease: "power3.inOut"
});

tl.to(".split-right", {
  xPercent: 100,
  rotateY: 90,
  transformOrigin: "left center",
  duration: 0.8,
  ease: "power3.inOut"
}, "<"); // Simultaneous with left
```

---

## 4. Libraries Comparison

### StPageFlip (page-flip v2.0.7)
- **npm:** `page-flip`
- **CDN:** `https://cdn.jsdelivr.net/npm/page-flip`
- **GitHub:** https://github.com/Nodlik/StPageFlip
- **What it does:** Realistic page-turning effect for books/magazines
- **Rendering:** Canvas-based (not DOM)
- **Pros:** Beautiful realistic page curl, touch support, responsive
- **Cons:** Canvas-based (not great for interactive content on pages), designed for multi-page books, not ideal for two-page theme swaps
- **Verdict:** ❌ **Not recommended** for this use case — it's for flipbooks, not full-viewport theme transitions

### Turn.js
- **Website:** http://www.turnjs.com/
- **What it does:** HTML5 page flip effect for books/magazines
- **Rendering:** CSS 3D transforms
- **Pros:** DOM-based, supports HTML content, well-established
- **Cons:** jQuery dependency, older library (less maintained), designed for multi-page books
- **Verdict:** ❌ **Not recommended** — outdated, jQuery-dependent, wrong paradigm

### GSAP Flip Plugin
- **Docs:** https://gsap.com/docs/v3/Plugins/Flip/
- **What it does:** FLIP animation technique for layout transitions
- **Pros:** Handles nested transforms, stagger, `absolute` mode, `fade` cross-fading, ScrollTrigger integration, free as of v3.9
- **Cons:** Not a "page curl" effect — it's a layout transition tool
- **Verdict:** ✅ **Best choice** for our use case — handles the theme swap + layout transition perfectly

### Custom Implementation (Recommended)

For the specific "dramatic full-viewport page flip between two themed sides" requirement, a **custom GSAP-powered implementation** is the best path:

**Why custom?**
1. StPageFlip and Turn.js are designed for multi-page books, not two-side theme flips
2. We need the ENTIRE viewport to flip, not just a contained element
3. We need theme color transitions synchronized with the 3D rotation
4. We need the pivot card to be the "trigger" that starts the flip
5. We want full control over easing, timing, and the dramatic effect

---

## 5. Implementation: Warm Gold ↔ Cold Blue Flip

### The Concept

```
[  "The Human" side  ]  ←→  [  "The Architect" side  ]
   Warm gold theme              Cold blue theme
   Storytelling                 Technical
   rotateY(0)                  rotateY(180deg)
   
         ↑ PIVOT CARD triggers the flip ↑
```

### Recommended Architecture

```
┌─────────────────────────────────────────────┐
│  .flip-container (perspective: 2000px)       │
│  ┌───────────────────────────────────────┐  │
│  │  .page.page--human (z-index: 2)       │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  Warm gold background           │  │  │
│  │  │  Story content                  │  │  │
│  │  │  ┌───────────────────────┐      │  │  │
│  │  │  │   🎯 PIVOT CARD       │      │  │  │
│  │  │  │   "Flip to see the    │      │  │  │
│  │  │  │    other side"        │      │  │  │
│  │  │  └───────────────────────┘      │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │  .page.page--architect (rotateY 180)  │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  Cold blue background           │  │  │
│  │  │  Technical content              │  │  │
│  │  │  ┌───────────────────────┐      │  │  │
│  │  │  │   🎯 PIVOT CARD       │      │  │  │
│  │  │  │   "Flip back"         │      │  │  │
│  │  │  └───────────────────────┘      │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Core Implementation (GSAP + Custom)

```js
class PageFlipTransition {
  constructor() {
    this.isFlipped = false;
    this.container = document.querySelector('.flip-container');
    this.frontPage = document.querySelector('.page--human');
    this.backPage = document.querySelector('.page--architect');
    this.pivotCards = document.querySelectorAll('.pivot-card');
    
    this.init();
  }
  
  init() {
    this.pivotCards.forEach(card => {
      card.addEventListener('click', () => this.flip());
    });
    
    // Keyboard shortcut
    document.addEventListener('keydown', (e) => {
      if (e.key === 'f' || e.key === 'F') this.flip();
    });
  }
  
  flip() {
    if (this.isAnimating) return;
    this.isAnimating = true;
    
    const tl = gsap.timeline({
      onComplete: () => {
        this.isFlipped = !this.isFlipped;
        this.isAnimating = false;
      }
    });
    
    // Phase 1: Pivot card "lifts" with glow
    tl.to('.pivot-card--active', {
      scale: 1.08,
      boxShadow: '0 30px 80px rgba(0,0,0,0.5)',
      duration: 0.25,
      ease: 'power2.out'
    });
    
    // Phase 2: Entire viewport flips
    const targetRotation = this.isFlipped ? 0 : -180;
    tl.to(this.frontPage, {
      rotateY: targetRotation,
      duration: 1.0,
      ease: 'power3.inOut',
      transformPerspective: 2000,
      transformOrigin: '50% 50%',
    }, 0.1);
    
    // Phase 3: Theme color transition (mid-flip)
    // CSS custom properties animate during the flip
    if (!this.isFlipped) {
      // Flipping to Architect (cold blue)
      tl.to(document.documentElement, {
        '--bg-primary': '#0a1628',
        '--bg-secondary': '#111d35',
        '--text-primary': '#e8f0ff',
        '--accent': '#4a9eff',
        '--glow': 'rgba(74, 158, 255, 0.3)',
        duration: 0.5,
        ease: 'power1.inOut',
      }, 0.3);
    } else {
      // Flipping back to Human (warm gold)
      tl.to(document.documentElement, {
        '--bg-primary': '#1a1409',
        '--bg-secondary': '#2a2015',
        '--text-primary': '#fff5e0',
        '--accent': '#d4a843',
        '--glow': 'rgba(212, 168, 67, 0.3)',
        duration: 0.5,
        ease: 'power1.inOut',
      }, 0.3);
    }
    
    // Phase 4: Shadow overlay during flip (depth illusion)
    tl.to('.flip-shadow-overlay', {
      opacity: 0.4,
      duration: 0.3,
      ease: 'power1.in'
    }, 0.1);
    tl.to('.flip-shadow-overlay', {
      opacity: 0,
      duration: 0.4,
      ease: 'power1.out'
    }, 0.6);
    
    // Phase 5: Pivot card settles
    tl.to('.pivot-card--active', {
      scale: 1,
      boxShadow: '0 10px 30px rgba(0,0,0,0.2)',
      duration: 0.3,
      ease: 'power2.inOut'
    }, 0.7);
  }
}

new PageFlipTransition();
```

### CSS for the Dual-Theme Flip

```css
:root {
  /* Default: Warm Gold (The Human) */
  --bg-primary: #1a1409;
  --bg-secondary: #2a2015;
  --text-primary: #fff5e0;
  --text-secondary: #c4a87a;
  --accent: #d4a843;
  --accent-glow: rgba(212, 168, 67, 0.3);
  --border: rgba(212, 168, 67, 0.2);
}

.flip-container {
  width: 100vw;
  height: 100vh;
  perspective: 2000px;
  overflow: hidden;
  position: relative;
}

.page {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  will-change: transform;
  overflow-y: auto;
}

.page--human {
  z-index: 2;
  background: linear-gradient(135deg, var(--bg-primary), var(--bg-secondary));
  color: var(--text-primary);
}

.page--architect {
  transform: rotateY(180deg);
  background: linear-gradient(135deg, #0a1628, #111d35);
  color: #e8f0ff;
}

/* Shadow overlay for depth during flip */
.flip-shadow-overlay {
  position: fixed;
  inset: 0;
  background: radial-gradient(ellipse at center, 
    rgba(0,0,0,0.6) 0%, 
    rgba(0,0,0,0) 70%);
  opacity: 0;
  pointer-events: none;
  z-index: 100;
}

/* Pivot card */
.pivot-card {
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  z-index: 10;
}

.pivot-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}

/* Subtle edge shadow during flip for book-like depth */
.page::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 40px;
  pointer-events: none;
  z-index: 50;
}

.page--human::before {
  right: 0;
  background: linear-gradient(to left, rgba(0,0,0,0.15), transparent);
}

.page--architect::before {
  left: 0;
  background: linear-gradient(to right, rgba(0,0,0,0.15), transparent);
}
```

### Scroll-Triggered Variant (Alternative to Click)

```js
// Pin the pivot section and flip as user scrolls past it
ScrollTrigger.create({
  trigger: '.pivot-section',
  start: 'top top',
  end: '+=100%',   // Pin for 100% of viewport height
  pin: true,
  scrub: 1,
  snap: {
    snapTo: [0, 1],
    duration: { min: 0.4, max: 0.8 },
    ease: 'power2.inOut'
  },
  onUpdate: (self) => {
    const progress = self.progress;
    // Rotate the page based on scroll progress
    gsap.set('.page--human', {
      rotateY: progress * -180,
      transformPerspective: 2000,
      transformOrigin: '50% 50%'
    });
    // Cross-fade theme colors
    gsap.set(document.documentElement, {
      '--accent': gsap.utils.interpolate('#d4a843', '#4a9eff', progress)
    });
  }
});
```

---

## 6. Performance Considerations

1. **`will-change: transform`** — Apply to `.page` elements to promote them to GPU layers
2. **`transformPerspective`** (GSAP) — Preferred over CSS `perspective` for GSAP-controlled animations (avoids creating new stacking contexts)
3. **Avoid animating `box-shadow` directly** — Use a pseudo-element with `opacity` animation instead
4. **`backface-visibility: hidden`** — Reduces paint area by ~50% during flip
5. **Content visibility** — Use `content-visibility: auto` on the hidden (back) page to skip rendering its contents until needed
6. **Throttle scroll-driven flips** — Use `scrub: 1` (1-second catch-up) instead of `scrub: true` (instant) for smoother scroll-linked flips

---

## 7. Recommendation Summary

| Approach | Suitability | Complexity | Visual Impact |
|----------|------------|------------|---------------|
| StPageFlip | ❌ Wrong paradigm | Low | Book curl (not what we want) |
| Turn.js | ❌ Outdated | Low | Book flip (not what we want) |
| CSS-only 3D | ⚠️ Limited | Medium | Good but hard to sync with theme |
| GSAP Flip Plugin | ✅ Great for layout | Medium | Smooth but not "page flip" |
| **GSAP Timeline (Custom)** | **✅ Best fit** | **Medium-High** | **Dramatic, controllable** |
| View Transitions API | ❌ 3D broken | Low | N/A for 3D |

### Final Recommendation: **Custom GSAP Timeline**

Use a **custom GSAP timeline** that:
1. Rotates the entire viewport container with `rotateY(-180)` and `transformPerspective: 2000`
2. Animates CSS custom properties for theme colors mid-flip (0.3s–0.8s mark)
3. Adds a radial shadow overlay during the flip for depth
4. Uses `backface-visibility: hidden` on both page faces
5. Triggered by the pivot card click (or optionally scroll-driven with ScrollTrigger)

This gives full control over the "dramatic page-turn" feel while cleanly swapping between the warm gold and cold blue themes.

---

## Sources

- CSS-Tricks: "Why Isn't My 3D View Transition Working?" (Jun 2026) — https://css-tricks.com/why-isnt-my-3d-view-transition-working/
- CSS-Tricks: "Things to Watch Out for When Working with CSS 3D" (Sep 2016) — https://css-tricks.com/things-watch-working-css-3d/
- GSAP Flip Plugin Docs — https://gsap.com/docs/v3/Plugins/Flip/
- GSAP Community Forums — https://gsap.com/community/
- StPageFlip (page-flip) — https://github.com/Nodlik/StPageFlip
- Turn.js — http://www.turnjs.com/
- Ryan Mulligan: "Animating with the Flip Plugin for GSAP" — https://ryanmulligan.dev/blog/gsap-flip-cart/
