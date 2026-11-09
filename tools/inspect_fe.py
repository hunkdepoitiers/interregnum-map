import urllib.request

req = urllib.request.Request("https://eu5db.com/_astro/LocText.DchzC0nD.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('locations.bin.gz')
idx_fe = c.rfind('function fe', 0, idx)
if idx_fe != -1:
    print(c[idx_fe:idx_fe+200])
else:
    idx_fe = c.rfind('var fe', 0, idx)
    if idx_fe != -1:
        print(c[idx_fe:idx_fe+200])
    else:
        # check imports
        print("Imports:", c[:400])
