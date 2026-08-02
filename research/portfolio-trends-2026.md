# Portfolio Website Trends 2025–2026: Research for "Two-Faced" Personal Site

> **Research Date:** 2026-08-03  
> **Sources:** Awwwards, CSS Design Awards, Codrops case studies, direct site analysis  
> **Goal:** Inform design of a dual-personality portfolio (Storyteller × Architect)

---

## TOP 20 Portfolio & Award-Winning Sites (2025–2026)

### 1. Spectral Field — Rob FWA
- **URL:** https://www.robfwa.com/
- **Award:** CSS Design Awards WOTD (Aug 2, 2026) — Score 8.17
- **Key Technique:** Canvas 2D + Perlin noise + FFT audio visualization. Users drop an audio file and a generative artwork is created in real-time using Web Audio API (FFT 2048) and procedural noise. Client-side only — audio never leaves the device.
- **Standout:** The entire site IS the portfolio piece. No traditional project grid — you experience the work by interacting with it. Canvas-based generative art responds to audio frequency data.
- **Tech:** Vanilla JS, Canvas 2D API, Web Audio API, Perlin noise
- **"Two-Faced" Application:** The audio-reactive canvas could switch visual palettes between "storyteller" (warm, organic noise) and "architect" (geometric, structured patterns) based on persona state.

---

### 2. Le Mans Classic — Richard Mille
- **URL:** https://lemansclassic.richardmille.com/
- **Award:** CSS Design Awards WOTD (Jul 16, 2026) — Score 8.34
- **Key Technique:** Cinematic storytelling with time-based chapters (06:30 Departure → 20:30 The night). Scroll-driven narrative with atmospheric photography, ambient sound toggle, and immersive "Below the Line" documentary framing.
- **Standout:** Each section is a time-stamped chapter. The scroll experience feels like reading a photojournalism piece, not browsing a website. Sound design integral to immersion.
- **Tech:** Scroll-based animations, ambient audio, chapter-based navigation
- **"Two-Faced" Application:** Time-based or scroll-depth-triggered persona transitions. The "storyteller" persona could use this chapter-based narrative approach, while the "architect" persona uses a more structured grid.

---

### 3. Nite Riot
- **URL:** https://www.nite-riot.com/
- **Award:** Featured on Codrops (Apr 2025), Awwwards recognized
- **Key Technique:** **Difference Blend Mode** as a unifying design system — applied to typography, imagery overlays, video hovers, page transitions, scroll effects, the logo, dark/light theme toggling, and even the 404 page. Horizontal case study scrolling with seamless case-to-case transitions.
- **Standout:** A single CSS property (`mix-blend-mode: difference`) becomes the entire design identity. Dark/light theme toggle reverses the entire color palette with zero redundant styles.
- **Tech Stack:** Webflow + GSAP + Barba.js + Embla.js + Lenis + Glightbox
- **Custom Easings:**
  - `easeSlowStartFastEnd`: `cubic-bezier(0.2, 0, 0.1, 1)`
  - `easeFastStartSmoothEnd`: `cubic-bezier(0.75, 0, 0, 1)`
  - `easeHeadings`: `cubic-bezier(0.75, 0, 0, 0.35)`
- **"Two-Faced" Application:** **MUST STUDY.** The Difference Blend Mode technique is perfect for a two-faced site — one persona could be the "normal" view, and the other could be the "difference" inverted view. A single toggle flips everything. The custom easing library approach also ensures consistent motion personality.

---

### 4. Roman Jean-Elie — WebGL Portfolio
- **URL:** https://www.romanjeanelie.com/
- **Award:** Codrops case study (Nov 2025)
- **Key Technique:** **WebGL fold effect** with directional freedom (vector projection in GLSL), **MeshPortal** technique for embedding 3D scenes within bounded DOM areas, 3D character (Mixamo) inside a portal that transitions between sections.
- **Standout:** The portal tracks DOM element bounds and converts them to WebGL coordinates, creating a "screen within a screen" that morphs position/size as you navigate. The fold effect uses circular arc mathematics with fake shadow based on curvature.
- **Tech Stack:** Next.js + Three.js/React Three Fiber + GSAP
- **GLSL Snippet (Fold Effect):**
  ```glsl
  vec2 dir = normalize(uDirection);
  float projValue = dot(vec2(position.xy), dir);
  vec2 curledPosition = curlPlane(projValue, effectiveSize, uCurlX, uCurlY, true);
  newposition.xy += dir * (curledPosition.x - projValue);
  newposition.z += curledPosition.y;
  ```
- **"Two-Faced" Application:** The MeshPortal technique could show two different 3D worlds — one for each persona. The fold effect could be the transition between them, literally "folding" the page from storyteller to architect mode.

---

### 5. homunculus Inc. 2026
- **URL:** https://homunculus.jp/
- **Award:** CSS Design Awards WOTD (Jul 30, 2026) — Score 8.14
- **Key Technique:** Immersive entrance experience with sound toggle (Enter with/without Sound). Japanese/English bilingual with overlay-based content panels. Minimal navigation with "Inside/Return" paradigm.
- **Standout:** The site begins with a choice — sound or silence. Content revealed through overlays with smooth transitions. The "Inside" metaphor creates a sense of entering a different space.
- **"Two-Faced" Application:** The "Enter with/without Sound" concept could become "Enter as Storyteller / Enter as Architect." The overlay-based content system supports dual content layers.

---

### 6. Russell Numo — Portfolio
- **URL:** https://www.russellnumo.nl/
- **Award:** CSS Design Awards WOTD (Jul 26, 2026) — Score 8.00
- **Key Technique:** Triple-identity hero section — "Frontend developer / UX/UI Designer / Creative" with repeated text that animates between roles. Interactive services section with clickable labels that expand descriptions. Progress bar at bottom.
- **Standout:** The hero explicitly presents multiple personas simultaneously. The services section uses a playful "← click me / click me →" interaction pattern. Amsterdam-based, clean motion design.
- **"Two-Faced" Application:** **DIRECTLY RELEVANT.** This site already demonstrates multi-persona presentation. The repeated text technique (title appearing multiple times with different emphasis) could represent the two faces.

---

### 7. Motiondeep
- **URL:** https://www.motiondeep.com
- **Award:** CSS Design Awards WOTD (Jul 29, 2026) — Score 8.25
- **Key Technique:** Gyroscope-based camera control ("TILT PHONE L OR R TO MOVE CAMERA"). Motion design, game dev, and experiential 3D portfolio with a playable game link (mechstorm.io).
- **Standout:** The portfolio itself is a 3D environment. Mobile gyroscope input controls the camera perspective — physical device movement = digital exploration.
- **"Two-Faced" Application:** Device orientation or mouse position could control which persona is visible. Tilt left = storyteller, tilt right = architect. The 3D environment could have two distinct zones.

---

### 8. Stokt — Creative Company
- **URL:** https://wearestokt.com/
- **Award:** CSS Design Awards WOTD (Jan 31, 2026) — Score 7.93
- **Key Technique:** Bold layout, motion, and 3D blended into a Framer-built platform. Evolving digital identity with experiments and animations showcased inline.
- **Standout:** Built entirely on Framer, proving that no-code/low-code platforms can achieve award-winning results. The "evolving identity" concept means the site itself changes over time.
- **"Two-Faced" Application:** Framer could be used for rapid prototyping of the dual-persona concept. The "evolving identity" approach means the two faces could shift and change over time.

---

### 9. Noomo Showcase
- **URL:** https://showcase.noomoagency.com
- **Award:** CSS Design Awards WOTD (Jul 25, 2026) — Score 8.03
- **Key Technique:** Immersive 3D & WebGL showcase with linked sub-sites for different aspects (Agency, Labs, Storytelling). Loading percentage indicator.
- **Standout:** The portfolio is split into distinct experiences — each sub-site has its own personality and technical approach, unified under one brand.
- **"Two-Faced" Application:** The multi-site architecture (Agency / Labs / Storytelling) directly maps to a dual-persona approach. Each "face" could be a distinct sub-experience.

---

### 10. Cipher
- **URL:** https://cipher.tv/
- **Award:** CSS Design Awards WOTD (Jul 23, 2026) — Score 8.15
- **Key Technique:** Minimal navigation with works/talents/about structure. Studio Jour Paris collaboration.
- **Standout:** Extremely minimal interface — the work speaks for itself. The "talents" section highlights people, not just projects.
- **"Two-Faced" Application:** The minimal approach could work for the "architect" persona (clean, structured) while the "storyteller" persona uses more expressive techniques.

---

### 11. Cula Technologies
- **URL:** https://www.cula.tech/
- **Award:** CSS Design Awards WOTD (Jul 28, 2026) — Score 8.15
- **Key Technique:** Tech-forward design with interactive elements and smooth transitions.
- **"Two-Faced" Application:** Tech aesthetic for the "architect" persona.

---

### 12. Jesko Jets
- **URL:** https://jeskojets.com
- **Award:** CSS Design Awards WOTD (Jul 22, 2026) — Score 8.16
- **Key Technique:** Luxury/aviation aesthetic with high-end visual presentation.
- **"Two-Faced" Application:** Luxury presentation techniques for premium feel in either persona.

---

### 13. The Watch — 60fps
- **URL:** https://thewatch.60fps.fr/
- **Award:** CSS Design Awards WOTD (Jul 17, 2026) — Score 8.34
- **Key Technique:** High-frame-rate animations (60fps namesake). Performance-focused motion design.
- **"Two-Faced" Application:** Performance-optimized animations ensure smooth persona transitions.

---

### 14. Duyu Care
- **URL:** https://duyucare.dops.agency/
- **Award:** CSS Design Awards WOTD (Jul 24, 2026) — Score 8.14
- **Key Technique:** Wellness/care aesthetic with gentle animations and calming color palette.
- **"Two-Faced" Application:** The gentle, human-centered approach could inform the "storyteller" persona's emotional tone.

---

### 15. Dr Grigoriak
- **URL:** https://grigoriak.doctor/
- **Award:** CSS Design Awards WOTD (Jul 21, 2026) — Score 8.15
- **Key Technique:** Medical/professional portfolio with clean typography and trust-building design.
- **"Two-Faced" Application:** Professional credibility techniques for the "architect" persona.

---

### 16. Flowty
- **URL:** https://flowty.co
- **Award:** CSS Design Awards WOTD (Jul 18, 2026) — Score 8.08
- **Key Technique:** Flow-based interactions with smooth scroll experiences.
- **"Two-Faced" Application:** Flow-state transitions between personas.

---

### 17. Nudot Studio
- **URL:** https://www.nudot.com.tw
- **Award:** CSS Design Awards WOTD (Jul 19, 2026) — Score 8.04
- **Key Technique:** "Cosmic Series" with rotating cosmic-themed visuals. Services displayed as floating keywords (Core-Site, Gen-AI Visual, Motion Flow, WebGL Realm, 3D Matrix). Bilingual (Chinese/English) with sophisticated typography.
- **Standout:** The keyword constellation approach — services and capabilities float as individual elements that could be rearranged. 14 years of visual mastery, 400+ deployed works.
- **"Two-Faced" Application:** The keyword constellation could represent different aspects of each persona. The cosmic/organic visuals for storyteller, structured matrix for architect.

---

### 18. Noho
- **URL:** https://noho.ink
- **Award:** CSS Design Awards WOTD (Jul 31, 2026) — Score 8.22
- **Key Technique:** Sustainability-focused furniture site with 3D model viewer (GLB files), energy usage awareness (dark mode saves 35% battery), reduce animation toggle, and quiz-based product recommendation.
- **Standout:** Environmental consciousness built into the design system itself. Dark mode isn't just aesthetic — it's an energy-saving feature. The "Reduce Animation" toggle acknowledges that animations have a real cost.
- **"Two-Faced" Application:** The energy-awareness approach could inform persona-specific performance modes. "Storyteller" = full animations, "Architect" = reduced animations for focus.

---

### 19. /zeroz Brand Site
- **URL:** https://otsuka-air.jp/
- **Award:** CSS Design Awards WOTD (Jul 27, 2026) — Score 8.09
- **Key Technique:** Japanese brand site with atmospheric design and brand storytelling.
- **"Two-Faced" Application:** Japanese design aesthetics for refined visual language.

---

### 20. Fitosauna
- **URL:** https://fitosauna.com/
- **Award:** CSS Design Awards WOTD (Jul 20, 2026) — Score 8.11
- **Key Technique:** Wellness/lifestyle brand with immersive product experience.
- **"Two-Faced" Application:** Immersive product presentation techniques.

---

## KEY TECHNIQUES & PATTERNS

### A. Page Transition Systems

| Technique | Library | Description | Best For |
|-----------|---------|-------------|----------|
| **Barba.js + GSAP** | barba.js.org | AJAX-based page transitions with GSAP animations | Multi-page sites with seamless transitions |
| **View Transitions API** | Native browser | `document.startViewTransition()` for SPA/MPA transitions | Modern browsers, simpler implementation |
| **Highway.js** | highway.js | Lightweight page transition router | Lighter alternative to Barba.js |
| **GSAP MorphSVG** | GSAP Plugin | SVG path morphing between page states | Icon/logo transitions between personas |

**Recommended for Two-Faced Site:** Barba.js + GSAP for page transitions, with GSAP MorphSVG for the persona-switch icon animation.

### B. CSS/JS Transition Techniques

#### Mix-Blend-Mode: Difference (from Nite Riot)
```css
/* The entire persona toggle could use this */
.persona-toggle {
  mix-blend-mode: difference;
  transition: all 0.6s cubic-bezier(0.75, 0, 0, 1);
}

/* Dark/light theme without redundant styles */
.architect-mode {
  background: #000;
  color: #fff;
}
.storyteller-mode {
  background: #fff;
  color: #000;
}
/* Difference mode handles the inversion automatically */
```

#### Custom Easings (from Nite Riot)
```css
:root {
  --ease-slow-start-fast-end: cubic-bezier(0.2, 0, 0.1, 1);
  --ease-fast-start-smooth-end: cubic-bezier(0.75, 0, 0, 1);
  --ease-headings: cubic-bezier(0.75, 0, 0, 0.35);
}
```

#### Scroll-Driven Animations (CSS Houdini)
```css
@keyframes persona-reveal {
  from { opacity: 0; transform: translateY(100px); }
  to { opacity: 1; transform: translateY(0); }
}

.persona-section {
  animation: persona-reveal linear;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}
```

### C. 3D / WebGL Techniques

#### MeshPortal (from Roman Jean-Elie)
- Render a separate 3D scene to a Frame Buffer Object (FBO)
- Display the FBO texture on a plane mesh with a custom mask shader
- Track DOM element bounds and convert to WebGL coordinates
- Animate portal position/size between sections

#### Fold Effect (GLSL)
- Vector projection for directional folding
- Circular arc mathematics for realistic curvature
- Fake shadow based on curvature amount
- Back-face rendering with separate texture

#### Gyroscope Camera Control (from Motiondeep)
```javascript
window.addEventListener('deviceorientation', (e) => {
  camera.rotation.y = THREE.MathUtils.degToRad(e.gamma * 0.5);
  camera.rotation.x = THREE.MathUtils.degToRad(e.beta * 0.5);
});
```

### D. Audio-Reactive Techniques (from Spectral Field)
- Web Audio API with FFT analysis (2048-point)
- Perlin noise for organic visual generation
- Canvas 2D for performance-critical rendering
- Client-side only processing (privacy-first)

---

## DUAL-PERSONA / SPLIT-IDENTITY PATTERNS

### Pattern 1: Blend Mode Toggle (Recommended)
**Inspiration:** Nite Riot's Difference Mode
- **How:** Use `mix-blend-mode: difference` on a full-screen overlay
- **Effect:** Single toggle inverts entire site — colors, images, text
- **Persona A (Storyteller):** Warm colors, organic shapes, narrative scroll
- **Persona B (Architect):** Inverted palette, geometric grid, structured layout

### Pattern 2: Portal/Window Reveal
**Inspiration:** Roman Jean-Elie's MeshPortal
- **How:** A "window" on the page shows a different 3D world depending on persona
- **Effect:** The portal morphs position and content as you scroll
- **Persona A:** Organic 3D environment (trees, waves, particles)
- **Persona B:** Architectural 3D environment (buildings, blueprints, grids)

### Pattern 3: Split-Screen Coexistence
**Inspiration:** Russell Numo's multi-identity hero
- **How:** Both personas visible simultaneously, separated by a draggable divider
- **Effect:** User controls the ratio between the two identities
- **Interaction:** Drag center divider to reveal more of one persona

### Pattern 4: Chapter-Based Narrative
**Inspiration:** Le Mans Classic's time-stamped chapters
- **How:** Scroll through a story where each chapter alternates persona
- **Effect:** The narrative itself IS the transition between identities
- **Structure:** Storyteller chapter → Architect chapter → Storyteller chapter...

### Pattern 5: Audio-Driven Switching
**Inspiration:** Spectral Field's audio reactivity
- **How:** Different audio frequencies trigger different visual states
- **Effect:** Music/voice controls which persona is dominant
- **Low frequencies:** Storyteller (warm, organic)
- **High frequencies:** Architect (geometric, structured)

---

## RECOMMENDED TECH STACK FOR TWO-FACED SITE

### Core
- **Framework:** Next.js (for SSR + React Three Fiber integration)
- **Animation:** GSAP + ScrollTrigger + MorphSVG
- **Page Transitions:** Barba.js or View Transitions API
- **3D:** Three.js / React Three Fiber (for portal effects)
- **Smooth Scroll:** Lenis

### CSS
- **Blend Modes:** `mix-blend-mode: difference` for persona toggle
- **Custom Properties:** CSS variables for theme switching
- **Scroll-Driven Animations:** CSS Houdini `animation-timeline`
- **Container Queries:** Responsive persona-specific layouts

### Performance
- **Reduced Motion:** Respect `prefers-reduced-motion` (like Noho)
- **Energy Awareness:** Optional reduced-animation mode
- **Lazy Loading:** Defer 3D/WebGL assets until persona is active

---

## DESIGN PRINCIPLES EXTRACTED

1. **One Big Idea:** Every award-winning site has a single unifying concept (Difference Mode, Fold Effect, Time-based Chapters). For a two-faced site, the "big idea" IS the duality itself.

2. **Custom Easings Matter:** Don't use default CSS easings. Create a library of 3-4 custom easings that define your motion personality.

3. **Preloader as Overture:** The loading screen sets the emotional tone. For a two-faced site, the preloader could show both personas merging/splitting.

4. **Horizontal Scrolling for Case Studies:** Multiple sites use horizontal scroll for project showcases. One persona could use vertical, the other horizontal.

5. **Sound as First-Class Citizen:** homunculus offers "Enter with/without Sound." Audio should be integral, not afterthought.

6. **404 Pages as Easter Eggs:** Nite Riot's 404 uses double Difference Mode. The error page could be a third "hidden" persona.

7. **Drag Interactions:** Nite Riot's "Inspired" page uses drag-to-explore with color inversion. Drag gestures could control persona blending.

---

## NEXT STEPS

- [ ] Prototype the Difference Blend Mode toggle with two color palettes
- [ ] Build a GSAP easing library with 3-4 custom curves
- [ ] Experiment with Barba.js page transitions between persona "pages"
- [ ] Create a MeshPortal proof-of-concept with two 3D environments
- [ ] Design the preloader as a persona-merge animation
- [ ] Test audio-reactive persona switching with Web Audio API

---

*Research compiled from Awwwards, CSS Design Awards, Codrops, and direct site analysis.*
