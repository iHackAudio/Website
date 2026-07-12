# CSS MAP — Portfolio Customization Reference

> Last updated: All sections final

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
| `--glow-accent` | `0 0 20px rgba(56,189,248,0.3), 0 0 60px rgba(56,189,248,0.1)` | Blue glow |
| `--glow-purple` | `0 0 20px rgba(124,58,237,0.3), 0 0 60px rgba(124,58,237,0.1)` | Purple glow |
| `--glow-gold` | `0 0 20px rgba(251,191,36,0.3), 0 0 60px rgba(251,191,36,0.1)` | Gold glow |
| `--glow-green` | `0 0 20px rgba(74,222,128,0.3), 0 0 60px rgba(74,222,128,0.1)` | Green glow |

---

## Section Index

| # | Section | ID | File | Description |
|---|---------|-----|------|-------------|
| 1 | Hero + About Me | `#hero` | index.html | Name, title, about, photo |
| 2 | Stats Strip | `#numbers` | index.html | Horizontal impact strip |
| 3 | Builds Teaser | `#builds-teaser` | index.html | 4 cards → CTA to builds.html |
| 4 | Foundation | `#foundation` | index.html | "Built everything. Spent nothing." |
| 5 | Published Work | `#work` | index.html | Audio players + Apple Podcasts |
| 6 | Technical Stack | `#stack` | index.html | Horizontal chip boxes |
| 7 | Experience | `#experience` | index.html | Timeline |
| 8 | Contact | `#contact` | index.html | CTA + links |
| 9 | Builds Deep Dive | builds.html | builds.html | Zigzag alternating layout |

---

## Section 1: Hero + About Me (`#hero`)

- `.hero-name` — Name heading (Space Mono, clamp 32-64px)
- `.hero-role` — Title line (accent color, uppercase)
- `.hero-statement` — One-liner
- `.hero-about` — About paragraph
- `.hero-photo img` — Profile photo (4:5 aspect, grayscale → color on hover, gold glow)
- `.hero-badges` / `.badge` — Status badges

## Section 2: Stats Strip (`#numbers`)

- 5 items in a grid
- `.number-val` — Blue accent, clamp 16-20px, count-up animation
- `.number-lbl` — Gold color, clamp 8-10px, uppercase
- Items: 8 Years, 10,000+ Hours, 3000+ Episodes, 50+ Audiobooks, AI AUDIO Production & Automation
- Hover: blue glow on values

## Section 3: Builds Teaser (`#builds-teaser`)

- 4 cards in a grid
- `.teaser-card` — Gold glow on hover
- `.teaser-card-tag` — Color-coded: purple (Platform), green (Automation), gold (Contextual Agentic), blue (Quality)
- Cards link to builds.html
- CTA button: "Explore the Platform"

## Section 4: Foundation (`#foundation`)

- `.foundation-headline` — "Built everything. Spent nothing." (gold span)
- `.foundation-body` — Narrative paragraph
- `.foundation-tags` / `.f-tag` — Horizontal tag words (gold glow on hover)
- Tags: No GPU owned, No cloud budget, No paid API tier, No team, No marketing spend, Solo founder, Free tier only

## Section 5: Published Work (`#work`)

- 3-column grid of audio players
- `.audio-track` — Vertical card layout
- `.audio-icon` — Circle play button (gold glow, play/pause toggle)
- `.audio-name` — Track name (gold on hover)
- `.audio-meta` — Duration info
- `.apple-badge` — Centered Apple Podcasts link (gold glow on hover)
- All audio files in `AUDIOCLIPS/` folder

## Section 6: Technical Stack (`#stack`)

- 2-column grid
- `.stack-group-title` — White text (Inter, 12px, uppercase, weight 600)
- `.stack-chips` / `.stack-chip` — Horizontal chip boxes (gold glow on hover)
- `.stack-chip.custom` — Purple text for custom-built tools (gold glow on hover)

## Section 7: Experience (`#experience`)

- Timeline layout
- `.timeline-dot` — Gold glow on hover
- `.timeline-content` — Card with gradient top border
- `.timeline-content.alt` — Purple gradient variant

## Section 8: Contact (`#contact`)

- Centered CTA
- `.contact-link.primary` — Blue background button
- Other links: Apple Podcasts, iHack Audio, Google Developer

---

## Page 2: Builds (`builds.html`)

### Build Order
1. iHack Audio — The Ecosystem (purple tag)
2. Podcast Automation (green tag)
3. AI Audio Auditor (green tag, "IN DEVELOPMENT", sub-images)
4. Script Director + Jojo (gold tag, sub-images)
5. 3D Spatial Map Engine (blue tag)
6. Forensic Audit Lab (gold tag, studio main image, sub-images)

### Layout
- Alternating zigzag: image left/content right, then reversed
- `.build-image img` — 16:9 aspect ratio
- `.build-image-group` — 2 half-size sub-images under main
- `.build-tag` — Color-coded category tags
- Floating scroll animations (`.float-in-left`, `.float-in-right`)

---

## Animations

| Class | Effect |
|-------|--------|
| `.reveal` | Fade up on scroll |
| `.reveal-delay-1/2/3` | Staggered reveal |
| `.float-in-left` | Slide from left |
| `.float-in-right` | Slide from right |
| `@keyframes pulse` | Green dot pulse |
| `@keyframes glow-pulse` | Gold glow pulse (playing audio) |

## Image Paths

All relative to repo root:

| Type | Path |
|------|------|
| Hero photo | `assets/optimized/hero-photo.webp` |
| Logo | `assets/optimized/logo.webp` |
| Ecosystem | `assets/optimized/ecosystem.webp` |
| Podcast Automation | `assets/optimized/contextual-scripting.webp` |
| Script Director | `assets/optimized/script-director.webp` |
| Spatial Map | `assets/optimized/spatial-map.webp` |
| Audit Result | `assets/optimized/audit-result.webp` |
| Audit Cinematic | `assets/optimized/audit-cinematic.webp` |
| Editor Analysis | `assets/optimized/editor-analysis.webp` |
| Editor Cuts | `assets/optimized/editor-cuts.webp` |
| Editor Perfect | `assets/optimized/editor-perfect.webp` |
| Audio Analyzer | `assets/optimized/audio-analyzer.webp` |
| Sub-images | `assets/optimized/sub-*.webp` |

## Audio Files

| File | Used As |
|------|---------|
| `PODCAST_AIRWAYS_SKY SKYLAR.mp3` | Podcast track 1 & 3 |
| `CINEMATIC STORY & SOUND_SAMPLE.mp3` | Podcast track 2 |
| `Audiobook  Blink and Gone_SAMPLE.mp3` | Audiobook track 1 |
| `Audiobook 3D Sound design_SAMPLE.mp3` | Audiobook track 2 |
| `Audiobook Cinematic Pace_SAMPLE.mp3` | Audiobook track 3 |

## Responsive Breakpoints

| Breakpoint | Changes |
|------------|---------|
| `≤900px` | Nav collapses, 2-col grids, stacked layout |
| `≤500px` | Single column, smaller stats |
