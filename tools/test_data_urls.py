import urllib.request
import json

headers = {"User-Agent": "Mozilla/5.0"}
for path in ["/data/versions.json", "/versions.json", "/data/1.4.7-0df48df2740c/map/geography.json", "/data/1.4.7-0df48df2740c/map/1337.4.1.json"]:
    try:
        url = f"https://eu5db.com{path}"
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req)
        print(f"SUCCESS {path} - status={res.status}, length={res.headers.get('content-length')}")
    except Exception as e:
        print(f"FAILED {path} - {e}")
