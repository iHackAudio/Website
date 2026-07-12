# CSS MAP — Portfolio Customization Reference

> Last updated: All sections complete (landing + builds page)

---

## Global Variables (`:root`)

| Variable | Value | Description |
|----------|-------|-------------|
| `--bg-0` | `#030712` | Deepest background |
| `--bg-1` | `#060a14` | Primary background |
| `--bg-2` | `#0a0e1a` | Card/section background |
| `--bg-3` | `#0f172a` | Elevated surface |
| `--bg-4` | `#1e293b` | Border/highlight surface |
| `--accent` | `#38bdf8` | Primary accent (sky blue) |
| `--accent-dim` | `#0c4a6e` | Muted accent |
| `--purple` | `#7c3aed` | Secondary accent |
| `--purple-dim` | `#1a0a2e` | Muted purple |
| `--gold` | `#fbbf24` | Highlight/achievement |
| `--gold-dim` | `#1a1000` | Muted gold |
| `--green` | `#4ade80` | Success/active |
| `--green-dim` | `#052e16` | Muted green |
| `--red` | `#f87171` | Error/constraint |
| `--text-1` | `#f8fafc` | Brightest text |
| `--text-2` | `#e2e8f0` | Primary text |
| `--text-3` | `#94a3b8` | Muted text |
| `--text-4` | `#475569` | Dimmest text |
| `--border` | `#1e293b` | Default border |
| `--border-accent` | `#1e3a5f` | Accent border |
| `--mono` | `'Space Mono', monospace` | Monospace font |
| `--sans` | `'Inter', sans-serif` | Sans-serif font |
| `--transition` | `all 0.3s cubic-bezier(0.4,0,0.2,1)` | Default transition |

---

## Section Index

| # | Section | ID | File Location | Description |
|---|---------|-----|---------------|-------------|
| 1 | Hero + About Me | `#hero` | index.html | Landing viewport with name, title, photo |
| 2 | The Numbers | `#numbers` | index.html | Horizontal impact strip |
| 3 | What I Built (Teaser) | `#builds-teaser` | index.html | 2-3 featured builds + CTA |
| 4 | Built on $0 | `#foundation` | index.html | Obstacles narrative |
| 5 | Published Work | `#work` | index.html | Podcasts, audiobooks, audio players |
| 6 | Technical Stack | `#stack` | index.html | Two-column tools layout |
| 7 | Experience | `#experience` | index.html | Timeline |
| 8 | Contact | `#contact` | index.html | CTA + links |
| 9 | Builds Deep Dive | `#builds` | builds.html | Zigzag alternating layout |

---

## Section 1: Hero + About Me (`#hero`)

**Layout:** Full viewport, centered content with photo
**Key selectors:**
- `#hero` — Section container
- `.hero-inner` — Content wrapper
- `.hero-name` — Name heading
- `.hero-role` — Title/role line
- `.hero-statement` — One-liner description
- `.hero-about` — About me paragraph
- `.hero-photo` — Profile photo container
- `.hero-bg` — Background gradient overlay
- `.hero-grid` — Grid pattern overlay

**Customization:**
- Change name: edit `.hero-name` content
- Change photo: update `src` in `.hero-photo img`
- Adjust gradient: modify `.hero-bg` background property
- Grid opacity: modify `.hero-grid` opacity

---

## Section 2: The Numbers (`#numbers`)

**Layout:** Horizontal strip, 6 items
**Key selectors:**
- `#numbers` — Section container
- `.numbers-grid` — Flex/grid container
- `.number-item` — Individual stat
- `.number-val` — Stat value (animated)
- `.number-lbl` — Stat label

**Customization:**
- Add/remove stats: edit `.number-item` elements
- Change values: update `data-target` attribute for count-up
- Animation speed: modify JS `duration` in count-up function

---

## Section 3: What I Built Teaser (`#builds-teaser`)

**Layout:** 2-3 featured cards + CTA button
**Key selectors:**
- `#builds-teaser` — Section container
- `.teaser-grid` — Card grid
- `.teaser-card` — Individual build card
- `.teaser-card img` — Build screenshot
- `.teaser-cta` — "See all builds" button

---

## Section 4: Built on $0 (`#foundation`)

**Layout:** Split — narrative left, obstacles right
**Key selectors:**
- `#foundation` — Section container
- `.foundation-grid` — Two-column grid
- `.foundation-narrative` — Left text column
- `.foundation-obstacles` — Right obstacles grid
- `.obstacle-card` — Individual obstacle item

---

## Section 5: Published Work (`#work`)

**Layout:** Audio players + case study cards
**Key selectors:**
- `#work` — Section container
- `.audio-player` — Custom audio player wrapper
- `.audio-player audio` — Native audio element
- `.case-study` — Case study card
- `.case-study img` — Case study screenshot

---

## Section 6: Technical Stack (`#stack`)

**Layout:** Two columns
**Key selectors:**
- `#stack` — Section container
- `.stack-grid` — Two-column grid
- `.stack-group` — Tool category group
- `.stack-item` — Individual tool
- `.stack-item.custom` — Custom-built tools (accent highlight)

---

## Section 7: Experience (`#experience`)

**Layout:** Vertical timeline
**Key selectors:**
- `#experience` — Section container
- `.timeline` — Timeline container
- `.timeline-item` — Individual entry
- `.timeline-dot` — Timeline dot
- `.timeline-content` — Entry content

---

## Section 8: Contact (`#contact`)

**Layout:** Centered CTA
**Key selectors:**
- `#contact` — Section container
- `.contact-headline` — Main heading
- `.contact-links` — Link buttons
- `.contact-link` — Individual link

---

## Page 2: Builds (`builds.html`)

**Layout:** Alternating zigzag sections
**Key selectors:**
- `.build-section` — Full-width build section
- `.build-section:nth-child(even)` — Reversed layout
- `.build-image` — Screenshot container (floats in)
- `.build-content` — Text content (floats in opposite)
- `.build-tag` — Category tag
- `.build-title` — Build name
- `.build-desc` — Description
- `.build-detail` — Expandable technical detail

**Customization:**
- Reverse order: toggle `.build-section.reverse` class
- Animation speed: modify `.reveal` transition values
- Image position: `.build-section.reverse` flips layout

---

## Animations

| Class | Effect | Duration |
|-------|--------|----------|
| `.reveal` | Fade up on scroll | 0.7s |
| `.reveal-delay-1` | Staggered reveal | +0.1s |
| `.reveal-delay-2` | Staggered reveal | +0.2s |
| `.reveal-delay-3` | Staggered reveal | +0.3s |
| `.float-in-left` | Slide from left | 0.8s |
| `.float-in-right` | Slide from right | 0.8s |

---

## Responsive Breakpoints

| Breakpoint | Layout Change |
|------------|---------------|
| `≤900px` | 2-column → 1-column, nav collapses |
| `≤500px` | Further simplification, stacked layout |

---

## Audio Player

Custom styled `<audio>` elements. To add new audio:
```html
<div class="audio-player">
  <span class="audio-title">Track Name</span>
  <audio controls src="AUDIOCLIPS/filename.mp3"></audio>
</div>
```

---

## Builds Page (builds.html)

### Page Header
- `.page-header` — Top section with title
- `.page-header h1` — Page title

### Build Sections
- `.build-section` — Full-width alternating section
- `.build-section:nth-child(even)` — Dark background variant
- `.build-section.reverse` — Flips image/content sides
- `.build-inner` — Grid container (2 columns)
- `.build-image` — Screenshot container with hover effect
- `.build-content` — Text content area
- `.build-tag` — Category tag (`.blue`, `.purple`, `.gold`, `.green`)
- `.build-num` — Section number (01–08)
- `.build-title` — Build name
- `.build-title .accent` — Blue accent text
- `.build-title .purple-text` — Purple accent text
- `.build-title .gold-text` — Gold accent text
- `.build-desc` — Description paragraph
- `.build-detail` — Technical detail box
- `.build-detail.purple-border` — Purple left border
- `.build-detail.gold-border` — Gold left border
- `.build-detail.green-border` — Green left border

### Customization
- Swap images: update `src` in `.build-image img`
- Change accent colors: modify `.build-tag` class
- Reverse layout: add/remove `.reverse` class on `.build-section`
- Animation direction: `.float-in-left` / `.float-in-right`

---

## Image Paths Reference

All images are relative to repo root:

**Personal photos:** `ihack app phtos/Shahnam Hossain Jilan [1-5].png`
**App screenshots:** `ihack app phtos/Main app - *.png`
**Ecosystem UI:** `ihack app phtos/iHack Audio Main Ecosystem UI.png`
**Audit results:** `ihack app phtos/*AUDIT RESULT.png`
**Audio editor:** `Buildig AI AUDIO EDITOR/*.png`
**Audio clips:** `AUDIOCLIPS/*.mp3`
**Logo:** `assets/images/ihack-logo.png`
