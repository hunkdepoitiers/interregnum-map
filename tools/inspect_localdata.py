import urllib.request

req = urllib.request.Request("https://eu5db.com/_astro/localData.DyEUZfeM.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
print(c)
