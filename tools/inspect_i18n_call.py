import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/i18n.BNHApIHh.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('Dr(await i(`${e}/map/geography.json`))')
print(c[idx-400:idx+100])
