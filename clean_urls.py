# Clean URLs: /about/ instead of about.html, /projects/<slug>/ instead of project-<slug>.html.
# Runs after build_site(), before translate_site(): moves each page into its own folder, rewrites every
# internal link to root-absolute clean URLs, and leaves a redirect stub at each old .html path.
import os, re, glob

def _clean_name(name):
    """'about' -> '/about/', 'project-x' -> '/projects/x/', 'index' -> '/'."""
    if name == 'index':
        return '/'
    for pre, folder in (('project-', 'projects'), ('award-', 'awards'), ('blog-', 'blog')):
        if name.startswith(pre):
            return f'/{folder}/{name[len(pre):]}/'
    return f'/{name}/'

def _rewrite(text, lang=None):
    base = re.escape(BASE_URL)
    # absolute language URLs: https://www.inessaid.com/fr/about.html -> /fr/about/
    text = re.sub(base + r'/(fr|ar)/([a-z0-9-]+)\.html', lambda m: BASE_URL + '/' + m.group(1) + _clean_name(m.group(2)).rstrip('/').replace('/index', '') + '/', text)
    # absolute site URLs
    text = re.sub(base + r'/([a-z0-9-]+)\.html', lambda m: BASE_URL + _clean_name(m.group(1)), text)
    # root-relative "/blog.html" (404 page JS)
    text = re.sub(r'(["\'])/([a-z0-9-]+)\.html', lambda m: m.group(1) + _clean_name(m.group(2)), text)
    # relative links: ../../project-x.html, about.html#book, index.html
    def rel(m):
        q, ups, name, tail = m.group(1), m.group(2), m.group(3), m.group(4) or ''
        if lang and not ups:           # a bare link inside /fr/ or /ar/ stays in that language
            url = f'/{lang}/' if name == 'index' else f'/{lang}/{name}/'
        else:
            url = _clean_name(name)
        return f'{q}{url}{tail}'
    text = re.sub(r'(["\'(=])((?:\.\./)*)([a-z0-9-]+)\.html(#[^"\'\s)]*)?(?=["\'\s)])', rel, text)
    # assets: web/x.jpg or ../web/x.jpg -> /web/x.jpg
    text = re.sub(r'(["\'(])(?:\.\./)*web/', r'\1/web/', text)
    # language switcher relative links
    text = re.sub(r'href="(?:\.\./)?(fr|ar)/"', r'href="/\1/"', text)
    # links that leave the site (and PDFs) open in a new tab
    text = re.sub(r'<a (?![^>]*\btarget=)([^>]*?)href="((?:https?://(?!www\.inessaid\.com)[^"]+)|(?:[^"]+\.pdf))"',
                  r'<a \1href="\2" target="_blank" rel="noopener"', text)
    return text

def _stub(target):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{BASE_URL}{target}">'
            f'<meta name="robots" content="noindex"><title>Ines Said</title>'
            f'<script>location.replace("{target}"+location.hash)</script></head>'
            f'<body><a href="{target}">This page has moved</a></body></html>')

def clean_urls():
    moved = 0
    # 1) rewrite links in every html/xml file first
    for f in glob.glob(os.path.join(OUT, '**', '*.html'), recursive=True) + [os.path.join(OUT, 'sitemap.xml')]:
        rel = os.path.relpath(f, OUT)
        lang = rel.split(os.sep)[0] if rel.split(os.sep)[0] in ('fr', 'ar') else None
        t = open(f, encoding='utf-8').read()
        n = _rewrite(t, lang)
        if n != t:
            open(f, 'w', encoding='utf-8').write(n)
    # 2) move flat pages into folders (root + fr/ + ar/), stub the old path
    for d, prefix in ((OUT, ''), (os.path.join(OUT, 'fr'), '/fr'), (os.path.join(OUT, 'ar'), '/ar')):
        for f in glob.glob(os.path.join(d, '*.html')):
            name = os.path.basename(f)[:-5]
            if name in ('index', '404'):
                continue
            clean = (prefix + _clean_name(name)) if not prefix else f'{prefix}/{name}/'
            dest_dir = os.path.join(OUT, clean.strip('/'))
            os.makedirs(dest_dir, exist_ok=True)
            os.replace(f, os.path.join(dest_dir, 'index.html'))
            with open(f, 'w', encoding='utf-8') as s:
                s.write(_stub(clean))
            moved += 1
    print(f'clean URLs: {moved} pages moved into folders, old .html paths redirect')
