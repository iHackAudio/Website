from fpdf import FPDF

# Colors
SIDEBAR_BG = (44, 62, 80)       # Dark blue-gray
SIDEBAR_TEXT = (200, 210, 220)   # Light gray
WHITE = (255, 255, 255)
DARK = (30, 30, 30)
ACCENT = (52, 152, 219)         # Blue accent
MUTED = (120, 120, 120)
BORDER = (180, 200, 210)

class CV(FPDF):
    pass

pdf = CV()
pdf.set_auto_page_break(auto=False)
pdf.add_page()

# Load fonts
pdf.add_font('Sans', '', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf')
pdf.add_font('Sans', 'B', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf')
pdf.add_font('Sans', 'I', '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf')

SIDEBAR_W = 68
PAGE_W = 210
PAGE_H = 297
MARGIN = 10
CONTENT_X = SIDEBAR_W + 12
CONTENT_W = PAGE_W - CONTENT_X - MARGIN

# ─── SIDEBAR BACKGROUND ───
pdf.set_fill_color(*SIDEBAR_BG)
pdf.rect(0, 0, SIDEBAR_W, PAGE_H, 'F')

# ─── PROFILE PHOTO PLACEHOLDER ───
# Draw a circle placeholder
cx, cy = SIDEBAR_W / 2, 35
r = 22
pdf.set_fill_color(60, 80, 100)
pdf.ellipse(cx - r, cy - r, r * 2, r * 2, 'F')
# Try to add actual photo if it exists
try:
    pdf.image('/home/work/.openclaw/workspace/Website/assets/optimized/hero-photo.webp', cx - r, cy - r, r * 2, r * 2)
except:
    pass

# ─── NAME & TITLE (SIDEBAR) ───
y = cy + r + 8
pdf.set_font('Sans', 'B', 13)
pdf.set_text_color(*WHITE)
pdf.set_x(5)
pdf.cell(SIDEBAR_W - 10, 6, 'SHAHNAM', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_x(5)
pdf.cell(SIDEBAR_W - 10, 6, 'HOSSAIN JILAN', align='C', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('Sans', '', 7)
pdf.set_text_color(*SIDEBAR_TEXT)
pdf.set_x(5)
pdf.cell(SIDEBAR_W - 10, 5, 'AI Audio Systems Architect', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_x(5)
pdf.cell(SIDEBAR_W - 10, 5, 'Founder, iHack Audio', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)

# ─── CONTACT (SIDEBAR) ───
def sidebar_section(title):
    pdf.set_x(8)
    pdf.set_font('Sans', 'B', 8)
    pdf.set_text_color(*WHITE)
    pdf.cell(SIDEBAR_W - 16, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(100, 120, 140)
    pdf.line(8, pdf.get_y(), SIDEBAR_W - 8, pdf.get_y())
    pdf.ln(2)

def sidebar_item(text):
    pdf.set_x(10)
    pdf.set_font('Sans', '', 7)
    pdf.set_text_color(*SIDEBAR_TEXT)
    pdf.cell(SIDEBAR_W - 20, 4.5, text, new_x="LMARGIN", new_y="NEXT")

sidebar_section('Contact')
sidebar_item('iHackaudio@gmail.com')
sidebar_item('Dhaka, Bangladesh')
sidebar_item('ihackaudio.github.io/Website')
sidebar_item('g.dev/shahnamjilan')
pdf.ln(4)

# ─── SKILLS (SIDEBAR) ───
sidebar_section('Skills')

def skill_bar(name, level):
    pdf.set_x(10)
    pdf.set_font('Sans', '', 7)
    pdf.set_text_color(*SIDEBAR_TEXT)
    pdf.cell(30, 4, name, new_x="END")
    # Bar background
    bar_x = 42
    bar_w = SIDEBAR_W - bar_x - 10
    bar_h = 2.5
    bar_y = pdf.get_y() + 1
    pdf.set_fill_color(60, 80, 100)
    pdf.rect(bar_x, bar_y, bar_w, bar_h, 'F')
    # Bar fill
    pdf.set_fill_color(*ACCENT)
    pdf.rect(bar_x, bar_y, bar_w * level, bar_h, 'F')
    pdf.ln(5)

skill_bar('Audio Production', 0.95)
skill_bar('AI/ML Pipelines', 0.90)
skill_bar('Voice Systems', 0.92)
skill_bar('Sound Design', 0.88)
skill_bar('Mastering', 0.93)
skill_bar('Spatial Audio', 0.85)
pdf.ln(4)

# ─── LANGUAGES (SIDEBAR) ───
sidebar_section('Languages')

def lang_bar(name, level):
    pdf.set_x(10)
    pdf.set_font('Sans', '', 7)
    pdf.set_text_color(*SIDEBAR_TEXT)
    pdf.cell(30, 4, name, new_x="END")
    bar_x = 42
    bar_w = SIDEBAR_W - bar_x - 10
    bar_h = 2.5
    bar_y = pdf.get_y() + 1
    pdf.set_fill_color(60, 80, 100)
    pdf.rect(bar_x, bar_y, bar_w, bar_h, 'F')
    pdf.set_fill_color(*ACCENT)
    pdf.rect(bar_x, bar_y, bar_w * level, bar_h, 'F')
    pdf.ln(5)

lang_bar('English', 0.95)
lang_bar('Bengali', 1.0)
pdf.ln(4)

# ─── TOOLS (SIDEBAR) ───
sidebar_section('Tools')
tools = ['Adobe Audition', 'iZotope RX', 'Auphonic', 'Descript', 'Riverside', 'Audacity',
         'Gemini 2.5 Pro', 'Gemini Live API', 'Gemma', 'Groq/Whisper', 'React/Express']
for t in tools:
    sidebar_item(t)

# ═══════════════════════════════════════════
# RIGHT SIDE - CONTENT
# ═══════════════════════════════════════════

def content_section(title):
    pdf.set_xy(CONTENT_X, pdf.get_y())
    pdf.set_font('Sans', 'B', 11)
    pdf.set_text_color(*DARK)
    pdf.cell(CONTENT_W, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.5)
    pdf.line(CONTENT_X, pdf.get_y(), CONTENT_X + 40, pdf.get_y())
    pdf.set_line_width(0.2)
    pdf.ln(3)

def content_body(text):
    pdf.set_xy(CONTENT_X, pdf.get_y())
    pdf.set_font('Sans', '', 8)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(CONTENT_W, 4, text)

def content_bullet(text):
    pdf.set_xy(CONTENT_X, pdf.get_y())
    pdf.set_font('Sans', '', 7.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(CONTENT_W, 3.8, f'\u2022  {text}')

def job_header(role, company, period):
    pdf.set_xy(CONTENT_X, pdf.get_y())
    pdf.set_font('Sans', 'B', 9)
    pdf.set_text_color(*DARK)
    pdf.cell(CONTENT_W * 0.6, 5, role, new_x="END")
    pdf.set_font('Sans', 'I', 7)
    pdf.set_text_color(*MUTED)
    pdf.cell(CONTENT_W * 0.4, 5, period, align='R', new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(CONTENT_X, pdf.get_y())
    pdf.set_font('Sans', '', 8)
    pdf.set_text_color(*ACCENT)
    pdf.cell(CONTENT_W, 4, company, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

# ─── PROFILE ───
pdf.set_y(15)
content_section('Profile')
content_body(
    'Audio production professional with 8 years of experience and 10,000+ hours of critical '
    'listening. Built an end-to-end AI audio production platform from zero budget \u2014 multi-agent '
    'orchestration, semantic audio editing, forensic quality audit, 3D spatial mapping. Published '
    'output ranked as a top AI podcast on Apple Podcasts.'
)
pdf.ln(4)

# ─── EXPERIENCE ───
content_section('Experience')

job_header('Founder & Lead AI Audio Systems Architect', 'iHack Audio', '2022 - Present')
content_bullet('Built end-to-end AI audio production platform \u2014 8 modules, 5 orchestrated agents')
content_bullet('Designed kinetic notation system for vocal performance engineering')
content_bullet('Created 5-pass semantic audio editing engine with pre-execution QC')
content_bullet('Built 3D spatial audio mapping pipeline (A24/Dolby Atmos target)')
content_bullet('Published output ranked as top AI podcast \u2014 zero marketing spend')
pdf.ln(3)

job_header('Top Rated Audio Editor & Podcast Producer', 'Upwork', '2017 - Present')
content_bullet('900+ production hours logged. Top Rated status maintained.')
content_bullet('Podcast production, audiobook narration QC, sound design, professional mastering')
content_bullet('Multi-character dialogue production for international clients')
pdf.ln(4)

# ─── PLATFORM ───
content_section('iHack Audio Platform (v3.0.0)')
content_bullet('Multi-Agent Swarm: 5 orchestrated agents, voice-native control via Gemini Live API')
content_bullet('Audio Studio Pro: Semantic editing \u2014 Whisper \u2192 word-level timestamps \u2192 VAD \u2192 Gemma \u2192 5-pass validation')
content_bullet('QuadCore: 4 parallel chapter engines, up to 30 API keys distributed across pool')
content_bullet('Forensic Audit: Automated quality scoring \u2014 scripting, technical, vocal, marketability')
content_bullet('Maya LoRA Voice Lab: Acoustic fingerprinting \u2014 F0, RMS, 13 MFCCs, cosine similarity')
pdf.ln(4)

# ─── EDUCATION / BUILT ON ZERO ───
content_section('Built on Zero')
content_body(
    'Total infrastructure budget: $0. Every system built on free tier \u2014 Google AI Studio, '
    'Groq, OpenRouter, Kaggle free GPU. Rate limits, quota caps, connection drops \u2014 all '
    'solved in architecture. Output still scored Tier 1 Broadcast standard.'
)
pdf.ln(4)

# ─── PUBLISHED WORK ───
content_section('Published Work')
content_bullet('iHack Audio Podcast \u2014 Ranked as top AI podcast on Apple Podcasts')
content_bullet('Multi-character AI narration, cinematic sound design, broadcast-standard mastering')
content_bullet('Production time: 4-6 minutes per episode, publication-ready')

# Save
output = '/home/work/.openclaw/workspace/Website/Shahnam_Jilan_CV.pdf'
pdf.output(output)
print(f'PDF saved: {output}')
print(f'Pages: {pdf.pages_count}')
