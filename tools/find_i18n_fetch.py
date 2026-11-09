import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/i18n.BNHApIHh.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
for m in re.finditer(r'fetch\(', c):
    idx = m.start()
    print(c[max(0, idx-50):min(len(c), idx+150)])
    print("="*40)
