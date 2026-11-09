import urllib.request

req = urllib.request.Request("https://eu5db.com/map-place.json?v=1.4.7-0df48df2740c&place=location:constantinople&lang=en", headers={"User-Agent": "Mozilla/5.0"})
try:
    res = urllib.request.urlopen(req)
    print("status:", res.status)
    print(res.read()[:500])
except Exception as e:
    print("FAILED:", e)
