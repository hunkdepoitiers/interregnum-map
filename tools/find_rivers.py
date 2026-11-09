import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/LocText.DchzC0nD.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
for m in re.finditer(r'rivers', c):
    idx = m.start()
    print(c[max(0, idx-100):min(len(c), idx+150)])
    print("="*40)
