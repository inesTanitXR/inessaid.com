# Trilingual site: builds /fr/ and /ar/ copies of every English page from the finished docs/ tree.
# Text lives in i18n/fr.json and i18n/ar.json, keyed by the English (inner HTML, whitespace-collapsed).
# Any English text without a translation is written to i18n/todo-<lang>.json and reported, so the
# three languages never drift apart silently.
import os, re, glob, json
import lxml.html
from lxml import etree

LANGS = {'fr': 'ltr', 'ar': 'rtl'}
INLINE = {'a', 'abbr', 'b', 'br', 'cite', 'em', 'i', 'img', 'mark', 'q', 's', 'small', 'span', 'strong',
          'sub', 'sup', 'time', 'u', 'wbr', 'bdi'}
SKIP = {'script', 'style', 'noscript', 'iframe', 'svg', 'code', 'template', 'textarea', 'select'}
ATTRS = ('alt', 'title', 'placeholder', 'aria-label')
META = ('description', 'og:title', 'og:description', 'twitter:title', 'twitter:description')
HIDDEN = ('_subject', '_autoresponse')
I18N = os.path.join(ROOT, 'i18n')

def _norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def _has_words(s):
    return re.search(r'[A-Za-z]{2,}', re.sub(r'<[^>]+>|&[a-z]+;', ' ', s)) is not None

def _skipped(el):
    return (el.tag in SKIP or 'brand' in (el.get('class') or '').split() or el.get('translate') == 'no'
            or 'lang-switch' in (el.get('class') or '').split())

def _inner(el):
    return (el.text or '') + ''.join(etree.tostring(c, encoding='unicode', method='html') for c in el)

def _all_inline(el):
    return all(isinstance(d.tag, str) and d.tag in INLINE for d in el.iterdescendants())

def _units(root):
    """Yield ('el', element) for translatable blocks and ('text', element, slot) for loose text."""
    def walk(el):
        if not isinstance(el.tag, str) or _skipped(el):
            return
        loose = (el.text or '') + ''.join(c.tail or '' for c in el)
        only_kids = len(el) > 1 and not _has_words(loose)
        if _all_inline(el) and _has_words(_inner(el)) and el.tag not in ('html', 'body', 'head') and not only_kids:
            yield ('el', el)
            return
        if el.text and _has_words(el.text):
            yield ('text', el, 'text')
        for c in el:
            yield from walk(c)
            if c.tail and _has_words(c.tail):
                yield ('text', c, 'tail')
    yield from walk(root)

def _attr_targets(doc):
    for el in doc.iter():
        if not isinstance(el.tag, str):
            continue
        anc = el
        skip = False
        while anc is not None:
            if isinstance(anc.tag, str) and _skipped(anc) and anc.tag != 'svg':
                skip = True; break
            anc = anc.getparent()
        if skip:
            continue
        for a in ATTRS:
            v = el.get(a)
            if v and _has_words(v):
                yield el, a
        if el.tag == 'meta' and (el.get('name') in META or el.get('property') in META) and el.get('content'):
            yield el, 'content'
        if el.tag == 'input' and (el.get('name') in HIDDEN or el.get('type') == 'submit') and el.get('value'):
            yield el, 'value'

def _en_pages():
    out = []
    for f in glob.glob(os.path.join(OUT, '**', 'index.html'), recursive=True):
        rel = os.path.relpath(f, OUT)
        if rel.split(os.sep)[0] in LANGS or 'http-equiv="refresh"' in open(f, encoding='utf-8').read(2000):
            continue
        out.append(rel)
    return sorted(out)

def _url_of(rel):
    d = os.path.dirname(rel)
    return '/' if not d else f'/{d}/'

def _loc(url, code):
    return url if code == 'en' else f'/{code}{url}'

def collect():
    """All English strings that need a translation, in page order."""
    seen = {}
    for rel in _en_pages():
        doc = lxml.html.fromstring(open(os.path.join(OUT, rel), encoding='utf-8').read())
        t = doc.find('.//title')
        if t is not None and t.text:
            seen.setdefault(_norm(t.text), rel)
        body = doc.find('body')
        for u in _units(body):
            s = _inner(u[1]) if u[0] == 'el' else getattr(u[1], u[2])
            seen.setdefault(_norm(s), rel)
        for el, a in _attr_targets(doc):
            seen.setdefault(_norm(el.get(a)), rel)
    return seen

def _load(code):
    p = os.path.join(I18N, f'{code}.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}

def _set_inner(el, html):
    for c in list(el):
        el.remove(c)
    frag = lxml.html.fragments_fromstring(html) if html else []
    el.text = None
    last = None
    for part in frag:
        if isinstance(part, str):
            if last is None:
                el.text = (el.text or '') + part
            else:
                last.tail = (last.tail or '') + part
        else:
            el.append(part); last = part

def _relink(doc, code):
    for el in doc.iter('a', 'link', 'form'):
        attr = 'action' if el.tag == 'form' else 'href'
        v = el.get(attr)
        if not v or el.tag == 'link' and el.get('rel') not in ('canonical',):
            if el.tag == 'link' and el.get('rel') == 'canonical':
                pass
            else:
                continue
        if el.tag == 'link':
            if v.startswith(BASE_URL + '/') and not v.startswith(BASE_URL + f'/{code}/'):
                el.set('href', BASE_URL + '/' + code + v[len(BASE_URL):])
            continue
        if v.startswith('/') and not v.startswith('//') and not re.match(r'/(web|fr|ar)/', v) and not v.endswith('.pdf'):
            el.set(attr, f'/{code}{v}')
    for el in doc.iter('input'):
        if el.get('name') == '_next' and el.get('value', '').startswith(BASE_URL):
            v = el.get('value')
            el.set('value', BASE_URL + '/' + code + v[len(BASE_URL):])
    for el in doc.iter('meta'):
        if el.get('property') == 'og:url' and el.get('content', '').startswith(BASE_URL):
            v = el.get('content'); el.set('content', BASE_URL + '/' + code + v[len(BASE_URL):])

def _switch_html(url, code):
    lab = {'en': 'EN', 'fr': 'FR', 'ar': '&#1593;&#1585;&#1576;&#1610;'}
    return '<div class="lang-switch">' + ''.join(
        f'<a href="{_loc(url, c)}" hreflang="{c}"{" class=\"on\"" if c == code else ""}>{lab[c]}</a>'
        for c in ('en', 'fr', 'ar')) + '</div>'

def _alternates(url):
    return ''.join(f'<link rel="alternate" hreflang="{c}" href="{BASE_URL}{_loc(url, c)}">' for c in ('en', 'fr', 'ar')) + \
           f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{url}">'

def _fix_chrome(text, url, code):
    text = re.sub(r'<div class="lang-switch">.*?</div>', lambda m: _switch_html(url, code), text, count=1, flags=re.S)
    text = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', text)
    return text.replace('</head>', _alternates(url) + '</head>', 1)

def translate_site():
    en = collect()
    report = {}
    for code, direction in LANGS.items():
        T = _load(code)
        missing = {k: v for k, v in en.items() if k not in T}
        json.dump({k: '' for k in missing}, open(os.path.join(I18N, f'todo-{code}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        report[code] = len(missing)
        tr = lambda s: T.get(_norm(s)) or s
        for rel in _en_pages():
            src = open(os.path.join(OUT, rel), encoding='utf-8').read()
            doc = lxml.html.fromstring(src)
            doc.set('lang', code); doc.set('dir', direction)
            t = doc.find('.//title')
            if t is not None and t.text:
                t.text = tr(t.text)
            for el, a in list(_attr_targets(doc)):
                el.set(a, tr(el.get(a)))
            for u in list(_units(doc.find('body'))):
                if u[0] == 'el':
                    k = _norm(_inner(u[1]))
                    if k in T and T[k]:
                        _set_inner(u[1], T[k])
                else:
                    el, slot = u[1], u[2]
                    s = getattr(el, slot)
                    k = _norm(s)
                    if k in T and T[k]:
                        lead = s[:len(s) - len(s.lstrip())]; trail = s[len(s.rstrip()):]
                        setattr(el, slot, lead + T[k] + trail)
            _relink(doc, code)
            html = '<!doctype html>' + lxml.html.tostring(doc, encoding='unicode', method='html')
            url = _url_of(rel)
            html = _fix_chrome(html, url, code)
            dest = os.path.join(OUT, code, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, 'w', encoding='utf-8').write(html)
        # legacy flat URLs from the first bilingual version
        for old in ('about',):
            open(os.path.join(OUT, code, f'{old}.html'), 'w', encoding='utf-8').write(_stub(f'/{code}/{old}/'))
    # English pages: per-page switcher + hreflang
    for rel in _en_pages():
        p = os.path.join(OUT, rel)
        html = _fix_chrome(open(p, encoding='utf-8').read(), _url_of(rel), 'en')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
    empty = [r for r in glob.glob(os.path.join(OUT, '**', '*.html'), recursive=True) if os.path.getsize(r) < 200]
    if empty:
        raise SystemExit(f'BUILD STOPPED: {len(empty)} empty pages, e.g. {empty[:3]}')
    # sitemap with every language
    urls = [_url_of(r) for r in _en_pages()]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u in urls:
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{BASE_URL}{_loc(u, c)}"/>' for c in ('en', 'fr', 'ar'))
        for c in ('en', 'fr', 'ar'):
            sm.append(f'<url><loc>{BASE_URL}{_loc(u, c)}</loc>{alts}</url>')
    sm.append('</urlset>')
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    print(f'translations: {len(_en_pages())} pages x 3 languages; missing fr={report["fr"]} ar={report["ar"]}'
          + ('' if not any(report.values()) else '  -> see i18n/todo-*.json'))
    return report
