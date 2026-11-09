import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/LocText.DchzC0nD.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('function Rn(')
print("Before Rn:")
print(c[max(0, idx-500):idx])
# Also search de(e)
print("import de:")
for m in re.finditer(r'import\s*\{[^}]*de[^}]*\}', c):
    print(m.group(0))
