# GSAP Advanced Animation Patterns — Page-Level Transitions

> Research compiled from GSAP official docs (v3.15), GSAP community forums, and Codrops tutorials.

---

## Table of Contents

1. [GSAP Flip Plugin — Layout Transitions](#1-gsap-flip-plugin--layout-transitions)
2. [Timeline Orchestration for Complex Transitions](#2-timeline-orchestration-for-complex-transitions)
3. [ScrollTrigger-Based Page Transitions](#3-scrolltrigger-based-page-transitions)
4. [GSAP + CSS 3D Transform Combinations](#4-gsap--css-3d-transform-combinations)
5. [Performance Best Practices](#5-performance-best-practices)
6. [gsap.matchMedia() for Responsive Animations](#6-gsapmatchmedia-for-responsive-animations)
7. [Combined Pattern: Full Page Theme Flip](#7-combined-pattern-full-page-theme-flip)

---

## 1. GSAP Flip Plugin — Layout Transitions

The Flip plugin (free since v3.9.0) implements the FLIP technique (First, Last, Invert, Play) to seamlessly animate between two completely different layout states, even when DOM structure changes dramatically.

### Core Workflow (3 Steps)

```js
// Step 1: Capture current state
const state = Flip.getState(".targets");

// Step 2: Make DOM/styling changes (reorder, toggle class, move elements)
element.classList.toggle("theme-dark");

// Step 3: Animate from old state to new
Flip.from(state, {
  duration: 1,
  ease: "power1.inOut",
  absolute: true,
});
```

### Key Flip.from() Options

| Option | Description |
|--------|-------------|
| `absolute` | `true` or selector — applies `position: absolute` during flip. Solves flex/grid layout challenges. |
| `absoluteOnLeave` | Sets leaving elements to `position: absolute` so they can animate out without affecting flow. |
| `fade` | Cross-fade when swapping elements with same `data-flip-id`. |
| `nested` | Prevents offset compounding when parent + child are both targets. |
| `simple` | Skips rotation/scale/skew calculations for faster performance with many elements. |
| `onEnter` | Callback for elements entering the layout — animate them in (e.g., fade). |
| `onLeave` | Callback for elements leaving the layout — animate them out. |
| `props` | Comma-delimited list of extra CSS properties to include (e.g., `"backgroundColor,color"`). |
| `toggleClass` | Applies a CSS class during the flip, removed at end. |

### Element Swapping with data-flip-id

```html
<!-- State A -->
<div data-flip-id="card1" class="card-a">Item 1</div>

<!-- State B (different element, same flip-id) -->
<div data-flip-id="card1" class="card-b">Item 1</div>
```

```js
const state = Flip.getState("[data-flip-id]");
swapDOM(); // Replace State A elements with State B elements
Flip.from(state, {
  duration: 0.8,
  fade: true,       // Cross-fade between old and new elements
  absolute: true,
  ease: "power2.inOut"
});
```

### Flip.fit() — Snap One Element to Another

```js
// Resize/reposition elementA to perfectly overlay elementB
Flip.fit(".elementA", ".elementB", {
  duration: 0.5,
  ease: "power2.out",
  scale: true
});
```

### Flip.to() — Animate TO Current State

```js
// Capture current state, make changes, then animate FROM current TO new
const state = Flip.getState(".items");
reorderItems(); // DOM manipulation
Flip.to(state, {
  duration: 0.6,
  ease: "power1.inOut",
  absolute: true,
  onComplete: () => console.log("Flip complete")
});
```

### Theme/Layout Switching Pattern

```js
function switchTheme(newTheme) {
  // Capture all elements that will change
  const state = Flip.getState(".card, .nav, .hero, .sidebar");

  // Apply new theme (changes layout, colors, sizes)
  document.body.className = `theme-${newTheme}`;

  // Animate the transition
  Flip.from(state, {
    duration: 1.2,
    ease: "power2.inOut",
    absolute: true,
    props: "backgroundColor,color,borderColor",
    stagger: 0.05,
    onEnter: elements => gsap.fromTo(elements,
      { opacity: 0, scale: 0.8 },
      { opacity: 1, scale: 1, duration: 0.6 }
    ),
    onLeave: elements => gsap.to(elements, {
      opacity: 0, scale: 0.8, duration: 0.4
    })
  });
}
```

---

## 2. Timeline Orchestration for Complex Transitions

### Multi-Phase Page Transition: Fade Out → Flip → Reveal

```js
function pageTransition(fromPage, toPage) {
  const master = gsap.timeline();

  // Phase 1: Fade out current page
  master.to(fromPage, {
    opacity: 0,
    y: -30,
    duration: 0.4,
    ease: "power2.in",
    onComplete: () => {
      fromPage.style.display = "none";
    }
  });

  // Phase 2: Flip transition
  master.add(() => {
    const state = Flip.getState(".shared-element");
    toPage.style.display = "block";
    Flip.from(state, {
      duration: 0.8,
      ease: "power2.inOut",
      absolute: true
    });
  });

  // Phase 3: Reveal new page elements
  master.from(toPage, {
    opacity: 0,
    duration: 0.3,
    ease: "power2.out"
  }, "-=0.4"); // Overlap with flip

  // Phase 4: Stagger in new page content
  master.from(".toPage .animate-in", {
    y: 40,
    opacity: 0,
    stagger: 0.08,
    duration: 0.5,
    ease: "power3.out"
  }, "-=0.2");

  return master;
}
```

### Timeline with Labels for Scrub Control

```js
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".page-transition-section",
    pin: true,
    scrub: 1,
    snap: {
      snapTo: "labels",
      duration: { min: 0.2, max: 3 },
      delay: 0.2,
      ease: "power1.inOut"
    }
  }
});

tl.addLabel("start")
  .from(".side-a", { opacity: 1 })
  .to(".side-a", { opacity: 0, rotateY: -90, duration: 0.5 })
  .addLabel("midpoint")
  .from(".side-b", { opacity: 0, rotateY: 90 })
  .to(".side-b", { opacity: 1, rotateY: 0, duration: 0.5 })
  .addLabel("end");
```

### Position Parameter for Precise Sequencing

```js
const tl = gsap.timeline();

// Absolute position
tl.to(".element1", { x: 100 }, 0);        // starts at 0s
tl.to(".element2", { x: 200 }, 0.5);      // starts at 0.5s

// Relative position
tl.to(".element3", { x: 300 }, "+=0.3");  // 0.3s after previous
tl.to(".element4", { x: 400 }, "-=0.2");  // overlaps 0.2s with previous

// Label-based
tl.addLabel("reveal");
tl.to(".element5", { opacity: 1 }, "reveal+=0.1");
```

---

## 3. ScrollTrigger-Based Page Transitions

### Pin + Flip Combination

```js
ScrollTrigger.create({
  trigger: ".transition-container",
  start: "top top",
  end: "+=200%",
  pin: true,
  scrub: true,
  onUpdate: (self) => {
    const progress = self.progress;

    if (progress > 0.5 && !isFlipped) {
      // Trigger flip at midpoint of scroll
      const state = Flip.getState(".layout-element");
      document.body.classList.add("alt-layout");
      Flip.from(state, {
        duration: 0.8,
        ease: "power2.inOut",
        absolute: true
      });
      isFlipped = true;
    } else if (progress <= 0.5 && isFlipped) {
      // Reverse flip when scrolling back
      const state = Flip.getState(".layout-element");
      document.body.classList.remove("alt-layout");
      Flip.from(state, {
        duration: 0.8,
        ease: "power2.inOut",
        absolute: true
      });
      isFlipped = false;
    }
  }
});
```

### Scroll-Driven 3D Rotation with Pinning

From the Codrops 3D text animation tutorial:

```js
ScrollTrigger.create({
  trigger: ".section-title",
  start: "center center",
  end: "+=2000svh",
  pin: ".wrapper",
  scrub: 2,
  animation: gsap.fromTo(
    ".content-wrapper",
    { rotateX: -80 },
    { rotateX: 270, ease: "none" }
  ),
});
```

Key properties:
- `pin: true` — fixes element during scroll
- `scrub: 2` — smooth 2-second lag between scroll and animation
- `snap` — snaps to labels for discrete transitions

### ScrollTrigger with Multiple Sections

```js
// Loop through sections — each gets its own ScrollTrigger
gsap.utils.toArray(".page-section").forEach((section) => {
  const content = section.querySelector(".content");

  gsap.from(content, {
    scrollTrigger: {
      trigger: section,
      start: "top 80%",
      end: "top 20%",
      scrub: true,
    },
    y: 60,
    opacity: 0,
  });
});
```

### Common ScrollTrigger Mistakes to Avoid

1. **Don't nest ScrollTriggers inside timelines** — A timeline controls its children; you can't also have ScrollTrigger control them independently.
2. **Don't use `to()` for the same property across multiple ScrollTriggers** — Use `fromTo()` or `immediateRender: false`.
3. **Create ScrollTriggers in DOM order** — Pinned elements add spacing; out-of-order creation causes offset miscalculations.
4. **Use `clamp()` for start values** — Prevents jumps on load: `start: "clamp(top bottom)"`.
5. **Call `ScrollTrigger.refresh()` after dynamic content loads**.

---

## 4. GSAP + CSS 3D Transform Combinations

### 3D Card/Page Flip with rotateY

```css
.card-container {
  perspective: 1000px;
}

.card {
  transform-style: preserve-3d;
  position: relative;
}

.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.card-back {
  transform: rotateY(180deg);
}
```

```js
// Flip card from front to back
gsap.to(".card", {
  rotateY: 180,
  duration: 0.8,
  ease: "power2.inOut",
  transformPerspective: 1000 // Inline perspective
});

// Page-level 3D flip between two "pages"
const tl = gsap.timeline();

tl.to(".page-a", {
  rotateY: -90,
  opacity: 0,
  duration: 0.6,
  ease: "power2.in",
  transformPerspective: 1200,
  transformOrigin: "left center"
})
.set(".page-a", { display: "none" })
.set(".page-b", {
  display: "block",
  rotateY: 90,
  opacity: 0,
  transformPerspective: 1200,
  transformOrigin: "right center"
})
.to(".page-b", {
  rotateY: 0,
  opacity: 1,
  duration: 0.6,
  ease: "power2.out"
});
```

### CSS 3D Properties for GSAP

| CSS Property | GSAP Usage | Purpose |
|---|---|---|
| `perspective` | `transformPerspective: 1000` | Sets depth for 3D space (child elements) |
| `transform-style: preserve-3d` | Set in CSS | Allows children to exist in 3D space |
| `backface-visibility: hidden` | Set in CSS | Hides reverse side of rotated elements |
| `rotateY()` | `rotateY: 180` | Horizontal flip (card flip) |
| `rotateX()` | `rotateX: 45` | Vertical tilt (tilt effects) |
| `translateZ()` | `z: 100` | Push forward/back in 3D space |

### force3D for GPU Acceleration

```js
// GSAP's force3D option promotes elements to their own composite layer
gsap.to(".element", {
  x: 500,
  force3D: true,  // Adds translateZ(0) to force GPU compositing
  duration: 1
});

// Default: "auto" — GSAP adds translateZ(0) during animation, removes after
gsap.to(".element", {
  x: 500,
  force3D: "auto"  // default behavior
});
```

### 3D Cylinder Text Effect (from Codrops)

```js
// Position items around a cylinder using trigonometry
function calculatePositions(items, wrapper) {
  const offset = 0.4;
  const radius = Math.min(window.innerWidth, window.innerHeight) * offset;
  const spacing = 180 / items.length;

  items.forEach((item, index) => {
    const angle = (index * spacing * Math.PI) / 180;
    const rotationAngle = index * -spacing;
    const y = Math.sin(angle) * radius;
    const z = Math.cos(angle) * radius;

    item.style.transform =
      `translate3d(-50%, -50%, 0) translate3d(0px, ${y}px, ${z}px) rotateX(${rotationAngle}deg)`;
  });
}

// Animate with ScrollTrigger
ScrollTrigger.create({
  trigger: ".title",
  start: "center center",
  end: "+=2000svh",
  pin: ".wrapper",
  scrub: 2,
  animation: gsap.fromTo(".text-wrapper",
    { rotateX: -80 },
    { rotateX: 270, ease: "none" }
  ),
});
```

CSS requirements:
```css
.wrapper {
  perspective: 70vw;
}
.text-wrapper {
  transform-style: preserve-3d;
}
.item {
  backface-visibility: hidden;
}
```

---

## 5. Performance Best Practices

### From GreenSock (Official Recommendations)

1. **Avoid CSS filters** — They're terrible for performance, especially Safari. Avoid `blur()`, `drop-shadow()`, etc. on animated elements.

2. **Animate transforms, not layout properties** — Use `x`, `y`, `scaleX`, `scaleY`, `rotation` instead of `width`, `height`, `top`, `left`. Transforms don't trigger layout recalculation.

3. **Use GSAP's shorthand properties** — `x: 50` is much better than `transform: "translateX(50px)"`. GSAP's shorthand is optimized internally.

4. **Set `will-change: transform`** on heavy elements — Promotes them to their own compositor layer. Use sparingly (only on elements that are tough on the renderer).

5. **Minimize pixel change area** — The more pixels that change per frame, the harder the browser works.

6. **Avoid SVG animation for large SVGs** — SVGs fabricate pixels via math (expensive). For large/complex SVGs, consider converting to raster or using `display: none` when off-screen.

7. **Set `pointer-events: none`** where possible — Reduces pointer event handling overhead (but keep it on interactive elements).

8. **Kill off-screen animations** — Don't run animations when elements are outside the viewport.

9. **Never mix CSS transitions with GSAP** — Don't apply CSS `transition` to elements also animated by GSAP. They fight each other.

10. **Consider WebGL (PixiJS)** for extremely heavy rendering — If you're pushing the browser renderer too hard, PixiJS/WebGL can be dramatically faster.

### Flip-Specific Performance

```js
// Use simple: true when no rotation/scale/skew on containers
Flip.from(state, {
  simple: true,  // Skips extra calculations for rotated/scaled containers
  duration: 0.8
});

// Batch flips to avoid conflicts
Flip.batch(".grid-item").on("flip", (batch) => {
  // Handle batched flips
});
```

### ScrollTrigger Performance

```js
ScrollTrigger.create({
  trigger: ".section",
  start: "top top",
  end: "+=500",
  scrub: true,
  // Use once: true if animation only plays once
  once: true,
  // Use fastScrollEnd for performance on fast scrolling
  fastScrollEnd: 300,
});
```

### Memory Management

```js
// Use gsap.context() for automatic cleanup (React/SPA)
let ctx = gsap.context(() => {
  gsap.to(".box", { x: 100 });
  ScrollTrigger.create({ ... });
}, scope);

// Cleanup on unmount
return () => ctx.revert();

// Manual cleanup
ctx.revert(); // Kills all animations and ScrollTriggers created in context
```

---

## 6. gsap.matchMedia() for Responsive Animations

`gsap.matchMedia()` (v3.11+) lets you scope GSAP animations to media queries. When a query stops matching, all animations/ScrollTriggers created in that scope are automatically reverted.

### Basic Syntax

```js
let mm = gsap.matchMedia();

mm.add("(min-width: 800px)", () => {
  // Desktop-only animations
  gsap.to(".hero", { y: -100, scrollTrigger: { ... } });

  return () => {
    // Optional cleanup when query stops matching
  };
});

mm.add("(max-width: 799px)", () => {
  // Mobile-only animations
  gsap.to(".hero", { y: -50, scrollTrigger: { ... } });
});
```

### Conditions Syntax (DRY Code)

```js
let mm = gsap.matchMedia();

mm.add({
  isDesktop: "(min-width: 800px)",
  isMobile: "(max-width: 799px)",
  prefersReducedMotion: "(prefers-reduced-motion: reduce)"
}, (context) => {
  let { isDesktop, isMobile, prefersReducedMotion } = context.conditions;

  if (prefersReducedMotion) {
    gsap.set(".animate", { opacity: 1 }); // No animation
    return;
  }

  const distance = isDesktop ? 200 : 50;

  gsap.to(".box", {
    x: distance,
    scrollTrigger: { trigger: ".section", scrub: true }
  });
});
```

### Reduced Motion Accessibility

```js
let mm = gsap.matchMedia();

mm.add("(prefers-reduced-motion: reduce)", () => {
  // Disable all animations for users who prefer reduced motion
  gsap.globalTimeline.timeScale(0);
  // Or set instant transitions
  gsap.defaults({ duration: 0 });
});
```

### Reverting All at Once

```js
let mm = gsap.matchMedia();

mm.add("(min-width: 800px)", () => { /* ... */ });
mm.add("(max-width: 799px)", () => { /* ... */ });

// Later: revert ALL matchMedia animations
mm.revert();
```

---

## 7. Combined Pattern: Full Page Theme Flip

Here's a complete pattern combining Flip, Timeline, ScrollTrigger, 3D transforms, and matchMedia for a page-level theme transition:

```js
gsap.registerPlugin(Flip, ScrollTrigger);

let mm = gsap.matchMedia();

// Desktop: scroll-driven flip
mm.add("(min-width: 800px)", () => {
  const container = document.querySelector(".theme-transition");
  const sideA = document.querySelector(".theme-light");
  const sideB = document.querySelector(".theme-dark");

  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: container,
      pin: true,
      scrub: 1,
      start: "top top",
      end: "+=150%",
      snap: {
        snapTo: "labels",
        duration: { min: 0.3, max: 0.8 },
        delay: 0.1
      }
    }
  });

  // Phase 1: Fade out + 3D rotate side A
  tl.addLabel("exit")
    .to(sideA, {
      opacity: 0,
      rotateY: -90,
      scale: 0.9,
      duration: 0.4,
      ease: "power2.in",
      transformPerspective: 1200,
      transformOrigin: "center center"
    })
    .set(sideA, { display: "none" });

  // Phase 2: Flip layout
  tl.add(() => {
    const state = Flip.getState(".shared-element");
    container.classList.add("dark-theme");
    Flip.from(state, {
      duration: 0.6,
      ease: "power2.inOut",
      absolute: true,
      props: "backgroundColor,color"
    });
  });

  // Phase 3: Reveal side B
  tl.addLabel("enter")
    .set(sideB, {
      display: "flex",
      rotateY: 90,
      opacity: 0,
      transformPerspective: 1200,
      transformOrigin: "center center"
    })
    .to(sideB, {
      rotateY: 0,
      opacity: 1,
      scale: 1,
      duration: 0.4,
      ease: "power2.out"
    });

  // Phase 4: Stagger in content
  tl.from(".dark-theme .animate-in", {
    y: 30,
    opacity: 0,
    stagger: 0.06,
    duration: 0.3,
    ease: "power3.out"
  }, "-=0.2");

  tl.addLabel("complete");
});

// Mobile: click-based flip (no scroll)
mm.add("(max-width: 799px)", () => {
  const btn = document.querySelector(".theme-toggle");

  btn.addEventListener("click", () => {
    const state = Flip.getState(".shared-element, .card, .nav");
    document.body.classList.toggle("dark-theme");

    Flip.from(state, {
      duration: 0.6,
      ease: "power2.inOut",
      absolute: true,
      props: "backgroundColor,color",
      stagger: 0.03
    });
  });
});
```

---

## Key Resources

- [GSAP Flip Plugin Docs](https://gsap.com/docs/v3/Plugins/Flip/)
- [GSAP ScrollTrigger Docs](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
- [gsap.matchMedia() Docs](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/)
- [GSAP Timeline Docs](https://gsap.com/docs/v3/GSAP/Timeline)
- [ScrollTrigger Tips & Mistakes](https://gsap.com/resources/st-mistakes/)
- [Codrops: 3D Scroll-Driven Text Animations](https://tympanus.net/codrops/2025/11/04/creating-3d-scroll-driven-text-animations-with-css-and-gsap/)
- [Ryan Mulligan: Animating with the Flip Plugin](https://ryanmulligan.dev/blog/gsap-flip-cart/)
- [GSAP Community: Best Practices for Smooth Experience](https://gsap.com/community/forums/topic/32460-best-practices-for-the-smoothest-experience/)
- [GSAP Community: Flip + ScrollTrigger Scrub](https://gsap.com/community/forums/topic/35930-triggering-flipfrom-with-a-scrolltrigger-scrub-animation-weird-glitch/)
- [Paul Lewis: FLIP Your Animations](https://aerotwist.com/blog/flip-your-animations/)
