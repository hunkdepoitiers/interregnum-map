import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/LocText.DchzC0nD.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('function Rn(')
print(c[idx:idx+800])
