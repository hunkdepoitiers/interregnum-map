import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('function ct')
# Look backwards from ct for I = or function I
idx_I = c.rfind('function I(', 0, idx)
if idx_I == -1:
    idx_I = c.rfind('var I=', 0, idx)
if idx_I != -1:
    print(c[idx_I:idx_I+300])
else:
    # check imports for I
    print(c[:500])
