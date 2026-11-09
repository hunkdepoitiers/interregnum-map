import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/ApiPage.D-nvKEz6.js", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
c = urllib.request.urlopen(req).read().decode('utf-8')
for m in re.finditer(r'function ApiPage|\bApiPage\b', c):
    idx = m.start()
    print(c[idx:idx+800])
