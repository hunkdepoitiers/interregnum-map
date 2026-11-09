import urllib.request

req = urllib.request.Request("https://eu5db.com/_astro/loaders.CU0FOIaO.js", headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode('utf-8')
print(content)
