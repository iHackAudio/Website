# Audio-Visual Integration Patterns for Web Portfolios

> Research compiled for the iHackAudio dual-identity portfolio site.
> Focus: interactive sound, audio-reactive visuals, and UX best practices.

---

## Table of Contents

1. [Technology Stack Overview](#1-technology-stack-overview)
2. [Web Audio API Fundamentals](#2-web-audio-api-fundamentals)
3. [Library Comparison: Howler.js vs Tone.js vs Raw Web Audio API](#3-library-comparison)
4. [Click / Scroll / Hover Sound Design](#4-click--scroll--hover-sound-design)
5. [Audio-Reactive Animations](#5-audio-reactive-animations)
6. [Page Transition Sound Effects (Whoosh / Paper Turn)](#6-page-transition-sound-effects)
7. [Ambient Sound Design per Side (Warm vs Cold)](#7-ambient-sound-design-per-side)
8. [Mute / Unmute Toggle UX](#8-mute--unmute-toggle-ux)
9. [Browser Autoplay Policy & Workarounds](#9-browser-autoplay-policy--workarounds)
10. [Best Practices: When to Use Sound, Volume Levels, Accessibility](#10-best-practices)
11. [Portfolio Sites with Audio: Case Studies & Patterns](#11-portfolio-sites-with-audio)
12. [GSAP + Audio Integration](#12-gsap--audio-integration)
13. [Recommended Architecture for iHackAudio](#13-recommended-architecture-for-ihackaudio)

---

## 1. Technology Stack Overview

| Technology | Purpose | Best For |
|---|---|---|
| **Web Audio API** (native) | Low-level audio processing, analysis, spatial audio | Custom effects, visualizations, fine-grained control |
| **Howler.js** (7KB gzipped) | Simplified audio playback across browsers | Sound effects, audio sprites, cross-browser reliability |
| **Tone.js** | DAW-like framework with synths, effects, scheduling | Musical/tonal sounds, generative audio, timing precision |
| **GSAP** | Animation timeline control | Syncing visual animations to audio events |
| **AnalyserNode** | Real-time frequency/waveform analysis | Audio-reactive visualizations |

### Recommendation for iHackAudio

**Use Howler.js for playback + native Web Audio API AnalyserNode for visualizations.**

- Howler.js handles cross-browser audio sprites (hover, click, page-flip sounds)
- Web Audio API's AnalyserNode provides real-time frequency data for reactive visuals
- Tone.js is overkill unless generating synthesized sounds on-the-fly
- GSAP handles all animation, with audio events triggering timeline actions

---

## 2. Web Audio API Fundamentals

### Core Architecture

The Web Audio API uses an **audio routing graph** model:

```
Source Node → Effect Nodes → Gain Node → Destination (speakers)
                  ↓
            Analyser Node → Canvas/WebGL visualization
```

### Key Nodes for This Project

| Node | Purpose | Use Case |
|---|---|---|
| `AudioContext` | Main audio processing context | Singleton, created on first user interaction |
| `GainNode` | Volume control | Master volume, per-sound volume, fade in/out |
| `AnalyserNode` | FFT analysis, waveform data | Audio-reactive visuals |
| `BiquadFilterNode` | EQ / filtering | Warm vs cold tonal shaping |
| `ConvolverNode` | Reverb / impulse response | Ambient space simulation |
| `StereoPannerNode` | Left/right panning | Spatial positioning of sounds |
| `AudioBufferSourceNode` | Play pre-loaded audio buffers | Short SFX (clicks, whooshes) |
| `MediaElementAudioSourceNode` | Stream from `<audio>` element | Long ambient loops |

### Basic Setup Pattern

```javascript
// Must be created/resumed after user gesture
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

// Create nodes
const masterGain = audioCtx.createGain();
const analyser = audioCtx.createAnalyser();
analyser.fftSize = 256; // Lower = faster, good for UI reactivity

// Connect chain
masterGain.connect(analyser);
analyser.connect(audioCtx.destination);

// Resume context (required by Chrome autoplay policy)
document.addEventListener('click', () => {
  if (audioCtx.state === 'suspended') audioCtx.resume();
}, { once: true });
```

### AnalyserNode for Visualizations

```javascript
const analyser = audioCtx.createAnalyser();
analyser.fftSize = 256;
const bufferLength = analyser.frequencyBinCount; // 128
const dataArray = new Uint8Array(bufferLength);

function visualize() {
  requestAnimationFrame(visualize);
  analyser.getByteFrequencyData(dataArray);
  // dataArray now has 0-255 values for each frequency bin
  // Use these to drive visual properties (scale, color, position)
}
```

---

## 3. Library Comparison

### Howler.js — Recommended for Sound Effects

**Pros:**
- Tiny (7KB gzipped), zero dependencies
- Automatic Web Audio → HTML5 Audio fallback
- Audio sprites for efficient loading
- Simple API: `new Howl({ src: ['sound.mp3'] }).play()`
- Auto-caching of loaded sounds
- Spatial audio support (stereo panning)
- Rate, fade, loop, seek controls

**Cons:**
- No built-in synthesis or effects processing
- No frequency analysis (need raw Web Audio API for that)

**Audio Sprites Pattern (ideal for hover/click sounds):**
```javascript
const uiSounds = new Howl({
  src: ['/audio/ui-sprites.mp3'],
  sprite: {
    hover:    [0, 200],      // 200ms hover sound
    click:    [300, 150],    // 150ms click sound
    flip:     [500, 800],    // 800ms page flip
    ambient:  [1500, 10000], // 10s ambient loop
  }
});

// Usage
element.addEventListener('mouseenter', () => uiSounds.play('hover'));
element.addEventListener('click', () => uiSounds.play('click'));
```

### Tone.js — For Synthesized / Musical Sounds

**Pros:**
- DAW-like architecture (transport, scheduling, synths)
- Built-in effects: reverb, delay, chorus, distortion, EQ
- Sample-accurate timing
- Musical time notation ("4n", "8t", "1m")

**Cons:**
- Larger bundle (~40KB+)
- More complex API
- Overkill for simple SFX playback

**Use Case:** If you want to **generate** the warm/cold ambient tones programmatically rather than pre-recording them.

```javascript
// Warm ambient tone (Human side)
const warmDrone = new Tone.Oscillator({
  frequency: 220,
  type: "sine",
  volume: -30
}).toDestination();

// Cold digital tone (Architect side) 
const coldDrone = new Tone.Oscillator({
  frequency: 440,
  type: "square",
  volume: -35
}).toDestination();

// Add filter for warmth
const warmFilter = new Tone.Filter(800, "lowpass").toDestination();
warmDrone.connect(warmFilter);
```

### Raw Web Audio API — For Visualizations

**Use when:** You need `AnalyserNode` data to drive canvas/WebGL visuals.

Howler.js exposes the underlying `AudioContext` via `Howler.ctx`, so you can tap into it:
```javascript
const analyser = Howler.ctx.createAnalyser();
Howler.masterGain.connect(analyser);
analyser.connect(Howler.ctx.destination);
```

---

## 4. Click / Scroll / Hover Sound Design

### Sound Categories & Timing

| Interaction | Sound Type | Duration | Volume | Notes |
|---|---|---|---|---|
| **Hover** (links, buttons) | Soft tick / subtle tone | 50-150ms | -24dB to -30dB | Should feel almost subliminal |
| **Click** (buttons, nav) | Satisfying click / tap | 100-200ms | -18dB to -24dB | Slightly louder than hover |
| **Scroll** | Soft whoosh / friction | 200-400ms | -24dB to -30dB | Throttled, not every pixel |
| **Page flip** | Paper whoosh | 600-1000ms | -12dB to -18dB | Main transition effect |
| **Ambient** | Continuous loop | 8-30s loop | -24dB to -36dB | Very quiet, atmospheric |

### Implementation Pattern

```javascript
class SoundManager {
  constructor() {
    this.enabled = true;
    this.masterVolume = 0.7;
    this.sounds = new Howl({
      src: ['/audio/ui-sprites.webm', '/audio/ui-sprites.mp3'],
      sprite: {
        hover:    [0, 120],
        click:    [200, 180],
        scroll:   [450, 300],
        flip:     [800, 900],
        ambientWarm:  [2000, 12000],
        ambientCold:  [15000, 12000],
      },
      volume: this.masterVolume,
    });
  }

  play(name) {
    if (!this.enabled) return;
    // Prevent sound stacking on rapid hover
    if (name === 'hover' && this._hoverThrottle) return;
    this._hoverThrottle = true;
    setTimeout(() => this._hoverThrottle = false, 80);
    this.sounds.play(name);
  }

  toggle() {
    this.enabled = !this.enabled;
    if (!this.enabled) this.sounds.fade(this.masterVolume, 0, 300);
    else this.sounds.fade(0, this.masterVolume, 300);
  }
}
```

### Scroll Sound Throttling

**Critical:** Do NOT play a sound on every scroll event. Use intersection observer or throttled scroll detection:

```javascript
// Play sound when a new section enters viewport
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      soundManager.play('scroll');
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.section').forEach(s => observer.observe(s));
```

### Hover Sound Throttling

```javascript
// Debounced hover — only plays if mouse stays on element for 100ms+
let hoverTimer;
document.querySelectorAll('[data-sound-hover]').forEach(el => {
  el.addEventListener('mouseenter', () => {
    hoverTimer = setTimeout(() => soundManager.play('hover'), 100);
  });
  el.addEventListener('mouseleave', () => clearTimeout(hoverTimer));
});
```

---

## 5. Audio-Reactive Animations

### Architecture

```
Audio Source → AnalyserNode → requestAnimationFrame loop → Visual Updates
```

### Frequency Band Extraction

Split the frequency data into meaningful bands for richer visual control:

```javascript
function getFrequencyBands(dataArray) {
  const bands = {
    bass: 0,     // 20-250 Hz   (indices ~0-5)
    lowMid: 0,   // 250-500 Hz  (indices ~5-12)
    mid: 0,      // 500-2kHz    (indices ~12-46)
    highMid: 0,  // 2k-4kHz     (indices ~46-93)
    high: 0,     // 4k-20kHz    (indices ~93-128)
  };

  const len = dataArray.length;
  const ranges = [
    ['bass', 0, Math.floor(len * 0.04)],
    ['lowMid', Math.floor(len * 0.04), Math.floor(len * 0.1)],
    ['mid', Math.floor(len * 0.1), Math.floor(len * 0.36)],
    ['highMid', Math.floor(len * 0.36), Math.floor(len * 0.72)],
    ['high', Math.floor(len * 0.72), len],
  ];

  for (const [name, start, end] of ranges) {
    let sum = 0;
    for (let i = start; i < end; i++) sum += dataArray[i];
    bands[name] = sum / (end - start) / 255; // Normalize 0-1
  }
  return bands;
}
```

### Driving CSS/JS Visuals from Audio Data

```javascript
function audioReactiveLoop() {
  requestAnimationFrame(audioReactiveLoop);
  analyser.getByteFrequencyData(dataArray);
  const bands = getFrequencyBands(dataArray);

  // Example: scale elements based on bass
  document.documentElement.style.setProperty('--bass', bands.bass);
  document.documentElement.style.setProperty('--mid', bands.mid);
  document.documentElement.style.setProperty('--high', bands.high);
}

// CSS usage:
// .glow-element { transform: scale(calc(1 + var(--bass) * 0.3)); }
// .wave-line { opacity: calc(0.3 + var(--mid) * 0.7); }
```

### Canvas Visualization Examples

**Waveform (oscilloscope):**
```javascript
function drawWaveform(canvas, analyser) {
  const ctx = canvas.getContext('2d');
  const dataArray = new Uint8Array(analyser.frequencyBinCount);
  
  function draw() {
    requestAnimationFrame(draw);
    analyser.getByteTimeDomainData(dataArray);
    
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#00ff88';
    ctx.beginPath();
    
    const sliceWidth = canvas.width / dataArray.length;
    let x = 0;
    
    for (let i = 0; i < dataArray.length; i++) {
      const v = dataArray[i] / 128.0;
      const y = (v * canvas.height) / 2;
      i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
      x += sliceWidth;
    }
    
    ctx.lineTo(canvas.width, canvas.height / 2);
    ctx.stroke();
  }
  draw();
}
```

**Frequency bars:**
```javascript
function drawBars(canvas, analyser) {
  const ctx = canvas.getContext('2d');
  const dataArray = new Uint8Array(analyser.frequencyBinCount);
  
  function draw() {
    requestAnimationFrame(draw);
    analyser.getByteFrequencyData(dataArray);
    
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    const barWidth = canvas.width / dataArray.length * 2.5;
    let x = 0;
    
    for (let i = 0; i < dataArray.length; i++) {
      const barHeight = (dataArray[i] / 255) * canvas.height;
      ctx.fillStyle = `hsl(${i * 2}, 80%, 50%)`;
      ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
      x += barWidth + 1;
    }
  }
  draw();
}
```

### GSAP + Audio-Reactive Integration

```javascript
// Use GSAP to smoothly interpolate audio-reactive values
const reactiveState = { scale: 1, hue: 0, glow: 0 };

function updateReactive() {
  requestAnimationFrame(updateReactive);
  analyser.getByteFrequencyData(dataArray);
  const bands = getFrequencyBands(dataArray);
  
  // GSAP smooths the values (prevents jittery visuals)
  gsap.to(reactiveState, {
    scale: 1 + bands.bass * 0.5,
    hue: bands.mid * 360,
    glow: bands.high * 20,
    duration: 0.1,
    ease: 'power2.out',
    onUpdate: () => {
      gsap.set('.reactive-element', {
        scale: reactiveState.scale,
        filter: `hue-rotate(${reactiveState.hue}deg) drop-shadow(0 0 ${reactiveState.glow}px currentColor)`,
      });
    }
  });
}
```

---

## 6. Page Transition Sound Effects

### Page Flip / Whoosh Sound

**Design characteristics:**
- Duration: 600-1000ms
- Frequency sweep: high-to-low (whoosh) or broadband noise burst
- Envelope: quick attack (10-50ms), sustained body, medium decay (200-400ms)
- Optional: subtle paper texture layer underneath

**Implementation with GSAP timeline:**

```javascript
function pageFlip(toSide) {
  const tl = gsap.timeline();
  
  // Play sound at animation start
  tl.call(() => soundManager.play('flip'), null, 0);
  
  // Visual flip animation
  tl.to('.page', {
    rotateY: toSide === 'architect' ? -180 : 0,
    duration: 0.8,
    ease: 'power2.inOut',
  }, 0);
  
  // Crossfade ambient sound
  tl.call(() => {
    if (toSide === 'architect') {
      soundManager.sounds.fade('ambientWarm', 0, 500);
      soundManager.sounds.play('ambientCold');
    } else {
      soundManager.sounds.fade('ambientCold', 0, 500);
      soundManager.sounds.play('ambientWarm');
    }
  }, null, 0.3);
  
  return tl;
}
```

### Alternative: Synthesized Flip Sound (Tone.js)

```javascript
function synthesizeFlip() {
  const noise = new Tone.Noise("pink").start();
  const env = new Tone.AmplitudeEnvelope({
    attack: 0.01,
    decay: 0.3,
    sustain: 0.1,
    release: 0.5,
  }).toDestination();
  
  const filter = new Tone.Filter({
    frequency: 2000,
    type: "bandpass",
    Q: 0.5,
  }).toDestination();
  
  const autoFilter = new Tone.AutoFilter("4n").toDestination().start();
  
  noise.connect(filter);
  filter.connect(env);
  env.connect(autoFilter);
  
  env.triggerAttackRelease("0.8");
  setTimeout(() => noise.stop(), 1000);
}
```

---

## 7. Ambient Sound Design per Side

### Warm Side (Human)

| Property | Value |
|---|---|
| **Character** | Organic, warm, analog |
| **Base frequency** | 220Hz (A3) — sub-bass drone |
| **Harmonics** | Even harmonics (sine-based) |
| **Filter** | Low-pass at 800Hz, gentle roll-off |
| **Effects** | Subtle reverb (large room), slight tape saturation |
| **Volume** | -30dB to -36dB (barely perceptible) |
| **Loop length** | 12-20 seconds (long enough to avoid obvious repetition) |

### Cold Side (Architect)

| Property | Value |
|---|---|
| **Character** | Digital, precise, crystalline |
| **Base frequency** | 440Hz (A4) — higher, more present |
| **Harmonics** | Odd harmonics (square/sawtooth-based, filtered) |
| **Filter** | High-pass at 200Hz, band-pass around 2kHz |
| **Effects** | Short reverb (digital/plate), subtle chorus, bit-crush hint |
| **Volume** | -30dB to -36dB |
| **Loop length** | 10-16 seconds |

### Implementation Strategy

**Option A: Pre-recorded audio files (recommended)**
- Record/produce ambient loops in a DAW
- Export as .webm (Opus) + .mp3 fallback
- ~50-100KB per 10-second loop
- More control over final sound quality

**Option B: Synthesized with Tone.js**
- Generate tones programmatically
- Smaller bundle, no audio file loading
- Less control over subtle texture
- Higher CPU usage

**Option C: Hybrid (best of both)**
- Pre-recorded ambient loops for the base layer
- Tone.js for interactive micro-sounds (hover, click tones)
- Web Audio API for real-time filtering and analysis

---

## 8. Mute / Unmute Toggle UX

### Design Requirements

- **Always visible** — fixed position, doesn't scroll away
- **Clear state indication** — icon changes (🔊 / 🔇), not just color
- **Accessible** — `aria-label`, keyboard focusable, screen reader friendly
- **Persists preference** — localStorage
- **Smooth transition** — fade in/out, not abrupt cut

### Implementation

```html
<button 
  id="sound-toggle" 
  class="fixed bottom-6 right-6 z-50 w-12 h-12 rounded-full 
         bg-white/10 backdrop-blur-sm border border-white/20 
         flex items-center justify-center transition-all duration-300
         hover:bg-white/20 hover:scale-110"
  aria-label="Toggle sound"
  aria-pressed="true"
>
  <svg class="sound-on-icon w-6 h-6" viewBox="0 0 24 24" fill="currentColor">
    <!-- speaker icon with sound waves -->
  </svg>
  <svg class="sound-off-icon w-6 h-6 hidden" viewBox="0 0 24 24" fill="currentColor">
    <!-- speaker icon with X -->
  </svg>
</button>
```

```javascript
class SoundToggle {
  constructor() {
    this.btn = document.getElementById('sound-toggle');
    this.enabled = localStorage.getItem('soundEnabled') !== 'false';
    this.updateUI();
    
    this.btn.addEventListener('click', () => this.toggle());
    this.btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.toggle();
      }
    });
  }
  
  toggle() {
    this.enabled = !this.enabled;
    localStorage.setItem('soundEnabled', this.enabled);
    
    if (this.enabled) {
      Howler.unmute(); // or custom fade-in
      gsap.to(Howler, { masterVolume: 0.7, duration: 0.5 });
    } else {
      gsap.to(Howler, { 
        masterVolume: 0, 
        duration: 0.5,
        onComplete: () => Howler.mute()
      });
    }
    
    this.updateUI();
  }
  
  updateUI() {
    this.btn.setAttribute('aria-pressed', this.enabled);
    this.btn.setAttribute('aria-label', this.enabled ? 'Mute sound' : 'Unmute sound');
    this.btn.querySelector('.sound-on-icon').classList.toggle('hidden', !this.enabled);
    this.btn.querySelector('.sound-off-icon').classList.toggle('hidden', this.enabled);
  }
}
```

### Visual Design Notes

- Position: bottom-right corner is conventional (bottom-left for LTR sites also works)
- Size: 44px minimum touch target (WCAG)
- Opacity: 60-80% default, 100% on hover
- Consider a subtle pulsing animation on first load to draw attention
- On mobile: ensure it doesn't overlap with important content

---

## 9. Browser Autoplay Policy & Workarounds

### The Problem

Since Chrome 66 (2018) and Chrome 71 for Web Audio API:
- **Autoplay with sound is blocked** until user interacts with the domain
- `AudioContext` starts in `suspended` state
- Must call `audioCtx.resume()` after user gesture (click, tap, keydown)

### What Works Without User Interaction

- ✅ Muted autoplay
- ✅ Preloading audio files
- ✅ Creating AudioContext (but it's suspended)
- ✅ Setting up audio graph / nodes

### What Requires User Interaction

- ❌ Playing any sound
- ❌ `AudioContext.resume()`
- ❌ `Howl.play()`

### Recommended Strategy for iHackAudio

```javascript
// 1. Create context and preload on page load
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

// 2. Show an "Enter" or "Enable Sound" prompt on first visit
//    This counts as user interaction and unlocks audio
async function initAudio() {
  if (audioCtx.state === 'suspended') {
    await audioCtx.resume();
  }
  // Now safe to play sounds
  soundManager.play('ambientWarm');
}

// 3. Gate the entire site behind a splash screen
//    "Click anywhere to enter" — this is both dramatic AND solves autoplay
document.getElementById('enter-btn').addEventListener('click', initAudio);
```

### Splash Screen Pattern

```
┌─────────────────────────────────────┐
│                                     │
│         iHackAudio                  │
│                                     │
│     Two Faces. One Sound.          │
│                                     │
│    [ Click to Enter · 🔊 ]         │
│                                     │
│   (audio unlocks on click)          │
└─────────────────────────────────────┘
```

This is **industry standard** for audio-heavy sites. It:
- Solves autoplay policy elegantly
- Sets expectations ("this site has sound")
- Creates a dramatic first impression
- Gives users an explicit opt-in

---

## 10. Best Practices

### When to Use Sound

| ✅ DO | ❌ DON'T |
|---|---|
| Subtle UI feedback (hover, click) | Loud, jarring notification sounds |
| Atmospheric ambient that reinforces theme | Random music that doesn't match content |
| Sound that demonstrates your expertise | Sound for the sake of having sound |
| Page transitions with purpose | Auto-playing videos with audio |
| Interactive elements that respond to audio | Sounds that repeat on a loop with no variation |

### Volume Levels (dB Reference)

| Element | dB Level | Perception |
|---|---|---|
| Master output | -6dB peak | Safe headroom |
| Ambient background | -24dB to -36dB | Subliminal, atmospheric |
| Hover sounds | -24dB to -30dB | Subtle, almost unconscious |
| Click/interaction sounds | -18dB to -24dB | Noticeable but not attention-grabbing |
| Page transition effects | -12dB to -18dB | Clear, intentional |
| Featured audio content | -6dB to -12dB | Prominent, focused listening |

### Golden Rules

1. **Default to OFF or very quiet** — let users opt IN to sound
2. **Always provide a mute toggle** — visible, accessible, persistent
3. **Respect `prefers-reduced-motion`** — also consider `prefers-reduced-audio` (not standard, but good practice)
4. **Never auto-play music** — ambient textures OK at low volume, full tracks NO
5. **Fade, don't cut** — smooth transitions (300-500ms fade) feel professional
6. **Throttle hover sounds** — minimum 80ms between plays
7. **Preload audio** — load during splash screen, not on first interaction
8. **Use audio sprites** — one HTTP request for all UI sounds
9. **Provide `.webm` (Opus) + `.mp3` fallback** — best compression + compatibility
10. **Test on mobile** — different autoplay rules, headphone vs speaker differences

### Accessibility Considerations

```css
@media (prefers-reduced-motion: reduce) {
  /* Disable audio-reactive animations */
  .reactive-element { animation: none !important; }
}

@media (prefers-reduced-motion: no-preference) {
  /* Full audio experience */
}
```

- Ensure all audio content has visual equivalents (don't convey info only through sound)
- Provide captions/transcripts for any spoken audio
- Make mute toggle keyboard-accessible
- Consider that some users may be on shared devices (libraries, offices)

---

## 11. Portfolio Sites with Audio: Case Studies & Patterns

### Common Patterns in Audio-Forward Portfolios

**1. Splash/Entry Screen**
- Nearly all professional audio portfolio sites use an entry screen
- "Enter with sound" / "Enter without sound" options
- Examples: recording studios, sound designers, music producers

**2. Ambient Soundscapes**
- Continuous low-volume atmospheric sound tied to page theme
- Changes subtly between sections/pages
- Acts as "sonic branding" — the site has a signature sound

**3. Interactive Sound Design**
- Every interactive element has a sonic counterpart
- Hover states create tonal variations
- Scrolling triggers textural sounds
- Creates a feeling of "playing" the website

**4. Audio Player Integration**
- Portfolio work embedded as playable audio
- Waveform visualizations for tracks
- Custom players that match site aesthetic

**5. Visual-Audio Synchronization**
- Beat-synced animations
- Frequency-reactive backgrounds
- Waveform as decorative element

### Notable Approaches

- **Recording studio sites**: Clean, minimal, with a "play reel" button front and center
- **Sound designer portfolios**: Often the most creative with web audio — turning the site itself into an instrument
- **Music producer sites**: Heavy use of embedded players, less ambient sound design
- **Audio engineer sites**: Balance between demonstrating technical skill and not overwhelming visitors

### Key Takeaway for iHackAudio

The site itself is the portfolio piece. The sound design IS the work sample. Every audio choice should communicate:
- Technical precision (clean implementation, no glitches)
- Artistic taste (appropriate levels, tasteful effects)
- Professional understanding (respect for UX, accessibility)

---

## 12. GSAP + Audio Integration

### Why GSAP for Audio-Visual Sync

GSAP excels at:
- Timeline-based sequencing (play sound at exact animation frame)
- Smooth value interpolation (prevent audio-reactive jitter)
- ScrollTrigger integration (sound on scroll milestones)
- Flip animations (page turn effects)

### Pattern: Audio Events in GSAP Timeline

```javascript
const tl = gsap.timeline({ paused: true });

// Visual animation
tl.to('.page-content', { 
  opacity: 0, 
  x: -100, 
  duration: 0.4,
  ease: 'power2.in'
}, 0);

// Play sound at specific point
tl.call(() => soundManager.play('flip'), null, 0.1);

// New page enters
tl.fromTo('.page-new', 
  { opacity: 0, x: 100 },
  { opacity: 1, x: 0, duration: 0.4, ease: 'power2.out' },
  0.4
);

// Crossfade ambient
tl.call(() => crossfadeAmbient('cold'), null, 0.3);
```

### Pattern: ScrollTrigger + Sound

```javascript
gsap.utils.toArray('.section').forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    start: 'top center',
    onEnter: () => {
      if (i % 2 === 0) soundManager.play('scroll');
      // Play sound on every other section to avoid fatigue
    },
    onEnterBack: () => soundManager.play('scroll'),
  });
});
```

### Pattern: Flip Animation (Two-Face Concept)

```javascript
function flipToFace(side) {
  const tl = gsap.timeline();
  
  // Sound: whoosh starts
  tl.call(() => soundManager.play('flip'), null, 0);
  
  // Visual: 3D flip
  tl.to('.card', {
    rotateY: side === 'architect' ? 180 : 0,
    duration: 0.8,
    ease: 'power3.inOut',
  }, 0);
  
  // Midpoint: swap content visibility
  tl.set('.human-content', { display: side === 'architect' ? 'none' : 'block' }, 0.4);
  tl.set('.architect-content', { display: side === 'architect' ? 'block' : 'none' }, 0.4);
  
  // Sound: ambient crossfade
  tl.call(() => {
    soundManager.sounds.fade(
      side === 'architect' ? 'ambientWarm' : 'ambientCold',
      0, 600
    );
    soundManager.play(side === 'architect' ? 'ambientCold' : 'ambientWarm');
  }, null, 0.3);
  
  // Visual: background color/gradient shift
  tl.to('body', {
    backgroundImage: side === 'architect' 
      ? 'linear-gradient(135deg, #0a0a1a, #1a1a3e)'
      : 'linear-gradient(135deg, #1a0a00, #3e1a0a)',
    duration: 0.6,
  }, 0.2);
  
  return tl;
}
```

---

## 13. Recommended Architecture for iHackAudio

### System Diagram

```
┌─────────────────────────────────────────────────────┐
│                    SoundManager                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ Howler.js│  │  Master   │  │   Toggle State   │  │
│  │  Sprites │  │  GainNode │  │  (localStorage)  │  │
│  └────┬─────┘  └────┬─────┘  └────────┬─────────┘  │
│       │              │                  │            │
│       └──────────────┼──────────────────┘            │
│                      │                               │
│              ┌───────▼────────┐                      │
│              │  AnalyserNode  │                      │
│              └───────┬────────┘                      │
│                      │                               │
└──────────────────────┼───────────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
    ┌────▼────┐  ┌─────▼─────┐  ┌───▼───┐
    │ Canvas  │  │ CSS Vars  │  │ GSAP  │
    │ Waveform│  │ --bass    │  │ TL    │
    └─────────┘  │ --mid     │  │ sync  │
                 │ --high    │  └───────┘
                 └───────────┘
```

### File Structure

```
audio/
├── sprites/
│   ├── ui-sprites.webm      # All UI sounds (hover, click, scroll, flip)
│   └── ui-sprites.mp3       # Fallback
├── ambient/
│   ├── warm-ambient.webm    # Human side atmosphere
│   ├── warm-ambient.mp3
│   ├── cold-ambient.webm    # Architect side atmosphere
│   └── cold-ambient.mp3
└── README.md                # Sound design notes

js/
├── audio/
│   ├── SoundManager.js      # Core audio controller
│   ├── AudioVisualizer.js   # AnalyserNode → canvas/CSS
│   ├── AmbientEngine.js     # Ambient crossfade logic
│   └── SoundToggle.js       # Mute/unmute UI
├── animations/
│   ├── PageFlip.js          # GSAP flip + sound sync
│   └── ScrollSounds.js      # ScrollTrigger + sound
└── main.js                  # Entry point, init
```

### Initialization Flow

```
1. Page loads
2. Show splash screen ("Click to Enter · 🔊")
3. User clicks → unlock AudioContext
4. Initialize SoundManager (preload sprites + ambient)
5. Initialize AudioVisualizer (connect AnalyserNode)
6. Initialize GSAP timelines with sound callbacks
7. Start ambient loop for current side
8. Fade in from splash → main content
```

### Audio Sprite Design

All UI sounds in a single sprite file:
```
[0ms    - 120ms]   → hover tick
[200ms  - 380ms]   → click tap
[450ms  - 750ms]   → scroll whoosh
[800ms  - 1700ms]  → page flip whoosh
[2000ms - 14000ms] → warm ambient loop
[15000ms- 27000ms] → cold ambient loop
```

Total: ~27 seconds, ~100-200KB in WebM/Opus.

---

## Summary of Key Decisions

| Decision | Recommendation |
|---|---|
| Audio library | **Howler.js** (playback) + **Web Audio API** (analysis) |
| Animation library | **GSAP** with ScrollTrigger |
| Sound loading | **Audio sprites** for UI, separate files for ambient |
| Audio formats | `.webm` (Opus) primary, `.mp3` fallback |
| Entry pattern | **Splash screen** with "Click to Enter" (solves autoplay) |
| Mute toggle | **Fixed bottom-right**, always visible, persists to localStorage |
| Ambient approach | **Pre-recorded loops**, crossfaded on side switch |
| Volume philosophy | **Quiet by default**, -24dB to -36dB for ambient, user can adjust |
| Audio-reactive | **AnalyserNode → CSS custom properties** for lightweight reactivity |
| Page flip sound | **GSAP timeline** with sound call at t=0.1s |
| Two-face audio | **Warm (analog, low-pass)** vs **Cold (digital, high-pass)** |

---

## References

- [MDN: Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- [MDN: Using Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [MDN: Visualizations with Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API)
- [MDN: AnalyserNode](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode)
- [Howler.js](https://howlerjs.com/)
- [Tone.js](https://tonejs.github.io/)
- [Chrome Autoplay Policy](https://developer.chrome.com/blog/autoplay)
- [GSAP Documentation](https://gsap.com/docs/)
