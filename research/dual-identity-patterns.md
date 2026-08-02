# Dual Identity Website Design Patterns — Research Findings

> Research compiled 2026-08-03
> Specific case: Portfolio for someone who is both a **Storyteller/Human** (warm, gold, serif, emotional) and an **Architect/Engineer** (cold, blue, monospace, technical)

---

## 1. Existing Design Patterns for Dual-Personality Sites

### 1.1 Split-Screen Static Layout

The most common approach. Two halves of the viewport, each showing a different identity. User clicks or scrolls to explore one side.

**How it works:**
- Left half: Identity A (warm, organic, serif typography)
- Right half: Identity B (cold, grid-based, monospace)
- A vertical divider line sits in the center, sometimes draggable
- Hovering one side causes the other to dim/blur

**Examples/Inspiration:**
- Agency sites showing "Creative" vs "Strategy" departments
- Photography portfolios with "Film" vs "Digital" sides
- Some architecture firms showing "Concept" vs "Execution"

**Pros:** Immediately communicates duality; low implementation complexity
**Cons:** Feels static; doesn't tell a story; wastes half the viewport

### 1.2 Scroll-Triggered Morph

The page starts in one identity and transforms into the other as the user scrolls past a defined threshold.

**How it works:**
- Hero section: Identity A fully rendered
- At ~50% scroll, a transition zone begins
- Background color shifts, typography morphs, layout restructures
- By the time scroll completes, Identity B is fully active
- The transition zone often uses a "wipe" or "reveal" effect

**Technical approach:**
- CSS `scroll-timeline` or GSAP ScrollTrigger
- CSS custom properties (`--bg`, `--text`, `--font-family`) interpolated via JS
- `mix-blend-mode` for visual blending in the transition zone

**Pros:** Narrative-driven; feels like a journey
**Cons:** User might not realize there are two identities; requires scroll commitment

### 1.3 Toggle/Switch with Dramatic Transition

A toggle button (often stylized as a physical switch, mask, or yin-yang) that flips the entire site between two modes.

**How it works:**
- A persistent UI element (toggle, button, or gesture) triggers the switch
- The transition is dramatic — not just color swap but layout, typography, imagery, and even content structure changes
- Often uses a full-screen wipe, page-turn, or morphing animation

**Examples:**
- Dark/light mode toggles that feel like turning a room's lights on/off
- "Creative/Technical" switches in developer portfolios
- "About me" pages with a literal mask that flips

**Pros:** User has control; can compare both sides; dramatic impact
**Cons:** Requires clear affordance so users know the toggle exists

### 1.4 Card-Flip / Page-Turn (Most Relevant to Our Case)

A physical metaphor where the entire page (or a key section) flips like a card or book page to reveal the other identity on the "back."

**How it works:**
- The page is treated as a 3D card with `perspective` on the parent container
- On trigger, `rotateY(180deg)` (or `rotateX` for vertical flip) is applied
- Front face = Identity A, back face = Identity B
- Both faces are absolutely positioned, with `backface-visibility: hidden`
- A "shadow" element underneath sells the 3D depth

**CSS Foundation:**
```css
.card-container {
  perspective: 2000px;
}

.card {
  transform-style: preserve-3d;
  transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.card.flipped {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
}

.card-face--back {
  transform: rotateY(180deg);
}
```

**Enhancement layers:**
- GSAP for orchestrated multi-property animation (not just rotation)
- A "page curl" shader (WebGL) for realistic paper-turning
- Sound effect on flip (subtle paper rustle)
- Tilt shift / depth-of-field blur during rotation
- Content fades in AFTER flip completes (staggered reveal)

**Pros:** Perfect metaphor for duality; tactile and memorable; clear "two sides" message
**Cons:** Needs careful performance tuning; 3D transforms can be janky on low-end devices

---

## 2. Dramatic Dark/Light Mode Transitions (Beyond Color Swap)

### 2.1 What Most Sites Do (Boring)
- Swap `background-color` and `text-color` with a CSS transition
- Maybe invert some images
- Done in 0.3s — forgettable

### 2.2 What Great Sites Do

**a) Full-screen radial wipe**
- A circle expands from the toggle button's position
- Inside the circle: new theme; outside: old theme
- The circle grows until it covers the entire viewport
- Implementation: `clip-path: circle(0% at x y)` → `clip-path: circle(150% at x y)`

**b) Diagonal wipe with parallax**
- A diagonal line sweeps across the screen
- Content on one side is "old theme," other side is "new theme"
- The line has a slight 3D tilt, creating depth
- Content elements have staggered delays as the wipe passes over them

**c) Element-by-element morph**
- Each element on the page transitions independently
- Background goes first, then text, then images, then borders
- Creates a "wave" effect across the page
- Uses Intersection Observer + staggered `transition-delay`

**d) Inversion with texture shift**
- The entire page gets a CSS `filter: invert(1)` with a hue-rotate
- But THEN individual elements are re-inverted to correct their colors
- Combined with a texture overlay shift (light noise → dark noise)
- Creates a photographic negative effect

**e) The "Light Switch" metaphor**
- Screen briefly goes completely black (100ms)
- Then the new theme "turns on" with a brief brightness bloom/flare
- A vignette effect fades in from the edges
- Audio: optional click sound

### 2.3 Key Principle
The transition should feel like entering a **different room**, not repainting the same room. This means:
- Typography changes (not just color — actual font swap)
- Layout shifts (grid density, spacing)
- Imagery style changes (warm filters → cold filters)
- Motion personality changes (organic easing → mechanical easing)

---

## 3. Split-Screen → Full-Page Morph Transitions

### 3.1 The "Doors" Pattern
- Two halves of the screen (left and right) close together like doors
- Behind the doors, the new page/identity loads
- The doors then open outward, revealing the new content
- GSAP timeline: scale X from 0→1 (close), swap content, scale X from 1→0 (open)

### 3.2 The "Curtain" Pattern
- One half slides over the other like a curtain
- The sliding half carries the new theme's background
- As it covers the old content, new content fades in on top
- Often used in full-page sliders (Swiper.js with creative effect)

### 3.3 The "Merge" Pattern
- Two split-screen halves move toward center and merge
- At the merge point, a flash/glow effect
- Then they expand outward again, now showing new content
- Works beautifully for showing two identities becoming one

### 3.4 The "Shatter" Pattern
- The split-screen divider "cracks" and the two halves shatter into fragments
- Fragments fly apart, revealing the new page behind them
- Three.js / WebGL particle system
- Most complex to implement but highest impact

---

## 4. "Two-Faced" Portfolio Design Case Studies

### 4.1 The Mask Portfolio
**Concept:** A portrait photo of the designer where half the face is artistic/painterly and the other half is wireframe/schematic. Clicking each half takes you to that identity's section.

**Execution:**
- Hero: Full-bleed portrait, split down the middle
- Left half: Oil painting style, warm tones, hand-drawn elements
- Right half: Blueprint style, cold tones, grid lines
- The divider line follows the face's center line (nose, lips)
- Hovering either half causes that side to "come alive" (subtle animation)

### 4.2 The Jekyll & Hyde Portfolio
**Concept:** Two completely different websites living at the same URL. A toggle (often a pill-shaped button reading "Creative ↔ Technical") switches between them.

**Execution:**
- Both "sites" share the same URL and navigation structure
- But visual design, copy tone, project presentation, and even page transitions differ
- The toggle is always visible, usually in the header
- State persists via localStorage
- Some versions show a split preview on the landing page before you choose

### 4.3 The Yin-Yang Portfolio
**Concept:** A circular motif where one half is warm and the other cold. As you scroll, the balance between the two shifts — more of one, less of the other.

**Execution:**
- Hero: Yin-yang inspired graphic with actual content embedded in each half
- Scroll: The dividing line curves and shifts, changing the proportion
- Sections alternate between identities
- The yin-yang motif appears in micro-interactions (loading spinners, hover states)

### 4.4 The Before/After Portfolio
**Concept:** A slider or scrubber that reveals the "raw" (human/storytelling) and "processed" (technical/architectural) versions of the same work.

**Execution:**
- A vertical divider the user can drag left/right
- Left of divider: Sketches, mood boards, emotional narratives
- Right of divider: Wireframes, code, technical specifications
- The divider has a label: "The Story" | "The System"

---

## 5. The Transition Point — How Designers Handle It

### 5.1 Trigger Mechanisms

| Trigger | Feel | Best For |
|---------|------|----------|
| **Scroll position** | Narrative, journey | Long-form storytelling |
| **Click/tap button** | Deliberate, user-controlled | Toggle between modes |
| **Hover zone** | Exploratory, playful | Split-screen layouts |
| **Time-based** | Cinematic, automatic | Landing page intros |
| **Gesture (swipe)** | Physical, tactile | Mobile-first designs |
| **Mouse position** | Ambient, responsive | Immersive experiences |
| **Scroll velocity** | Dynamic, reactive | Scroll-driven animations |

### 5.2 Smoothing Techniques

**a) Shared Element Transitions (View Transitions API)**
- Elements that exist in both identities (logo, navigation) stay pinned
- Only the "changing" elements transition
- Uses `document.startViewTransition()` for native browser support
- Elements with `view-transition-name` morph between their two states

**b) Color interpolation in OKLCH**
- Don't interpolate in RGB (ugly muddy midpoints)
- Use OKLCH color space for perceptually smooth color transitions
- `color-mix(in oklch, var(--warm-gold), var(--cold-blue), var(--progress))`

**c) Typography interpolation**
- Don't just swap fonts — cross-fade them
- Both fonts load simultaneously; one fades out as the other fades in
- For variable fonts: interpolate weight, width, and slant axes
- At the midpoint, both fonts are at 50% opacity — creates a ghostly hybrid

**d) Layout morphing**
- Use CSS `contain: layout` for isolation
- Animate `grid-template-columns` and `grid-template-rows`
- Or use the FLIP technique (First, Last, Invert, Play) for position changes

**e) Easing curves per identity**
- Warm/organic identity: `cubic-bezier(0.25, 0.46, 0.45, 0.94)` — ease-out with overshoot
- Cold/technical identity: `cubic-bezier(0.4, 0, 0.2, 1)` — material design standard
- Transition between them: interpolate the curve itself based on progress

### 5.3 The "In-Between" Moment

The most interesting design opportunity is the **midpoint** of the transition — the moment when neither identity is fully present. Designers use this moment to:

- Show a brief "neutral" state (black/white, no personality)
- Display a unifying message: "Both of these are me"
- Show a visual metaphor (two colors mixing, two shapes merging)
- Create a "glitch" effect that resolves into the new identity
- Display a morphing logo that represents the fusion

---

## 6. Specific Recommendation: Storyteller/Human ↔ Architect/Engineer

### 6.1 The Design System

| Property | Storyteller (Face A) | Architect (Face B) |
|----------|---------------------|-------------------|
| **Background** | Warm cream `#FAF6F0` | Cool dark `#0A1628` |
| **Primary text** | Rich charcoal `#2D2A26` | Clean white `#E8EDF3` |
| **Accent** | Gold `#C8963E` | Electric blue `#3B82F6` |
| **Heading font** | Playfair Display / Lora (serif) | JetBrains Mono / IBM Plex Mono |
| **Body font** | Source Serif Pro / Merriweather | Inter / IBM Plex Sans |
| **Layout** | Asymmetric, editorial, generous whitespace | Grid-based, dense, systematic |
| **Images** | Warm filters, film grain, soft focus | Cold filters, sharp, high contrast |
| **Motion** | Organic, spring-based easing | Mechanical, linear-ish easing |
| **Borders** | Soft, rounded, hand-drawn feel | Sharp, precise, pixel-perfect |
| **Shadows** | Warm, diffused, layered | Cold, hard-edged, minimal |

### 6.2 The Card-Flip Implementation

**Structure:**
```
<div class="identity-card" data-state="storyteller">
  <div class="card-face card-front">
    <!-- Storyteller content -->
  </div>
  <div class="card-face card-back">
    <!-- Architect content -->
  </div>
</div>
```

**The Flip Trigger:**
- A persistent toggle in the header: two overlapping circles (one gold, one blue)
- Also triggered by a keyboard shortcut (e.g., `T` for toggle)
- On mobile: a swipe gesture (left/right) or a floating action button
- The toggle rotates 180° along with the card, reinforcing the physical metaphor

**The Animation Sequence (using GSAP):**

```javascript
// Phase 1: Lift (0-0.2s) — Card "lifts" toward viewer
// scale: 1 → 1.05, shadow grows, slight rotateX tilt

// Phase 2: Flip (0.2-0.6s) — The actual rotation
// rotateY: 0 → 180deg, perspective maintained

// Phase 3: Land (0.6-0.8s) — Card "settles" onto surface
// scale: 1.05 → 1, shadow reduces, slight bounce

// Phase 4: Content Reveal (0.8-1.2s) — New content fades in
// Staggered: headings first (0.1s delay), then body (0.2s), then images (0.3s)
```

**Enhancement Details:**
- During Phase 2, a subtle paper texture overlay appears at the rotation's edge
- The background color transitions independently (doesn't wait for the flip)
- Navigation items morph (serif ↔ mono) with a slight delay
- A very subtle sound effect (optional): page turn / paper rustle
- The gold/blue accent color cross-fades through OKLCH interpolation

### 6.3 Page-Level Architecture

```
Landing Page (split-screen preview)
├── Left half: Storyteller world (warm, inviting)
├── Right half: Architect world (cool, precise)
├── Center: "Choose your lens" or auto-progresses
│
├── /storyteller (or scroll/flip to reveal)
│   ├── Hero: Personal narrative, emotional hook
│   ├── Projects: Case studies with storytelling focus
│   ├── About: Personal journey, values, voice
│   └── Contact: Conversational, warm tone
│
├── /architect (or scroll/flip to reveal)
│   ├── Hero: Technical capabilities, systems thinking
│   ├── Projects: Technical breakdowns, architecture diagrams
│   ├── About: Skills matrix, technical philosophy
│   └── Contact: Structured form, professional tone
│
└── /unified (optional hidden section)
    └── Where both identities overlap — the real person
```

### 6.4 Technical Stack Recommendation

- **Animation engine:** GSAP 3 + ScrollTrigger + Flip plugin
- **3D transforms:** CSS `transform-style: preserve-3d` + `perspective`
- **Color transitions:** CSS custom properties with OKLCH interpolation
- **Font loading:** `font-display: swap` with both font families preloaded
- **View Transitions API:** For SPA-style page morphing (with GSAP fallback)
- **State management:** Simple `data-identity` attribute on `<html>` + localStorage
- **Performance:** `will-change: transform` on the card; `contain: layout` on faces
- **Accessibility:** `prefers-reduced-motion` → instant swap instead of flip; ARIA live regions for content changes

### 6.5 Mobile Considerations

- Full-viewport card flip works well on mobile (portrait)
- The toggle becomes a floating pill at the bottom of the screen
- Swipe gesture: swipe left for Architect, right for Storyteller (or vice versa)
- On very small screens, the split-screen landing page stacks vertically instead
- Reduce animation complexity on low-end devices (`navigator.hardwareConcurrency` check)

---

## 7. Key References & Inspiration Sources

### Codrops / Tympanus
- **Persistent Page Transitions with WebGPU** (2026) — GPU-powered seamless transitions between pages using persistent canvas scenes. Demonstrates how to eliminate DOM "popping" during transitions.
- **GSAP Flip Transitions** — Extensive use of GSAP's Flip plugin for layout animations that morph between states.
- **Scroll-Driven Animations** — CSS `scroll-timeline` and `animation-timeline` for scroll-based effects.

### Awwwards Portfolio Collection
- Curated collection of award-winning portfolio sites at awwwards.com/websites/portfolio
- Many feature creative dual-theme or split-personality approaches
- Architecture category sites often use the cold/precise aesthetic relevant to the Engineer side

### CSS / Animation Techniques
- **FLIP Animation Technique** (First, Last, Invert, Play) by Paul Lewis — for performant layout animations
- **View Transitions API** — Native browser API for page-to-page transitions with shared element morphing
- **CSS `scroll-timeline`** — Scroll-linked animations without JavaScript
- **OKLCH Color Space** — Perceptually uniform color interpolation for smooth theme transitions
- **CSS `perspective` and `transform-style: preserve-3d`** — Foundation for card-flip effects

### GSAP Ecosystem
- **GSAP 3** — Industry-standard animation library
- **ScrollTrigger** — Scroll-based animation triggers
- **Flip Plugin** — Layout animation between states
- **MotionPath** — Animate along SVG paths
- **SplitText** — Character/word/line-level text animation

### Design Inspiration
- Dribbble: "split personality portfolio" and "dual theme website" searches
- Behance: "dark light mode transition" and "portfolio concept" collections
- Awwwards SOTD: Filter by "portfolio" + "animation" categories
- SiteInspire: Filter by "personal" category for individual portfolio inspiration

---

## 8. Summary: The Ideal Approach for This Project

The **card-flip metaphor** is the strongest fit because:

1. **It's physical** — flipping a card/page is a universal human experience
2. **It clearly communicates duality** — two distinct sides, one object
3. **It's interactive** — the user controls when the flip happens
4. **It's memorable** — nobody forgets a site that literally flips between two worlds
5. **It scales well** — works on desktop (click) and mobile (swipe)

The transition should be **orchestrated, not instant**:
- Background shifts first (sets the mood)
- Card lifts slightly (builds anticipation)
- Card rotates (the dramatic moment)
- Content reveals staggered (lets the user absorb the new world)
- Typography morphs last (the final detail that sells the new identity)

The key insight: **the transition IS the content**. The way you flip between identities says as much about the person as either identity alone. Make it beautiful, make it intentional, make it feel like turning a page in a book — because that's exactly what a storyteller-architect would do.
