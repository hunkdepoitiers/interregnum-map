import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('function ct')
matches = re.findall(r'(\b[a-zA-Z0-9_$]+\s*=\s*[^;]+I\([^;]+;)', c[idx-2000:idx])
for m in matches:
    print(m)
# Also search where I is defined
for m in re.finditer(r'(?:var|let|const|function)\s+I\b', c):
    p = m.start()
    print("Def of I:", c[p:p+150])
