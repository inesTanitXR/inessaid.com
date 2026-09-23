# Rich, Tanit-style section components and page layouts.
# Loaded by build.py (exec'd into its namespace), so it can use href, card_html,
# post_card, PROJECTS, AWARDS, POSTS, embeds_block, NEWSLETTER_URL, SQUIGGLE, etc.

SECTIONS_CSS = r"""
/* polaroid page header */
.phead{position:relative;overflow:hidden;border-bottom:1px solid var(--line)}
.phead-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center;min-height:400px}
.phead .page-head{padding:56px 0 48px}
.phead .page-head h1{font-size:clamp(2.3rem,5vw,3.6rem)}
.phead .crumbs{font-size:.8rem;margin:0 0 16px;color:var(--muted)}
.phead .crumbs a{color:var(--gold);font-weight:700}
.phead .crumbs span{color:var(--body)}
.polaroids{position:relative;height:360px}
.pol{position:absolute;margin:0;background:#fff;padding:10px 10px 36px;border-radius:3px;box-shadow:0 16px 38px rgba(67,32,58,.2);transition:transform .25s}
.pol img{display:block;width:100%;height:100%;object-fit:cover;border-radius:2px}
.pol::before{content:"";position:absolute;top:-13px;left:50%;width:92px;height:26px;margin-left:-46px;background:rgba(232,205,150,.75);border-radius:2px}
.pol.p1{width:60%;height:80%;top:3%;left:2%;transform:rotate(-4deg);z-index:2}
.pol.p2{width:50%;height:66%;bottom:0;right:3%;transform:rotate(5deg)}
.pol.p2::before{transform:rotate(8deg)}
.pol.single{width:70%;height:90%;top:3%;left:14%;transform:rotate(-3deg)}
.phead:hover .pol.p1{transform:rotate(-2deg) translateY(-4px)}
.phead:hover .pol.p2{transform:rotate(3deg) translateY(-4px)}
.pol.ph div{height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;
  background:radial-gradient(circle at 30% 30%,var(--tint-blush),var(--tint-lav));border-radius:2px}
.pol.ph b{font-family:"Yeseva One",serif;font-weight:400;font-size:2.2rem;color:var(--lav)}
.pol.ph span{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
@media(max-width:820px){.phead-grid{grid-template-columns:1fr;gap:0}.phead .page-head{padding:40px 0 10px}.polaroids{height:300px;margin-bottom:36px}}

/* ---------- section components ---------- */
.band [style*="text-align:center"] .sec-title::after,.cta-end .sec-title::after,.recognized .sec-title::after{margin-left:auto;margin-right:auto}
.cta-end + footer, .halfbleed + footer{margin-top:0}
.sec-kicker{font-size:.72rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.center{text-align:center}
.center .sec-title::after{margin-left:auto;margin-right:auto}
.statement{padding:72px 0 40px}
.statement h2{font-size:clamp(1.8rem,3.6vw,2.6rem);max-width:24ch;margin:0 auto 18px}
.statement p{max-width:62ch;margin:0 auto;font-size:1.08rem}
.recognized{background:var(--tint-blush);padding:34px 0 30px}
.recognized .row{display:flex;flex-wrap:wrap;justify-content:center;gap:18px 44px;margin-top:14px}
.recognized a,.recognized div.item{display:flex;flex-direction:column;align-items:center;gap:4px;color:var(--ink);text-align:center;max-width:150px}
.recognized b{font-family:"Yeseva One",serif;font-weight:400;font-size:1.12rem;line-height:1.15}
.recognized span{font-size:.72rem;color:var(--muted);letter-spacing:.02em}
.recognized a:hover{text-decoration:none}
.recognized a:hover b{color:var(--lav)}
/* icon cards */
.icon-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.icon-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 24px 22px;display:flex;flex-direction:column;
  transition:transform .18s,box-shadow .18s;color:inherit}
a.icon-card:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgba(94,34,70,.12);text-decoration:none}
.icon-card svg{width:50px;height:50px;stroke:var(--lav);stroke-width:1.6;fill:none;stroke-linecap:round;stroke-linejoin:round;margin-bottom:14px}
.icon-card h3{font-size:1.18rem;margin:0 0 8px;color:var(--ink)}
.icon-card p{font-size:.93rem;margin:0 0 14px;color:var(--body)}
.icon-card .go{margin-top:auto;font-size:.82rem;font-weight:700;color:var(--gold)}
.icon-card .price{margin-top:auto;font-family:"Yeseva One",serif;font-size:1.25rem;color:var(--lav)}
@media(max-width:900px){.icon-cards{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.icon-cards{grid-template-columns:1fr}}
/* split + collage */
.split{display:grid;grid-template-columns:1.05fr 1fr;gap:56px;align-items:center}
.split.rev .split-media{order:2}
.split h2{font-size:clamp(1.7rem,3.2vw,2.4rem);margin:0 0 14px}
.split p{margin:0 0 14px}
.split ul.ticks{list-style:none;padding:0;margin:6px 0 24px}
.split ul.ticks li{padding:6px 0 6px 26px;position:relative;font-size:.96rem}
.split ul.ticks li::before{content:"\2726";position:absolute;left:0;top:6px;color:var(--gold)}
.collage{display:grid;grid-template-columns:1.4fr 1fr;grid-auto-rows:150px;gap:12px}
.collage figure{margin:0}
.collage img{width:100%;height:100%;object-fit:cover;border-radius:12px;border:6px solid #fff;box-shadow:0 8px 22px rgba(67,32,58,.14);cursor:zoom-in}
.collage figure:first-child{grid-row:span 2}
.collage figure:nth-child(4){grid-column:span 2}
@media(max-width:820px){.split{grid-template-columns:1fr}.split.rev .split-media{order:0}}
/* stats over photo */
.stats-photo{position:relative;padding:70px 0;background:#43203a center/cover no-repeat;color:#fff;overflow:hidden}
.stats-photo::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(52,19,40,.9),rgba(52,19,40,.7))}
.stats-photo .wrap{position:relative}
.stats-photo .nums{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;text-align:center}
.stats-photo b{display:block;font-family:"Yeseva One",serif;font-weight:400;font-size:clamp(2.2rem,4.6vw,3.4rem);color:var(--gold);line-height:1}
.stats-photo span{display:block;margin-top:10px;font-size:.92rem;color:#f3dcd6}
@media(max-width:760px){.stats-photo .nums{grid-template-columns:1fr 1fr}}
/* timeline */
.timeline{position:relative;max-width:860px;margin:0 auto;padding-left:36px}
.timeline::before{content:"";position:absolute;left:11px;top:6px;bottom:6px;width:2px;background:linear-gradient(var(--gold),var(--lav))}
.tl-year{font-family:"Yeseva One",serif;font-size:1.6rem;color:var(--lav);margin:30px 0 12px;position:relative}
.tl-year::before{content:"";position:absolute;left:-31px;top:10px;width:14px;height:14px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 5px var(--cream)}
.tl-item{display:flex;gap:16px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 16px 12px 12px;margin:0 0 10px;color:inherit;transition:transform .15s,box-shadow .15s}
a.tl-item:hover{transform:translateX(4px);box-shadow:0 10px 26px rgba(94,34,70,.1);text-decoration:none}
.tl-item img{width:74px;height:74px;object-fit:cover;border-radius:10px;flex:none}
.tl-item .tl-dot{width:74px;height:74px;border-radius:10px;flex:none;background:var(--tint-lav);display:flex;align-items:center;justify-content:center;color:var(--lav);font-size:1.6rem}
.tl-item b{display:block;font-family:"Yeseva One",serif;font-weight:400;font-size:1.08rem;color:var(--ink)}
.tl-item span{font-size:.88rem;color:var(--muted)}
/* date cards */
.date-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.date-card{display:flex;gap:18px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px;color:inherit}
a.date-card:hover{box-shadow:0 10px 26px rgba(94,34,70,.1);text-decoration:none}
.date-card .d{flex:none;width:64px;text-align:center;border-right:1px solid var(--line);padding-right:16px}
.date-card .d b{display:block;font-family:"Yeseva One",serif;font-weight:400;font-size:1.9rem;color:var(--lav);line-height:1}
.date-card .d span{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.date-card .k{font-size:.7rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.date-card h3{font-size:1.05rem;margin:4px 0 4px;color:var(--ink)}
.date-card p{margin:0;font-size:.88rem;color:var(--body)}
@media(max-width:760px){.date-cards{grid-template-columns:1fr}}
/* quote / press cards */
.quote-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.quote-card{background:#fff;border:1px solid var(--line);border-top:4px solid var(--lav);border-radius:14px;padding:20px 20px 18px;color:inherit;display:flex;flex-direction:column;transition:transform .15s,box-shadow .15s}
.quote-card:nth-child(3n+2){border-top-color:var(--gold)}
.quote-card:nth-child(3n){border-top-color:var(--pink)}
a.quote-card:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(94,34,70,.12);text-decoration:none}
.quote-card .k{font-size:.7rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.quote-card h3{font-size:1.08rem;margin:6px 0 8px;color:var(--ink)}
.quote-card p{margin:0 0 12px;font-size:.88rem}
.quote-card .go{margin-top:auto;font-size:.8rem;font-weight:700;color:var(--lav)}
@media(max-width:900px){.quote-cards{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.quote-cards{grid-template-columns:1fr}}
/* half-bleed */
.halfbleed{display:grid;grid-template-columns:1fr 1fr;min-height:440px}
.halfbleed .hb-img{background:center/cover no-repeat}
.halfbleed .hb-text{background:var(--tint-blush);padding:64px 7vw 64px 56px;display:flex;flex-direction:column;justify-content:center}
.halfbleed.rev .hb-img{order:2}
.halfbleed.rev .hb-text{padding:64px 56px 64px 7vw}
.halfbleed h2{font-size:clamp(1.7rem,3vw,2.3rem);margin:0 0 14px}
.halfbleed h3{font-size:1.15rem;margin:18px 0 6px}
.halfbleed p{margin:0 0 10px;max-width:52ch}
@media(max-width:820px){.halfbleed{grid-template-columns:1fr}.halfbleed .hb-img{min-height:280px}.halfbleed.rev .hb-img{order:0}}
/* filters */
.filters{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:0 0 30px}
.filters button{font:inherit;font-size:.85rem;font-weight:700;border:1.5px solid var(--line);background:#fff;color:var(--ink);border-radius:999px;padding:8px 18px;cursor:pointer;transition:all .15s}
.filters button:hover{border-color:var(--lav)}
.filters button.on{background:var(--lav);border-color:var(--lav);color:#fff}
.filters button .n{opacity:.7;margin-left:4px;font-weight:400}
[data-cat].hide{display:none!important}
.card .cat-tag{position:absolute;top:12px;left:12px;background:#fffffff0;color:var(--lav-deep);font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;border-radius:999px;padding:5px 11px}
.card .thumb{position:relative}
/* platform strip */
.platforms{display:flex;flex-wrap:wrap;justify-content:center;gap:12px}
.platforms span{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--line);border-radius:999px;padding:10px 18px;font-weight:700;font-size:.9rem;color:var(--ink)}
.platforms span::before{content:"\2726";color:var(--gold)}
/* tint feature */
.tint{background:linear-gradient(180deg,var(--tint-blush),var(--cream))}
/* gallery: first image hero */
.gallery{grid-auto-flow:dense}
.gallery figure:first-child{grid-column:span 2;grid-row:span 2}
.gallery figure:first-child img{aspect-ratio:auto;height:100%;min-height:320px}
"""

SECTIONS_JS = r"""<script>
(function(){
  document.querySelectorAll('.filters').forEach(function(bar){
    var scope=document.querySelector(bar.dataset.target);
    if(!scope) return;
    bar.addEventListener('click',function(e){
      var b=e.target.closest('button'); if(!b) return;
      bar.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});
      var f=b.dataset.filter;
      scope.querySelectorAll('[data-cat]').forEach(function(el){
        el.classList.toggle('hide', f!=='all' && el.dataset.cat.split(' ').indexOf(f)<0);
      });
    });
  });
})();
</script>"""

ICONS = {
 'column': '<path d="M10 42h28M12 38h24M14 14h20M12 10h24l-12-6zM16 14v24M24 14v24M32 14v24"/>',
 'headset': '<path d="M6 20c0-3 2-5 5-5h26c3 0 5 2 5 5v8c0 3-2 5-5 5h-7l-3-4h-6l-3 4h-7c-3 0-5-2-5-5z"/><circle cx="16" cy="24" r="3"/><circle cx="32" cy="24" r="3"/>',
 'mic': '<rect x="18" y="5" width="12" height="22" rx="6"/><path d="M11 22c0 7 6 12 13 12s13-5 13-12M24 34v8M17 42h14"/>',
 'trophy': '<path d="M16 6h16v10c0 5-4 9-8 9s-8-4-8-9zM16 9H9c0 6 3 9 7 9M32 9h7c0 6-3 9-7 9M24 25v8M17 42h14l-2-9H19z"/>',
 'gavel': '<path d="M26 8l12 12M22 12l12 12M24 10l-8 8 12 12 8-8M20 22L7 35l4 4 13-13M8 44h20"/>',
 'globe': '<circle cx="24" cy="24" r="17"/><path d="M7 24h34M24 7c5 5 7 11 7 17s-2 12-7 17c-5-5-7-11-7-17s2-12 7-17z"/>',
 'spark': '<path d="M24 5l4 15 15 4-15 4-4 15-4-15-15-4 15-4z"/>',
 'book': '<path d="M8 10c6-2 11-1 16 3 5-4 10-5 16-3v28c-6-2-11-1-16 3-5-4-10-5-16-3zM24 13v28"/>',
 'cube': '<path d="M24 5l16 9v20l-16 9-16-9V14zM24 5v38M8 14l16 9 16-9"/>',
 'camera': '<rect x="6" y="14" width="36" height="24" rx="4"/><circle cx="24" cy="26" r="7"/><path d="M17 14l3-5h8l3 5"/>',
 'wave': '<path d="M5 20c5-5 9-5 14 0s9 5 14 0 9-5 10-4M5 30c5-5 9-5 14 0s9 5 14 0 9-5 10-4M5 40c5-5 9-5 14 0s9 5 14 0 9-5 10-4"/><circle cx="36" cy="10" r="4"/>',
 'people': '<circle cx="17" cy="16" r="6"/><circle cx="33" cy="18" r="5"/><path d="M5 40c0-7 5-12 12-12s12 5 12 12M29 40c0-5 2-9 6-10 5 0 8 4 8 10"/>',
 'bulb': '<path d="M18 36h12M19 41h10M24 5c-8 0-13 6-13 12 0 5 3 8 5 11 1 2 2 4 2 6h12c0-2 1-4 2-6 2-3 5-6 5-11 0-6-5-12-13-12z"/>',
 'game': '<rect x="5" y="15" width="38" height="20" rx="10"/><path d="M14 21v8M10 25h8"/><circle cx="31" cy="23" r="1.5"/><circle cx="36" cy="27" r="1.5"/>',
 'palette': '<path d="M24 5C13 5 5 13 5 23c0 9 7 16 15 16 3 0 4-2 3-4s0-5 3-5h5c7 0 12-4 12-10 0-9-9-15-19-15z"/><circle cx="15" cy="20" r="2.5"/><circle cx="22" cy="13" r="2.5"/><circle cx="31" cy="14" r="2.5"/>',
 'dive': '<circle cx="24" cy="12" r="5"/><path d="M8 26c5 4 11 4 16 0s11-4 16 0M8 34c5 4 11 4 16 0s11-4 16 0M8 42c5 4 11 4 16 0s11-4 16 0"/>',
 'mountain': '<path d="M4 40l14-22 8 12 5-7 13 17z"/><circle cx="35" cy="11" r="4"/>',
 'tanit': '<circle cx="24" cy="9" r="5"/><path d="M8 20h32M8 20v-5M40 20v-5M24 15L11 43h26z"/>',
 'screen': '<rect x="5" y="8" width="38" height="24" rx="3"/><path d="M17 40h14M24 32v8"/>',
 'pin': '<path d="M24 44s14-13 14-24a14 14 0 10-28 0c0 11 14 24 14 24z"/><circle cx="24" cy="20" r="5"/>',
 'news': '<rect x="6" y="8" width="30" height="32" rx="3"/><path d="M36 16h6v20a4 4 0 01-8 0M12 16h18M12 23h18M12 30h11"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 48 48" aria-hidden="true">{ICONS[name]}</svg>'

def statement(kicker, title, text):
    return (f'<section class="statement center"><div class="wrap"><p class="sec-kicker">{kicker}</p>'
            f'<h2 class="sec-title">{title}</h2><p>{text}</p></div></section>')

def recognized(title, items):
    cells = ''.join(
        (f'<a href="{u}"><b>{n}</b><span>{c}</span></a>' if u else f'<div class="item"><b>{n}</b><span>{c}</span></div>')
        for n, c, u in items)
    return f'<section class="recognized center"><div class="wrap"><p class="sec-kicker">{title}</p><div class="row">{cells}</div></div></section>'

def icon_cards(items):
    out = []
    for ic, title, text, link, label in items:
        tail = f'<span class="go">{label} &rarr;</span>' if link else (f'<span class="price">{label}</span>' if label else '')
        tag = 'a' if link else 'div'
        attr = f' href="{link}"' if link else ''
        out.append(f'<{tag} class="icon-card"{attr}>{icon(ic)}<h3>{title}</h3><p>{text}</p>{tail}</{tag}>')
    return f'<div class="icon-cards">{"".join(out)}</div>'

def section(inner, kicker='', title='', sub='', cls='', center=True):
    head = ''
    if title:
        head = (f'<div class="{"center" if center else ""}" style="margin-bottom:34px">'
                f'{f"<p class=sec-kicker>{kicker}</p>" if kicker else ""}<h2 class="sec-title">{title}</h2>'
                f'{f"<p class=sec-sub style=margin-left:auto;margin-right:auto>{sub}</p>" if sub and center else (f"<p class=sec-sub>{sub}</p>" if sub else "")}</div>')
    return f'<section class="block {cls}"><div class="wrap">{head}{inner}</div></section>'

def collage(imgs):
    figs = ''.join(f'<figure><img src="web/{i}.jpg" alt="{a}" loading="lazy"></figure>' for i, a in imgs[:5])
    return f'<div class="collage">{figs}</div>'

def split(media_html, kicker, title, paras, ticks=None, buttons=None, rev=False):
    ps = ''.join(f'<p>{p}</p>' for p in paras)
    tk = ('<ul class="ticks">' + ''.join(f'<li>{t}</li>' for t in ticks) + '</ul>') if ticks else ''
    bt = ''
    if buttons:
        bt = '<div class="btn-row">' + ''.join(
            f'<a class="btn{" ghost" if i else ""}" href="{u}">{l}</a>' for i, (l, u) in enumerate(buttons)) + '</div>'
    return (f'<div class="split{" rev" if rev else ""}"><div class="split-media">{media_html}</div>'
            f'<div><p class="sec-kicker">{kicker}</p><h2>{title}</h2>{ps}{tk}{bt}</div></div>')

def stats_photo(img, nums):
    cells = ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in nums)
    return (f'<section class="stats-photo" style="background-image:url(web/{img}.jpg)"><div class="wrap">'
            f'<div class="nums">{cells}</div></div></section>')

def timeline(years):
    out = []
    for year, items in years:
        out.append(f'<div class="tl-year">{year}</div>')
        for title, sub, link, img in items:
            th = f'<img src="web/{img}.jpg" alt="" loading="lazy">' if img else '<div class="tl-dot">&#10022;</div>'
            tag = 'a' if link else 'div'
            attr = f' href="{link}"' if link else ''
            out.append(f'<{tag} class="tl-item"{attr}>{th}<div><b>{title}</b><span>{sub}</span></div></{tag}>')
    return f'<div class="timeline">{"".join(out)}</div>'

def date_cards(items):
    out = []
    for day, mon, kicker, title, text, link in items:
        tag = 'a' if link else 'div'
        attr = f' href="{link}"' if link else ''
        out.append(f'<{tag} class="date-card"{attr}><div class="d"><b>{day}</b><span>{mon}</span></div>'
                   f'<div><span class="k">{kicker}</span><h3>{title}</h3><p>{text}</p></div></{tag}>')
    return f'<div class="date-cards">{"".join(out)}</div>'

def quote_cards(items):
    out = []
    for kicker, title, text, link, label in items:
        out.append(f'<a class="quote-card" href="{link}"><span class="k">{kicker}</span><h3>{title}</h3>'
                   f'<p>{text}</p><span class="go">{label} &rarr;</span></a>')
    return f'<div class="quote-cards">{"".join(out)}</div>'

def halfbleed(img, pos, kicker, title, blocks, buttons=None, rev=False):
    body = ''
    for h, p in blocks:
        body += (f'<h3>{h}</h3>' if h else '') + f'<p>{p}</p>'
    bt = ''
    if buttons:
        bt = '<div class="btn-row" style="margin-top:16px">' + ''.join(
            f'<a class="btn{" ghost" if i else ""}" href="{u}">{l}</a>' for i, (l, u) in enumerate(buttons)) + '</div>'
    return (f'<section class="halfbleed{" rev" if rev else ""}"><div class="hb-img" style="background-image:url(web/{img}.jpg);background-position:{pos}"></div>'
            f'<div class="hb-text"><p class="sec-kicker">{kicker}</p><h2>{title}</h2>{body}{bt}</div></section>')

def filters(target, cats, counts):
    total = sum(counts.values())
    btns = f'<button class="on" data-filter="all">All<span class="n">{total}</span></button>' + ''.join(
        f'<button data-filter="{k}">{lbl}<span class="n">{counts.get(k, 0)}</span></button>' for k, lbl in cats)
    return f'<div class="filters" data-target="{target}">{btns}</div>'

def head_block(kicker, h1, sub):
    # the bannerize() step turns this into a photo banner
    return f'<div class="wrap"><div class="page-head"><p class="kicker">{kicker}</p><h1>{h1}</h1><p class="sub">{sub}</p></div></div>'


# ======================= PAGES =======================

def body_about(preview):
    H = lambda p: href(p, preview)
    return head_block('About', 'Art, technology &amp; a little bit of magic.',
                      'Immersive artist and XR developer from Tunisia.') + \
    statement('Hi, I\'m Ines!', "I grew up a 15-minute walk from Roman ruins.",
        "Today I help preserve places like them in 3D. I'm an immersive artist and XR developer from Tunisia, and I love "
        "using art and technology to protect our heritage, talk about climate change and make learning more fun.") + \
    section(split(collage([('statue-pose', 'Ines matching poses with an ancient statue'),
                           ('mosaic-portrait', 'Ines in front of an ancient mosaic'),
                           ('el-jem', 'Ines at the El Jem Amphitheater'),
                           ('neapolis-swim', 'Searching for sunken Neapolis')]),
        'What I do', 'Heritage, climate and a lot of heart',
        ["I founded <strong>Tanit XR</strong>, Tunisia's first open-source heritage archive. With our amazing volunteers, "
         "we've scanned more than 80 artifacts across 20 sites, including the El Jem Amphitheater!",
         "At <strong>Froliq</strong>, I'm the Lead XR Developer. I build VR and AR experiences that teach people about "
         "energy and sustainability, from the Smithsonian's FUTURES exhibition to Oracle's Connected Hub."],
        ticks=['Founder, Tanit XR (2025–)', 'Lead XR Developer, Froliq (2023–)',
               'Author of the weekly <a href="%s">Art, XR &amp; Impact Opportunities</a> newsletter' % NEWSLETTER_URL,
               'Living between Washington, D.C. and Tunisia, and I speak English, Arabic and French'],
        buttons=[('See my projects', H('projects')), ('Invite me to speak', H('speaking'))])) + \
    stats_photo('el-jem', [('600K+', 'visitors to the Smithsonian exhibition featuring my work'),
                           ('80+', 'artifacts preserved in 3D with Tanit XR'),
                           ('11K+', 'people reached in 2025 across 40+ events'),
                           ('3', 'languages I present in')]) + \
    section(icon_cards([
        ('tanit', 'Heritage preservation', "Scanning Tunisia's mosaics, statues and ruins before we lose them.", H('p-tanit-xr'), 'Tanit XR'),
        ('wave', 'Climate art', 'Installations that help people feel climate change, not just read about it.', H('p-shadows-of-tomorrow'), 'Shadows of Tomorrow'),
        ('headset', 'XR development', 'Apple Vision Pro, Meta Quest, mobile AR and WebXR for museums and industry.', H('p-oracle-connected-hub'), 'Connected Hub'),
        ('game', 'Learning &amp; play', 'VR games and even a soccer game that teach kids about energy.', H('p-froliq-minigames'), 'The mini-games'),
        ('book', 'Research', 'Published in ACM and IEEE, including a 2023 Best Paper Award.', H('a-ieee-best-paper'), 'The paper'),
        ('people', 'Community &amp; mentoring', 'Workshops, judging and a newsletter full of opportunities for creatives.', 'https://tanitxr.org/opportunities/', 'See the opportunities'),
    ]), 'What I do', 'The things I love working on') + \
    section(timeline([
        ('2026', [('Auggie Awards finalist — Best Societal Impact', 'Tanit XR at Augmented World Expo', H('a-auggie-finalist'), 'auggie-finalist'),
                  ('Presented inside the El Jem Amphitheater', 'El Jem International Conference, Tunisia', H('b-el-jem-colosseum'), 'eljem-conf'),
                  ('Spoke on the main stage at the Energy Thought Summit', 'San Antonio, TX', H('speaking'), 'ets-stage')]),
        ('2025', [('Founded Tanit XR', "Tunisia's first open-source heritage archive", H('p-tanit-xr'), 'tanit-birthday'),
                  ('EE 30 Under 30, Class of 2025', 'North American Association for Environmental Education', H('a-ee-30-under-30'), 'ee30')]),
        ('2023', [('Lead XR Developer at Froliq', 'Leading immersive projects for energy and education', H('projects'), 'oracle-booth'),
                  ('IEEE Best Paper Award', 'Mini VR game engines as a way to learn', H('a-ieee-best-paper'), 'vr-portrait')]),
        ('2022', [('Joined Froliq · Smithsonian FUTURES', 'Future of Energy &amp; Water installation', H('p-smithsonian-futures'), 'futures-wide'),
                  ('Covid Reflections launches', 'AR public art toured Florida, California &amp; Japan', H('p-covid-reflections'), 'covid-truck')]),
        ('2020–21', [("M.S. Digital Arts &amp; Sciences", 'University of Florida — Digital Worlds Institute', None, None)]),
        ('2015–19', [('B.E. Computer Science', 'University of South Florida · exchange at Deakin University', None, None),
                     ('3D Virtualization Lab', 'My very first 3D scans, and the dream of doing this for Tunisia', None, None)]),
    ]), 'My journey', 'How I got here', cls='tint') + \
    '<div class="wrap"><div class="pull"><p>"Education should make people feel connected to the planet, not just informed about it."</p>' \
    '<span>From her EE 30 Under 30 profile — NAAEE</span></div></div>' + \
    halfbleed('coast-walk', 'center 40%', 'Outside of work', "When I'm not in a headset", [
        ("I'm a certified scuba diver", "The ocean is my happy place. Tunisia even has sunken cities to look for!"),
        ('I love hiking &amp; spotting wildlife', "I'm happiest on a trail, looking for animals I've never seen before."),
        ('I paint and make things by hand', 'Watercolor, drawing and little crafts. It feels so good to make something you can hold.'),
    ], buttons=[('Read my blog', H('blog'))]) + \
    section('<div class="two-col"><div><h2 class="sec-title" style="font-size:1.5rem">Experience</h2><ul class="list">'
        '<li><div><span class="t">Founder — Tanit XR</span><div class="d">Open-source digital heritage archive; 80+ artifacts across 20 sites</div></div><span class="who">2025–</span></li>'
        '<li><div><span class="t">Lead XR Developer — Froliq</span><div class="d">Leading XR projects from concept to execution</div></div><span class="who">2023–</span></li>'
        '<li><div><span class="t">XR Developer — Froliq</span><div class="d">Smithsonian FUTURES installation and VR energy-education games</div></div><span class="who">2022–23</span></li>'
        '<li><div><span class="t">Adjunct Lecturer — University of Florida</span><div class="d">Taught VR application development for Android and wearables</div></div><span class="who">2023</span></li>'
        '<li><div><span class="t">Software Engineer — University of Florida</span></div><span class="who">2021–23</span></li>'
        '<li><div><span class="t">3D Virtualization Lab Intern — USF</span><div class="d">Artec scanners, drones, photogrammetry</div></div><span class="who">2018–19</span></li>'
        '</ul></div><div><h2 class="sec-title" style="font-size:1.5rem">Education</h2><ul class="list">'
        '<li><div><span class="t">M.S. Digital Arts &amp; Sciences</span><div class="d">University of Florida — MiDAS, Digital Worlds Institute</div></div><span class="who">2020–21</span></li>'
        '<li><div><span class="t">B.E. Computer Science</span><div class="d">University of South Florida</div></div><span class="who">2015–19</span></li>'
        '<li><div><span class="t">Exchange — Computer Science</span><div class="d">Deakin University, Australia</div></div><span class="who">2017</span></li>'
        '</ul></div></div>', 'My background', 'Experience &amp; education')


PROJECT_CATS = {
    'tanit-xr': 'heritage', 'sparc': 'art research', 'shadows-of-tomorrow': 'art climate',
    'covid-reflections': 'art health', 'smithsonian-futures': 'art energy',
    'oracle-connected-hub': 'energy', 'nypa-vision-pro': 'energy', 'vistra-tour': 'energy',
    'nuclear-capture': 'energy heritage', 'froliq-minigames': 'learning', 'sustainaball': 'learning',
    'stevie': 'learning', 'exelon-stem': 'learning',
}
CAT_LABELS = [('heritage', 'Heritage'), ('art', 'Art &amp; installations'), ('energy', 'Energy &amp; industry'),
              ('learning', 'Learning &amp; play'), ('climate', 'Climate')]

def card_cat(p, preview, cat_label):
    html = card_html(p, preview)
    html = html.replace('<a class="card"', f'<a class="card" data-cat="{PROJECT_CATS.get(p["slug"], "")}"', 1)
    return html.replace('<div class="thumb', f'<div class="thumb', 1).replace(
        '</div><div class="card-body">', f'<span class="cat-tag">{cat_label}</span></div><div class="card-body">', 1)

def body_projects(preview):
    H = lambda p: href(p, preview)
    counts = {}
    for s, c in PROJECT_CATS.items():
        for k in c.split():
            counts[k] = counts.get(k, 0) + 1
    label = {k: re.sub('&amp;', '&', v) for k, v in CAT_LABELS}
    cards = ''.join(card_cat(p, preview, label.get(PROJECT_CATS.get(p['slug'], '').split()[0], '').replace('&', '&amp;'))
                    for p in PROJECTS if p['slug'] != 'tanit-xr')
    return head_block('Portfolio', 'Projects', 'Heritage, art, energy and education. Here is some of the work I\'m most proud of.') + \
    section(split(collage([('el-jem', 'El Jem Amphitheater'), ('tanit-archive', 'Tanit XR scanned artifacts'),
                           ('tanit-museum-1', 'Tanit XR virtual museum'), ('site-visit', 'Scouting sites in Tunisia')]),
        'My heart project', 'Tanit XR',
        ["Tunisia's first open-source archive of endangered artifacts. Our volunteers scan statues, mosaics and ruins "
         "with their phones, and our community turns them into 3D models, a virtual museum and AR experiences."],
        ticks=['80+ artifacts across 20 sites', 'Largest reconstruction of the El Jem Amphitheater to date',
               'Auggie Awards finalist, Best Societal Impact (2026)', 'Featured by Al Jazeera and Niantic Spatial'],
        buttons=[('Read the full story', H('p-tanit-xr')), ('Visit tanitxr.org', 'https://tanitxr.org')])) + \
    section(filters('#proj-grid', CAT_LABELS, {k: counts.get(k, 0) for k, _ in CAT_LABELS}) +
            f'<div class="cards" id="proj-grid">{cards}</div>',
            'Explore', 'All my projects', 'Pick a topic, and click any project to read the full story.', cls='tint') + \
    stats_photo('futures-wide', [('13', 'projects and counting'), ('600K+', 'museum visitors reached'),
                                 ('5', 'platforms, from Vision Pro to the web'), ('4', 'countries exhibited')]) + \
    section('<div class="platforms"><span>Apple Vision Pro</span><span>Meta Quest 3</span><span>iPad &amp; iPhone AR</span>'
            '<span>WebXR</span><span>Unity</span><span>Photogrammetry</span><span>Gaussian splats</span><span>Projection mapping</span></div>',
            'What I work with', 'My favorite tools') + \
    cta_band("Let's work together", 'Have a project in mind?',
             "I'd love to hear about it! Whether you want to scan a collection or build something in XR, let's talk.",
             ('Start a conversation', H('speaking') + ('' if preview else '#book')), ('Download my one-pager', 'web/ines-said-speaker.pdf'))


def body_awards(preview):
    H = lambda p: href(p, preview)
    return head_block('Recognition', 'Awards &amp; Recognition',
                      'I feel so lucky and grateful for every one of these, and for the people behind them.') + \
    recognized('Recognized by', [
        ('Auggie Awards', 'Finalist · 2026', H('a-auggie-finalist')),
        ('NAAEE', 'EE 30 Under 30 · 2025', H('a-ee-30-under-30')),
        ('IEEE', 'Best Paper · 2023', H('a-ieee-best-paper')),
        ('GFAA', 'Excellence Award', H('a-gfaa-excellence')),
        ('Smithsonian', 'FUTURES exhibition', H('p-smithsonian-futures')),
        ('AWE XR Prize', 'MVP finalist', H('a-awe-xr-prize')),
    ]) + \
    section(split(collage([('auggie-finalist', 'Tanit XR team, Auggie finalists'), ('auggie-night', 'Auggie Awards night'),
                           ('vision-board', 'The Auggies on the vision board'), ('awe-entrance', 'Arriving at AWE 2026')]),
        'Latest news · 2026', 'We were finalists at the Auggie Awards!',
        ["I put the Auggies on my vision board in January, and by May, Tanit XR was a finalist for <strong>Best Societal "
         "Impact</strong>! The Auggies are the biggest awards in XR, presented at Augmented World Expo in Long Beach."],
        ticks=['Thank you so much to everyone who voted for us', 'Our team got one of the loudest cheers in the room', 'And the next day, I saw a whale jump out of the ocean!'],
        buttons=[('Read the story', H('a-auggie-finalist')), ('The whale post', H('b-auggie-finalist-whale'))])) + \
    section(timeline([
        ('2026', [('Auggie Awards Finalist — Best Societal Impact', 'Augmented World Expo · Tanit XR', H('a-auggie-finalist'), 'auggie-finalist'),
                  ('Judge — EE 30 Under 30, Class of 2026', 'NAAEE', 'https://naaee.org/programs/ee-30-under-30', 'ee30-class'),
                  ('Judge — HICC', "UF Warrington's Heavener International Case Competition", 'https://warrington.ufl.edu/undergraduate/hicc/', None),
                  ('Track sponsor &amp; judge — ImmerseGT', "Georgia Tech's 36-hour XR hackathon", 'https://tanitxr.org/immersegt-2026/', None)]),
        ('2025', [('EE 30 Under 30 — Class of 2025', 'North American Association for Environmental Education', H('a-ee-30-under-30'), 'ee30')]),
        ('2023', [('Best Paper Award — IEEE ISEC', 'With Dr. Angelos Barmpoutis and Wenbin Guo', H('a-ieee-best-paper'), 'vr-portrait')]),
        ('Along the way', [('Excellence Award — GFAA Biennial', 'For Shadows of Tomorrow', H('a-gfaa-excellence'), 'heat'),
                           ('XR Prize Challenge — MVP Finalist', 'Augmented World Expo', H('a-awe-xr-prize'), 'heat-door'),
                           ('Hackathon wins — Google, IBM &amp; MIT', 'MiDAS cohort and MIT Reality Hack', H('a-hackathon-wins'), 'rh-printed-award'),
                           ('Smithsonian FUTURES', '600,000+ visitors', H('p-smithsonian-futures'), 'futures-wide')]),
    ]), 'Timeline', 'All my awards', 'Click any of them to read the story behind it.', cls='tint') + \
    stats_photo('auggie-night', [('7', 'honors &amp; recognitions'), ('5', 'judging roles'),
                                 ('3', 'continents where my work has been shown'), ('1', 'whale sighting, just saying')]) + \
    section(icon_cards([
        ('gavel', 'Games for Change Awards', 'Judging the top industry honors for games with real-world impact.', 'https://www.gamesforchange.org/', 'Games for Change'),
        ('game', 'G4C Student Challenge', 'The largest student game-design competition in the U.S.', 'https://www.gamesforchange.org/studentchallenge/', 'The challenge'),
        ('mountain', 'EE 30 Under 30 · 2026', 'Selecting the next class of environmental-education leaders.', 'https://naaee.org/programs/ee-30-under-30', 'NAAEE'),
        ('trophy', 'HICC', "Judging global business teams at UF's Heavener International Case Competition.", 'https://warrington.ufl.edu/undergraduate/hicc/', 'HICC'),
        ('tanit', 'ImmerseGT track', 'Tanit XR sponsored and judged a Tunisian-heritage hackathon track.', 'https://tanitxr.org/immersegt-2026/', 'The track'),
        ('spark', 'Need a judge?', "I'd love to help judge your competition or hackathon!", H('speaking') + ('' if preview else '#book'), 'Invite me to judge'),
    ]), 'Judging', 'I also love being a judge') + \
    cta_band('Speaking', 'Want me to speak at your event?',
             "I'd love to share these stories with your audience, in English, Arabic or French.",
             ('Book me to speak', H('speaking') + ('' if preview else '#book')), ('See my projects', H('projects')))


def body_speaking(preview):
    H = lambda p: href(p, preview)
    form = re.search(r'<form class="contact-form".*?</form>', _OLD_SPEAKING(preview), re.S).group(0)
    return head_block('Speaking &amp; Media', "I'd love to speak at your event!",
                      'I talk about heritage, climate and how XR can make learning more fun.') + \
    section(split(collage([('ets-stage', 'Ines on the Energy Thought Summit main stage'), ('stage', 'Ines on stage at ELLEvate'),
                           ('dmv-panel', 'Beyond the Byte panel'), ('speaker-card', 'AWE USA 2026 speaker card')]),
        'Keynotes · Panels · Workshops', 'Let\'s work together',
        ["I give keynotes, panels, workshops and university guest lectures, in person or online, in "
         "<strong>English, Arabic or French</strong>. I've spoken everywhere from AWE to inside a Roman amphitheater in Tunisia!"],
        ticks=['In 2025, I got to meet more than 11,000 people at 40+ events',
               'My LinkedIn posts reached 167K views this past year, so I always share the events I speak at',
               "I've worked with teams at Oracle Utilities, Exelon, Vistra, NYPA, the Smithsonian and NEF"],
        buttons=[('Book me to speak', '#book'), ('Speaker one-pager (PDF)', 'web/ines-said-speaker.pdf')])) + \
    recognized('Recent stages', [
        ('AWE USA', 'Speaker · 2022 &amp; 2026', 'https://www.awexr.com/usa-2026/speakers/2677-ines-said'),
        ('Energy Thought Summit', 'Main stage · 2026', 'https://energythoughtsummit.com/'),
        ('El Jem Conference', 'Inside the amphitheater', 'https://tanitxr.org/el-jem-conference/'),
        ('Games for Change', 'Speaker · 2022', 'https://www.youtube.com/watch?v=RNaUaQgXaio'),
        ('Global XR Conference', 'Speaker · 2022', 'https://www.youtube.com/watch?v=FMcdT8H5ffE'),
        ('Inloco Gallery', 'MetaTalks · 2025', 'https://x.com/InlocoG21235/status/1989010660512985594'),
    ]) + \
    section(icon_cards([
        ('column', 'XR for cultural heritage', 'How a phone and a group of volunteers can save 3,000 years of history.', '#book', 'Book this talk'),
        ('wave', 'Climate and art', 'How immersive art can help people feel climate change in a personal way.', '#book', 'Book this talk'),
        ('cube', 'From scans to XR', 'My step-by-step process for 3D scanning, from phone to headset.', '#book', 'Book this talk'),
        ('headset', 'XR for industry', 'How VR and AR help energy companies train people and share their work.', '#book', 'Book this talk'),
        ('game', 'Learning through play', 'Why students learn best by building, with games, VR and hackathons.', '#book', 'Book this talk'),
        ('people', 'Women in XR', 'My journey in immersive tech, and building a community of women around it.', '#book', 'Book this talk'),
    ]), 'Topics', 'What I love talking about') + \
    section(date_cards([
        ('24', 'Sep 26', 'Video · Spatial Creator Spotlight', 'My episode premieres!', 'I talked about my journey, Tanit XR and XR for good. Come watch!', 'https://youtu.be/CY6u3LGEN3E'),
        ('18', 'Jun 26', 'AWE USA 2026 · Long Beach', 'From Scans to XR: A Practical Pipeline for Cultural Heritage', 'With Margarita Johnson of Tanit XR.', 'https://www.awexr.com/usa-2026/speakers/2677-ines-said'),
        ('27', 'Apr 26', 'Energy Thought Summit · San Antonio', 'Photogrammetry for energy &amp; heritage', 'Main stage, with Froliq and Tanit XR.', 'https://energythoughtsummit.com/'),
        ('Apr', '2026', 'El Jem International Conference', 'Presenting Tanit XR inside the Roman amphitheater', 'Paper published in English, French &amp; Tunisian Arabic.', 'https://tanitxr.org/el-jem-conference/'),
        ('8', 'Apr 26', 'Crystal City, VA', 'XR, AI &amp; immersive technology — panel', 'A D.C.-area panel on the future of immersive tech.', None),
        ('Nov', '2025', 'Inloco Gallery · MetaTalks', 'Immersive art &amp; spatial storytelling', 'Panel hosted by Inloco Gallery.', 'https://x.com/InlocoG21235/status/1989010660512985594'),
        ('2026', 'DMV', 'Beyond the Byte', 'Panel on immersive technology', 'In the Washington, D.C. area.', None),
    ]), 'Where I\'ve been', 'Recent talks', cls='tint') + \
    section(icon_cards([
        ('mic', 'Keynote', 'A 30 to 45 minute talk, made for your audience.', None, 'from $2,000'),
        ('camera', 'Workshop', 'A hands-on half day of 3D scanning or XR with your team.', None, 'from $2,500'),
        ('people', 'Panel or lecture', 'Panels, fireside chats and guest lectures at universities.', None, 'from $750'),
        ('screen', 'Virtual talk', 'Any topic, live online, wherever you are.', None, 'from $500'),
        ('bulb', 'XR development', 'I can help you build your idea for Vision Pro, Quest, phones or the web.', '#book', "Let's talk"),
        ('tanit', 'Heritage scanning', 'Scanning, 3D archives and virtual museums for your collection, like we do at Tanit XR.', '#book', "Let's talk"),
    ]), 'Work with me', 'Ways we can work together', 'I offer lower rates for community groups, nonprofits and students, so please just ask!') + \
    section(embeds_block([
        dict(kind='youtube', id='CY6u3LGEN3E', title='NEW: My episode of Spatial Creator Spotlight (2026)'),
        dict(kind='youtube', id='88-GTiDBTCc', title='Faster Iteration in AR Using Unity — AWE 2022'),
        dict(kind='youtube', id='RNaUaQgXaio', title='Playful Resilience — Games for Change 2022'),
        dict(kind='youtube', id='FMcdT8H5ffE', title='AR in Public Health Awareness — Global XR Conference 2022'),
    ], preview), 'Watch', 'Some of my talks', cls='tint') + \
    section(f'<div class="split"><div><p class="sec-kicker">Booking</p><h2 id="book">Let\'s talk</h2>'
            f'<p>Want me to speak, run a workshop or work on a project with you? Send me a message and I\'ll get back to you within a few days!</p><ul class="ticks" style="list-style:none;padding:0">'
            f'<li style="padding:6px 0 6px 26px;position:relative">&#10022; ines@tanitxr.org</li>'
            f'<li style="padding:6px 0 6px 26px;position:relative">&#10022; Based in D.C. and Tunisia, and happy to travel</li></ul></div>'
            f'<div>{form}</div></div>')


def body_press(preview):
    AJ = ('https://www.aljazeera.net/amp/culture/2025/10/12/%D8%AA%D8%A7%D9%86%D9%8A%D8%AA-%D8%A5%D9%83%D8%B3-%D8%A2%D8%B1-'
          '%D9%85%D9%86%D8%B5%D8%A9-%D8%BA%D9%8A%D8%B1-%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9-%D8%AA%D9%88%D8%AB%D9%82')
    return head_block('In the news', 'Press', 'Thank you to everyone who has shared our work!') + \
    recognized('As featured in', [
        ('Al Jazeera', 'Culture · 2025', AJ), ('Niantic Spatial', 'Video feature · 2026', 'https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873/'),
        ('ABC', 'WCJB · 2022', 'https://www.wcjb.com/2022/04/11/university-florida-launches-covid-reflections-project-utilizing-ai-increase-vaccination/'),
        ('CBS', 'CBS4 News', 'https://mycbs4.com/news/local/university-of-florida-vaccine-exhibit'),
        ('UF News', '2022', 'https://news.ufl.edu/2022/04/covid-reflections/'),
        ('Carthage Magazine', 'Feature', 'https://carthagemagazine.com/tanit-xr-preserving-tunisias-heritage-through-immersive-technology/'),
    ]) + \
    halfbleed('site-visit', 'center 40%', 'Featured story · Al Jazeera', "A non-profit platform documenting Tunisia's heritage", [
        (None, "In 2025, Al Jazeera wrote about Tanit XR and how our volunteers are using their phones to build Tunisia's "
               "first open 3D archive of endangered heritage. I was so happy to see our story shared in Arabic!"),
    ], buttons=[('Read on Al Jazeera', AJ), ('About Tanit XR', href('p-tanit-xr', preview))]) + \
    section(quote_cards([
        ('Video · Spatial Creator Spotlight · 2026', 'My episode of Spatial Creator Spotlight', 'A conversation about my journey, Tanit XR and using XR for good. The full episode is on YouTube!', 'https://youtu.be/CY6u3LGEN3E', 'Watch'),
        ('Video · Niantic Spatial · 2026', 'El Jem "sets a benchmark for large-scale reality capture"', "Niantic Spatial featured Tanit XR's multi-scan reconstruction of the El Jem Amphitheater.", 'https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873/', 'Watch'),
        ('Magazine · Carthage Magazine', "Preserving Tunisia's heritage through immersive technology", 'A feature on Tanit XR, its volunteers and its open archive.', 'https://carthagemagazine.com/tanit-xr-preserving-tunisias-heritage-through-immersive-technology/', 'Read'),
        ('TV · ABC 20 WCJB · 2022', 'UF launches "Covid Reflections"', 'Local TV covers the AR public art project paired with vaccine clinics.', 'https://www.wcjb.com/2022/04/11/university-florida-launches-covid-reflections-project-utilizing-ai-increase-vaccination/', 'Watch'),
        ('TV · CBS4 News', 'University of Florida vaccine exhibit', 'CBS4 visits Covid Reflections on the road in Florida.', 'https://mycbs4.com/news/local/university-of-florida-vaccine-exhibit', 'Watch'),
        ('News · UF News · 2022', 'Using AI in the arts to promote COVID-19 vaccines', "The university's story on Covid Reflections.", 'https://news.ufl.edu/2022/04/covid-reflections/', 'Read'),
        ('TV · CBS4 News', 'UF artists host "In the Machine" at 4Most Gallery', 'An exhibition at the convergence of technology and art.', 'https://mycbs4.com/news/local/uf-artists-host-in-the-machine-exhibit-at-4most-gallery', 'Watch'),
        ('Blog · UF Digital Worlds', '"In the Machine": technology converges with art', 'Faculty and alumni collaborate on a technology-and-art exhibition.', 'https://ufdigitalworlds.medium.com/uf-digital-worlds-faculty-and-alumni-collaborate-for-in-the-machine-exhibition-showcasing-the-e9b3f8fd2582', 'Read'),
        ('News · UF College of the Arts', 'MiDAS cohort builds a track record of hackathon success', 'Hackathon wins backed by Google and IBM.', 'https://arts.ufl.edu/in-the-loop/news/midas-cohort-builds-track-record-of-hackathon-success/', 'Read'),
        ('Writing · Medium — Women Write', 'Tanit XR, in my own words', 'Why I started Tunisia\'s first open-source heritage archive.', 'https://medium.com/women-write/tanit-xr-preserving-tunisias-heritage-through-immersive-technology-c9238dab7675', 'Read'),
    ]), 'Coverage', 'Stories about our work', cls='tint') + \
    section('<div class="media-strip"><figure><img src="web/news-abc.jpg" alt="TV news segment on Covid Reflections"><figcaption>Covid Reflections on the evening news.</figcaption></figure>'
            '<figure><img src="web/carthage-mag.jpg" alt="Carthage Magazine feature on Tanit XR"><figcaption>Tanit XR in Carthage Magazine.</figcaption></figure></div>',
            'Clippings', 'On TV and in print') + \
    cta_band('Media kit', 'Writing a story?',
             "I'd love to help! Download my one-pager, or reach out for an interview in English, Arabic or French.",
             ('Download the one-pager', 'web/ines-said-speaker.pdf'), ('Contact me', href('speaking', preview) + ('' if preview else '#book')))


POST_CATS = {'Tanit XR': 'tanit', 'Field notes': 'field', 'Tools': 'tools'}

def body_blog(preview):
    H = lambda p: href(p, preview)
    first, rest = POSTS[0], POSTS[1:]
    cards = ''.join(post_card(p, preview).replace('<a class="card"', f'<a class="card" data-cat="{POST_CATS.get(p["tag"], "other")}"', 1)
                    for p in rest)
    counts = {}
    for p in rest:
        k = POST_CATS.get(p['tag'], 'other'); counts[k] = counts.get(k, 0) + 1
    return head_block('Blog', 'Notes from the field', 'Little stories from scanning trips, events and life between Tunisia and the U.S.') + \
    section(split(f'<a href="{H("b-" + first["slug"])}"><img src="web/{first["img"]}.jpg" alt="{first["title"]}" '
                  f'style="width:100%;border-radius:18px;border:8px solid #fff;box-shadow:0 12px 30px rgba(67,32,58,.16);aspect-ratio:4/3;object-fit:cover"></a>',
        f'Latest · {first["tag"]} · {first["date"]}', first['title'], [first['excerpt']],
        buttons=[('Read the story', H('b-' + first['slug']))])) + \
    section(filters('#post-grid', [('tanit', 'Tanit XR'), ('field', 'Field notes'), ('tools', 'Tools')], counts) +
            f'<div class="cards" id="post-grid">{cards}</div>', 'Archive', 'More stories', cls='tint') + \
    cta_band('Newsletter', 'Art, XR &amp; Impact Opportunities',
             'Every week I share grants, residencies, fellowships and open calls for creatives. It\'s free!',
             ('Subscribe on LinkedIn', NEWSLETTER_URL), ('See all opportunities', 'https://tanitxr.org/opportunities/'))


TANIT_OPPS = 'https://tanitxr.org/opportunities/'

def body_opportunities(preview):
    H = lambda p: href(p, preview)
    return head_block('Art, XR &amp; Impact Opportunities', 'Opportunities for creatives',
                      'Every week I share grants, residencies, fellowships and open calls. It all lives on the Tanit XR board!') + \
    statement('Why I do this', 'I know how hard it is to find opportunities.',
        "When I was starting out, I spent hours looking for grants and calls for artists who work with technology. "
        "So now I collect them every week and share them with everyone, for free. I hope they help you find your next big thing!") + \
    section(split(collage([('workshop', 'Ines leading a workshop'), ('awe-team', 'The Tanit XR team at AWE'),
                           ('rh-hack-table', 'Hacking at MIT Reality Hack'), ('ee30-class', 'EE 30 Under 30 class')]),
        'The board', 'Everything is on the Tanit XR opportunities board',
        ["I moved the full board to Tanit XR so our whole community can use it. You can search, filter by type "
         "and see how many days are left before each deadline."],
        ticks=['Grants, residencies, fellowships, awards and calls for speakers',
               'Deadlines that count down so you never miss one',
               'New opportunities added every week',
               'You can even submit an opportunity you found'],
        buttons=[('Open the opportunities board', TANIT_OPPS), ('Subscribe on LinkedIn', NEWSLETTER_URL)])) + \
    stats_photo('awe-team', [('7,000+', 'people follow along on LinkedIn'), ('50+', 'opportunities on the board'),
                             ('Weekly', 'new editions'), ('Free', 'always')]) + \
    section(icon_cards([
        ('trophy', 'Grants &amp; awards', 'Funding and prizes for art, XR and social impact projects.', TANIT_OPPS, 'See grants'),
        ('pin', 'Residencies', 'Time and space to make your work, all around the world.', TANIT_OPPS, 'See residencies'),
        ('people', 'Fellowships', 'Programs that support you as an artist, founder or leader.', TANIT_OPPS, 'See fellowships'),
        ('mic', 'Calls for speakers', 'Conferences looking for speakers, demos and exhibits.', TANIT_OPPS, 'See calls'),
        ('news', 'The newsletter', 'Get the new opportunities every week, right on LinkedIn.', NEWSLETTER_URL, 'Subscribe'),
        ('spark', 'Share one with us', 'Found something great? Send it and we\'ll add it to the board.', TANIT_OPPS, 'Submit an opportunity'),
    ]), "What you'll find", 'All kinds of opportunities') + \
    cta_band('Tanit XR', 'Ready to find your next opportunity?',
             'The full board, with every deadline, lives on the Tanit XR website.',
             ('Go to the board', TANIT_OPPS), ('Subscribe to the newsletter', NEWSLETTER_URL))
