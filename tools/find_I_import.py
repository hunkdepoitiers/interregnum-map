import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
for m in re.finditer(r'import\s*\{([^}]+)\}\s*from\s*["\']([^"\']+)["\']', c):
    items = m.group(1).split(',')
    for it in items:
        if ' as I' in it or it.strip() == 'I':
            print(f"Found I from {m.group(2)}: {it}")
