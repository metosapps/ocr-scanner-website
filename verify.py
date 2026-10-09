from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json

ROOT = Path(__file__).parent
PUBLIC = ROOT / 'dist'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.images = set(), [], []
        self.h1 = self.main = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, 'Duplicate ID: ' + a['id']
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag in ('a', 'link') and 'href' in a: self.refs.append(a['href'])
        if tag in ('img', 'script') and 'src' in a: self.refs.append(a['src'])
        if tag == 'img':
            assert 'alt' in a, 'Image missing alt'
            self.images.append(a['src'])

pages = {}
for path in sorted(PUBLIC.glob('*.html')):
    p = Page(); p.feed(path.read_text())
    assert p.h1 == 1 and p.main == 1, f'{path.name}: one h1 and main required'
    pages[path.resolve()] = p

checked = 0
for path, p in pages.items():
    for ref in p.refs:
        u = urlsplit(ref)
        if u.scheme or u.netloc: continue
        target = (PUBLIC / unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent / unquote(u.path)) if u.path else path
        if target.is_dir(): target /= 'index.html'
        target = target.resolve()
        assert target.exists(), f'{path.name}: missing {ref}'
        if u.fragment:
            assert target in pages and unquote(u.fragment) in pages[target].ids, f'{path.name}: missing anchor {ref}'
        checked += 1
# Current public copy must distinguish available local OCR from unconfigured cloud OCR.
copy = {name: (PUBLIC / name).read_text() for name in ('index.html', 'privacy.html', 'terms.html', 'support.html')}
assert 'Datalab cloud processing is in preparation and is not currently available.' in copy['index.html']
assert 'not currently available' in copy['support.html']
assert 'Cloud OCR is unavailable until' in copy['privacy.html']
for name, text in copy.items():
    assert 'Datalab' in text and 'Cloudflare' in text, name
    assert '24 hours' in text and 'scheduled' in text, name
    assert 'Google sign-in' in text or 'sign in with Google' in text, name
    assert 'currently selected' not in text and 'current mode remains TEST' not in text, name
assert 'test and commercial ads are currently disabled' in copy['index.html'].lower()
assert 'current advertising mode is OFF' in copy['support.html']
assert '48 hours after content expiry' in copy['privacy.html']
assert 'provider deletion guarantee' in copy['privacy.html']
assert 'applicable service agreement' in copy['privacy.html']

result = {
    'status': 'PASS',
    'verificationScope': 'Current static HTML structure, image alt attributes, local links/assets and local/cloud availability/retention disclosures.',
    'htmlPages': len(pages),
    'cloudAvailability': 'in preparation; unavailable until server/sign-in setup',
    'advertisingMode': 'OFF',
    'localLinksAndAssetsChecked': checked,
    'javascriptSyntax': 'Not executed by this script; run node --check dist/app.js separately.',
    'browserChecks': {
        'scope': 'Prior browser baseline; not rerun by this script or for the current copy change.',
        'checks': ['desktop: no horizontal overflow', 'mobile: menu opens and navigation works',
                   'gallery: modal opens, image loads and closes', 'FAQ: disclosure expands',
                   'support: email links visible', 'privacy: RTL Arabic summary and no horizontal overflow'],
    },
    'publicContact': 'chennoufo11@gmail.com',
    'downloadLink': 'awaiting verified Galaxy Store listing',
}
(ROOT / 'QA.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
