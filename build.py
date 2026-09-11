#!/usr/bin/env python3
"""Build inessaid.com — lavender edition.

Outputs:
  site/  — index.html, about/projects/awards/talks/press.html,
           project-<slug>.html detail pages, web/ images
  preview.html — single-file version with hash routing + data-URI images
"""
import base64, os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'docs')

CSS = r"""
:root{
  --lav:#8e3a63; --lav-deep:#5e2246; --tint-lav:#f8e6e4; --tint-blush:#f9eeda;
  --pink:#b9486b; --gold:#c08a2e;
  --ink:#43203a; --body:#5c3a4e; --muted:#a4808f; --line:#eed9d2; --soft:#f9efe9;
  --cream:#fdf3ee; --deep:#5e2246;
}
*{box-sizing:border-box}
body{
  margin:0;background:var(--cream);color:var(--body);
  font-family:"Bitter",Georgia,serif;
  font-size:17px;line-height:1.7;
}
h1,h2,h3{font-weight:400 !important}
.squiggle{display:block;width:100%;height:22px;margin:0}
.squiggle path{stroke:var(--lav);stroke-width:2.5;fill:none;opacity:.55}

/* handmade touches */
.page-head h1::after, .sec-title::after{
  content:"";display:block;height:12px;margin-top:12px;
  background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 14' preserveAspectRatio='none'><path d='M0 7 Q 10 1,20 7 T 40 7 T 60 7 T 80 7 T 100 7 T 120 7 T 140 7 T 160 7' fill='none' stroke='%23c08a2e' stroke-width='2.6' stroke-linecap='round'/></svg>") left center/160px 12px no-repeat}
.page-head h1::after{width:170px}
.sec-title::after{width:110px;background-size:110px 10px;height:10px}
.intro-home h1::after,.hero-cine h1::after{margin-left:auto;margin-right:auto;background-position:center}
.page-head{position:relative;z-index:0}
.page-head::before{content:"";position:absolute;z-index:-1;width:320px;height:200px;left:-70px;top:-24px;
  background:radial-gradient(closest-side,#f2cfdc99,transparent 72%);
  border-radius:62% 38% 55% 45%/48% 62% 38% 52%}
.page-head::after{content:"";position:absolute;z-index:-1;width:240px;height:160px;right:-30px;top:30px;
  background:radial-gradient(closest-side,#ecd9a866,transparent 70%);
  border-radius:44% 56% 38% 62%/58% 44% 56% 42%}
/* scrapbook photos */
.gallery figure{transition:transform .2s}
.gallery figure:nth-child(odd){transform:rotate(-1.3deg)}
.gallery figure:nth-child(even){transform:rotate(1.1deg)}
.gallery figure:hover{transform:rotate(0) scale(1.02)}
.gallery img{border:8px solid #fff;box-shadow:0 8px 24px rgba(67,32,58,.16);border-radius:4px}
.media-strip figure:nth-child(odd){transform:rotate(-.8deg)}
.media-strip figure:nth-child(even){transform:rotate(.7deg)}
.media-strip img{border:8px solid #fff;box-shadow:0 8px 24px rgba(67,32,58,.14);border-radius:4px}
.side-photo img{border-radius:18px 42px 24px 38px/34px 20px 42px 26px;border:8px solid #fff;box-shadow:0 10px 28px rgba(67,32,58,.16)}
.detail-hero img{border-radius:22px 48px 26px 44px/40px 24px 46px 28px}
.photo-band img{border:6px solid #fff2}
.tanit-mark{display:block;margin:0 auto 18px;width:30px;height:38px;opacity:.9}
.tanit-mark path,.tanit-mark circle,.tanit-mark line{stroke:#d8a9a0;stroke-width:2;fill:none;stroke-linecap:round}
/* languages */
.lang-switch{display:flex;gap:10px;align-items:center;font-size:.78rem;font-weight:700}
.lang-switch a{color:var(--muted)}
.lang-switch a.on{color:var(--lav-deep);border-bottom:2px solid var(--gold)}
[dir="rtl"] body, [dir="rtl"]{font-family:"Noto Naskh Arabic","Bitter",serif}
[dir="rtl"] h1,[dir="rtl"] h2,[dir="rtl"] h3,[dir="rtl"] .brand,[dir="rtl"] .stats b{font-family:"Aref Ruqaa",serif}
[dir="rtl"] .kicker,[dir="rtl"] nav a,[dir="rtl"] .btn{letter-spacing:0}
[dir="rtl"] .page-head h1::after,[dir="rtl"] .sec-title::after{background-position:right center}
h1,h2,h3{font-family:"Yeseva One",Georgia,serif;font-weight:600;color:var(--ink);letter-spacing:-.01em;text-wrap:balance}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
a{color:var(--lav-deep);text-decoration:none}
a:hover{text-decoration:underline;text-underline-offset:3px}
a:focus-visible,button:focus-visible{outline:2px solid var(--lav);outline-offset:3px;border-radius:4px}
img{max-width:100%}

/* header */
.site-header{position:sticky;top:0;background:#fdf3eeee;backdrop-filter:blur(8px);border-bottom:1px solid var(--line);z-index:10}
.site-header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:66px;flex-wrap:wrap}
.brand{font-family:"Yeseva One",serif;font-weight:700;font-size:1.3rem;color:var(--ink)}
.brand em{font-style:normal;color:var(--lav)}
.brand:hover{text-decoration:none;color:var(--lav-deep)}
nav{display:flex;gap:24px;flex-wrap:wrap}
nav a{font-size:.8rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--body)}
nav a:hover{color:var(--lav-deep);text-decoration:none}
nav a.active{color:var(--lav-deep);border-bottom:2px solid var(--lav);padding-bottom:2px}

/* page head */
.page-head{padding:64px 0 8px}
.page-head .kicker{margin-bottom:10px}
.page-head h1{font-size:clamp(2.2rem,5vw,3.4rem);margin:0 0 10px}
.page-head p.sub{max-width:62ch;color:var(--muted);font-size:1.08rem;margin:0}

/* hero (home) — Xiye-style photo band + personal intro */
.photo-band{background:var(--deep);padding:30px 0}
.photo-band .strip{display:grid;grid-template-columns:1fr 1.3fr 1fr;gap:14px;max-width:1160px;margin:0 auto;padding:0 20px;align-items:center}
.photo-band img{display:block;width:100%;height:360px;object-fit:cover;border-radius:6px}
.photo-band .strip figure{margin:0}
.photo-band .strip figure:nth-child(2) img{height:430px}
@media(max-width:760px){.photo-band .strip{grid-template-columns:1fr}.photo-band .strip figure:nth-child(1),.photo-band .strip figure:nth-child(3){display:none}}
.intro-home{text-align:center;padding:68px 24px 20px;max-width:760px;margin:0 auto}
.intro-home h1{font-size:clamp(2.6rem,6vw,4rem);margin:10px 0 0;color:var(--ink)}
.intro-home h1 em{font-style:normal;color:var(--lav)}
.intro-home p.lede{font-size:1.13rem;margin:24px auto 30px;max-width:58ch}
.intro-home .btn-row{justify-content:center}

/* hero (home) — cinematic full-bleed */
.hero-cine{position:relative;min-height:540px;display:flex;align-items:center;background:url(web/el-jem.jpg) center 30%/cover no-repeat #43203a}
.hero-cine::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,14,32,.55),rgba(56,22,44,.62) 55%,rgba(56,22,44,.82))}
.hero-cine .inner{position:relative;max-width:860px;margin:0 auto;padding:120px 24px 100px;text-align:center;color:#fdf3ee}
.hero-cine .kicker{color:var(--gold);justify-content:center}
.hero-cine h1{font-size:clamp(2.8rem,6.5vw,4.6rem);line-height:1.08;margin:0;color:#fff;text-shadow:0 2px 24px rgba(30,8,24,.5)}
.hero-cine p.lede{font-size:1.14rem;color:#f6e3dc;max-width:58ch;margin:26px auto 34px}
.hero-cine .btn.ghost{background:transparent;color:#fff;border:2px solid #ffffffaa}
.hero-cine .btn.ghost:hover{background:#ffffff22;border-color:#fff}
.hero{padding:72px 0 64px}
.hero .grid{display:grid;grid-template-columns:1.35fr 1fr;gap:56px;align-items:center}
.kicker{font-size:.78rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--pink);margin:0 0 14px}
.kicker::before{content:"\2726\00a0\00a0";color:var(--lav)}
.hero h1{font-size:clamp(2.6rem,6vw,4.3rem);line-height:1.06;margin:0}
.hero h1 em{font-style:italic;color:var(--lav-deep)}
.hero p.lede{font-size:1.13rem;max-width:56ch;margin:24px 0 30px}
.btn-row{display:flex;gap:14px;flex-wrap:wrap}
.btn{display:inline-block;background:var(--gold);color:#341326;font-weight:700;font-size:.95rem;
  padding:13px 30px;border-radius:999px;transition:background .15s,transform .15s;box-shadow:0 6px 18px #c08a2e33}
.btn:hover{background:#a97722;text-decoration:none;transform:translateY(-2px)}
.btn.ghost{background:#fff;color:var(--pink);border:2px solid var(--tint-blush);box-shadow:none;padding:11px 28px}
.btn.ghost:hover{background:var(--tint-blush);border-color:var(--tint-blush)}
.hero-photo{position:relative;margin:0}
.hero-photo::before{content:"";position:absolute;inset:6% -6% -6% 6%;background:var(--tint-lav);
  border-radius:58% 42% 55% 45% / 48% 55% 45% 52%}
.hero-photo::after{content:"\2726";position:absolute;top:-14px;right:8%;font-size:1.6rem;color:var(--gold)}
.hero-photo img{position:relative;display:block;width:100%;max-width:370px;margin-left:auto;
  border-radius:36% 64% 52% 48% / 42% 46% 54% 58%;object-fit:cover;aspect-ratio:1/1.06}
@media(max-width:820px){.hero .grid{grid-template-columns:1fr}.hero-photo img{margin:20px auto 0}}

/* bands */
.band{padding:56px 0}
.band.lav{background:var(--tint-lav)}
.band.blush{background:var(--tint-blush)}
.band.soft{background:var(--soft)}
.band.deep{background:var(--deep)}
.band.deep .sec-title,.band.deep h2{color:#fdf3ee}
.band.deep p,.band.deep span{color:#f0d9d4}
.band.deep .kicker{color:var(--gold)}
.band.deep .btn.ghost{background:transparent;color:#fff;border:2px solid #ffffff88}
.band.deep .btn.ghost:hover{background:#ffffff1e;border-color:#fff}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:32px;text-align:center}
.stats b{display:block;font-family:"Yeseva One",serif;font-weight:700;font-size:2rem;color:var(--lav-deep)}
.stats span{display:block;font-size:.9rem;margin-top:6px}
.stats a{display:block;color:inherit;border-radius:16px;padding:14px 10px;transition:background .15s,transform .15s}
.stats a:hover{background:#ffffffb0;text-decoration:none;transform:translateY(-2px)}
@media(max-width:760px){.stats{grid-template-columns:1fr 1fr;gap:26px}}

/* sections */
section.block{padding:72px 0}
.sec-title{font-size:clamp(1.7rem,3.4vw,2.3rem);margin:0 0 8px}
.sec-sub{color:var(--muted);margin:0 0 36px;max-width:60ch}

/* cards */
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.cards.two{grid-template-columns:repeat(2,1fr)}
a.card{color:inherit;display:flex}
a.card:hover{text-decoration:none}
.card-inner{background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;
  display:flex;flex-direction:column;width:100%;transition:transform .18s,box-shadow .18s}
a.card:hover .card-inner{transform:translateY(-4px);box-shadow:0 14px 34px #8a63d226}
.thumb{aspect-ratio:3/2;overflow:hidden;background:var(--soft)}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.thumb.ph{display:flex;align-items:center;justify-content:center;flex-direction:column;gap:6px}
.thumb.ph.lav{background:var(--tint-lav)}
.thumb.ph.blush{background:var(--tint-blush)}
.thumb.ph b{font-family:"Yeseva One",serif;font-weight:700;font-size:1.5rem;color:var(--ink)}
.thumb.ph span{font-size:.72rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.card-body{padding:20px 22px 22px;display:flex;flex-direction:column;gap:10px;flex:1}
.card-body h3{font-size:1.22rem;margin:0}
.card-body p{margin:0;font-size:.94rem}
.card-more{margin-top:auto;padding-top:10px;font-size:.82rem;font-weight:800;letter-spacing:.06em;
  text-transform:uppercase;color:var(--lav-deep)}
.chips{display:flex;gap:8px;flex-wrap:wrap;padding-top:4px}
.chip{font-size:.68rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;
  color:var(--lav-deep);background:var(--tint-lav);border-radius:999px;padding:4px 12px}
.chip.blush{color:var(--pink);background:var(--tint-blush)}
@media(max-width:900px){.cards{grid-template-columns:1fr 1fr}}
@media(max-width:620px){.cards,.cards.two{grid-template-columns:1fr}}

/* project detail */
.detail-hero{margin:36px 0 0}
.detail-hero img{display:block;width:100%;max-height:520px;object-fit:cover;border-radius:24px}
.detail-grid{display:grid;grid-template-columns:1.5fr 1fr;gap:52px;padding:52px 0 0;align-items:start}
.detail-grid .prose p{margin:0 0 1.15em;max-width:64ch}
.fact-card{background:var(--soft);border:1px solid var(--line);border-radius:20px;padding:26px 28px}
.fact-card h3{font-size:.78rem;font-weight:800;font-family:"Bitter",serif;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);margin:0 0 12px}
.fact-card ul{list-style:none;margin:0 0 8px;padding:0}
.fact-card li{padding:8px 0;border-top:1px dashed var(--line);font-size:.94rem}
.fact-card li:first-child{border-top:none;padding-top:0}
.fact-card li b{color:var(--ink)}
.backlink{display:inline-block;margin:28px 0 0;font-weight:800;font-size:.82rem;letter-spacing:.08em;text-transform:uppercase}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:52px 0 0}
.gallery figure{margin:0}
.gallery img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:16px}
.gallery figcaption{font-size:.8rem;color:var(--muted);padding-top:8px}
@media(max-width:820px){.detail-grid{grid-template-columns:1fr}.gallery{grid-template-columns:1fr 1fr}}

/* embeds: videos + 3D models */
.embeds{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin:52px 0 0}
.embeds.one{grid-template-columns:1fr;max-width:760px}
.embed figure{margin:0}
.embed iframe{display:block;width:100%;aspect-ratio:16/10;border:0;border-radius:16px;background:var(--soft)}
.embed figcaption{font-size:.8rem;color:var(--muted);padding-top:8px}
.embed-ph{display:flex;align-items:center;justify-content:center;text-align:center;aspect-ratio:16/10;
  background:var(--tint-lav);border-radius:16px;font-weight:800;color:var(--lav-deep);padding:20px}
@media(max-width:680px){.embeds{grid-template-columns:1fr}}

/* about */
.two-col{display:grid;grid-template-columns:1.3fr 1fr;gap:52px;align-items:start}
.two-col .prose p{margin:0 0 1.15em;max-width:62ch}
.side-photo{margin:0}
.side-photo img{display:block;width:100%;border-radius:24px}
.side-photo figcaption{font-size:.82rem;color:var(--muted);padding-top:10px}
.pull{background:var(--tint-blush);border-radius:24px;padding:34px 38px;margin:44px 0}
.pull p{font-family:"Yeseva One",serif;font-style:italic;font-weight:600;font-size:1.45rem;line-height:1.45;color:var(--ink);margin:0}
.pull span{display:block;font-family:"Bitter",serif;font-style:normal;font-weight:700;font-size:.82rem;color:var(--pink);margin-top:14px;letter-spacing:.06em;text-transform:uppercase}
.now-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:8px}
.now{background:var(--tint-lav);border-radius:16px;padding:20px 22px}
.now b{display:block;font-family:"Yeseva One",serif;font-weight:700;font-size:1.02rem;color:var(--ink)}
.now span{font-size:.88rem;color:var(--body)}
@media(max-width:900px){.now-grid{grid-template-columns:1fr 1fr}}
@media(max-width:820px){.two-col{grid-template-columns:1fr}}

/* lists */
.list{list-style:none;margin:0;padding:0}
.list li{display:grid;grid-template-columns:1fr auto;gap:6px 28px;padding:18px 2px;border-top:1px solid var(--line);align-items:baseline}
.list li:last-child{border-bottom:1px solid var(--line)}
.list .t{font-family:"Yeseva One",serif;font-weight:600;font-size:1.12rem;color:var(--ink)}
.list .t a{color:var(--ink)}
.list .t a:hover{color:var(--lav-deep)}
.list .d{color:var(--muted);font-size:.94rem}
.list .who{font-size:.75rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--pink);text-align:right;white-space:nowrap}
@media(max-width:620px){.list li{grid-template-columns:1fr}.list .who{text-align:left}}
.media-strip{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin:44px 0 0}
.media-strip figure{margin:0}
.media-strip img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:20px}
.media-strip figcaption{font-size:.8rem;color:var(--muted);padding-top:8px}
@media(max-width:620px){.media-strip{grid-template-columns:1fr}}

/* footer */
footer{background:var(--deep);margin-top:72px;padding:52px 0 44px}
footer .foot-grid h3{color:#d8a9a0}
footer .foot-grid a{color:#fdf3ee}
footer .foot-grid p{color:#eccfc8}
footer .legal{border-top:1px solid #7c4062;color:#d8a9a0}
.foot-grid{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:36px}
.foot-grid h3{font-family:"Bitter",serif;font-size:.76rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
.foot-grid a{display:block;color:var(--ink);font-weight:700;padding:3px 0}
.foot-grid p{margin:0;color:var(--body);font-size:.92rem;max-width:34ch}
.legal{border-top:1px solid #ddd0f0;margin-top:40px;padding-top:20px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;color:var(--muted);font-size:.8rem}
@media(max-width:760px){.foot-grid{grid-template-columns:1fr}}
/* opportunities board */
.opp-table{width:100%;border-collapse:collapse;font-size:.95rem}
.opp-table th{font-size:.72rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);
  text-align:left;padding:10px 14px;border-bottom:2px solid var(--line)}
.opp-table td{padding:14px;border-bottom:1px solid var(--line);vertical-align:top}
.opp-table td a{color:var(--ink)}
.opp-table td a:hover{color:var(--lav-deep)}
.opp-desc{font-size:.85rem;color:var(--muted);max-width:46ch;margin-top:3px}
.opp-amount{font-weight:800;color:var(--lav-deep);white-space:nowrap}
.opp-date{white-space:nowrap;color:var(--body);font-variant-numeric:tabular-nums}
.opp-badge{display:inline-block;font-size:.72rem;font-weight:800;letter-spacing:.04em;border-radius:999px;padding:4px 12px;white-space:nowrap}
.opp-badge.open{background:var(--tint-lav);color:var(--lav-deep)}
.opp-badge.soon{background:var(--tint-blush);color:var(--pink)}
.opp-badge.closed{background:var(--soft);color:var(--muted)}
tr.opp-closed{display:none;opacity:.55}
.opp-table.show-closed tr.opp-closed{display:table-row}

/* contact form */
.contact-form{background:var(--soft);border:1px solid var(--line);border-radius:24px;padding:34px 36px;max-width:640px}
.contact-form label{display:block;font-size:.78rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:16px 0 6px}
.contact-form input,.contact-form select,.contact-form textarea{
  width:100%;border:1px solid var(--line);border-radius:12px;padding:12px 14px;
  font-family:"Bitter",serif;font-size:1rem;color:var(--ink);background:#fff}
.contact-form input:focus,.contact-form select:focus,.contact-form textarea:focus{outline:2px solid var(--lav);border-color:var(--lav)}
.contact-form button{margin-top:22px;background:var(--lav);color:#fff;font-weight:800;font-size:.95rem;
  border:0;padding:13px 30px;border-radius:999px;cursor:pointer;font-family:"Bitter",serif;box-shadow:0 6px 18px #8a63d240}
.contact-form button:hover{background:var(--lav-deep)}
@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Yeseva+One&'
         'family=Bitter:ital,wght@0,400;0,600;0,700;1,400&'
         'family=Aref+Ruqaa:wght@400;700&family=Noto+Naskh+Arabic:wght@400;600;700&display=swap">')

PAGES = ['home', 'about', 'projects', 'awards', 'speaking', 'opportunities', 'press', 'blog']
LABEL = {'home': 'Home', 'about': 'About', 'projects': 'Projects', 'awards': 'Awards',
         'speaking': 'Speaking', 'opportunities': 'Opportunities', 'press': 'Press', 'blog': 'Blog'}
TITLE = {'home': 'Ines Said | XR Immersive Artist and Technologist',
         'about': 'About | Ines Said', 'projects': 'Projects | Ines Said',
         'awards': 'Awards & Recognition | Ines Said', 'speaking': 'Speaking & Media | Ines Said',
         'opportunities': 'Art, XR & Impact Opportunities | Ines Said',
         'press': 'Press | Ines Said', 'blog': 'Blog | Ines Said'}

NEWSLETTER_URL = 'https://www.linkedin.com/newsletters/art-xr-impact-opportunities-7370189407523454976/'

def href(page, preview):
    if preview:
        return '#/' + page
    if page == 'home':
        return 'index.html'
    if page.startswith('p-'):
        return 'project-' + page[2:] + '.html'
    if page.startswith('b-'):
        return 'blog-' + page[2:] + '.html'
    if page.startswith('a-'):
        return 'award-' + page[2:] + '.html'
    return page + '.html'

# --- video / 3D model embeds ---
def embed_html(e, preview):
    kind, eid, title = e['kind'], e['id'], e['title']
    style = ''
    if kind == 'youtube':
        src, watch = f'https://www.youtube.com/embed/{eid}', f'https://www.youtube.com/watch?v={eid}'
    elif kind == 'vimeo':
        src, watch = f'https://player.vimeo.com/video/{eid}', f'https://vimeo.com/{eid}'
    elif kind == 'linkedin':
        src = f'https://www.linkedin.com/embed/feed/update/urn:li:activity:{eid}'
        watch = f'https://www.linkedin.com/feed/update/urn:li:activity:{eid}/'
        style = ' style="aspect-ratio:1/1;max-width:560px"'
    else:  # sketchfab
        src, watch = f'https://sketchfab.com/models/{eid}/embed', f'https://sketchfab.com/3d-models/{eid}'
    if preview:
        icon = '&#127963;' if kind == 'sketchfab' else '&#9658;'
        return (f'<div class="embed"><a class="embed-ph" href="{watch}">{icon}&nbsp; {title}<br>'
                f'<span style="font-weight:700;font-size:.8rem;color:var(--muted)">(plays here on the live site — click to open)</span></a></div>')
    allow = 'autoplay; fullscreen; xr-spatial-tracking' if kind == 'sketchfab' else 'accelerometer; autoplay; encrypted-media; picture-in-picture'
    return (f'<div class="embed"><figure><iframe src="{src}" title="{title}" loading="lazy"{style} '
            f'allow="{allow}" allowfullscreen></iframe><figcaption>{title}</figcaption></figure></div>')

def embeds_block(embeds, preview, heading=None):
    if not embeds:
        return ''
    h = f'<h2 class="sec-title" style="font-size:1.4rem;margin:52px 0 0">{heading}</h2>' if heading else ''
    cls = 'embeds one' if len(embeds) == 1 else 'embeds'
    return h + f'<div class="{cls}">' + ''.join(embed_html(e, preview) for e in embeds) + '</div>'

def lang_switch(current='en', prefix=''):
    # prefix: '' on root pages, '../' on /fr/ and /ar/ pages
    en = f'{prefix}index.html' if prefix else 'index.html'
    fr = f'{prefix}fr/' if prefix == '' else ('' if current == 'fr' else '../fr/')
    ar = f'{prefix}ar/' if prefix == '' else ('' if current == 'ar' else '../ar/')
    def a(code, url, label):
        cls = ' class="on"' if current == code else ''
        return f'<a href="{url or "#"}"{cls}>{label}</a>'
    return ('<div class="lang-switch">' + a('en', en if current != 'en' else '#', 'EN') +
            a('fr', fr if current != 'fr' else '#', 'FR') +
            a('ar', ar if current != 'ar' else '#', '&#1593;&#1585;&#1576;&#1610;') + '</div>')

def nav_html(active, preview, lang='en'):
    links = []
    for p in PAGES:
        cls = ' class="active"' if p == active else ''
        links.append(f'<a href="{href(p, preview)}"{cls}>{LABEL[p]}</a>')
    switch = '' if preview else lang_switch('en', '')
    return ('<header class="site-header"><div class="wrap">'
            f'<a class="brand" href="{href("home", preview)}">Ines Said<em>&thinsp;&#10022;</em></a>'
            '<nav>' + ''.join(links) + '</nav>' + switch + '</div></header>')

FOOTER = """
<footer><div class="wrap">
  <svg class="tanit-mark" viewBox="0 0 30 38" aria-hidden="true">
    <circle cx="15" cy="6" r="4"/>
    <line x1="3" y1="15" x2="27" y2="15"/>
    <line x1="3" y1="15" x2="3" y2="11"/>
    <line x1="27" y1="15" x2="27" y2="11"/>
    <path d="M15 12 L5 34 H25 Z"/>
  </svg>
  <div class="foot-grid">
    <div>
      <h3>Ines Said</h3>
      <p>XR immersive artist and technologist. Preserving heritage and confronting
      climate challenges through augmented and virtual reality.</p>
    </div>
    <div>
      <h3>Contact</h3>
      <a href="mailto:ines@tanitxr.org">ines@tanitxr.org</a>
      <a href="mailto:inessaid88@gmail.com">inessaid88@gmail.com</a>
    </div>
    <div>
      <h3>Follow</h3>
      <a href="https://www.linkedin.com/in/inessaid/">LinkedIn</a>
      <a href="https://www.instagram.com/inessaidd/">Instagram</a>
      <a href="https://www.facebook.com/ines1said/">Facebook</a>
      <a href="https://tanitxr.org">tanitxr.org</a>
    </div>
  </div>
  <div class="legal"><span>&copy; 2026 Ines Said. All rights reserved.</span><span>Made with love, between Tunisia &amp; D.C. &#10022;</span></div>
</div></footer>"""

# ---------------- projects data ----------------
# img: web/<name>.jpg  |  ph: (big, small, tone) placeholder tile
PROJECTS = [
 dict(slug='tanit-xr', title='Tanit XR', category='Cultural Heritage',
   img='el-jem', alt='Ines Said at the El Jem Amphitheater in Tunisia',
   card="Tunisia's first open-source digital heritage archive — 80+ artifacts documented across 20 archaeological sites, from mosaics to the El Jem Amphitheater.",
   chips=['Photogrammetry', 'Gaussian splats', '!Auggie finalist'],
   paras=[
     "Tanit XR is Tunisia's first open-source archive of endangered artifacts, named after the Carthaginian goddess of protection. Volunteers on the ground scan endangered sculptures, mosaics, and archaeological sites across Carthage and Tunisia — heritage spanning nearly 3,000 years — and a global community turns those scans into interactive digital artworks and VR/AR museum experiences that help Tunisians celebrate and share their cultural legacy with the world.",
     "Since its founding in 2025, the volunteer team of technologists, artists, and heritage enthusiasts has documented more than 80 artifacts across 20 sites, published openly on tanitxr.org and Sketchfab. Its multi-scan reconstruction of the El Jem Amphitheater — the largest to date — was featured by Niantic Spatial as a benchmark for large-scale reality capture.",
     "Beyond scanning, Tanit XR runs free education programs — including a Gaussian Splats course teaching anyone to capture and publish explorable 3D environments — because preserving heritage also means spreading the skills to do it."],
   facts=[('Founded', '2025 — nonprofit, volunteer-driven; core team of 7 plus volunteers worldwide'),
          ('Archive', '80+ artifacts, 20 sites, open access'),
          ('Partners', "Sketchfab Cultural Heritage Program, USF, INP, Tunisian Federation of Travel Agencies, AAAS, Unique Mappers"),
          ('Education', 'Free "Splats With Phones" course by Mark Jeffcock; research paper published in English, French &amp; Tunisian Arabic'),
          ('Hackathons', "Sponsored a Tunisian-heritage track at ImmerseGT 2026, Georgia Tech's 36-hour XR hackathon"),
          ('Recognition', 'Auggie Awards finalist, Best Societal Impact (AWE 2026); featured by Al Jazeera and Niantic Spatial')],
   embeds_heading='Watch &amp; explore in 3D',
   embeds=[dict(kind='linkedin', id='7488488682652495873', title='Niantic Spatial features our El Jem Amphitheater reconstruction'),
           dict(kind='sketchfab', id='e7bfb3b0767248f5b4064ca8c57dc6e4', title='Tanit Stela — Tophet of Salammbô, Carthage'),
           dict(kind='sketchfab', id='afe868bfb0454b0faa7d95d7961a5ba6', title='Corinthian Capital — Byrsa Hill, Carthage'),
           dict(kind='sketchfab', id='5766b06d2fc44df8bdc8319b11d49e7c', title='Bird of Prey Statue — Roman Villas of Carthage'),
           dict(kind='sketchfab', id='9027a243275242a19956a84a297d1e1e', title='Roman Column — Byrsa Hill, Carthage')],
   links=[('Donate (via fiscal sponsor FCIF)', 'https://donors.tuesday.app/campaign/73DO5'),
          ('Volunteer with Tanit XR', 'https://tanitxr.org/volunteer/'),
          ('Free course: Splats With Phones', 'https://tanitxr.org/photogrammetry-with-phones-by-mark-jeffcock/'),
          ('Full 3D archive on Sketchfab', 'https://sketchfab.com/TanitXR'),
          ('tanitxr.org', 'https://tanitxr.org'),
          ('Al Jazeera feature', 'https://www.aljazeera.net/amp/culture/2025/10/12/%D8%AA%D8%A7%D9%86%D9%8A%D8%AA-%D8%A5%D9%83%D8%B3-%D8%A2%D8%B1-%D9%85%D9%86%D8%B5%D8%A9-%D8%BA%D9%8A%D8%B1-%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9-%D8%AA%D9%88%D8%AB%D9%82'),
          ('Carthage Magazine', 'https://carthagemagazine.com/tanit-xr-preserving-tunisias-heritage-through-immersive-technology/')],
   gallery=[('tanit-archive', 'The open archive: 3D-scanned artifacts, free for everyone.'),
            ('tanit-museum-1', 'Sneak peek: the Tanit XR virtual museum.'),
            ('xrw-museum', 'Tanit XR pieces in the XR Women Global Museum.'),
            ('site-visit', 'Scouting sites across Tunisia.'),
            ('site-column', 'Ancient columns, documented before they erode.'),
            ('carthage-mag', 'Tanit XR featured in Carthage Magazine.')]),

 dict(slug='shadows-of-tomorrow', title='Shadows of Tomorrow', category='Climate · XR Installation',
   img='heat', alt='Ines Said at the HEAT exhibition wall for Shadows of Tomorrow',
   card='XR climate installation where holding hands transforms a damaged world into a restored one. Excellence Award at the GFAA Biennial; AWE XR Prize MVP finalist.',
   chips=['Body tracking', 'Unity', '!Excellence Award'],
   paras=[
     "Shadows of Tomorrow is an extended-reality climate installation that uses body tracking to place viewers' silhouettes inside climate data. Alone, you see a climate-damaged world; the moment two people hold hands, the scene transforms into a restored one — collective action, made literal.",
     "The piece received an Excellence Award at the GFAA Biennial, presented by Miami's Chief Heat Officer Jane Gilbert and climate author Jeff Goodell, and ran continuously for three months in the gallery.",
     "It has been shown at Parsons School of Design in New York City, MIT Reality Hack in Boston, and Ringling College in Sarasota, and advanced to the MVP finalist stage of the AWE XR Prize Challenge."],
   facts=[('Award', "Excellence Award — GFAA Biennial, presented by Miami's Chief Heat Officer"),
          ('Finalist', 'AWE XR Prize Challenge — MVP'),
          ('Shown at', 'Parsons (NYC), MIT Reality Hack (Boston), Ringling College (Sarasota)')],
   links=[], gallery=[('heat-door', 'The HEAT exhibition — three months of continuous operation.')]),

 dict(slug='smithsonian-futures', title='Smithsonian FUTURES — Future of Energy & Water', category='Museum · Immersive',
   img='futures-wide', alt='The Smithsonian FUTURES exhibition hall',
   card="Immersive installation co-created for the Smithsonian's landmark FUTURES exhibition in Washington, D.C. — a show that welcomed 600,000+ visitors.",
   chips=['Smithsonian', 'VR', 'Sustainability'],
   paras=[
     "For the Smithsonian's FUTURES exhibition — the Institution's landmark 175th-anniversary show in Washington, D.C. — I co-created the Future of Energy and Water immersive experience with the team at Froliq.",
     "The installation invites visitors to explore how energy and water systems could work in a sustainable future, blending art, technology, and environmental storytelling into an interactive experience. More than 10,000 visitors stepped through the experience itself, within an exhibition that welcomed over 600,000 people."],
   facts=[('Venue', 'Smithsonian Arts + Industries Building, Washington, D.C.'),
          ('Exhibition', 'FUTURES — 600,000+ visitors'),
          ('Experience', '10,000+ direct participants')],
   links=[('Oracle: a virtual journey with the Smithsonian', 'https://www.oracle.com/utilities/opower-energy-efficiency/future-of-energy-and-water-part-1/'),
          ('Smithsonian FUTURES announcement', 'https://www.si.edu/newsdesk/releases/smithsonian-debut-groundbreaking-futures-exhibition-its-175th-anniversary')],
   gallery=[]),

 dict(slug='oracle-connected-hub', title='Oracle Connected Hub', category='Energy · Enterprise AR',
   img='oracle-booth', alt='Ines Said demonstrating the Oracle Connected Hub grid simulator in a headset',
   card="The digital-twin AR apps for Oracle's Connected Hub — a working scale model of a neighborhood, with real solar panels and laser-lit power lines, brought to life in augmented reality.",
   chips=['Mobile AR', 'Quest 3', 'Vision Pro', 'Digital twin'],
   paras=[
     "Oracle's Connected Hub is a physical scale model of a working neighborhood — and it really works: real solar panels generate electricity, laser-lit fibre-optic power lines show live power flow, a wind turbine spins, batteries charge and discharge, EVs plug in, and 16 smart homes glow with the status of their meters, thermostats, and devices — all connected to Oracle's real utility-management software, so what happens in the model happens in the software, live.",
     "At Froliq, I build the digital-twin layer: the family of AR applications that bring the neighborhood to life. Point a device at the model — or open the fully digital version anywhere in the world — and animated overlays show energy flowing through the grid, outages being predicted and resolved, EVs charging with real-time billing, and solar and wind responding to the network. It turns invisible infrastructure into something you can watch, touch, and play with.",
     "The app family spans iPad AR, Windows, Meta Quest 3 mixed-reality passthrough, and Apple Vision Pro, and travels with the hubs to the industry's biggest stages — DISTRIBUTECH (Orlando and Dallas), Oracle Edge, Oracle CloudWorld, and the Energy Thought Summit — reaching thousands of utility professionals.",
     "It's my favorite kind of project: the same instinct as my heritage work, pointed at the future instead of the past. Complex systems people can't normally see, made touchable."],
   facts=[('Client', 'Oracle Utilities, with Froliq'),
          ('Role', 'Lead XR Developer — the AR digital-twin app family'),
          ('Platforms', 'iPad AR, Windows, Meta Quest 3 passthrough, Apple Vision Pro'),
          ('Shown at', 'DISTRIBUTECH, Oracle Edge, Oracle CloudWorld, Energy Thought Summit')],
   links=[], gallery=[('oracle-demo', 'Demoing the grid simulator on the conference floor.'),
                      ('ets-stage', 'Presenting the work on the Energy Thought Summit main stage.')]),

 dict(slug='nypa-vision-pro', title='NYPA Grid Experience on Apple Vision Pro', category='Energy · Spatial Computing',
   img=None, alt='', ph=('visionOS', 'Apple Vision Pro', 'lav'),
   card='A native visionOS energy-grid experience built for the New York Power Authority — a spatial cousin of the Connected Hub, living as a hologram in the room.',
   chips=['visionOS', 'Unity PolySpatial'],
   paras=[
     "For the New York Power Authority, I built a native Apple Vision Pro app with Unity PolySpatial — a spatial-computing take on the same idea as the Oracle Connected Hub, but its own application, designed for NYPA.",
     "The energy-grid model lives in a bounded volume in the room — stakeholders walk around it, lean into it, and interact with grid scenarios using only their eyes and hands, delivered to testers via TestFlight.",
     "It's an earlier-stage experience than the Connected Hub family, but it answered a question worth asking out loud: what does grid visualization feel like when the computer disappears entirely?"],
   facts=[('Client', 'New York Power Authority'), ('Platform', 'Apple Vision Pro (visionOS)'),
          ('Stack', 'Unity PolySpatial, RealityKit')],
   links=[], gallery=[]),

 dict(slug='vistra-tour', title='Vistra Energy Hazard Tour', category='Safety · WebXR',
   img=None, alt='', ph=('WebXR', 'Power plant tour', 'blush'),
   card='A guided virtual safety tour of the Vistra Midlothian power plant — four interactive hazard zones, running in any browser and in VR.',
   chips=['WebXR', 'Needle Engine', 'Unity'],
   paras=[
     "A guided, single-player virtual tour of the Vistra Midlothian power plant: four hazard zones, each with interactive storytelling that teaches what the hazard is and how to stay safe around it. The plant's enclosures are fully modeled, animated, and functional — this isn't a slideshow, it's the plant, working.",
     "The tour serves multiple audiences at once: internal safety training, stakeholder engagement, and career-fair buzz — and it's used by plant managers, directors, and leaders at Vistra.",
     "Originally built for a dedicated VR platform, it was rebuilt for the open web with Unity and Needle Engine — so it now runs in any browser, on phones and laptops, and in VR headsets, with no installation required."],
   facts=[('Client', 'Vistra'), ('Used by', 'Plant managers, directors, and leaders'),
          ('Use cases', 'Safety training, stakeholder engagement, career fairs'),
          ('Platform', 'Web, mobile, and WebXR (VR headsets) — Unity + Needle Engine')],
   links=[], gallery=[]),

 dict(slug='froliq-minigames', title='Froliq VR Mini-Game Series', category='STEM Education · VR',
   img=None, alt='', ph=('STEM &times; VR', 'Educational games', 'lav'),
   card='VR games that teach energy and the environment: sort waste in Recyclotopia, audit home energy in BungaLoad, power towns with wind in Fantastic Winds.',
   chips=['VR', 'Unity', 'Education'],
   paras=[
     "A series of VR mini-games for energy and environmental education: race a conveyor belt sorting waste into recycling bins in Recyclotopia (levels get faster and add more bins every minute), hunt down energy-wasting lights, appliances, and leaky faucets room-by-room through a virtual home in BungaLoad, and physically fan wind turbines to power up a town in Fantastic Winds — watching buildings light up as the blades spin.",
     "The games connect through a Mario Party-style VR lobby with three doors, a live leaderboard with gold-silver-bronze trophies, and a player profile that tracks everything across games: items recycled, kilowatts saved, houses powered, and facts discovered — replay enough and you earn statuses like \"Efficiency Expert.\"",
     "Each game teaches one idea that sticks: my sorting choice matters; small savings add up room by room; X turbines spinning equals Y homes powered. The suite has been played at career fests, Texas schools, and workforce-development events, designed for stationary point-and-click play so anyone can pick it up."],
   facts=[('Studio', 'Froliq'), ('Platform', 'Standalone VR headsets, stationary play'),
          ('Played at', 'Career fests, Texas schools, workforce events'),
          ('Design', 'Shared lobby, live leaderboard, cross-game player stats')],
   links=[], gallery=[]),

 dict(slug='sustainaball', title='Sustainaball', category='STEM Education · Interactive AR',
   img='froliq-playground', alt='The Froliq team with the Sustainaball projection soccer game at the AWE playground',
   card='A projection-based interactive soccer game with motion detection — kick a real ball at projected sustainability challenges. Played by 100+ students and showcased at the AWE 2026 playground.',
   chips=['Projection AR', 'Motion detection', '!AWE playground'],
   paras=[
     "Sustainaball is a projection-based interactive soccer game: a real ball, a projected field, and motion detection that turns every kick into a sustainability challenge. It's multiplayer-friendly and physical — the rare educational game that gets a whole room moving.",
     "We built it at Froliq for energy and environmental education, and it's been a hit with everyone from 7th graders to college students — more than 100 students have played. It was also our showcase at the Augmented World Expo 2026 playground, where the XR industry lined up to kick a ball at clean-energy trivia.",
     "Kelly and I had entirely too much fun building this one."],
   facts=[('Studio', 'Froliq'), ('Tech', 'Projection mapping + motion detection'),
          ('Reach', '100+ students, grades 7 through college; AWE 2026 playground')],
   links=[], gallery=[]),

 dict(slug='stevie', title='StEVie', category='STEM Education · Mobile AR',
   img=None, alt='', ph=('StEVie', 'AR energy storytelling', 'lav'),
   card='Location-based augmented-reality storytelling about energy in real time — accessible anywhere, on the devices students already have.',
   chips=['Mobile AR', 'Storytelling'],
   paras=[
     "StEVie is an augmented-reality storytelling experience about energy — location-based, interactive, and accessible anywhere, because it runs on the phones and tablets students already carry.",
     "Around 30 young people from the E4 youth community have played it so far, following energy stories that unfold in real time in the world around them. It's part of the same Froliq belief that runs through all our education work: meet learners where they are, with the devices they have."],
   facts=[('Studio', 'Froliq'), ('Tech', 'Location-based mobile AR'),
          ('Community', 'E4 youth program')],
   links=[], gallery=[]),

 dict(slug='exelon-stem', title='Exelon STEM Program', category='Workforce · VR Simulations',
   img=None, alt='', ph=('STEM', 'Six utilities', 'blush'),
   card="XR simulations of real utility careers for Exelon's five-year STEM program across all six of its utilities — from career fairs to classrooms.",
   chips=['VR', 'Workforce development'],
   paras=[
     "Exelon runs a five-year STEM program across all six of its utilities, and Froliq builds the immersive layer: XR and VR simulations that let students step into real utility roles — the jobs that keep the lights on — at career fairs and in classrooms.",
     "The program pairs educator and community partnerships with hands-on XR experiences, creating a proven pathway from a student's first STEM exposure to a real career in energy. It's workforce development that starts with wonder."],
   facts=[('Client', 'Exelon, with Froliq'), ('Scale', 'Five-year program, six utilities'),
          ('Settings', 'Career fairs, classrooms, community events')],
   links=[], gallery=[]),

 dict(slug='nuclear-capture', title='Nuclear Plant Reality Capture', category='Energy · 3D Scanning',
   img='portalcam', alt='Ines Said and colleague with the PortalCam LiDAR scanner',
   card='LiDAR-scanning the Davis-Besse nuclear power plant — turbine deck to cooling tower — and rendering it as Gaussian splats for training in web, VR, and AR.',
   chips=['LiDAR', 'Gaussian splats', 'Training'],
   paras=[
     "Some places are too critical, too controlled, or too complex to train in casually — a nuclear power plant is all three. At Froliq, we 3D-scanned facilities at the Davis-Besse nuclear power plant, including the turbine deck and cooling tower, using the PortalCam LiDAR scanner.",
     "The scans render into Gaussian splats — the same technique behind Tanit XR's heritage captures — producing photoreal, explorable environments that can be deployed to web, VR, or AR for training and visual simulation. Staff can learn a space before they ever set foot in it.",
     "It's the perfect symmetry of my work: the exact pipeline I use to preserve 3,000-year-old amphitheaters, pointed at the most modern infrastructure there is."],
   facts=[('Client project', 'Froliq — Davis-Besse Nuclear Power Station'),
          ('Captured', 'Turbine deck, cooling tower, and other facilities'),
          ('Pipeline', 'PortalCam LiDAR → Gaussian splats → web/VR/AR')],
   links=[], gallery=[]),

 dict(slug='covid-reflections', title='Covid Reflections', category='Public Health · AR Public Art',
   img='covid-truck', alt='Covid Reflections AR installation presented outdoors beside a mobile vaccine clinic',
   card='AR public art paired with mobile health clinics, touring Florida, California, and Japan — 200+ people received check-ups alongside the installation.',
   chips=['Mobile AR', 'Public art'],
   paras=[
     "Covid Reflections is an augmented-reality public art installation that toured Florida, California, and Japan, pairing immersive art with real public-health outreach.",
     "In Florida, the installation traveled with health check-up and vaccination trucks — more than 200 people received check-ups alongside the artwork. The project was covered by ABC 20 WCJB, CBS4 News, and UF News, and the research behind it was published in ACM venues."],
   facts=[('Toured', 'Florida, California, Japan'),
          ('Impact', '200+ health check-ups at paired clinics'),
          ('Coverage', 'ABC, CBS, UF News; published in ACM')],
   links=[('UF News story', 'https://news.ufl.edu/2022/04/covid-reflections/')],
   embeds_heading='Watch',
   embeds=[dict(kind='vimeo', id='699905464', title='AR in Public Health Interactions — AI & Society Symposium'),
           dict(kind='youtube', id='PPh12oJ38rQ', title='The AR Minute with Nathan C — on Covid Reflections')],
   gallery=[('covid-outdoor', 'The AR installation beside a mobile clinic.')]),

 dict(slug='sparc', title='spARc', category='AR Animation · Research',
   img=None, alt='', ph=('spARc', 'AR animation tool', 'blush'),
   card='An immersive 3D animation tool that lets anyone animate in AR — two-handed controls, no rigging or skinning, and a radial time slider for precise keyframing.',
   chips=['AR', 'HCI research', '!Published research'],
   paras=[
     "3D animation brings games, films, and advertising to life — but traditional animation software is a wall of menus, rigging, and skinning that shuts beginners out. spARc is an immersive 3D animation tool that tears that wall down: you animate directly in augmented reality with a simple two-handed setup, no rigging or skinning required.",
     "Its interface was shaped by focus-group research, including a signature radial time slider — replacing the conventional horizontal timeline to reduce arm fatigue and make keyframe selection more precise in mid-air."],
   facts=[('Type', 'Immersive animation tool + HCI research'),
          ('Interface', 'Two-handed AR animating, radial time slider'),
          ('Designed with', 'Focus-group research')],
   links=[], gallery=[]),
]

def card_html(p, preview, prefix='p-', more='View project'):
    if p.get('img'):
        thumb = f'<div class="thumb"><img src="web/{p["img"]}.jpg" alt="{p["alt"]}" loading="lazy"></div>'
    else:
        big, small, tone = p['ph']
        thumb = f'<div class="thumb ph {tone}"><b>{big}</b><span>{small}</span></div>'
    ch = ''.join(f'<span class="chip{" blush" if c.startswith("!") else ""}">{c.lstrip("!")}</span>' for c in p['chips'])
    link = p.get('href') or href(prefix + p['slug'], preview)
    return (f'<a class="card" href="{link}"><div class="card-inner">{thumb}'
            f'<div class="card-body"><h3>{p["title"]}</h3><p>{p["card"]}</p>'
            f'<div class="chips">{ch}</div><span class="card-more">{more} &rarr;</span></div></div></a>')

def body_detail(p, preview, back_page='projects', back_label='All projects'):
    hero = ''
    if p.get('img'):
        hero = f'<div class="detail-hero"><img src="web/{p["img"]}.jpg" alt="{p["alt"]}"></div>'
    paras = ''.join(f'<p>{t}</p>' for t in p['paras'])
    facts = ''.join(f'<li><b>{k}</b> — {v}</li>' for k, v in p['facts'])
    links = ''
    if p['links']:
        links = ('<h3 style="margin-top:20px">Links</h3><ul>' +
                 ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in p['links']) + '</ul>')
    gallery = ''
    if p['gallery']:
        figs = ''.join(f'<figure><img src="web/{g}.jpg" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
                       for g, cap in p['gallery'])
        gallery = f'<div class="gallery">{figs}</div>'
    emb = embeds_block(p.get('embeds'), preview, p.get('embeds_heading'))
    return f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">{p['category']}</p>
    <h1>{p['title']}</h1>
  </div>
  {hero}
  <div class="detail-grid">
    <div class="prose">{paras}</div>
    <div class="fact-card"><h3>At a glance</h3><ul>{facts}</ul>{links}</div>
  </div>
  {emb}
  {gallery}
  <a class="backlink" href="{href(back_page, preview)}">&larr; {back_label}</a>
</div>
"""

# ---------------- awards ----------------
AWARDS = [
 dict(slug='auggie-finalist', title='Auggie Awards Finalist — Best Societal Impact',
   category='Augmented World Expo · 2026', img='auggie-finalist',
   alt='Tanit XR team with the Auggie Awards 2026 Finalist graphic',
   card="The XR industry's most recognized awards. Tanit XR made the finals in Best Societal Impact — a category with its highest-ever number of nominations.",
   chips=['Tanit XR', '!2026'],
   paras=[
     "The Auggie Awards at Augmented World Expo are the XR industry's most recognized honors — and I've been watching them since I was a student, dreaming of being on that stage. In January 2026, I put the Auggies on my vision board. By May, Tanit XR was announced as a finalist for Best Societal Impact.",
     "The category hit its highest nomination count ever that year, full of projects in accessibility, education, and healthcare — which made the finalist spot mean even more. The community voted, and on ceremony night at AWE in Long Beach, we got one of the loudest cheers in the room.",
     "We didn't take the trophy home — but the next day a whale jumped out of the ocean in front of me, and I chose to take that as a sign. We'll be back."],
   facts=[('Category', 'Best Societal Impact'), ('For', 'Tanit XR'), ('Year', '2026, Long Beach, CA')],
   links=[('Official finalists announcement', 'https://www.awexr.com/blog/1382-2026-auggie-awards-finalists-announced')],
   gallery=[('vision-board', 'January 2026: the Auggies on the vision board.'),
            ('auggie-night', 'Auggie Awards night at AWE.'),
            ('awe-entrance', 'With the team at AWE 2026.')]),

 dict(slug='ee-30-under-30', title='EE 30 Under 30 — Class of 2025',
   category='NAAEE · 2025', img='ee30',
   alt='NAAEE EE 30 Under 30 announcement graphic featuring Ines Said',
   card='Named one of 30 environmental-education leaders under 30 worldwide by the North American Association for Environmental Education.',
   chips=['Environmental education', '!Class of 2025'],
   paras=[
     "Each year, the North American Association for Environmental Education (NAAEE) selects 30 leaders under 30 from around the world who are changing how people learn about the environment. I was honored to be named to the Class of 2025 for using immersive technology to turn environmental and cultural education into experiences people can feel.",
     "My selection story starts on a Florida beach, where I realized that what looked like sand was actually fragments of microplastic. That moment cemented my belief that direct observation — actually seeing and feeling a problem — changes behavior in a way statistics never will. It's the idea behind Shadows of Tomorrow, behind the Froliq education games, and behind Tanit XR's link between climate change and disappearing heritage.",
     "Being part of this community of educators, scientists, and artists has been one of the most energizing parts of my year — and the story came full circle fast: in 2026, NAAEE invited me back as a judge, helping select the next class of EE 30 Under 30 leaders."],
   facts=[('Organization', 'North American Association for Environmental Education'),
          ('Class', '2025 honoree'), ('And then', 'Judge for the Class of 2026'),
          ('For', 'XR for environmental & cultural education')],
   links=[('Her EE 30 Under 30 profile', 'https://naaee.org/people/ines-said')],
   gallery=[('ee30-class', 'Meet the Class of 2025.')]),

 dict(slug='gfaa-excellence', title='Excellence Award — GFAA Biennial',
   category='Gainesville Fine Arts Association', img='heat',
   alt='Ines Said at the HEAT exhibition wall for Shadows of Tomorrow',
   card="For Shadows of Tomorrow — presented by Miami's Chief Heat Officer Jane Gilbert and climate author Jeff Goodell at the HEAT exhibition.",
   chips=['Shadows of Tomorrow', '!Excellence Award'],
   paras=[
     "Shadows of Tomorrow, my XR climate installation, received the Excellence Award at the Gainesville Fine Arts Association Biennial — presented by two people whose work on extreme heat I deeply admire: Jane Gilbert, Miami's (and the world's first) Chief Heat Officer, and Jeff Goodell, author of 'The Heat Will Kill You First.'",
     "The installation uses body tracking to place viewers' own silhouettes inside climate data: alone, you stand in a climate-damaged world; hold someone's hand, and the scene transforms into a restored one. It ran continuously for three months in the gallery as part of the HEAT exhibition.",
     "Having the award handed over by the people leading the real-world fight against extreme heat made it the most meaningful recognition this piece has received."],
   facts=[('For', 'Shadows of Tomorrow'), ('Presented by', "Jane Gilbert (Miami's Chief Heat Officer) and author Jeff Goodell"),
          ('Exhibition', 'HEAT — three months of continuous operation')],
   links=[('Gainesville Fine Arts Association', 'https://gainesvillefinearts.org/')],
   gallery=[('heat-door', 'The HEAT exhibition.')]),

 dict(slug='ieee-best-paper', title='Best Paper Award — IEEE ISEC',
   category='IEEE Integrated STEM Education Conference · 2023', img='vr-portrait',
   alt='Ines Said wearing a VR headset',
   card='For "Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts & Sciences," with Dr. Angelos Barmpoutis and Wenbin Guo.',
   chips=['Research', 'VR education'],
   paras=[
     "At the University of Florida's Digital Worlds Institute, I worked with Professor Angelos Barmpoutis and Wenbin Guo on a question I care about a lot: how do you teach emerging technology in a way that actually sticks? The answer we studied — don't hand students a finished game engine; have them build mini VR game engines themselves.",
     "Our paper, “Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts &amp; Sciences,” was presented at the 2023 IEEE Integrated STEM Education Conference, where it received a Best Paper Award.",
     "That building-to-learn philosophy runs through everything I've done since — the VR education games at Froliq, the scanning workshops at Tanit XR, and the courses where volunteers learn photogrammetry by documenting real heritage."],
   facts=[('Paper', '"Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts & Sciences"'),
          ('Authors', 'A. Barmpoutis, W. Guo, I. Said'),
          ('Venue', '2023 IEEE Integrated STEM Education Conference (ISEC)')],
   links=[('The paper on IEEE Xplore', 'https://ieeexplore.ieee.org/document/10402239'),
          ('ResearchGate profile', 'https://www.researchgate.net/profile/Ines-Said-2')],
   gallery=[]),

 dict(slug='awe-xr-prize', title='XR Prize Challenge — MVP Finalist',
   category='Augmented World Expo', img='heat-door',
   alt='Shadows of Tomorrow at the HEAT exhibition',
   card="Shadows of Tomorrow advanced to the MVP finalist stage of AWE's international XR Prize Challenge.",
   chips=['Shadows of Tomorrow', 'International'],
   paras=[
     "Augmented World Expo's XR Prize Challenge draws entries from around the world, and Shadows of Tomorrow advanced to the MVP finalist stage — international recognition for a piece that began as a local gallery installation.",
     "Reaching the finalist stage put the project in front of the global XR community and opened the doors that later took the work to MIT Reality Hack, Parsons, and Ringling College."],
   facts=[('Competition', 'AWE XR Prize Challenge'), ('Stage', 'MVP Finalist'), ('For', 'Shadows of Tomorrow')],
   links=[('Augmented World Expo', 'https://www.awexr.com/')],
   gallery=[]),

 dict(slug='hackathon-wins', title='Hackathon Wins — Google, IBM & MIT',
   category='MiDAS · Reality Hack', img='rh-printed-award',
   alt='Holding a 3D-printed statue award at MIT Reality Hack',
   card='A track record of hackathon wins backed by Google and IBM — plus an MIT Reality Hack tradition of printing our own awards.',
   chips=['MIT Reality Hack', '!Google & IBM'],
   paras=[
     "Through the University of Florida's MiDAS program, my cohort built a track record of hackathon success — wins supported by organizations including Google and IBM — turning weekend sprints into working immersive prototypes.",
     "The tradition continues at MIT Reality Hack, where I keep coming back for the community as much as the competition. In 2026, when the event got cut short, my teammates and I 3D-printed our own little award — because celebrating with your team is the point.",
     "Hackathons are where I test the fastest version of an idea. More than one project on this site started as a 48-hour prototype."],
   facts=[('Backed by', 'Google, IBM, and others'), ('Program', 'UF MiDAS — Digital Arts & Sciences'),
          ('Regular at', 'MIT Reality Hack, Boston')],
   links=[('UF: MiDAS cohort builds hackathon track record', 'https://arts.ufl.edu/in-the-loop/news/midas-cohort-builds-track-record-of-hackathon-success/')],
   gallery=[('rh-hack-table', 'Community hacking at MIT Reality Hack.'),
            ('rh-snow-1', 'Boston in January — worth it.')]),

 dict(slug='g4c-judge', title='Judge — Games for Change',
   category='Games for Change · Awards & Student Challenge', img='workshop',
   alt='Ines Said leading a classroom workshop',
   card='Invited to judge both the Games for Change Awards — the top honors for games with real-world impact — and their national Student Challenge.',
   chips=['Games for impact', 'Jury service'],
   paras=[
     "Games for Change is the home of games that take on real-world problems, and I've had the honor of judging on both sides of it: the Games for Change Awards, which recognize the best impact-driven games in the industry, and the Student Challenge, the largest student game-design competition in the U.S.",
     "Judging the industry awards means weighing work from studios around the world; judging the students means spotting the sparks — young people building games about climate, health, and their own communities. I love both for the same reason: it's a front-row seat to where games-for-impact is heading.",
     "It's also the mentorship side of my work in concentrated form — the same belief that drives the Froliq education games and Tanit XR's volunteer programs: people learn best by making, and games are a serious way to think about serious things."],
   facts=[('Organization', 'Games for Change'),
          ('Roles', 'Judge — Games for Change Awards; Judge — Student Challenge')],
   links=[('Games for Change', 'https://www.gamesforchange.org/')],
   gallery=[]),

 dict(slug='futures', title='Smithsonian FUTURES Exhibition',
   category='Smithsonian Institution', img='futures-wide',
   alt='The Smithsonian FUTURES exhibition hall',
   card="Co-created an installation for the Smithsonian's landmark 175th-anniversary exhibition — 600,000+ visitors in Washington, D.C.",
   chips=['Smithsonian', '600,000+ visitors'],
   href=None,  # filled below: links straight to the project page
   paras=[], facts=[], links=[], gallery=[]),
]

# ---------------- blog posts ----------------
POSTS = [
 dict(slug='scanning-in-minutes', title='Scanning in minutes, not days',
   date='September 2026', tag='Tools', img='portalcam',
   liurl='https://www.linkedin.com/feed/update/urn:li:activity:7500264787075956736/',
   imgcap='Testing the PortalCam by XGRIDS with Kelly at Froliq.',
   excerpt="We just got the PortalCam by XGRIDS at Froliq — and I'm amazed at how fast this technology is moving.",
   paras=[
     "We're so excited to finally have the PortalCam by XGRIDS! Kelly and I have been testing it at Froliq, and we can't wait to put it to work on our upcoming projects.",
     "What amazes me most is the pace of this technology. Just a couple of years ago, it used to take me days and days to scan a single spot. Now it's a matter of minutes.",
     "For heritage work, speed changes everything: more sites, more artifacts, more chances to document something before it's gone. If you've been using the PortalCam and have tips or suggestions, I'm happy to hear them!"]),

 dict(slug='sunken-city', title='Looking for a sunken city before breakfast',
   date='August 2026', tag='Tanit XR', img='neapolis-swim',
   liurl='https://www.linkedin.com/feed/update/urn:li:activity:7493771371995377664/',
   imgcap='Scanning the surface of the sea above Neapolis at 6 AM.',
   excerpt='We took a paddle boat out at 6 AM to look for the underwater ruins of ancient Neapolis — a Roman city 15 minutes from my house.',
   paras=[
     "We went looking for the underwater ruins of ancient Neapolis in Tunisia! Laura K. Harrison (archaeologist and digital heritage expert) and Caroline Nickerson (citizen-science leader) flew all the way from Florida, and we took a paddle boat out along the coast of Neapolis at 6 AM, hoping to catch a glimpse of the submerged city from the surface.",
     "For reference: there is nothing that points you to the ruins. We went out twice — but the second time, the water was so clear that we believe we could finally see them below us: fragments of roads, walls, and stairs from a coastal settlement that was once a hub for manufacturing garum, the Romans' beloved fermented fish sauce.",
     "Neapolis was destroyed by an earthquake in 365 AD. It sits near my hometown, Nabeul — a 15-minute walk from my house. Moments like this are why I love what we do at Tanit XR: Tunisia holds so many incredible stories, on land and underwater, and getting to share them with the world is the best part.",
     "(My GoPro broke the second it touched the water, so no underwater shots this time.)"],
   gallery=[('neapolis-2', 'Out on the water at 6 AM.'),
            ('neapolis-3', 'Scanning the surface for shapes below.'),
            ('neapolis-4', 'The expedition vessel, mermaid tail included.')]),

 dict(slug='tanit-xr-turns-one', title='Tanit XR turns one',
   date='August 2026', tag='Tanit XR', img='tanit-birthday',
   liurl='https://www.linkedin.com/feed/update/urn:li:activity:7492020739622006784/',
   imgcap='One year of Tanit XR.',
   excerpt='A year ago I started Tanit XR to preserve the Tunisian heritage I grew up with. Here is what a year of volunteers and phone scans can do.',
   paras=[
     "A year ago, I started Tanit XR to preserve the Tunisian heritage I grew up with. Volunteers on the ground scan endangered sites with their phones, and our global community turns those scans into XR preservation and education tools.",
     "We named it after Tanit, the Carthaginian goddess of protection — because that's what we do.",
     "So far, the leadership team and I have self-funded everything, with a few small grants here and there. If you'd like to support the work, you can donate through our fiscal sponsor, the Florida Community Innovation Foundation — or just join us. Love history? Curious about XR? All are welcome.",
     "Honestly, I already got my wish: I do what I love with people I care about."]),

 dict(slug='auggie-finalist-whale', title="We didn't win the Auggie — but I saw a whale",
   date='June 2026', tag='Field notes', img='auggie-night',
   imgcap='Auggie Awards night at AWE 2026.',
   excerpt='Tanit XR was a finalist for Best Societal Impact at the Auggie Awards. We got one of the loudest cheers in the room — and the next day, the ocean delivered.',
   paras=[
     "It was an honor for the Tanit XR team to be finalists at the Auggie Awards this year at AWE, in the Best Societal Impact category. We didn't win — but I can attest we got one of the loudest cheers in the room.",
     "And then, the next day, a giant whale fully jumped out of the ocean in front of me. Witnessing that has long been on my bucket list. I'm taking it as a sign, and we'll see you at the Auggies again next year!",
     "Thank you to everyone who voted for Tanit XR, and to everyone who came up at AWE to say they've been following our work — especially the community at XR Women Global. One of our amazing volunteers, Margarita Johnson, joined me on stage to co-present our talk on the scan-to-XR pipeline, and Kelly and I had the best time running Froliq's sustainability soccer game on the playground.",
     "AWE was incredible this year. Already can't wait for the next one."],
   gallery=[('awe-entrance', 'Arriving at AWE 2026 in Long Beach.'),
            ('froliq-playground', 'The Froliq crew at the playground — come play soccer with us.')]),

 dict(slug='el-jem-colosseum', title='Presenting inside a Roman colosseum',
   date='April 2026', tag='Tanit XR', img='el-jem',
   imgcap='The El Jem Amphitheater — our largest reconstruction, and my stage for a day.',
   excerpt="I couldn't believe I was about to present — inside the El Jem Amphitheater, at a conference where more than half the researchers were women.",
   paras=[
     "I couldn't believe I was about to present — inside a colosseum! I spoke about Tanit XR at the El Jem International Conference, standing inside the very amphitheater our team had scanned for our largest 3D reconstruction to date.",
     "There's something surreal about showing a digital twin of a monument while standing inside the original. The El Jem reconstruction — stitched together from many scans without losing architectural detail — was later featured by Niantic Spatial as a benchmark for large-scale reality capture.",
     "Our paper explored how digital documentation, XR, and citizen science can support community-driven heritage preservation in Tunisia and beyond — and we published it in English, French, and Tunisian Arabic, so the communities it's about can actually read it.",
     "My sister came with me, and one of my favorite details: more than half the researchers presenting at the conference were women. The future of digital heritage in Tunisia looks bright."],
   gallery=[('eljem-conf', 'At the El Jem conference with my sister.')]),

 dict(slug='virtual-museum-sneak-peek', title='A sneak peek at the Tanit XR virtual museum',
   date='Spring 2026', tag='Tanit XR', img='tanit-museum-1',
   imgcap='Inside the Tanit XR virtual museum.',
   excerpt='A virtual space where the artifacts we scan go on display — wander Tunisian streets and courtyards, from anywhere in the world.',
   paras=[
     "A little sneak peek of our Tanit XR virtual museum! This space will display the artifacts and places our volunteers have scanned across Tunisia — not in sterile display cases, but in the kind of whitewashed streets and courtyards they belong to.",
     "Visitors explore together from anywhere in the world. A kid in Tunis, a researcher in Boston, and a grandmother in Nabeul can wander the same alleys and stand in front of the same 3,000-year-old pieces at the same time.",
     "Our scanned artifacts are also on display in the XR Women Global Museum — heritage preservation and community, hand in hand."],
   gallery=[('tanit-museum-2', 'Your guide through the museum.'),
            ('tanit-museum-3', 'Courtyards built for wandering.'),
            ('tanit-museum-4', 'Streets modeled on the real Tunisia.'),
            ('xrw-museum', 'Tanit XR pieces in the XR Women Global Museum.')]),

 dict(slug='storm-revealed-ruins', title='The storm that revealed 2,000-year-old ruins',
   date='February 2026', tag='Field notes', img='storm-ruins-1',
   imgcap='After the storm: newly exposed ruins on the coast near Nabeul.',
   excerpt="My hometown flooded in Tunisia's worst rainfall in 70 years. When the water receded, the coast had given something back.",
   paras=[
     "The last few days were stressful and heartbreaking: my hometown was severely flooded in Tunisia's worst rainfall in 70 years. Schools closed across the capital and the coastal towns, and I watched from afar as the streets I grew up on filled with water.",
     "And then, when the storm passed, something unexpected: the floods had revealed a new archaeological site near my house, dating back more than 2,000 years — walls and structures no one alive had ever seen.",
     "That's the double edge of climate change for heritage: the same storms that destroy ancient sites sometimes expose new ones, briefly, before erosion takes them. It's exactly why Tanit XR exists — to scan what the earth shows us before it disappears again."],
   gallery=[('storm-ruins-2', 'Structures exposed by the receding water.')]),

 dict(slug='mit-reality-hack-2026', title='Snow, friends, and a 3D-printed award',
   date='January 2026', tag='Field notes', img='rh-snow-1',
   imgcap='Boston in January.',
   excerpt="MIT Reality Hack got cut short this year — so my team printed our own award. Hacking is better with friends.",
   paras=[
     "MIT Reality Hack got cut short this year — but wow, what an amazing time. I came back to Boston for the community hack with Caroline, her first Reality Hack, and hacking really is better with friends.",
     "When the event ended early, my teammates and I refused to leave without a ceremony: we 3D-printed ourselves our own little award. It is possibly my favorite trophy on the shelf.",
     "Between the snow, the late-night prototyping, and the people who come back year after year, Reality Hack remains my favorite way to start a year in XR."],
   gallery=[('rh-printed-award', 'The prestigious self-printed award.'),
            ('rh-hack-table', 'Community hacking.'),
            ('rh-snow-2', 'Worth every snowflake.')]),
]

def post_card(p, preview):
    return (f'<a class="card" href="{href("b-"+p["slug"], preview)}"><div class="card-inner">'
            f'<div class="thumb"><img src="web/{p["img"]}.jpg" alt="{p.get("imgcap", p["title"])}" loading="lazy"></div>'
            f'<div class="card-body"><h3>{p["title"]}</h3><p>{p["excerpt"]}</p>'
            f'<div class="chips"><span class="chip">{p["tag"]}</span><span class="chip blush">{p["date"]}</span></div>'
            f'<span class="card-more">Read the story &rarr;</span></div></div></a>')

def body_blog(preview):
    items = ''.join(post_card(p, preview) for p in POSTS)
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">Blog</p>
  <h1>Notes from the field</h1>
  <p class="sub">Stories from scanning trips, exhibitions, and life between Tunisia and the U.S.</p>
</div></div>
<section class="block" style="padding-top:36px"><div class="wrap">
  <div class="cards two">{items}</div>
</div></section>
<div class="band blush"><div class="wrap" style="text-align:center">
  <h2 class="sec-title" style="margin-bottom:10px">Art, XR &amp; Impact Opportunities</h2>
  <p style="max-width:56ch;margin:0 auto 24px">My weekly round-up of grants, residencies, fellowships,
  and open calls at the intersection of creative practice and technology.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn" href="{NEWSLETTER_URL}">Subscribe on LinkedIn</a>
    <a class="btn ghost" href="{href('opportunities', preview)}">Browse the deadline board</a>
  </div>
</div></div>
"""

def body_post(p, preview):
    hero = ''
    if p.get('img'):
        hero = (f'<div class="detail-hero"><img src="web/{p["img"]}.jpg" alt="{p.get("imgcap", p["title"])}"></div>'
                f'<p style="font-size:.8rem;color:var(--muted);margin:10px 0 0">{p.get("imgcap", "")}</p>')
    paras = ''.join(f'<p>{t}</p>' for t in p['paras'])
    gallery = ''
    if p.get('gallery'):
        figs = ''.join(f'<figure><img src="web/{g}.jpg" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
                       for g, cap in p['gallery'])
        gallery = f'<div class="gallery">{figs}</div>'
    emb = embeds_block(p.get('embeds'), preview)
    return f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">{p['tag']} &middot; {p['date']}</p>
    <h1>{p['title']}</h1>
  </div>
  {hero}
  <div class="detail-grid" style="grid-template-columns:1fr;max-width:720px">
    <div class="prose">{paras}</div>
  </div>
  {emb}
  {gallery}
  {f'<p style="margin:36px 0 0"><a href="{p["liurl"]}" style="font-size:.85rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase">Read the original post on LinkedIn &rarr;</a></p>' if p.get('liurl') else ''}
  <a class="backlink" href="{href('blog', preview)}">&larr; All posts</a>
</div>
"""

# ---------------- page bodies ----------------

SQUIGGLE = ('<svg class="squiggle" viewBox="0 0 1200 22" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0 11 Q 25 0, 50 11 T 100 11 T 150 11 T 200 11 T 250 11 T 300 11 T 350 11 T 400 11 '
            'T 450 11 T 500 11 T 550 11 T 600 11 T 650 11 T 700 11 T 750 11 T 800 11 T 850 11 T 900 11 '
            'T 950 11 T 1000 11 T 1050 11 T 1100 11 T 1150 11 T 1200 11"/></svg>')

def body_home(preview):
    featured = ''.join(card_html(p, preview) for p in PROJECTS[:3])
    return f"""
<div class="photo-band"><div class="strip">
  <figure><img src="web/statue-pose.jpg" alt="Ines Said matching poses with an ancient statue at a Tunisian dig site"></figure>
  <figure><img src="web/mosaic-portrait.jpg" alt="Ines Said in front of an ancient mosaic wall"></figure>
  <figure><img src="web/ets-fireside.jpg" alt="Ines Said speaking on the Energy Thought Summit stage"></figure>
</div></div>

<div class="intro-home">
  <p class="kicker">XR Immersive Artist &amp; Technologist</p>
  <h1>Hello, I'm <em>Ines Said</em>.</h1>
  <p class="lede">I grew up a fifteen-minute walk from the ruins of Roman Neapolis in Tunisia —
  now I preserve places like it in 3D. Founder of <strong>Tanit XR</strong>, Lead XR Developer
  at <strong>Froliq</strong>, and maker of installations on heritage and climate shown
  everywhere from the Smithsonian to MIT.</p>
  <div class="btn-row">
    <a class="btn" href="{href('projects', preview)}">Explore my work</a>
    <a class="btn ghost" href="{href('about', preview)}">More about me</a>
  </div>
</div>

<div class="band lav"><div class="wrap"><div class="stats">
  <a href="{href('p-smithsonian-futures', preview)}"><b>600,000+</b><span>visitors to the Smithsonian FUTURES exhibition featuring her installation</span></a>
  <a href="https://naaee.org/people/ines-said"><b>30 Under 30</b><span>EE 30 Under 30, Class of 2025 — NAAEE</span></a>
  <a href="{href('projects', preview)}"><b>11,000+</b><span>people reached in 2025 across 40+ events</span></a>
  <a href="https://www.awexr.com/blog/1382-2026-auggie-awards-finalists-announced"><b>Auggie Finalist</b><span>Best Societal Impact — Tanit XR, AWE 2026</span></a>
  <a href="https://www.linkedin.com/in/inessaid/"><b>7,000+</b><span>followers on LinkedIn — doubled in the past year</span></a>
  <a href="{NEWSLETTER_URL}"><b>167K</b><span>impressions this past year, 30,000+ people reached</span></a>
  <a href="{href('speaking', preview)}"><b>1 in 4</b><span>of her audience is a founder, executive, or director</span></a>
  <a href="{href('about', preview)}"><b>3 languages</b><span>presenting in English, Arabic &amp; French</span></a>
</div>
<p style="text-align:center;margin:44px 0 0;font-size:.78rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)">As featured in</p>
<p style="text-align:center;margin:10px 0 0;font-family:"Yeseva One",serif;font-weight:600;font-size:1.05rem">
  <a href="https://www.aljazeera.net/amp/culture/2025/10/12/%D8%AA%D8%A7%D9%86%D9%8A%D8%AA-%D8%A5%D9%83%D8%B3-%D8%A2%D8%B1-%D9%85%D9%86%D8%B5%D8%A9-%D8%BA%D9%8A%D8%B1-%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9-%D8%AA%D9%88%D8%AB%D9%82" style="color:var(--ink)">Al Jazeera</a> &nbsp;&middot;&nbsp;
  <a href="https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873/" style="color:var(--ink)">Niantic Spatial</a> &nbsp;&middot;&nbsp;
  <a href="https://www.wcjb.com/2022/04/11/university-florida-launches-covid-reflections-project-utilizing-ai-increase-vaccination/" style="color:var(--ink)">ABC</a> &nbsp;&middot;&nbsp;
  <a href="https://mycbs4.com/news/local/university-of-florida-vaccine-exhibit" style="color:var(--ink)">CBS</a> &nbsp;&middot;&nbsp;
  <a href="https://news.ufl.edu/2022/04/covid-reflections/" style="color:var(--ink)">UF News</a> &nbsp;&middot;&nbsp;
  <a href="https://carthagemagazine.com/tanit-xr-preserving-tunisias-heritage-through-immersive-technology/" style="color:var(--ink)">Carthage Magazine</a>
</p>
</div></div>

{SQUIGGLE}

<section class="block"><div class="wrap">
  <h2 class="sec-title">Featured work</h2>
  <p class="sec-sub">Heritage, climate, and public health — built in augmented and virtual reality.</p>
  <div class="cards">{featured}</div>
  <p style="margin:34px 0 0"><a class="btn ghost" href="{href('projects', preview)}">See all projects</a></p>
</div></section>

{SQUIGGLE}

<div class="band soft"><div class="wrap">
  <h2 class="sec-title">Latest</h2>
  <p class="sec-sub">Recent milestones and field notes.</p>
  <ul class="list">
    <li><div><span class="t"><a href="{href('b-auggie-finalist-whale', preview)}">Auggie Awards finalist — Best Societal Impact</a></span><div class="d">Tanit XR was a finalist at the XR industry's top awards at Augmented World Expo, with one of the loudest cheers in the room.</div></div><span class="who">AWE &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873/">El Jem Amphitheater — largest reconstruction to date</a></span><div class="d">Tanit XR's multi-scan 3D reconstruction of the iconic Roman amphitheater was featured by Niantic Spatial as a benchmark for large-scale reality capture — watch their video.</div></div><span class="who">Niantic Spatial</span></li>
    <li><div><span class="t"><a href="https://tanitxr.org/photogrammetry-with-phones-by-mark-jeffcock/">Free course: Splats With Phones</a></span><div class="d">A free 6-week live course with Tanit XR, led by XR educator Mark Jeffcock — 3D scanning with your phone, Gaussian splats, and publishing explorable environments. No experience required.</div></div><span class="who">Tanit XR</span></li>
    <li><div><span class="t"><a href="{href('b-sunken-city', preview)}">Searching for the underwater ruins of Neapolis</a></span><div class="d">Paddling out at 6 AM off the coast near Nabeul with visiting archaeologists to spot the submerged Roman city — roads, walls, and stairs beneath clear water.</div></div><span class="who">Field notes</span></li>
    <li><div><span class="t"><a href="https://tanitxr.org/immersegt-2026/">A Tanit XR track at Georgia Tech's ImmerseGT hackathon</a></span><div class="d">36 hours, real 3D scans of Tunisian heritage, and a winning project — "From Mystery to History" — reimagining preservation with XR and photogrammetry.</div></div><span class="who">ImmerseGT &middot; 2026</span></li>
  </ul>
</div></div>

<div class="band deep"><div class="wrap"><div class="two-col" style="align-items:center">
  <div>
    <p class="kicker">Speaking</p>
    <h2 class="sec-title" style="margin-bottom:10px">Bring XR to your next event.</h2>
    <p style="max-width:56ch;margin:0 0 24px">Keynotes, panels, and workshops on cultural heritage,
    climate, and immersive technology — from the Smithsonian to a Roman colosseum to the Energy
    Thought Summit main stage. In person or virtual, in English, Arabic, or French.</p>
    <div class="btn-row">
      <a class="btn" href="mailto:ines@tanitxr.org?subject=Speaking%20inquiry">Book me to speak</a>
      <a class="btn ghost" href="{href('speaking', preview)}">Topics &amp; past talks</a>
    </div>
  </div>
  <figure class="side-photo" style="margin:0">
    <img src="web/ets-stage.jpg" alt="Ines Said presenting on the Energy Thought Summit main stage" style="max-height:420px;object-fit:cover">
  </figure>
</div></div></div>

<section class="block"><div class="wrap">
  <h2 class="sec-title">Life in the field</h2>
  <p class="sec-sub">Where the work actually happens — dig sites, stages, oceans, and classrooms.</p>
  <div class="gallery" style="grid-template-columns:repeat(4,1fr);margin:0">
    <figure><img src="web/neapolis-swim.jpg" alt="Searching the sea above the sunken city of Neapolis" loading="lazy"><figcaption>Hunting a sunken city.</figcaption></figure>
    <figure><img src="web/statue-pose.jpg" alt="Matching poses with an ancient statue in Tunisia" loading="lazy"><figcaption>Meeting the locals, est. 200 AD.</figcaption></figure>
    <figure><img src="web/froliq-playground.jpg" alt="The Froliq team at the AWE playground" loading="lazy"><figcaption>Game day at AWE.</figcaption></figure>
    <figure><img src="web/workshop.jpg" alt="Teaching a classroom workshop" loading="lazy"><figcaption>Passing it on.</figcaption></figure>
  </div>
</div></section>

<div class="band blush"><div class="wrap" style="text-align:center">
  <p class="kicker" style="justify-content:center">Nonprofit</p>
  <h2 class="sec-title" style="margin-bottom:10px">Support Tanit XR 🏺</h2>
  <p style="max-width:58ch;margin:0 auto 24px">Tunisia's heritage is eroding faster than it can be protected.
  Tanit XR is volunteer-run and self-funded — you can donate through our fiscal sponsor, the Florida Community
  Innovation Foundation, or join us as a volunteer. Love history? Curious about XR? All are welcome.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn" href="https://donors.tuesday.app/campaign/73DO5">Donate to Tanit XR</a>
    <a class="btn ghost" href="https://tanitxr.org/volunteer/">Become a volunteer</a>
  </div>
</div></div>
"""

def body_about(preview):
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">About</p>
  <h1>Art, technology &amp; a little bit of magic.</h1>
  <p class="sub">Tunisian immersive artist and XR technologist — preserving heritage and confronting climate challenges.</p>
</div></div>
<section class="block" style="padding-top:36px"><div class="wrap">
  <div class="two-col">
    <div class="prose">
      <p>I'm a Tunisian immersive artist and XR technologist whose work combines art,
      technology, and sustainability to preserve heritage and confront global challenges.</p>
      <p>Through <strong>Tanit XR</strong> — Tunisia's first open-source digital heritage
      archive, named after the Carthaginian goddess of protection — I use 3D scanning to
      preserve mosaics, statues, and archaeological sites dating back nearly 3,000 years.
      Since founding it in 2025, our volunteer team has documented 80+ artifacts across 20
      sites, built partnerships with the Tunisian Federation of Travel Agencies and
      Sketchfab's Cultural Heritage Program, and produced the largest reconstruction of the
      El Jem Amphitheater to date, featured by Niantic Spatial. I grew up a 15-minute walk
      from the ruins of Roman Neapolis in Nabeul — this work is personal.</p>
      <p>My climate installation <strong>Shadows of Tomorrow</strong> received an Excellence
      Award presented by Miami's Chief Heat Officer Jane Gilbert and author Jeff Goodell, and
      was showcased at MIT Reality Hack, Parsons, and Ringling College.
      <strong>Covid Reflections</strong>, an augmented-reality public art project, toured
      Florida, California, and Japan alongside mobile health clinics, and was covered by ABC,
      CBS, and UF News.</p>
      <p>As Lead XR Developer at <strong>Froliq</strong>, I build immersive experiences for
      energy and sustainability education — including the <em>Future of Energy and Water</em>
      installation for the Smithsonian's FUTURES exhibition, seen by an exhibition audience of
      more than 600,000 visitors. In 2025 alone, these applications reached 11,000+ attendees
      across 40+ events.</p>
      <p>My research has been published in ACM and IEEE — including a Best Paper Award at the
      2023 IEEE Integrated STEM Education Conference for work on teaching through building
      mini VR game engines, with Dr. Angelos Barmpoutis and Wenbin Guo — and my projects have
      earned multiple hackathon wins supported by organizations including Google and IBM.
      I'm increasingly on the judging side of the table too — the Games for Change Awards and
      Student Challenge, the EE 30 Under 30 selection, and Tanit XR's own hackathon track at
      Georgia Tech's ImmerseGT — and I mentor emerging
      artists and technologists through workshops and global networks.</p>
      <p>Away from the headset, I'm a certified scuba diver who's happiest hiking and
      wildlife-spotting — the same places my work tries to protect.</p>
    </div>
    <div>
      <figure class="side-photo">
        <img src="web/statue-pose.jpg" alt="Ines Said at an archaeological site in Tunisia, mirroring the pose of an ancient statue">
        <figcaption>On site — documenting Tunisia's endangered heritage.</figcaption>
      </figure>
    </div>
  </div>
  <div class="pull">
    <p>"Education should make people feel connected to the planet, not just informed about it."</p>
    <span>From her EE 30 Under 30 profile — NAAEE</span>
  </div>
  <h2 class="sec-title" style="font-size:1.5rem">Currently</h2>
  <div class="now-grid">
    <div class="now"><b>Founder</b><span>Tanit XR — open-source heritage archive (2025–)</span></div>
    <div class="now"><b>Lead XR Developer</b><span>Froliq (2023–)</span></div>
    <div class="now"><b>Newsletter Author</b><span><a href="{NEWSLETTER_URL}">Art, XR &amp; Impact Opportunities</a> — weekly, on LinkedIn</span></div>
    <div class="now"><b>Based in</b><span>Washington, D.C. area &amp; Tunisia</span></div>
  </div>

  <div class="two-col" style="margin-top:56px">
    <div>
      <h2 class="sec-title" style="font-size:1.5rem">Experience</h2>
      <ul class="list">
        <li><div><span class="t">Founder — Tanit XR</span><div class="d">Open-source digital heritage archive; 80+ artifacts across 20 sites</div></div><span class="who">2025–</span></li>
        <li><div><span class="t">Lead XR Developer — Froliq</span><div class="d">Leading XR projects from concept to execution across a multidisciplinary team</div></div><span class="who">2023–</span></li>
        <li><div><span class="t">XR Developer — Froliq</span><div class="d">Smithsonian FUTURES installation and VR energy-education games</div></div><span class="who">2022–23</span></li>
        <li><div><span class="t">Adjunct Lecturer — University of Florida</span><div class="d">Taught VR application development for Android and wearables</div></div><span class="who">2023</span></li>
        <li><div><span class="t">Software Engineer — University of Florida</span><div class="d"></div></div><span class="who">2021–23</span></li>
        <li><div><span class="t">3D Virtualization Lab Intern — USF</span><div class="d">Artec scanners, drones, photogrammetry; first virtual environments of scanned artifacts</div></div><span class="who">2018–19</span></li>
      </ul>
    </div>
    <div>
      <h2 class="sec-title" style="font-size:1.5rem">Education</h2>
      <ul class="list">
        <li><div><span class="t">M.S. Digital Arts &amp; Sciences</span><div class="d">University of Florida — MiDAS, Digital Worlds Institute (AR/VR focus)</div></div><span class="who">2020–21</span></li>
        <li><div><span class="t">B.E. Computer Science</span><div class="d">University of South Florida</div></div><span class="who">2015–19</span></li>
        <li><div><span class="t">Exchange — Computer Science</span><div class="d">Deakin University, Australia</div></div><span class="who">2017</span></li>
      </ul>
    </div>
  </div>
  <div class="media-strip">
    <figure><img src="web/mosaic-portrait.jpg" alt="Ines Said in front of an ancient mosaic wall"><figcaption>A mosaic wall thousands of years old, smart glasses on standby.</figcaption></figure>
    <figure><img src="web/el-jem.jpg" alt="Ines Said at the El Jem Amphitheater"><figcaption>El Jem — our largest reconstruction, and a 3rd-century office view.</figcaption></figure>
    <figure><img src="web/workshop.jpg" alt="Ines Said leading a classroom workshop"><figcaption>Workshops and mentoring for emerging artists and technologists.</figcaption></figure>
    <figure><img src="web/ets-fireside.jpg" alt="Ines Said on stage at the Energy Thought Summit"><figcaption>Talking energy and photogrammetry at ETS 2026.</figcaption></figure>
    <figure><img src="web/coast-walk.jpg" alt="Ines Said walking coastal ruins in Tunisia"><figcaption>Field walks — half survey, half joy.</figcaption></figure>
    <figure><img src="web/neapolis-4.jpg" alt="The Neapolis expedition paddle boat, mermaid tail included"><figcaption>Serious research vessel (mermaid tail included).</figcaption></figure>
  </div>
</div></section>
"""

PROJECT_GROUPS = [
    ('Cultural heritage', 'Preserving what time is taking.', ['tanit-xr']),
    ('Immersive art & installations', 'Museum floors, gallery walls, and city streets.',
     ['smithsonian-futures', 'shadows-of-tomorrow', 'covid-reflections', 'sparc']),
    ('Energy & industry', 'Invisible infrastructure, made touchable — my client work at Froliq.',
     ['oracle-connected-hub', 'nypa-vision-pro', 'vistra-tour', 'nuclear-capture']),
    ('Learning & play', 'Games and experiences that turn students into makers.',
     ['froliq-minigames', 'sustainaball', 'stevie', 'exelon-stem']),
]

def body_projects(preview):
    by_slug = {p['slug']: p for p in PROJECTS}
    sections = []
    for title, sub, slugs in PROJECT_GROUPS:
        cards = ''.join(card_html(by_slug[s], preview) for s in slugs if s in by_slug)
        sections.append(
            f'<section class="block" style="padding-top:40px"><div class="wrap">'
            f'<h2 class="sec-title">{title}</h2><p class="sec-sub">{sub}</p>'
            f'<div class="cards two">{cards}</div></div></section>')
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">Portfolio</p>
  <h1>Projects</h1>
  <p class="sub">Thirteen projects across heritage, art, energy, and education. Click any of them for the full story.</p>
</div></div>
{''.join(sections)}
"""

def body_awards(preview):
    cards = []
    for a in AWARDS:
        a = dict(a)
        if a['slug'] == 'futures':
            a['href'] = href('p-smithsonian-futures', preview)
        cards.append(card_html(a, preview, prefix='a-', more='Read the story'))
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">Recognition</p>
  <h1>Awards &amp; Recognition</h1>
  <p class="sub">Honors across environmental education, immersive art, and XR research — click any award for the story behind it.</p>
</div></div>
<section class="block" style="padding-top:36px"><div class="wrap">
  <div class="cards two">{''.join(cards)}</div>

  <h2 class="sec-title" style="margin:72px 0 8px">Judging &amp; jury service</h2>
  <p class="sec-sub">Increasingly on the other side of the table.</p>
  <ul class="list">
    <li><div><span class="t"><a href="https://www.gamesforchange.org/">Judge — Games for Change Awards</a></span><div class="d">The top industry honors for games with real-world impact</div></div><span class="who">G4C</span></li>
    <li><div><span class="t"><a href="https://www.gamesforchange.org/studentchallenge/">Judge — Games for Change Student Challenge</a></span><div class="d">The largest student game-design competition in the U.S.</div></div><span class="who">G4C</span></li>
    <li><div><span class="t"><a href="https://naaee.org/programs/ee-30-under-30">Judge — EE 30 Under 30, Class of 2026</a></span><div class="d">Selecting the next class of environmental-education leaders, one year after being named to the Class of 2025</div></div><span class="who">NAAEE &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://warrington.ufl.edu/undergraduate/hicc/">Judge — Heavener International Case Competition (HICC)</a></span><div class="d">Judging top undergraduate business teams from around the world as they solve a real industry case, at UF's Warrington College of Business</div></div><span class="who">UF &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://tanitxr.org/immersegt-2026/">Track sponsor &amp; judge — ImmerseGT</a></span><div class="d">Tanit XR sponsored a dedicated Tunisian-heritage track at Georgia Tech's 36-hour XR hackathon, with prizes — won by "From Mystery to History"</div></div><span class="who">Georgia Tech &middot; 2026</span></li>
  </ul>
</div></section>
"""

def body_speaking(preview):
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">Speaking &amp; Media</p>
  <h1>Invite me to your stage.</h1>
  <p class="sub">I speak about XR for cultural heritage, climate and sustainability through immersive tech,
  and building XR that changes how people learn — from the Smithsonian to a Roman colosseum.</p>
</div></div>
<section class="block" style="padding-top:32px"><div class="wrap">
  <div class="two-col">
    <div>
      <p style="max-width:60ch;margin:0 0 18px">I'm available for <strong>keynotes, panels, workshops, and
      university guest lectures</strong> — in person or virtual, in <strong>English, Arabic, or French</strong>.
      Recent stages include Augmented World Expo, Games for Change, the Global XR Conference, and the
      El Jem International Conference in Tunisia — where I presented inside the Roman amphitheater itself.</p>
      <div class="stats" style="text-align:left;grid-template-columns:repeat(2,1fr);gap:18px;margin:0 0 22px">
        <div><b>11,000+</b><span>reached in person in 2025, across 40+ events</span></div>
        <div><b>167K</b><span>LinkedIn impressions this past year</span></div>
        <div><b>7,000+</b><span>followers — every stage I'm on, they hear about</span></div>
        <div><b>1 in 4</b><span>of my audience is a founder, exec, or director</span></div>
      </div>
      <p style="max-width:60ch;margin:0 0 18px;font-size:.92rem;color:var(--muted)"><strong style="color:var(--ink)">Trusted by teams at:</strong>
      Oracle Utilities &middot; Exelon &middot; Vistra &middot; New York Power Authority &middot;
      the Smithsonian &middot; NEF</p>
      <div class="chips" style="margin:0 0 26px">
        <span class="chip">XR for cultural heritage</span>
        <span class="chip blush">Climate &amp; sustainability tech</span>
        <span class="chip">From scans to XR: practical pipelines</span>
        <span class="chip blush">AR for public health</span>
        <span class="chip">Women in XR</span>
        <span class="chip blush">STEM education through games</span>
      </div>
      <div class="btn-row">
        <a class="btn" href="#book">Book me to speak</a>
        <a class="btn ghost" href="web/ines-said-speaker.pdf">Speaker one-pager (PDF)</a>
      </div>
    </div>
    <figure class="side-photo">
      <img src="web/ets-stage.jpg" alt="Ines Said presenting her photogrammetry work on the Energy Thought Summit main stage, with her 3D scans on the big screens">
      <figcaption>On the main stage at the Energy Thought Summit 2026 — Tunisia's scans on the big screens.</figcaption>
    </figure>
  </div>
  {embeds_block([
    dict(kind='youtube', id='88-GTiDBTCc', title='Faster Iteration in AR Using Unity — AWE 2022'),
    dict(kind='youtube', id='RNaUaQgXaio', title='Playful Resilience — Games for Change 2022'),
    dict(kind='youtube', id='FMcdT8H5ffE', title='AR in Public Health Awareness — Global XR Conference 2022'),
    dict(kind='vimeo', id='614678798', title='Environment Design in Unity — National Public Lands Day 2021'),
  ], preview, heading='Watch me speak')}

  <h2 class="sec-title" style="margin:64px 0 8px">Talks &amp; appearances</h2>
  <ul class="list">
    <li><div><span class="t"><a href="https://tanitxr.org/el-jem-conference/">Presenting Tanit XR inside the El Jem Amphitheater</a></span><div class="d">El Jem International Conference — research paper on XR and citizen science for heritage preservation, published in English, French, and Tunisian Arabic</div></div><span class="who">El Jem &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://energythoughtsummit.com/">Photogrammetry for Energy &amp; Heritage — main stage</a></span><div class="d">Energy Thought Summit (ETS26), San Antonio — presenting her photogrammetry work with Froliq and Tanit XR</div></div><span class="who">ETS &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://x.com/InlocoG21235/status/1989010660512985594">Inloco Gallery — MetaTalks</a></span><div class="d">Panel on immersive art and spatial storytelling, hosted by Inloco Gallery</div></div><span class="who">Inloco &middot; 2025</span></li>
    <li><div><span class="t">Beyond the Byte — panel</span><div class="d">Panel on immersive technology, in the Washington, D.C. area</div></div><span class="who">DMV &middot; 2026</span></li>
    <li><div><span class="t">XR, AI &amp; Immersive Technology — panel</span><div class="d">Panel discussion in Crystal City, Virginia</div></div><span class="who">Crystal City &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://www.awexr.com/usa-2026/speakers/2677-ines-said">From Scans to XR: A Practical Pipeline for Cultural Heritage</a></span><div class="d">Augmented World Expo USA — with Margarita Johnson (Tanit XR)</div></div><span class="who">AWE &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://www.youtube.com/watch?v=88-GTiDBTCc">Faster Iteration in AR Using Unity</a></span><div class="d">Augmented World Expo</div></div><span class="who">AWE &middot; 2022</span></li>
    <li><div><span class="t"><a href="https://www.youtube.com/watch?v=RNaUaQgXaio">Playful Resilience</a></span><div class="d">Games for Change</div></div><span class="who">G4C &middot; 2022</span></li>
    <li><div><span class="t"><a href="https://www.youtube.com/watch?v=FMcdT8H5ffE">AR in Public Health Awareness</a></span><div class="d">Global XR Conference</div></div><span class="who">2022</span></li>
    <li><div><span class="t"><a href="https://vimeo.com/699905464">AR in Public Health Interactions</a></span><div class="d">AI and Interactions with Society Mini-Symposium</div></div><span class="who">2022</span></li>
    <li><div><span class="t"><a href="https://vimeo.com/705933196">HoloKeys — Lightning Round</a></span><div class="d">UF College of the Arts Strategic Opportunity Fund</div></div><span class="who">2021–22</span></li>
    <li><div><span class="t"><a href="https://vimeo.com/614678798">Environment Design in Unity</a></span><div class="d">National Public Lands Day, UF Digital Worlds</div></div><span class="who">2021</span></li>
    <li><div><span class="t"><a href="https://www.youtube.com/watch?v=PPh12oJ38rQ">The AR Minute with Nathan C</a></span><div class="d">Awesome Future — with Austin Stanbury</div></div><span class="who">Interview</span></li>
  </ul>
  <div class="media-strip">
    <figure><img src="web/ets-fireside.jpg" alt="Ines Said in a fireside conversation on the colorful ETS 2026 stage"><figcaption>Fireside at the Energy Thought Summit 2026.</figcaption></figure>
    <figure><img src="web/dmv-panel.jpg" alt="Ines Said on the Beyond the Byte panel"><figcaption>On the Beyond the Byte panel in the D.C. area.</figcaption></figure>
    <figure><img src="web/stage.jpg" alt="Ines Said speaking on stage at a summit"><figcaption>On stage — speaking on XR, art, and impact.</figcaption></figure>
    <figure><img src="web/speaker-card.jpg" alt="AWE USA 2026 speaker card for Ines Said"><figcaption>Speaker — Augmented World Expo USA 2026.</figcaption></figure>
  </div>

  <h2 class="sec-title" style="margin:72px 0 8px">Workshops &amp; consulting</h2>
  <p class="sec-sub">Beyond the stage — hands-on training and XR development for teams.</p>
  <div class="cards">
    <div class="card"><div class="card-inner"><div class="card-body">
      <h3>3D-scanning workshops</h3>
      <p>Train your team to capture your collection, facility, or site in 3D — photogrammetry
      and Gaussian splatting with the phones already in their pockets. Half-day to multi-day,
      for museums, universities, and companies. Based on the curriculum behind Tanit XR's
      free public courses.</p>
      <div class="chips"><span class="chip">Photogrammetry</span><span class="chip blush">Hands-on</span></div>
    </div></div></div>
    <div class="card"><div class="card-inner"><div class="card-body">
      <h3>XR consulting &amp; development</h3>
      <p>From concept to headset: AR, VR, and WebXR experiences on Apple Vision Pro, Meta
      Quest, mobile, and the open web. The same pipeline behind installations for the
      Smithsonian, Oracle Utilities, and power-industry clients.</p>
      <div class="chips"><span class="chip">Vision Pro</span><span class="chip blush">Quest</span><span class="chip">WebXR</span></div>
    </div></div></div>
    <div class="card"><div class="card-inner"><div class="card-body">
      <h3>Heritage digitization</h3>
      <p>End-to-end digital preservation for cultural institutions: on-site scanning,
      open-access archives, virtual museums, and AR experiences — the Tanit XR model,
      applied to your collection.</p>
      <div class="chips"><span class="chip">Museums</span><span class="chip blush">Archives</span></div>
    </div></div></div>
  </div>

  <h2 class="sec-title" id="book" style="margin:72px 0 8px">Let's talk</h2>
  <p class="sec-sub">Booking a talk, planning a workshop, or exploring a project — this lands straight in my inbox.</p>
  <form class="contact-form" action="https://formsubmit.co/ines@tanitxr.org" method="POST">
    <input type="hidden" name="_subject" value="Inquiry from inessaid.com">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="_honey" style="display:none">
    <label for="cf-name">Your name</label>
    <input id="cf-name" type="text" name="name" required>
    <label for="cf-email">Email</label>
    <input id="cf-email" type="email" name="email" required>
    <label for="cf-org">Organization</label>
    <input id="cf-org" type="text" name="organization">
    <label for="cf-type">What are you looking for?</label>
    <select id="cf-type" name="inquiry_type">
      <option>Speaking — keynote or talk</option>
      <option>Speaking — panel or guest lecture</option>
      <option>Workshop or training</option>
      <option>XR consulting / development</option>
      <option>Tanit XR — partnership or press</option>
      <option>Something else</option>
    </select>
    <label for="cf-msg">Tell me about it</label>
    <textarea id="cf-msg" name="message" rows="5" required></textarea>
    <button type="submit">Send inquiry</button>
  </form>
</div></section>
"""

def body_press(preview):
    return """
<div class="wrap"><div class="page-head">
  <p class="kicker">In the news</p>
  <h1>Press</h1>
  <p class="sub">Coverage of Tanit XR, Covid Reflections, and immersive art for impact.</p>
</div></div>
<section class="block" style="padding-top:36px"><div class="wrap">
  <ul class="list">
    <li><div><span class="t"><a href="https://www.aljazeera.net/amp/culture/2025/10/12/%D8%AA%D8%A7%D9%86%D9%8A%D8%AA-%D8%A5%D9%83%D8%B3-%D8%A2%D8%B1-%D9%85%D9%86%D8%B5%D8%A9-%D8%BA%D9%8A%D8%B1-%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9-%D8%AA%D9%88%D8%AB%D9%82">Tanit XR: a non-profit platform documenting Tunisia's heritage</a></span></div><span class="who">Al Jazeera &middot; 2025</span></li>
    <li><div><span class="t"><a href="https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873/">Tanit XR's El Jem reconstruction "sets a benchmark for large-scale reality capture"</a></span></div><span class="who">Niantic Spatial &middot; 2026</span></li>
    <li><div><span class="t"><a href="https://carthagemagazine.com/tanit-xr-preserving-tunisias-heritage-through-immersive-technology/">Preserving Tunisia's heritage through immersive technology</a></span></div><span class="who">Carthage Magazine</span></li>
    <li><div><span class="t"><a href="https://news.ufl.edu/2022/04/covid-reflections/">Using AI in the arts to promote COVID-19 vaccines</a></span></div><span class="who">UF News &middot; 2022</span></li>
    <li><div><span class="t"><a href="https://www.wcjb.com/2022/04/11/university-florida-launches-covid-reflections-project-utilizing-ai-increase-vaccination/">UF launches "Covid Reflections"</a></span></div><span class="who">ABC 20 WCJB &middot; 2022</span></li>
    <li><div><span class="t"><a href="https://mycbs4.com/news/local/university-of-florida-vaccine-exhibit">University of Florida vaccine exhibit</a></span></div><span class="who">CBS4 News</span></li>
    <li><div><span class="t"><a href="https://mycbs4.com/news/local/uf-artists-host-in-the-machine-exhibit-at-4most-gallery">UF artists host "In the Machine" at 4Most Gallery</a></span></div><span class="who">CBS4 News</span></li>
    <li><div><span class="t"><a href="https://ufdigitalworlds.medium.com/uf-digital-worlds-faculty-and-alumni-collaborate-for-in-the-machine-exhibition-showcasing-the-e9b3f8fd2582">"In the Machine": technology converges with art</a></span></div><span class="who">UF Digital Worlds</span></li>
    <li><div><span class="t"><a href="https://arts.ufl.edu/in-the-loop/news/midas-cohort-builds-track-record-of-hackathon-success/">MiDAS cohort builds track record of hackathon success</a></span></div><span class="who">UF Arts</span></li>
    <li><div><span class="t"><a href="https://medium.com/women-write/tanit-xr-preserving-tunisias-heritage-through-immersive-technology-c9238dab7675">Tanit XR — in her own words (Women Write)</a></span></div><span class="who">Medium &middot; Writing</span></li>
  </ul>
  <div class="media-strip">
    <figure><img src="web/news-abc.jpg" alt="Local TV news segment covering the Covid Reflections launch"><figcaption>Covid Reflections on the evening news.</figcaption></figure>
    <figure><img src="web/carthage-mag.jpg" alt="Carthage Magazine feature on Tanit XR"><figcaption>Tanit XR in Carthage Magazine.</figcaption></figure>
  </div>
</div></section>
"""

# ---------------- opportunities board ----------------
# Update this list (or tell Claude the new edition) and rebuild — the page computes
# countdowns and open/closed automatically from the deadline dates.
OPPS = [
 ('ISO Immersive Media Fund — Indigenous Creators', 'Fund', '$500K CAD', '2026-06-30', 'https://www.agog.world/', 'For US Indigenous XR storytellers, presented with Agog'),
 ('AWS She Builds Mentorship', 'Mentorship', 'Free', '2026-06-30', 'https://aws.amazon.com/', '12-week mentorship pairing women in tech with a dedicated AWS mentor'),
 ('Global Good Fund Fellowship 2027', 'Fellowship', '$10K + coaching', '2026-06-30', 'https://globalgoodfund.org/', 'Leadership grant and executive coaching for social entrepreneurs worldwide'),
 ('NEW INC — New Museum Incubator', 'Residency', 'Year-long', '2026-07-08', 'https://www.newinc.org/', 'Art + design + tech incubator with an Extended Realities track'),
 ('UNESCO Youth for Peace — Intercultural Leadership', 'Grant', '$10K seed', '2026-07-19', 'https://www.unesco.org/', 'Seed funding + training for emerging leaders 25–45; 2026 theme: human connection in the age of AI'),
 ('VH AWARD (7th Edition) — Hyundai', 'Award', 'Production grant', '2026-07-21', 'https://vhaward.com/', 'Production grant + Ars Electronica online residency for emerging media artists of Asian descent or the diaspora'),
 ('TED × POSCA Global Artist Residency', 'Residency', '$15K', '2026-07-31', 'https://www.ted.com/', 'Four artists fund community-rooted public art on repair and resilience — open worldwide'),
 ('Global Innovation Challenge 2026', 'Grant', 'up to $15K', '2026-08-31', 'https://www.globalinnovationchallenge.org/', 'Grants for youth changemakers 18–30 solving social and environmental problems'),
 ('WomenTech Network Global Awards 2026', 'Award', 'Recognition', '2026-10-01', 'https://www.womentech.net/', 'Nominate yourself or someone shaping tech'),
 ('AWE USA 2027 — Call for Speakers', 'Speaking', 'Stage', '2027-01-31', 'https://www.awexr.com/', "Speak, demo, or exhibit at next year's biggest XR conference — get in early"),
 ('Climate Change AI Summer School', 'Program', '~$10', '2026-07-19', 'https://www.climatechange.ai/', 'Virtual summer school on climate + machine learning; newcomers welcome'),
]

def body_opportunities(preview):
    rows = []
    for name, cat, amount, deadline, url, desc in OPPS:
        rows.append(
            f'<tr data-deadline="{deadline}">'
            f'<td><a href="{url}"><b>{name}</b></a><div class="opp-desc">{desc}</div></td>'
            f'<td><span class="chip">{cat}</span></td>'
            f'<td class="opp-amount">{amount}</td>'
            f'<td class="opp-date">{deadline}</td>'
            f'<td class="opp-left">—</td></tr>')
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">Newsletter</p>
  <h1>Art, XR &amp; Impact Opportunities</h1>
  <p class="sub">Grants, residencies, fellowships, and open calls at the intersection of creative
  practice and technology — curated weekly. Deadlines below update their countdowns automatically.</p>
</div></div>
<section class="block" style="padding-top:28px"><div class="wrap">
  <div class="stats" style="text-align:left;margin-bottom:36px;grid-template-columns:repeat(3,1fr)">
    <div><b>7,000+</b><span>LinkedIn followers receive every edition</span></div>
    <div><b>167K</b><span>impressions in the past year, 30K+ people reached</span></div>
    <div><b>1 in 4</b><span>readers is a founder, executive, director, or owner</span></div>
  </div>
  <div class="btn-row" style="margin-bottom:28px">
    <a class="btn" href="{NEWSLETTER_URL}">Subscribe to the weekly newsletter</a>
    <button class="btn ghost" id="opp-toggle" type="button">Show closed deadlines</button>
    <a class="btn ghost" href="mailto:ines@tanitxr.org?subject=Feature%20an%20opportunity">Feature your opportunity</a>
  </div>
  <div style="overflow-x:auto">
    <table class="opp-table" id="opp-table">
      <thead><tr><th>Opportunity</th><th>Type</th><th>Amount</th><th>Deadline</th><th>Time left</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
  </div>
  <p style="color:var(--muted);font-size:.85rem;margin-top:24px">From the latest editions of the
  newsletter — full details and links in each <a href="{NEWSLETTER_URL}">edition on LinkedIn</a>.</p>
</div></section>
<script>
(function(){{
  var tbl = document.getElementById('opp-table');
  if (!tbl || tbl.dataset.done) return; tbl.dataset.done = 1;
  var rows = [...tbl.tBodies[0].rows], now = new Date();
  rows.forEach(function(r){{
    var d = new Date(r.dataset.deadline + 'T23:59:59');
    var days = Math.ceil((d - now) / 86400000);
    var cell = r.querySelector('.opp-left');
    if (days < 0) {{ cell.innerHTML = '<span class="opp-badge closed">Closed</span>'; r.classList.add('opp-closed'); }}
    else if (days <= 14) {{ cell.innerHTML = '<span class="opp-badge soon">' + days + ' days</span>'; }}
    else {{ cell.innerHTML = '<span class="opp-badge open">' + days + ' days</span>'; }}
    r.dataset.days = days;
  }});
  rows.sort(function(a,b){{
    var da = +a.dataset.days, db = +b.dataset.days;
    return (da < 0) - (db < 0) || da - db;
  }}).forEach(function(r){{ tbl.tBodies[0].appendChild(r); }});
  var btn = document.getElementById('opp-toggle'), showing = false;
  btn.addEventListener('click', function(){{
    showing = !showing;
    tbl.classList.toggle('show-closed', showing);
    btn.textContent = showing ? 'Hide closed deadlines' : 'Show closed deadlines';
  }});
}})();
</script>
"""

BODIES = {'home': body_home, 'about': body_about, 'projects': body_projects,
          'awards': body_awards, 'speaking': body_speaking,
          'opportunities': body_opportunities, 'press': body_press, 'blog': body_blog}

HEAD = ('<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')

BASE_URL = 'https://www.inessaid.com'
DEFAULT_DESC = ('Ines Said — Tunisian immersive artist and XR technologist. Founder of Tanit XR, '
                "Tunisia's first open-source heritage archive, and Lead XR Developer at Froliq. "
                'Exhibited at the Smithsonian and MIT.')

PERSON_JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Ines Said",
  "url": "https://www.inessaid.com",
  "image": "https://www.inessaid.com/web/portrait.jpg",
  "jobTitle": "XR Immersive Artist and Technologist",
  "worksFor": {"@type": "Organization", "name": "Froliq"},
  "founder": {"@type": "Organization", "name": "Tanit XR", "url": "https://tanitxr.org"},
  "alumniOf": [
    {"@type": "CollegeOrUniversity", "name": "University of Florida"},
    {"@type": "CollegeOrUniversity", "name": "University of South Florida"}
  ],
  "email": "mailto:ines@tanitxr.org",
  "knowsAbout": ["Extended Reality", "Augmented Reality", "Virtual Reality", "Cultural Heritage Preservation", "3D Scanning", "Photogrammetry", "Gaussian Splatting", "Climate Art", "Unity"],
  "knowsLanguage": ["English", "Arabic", "French"],
  "nationality": {"@type": "Country", "name": "Tunisia"},
  "homeLocation": [{"@type": "Place", "name": "Washington, D.C. area"}, {"@type": "Place", "name": "Tunisia"}],
  "award": ["EE 30 Under 30, Class of 2025 (NAAEE)", "IEEE Best Paper Award", "GFAA Biennial Excellence Award", "Auggie Awards Finalist, Best Societal Impact (2026)"],
  "sameAs": [
    "https://www.linkedin.com/in/inessaid/",
    "https://www.instagram.com/inessaidd/",
    "https://www.facebook.com/ines1said/",
    "https://tanitxr.org/person/ines-said/",
    "https://www.researchgate.net/profile/Ines-Said-2",
    "https://medium.com/women-write/tanit-xr-preserving-tunisias-heritage-through-immersive-technology-c9238dab7675",
    "https://naaee.org/people/ines-said",
    "https://www.awexr.com/usa-2026/speakers/2677-ines-said"
  ]
}
</script>"""

def seo(title, desc, path, jsonld=False):
    url = BASE_URL + '/' + (path if path != 'index.html' else '')
    tags = (f'<title>{title}</title>'
            f'<meta name="description" content="{desc}">'
            f'<link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="website">'
            f'<meta property="og:title" content="{title}">'
            f'<meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{BASE_URL}/web/portrait.jpg">'
            f'<meta property="og:site_name" content="Ines Said">'
            f'<meta name="twitter:card" content="summary_large_image">')
    if jsonld:
        tags += PERSON_JSONLD
    return tags

def page_html(page):
    body = BODIES[page](False)
    name = 'index.html' if page == 'home' else page + '.html'
    return (f'<!doctype html><html lang="en"><head>{HEAD}'
            f'{seo(TITLE[page], DEFAULT_DESC, name, jsonld=(page in ("home", "about")))}'
            f'{FONTS}<style>{CSS}</style></head><body>'
            f'{nav_html(page, False)}{body}{FOOTER}</body></html>')

def detail_page_html(p):
    name = f'project-{p["slug"]}.html'
    desc = p['card'].replace('"', '&quot;')
    return (f'<!doctype html><html lang="en"><head>{HEAD}'
            f'{seo(p["title"] + " | Ines Said", desc, name)}'
            f'{FONTS}<style>{CSS}</style></head><body>'
            f'{nav_html("projects", False)}{body_detail(p, False)}{FOOTER}</body></html>')

def build_site():
    os.makedirs(OUT, exist_ok=True)
    web_out = os.path.join(OUT, 'web')
    if os.path.isdir(web_out):
        shutil.rmtree(web_out)
    shutil.copytree(os.path.join(ROOT, 'web'), web_out)
    for page in PAGES:
        name = 'index.html' if page == 'home' else page + '.html'
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(page_html(page))
    for p in PROJECTS:
        with open(os.path.join(OUT, f'project-{p["slug"]}.html'), 'w', encoding='utf-8') as f:
            f.write(detail_page_html(p))
    for p in POSTS:
        name = f'blog-{p["slug"]}.html'
        html = (f'<!doctype html><html lang="en"><head>{HEAD}'
                f'{seo(p["title"] + " | Ines Said", p["excerpt"].replace(chr(34), "&quot;"), name)}'
                f'{FONTS}<style>{CSS}</style></head><body>'
                f'{nav_html("blog", False)}{body_post(p, False)}{FOOTER}</body></html>')
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(html)
    for a in AWARDS:
        if not a['paras']:
            continue
        name = f'award-{a["slug"]}.html'
        html = (f'<!doctype html><html lang="en"><head>{HEAD}'
                f'{seo(a["title"] + " | Ines Said", a["card"].replace(chr(34), "&quot;"), name)}'
                f'{FONTS}<style>{CSS}</style></head><body>'
                f'{nav_html("awards", False)}{body_detail(a, False, "awards", "All awards")}{FOOTER}</body></html>')
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(html)
    # legacy Wix URL redirects (protect indexed URLs + knowledge panel)
    LEGACY = {
        'about': 'about.html', 'projects': 'projects.html',
        'awards-recognition': 'awards.html', 'press': 'press.html',
        'talks-media': 'speaking.html', 'blog': 'blog.html',
        'art-xr-and-impact-opportunities': 'opportunities.html',
        'projects/tanit-xr---cultural-heritage': 'project-tanit-xr.html',
        'projects/covid-reflections': 'project-covid-reflections.html',
        'projects/shadows-of-tomorrow': 'project-shadows-of-tomorrow.html',
        'projects/oracle-connected-hub-ar-application': 'project-oracle-connected-hub.html',
        'projects/sparc': 'project-sparc.html',
        'post/ines-said-an-xr-immersive-artist-technologist': 'about.html',
    }
    for old, new in LEGACY.items():
        d = os.path.join(OUT, old)
        os.makedirs(d, exist_ok=True)
        depth = old.count('/') + 1
        target = '../' * depth + new
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
                    f'<meta http-equiv="refresh" content="0;url={target}">'
                    f'<link rel="canonical" href="{BASE_URL}/{new}">'
                    f'<title>Redirecting</title></head>'
                    f'<body><a href="{target}">This page has moved</a></body></html>')
    # smart 404: catches any unmapped old Wix URL and routes it sensibly
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(f'''<!doctype html><html lang="en"><head>{HEAD}<title>Ines Said</title>{FONTS}<style>{CSS}</style>
<script>
(function(){{
  var p = location.pathname.toLowerCase();
  var map = [[/\\/post\\//,'/blog.html'],[/\\/blog/,'/blog.html'],[/\\/projects/,'/projects.html'],
             [/awards/,'/awards.html'],[/talks|media|speak/,'/speaking.html'],[/press/,'/press.html'],
             [/opportun/,'/opportunities.html'],[/about/,'/about.html']];
  for (var i=0;i<map.length;i++) if (map[i][0].test(p)) {{ location.replace(map[i][1]); return; }}
}})();
</script></head><body>
{nav_html('home', False)}
<div class="wrap"><div class="page-head">
  <p class="kicker">Page moved</p>
  <h1>This page has a new home.</h1>
  <p class="sub">The site was rebuilt — everything is still here. Try <a href="/">the homepage</a>,
  <a href="/projects.html">projects</a>, or <a href="/blog.html">the blog</a>.</p>
</div></div>{FOOTER}</body></html>''')
    # sitemap + robots for search engines
    urls = (['index.html'] + [pg + '.html' for pg in PAGES[1:]] +
            [f'project-{p["slug"]}.html' for p in PROJECTS] +
            [f'blog-{p["slug"]}.html' for p in POSTS] +
            [f'award-{a["slug"]}.html' for a in AWARDS if a['paras']])
    entries = ''.join(f'<url><loc>{BASE_URL}/{u if u != "index.html" else ""}</loc></url>' for u in urls)
    with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>')
    # CNAME temporarily disabled for github.io preview — RESTORE before DNS cutover:
    # with open(os.path.join(OUT, 'CNAME'), 'w', encoding='utf-8') as f:
    #     f.write('www.inessaid.com\n')
    with open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n')
    print('site/ written:', len(PAGES), 'pages +', len(PROJECTS), 'project pages + sitemap.xml + robots.txt')

def build_preview():
    sections = []
    for page in PAGES:
        sections.append(f'<main data-page="{page}" hidden>{BODIES[page](True)}</main>')
    for p in PROJECTS:
        sections.append(f'<main data-page="p-{p["slug"]}" hidden>{body_detail(p, True)}</main>')
    for p in POSTS:
        sections.append(f'<main data-page="b-{p["slug"]}" hidden>{body_post(p, True)}</main>')
    for a in AWARDS:
        if a['paras']:
            sections.append(f'<main data-page="a-{a["slug"]}" hidden>{body_detail(a, True, "awards", "All awards")}</main>')
    router = """
<script>
(function(){
  var pages = document.querySelectorAll('main[data-page]');
  var navs = document.querySelectorAll('nav a');
  function show(){
    var p = (location.hash || '#/home').replace('#/','') || 'home';
    var found = false;
    pages.forEach(function(m){ var on = m.dataset.page === p; m.hidden = !on; if(on) found = true; });
    if (!found){ pages.forEach(function(m){ m.hidden = m.dataset.page !== 'home'; }); p = 'home'; }
    var navKey = p.indexOf('p-') === 0 ? 'projects' : (p.indexOf('b-') === 0 ? 'blog' : (p.indexOf('a-') === 0 ? 'awards' : p));
    navs.forEach(function(a){
      a.classList.toggle('active', a.getAttribute('href') === '#/' + navKey);
    });
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange', show);
  show();
})();
</script>"""
    html = (f'<meta charset="utf-8"><title>Ines Said</title>{FONTS}<style>{CSS}</style>'
            f'{nav_html("home", True)}{"".join(sections)}{FOOTER}{router}')
    def inline(m):
        data = base64.b64encode(open(os.path.join(ROOT, m.group(1)), 'rb').read()).decode()
        return f'src="data:image/jpeg;base64,{data}"'
    html = re.sub(r'src="(web/[a-z0-9-]+\.jpg)"', inline, html)
    def inline_css(m):
        data = base64.b64encode(open(os.path.join(ROOT, m.group(1)), 'rb').read()).decode()
        return f'url(data:image/jpeg;base64,{data})'
    html = re.sub(r'url\((web/[a-z0-9-]+\.jpg)\)', inline_css, html)
    with open(os.path.join(ROOT, 'preview.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print('preview.html written:', len(html)//1024, 'KB')

# ---------------- French & Arabic pages ----------------
L10N = {
 'fr': dict(dir='ltr', lang='fr',
   nav=[('index.html','Accueil'),('about.html','À propos'),('../projects.html','Projets'),
        ('../awards.html','Prix'),('../speaking.html','Conférences'),('../opportunities.html','Opportunités'),
        ('../press.html','Presse'),('../blog.html','Blog')],
   home_title='Ines Said | Artiste immersive et technologue XR',
   home_desc="Ines Said — artiste immersive et technologue XR tunisienne. Fondatrice de Tanit XR, développeuse XR principale chez Froliq. Exposée au Smithsonian et au MIT.",
   kicker='Artiste immersive &amp; technologue XR',
   hello='Bonjour, je suis <em>Ines Said</em>.',
   lede="J'ai grandi à quinze minutes à pied des ruines romaines de Néapolis, en Tunisie — aujourd'hui, je préserve des lieux comme celui-là en 3D. Fondatrice de <strong>Tanit XR</strong>, premier archive open source des artefacts menacés de Tunisie, et développeuse XR principale chez <strong>Froliq</strong>. Mes installations sur le patrimoine et le climat ont été exposées dans le monde entier, du Smithsonian au MIT.",
   btn_work='Découvrir mon travail', btn_about='En savoir plus',
   stats=[('600 000+', "visiteurs de l'exposition FUTURES du Smithsonian, où figurait son installation"),
          ('30 Under 30', 'EE 30 Under 30, promotion 2025 — NAAEE'),
          ('11 000+', 'personnes touchées en 2025 lors de plus de 40 événements'),
          ('Finaliste Auggie', 'Meilleur impact sociétal — Tanit XR, AWE 2026')],
   featured_h='Projets phares', featured_sub='Patrimoine, climat et santé publique — en réalité augmentée et virtuelle. (Pages projets en anglais.)',
   featured=[('../project-tanit-xr.html','Tanit XR', "Premier archive numérique open source du patrimoine tunisien : plus de 80 artefacts documentés sur 20 sites, des mosaïques à l'amphithéâtre d'El Jem."),
             ('../project-shadows-of-tomorrow.html','Shadows of Tomorrow', "Installation XR sur le climat : seul, on voit un monde abîmé — main dans la main, il se restaure. Prix d'excellence à la biennale de la GFAA."),
             ('../project-smithsonian-futures.html','Smithsonian FUTURES', "Installation immersive co-créée pour l'exposition FUTURES du Smithsonian à Washington — plus de 600 000 visiteurs.")],
   speak_h='Invitez-moi sur votre scène.',
   speak_p="Conférences, panels et ateliers sur le patrimoine culturel, le climat et les technologies immersives — du Smithsonian à un colisée romain. En présentiel ou en ligne, en français, en arabe ou en anglais.",
   speak_btn='Réserver une intervention',
   support_h='Soutenez Tanit XR 🏺',
   support_p="Le patrimoine tunisien s'érode plus vite qu'on ne peut le protéger. Tanit XR est une initiative bénévole et autofinancée — vous pouvez faire un don via notre sponsor fiscal, la Florida Community Innovation Foundation, ou nous rejoindre comme bénévole.",
   support_btn='Faire un don', volunteer_btn='Devenir bénévole',
   about_title='À propos | Ines Said',
   about_h1="L'art, la technologie et un peu de magie.",
   about_sub='Artiste immersive et technologue XR tunisienne — préserver le patrimoine, affronter le climat.',
   about_paras=[
     "Je suis une artiste immersive et technologue XR tunisienne. Mon travail mêle art, technologie et durabilité pour préserver le patrimoine et affronter les défis mondiaux.",
     "Avec <strong>Tanit XR</strong> — premier archive numérique open source du patrimoine tunisien, baptisé du nom de la déesse carthaginoise de la protection — j'utilise la numérisation 3D pour préserver mosaïques, statues et sites archéologiques vieux de près de 3 000 ans. Depuis sa fondation en 2025, notre équipe bénévole a documenté plus de 80 artefacts sur 20 sites, noué des partenariats avec la Fédération tunisienne des agences de voyages et le programme patrimoine culturel de Sketchfab, et réalisé la plus grande reconstruction de l'amphithéâtre d'El Jem à ce jour, mise à l'honneur par Niantic Spatial. J'ai grandi à quinze minutes à pied des ruines de la Néapolis romaine, à Nabeul — ce travail est personnel.",
     "Mon installation climatique <strong>Shadows of Tomorrow</strong> a reçu un prix d'excellence remis par Jane Gilbert, Chief Heat Officer de Miami, et l'auteur Jeff Goodell. <strong>Covid Reflections</strong>, projet d'art public en réalité augmentée, a tourné en Floride, en Californie et au Japon aux côtés de cliniques mobiles.",
     "Développeuse XR principale chez <strong>Froliq</strong>, je crée des expériences immersives pour l'éducation à l'énergie et à la durabilité — dont l'installation <em>Future of Energy and Water</em> pour l'exposition FUTURES du Smithsonian, vue par plus de 600 000 visiteurs.",
     "Mes recherches sont publiées dans l'ACM et l'IEEE (Best Paper Award, IEEE ISEC 2023), et je siège de plus en plus souvent du côté des jurys — Games for Change, EE 30 Under 30, et le hackathon ImmerseGT de Georgia Tech, dont Tanit XR a parrainé une piste dédiée au patrimoine tunisien.",
     "Loin des casques, je suis plongeuse certifiée, heureuse en randonnée et à l'affût de la faune — dans les lieux mêmes que mon travail tente de protéger."],
   about_caption="Sur le terrain — documenter le patrimoine tunisien menacé.",
   quote="« L'éducation doit faire sentir aux gens qu'ils sont liés à la planète, pas seulement informés à son sujet. »",
   quote_src='Extrait de son profil EE 30 Under 30 — NAAEE',
   full_bio='Parcours complet (en anglais) →'),

 'ar': dict(dir='rtl', lang='ar',
   nav=[('index.html','الرئيسية'),('about.html','من أنا'),('../projects.html','المشاريع'),
        ('../awards.html','الجوائز'),('../speaking.html','المحاضرات'),('../opportunities.html','الفرص'),
        ('../press.html','الصحافة'),('../blog.html','المدوّنة')],
   home_title='إيناس سعيد | فنانة غامرة ومطوّرة XR',
   home_desc='إيناس سعيد — فنانة تونسية ومطوّرة XR. مؤسِّسة Tanit XR، وتعمل لدى Froliq بصفة Lead XR Developer. عُرضت أعمالها في Smithsonian وMIT.',
   kicker='فنانة غامرة ومطوّرة XR',
   hello='مرحبًا، أنا <em>إيناس سعيد</em>.',
   lede='نشأتُ على بُعد خمس عشرة دقيقة سيرًا من أطلال نيابوليس الرومانية في تونس — واليوم أحفظ أماكن مثلها بتقنيات ثلاثية الأبعاد. أنا مؤسِّسة <strong>Tanit XR</strong>، أول أرشيف مفتوح المصدر للآثار المهدَّدة في تونس، وأعمل لدى <strong>Froliq</strong> بصفة Lead XR Developer. عُرضت أعمالي حول التراث والمناخ حول العالم، من Smithsonian إلى MIT.',
   btn_work='اكتشفوا أعمالي', btn_about='المزيد عنّي',
   stats=[('+600,000', 'زائر لمعرض FUTURES في Smithsonian الذي ضمّ عملي'),
          ('EE 30 Under 30', 'ضمن قائمة NAAEE لقادة التعليم البيئي، دفعة 2025'),
          ('+11,000', 'شخص وصلت إليهم أعمالي في 2025 عبر أكثر من 40 فعالية'),
          ('نهائيات Auggie', 'أفضل أثر مجتمعي — Tanit XR، AWE 2026')],
   featured_h='أبرز المشاريع', featured_sub='التراث والمناخ والصحة العامة — بالواقع المعزَّز والافتراضي. (صفحات المشاريع بالإنجليزية.)',
   featured=[('../project-tanit-xr.html','Tanit XR', 'أول أرشيف رقمي مفتوح المصدر للتراث التونسي: أكثر من 80 قطعة أثرية موثَّقة في 20 موقعًا، من الفسيفساء إلى مسرح الجم.'),
             ('../project-shadows-of-tomorrow.html','Shadows of Tomorrow', 'عمل فنّي مناخي غامر: وحدك ترى عالمًا متضررًا — وحين تمسك يدَ شخصٍ آخر، يعود العالم إلى الحياة. جائزة التميّز في بينالي GFAA.'),
             ('../project-smithsonian-futures.html','Smithsonian FUTURES', 'تجربة غامرة شاركتُ في صنعها لمعرض FUTURES في واشنطن — زاره أكثر من 600,000 شخص.')],
   speak_h='ادعوني إلى منصّتكم.',
   speak_p='محاضرات وندوات وورشات حول التراث الثقافي والمناخ والتقنيات الغامرة — من Smithsonian إلى المدرّج الروماني في الجم. حضوريًا أو عن بُعد، بالعربية أو الفرنسية أو الإنجليزية.',
   speak_btn='احجزوا محاضرة',
   support_h='ادعموا Tanit XR 🏺',
   support_p='تراث تونس يتآكل أسرع مما نستطيع حمايته. Tanit XR مبادرة تطوعية ذاتية التمويل — يمكنكم التبرّع عبر راعينا المالي Florida Community Innovation Foundation، أو الانضمام إلينا كمتطوعين. تحبّون التاريخ؟ يثير الـ XR فضولكم؟ أهلًا بالجميع.',
   support_btn='تبرّعوا الآن', volunteer_btn='انضمّوا كمتطوعين',
   about_title='من أنا | إيناس سعيد',
   about_h1='فنٌّ وتقنية وقليلٌ من السحر.',
   about_sub='فنانة تونسية ومطوّرة XR — أحفظ التراث وأواجه تغيّر المناخ.',
   about_paras=[
     'أنا فنانة غامرة ومطوّرة XR من تونس. يجمع عملي بين الفن والتقنية والاستدامة لحفظ التراث ومواجهة التحديات العالمية.',
     'عبر <strong>Tanit XR</strong> — أول أرشيف رقمي مفتوح المصدر للتراث التونسي، سمّيته على اسم تانيت، الإلهة القرطاجية الحامية — أستخدم المسح ثلاثي الأبعاد لحفظ الفسيفساء والتماثيل والمواقع الأثرية التي يقارب عمرها ثلاثة آلاف سنة. منذ التأسيس في 2025، وثّق فريقنا التطوعي أكثر من 80 قطعة أثرية في 20 موقعًا، وعقد شراكات مع الجامعة التونسية لوكالات الأسفار وبرنامج التراث الثقافي لدى Sketchfab، وأنجزنا أكبر إعادة بناء رقمية لمسرح الجم حتى اليوم — وقد احتفت بها Niantic Spatial. نشأتُ على بُعد ربع ساعة سيرًا من أطلال نيابوليس الرومانية في نابل — هذا العمل شخصيّ بالنسبة إليّ.',
     'نال عملي المناخي <strong>Shadows of Tomorrow</strong> جائزة التميّز، وقد سلّمتها لي Jane Gilbert، أول مسؤولة عن ملفّ الحرارة في ميامي، والكاتب Jeff Goodell. أمّا <strong>Covid Reflections</strong>، وهو عمل فنّي عام بالواقع المعزَّز، فقد جال فلوريدا وكاليفورنيا واليابان مرافقًا عيادات صحية متنقّلة.',
     'وفي <strong>Froliq</strong>، حيث أعمل بصفة Lead XR Developer، أبتكر تجارب غامرة للتثقيف في مجالي الطاقة والاستدامة — من بينها تجربة <em>Future of Energy and Water</em> لمعرض FUTURES في Smithsonian، الذي زاره أكثر من 600,000 شخص.',
     'نُشرت أبحاثي لدى ACM وIEEE (جائزة أفضل ورقة بحثية في مؤتمر IEEE ISEC 2023)، وصرتُ أجلس أكثر فأكثر في مقاعد التحكيم — لدى Games for Change وEE 30 Under 30، وفي هاكاثون ImmerseGT بجامعة Georgia Tech حيث رعت Tanit XR مسارًا خاصًا بالتراث التونسي.',
     'وبعيدًا عن النظارات، أنا غوّاصة معتمدة، أسعد ما أكون في رحلات المشي ومراقبة الحياة البرية — في الأماكن نفسها التي يحاول عملي حمايتها.'],
   about_caption='في الميدان — أوثّق تراث تونس المهدَّد.',
   quote='«على التعليم أن يجعل الناس يشعرون بارتباطهم بالكوكب، لا أن يكتفي بإخبارهم عنه.»',
   quote_src='من ملفّها في EE 30 Under 30 — NAAEE',
   full_bio='← السيرة الكاملة (بالإنجليزية)'),
}

def lang_nav(L, active):
    ACT = ' class="active"'
    links = ''.join(f'<a href="{u}"{ACT if u.endswith(active) else ""}>{t}</a>' for u, t in L['nav'])
    return ('<header class="site-header"><div class="wrap">'
            f'<a class="brand" href="index.html">Ines Said<em>&thinsp;&#10022;</em></a>'
            f'<nav>{links}</nav>{lang_switch(L["lang"], "../")}</div></header>')

def lang_footer(L):
    return FOOTER.replace('href="mailto', 'href="mailto')  # same footer, contacts are universal

def lang_page(L, title, desc, path, body):
    return (f'<!doctype html><html lang="{L["lang"]}" dir="{L["dir"]}"><head>{HEAD}'
            f'<title>{title}</title><meta name="description" content="{desc}">'
            f'<link rel="canonical" href="{BASE_URL}/{path}">'
            f'<link rel="alternate" hreflang="en" href="{BASE_URL}/">'
            f'<link rel="alternate" hreflang="fr" href="{BASE_URL}/fr/">'
            f'<link rel="alternate" hreflang="ar" href="{BASE_URL}/ar/">'
            f'{FONTS}<style>{CSS}</style></head><body>'
            f'{lang_nav(L, path.split("/")[-1] or "index.html")}{body}{lang_footer(L)}</body></html>')

def lang_home_body(L):
    stats = ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in L['stats'])
    cards = ''.join(
        f'<a class="card" href="{u}"><div class="card-inner"><div class="card-body">'
        f'<h3>{t}</h3><p>{d}</p><span class="card-more">&rarr;</span></div></div></a>'
        for u, t, d in L['featured'])
    return f"""
<div class="photo-band"><div class="strip">
  <figure><img src="../web/statue-pose.jpg" alt=""></figure>
  <figure><img src="../web/mosaic-portrait.jpg" alt="Ines Said"></figure>
  <figure><img src="../web/ets-fireside.jpg" alt=""></figure>
</div></div>
<div class="intro-home">
  <p class="kicker">{L['kicker']}</p>
  <h1>{L['hello']}</h1>
  <p class="lede">{L['lede']}</p>
  <div class="btn-row">
    <a class="btn" href="../projects.html">{L['btn_work']}</a>
    <a class="btn ghost" href="about.html">{L['btn_about']}</a>
  </div>
</div>
<div class="band lav"><div class="wrap"><div class="stats">{stats}</div></div></div>
{SQUIGGLE}
<section class="block"><div class="wrap">
  <h2 class="sec-title">{L['featured_h']}</h2><p class="sec-sub">{L['featured_sub']}</p>
  <div class="cards">{cards}</div>
</div></section>
<div class="band deep"><div class="wrap" style="text-align:center">
  <h2 class="sec-title" style="margin-bottom:10px">{L['speak_h']}</h2>
  <p style="max-width:58ch;margin:0 auto 24px">{L['speak_p']}</p>
  <a class="btn" href="mailto:ines@tanitxr.org?subject=Speaking%20inquiry">{L['speak_btn']}</a>
</div></div>
<div class="band blush"><div class="wrap" style="text-align:center">
  <h2 class="sec-title" style="margin-bottom:10px">{L['support_h']}</h2>
  <p style="max-width:58ch;margin:0 auto 24px">{L['support_p']}</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn" href="https://donors.tuesday.app/campaign/73DO5">{L['support_btn']}</a>
    <a class="btn ghost" href="https://tanitxr.org/volunteer/">{L['volunteer_btn']}</a>
  </div>
</div></div>
"""

def lang_about_body(L):
    paras = ''.join(f'<p>{t}</p>' for t in L['about_paras'])
    return f"""
<div class="wrap"><div class="page-head">
  <p class="kicker">{L['kicker']}</p>
  <h1>{L['about_h1']}</h1>
  <p class="sub">{L['about_sub']}</p>
</div></div>
<section class="block" style="padding-top:36px"><div class="wrap">
  <div class="two-col">
    <div class="prose">{paras}
      <p><a href="../about.html"><strong>{L['full_bio']}</strong></a></p>
    </div>
    <figure class="side-photo">
      <img src="../web/statue-pose.jpg" alt="Ines Said">
      <figcaption>{L['about_caption']}</figcaption>
    </figure>
  </div>
  <div class="pull"><p>{L['quote']}</p><span>{L['quote_src']}</span></div>
</div></section>
"""

def build_langs():
    for code, L in L10N.items():
        d = os.path.join(OUT, code)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(lang_page(L, L['home_title'], L['home_desc'], f'{code}/', lang_home_body(L)))
        with open(os.path.join(d, 'about.html'), 'w', encoding='utf-8') as f:
            f.write(lang_page(L, L['about_title'], L['about_sub'], f'{code}/about.html', lang_about_body(L)))
    print('language pages written: fr/, ar/')

if __name__ == '__main__':
    build_site()
    build_langs()
    build_preview()
