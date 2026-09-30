# Portfolio additions (2026-09-30): projects from the Froliq and Tanit XR sites that were missing here,
# richer detail for existing ones, publications, exhibitions, the Tanit XR community sections and the
# Work-with-me page. Facts come from frlq.co / tanitxr.org only. Items marked CHECK need Ines's confirmation.

NEW_PROJECTS = [
 dict(slug='tanit-virtual-museum', title='Tanit XR Virtual Museum', category='Cultural heritage · in progress',
   img='tx-museum-dome', alt='The domed hall of the Tanit XR virtual museum, built in Unity',
   card="The first community-led virtual museum of Tunisian heritage. Real scanned objects, life-size, in hand-modeled whitewashed rooms. Built in Unity by our volunteers.",
   chips=['Unity', 'Gaussian splats', 'Volunteer-built', '!In progress'],
   paras=[
     "This is the project I'm most excited about right now. Every object inside the museum was scanned in Tunisia by our volunteers, one at a time, and cleaned up by volunteers around the world. Then the objects are placed life-size in rooms that our volunteers modeled by hand: whitewashed walls, arches, a domed hall, a courtyard with a pool, tiled corridors, just like the ones back home.",
     "The museum is built in Unity with photogrammetry and Gaussian splats, and it has ambient sound recorded at the real sites. Our guide, Nura, was modeled in Blender by the community. Her narrated tour, \"Before It's Gone,\" is being written right now.",
     "Progress so far: the first courtyard in January 2026, the domed hall and courtyard with a pool in March, and the second wing in greybox in August. We're planning to release it on Viverse so anyone can walk in from a browser or a headset.",
     "My role is founder and coordinator. The rooms, the room kit and the models are the work of volunteers like Patrick Molen, Ala, Kristina Reyes, Cam Kania, Claire Natanek, Rachel West, Nick Kaufmann, Ana Beatriz Vega and Ray. I'm so grateful to every one of them!"],
   facts=[('Role', 'Founder and coordinator; the rooms and models are volunteer work'), ('Team', 'Tanit XR volunteers on four continents'),
          ('Tools', 'Unity, Blender, photogrammetry, Gaussian splats'), ('Started', 'January 2026'),
          ('Status', 'Second wing in greybox (August 2026); release planned on Viverse'),
          ('Guide', 'Nura, with her tour "Before It\'s Gone"')],
   links=[('The museum page on tanitxr.org', 'https://tanitxr.org/museum/'), ('Volunteer with us', 'https://tanitxr.org/volunteer/')],
   embeds_heading='Walk through (recorded in the Unity editor)',
   embeds=[dict(kind='video', id='museum-walkthrough-03', poster='tx-museum-dome', title='The domed hall and courtyard, March 2026'),
           dict(kind='video', id='museum-second-room', poster='tx-museum-greybox', title='The second wing, in greybox')],
   gallery=[('tx-museum-arches', 'The hall of arches.'), ('tx-museum-pool', 'The courtyard with a pool.'),
            ('tx-museum-corridor', 'A tiled corridor.'), ('tx-museum-niche', 'A statue in its niche.'),
            ('tx-museum-jan', 'January 2026: the very first courtyard.'), ('tx-nura', 'Nura, our guide.')]),

 dict(slug='tanit-explore', title='Explore in 3D, with Nura', category='Cultural heritage · web',
   img='tx-explore-hero', alt='The Explore in 3D collection on tanitxr.org, with Nura the guide',
   card="Every object our volunteers scanned, in your browser. Turn it with a finger, hear Nura tell its story, save your favorites, or put on a headset.",
   chips=['WebXR', 'Three.js', 'Gaussian splats', 'AR'],
   paras=[
     "Explore is the front door to everything Tanit XR has scanned. Every object our volunteers captured in Tunisia, one at a time, is in the browser. Turn each one with a finger. Nura, our guide, floats beside you and tells you what you're looking at.",
     "The collection is organized into little halls with names I love: Stones raised to Tanit, The people of Carthage, What held the roof up, Floors people walked on, Doors still in use, Where prayer faces, Words cut in stone. There's a map, sounds from the sites, and an AR button so you can see an object in your own room.",
     "You can save the ones you love, share them, collect badges, and step into each volunteer's own gallery to see what they scanned or modeled. As of September 2026 there are 69 objects in the collection, and more are added as volunteers finish them.",
     "We built it to be light and respectful: no cookies, no tracking beyond a simple visit count, and everything free to download."],
   facts=[('Role', 'Founder; I lead the web build and the experience design'), ('Team', 'Tanit XR volunteers'),
          ('Tools', 'WebXR, Three.js, Gaussian splats, Sketchfab'), ('Launched', '2026'),
          ('Collection', '69 objects in the browser (September 2026), 100+ models published in total')],
   links=[('Open Explore on tanitxr.org', 'https://tanitxr.org/explore/'), ('Tanit XR on Sketchfab', 'https://sketchfab.com/TanitXR')],
   embeds_heading='Try it right here',
   embeds=[dict(kind='page', id='https://tanitxr.org/explore/', title='This is the live Explore page on tanitxr.org. Open it full screen')],
   gallery=[('tx-explore-gallery', "A volunteer's gallery."), ('tx-alyssa-3', 'Illustration by our volunteer Alyssa George.')]),
]

# Extra detail pulled from frlq.co for projects that already exist here.
ENRICH = {
 'froliq-minigames': dict(
   facts_add=[('Client', 'National Energy Foundation (NEF)')],
   gallery_add=[('fq-recyclotopia', 'Recyclotopia: sort fast, five mistakes and it\'s game over.'),
                ('fq-bungaload', 'BungaLoad: four rooms, two minutes each, get the meter under 30%.'),
                ('fq-fantasticwinds', 'FantasticWinds: five levels, one minute each.'),
                ('fq-nef-hub', 'The Mario Party-style hub with the leaderboard.')],
   embeds_add=[dict(kind='youtube', id='fhi4HOKOqMg', title='Recyclotopia gameplay')]),
 'sustainaball': dict(
   facts_add=[('Client', 'Austin Energy and Austin FC')],
   gallery_add=[('fq-sustainaball', 'Sustainaball on the field.')],
   embeds_add=[dict(kind='youtube', id='lU-qdaFcKII', title='Sustainaball')]),
 'smithsonian-futures': dict(
   facts_add=[('Client', 'Smithsonian and Oracle'), ('On view', 'November 20, 2021 to July 6, 2022, Arts and Industries Building, Washington, D.C.'),
              ('Built with', 'Oracle and EDX Technologies')],
   gallery_add=[('fq-smithsonian', 'Time traveling from 1850 to 2050 at FUTURES.')]),
 'oracle-connected-hub': dict(
   facts_add=[('Since', '2023, starting with an AR outage visualization at the Oracle Industry Lab in Chicago')],
   gallery_add=[('fq-oracle', 'The Connected Hub: a miniature living utility neighborhood.'),
                ('fq-oracle-outage', 'Oracle Industry Lab, Chicago, 2023: outages in AR.')]),
 'vistra-tour': dict(
   gallery_add=[('fq-vistra', 'The gas turbine room, the heart of the plant.')]),
 'exelon-stem': dict(
   facts_add=[('Where', 'Washington, D.C., Maryland, Pennsylvania and beyond')],
   gallery_add=[('fq-exelon', 'Students trying a utility job in VR.'), ('fq-austin-isd', 'With Austin ISD and EcoRise teachers, 2026.'),
                ('fq-ace-celerate', 'ACE-Celerate with Atlantic City Electric: 200 high school students.')]),
 'nuclear-capture': dict(
   gallery_add=[('fq-davis-besse', 'Davis-Besse: a 3D photo of the plant you can step inside.')]),
 'tanit-xr': dict(
   gallery_add=[('tx-community-2', 'Volunteers together.'), ('tx-immersegt-1', 'Our track at ImmerseGT 2026, Georgia Tech.'),
                ('tx-awe-talk', 'AWE USA 2026 with Margarita Johnson.'), ('tx-alyssa-2', 'One archive, volunteers on every continent. Illustration by Alyssa George.')]),
 'ee-30-under-30': dict(gallery_add=[('tx-ee30-photo', 'EE 30 Under 30, Class of 2025.')]),
}

NEW_GROUP_SLUGS = {
 'Cultural heritage': ['tanit-virtual-museum', 'tanit-explore'],
}
NEW_CATS = {
 'tanit-virtual-museum': 'heritage', 'tanit-explore': 'heritage', }

PUBLICATIONS = [
 ('2026', 'Digital documentation, XR and citizen science for community-led heritage preservation in Tunisia and beyond',
  'Tanit XR team. El Jem International Conference, April 2026. Published in English, French and Tunisian Arabic.',
  [('English (PDF)', 'web/el-jem-2026-paper-english.pdf'), ('Français (PDF)', 'web/el-jem-2026-paper-french.pdf'), ('العربية (PDF)', 'web/el-jem-2026-paper-arabic.pdf')]),
 ('2023', 'Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts &amp; Sciences',
  'A. Barmpoutis, W. Guo, I. Said. IEEE Integrated STEM Education Conference (ISEC) 2023. Best Paper Award.',
  [('IEEE Xplore', 'https://ieeexplore.ieee.org/document/10402239')]),
 ('2022', 'Covid Reflections: augmented reality public art alongside mobile health clinics',
  'Published with ACM. Presented at the AI &amp; Society Symposium (University of Florida).',
  [('UF News', 'https://news.ufl.edu/2022/04/covid-reflections/')]),
 ('', 'spARc: two-handed AR animation with a radial time slider',
  'HCI research on an immersive animation tool, designed with focus groups.',
  [('ResearchGate', 'https://www.researchgate.net/profile/Ines-Said-2')]),
]

EXHIBITIONS = [
 ('2021–22', 'Smithsonian FUTURES', 'Arts and Industries Building, Washington, D.C. Future of Energy and Water, with Froliq and Oracle. 600,000+ visitors.', 'p-smithsonian-futures'),
 ('2022', 'Covid Reflections on tour', 'AR public art with mobile health clinics in Florida, California and Japan.', 'p-covid-reflections'),
 ('', 'HEAT, GFAA Biennial', 'Shadows of Tomorrow, Gainesville Fine Arts Association. Three months in the gallery, Excellence Award.', 'p-shadows-of-tomorrow'),
 ('', 'In the Machine', '4Most Gallery, Gainesville. Technology meets art, with UF Digital Worlds faculty and alumni.', None),
 ('', 'MIT Reality Hack, Parsons, Ringling College', 'Shadows of Tomorrow shown in Boston, New York City and Sarasota.', 'p-shadows-of-tomorrow'),
 ('2025–26', 'XR Women Museum', 'Tanit XR objects in two exhibitions, including Garden: In Full Bloom, an immersive museum of 30+ gallery worlds directed by Paige Dansinger.', 'p-tanit-xr'),
]

def publications_html(preview):
    items = ''
    for year, title, meta, links in PUBLICATIONS:
        ln = ' &middot; '.join(f'<a href="{u}">{t}</a>' for t, u in links)
        items += (f'<li><div><span class="t">{title}</span><div class="d">{meta}<br>{ln}</div></div>'
                  f'<span class="who">{year}</span></li>')
    return section(f'<ul class="list">{items}</ul>', 'Research', 'Publications',
                   'I love that my work gets to live in papers too. Here are the ones you can read.')

def exhibitions_html(preview):
    H = lambda p: href(p, preview)
    items = ''
    for year, title, meta, link in EXHIBITIONS:
        t = f'<a href="{H(link)}">{title}</a>' if link else title
        items += f'<li><div><span class="t">{t}</span><div class="d">{meta}</div></div><span class="who">{year}</span></li>'
    return section(f'<ul class="list">{items}</ul>', 'Exhibitions', 'Where my work has been shown',
                   'Museum floors, gallery walls and a few virtual worlds.')

def tanit_sections(preview):
    """The community-first story of Tanit XR, shown on its project page."""
    H = lambda p: href(p, preview)
    out = section(
        f'<div class="nura-card"><img src="web/tx-nura.jpg" alt="Nura, the Tanit XR guide" loading="lazy"><div>'
        f'<p class="sec-kicker">Meet Nura</p><h3>Our guide will show you around</h3>'
        f'<p>Nura floats beside you in the collection and tells you the story of each object. Pick one above, or step into the full experience on tanitxr.org.</p>'
        f'<a class="btn" href="https://tanitxr.org/explore/">Explore with Nura</a></div></div>')
    out += section(
        split(collage([('tx-community-1', 'Tanit XR volunteers'), ('tx-community-3', 'Volunteers on a site visit'),
                       ('tx-community-4', 'Scanning together'), ('tx-community-5', 'The community'), ('tx-alyssa-1', 'Illustration by Alyssa George')]),
              'Community', 'We started as an archive. We became a community.',
              ["Tanit XR is 85+ volunteers in Tunisia, the United States, Europe and Nigeria. We meet every Thursday at 12 pm Eastern (5 pm in Tunisia) to review scans, plan trips and help each other.",
               "Volunteers who have never been to Tunisia learn its history while modeling lamps, pottery and plants for our virtual museum, and we learn about theirs. That cultural exchange is the heart of it. So far our volunteers have modeled 34 objects by hand, like Rachel West's murex shell and Claire Natanek's Tunisian lamps."],
              ticks=['Weekly community call, every Thursday',
                     'Short history lessons on the sites we scan, recorded each week by Julia Moreno-Molen',
                     'Splats With Phones, our free 6-week scanning course taught by Mark Jeffcock',
                     'Mentoring, portfolio reviews and mock interviews for students and early-career volunteers'],
              buttons=[('Volunteer with us', 'https://tanitxr.org/volunteer/'), ('The Splats With Phones course', 'https://tanitxr.org/photogrammetry-with-phones-by-mark-jeffcock/')]),
        cls='tint')
    out += section(icon_cards([
        ('column', 'What we scan', 'Objects, one at a time, with our phones: the Punic stela of the Tophet of Salammbo, the Corinthian capital of Byrsa Hill, the mihrab niche of the medina of Tunis, carved fragments with inscriptions.', H('p-tanit-explore'), 'Explore them in 3D'),
        ('wave', 'Neapolis after the storm', 'In January 2026, Storm Harry stripped the sand off the coast at Nabeul and exposed parts of Neapolis. Within days our volunteer Youssef Lakdhar captured the newly revealed ruins in 3D.', H('b-storm-revealed-ruins'), 'The story'),
        ('globe', 'Beyond Tunisia', 'The Unique Mappers Network, 500+ citizen scientists in Nigeria founded by Victor Sunday, is replicating the Tanit XR model with a mini-grant from our fiscal sponsor. Their first 50 scans are due before the end of 2026.', 'https://tanitxr.org/uniquemappers/', 'Unique Mappers'),
        ('cube', 'The virtual museum', 'Our volunteers are building a museum in Unity with the real scanned objects placed life-size in hand-modeled rooms. Nura, our guide, will walk you through.', H('p-tanit-virtual-museum'), 'See the museum'),
        ('gavel', 'Hackathons we sponsored', 'A Tunisian-heritage track at ImmerseGT 2026 (Georgia Tech, 36 hours, winner: From Mystery to History) and two tracks at CityCamp Gainesville Hack Day 2026, where 23 projects were submitted.', 'https://tanitxr.org/immersegt-2026/', 'ImmerseGT 2026'),
        ('people', 'The people', 'Dr. Laura Harrison is our Chief Scientist and Dr. Caroline Nickerson leads partnerships and community. My sister Melek Said is our regional manager in Tunisia. Our fiscal sponsor is Florida Community Innovation, a US 501(c)(3).', 'https://tanitxr.org/our-people/', 'Meet the team'),
    ]), 'How it works', 'Community first, then the objects')
    out += recognized('Tanit XR in the world', [
        ('Auggie Awards', 'Finalist, Best Societal Impact · 2026', 'https://www.awexr.com/blog/1382-2026-auggie-awards-finalists-announced'),
        ('Voices of VR', 'Episode #1728 with Kent Bye', 'https://voicesofvr.com/1728-preserving-tunisian-cultural-heritage-with-tanit-xr-reality-capture'),
        ('Niantic Spatial', 'Interview with Nathan Bowser', 'https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873/'),
        ('Al Jazeera', 'Culture feature · 2025', 'https://www.aljazeera.net/amp/culture/2025/10/12/%D8%AA%D8%A7%D9%86%D9%8A%D8%AA-%D8%A5%D9%83%D8%B3-%D8%A2%D8%B1-%D9%85%D9%86%D8%B5%D8%A9-%D8%BA%D9%8A%D8%B1-%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9-%D8%AA%D9%88%D8%AB%D9%82'),
        ('AWE USA 2026', 'Talk with Margarita Johnson', 'https://www.awexr.com/usa-2026/speakers/2677-ines-said'),
        ('XR Women Museum', 'Two exhibitions', 'https://framevr.io/xrwomenmuseum'),
    ])
    return out

def body_work(preview):
    H = lambda p: href(p, preview)
    head = banner('Work with me', "Let's make something together", 'Talks, workshops, XR development and heritage scanning. Here is how we can work together.',
                  img='workshop', img2='oracle-demo', preview=preview)
    services = section(icon_cards([
        ('mic', 'Keynotes and talks', 'Heritage, climate and XR, told through the projects on this site. In person or online, in English, Arabic or French.', '#book', 'from $2,000'),
        ('camera', 'Scanning workshops', 'Half-day or full-day workshops on 3D scanning with phones, photogrammetry and Gaussian splats. We have been asked to train groups of 200!', '#book', 'from $2,500'),
        ('people', 'Panels and guest lectures', 'University classes, panels and podcasts about XR, heritage and STEM education.', '#book', 'from $750'),
        ('screen', 'Virtual talks', 'A 30 to 60 minute session for your team, class or community, anywhere in the world.', '#book', 'from $500'),
        ('headset', 'XR development', 'Apple Vision Pro, Meta Quest, mobile AR and WebXR. From a first prototype to a demo that travels to conferences.', '#book', "Let's talk"),
        ('tanit', 'Heritage and community projects', 'Want to start a scanning community like Tanit XR where you live, or bring our method to your museum or school? I would love to help.', '#book', "Let's talk"),
    ]), 'What I can do for you', 'Ways we can work together',
        'Community, nonprofit and student rates are always available. Just ask!')
    trust = recognized('People I have worked with', [
        ('Smithsonian', 'FUTURES exhibition', H('p-smithsonian-futures')), ('Oracle', 'Connected Hub', H('p-oracle-connected-hub')),
        ('Exelon', 'STEM program', H('p-exelon-stem')), ('Vistra', 'Plant tours and scans', H('p-vistra-tour')),
        ('NYPA', 'Vision Pro app', H('p-nypa-vision-pro')), ('NEF', 'VR mini-games', H('p-froliq-minigames')),
        ('Austin Energy', 'Sustainaball', H('p-sustainaball')),
    ])
    downloads = section(icon_cards([
        ('book', 'My CV (PDF)', 'Experience, education, publications, exhibitions and awards on two pages.', 'web/ines-said-cv.pdf', 'Download'),
        ('news', 'Speaker one-pager (PDF)', 'Topics, past stages and rates, ready to forward to your events team.', 'web/ines-said-speaker.pdf', 'Download'),
        ('spark', 'Press kit', 'Bio, photos and logos for your program or article.', H('press'), 'Open'),
    ]), 'Downloads', 'The paperwork, made easy', cls='tint')
    return head + services + trust + downloads


def body_work_page(preview):
    form = re.search(r'<form class="contact-form".*?</form>', _OLD_SPEAKING(preview), re.S).group(0)
    booking = section(f'<div id="book" class="book-wrap">{form}</div>', 'Book me', 'Tell me about your event or project',
                      'I read every message myself and reply within a few days.')
    return body_work(preview) + booking

def _insert_before_cta(html, extra):
    i = html.rfind('<div class="band deep cta-end')
    return html + extra if i < 0 else html[:i] + extra + html[i:]

_about_base = body_about
def body_about(preview):
    return _insert_before_cta(_about_base(preview), publications_html(preview))

_awards_base = body_awards
def body_awards(preview):
    return _insert_before_cta(_awards_base(preview), exhibitions_html(preview))
