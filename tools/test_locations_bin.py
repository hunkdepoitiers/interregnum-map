import urllib.request

req = urllib.request.Request("https://eu5db.com/data/1.4.7-0df48df2740c/map/locations.bin.gz?d=e79d47c41710", headers={"User-Agent": "Mozilla/5.0"})
res = urllib.request.urlopen(req)
print("status:", res.status)
print("content-length:", res.headers.get("content-length"))
data = res.read()
print("read length:", len(data))
