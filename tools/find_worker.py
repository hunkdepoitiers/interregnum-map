import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
for m in re.finditer(r'new\s+Worker\([^)]+\)', c):
    print("Worker match:", m.group(0))

for m in re.finditer(r'Worker', c):
    idx = m.start()
    print(c[max(0, idx-50):min(len(c), idx+100)])
