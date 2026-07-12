from fpdf import FPDF

class CV(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('DejaVu', 'I', 7)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, 'Shahnam Hossain Jilan', align='C')

    def section_title(self, title):
        self.set_font('DejaVu', 'B', 10)
        self.set_text_color(56, 189, 248)
        self.cell(0, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(56, 189, 248)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def body_text(self, text, bold=False):
        self.set_font('DejaVu', 'B' if bold else '', 8.5)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 4.2, text)

    def bullet(self, text):
        self.set_font('DejaVu', '', 8)
        self.set_text_color(50, 50, 50)
        self.set_x(self.l_margin)
        self.multi_cell(0, 4.2, f'\u2022  {text}')

    def job_header(self, role, company, period):
        self.set_font('DejaVu', 'B', 9)
        self.set_text_color(30, 30, 30)
        self.cell(0, 5, role, new_x="LMARGIN", new_y="NEXT")
        self.set_font('DejaVu', '', 8)
        self.set_text_color(80, 80, 80)
        self.cell(0, 4, f'{company}  |  {period}', new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

pdf = CV()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_margins(18, 15, 18)

pdf.add_font('DejaVu', '', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf')
pdf.add_font('DejaVu', 'B', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf')
pdf.add_font('DejaVu', 'I', '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf')

# HEADER
pdf.set_font('DejaVu', 'B', 18)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 9, 'SHAHNAM HOSSAIN JILAN', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('DejaVu', '', 10)
pdf.set_text_color(56, 189, 248)
pdf.cell(0, 5, 'AI Audio Systems Architect  |  Founder, iHack Audio', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('DejaVu', '', 7.5)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 4, 'Dhaka, Bangladesh (Remote)  |  iHackaudio@gmail.com  |  ihackaudio.github.io/Website  |  g.dev/shahnamjilan', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)

# SUMMARY
pdf.section_title('Summary')
pdf.body_text(
    'Audio production professional with 8 years of experience and 10,000+ hours of critical listening. '
    'Built an end-to-end AI audio production platform from zero budget \u2014 multi-agent orchestration, '
    'semantic audio editing, forensic quality audit, 3D spatial mapping. Published output ranked as a '
    'top AI podcast on Apple Podcasts. Deep understanding of both audio production and the AI systems '
    'that produce audio.'
)
pdf.ln(2)

# CORE EXPERTISE
pdf.section_title('Core Expertise')
cols = [
    ['Audio production (8 years)', 'AI-native pipeline design'],
    ['Vocal performance analysis', 'Waveform & spectral analysis'],
    ['Semantic audio validation', 'Voice acoustic fingerprinting'],
    ['Broadcast-standard mastering', 'Multi-agent orchestration'],
]
for row in cols:
    for i, item in enumerate(row):
        x = pdf.l_margin + i * 88
        pdf.set_xy(x, pdf.get_y())
        pdf.set_font('DejaVu', '', 8)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(88, 4.2, f'\u2022  {item}')
    pdf.ln(4.2)
pdf.ln(2)

# EXPERIENCE
pdf.section_title('Professional Experience')

pdf.job_header('Founder & Lead AI Audio Systems Architect', 'iHack Audio', '2022 \u2013 Present')
pdf.bullet('Built end-to-end AI audio production platform \u2014 8 modules, 5 orchestrated agents')
pdf.bullet('Designed kinetic notation system for vocal performance engineering [Archetype, Intensity, Stage]')
pdf.bullet('Created 5-pass semantic audio editing engine with pre-execution QC (industry first)')
pdf.bullet('Built 3D spatial audio mapping pipeline targeting A24/Dolby Atmos standard')
pdf.bullet('Published output ranked as top AI podcast \u2014 zero marketing spend')
pdf.ln(2)

pdf.job_header('Top Rated Audio Editor & Podcast Producer', 'Upwork', '2017 \u2013 Present')
pdf.bullet('900+ production hours logged. Top Rated status maintained.')
pdf.bullet('Podcast production, audiobook narration QC, sound design, professional mastering')
pdf.bullet('Multi-character dialogue production for international clients')
pdf.ln(2)

# PLATFORM
pdf.section_title('iHack Audio Platform (v3.0.0)')
pdf.bullet('Multi-Agent Swarm: 5 orchestrated agents (Jarvis, Aura + workers), voice-native control')
pdf.bullet('Audio Studio Pro: Semantic editing \u2014 Whisper \u2192 word-level timestamps \u2192 VAD \u2192 Gemma analysis \u2192 5-pass validation')
pdf.bullet('QuadCore: 4 parallel chapter engines, up to 30 API keys distributed across pool')
pdf.bullet('Forensic Audit System: Automated quality scoring \u2014 scripting, technical, vocal, marketability')
pdf.bullet('3D Spatial Map Engine: Line-by-line spatial audio design with stereo field coordinates')
pdf.bullet('Maya LoRA Voice Lab: Acoustic fingerprinting \u2014 F0, RMS, 13 MFCCs, cosine similarity scoring')
pdf.bullet('Jojo: Voice-native controller \u2014 entire app operable by speech via Gemini Live API')
pdf.ln(2)

# BUILT ON ZERO
pdf.section_title('Built on Zero')
pdf.body_text(
    'Total infrastructure budget: $0. Every system built on free tier \u2014 Google AI Studio, Groq, '
    'OpenRouter, Kaggle free GPU. Semantic editing engine runs on Kaggle notebook with live tunnel. '
    'Rate limits, quota caps, connection drops \u2014 all solved in architecture. Output still scored '
    'Tier 1 Broadcast standard.'
)
pdf.ln(2)

# TECHNICAL STACK
pdf.section_title('Technical Stack')
pdf.set_font('DejaVu', '', 8)
pdf.set_text_color(50, 50, 50)
pdf.multi_cell(0, 4.2,
    'Audio: Adobe Audition, iZotope RX, Auphonic, Descript, Riverside, Audacity\n'
    'AI: Gemini 2.5 Pro/Flash, Gemini Live API, Gemma, Groq, Whisper, OpenRouter\n'
    'Custom: iHack Audio Studio Pro, iHack Mastering App, Maya LoRA Voice Lab, Multi-Agent Swarm\n'
    'Principles: RMS/LUFS standards, VAD segmentation, spatial audio, kinetic notation, spectral analysis'
)
pdf.ln(2)

# PUBLISHED WORK
pdf.section_title('Published Work')
pdf.bullet('iHack Audio Podcast \u2014 Ranked as top AI podcast on Apple Podcasts')
pdf.bullet('Multi-character AI narration, cinematic sound design, broadcast-standard mastering')
pdf.bullet('Production time: 4-6 minutes per episode, publication-ready')

output_path = '/home/work/.openclaw/workspace/Website/Shahnam_Jilan_CV.pdf'
pdf.output(output_path)
print(f'PDF saved: {output_path}')
print(f'Pages: {pdf.pages_count}')
