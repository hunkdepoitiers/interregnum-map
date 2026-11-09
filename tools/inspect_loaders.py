import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/loaders.CU0FOIaO.js", headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode('utf-8')

print("loaders.js length:", len(content))
for m in re.finditer(r'fetch\([^\)]+\)', content):
    print(m.group(0))

matches = set(re.findall(r'["\']([^"\']*(?:/data/|\.bin|\.json|map)[^"\']*)["\']', content))
for m in sorted(matches):
    if len(m) < 150:
        print(m)
