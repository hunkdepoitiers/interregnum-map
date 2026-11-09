import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/LocText.DchzC0nD.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx_exp = c.rfind('export{')
exp_str = c[idx_exp:]
m = re.search(r'([a-zA-Z0-9_$]+)\s+as\s+ht\b', exp_str)
if m:
    orig = m.group(1)
    print("ht is originally:", orig)
    for fm in re.finditer(rf'(?:function|var|let|const)\s+{orig}\b', c):
        print(c[fm.start():fm.start()+300])
else:
    print("Could not find ht in exports, searching...")
    for it in exp_str.split(','):
        if 'ht' in it:
            print("Export matching ht:", it)
