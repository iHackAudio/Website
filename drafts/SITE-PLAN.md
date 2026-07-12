# Portfolio Site Plan — Shahnam Hossain Jilan

## Design Philosophy

**"Proof over claims."** Every section either shows what you built or provides evidence it works. No fluff, no buzzwords — just substance presented beautifully.

**Aesthetic:** Dark, cinematic, refined. Think Apple product pages meet Bloomberg Terminal. Clean typography, generous whitespace, scroll-driven reveals. The site itself should feel like a product — polished, intentional, engineered.

---

## Site Structure

### Page 1 — Landing (index.html)

**Section 1: Hero + About Me**
- Full viewport. Name, title, one-liner.
- Below the fold: short "About Me" paragraph — who you are, what you do, your philosophy.
- Personal photo (best of 1-5) integrated into the layout.
- Subtle animated waveform or audio visualization as background element (CSS/canvas, no heavy libs)
- Scroll indicator

**Section 2: The Numbers (Impact Strip)**
- Horizontal bar, not a grid — punchy, scannable
- 8 Years Production · 20K+ Listening Hours · 900+ Upwork Hours (Top Rated) · #1 Apple Podcasts · 8 Modules Built · 5 AI Agents Orchestrated
- Numbers animate on scroll (count-up effect)

**Section 3: What I Built — Teaser + Link**
- Brief showcase: 2-3 featured builds with preview images
- CTA: "See the full platform" → links to `/builds` page
- Keeps the landing page focused and scannable

**Section 4: The Foundation — Built on $0**
- Split layout: left = narrative, right = obstacles grid
- "Built everything. Spent nothing."
- Obstacles overcome: No GPU, No cloud budget, No paid API tier
- Solutions: Kaggle notebooks tunneled live, free tier orchestration, rate limit architecture
- Closing line: "Give this system real compute — the ceiling disappears entirely."

**Section 5: Published Work & Proof**
- Featured: iHack Audio Podcast (Apple Podcasts embed or link)
- "Ranked #1 for 'AI AUDIO' — Zero marketing spend."
- Before/after waveform comparison (if you provide one)
- Case study cards: Audiobook production, Podcast automation, Voice system
- Screenshots from the app showing audit results, ecosystem UI

**Section 6: Technical Stack**
- Clean two-column layout
- Left: Audio tools (professional) — Auphonic, Adobe Audition, iZotope RX, Descript, etc.
- Right: AI/Infrastructure — Gemini, Gemma, Whisper, React/Express
- Custom-built tools highlighted differently (accent color)

**Section 7: Experience**
- Timeline style, not cards
- iHack Audio (2022–Present): Founder, key achievements
- Upwork (2017–Present): Top Rated, 900+ hours
- Keep it tight — bullets, not paragraphs

**Section 8: Contact**
- Clean, centered
- Email, LinkedIn, Apple Podcasts link
- "Let's talk." — simple CTA

**Footer**
- Minimal. Name, year, "Built by hand."

---

### Page 2 — /builds (What I Built — Deep Dive)

**Layout: Alternating Zigzag Sections**

Each build gets its own full-width section with:
- Floating animation on scroll (fade + slide in)
- Colored accent text for key phrases
- Alternating layout:
  ```
  ----------------------------------------------
  |  Image    |  Title + Description            |
  ----------------------------------------------
  |  Title + Description  |  Image              |
  ----------------------------------------------
  ```
- Each section has: purpose, what it does, how it works, screenshot

**Builds to feature:**
1. Jojo — Voice-Native Application Controller
2. Audiopook Production Engine
3. Podcast Automation
4. AI Audio Auditor — Contextual Audio Editing
5. Script Director (with Kinetic Notation)
6. QuadCore — Parallel Narration Engine
7. Maya LoRA — Voice Lab & Acoustic Fingerprinting
8. 3D Spatial Map Engine

Each build = its own zigzag section with purpose description + screenshot from `ihack app phtos/` or `Buildig AI AUDIO EDITOR/`

---

## Image Usage Plan

From `ihack app phtos/`:
- **Shahnam Hossain Jilan 1-5.png** → Hero or About section (pick best 1-2)
- **iHack Audio Main Ecosystem UI.png** → "What I Built" section hero image
- **Main app screenshots** → Platform deep-dive page
- **Audit result screenshots** → "Quality — Verified" section
- **Podcast automation screenshots** → Published Work section
- **Sound Design / Mini Mastering** → Platform page

From `Buildig AI AUDIO EDITOR/`:
- **Analysis UI, Cut selection, Example of perfect cut** → Platform page, semantic editing section
- **Error cases** → Show depth of understanding (optional, platform page)

---

## Inspiration References

Sites that match the vibe:

1. **linear.app** — Clean, dark, product-focused. Beautiful scroll animations. Typography hierarchy.
2. **stripe.com** — Refined dark sections, gradient accents, professional without being boring.
3. **brittanychiang.com** — Developer portfolio gold standard. Clean, fast, no BS.
4. **rauno.me** — Minimal, immersive, beautiful transitions.
5. **spline.com** — 3D elements done right (we won't use 3D, but the layout rhythm is perfect).
6. **brianlovin.com** — Content-first, beautiful typography, dark mode done right.

---

## Tech Stack

- **Single HTML file** (or minimal multi-page static)
- **CSS:** Custom properties, grid, flexbox, scroll-driven animations
- **JS:** Vanilla only — no frameworks, no dependencies
- **Fonts:** Inter (body) + Space Mono (accents) — already in your demo, they work
- **Deployment:** GitHub Pages (free, auto-deploy from repo)
- **Performance:** Sub-1s load time, no external JS libs

---

## Color Palette

Keeping your existing palette — it's strong:
- **Background:** `#030712` → `#0a0e1a` (deep navy-black)
- **Primary accent:** `#38bdf8` (sky blue)
- **Secondary:** `#7c3aed` (purple)
- **Gold:** `#fbbf24` (for highlights/achievements)
- **Text:** `#f8fafc` (bright) → `#94a3b8` (muted)

---

## Content Changes from CHANGES.txt

All applied:
- [x] 20K hours (updated from 10K)
- [x] Remove 52s / 10/10 / 9.8 specific metrics → ecosystem language
- [x] Remove $550-$850 PFH
- [x] "Built on Zero" → obstacles narrative
- [x] Platform v3.0.0 → dedicated section/page
- [x] "Forensic Audit" → "Quality — Verified, not theorized"
- [x] Professional/businessman tone throughout

---

## Decisions Made

- [x] Hero photo: #2 (Shahnam Hossain Jilan 2.png)
- [x] iHack Audio logo: uploaded (ihack-logo.png)
- [x] Builds page: Separate `/builds` page with zigzag layout
- [x] Apple Podcasts episodes: from Netlify site (see below)
- [x] Before/after waveform: N/A (not available)

## Podcast Episodes to Feature

From ihack-audio.netlify.app:
1. When AI Takes Over the Podcast (3:15)
2. My AI Host Got Upset (2:08)
3. My AI Wants to Be HUMAN (2:18)
4. Podcast Airways — Sky Skylar (4:14)

## Audiobook Samples
1. 3D Sound Design Sample (3:13)
2. Cinematic Pace Sample (3:38)
3. Cinematic Story & Sound (3:50)
