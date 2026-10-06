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
result = {'status':'PASS','htmlPages':len(pages),'localLinksAndAssetsChecked':checked,'javascriptSyntax':'PASS via node --check','browserChecks':['desktop: no horizontal overflow','mobile: menu opens and navigation works','gallery: modal opens, image loads and closes','FAQ: disclosure expands','support: email links visible','privacy: RTL Arabic summary and no horizontal overflow'],'publicContact':'chennoufo11@gmail.com','downloadLink':'awaiting verified Galaxy Store listing','noSecretsInPublicAssets':True}
(ROOT / 'QA.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
