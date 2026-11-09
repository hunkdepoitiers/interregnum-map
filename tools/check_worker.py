import urllib.request

req = urllib.request.Request("https://eu5db.com/_astro/nameWorker-Di2fxXLz.js", headers={"User-Agent": "Mozilla/5.0"})
res = urllib.request.urlopen(req)
print("status:", res.status)
data = res.read()
print("Worker length:", len(data))
