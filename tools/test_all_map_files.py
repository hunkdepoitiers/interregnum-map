import urllib.request

version = "1.4.7-0df48df2740c"
map_hash = "e79d47c41710"
files = [
    f"/data/{version}/map/geography.json?d={map_hash}",
    f"/data/{version}/map/locations.bin.gz?d={map_hash}",
    f"/data/{version}/map/rivers.json?d={map_hash}",
    f"/data/{version}/map/connections.json?d={map_hash}",
    f"/data/{version}/map/places.json?d={map_hash}",
    f"/data/{version}/map/names.json?d={map_hash}",
    f"/data/tr/{version}/map/names.json?d=4f9d5290228f",
    f"/data/{version}/map/1337.4.1.json?d={map_hash}",
    f"/data/{version}/map/1337.4.1.pops.json?d={map_hash}",
    f"/data/{version}/map/mentions.json?d={map_hash}",
    "/data/versions.json"
]

headers = {"User-Agent": "Mozilla/5.0"}
total_size = 0
for f in files:
    try:
        req = urllib.request.Request(f"https://eu5db.com{f}", headers=headers)
        res = urllib.request.urlopen(req)
        sz = len(res.read())
        total_size += sz
        print(f"OK ({sz/1024:.1f} KB): {f}")
    except Exception as e:
        print(f"FAILED: {f} -> {e}")

print(f"\nTotal size: {total_size / (1024*1024):.2f} MB")
