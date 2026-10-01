#!/usr/bin/python3
"""Two-page CV PDF for Ines Said, in the site's cream and plum palette. Run from the repo root."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import textwrap

CREAM = HexColor('#fdf3ee'); TINT = HexColor('#f8e6e4'); PLUM = HexColor('#5e2246'); BERRY = HexColor('#8e3a63')
GOLD = HexColor('#c08a2e'); INK = HexColor('#43203a'); BODY = HexColor('#5c3a4e'); MUTED = HexColor('#a4808f')
W, H = letter
c = canvas.Canvas('web/ines-said-cv.pdf', pagesize=letter)
c.setTitle('Ines Said, CV'); c.setAuthor('Ines Said')
M = 44; y = 0

def page_frame():
    c.setFillColor(CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(PLUM); c.rect(0, H - 7, W, 7, fill=1, stroke=0)

def heading(title):
    global y
    if y < 110:
        new_page()
    c.setFont('Helvetica-Bold', 12.5); c.setFillColor(INK); c.drawString(M, y, title)
    c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(M, y - 5, M + 34, y - 5)
    y -= 20

def entry(left, title, sub='', width=96):
    global y
    if y < 70:
        new_page()
    c.setFont('Helvetica-Bold', 8.6); c.setFillColor(BERRY); c.drawString(M, y, left)
    c.setFont('Helvetica-Bold', 9.6); c.setFillColor(INK); c.drawString(M + 78, y, title); y -= 12
    if sub:
        c.setFont('Helvetica', 8.8); c.setFillColor(BODY)
        for ln in textwrap.wrap(sub, width):
            c.drawString(M + 78, y, ln); y -= 11
    y -= 3

def new_page():
    global y
    c.showPage(); page_frame(); y = H - 52
    c.setFont('Helvetica', 8.5); c.setFillColor(MUTED); c.drawString(M, H - 28, 'Ines Said  ·  CV  ·  page 2'); y = H - 60

# ---- page 1 ----
page_frame()
try:
    img = ImageReader('web/portrait.jpg'); iw, ih = img.getSize(); pw = 78; ph = pw * ih / iw
    c.drawImage(img, W - M - pw, H - 40 - ph, pw, ph, mask='auto')
except Exception:
    pass
y = H - 64
c.setFont('Helvetica-Bold', 28); c.setFillColor(INK); c.drawString(M, y, 'Ines Said'); y -= 19
c.setFont('Helvetica-Bold', 11); c.setFillColor(BERRY); c.drawString(M, y, 'Immersive artist and XR developer'); y -= 17
c.setFont('Helvetica', 9.3); c.setFillColor(BODY)
for ln in ('ines@tanitxr.org  ·  www.inessaid.com  ·  linkedin.com/in/inessaid',
           'Washington, D.C. area and Tunisia  ·  English, Arabic, French'):
    c.drawString(M, y, ln); y -= 12.5
y -= 8
intro = ("I'm from Sidi Mahersi, Nabeul, a 15-minute walk from the ruins of Neapolis. I build immersive experiences "
         "about heritage, climate and energy: I founded Tanit XR, a volunteer community scanning Tunisia's endangered "
         "heritage in 3D (100+ free models, 85+ volunteers on four continents), and I'm the Lead XR Developer at Froliq, "
         "where my work has been shown at the Smithsonian and travels with Oracle, Exelon and Vistra.")
c.setFont('Helvetica', 9.5); c.setFillColor(BODY)
for ln in textwrap.wrap(intro, 108):
    c.drawString(M, y, ln); y -= 12.5
y -= 14

heading('Experience')
entry('2025 –', 'Founder, Tanit XR', 'Volunteer community scanning Tunisian heritage in 3D, one object at a time, with phones. Weekly community call, history lessons, the free Splats With Phones course, mentoring. Model being replicated in Nigeria with the Unique Mappers Network. Fiscally sponsored by Florida Community Innovation, a US 501(c)(3).')
entry('2023 –', 'Lead XR Developer, Froliq', 'I lead our AR and VR projects for energy, education and industry: Oracle Connected Hub (iPad, Quest 3, Vision Pro, Windows), NYPA Grid Experience on Apple Vision Pro, the Vistra Energy Hazard Tour, nuclear plant reality capture, the NEF VR mini-games, Sustainaball, StEVie and the Exelon STEM program.')
entry('2022 – 23', 'XR Developer, Froliq', 'Future of Energy and Water for the Smithsonian FUTURES exhibition (with Oracle), 600,000+ visitors; VR energy-education games.')
entry('2023', 'Adjunct Lecturer, University of Florida', 'Taught VR application development for Android and wearables.')
entry('2021 – 23', 'Software Engineer, University of Florida', 'Covid Reflections (AR public art with mobile health clinics) and spARc (AR animation tool), Digital Worlds Institute.')
entry('2018 – 19', '3D Virtualization Lab Intern, University of South Florida', 'Artec scanners, drones, photogrammetry.')

heading('Education')
entry('2020 – 21', 'M.S. Digital Arts & Sciences', 'University of Florida, MiDAS, Digital Worlds Institute.')
entry('2015 – 19', 'B.E. Computer Science', 'University of South Florida. Exchange at Deakin University, Australia (2017).')

heading('Awards and recognition')
for left, t, s in [
    ('2026', 'Auggie Awards finalist, Best Societal Impact', 'Augmented World Expo, for Tanit XR.'),
    ('2025', 'EE 30 Under 30, Class of 2025', 'North American Association for Environmental Education (NAAEE).'),
    ('2023', 'Best Paper Award, IEEE ISEC 2023', 'Developing Mini VR Game Engines as an Engaging Learning Method (with A. Barmpoutis and W. Guo).'),
    ('', 'Excellence Award, GFAA Biennial', 'For Shadows of Tomorrow, presented by Miami Chief Heat Officer Jane Gilbert and author Jeff Goodell.'),
    ('', 'XR Prize Challenge, MVP finalist', 'Augmented World Expo, for Shadows of Tomorrow.'),
    ('', 'Hackathon wins', 'Supported by Google and IBM through UF MiDAS; MIT Reality Hack.'),
]:
    entry(left, t, s)

# ---- page 2 ----
new_page()
heading('Publications')
for left, t, s in [
    ('2026', 'Digital documentation, XR and citizen science for community-led heritage preservation in Tunisia and beyond', 'Tanit XR. El Jem International Conference. Published in English, French and Tunisian Arabic.'),
    ('2023', 'Immersive Climate Narratives: Using Extended Reality to Raise Climate Change Awareness', 'I. Said, A. J. Stanbury, E. Delhagen, H. Kang. ACM VRST.'),
    ('2023', 'Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts and Sciences', 'A. Barmpoutis, W. Guo, I. Said. IEEE ISEC. Best Paper Award.'),
    ('2022', 'Covid Reflections: AR in Public Health Communications', 'I. Said, A. J. Stanbury, E. Delhagen, A. Winger-Bearskin. ACM VRST.'),
    ('2021', 'HoloKeys: Interactive Piano Education Using Augmented Reality and IoT', 'A. J. Stanbury, I. Said, H. J. Kang. ACM VRST. Cited 18 times.'),
    ('2021', 'SpArc: A VR Animating Tool at Your Fingertips', 'B. Li, I. Said, L. Kirova, M. Blokhina, H. J. Kang. ACM VRST.'),
    ('2021', 'Immersive learning with an AI-enhanced virtual standardized patient to improve dental students\u2019 communication', 'A. Gowthaman, L. Kirova, B. Li, P. Molen, I. Said, J. Smith, C. Sukotjo. ACHI 2021.'),
]:
    entry(left, t, s)

heading('Exhibitions')
for left, t, s in [
    ('2021 – 22', 'Smithsonian FUTURES, Washington, D.C.', 'Future of Energy and Water, with Froliq and Oracle. 600,000+ visitors.'),
    ('2022', 'Covid Reflections on tour', 'Florida, California and Japan, with mobile health clinics. Covered by ABC, CBS and UF News.'),
    ('', 'HEAT, GFAA Biennial, Gainesville', 'Shadows of Tomorrow, three months in the gallery.'),
    ('', 'MIT Reality Hack, Parsons School of Design, Ringling College', 'Shadows of Tomorrow.'),
    ('', 'In the Machine, 4Most Gallery, Gainesville', 'With UF Digital Worlds faculty and alumni.'),
    ('2025 – 26', 'XR Women Museum', 'Tanit XR objects in two exhibitions.'),
]:
    entry(left, t, s)

heading('Talks and judging')
for left, t, s in [
    ('2026', 'AWE USA, Long Beach', 'From Scans to XR: A Practical Pipeline for Cultural Heritage, with Margarita Johnson. Also spoke at AWE 2022.'),
    ('2026', 'Energy Thought Summit, San Antonio', 'Main stage: photogrammetry for energy and heritage.'),
    ('2026', 'El Jem International Conference, Tunisia', 'Presented Tanit XR at the El Jem Museum, a few steps from the amphitheater.'),
    ('2026', 'Spatial Creator Spotlight; Voices of VR #1728', 'Full episode on Tanit XR; interview with Kent Bye at AWE.'),
    ('', 'Judge', 'Games for Change Awards and Student Challenge; EE 30 Under 30 Class of 2026 selection; Heavener International Case Competition 2025 (University of Florida); E4 Youth Showcase 2025 (Austin).'),
    ('', 'Hackathon tracks organized', 'Tunisian-heritage track at ImmerseGT 2026 (Georgia Tech); two tracks at CityCamp Gainesville Hack Day 2026.'),
]:
    entry(left, t, s)

heading('Tools')
c.setFont('Helvetica', 9.5); c.setFillColor(BODY)
for ln in textwrap.wrap('Unity, Unity PolySpatial (visionOS), Meta Quest, Apple Vision Pro, mobile AR (ARKit, ARCore), WebXR, Three.js, Needle Engine, Blender, photogrammetry and Gaussian splats (Scaniverse, PortalCam, RealityCapture), C#, Python, JavaScript.', 108):
    c.drawString(M, y, ln); y -= 12.5
c.setFont('Helvetica-Oblique', 8.5); c.setFillColor(MUTED); c.drawString(M, 30, 'Latest version and links: www.inessaid.com/work-with-me/')
c.save()
print('web/ines-said-cv.pdf written')
