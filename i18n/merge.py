# Merge translator output (i18n/parts/<lang>-*.json) into i18n/<lang>.json,
# checking that each translation keeps the same links and tags as the English.
import json, glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

def sig(s):
    return (sorted(re.findall(r'href="([^"]*)"', s)), sorted(re.findall(r'<(\w+)', s)))

for code in ('fr', 'ar'):
    path = os.path.join(HERE, f'{code}.json')
    T = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    added = bad = 0
    for f in sorted(glob.glob(os.path.join(HERE, 'parts', f'{code}-*.json'))):
        for k, v in json.load(open(f, encoding='utf-8')).items():
            if not v:
                continue
            if sig(k) != sig(v):
                bad += 1
                print(f'  [{code}] tag/link mismatch, skipped: {k[:70]!r}')
                continue
            T[k] = v
            added += 1
    json.dump(dict(sorted(T.items())), open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{code}: {added} merged, {bad} rejected, {len(T)} total')
