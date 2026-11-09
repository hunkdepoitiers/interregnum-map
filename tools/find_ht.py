import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/LocText.DchzC0nD.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
# Find export { ... ht as ... } or function ht
for m in re.finditer(r'(?:function\s+ht\b|var\s+ht\b|let\s+ht\b|const\s+ht\b)', c):
    idx = m.start()
    print(c[idx:idx+300])
    print("="*40)

# Check export list
idx_exp = c.rfind('export{')
print("Exports:", c[idx_exp:idx_exp+400])
