# Hand-drawn sketch doodles scattered faintly behind sections: Tunisian heritage, the sea,
# jasmine and oranges from Nabeul, and a few XR tools. Line art only, wobbly on purpose.
import re, hashlib

SKETCH_SYMBOLS = {
 'column': '''<symbol id="sk-column" viewBox="0 0 60 120"><path d="M12 14c6-3 12-3 18-1s12 2 18-1M10 20h40M14 20l2 88M46 20l-2 88M20 24l1 80M30 23v82M40 24l-1 80M9 110c8 3 34 3 42 0M7 116c10 3 36 3 46 0M15 13c-3-5 1-9 5-8s5 4 3 7M45 13c3-5-1-9-5-8s-5 4-3 7"/></symbol>''',
 'amphora': '''<symbol id="sk-amphora" viewBox="0 0 70 110"><path d="M24 10c6-2 16-2 22 0M22 15c8-2 18-2 26 0M25 16c-2 8-10 12-12 24s4 26 8 34 5 14 4 22c-1 4 8 6 10 6s11-2 10-6c-1-8 0-14 4-22s10-22 8-34-10-16-12-24M20 24c-8 2-12 8-10 16s8 8 10 6M50 24c8 2 12 8 10 16s-8 8-10 6M26 40c6 2 12 2 18 0M23 60c8 3 16 3 24 0"/></symbol>''',
 'jasmine': '''<symbol id="sk-jasmine" viewBox="0 0 80 100"><path d="M40 44c-2-10 0-16 6-18s10 6 6 12M40 44c8-6 16-6 18 0s-4 10-10 8M40 44c10 2 14 8 10 14s-10 2-12-4M40 44c-2 10-8 14-14 10s-2-12 4-12M40 44c-10-2-14-8-10-14s10-2 12 4M38 44a3 3 0 1 0 4 0M38 56c-2 14-4 26-6 40M32 74c-8-2-14 2-16 8s6 6 12 2M34 84c8-4 14-2 16 4s-6 6-12 2"/></symbol>''',
 'shell': '''<symbol id="sk-shell" viewBox="0 0 90 80"><path d="M46 40c-2-8 8-12 14-6s4 18-6 22-24 0-28-12 6-28 22-30 30 10 32 26-8 30-24 34-34-6-40-22 4-34 20-40"/><path d="M28 60l-8 10M36 66l-4 10M48 66l2 10M58 60l6 8M20 46l-10 4"/></symbol>''',
 'wave': '''<symbol id="sk-wave" viewBox="0 0 160 40"><path d="M2 12c12-10 22-10 34 0s22 10 34 0 22-10 34 0 22 10 34 0 14-6 20-4M8 30c12-10 22-10 34 0s22 10 34 0 22-10 34 0 22 10 34 0"/></symbol>''',
 'headset': '''<symbol id="sk-headset" viewBox="0 0 110 70"><path d="M14 22c6-8 20-12 41-12s35 4 41 12c4 6 4 22 0 28-6 8-18 6-24 0-4-4-10-6-17-6s-13 2-17 6c-6 6-18 8-24 0-4-6-4-22 0-28zM10 30H4c-2 0-2 8 0 8h6M100 30h6c2 0 2 8 0 8h-6M30 8c8-3 18-4 25-4s17 1 25 4M46 24c4-2 14-2 18 0"/></symbol>''',
 'tanit': '''<symbol id="sk-tanit" viewBox="0 0 70 90"><path d="M35 8a9 9 0 1 0 .1 0M20 30c8 0 22 0 30 0M12 26c-4 0-4 8 0 8M58 26c4 0 4 8 0 8M35 30v8M22 38h26L58 80H12z"/></symbol>''',
 'mosaic': '''<symbol id="sk-mosaic" viewBox="0 0 100 70"><path d="M6 8l14-2 2 12-14 3zM24 6l12-2 2 12-12 2zM40 4l14-1 1 12-14 2zM58 5l12-2 2 12-12 2zM76 6l14-1 0 12-14 1zM4 24l12-2 2 12-12 2zM22 22l14-1 1 12-14 2zM42 20l12-2 2 12-12 2zM60 22l12-1 0 12-12 1zM78 23l12-2 2 12-12 2zM8 42l12-2 2 12-12 2zM26 40l12-1 2 12-12 2zM44 38l14-1 0 12-14 2zM62 40l12-1 1 12-12 1z"/></symbol>''',
 'olive': '''<symbol id="sk-olive" viewBox="0 0 120 70"><path d="M4 50c30-16 60-26 110-30M30 40c-4-10 0-18 8-20s10 8 4 16M44 34c-2-12 4-18 12-18s8 10 0 16M60 28c0-12 8-16 16-14s6 12-2 16M78 22c2-10 12-14 18-10s2 12-6 14M22 50c-10 2-18-2-20-10s8-8 14-2M40 46c-8 6-16 4-20-2s6-10 12-6M58 40c-6 8-14 8-18 2s4-10 10-8M76 34c-4 8-12 10-16 4s2-10 8-8M90 48a5 6 0 1 0 .1 0M100 40a5 6 0 1 0 .1 0"/></symbol>''',
 'arch': '''<symbol id="sk-arch" viewBox="0 0 140 90"><path d="M6 88V40c0-20 14-32 30-32s30 12 30 32v48M72 88V40c0-20 14-32 30-32s30 12 30 32v48M2 88h136M14 84V44c0-14 10-22 22-22s22 8 22 22v40M80 84V44c0-14 10-22 22-22s22 8 22 22v40M6 40h10M60 40h12M126 40h10"/></symbol>''',
 'fish': '''<symbol id="sk-fish" viewBox="0 0 120 60"><path d="M10 30c16-20 40-26 64-22 12 2 22 10 30 22-8 12-18 20-30 22-24 4-48-2-64-22zM104 30l14-14v28zM40 22l4-12 10 10M40 38l4 12 10-10M30 30a3 3 0 1 0 .1 0M56 20c2 6 2 14 0 20M70 18c2 8 2 16 0 24M84 20c2 6 2 14 0 20"/></symbol>''',
 'orange': '''<symbol id="sk-orange" viewBox="0 0 80 90"><path d="M40 30a26 26 0 1 0 .1 0M40 30c-2-8 0-14 6-18M46 12c8-6 16-4 20 2-6 6-14 6-20-2M34 20c-8-6-16-4-20 2 6 6 14 6 20-2M28 56c4 4 20 4 24 0"/></symbol>''',
 'star': '''<symbol id="sk-star" viewBox="0 0 40 40"><path d="M20 4c2 8 6 12 16 16-10 4-14 8-16 16-2-8-6-12-16-16 10-4 14-8 16-16z"/></symbol>''',
 'heart': '''<symbol id="sk-heart" viewBox="0 0 60 56"><path d="M30 50C14 38 4 30 4 18 4 10 10 4 18 4c6 0 10 4 12 8 2-4 6-8 12-8 8 0 14 6 14 14 0 12-10 20-26 32z"/></symbol>''',
 'phone': '''<symbol id="sk-phone" viewBox="0 0 90 100"><path d="M28 6h30c4 0 6 2 6 6v76c0 4-2 6-6 6H28c-4 0-6-2-6-6V12c0-4 2-6 6-6zM38 10h10M40 88h6M22 30c-8 4-12 10-12 20s4 16 12 20M64 30c8 4 12 10 12 20s-4 16-12 20M14 22c-10 6-12 16-12 28s2 22 12 28M72 22c10 6 12 16 12 28s-2 22-12 28"/></symbol>''',
 'boat': '''<symbol id="sk-boat" viewBox="0 0 120 70"><path d="M10 40h100l-14 20H24zM60 40V8M60 12c14 4 24 10 28 24H60M56 24c-10-6-20-8-30 4M2 66c10-6 20-6 30 0s20 6 30 0 20-6 30 0 18 6 26 0"/></symbol>''',
 'ines': '''<symbol id="sk-ines" viewBox="0 0 100 120"><path d="M35 34c-3-7 2-13 8-11 1-6 8-9 13-5 5-4 12-1 13 5 6-2 11 4 8 11"/><path d="M27 42c-4-2-8 2-6 7-4 2-4 8 0 10-4 3-3 9 2 10-3 4 0 9 5 9-1 5 4 8 8 6M73 42c4-2 8 2 6 7 4 2 4 8 0 10 4 3 3 9-2 10 3 4 0 9-5 9 1 5-4 8-8 6"/><path d="M30 44c-3 3-2 7 1 8M70 44c3 3 2 7-1 8M26 62c-2 3 0 7 3 7M74 62c2 3 0 7-3 7M31 78c-1 4 2 6 5 5M69 78c1 4-2 6-5 5"/><path d="M36 38c2-4 7-6 14-6s12 2 14 6"/><path d="M28 50c8-1 12 3 22 3s14-4 22-3M30 56c4 6 10 8 20 8s16-2 20-8"/><path d="M28 50c-3 0-5 3-5 6s2 6 5 6M72 50c3 0 5 3 5 6s-2 6-5 6"/><path d="M44 72c3 3 9 3 12 0"/><path d="M40 82c-10 4-16 12-18 24M60 82c10 4 16 12 18 24M50 84v22"/><path d="M22 106c18 6 38 6 56 0"/><path d="M38 84c4 3 8 4 12 4s8-1 12-4"/></symbol>''',
 'khamsa': '''<symbol id="sk-khamsa" viewBox="0 0 90 110"><path d="M30 60V30c0-4 3-7 6-7s6 3 6 7v22M42 52V18c0-4 3-7 6-7s6 3 6 7v34M54 52V26c0-4 3-7 6-7s6 3 6 7v30M66 56V38c0-3 3-6 6-6s6 3 6 6v26c0 22-14 36-33 36S12 88 12 66V50c0-4 3-7 7-7s7 3 7 7v14M30 60c-2-6-6-8-11-6"/><path d="M32 74c6-6 20-6 26 0-6 6-20 6-26 0zM45 71a3 3 0 1 0 .1 0"/><path d="M40 92c3 3 7 3 10 0"/></symbol>''',
 'khlala': '''<symbol id="sk-khlala" viewBox="0 0 90 110"><path d="M45 10a9 9 0 1 0 .1 0M45 19v10"/><path d="M45 29L14 90h62z"/><path d="M45 44L26 82h38z"/><path d="M45 56l-8 18h16zM45 64a3 3 0 1 0 .1 0"/><path d="M30 90c0 6 6 10 15 10s15-4 15-10M45 100v8M36 99l-4 8M54 99l4 8"/><path d="M20 84h50"/></symbol>''',
 'yaz': '''<symbol id="sk-yaz" viewBox="0 0 90 110"><path d="M14 20c6 12 14 20 22 26M76 20c-6 12-14 20-22 26M14 100c6-12 14-20 22-26M76 100c-6-12-14-20-22-26M36 46c-4 4-4 24 0 28M54 46c4 4 4 24 0 28M36 46h18M36 74h18M45 8v14M45 98v10"/></symbol>''',
 'berber': '''<symbol id="sk-berber" viewBox="0 0 110 90"><path d="M55 8l40 37-40 37-40-37zM55 24l24 21-24 21-24-21zM55 38l8 7-8 7-8-7z"/><path d="M4 46h10M96 46h10M18 12l6 6M92 12l-6 6M18 80l6-6M92 80l-6-6M55 84v6"/></symbol>''',
 'door': '''<symbol id="sk-door" viewBox="0 0 90 120"><path d="M14 116V44c0-20 14-32 31-32s31 12 31 32v72M8 116h74M45 20v96M22 40h46M22 60h46M22 80h46M22 100h46"/><path d="M28 50a1.5 1.5 0 1 0 .1 0M36 50a1.5 1.5 0 1 0 .1 0M54 50a1.5 1.5 0 1 0 .1 0M62 50a1.5 1.5 0 1 0 .1 0M28 70a1.5 1.5 0 1 0 .1 0M36 70a1.5 1.5 0 1 0 .1 0M54 70a1.5 1.5 0 1 0 .1 0M62 70a1.5 1.5 0 1 0 .1 0M28 90a1.5 1.5 0 1 0 .1 0M36 90a1.5 1.5 0 1 0 .1 0M54 90a1.5 1.5 0 1 0 .1 0M62 90a1.5 1.5 0 1 0 .1 0"/><path d="M38 66a4 4 0 1 0 .1 0M52 66a4 4 0 1 0 .1 0"/></symbol>''',
 'eye': '''<symbol id="sk-eye" viewBox="0 0 110 60"><path d="M6 30c14-18 30-26 49-26s35 8 49 26c-14 18-30 26-49 26S20 48 6 30z"/><path d="M55 14a16 16 0 1 0 .1 0M55 22a8 8 0 1 0 .1 0"/><path d="M28 12l-4-6M82 12l4-6M55 4V0M28 48l-4 6M82 48l4 6"/></symbol>''',
 'palette': '''<symbol id="sk-palette" viewBox="0 0 90 80"><path d="M44 6C22 6 6 20 6 40s16 30 32 30c8 0 8-6 6-10s0-8 6-8h10c14 0 24-8 24-22C84 16 66 6 44 6zM26 30a4 4 0 1 0 .1 0M40 18a4 4 0 1 0 .1 0M58 18a4 4 0 1 0 .1 0M68 32a4 4 0 1 0 .1 0M62 62l22-24"/></symbol>''',
}

SKETCH_SPRITE = ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">'
                 + ''.join(SKETCH_SYMBOLS.values()) + '</svg>')

SKETCH_CSS = '''
.sk-layer{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.sk{position:absolute;fill:none;stroke:var(--lav);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;opacity:.2}
.sk.gold{stroke:var(--gold);opacity:.24}
.band.deep .sk,.cta-end .sk,footer .sk{stroke:#f3dcd6;opacity:.14}
.band.deep .sk.gold,.cta-end .sk.gold,footer .sk.gold{stroke:#e8cd96;opacity:.2}
.has-sk{position:relative}
.has-sk>.wrap{position:relative;z-index:1}
@media(max-width:820px){.sk{transform:scale(.7)}}
'''

# Where each sketch may sit (corner) and how big it is. Positions keep clear of the centred text.
_SPOTS = [('left:-14px;top:18px', 'tl'), ('right:-10px;top:26px', 'tr'), ('left:2%;bottom:14px', 'bl'),
          ('right:3%;bottom:10px', 'br'), ('left:1%;top:44%', 'ml'), ('right:1%;top:40%', 'mr'),
          ('left:8%;top:6px', 'tl2'), ('right:9%;bottom:6px', 'br2')]
_SIZES = {'column': 104, 'amphora': 96, 'jasmine': 100, 'shell': 96, 'wave': 170, 'headset': 116, 'tanit': 84,
          'mosaic': 108, 'olive': 136, 'arch': 146, 'fish': 124, 'orange': 84, 'star': 34, 'heart': 52,
          'phone': 80, 'boat': 124, 'palette': 90, 'ines': 96, 'khamsa': 84, 'khlala': 80, 'yaz': 76, 'berber': 100, 'door': 82, 'eye': 96}
_ROT = [-14, -8, -4, 5, 9, 15]

def sketch_svg(name, style='', cls='', rot=0):
    w = _SIZES[name]
    return (f'<svg class="sk {cls}" style="{style};width:{w}px;transform:rotate({rot}deg)" aria-hidden="true">'
            f'<use href="#sk-{name}"/></svg>')

def _pick(seed, n, k):
    h = hashlib.md5(seed.encode()).digest()
    out, used = [], set()
    for b in h:
        i = b % n
        if i not in used:
            used.add(i); out.append(i)
        if len(out) == k:
            break
    return out

def sketch_layer(seed, names=None, count=3, force=None):
    """A deterministic little scatter of doodles for one section."""
    pool = names or list(SKETCH_SYMBOLS)
    idx = _pick(seed, len(pool), count)
    if force and force in pool and pool.index(force) not in idx:
        idx[0] = pool.index(force)
    spots = _pick(seed + 's', len(_SPOTS), count)
    rots = _pick(seed + 'r', len(_ROT), count)
    parts = []
    for j, i in enumerate(idx):
        name = pool[i]
        cls = 'gold' if (j + len(seed)) % 3 == 0 else ''
        parts.append(sketch_svg(name, _SPOTS[spots[j]][0], cls, _ROT[rots[j]]))
    return '<div class="sk-layer">' + ''.join(parts) + '</div>'

_SECTION_RE = re.compile(r'<(section class="(?:block|recognized|related|statement|hero2)[^"]*"|div class="band [^"]*"|header class="phead")>')

def sketchify(page, html):
    """Give every block/band/page header on a page a faint doodle layer, then add the sprite once."""
    n = [0]
    def rep(m):
        n[0] += 1
        tag = m.group(1)
        if 'has-sk' in tag:
            return m.group(0)
        tag = tag.replace('class="', 'class="has-sk ', 1)
        return f'<{tag}>' + sketch_layer(f'{page}-{n[0]}', force='ines' if n[0] in (1, 4) else None)
    html = _SECTION_RE.sub(rep, html)
    html = html.replace('<footer><div class="wrap">', '<footer class="has-sk">' + sketch_layer(page + '-footer', ['jasmine', 'olive', 'wave', 'shell', 'boat', 'star', 'fish', 'orange', 'ines', 'khamsa', 'khlala', 'eye'], force='ines') + '<div class="wrap">', 1)
    return html.replace('<body>', '<body>' + SKETCH_SPRITE, 1)
