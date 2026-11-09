import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
# Find where ct and et are defined
for m in re.finditer(r'function ct\(|var ct=|function et\(|var et=', c):
    idx = m.start()
    print(c[idx:idx+400])
    print("="*40)
