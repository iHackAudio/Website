# Portfolio Site Plan — Shahnam Hossain Jilan

## Design Philosophy

**"Proof over claims."** Every section either shows what you built or provides evidence it works. No fluff, no buzzwords — just substance presented beautifully.

**Aesthetic:** Dark, cinematic, refined. Think Apple product pages meet Bloomberg Terminal. Clean typography, generous whitespace, scroll-driven reveals. The site itself should feel like a product — polished, intentional, engineered.

---

## Site Structure

### Page 1 — Landing (Single-Page Portfolio)

**Section 1: Hero**
- Full viewport. Minimal.
- Name: SHAHNAM HOSSAIN JILAN
- Title: AI Audio Systems Architect
- One-liner: "I build systems that teach AI to understand, produce, and validate audio at broadcast quality."
- Subtle animated waveform or audio visualization as background element (CSS/canvas, no heavy libs)
- Scroll indicator

**Section 2: The Numbers (Impact Strip)**
- Horizontal bar, not a grid — punchy, scannable
- 8 Years Production · 20K+ Listening Hours · 900+ Upwork Hours (Top Rated) · #1 Apple Podcasts · 8 Modules Built · 5 AI Agents Orchestrated
- Numbers animate on scroll (count-up effect)

**Section 3: What I Built — iHack Audio Platform**
- Section header: "iHack Audio Platform v3.0.0"
- Subtext: "End-to-end AI audio production infrastructure. Not a wrapper. Not a chatbot."
- Visual grid of modules (cards with icons):
  1. Multi-Agent Swarm Orchestrator
  2. Audio Studio Pro — Semantic Editing Engine
  3. QuadCore — Parallel Narration Engine
  4. Quality — Verified, Not Theorized
  5. 3D Spatial Map Engine
  6. Contextual Scripting Automation
  7. Automated Studio — One-Click Pipeline
  8. Maya LoRA — Voice Lab & Acoustic Fingerprinting
- Each card: icon, name, 1-line description, expandable detail
- Screenshots from `ihack app phtos/` embedded as visual proof

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

### Page 2 — /platform (Deep Dive)

- Dedicated page for iHack Audio Platform v3.0.0
- Full module breakdown with screenshots
- Architecture diagram (if you provide one, or I can create an SVG)
- Technical detail for each module
- Links back to main portfolio

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

## Questions Before Building

1. Which personal photo is your favorite? (1-5) — I'll use it in the hero
2. Do you have a logo for iHack Audio? Or just the "iH·" monogram?
3. Want the platform deep-dive on the same page or a separate /platform page?
4. Any specific Apple Podcasts episodes to feature?
5. Before/after waveform — do you have one? (The xAI prep mentioned this)
