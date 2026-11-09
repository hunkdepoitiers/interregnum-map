import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/ApiPage.D-nvKEz6.js", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
c = urllib.request.urlopen(req).read().decode('utf-8')
print("ApiPage text preview of fetch:")
for m in re.finditer(r'fetch\([^)]+\)', c):
    start = max(0, m.start() - 100)
    end = min(len(c), m.end() + 100)
    print(c[start:end])
    print("-" * 50)
