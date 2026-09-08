#!/usr/bin/env python3
"""Speaker one-pager PDF for Ines Said — lavender brand, letter size."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

LAV = HexColor('#8a63d2'); LAV_DEEP = HexColor('#6a44b8'); TINT = HexColor('#f1ebfb')
BLUSH = HexColor('#fdeff5'); PINK = HexColor('#d1518f'); INK = HexColor('#31264a')
BODY = HexColor('#4c4160'); MUTED = HexColor('#907fa8'); GOLD = HexColor('#b8923f')

W, H = letter
c = canvas.Canvas('web/ines-said-speaker.pdf', pagesize=letter)
c.setTitle('Ines Said — Speaker One-Pager')
c.setAuthor('Ines Said')

LEFT = 218  # left column width

# ---- left column ----
c.setFillColor(TINT); c.rect(0, 0, LEFT, H, fill=1, stroke=0)
c.setFillColor(LAV); c.rect(0, H-8, W, 8, fill=1, stroke=0)

# portrait
img = ImageReader('web/portrait.jpg')
iw, ih = img.getSize()
pw = LEFT - 56; ph = pw * ih / iw
c.drawImage(img, 28, H - 44 - ph, pw, ph, mask='auto')

def label(x, y, text):
    c.setFont('Helvetica-Bold', 8.2); c.setFillColor(PINK)
    c.drawString(x, y, text.upper())
    return y - 15

y = H - 44 - ph - 30
y = label(28, y, '✦  Contact')
c.setFont('Helvetica-Bold', 10.5); c.setFillColor(INK)
c.drawString(28, y, 'ines@tanitxr.org'); y -= 14
c.setFont('Helvetica', 9.5); c.setFillColor(BODY)
c.drawString(28, y, 'www.inessaid.com'); y -= 13
c.drawString(28, y, 'linkedin.com/in/inessaid'); y -= 13
c.drawString(28, y, 'Washington, D.C. area & Tunisia'); y -= 30

y = label(28, y, '✦  Languages')
c.setFont('Helvetica', 9.5); c.setFillColor(BODY)
c.drawString(28, y, 'English  ·  Arabic  ·  French'); y -= 30

y = label(28, y, '✦  By the numbers')
stats = [
    ('600,000+', 'visitors to the Smithsonian FUTURES\nexhibition featuring her installation'),
    ('11,000+', 'people reached in 2025\nacross 40+ events'),
    ('30 Under 30', 'EE 30 Under 30, Class of 2025 (NAAEE)'),
    ('Auggie Finalist', 'Best Societal Impact, AWE 2026'),
]
for big, small in stats:
    c.setFont('Helvetica-Bold', 13); c.setFillColor(LAV_DEEP)
    c.drawString(28, y, big); y -= 13
    c.setFont('Helvetica', 8.4); c.setFillColor(BODY)
    for ln in small.split('\n'):
        c.drawString(28, y, ln); y -= 10.5
    y -= 8

# ---- right column ----
x = LEFT + 30; right_w = W - x - 36
y = H - 64
c.setFont('Helvetica-Bold', 30); c.setFillColor(INK)
c.drawString(x, y, 'Ines Said'); y -= 20
c.setFont('Helvetica-Bold', 11.5); c.setFillColor(LAV_DEEP)
c.drawString(x, y, 'XR Immersive Artist & Technologist  ·  Speaker'); y -= 26

c.setFont('Helvetica', 9.8); c.setFillColor(BODY)
intro = ('Tunisian immersive artist and XR technologist. Founder of Tanit XR — '
         "Tunisia's first open-source archive of endangered artifacts — and Lead XR "
         'Developer at Froliq. Her installations on heritage and climate have been '
         'exhibited internationally, including at the Smithsonian and MIT, with research '
         'published in ACM and IEEE (Best Paper Award). She has presented everywhere '
         'from the Energy Thought Summit main stage to the inside of a Roman colosseum.')
import textwrap
for ln in textwrap.wrap(intro, 74):
    c.drawString(x, y, ln); y -= 13
y -= 12

def section(y, title):
    c.setFont('Helvetica-Bold', 12.5); c.setFillColor(INK)
    c.drawString(x, y, title)
    c.setStrokeColor(LAV); c.setLineWidth(2)
    c.line(x, y - 5, x + 30, y - 5)
    return y - 22

y = section(y, 'Speaking topics')
topics = ['XR for cultural heritage — from 3,000-year-old mosaics to Gaussian splats',
          'Climate & sustainability through immersive technology',
          'From scans to XR: practical photogrammetry pipelines',
          'AR for public health · Women in XR · STEM education through games']
c.setFont('Helvetica', 9.8)
for t in topics:
    c.setFillColor(GOLD); c.drawString(x, y, '✦')
    c.setFillColor(BODY); c.drawString(x + 14, y, t); y -= 15
y -= 12

y = section(y, 'Selected stages')
stages = ['Augmented World Expo (AWE) USA — speaker, 2022 & 2026',
          'Energy Thought Summit (ETS26) — main stage, San Antonio',
          'El Jem International Conference — inside the Roman amphitheater, Tunisia',
          'Games for Change · Global XR Conference · Inloco Gallery MetaTalks',
          'Smithsonian FUTURES (installation) · MIT Reality Hack · Parsons']
c.setFont('Helvetica', 9.8)
for s in stages:
    c.setFillColor(LAV); c.drawString(x, y, '✦')
    c.setFillColor(BODY); c.drawString(x + 14, y, s); y -= 15
y -= 12

y = section(y, 'Formats & rates')
c.setFillColor(BLUSH)
c.roundRect(x - 6, y - 96, right_w + 6, 104, 10, fill=1, stroke=0)
rates = [('Keynote / featured talk', 'from $2,000'),
         ('Half-day workshop (photogrammetry, XR)', 'from $2,500'),
         ('Panel or university guest lecture', 'from $750'),
         ('Virtual talk', 'from $500')]
ry = y - 6
for name, price in rates:
    c.setFont('Helvetica', 9.8); c.setFillColor(BODY); c.drawString(x + 6, ry, name)
    c.setFont('Helvetica-Bold', 9.8); c.setFillColor(PINK)
    c.drawRightString(x + right_w - 12, ry, price)
    ry -= 16
c.setFont('Helvetica-Oblique', 8.4); c.setFillColor(MUTED)
c.drawString(x + 6, ry - 2, 'Community, nonprofit, and student rates available — just ask.')
y = ry - 30

# ETS stage photo strip
img2 = ImageReader('web/ets-stage.jpg')
iw2, ih2 = img2.getSize()
ph2 = 118; pw2 = ph2 * iw2 / ih2
img3 = ImageReader('web/el-jem.jpg')
iw3, ih3 = img3.getSize()
pw3 = right_w - pw2 - 10; ph3 = ph2
c.drawImage(img2, x, y - ph2, pw2, ph2, mask='auto')
c.drawImage(img3, x + pw2 + 10, y - ph2, pw3, ph3, preserveAspectRatio=True, anchor='c', mask='auto')
y -= ph2 + 16

c.setFont('Helvetica-Bold', 11); c.setFillColor(LAV_DEEP)
c.drawString(x, 34, 'Book: ines@tanitxr.org  ·  www.inessaid.com/speaking')
c.setFont('Helvetica', 8.4); c.setFillColor(MUTED)
c.drawString(28, 20, '© 2026 Ines Said')

c.save()
print('PDF written to web/ines-said-speaker.pdf')
