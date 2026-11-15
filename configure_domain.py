from pathlib import Path
import sys,re,xml.sax.saxutils as xu
from urllib.parse import urlparse
if len(sys.argv)!=2: raise SystemExit('사용법: python configure_domain.py https://실제-도메인')
base=sys.argv[1].rstrip('/')
u=urlparse(base)
if u.scheme!='https' or not u.netloc or 'example' in u.netloc:raise SystemExit('HTTPS 실제 도메인을 입력하세요.')
p=Path(__file__).parent/'index.html';s=p.read_text(encoding='utf8')
# repeatable: removes previous canonical, og:url, social absolute tags
s=re.sub(r'<link rel="canonical"[^>]*>','',s)
s=re.sub(r'<meta (?:property="og:(?:url|image)"|name="twitter:image")[^>]*>','',s)
tags=f'<link rel="canonical" href="{base}/"><meta property="og:url" content="{base}/"><meta property="og:image" content="{base}/social-preview.jpg"><meta name="twitter:image" content="{base}/social-preview.jpg">'
s=s.replace('</head>',tags+'</head>')
# Replace JSON LD with real URL fields
import json
m=re.search(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)
if m:
 obj=json.loads(m.group(1))
 for node in obj['@graph']:
  node['url']=base+'/'
  node['@id']=base+'/#'+('restaurant' if node['@type']=='Restaurant' else 'website')
  if node['@type']=='Restaurant':node['image']=base+'/social-preview.jpg'
 s=s[:m.start(1)]+json.dumps(obj,ensure_ascii=False,separators=(',',':'))+s[m.end(1):]
p.write_text(s,encoding='utf8')
(Path(__file__).parent/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+xu.escape(base+'/')+'</loc></url></urlset>',encoding='utf8')
(Path(__file__).parent/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n',encoding='utf8')
print('설정 완료:',base)
