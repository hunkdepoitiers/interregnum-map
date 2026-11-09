import urllib.request

base = "http://localhost:3000"
version = "1.4.7-0df48df2740c"
map_hash = "e79d47c41710"

urls = [
    f"/data/versions.json",
    f"/data/{version}/map/geography.json?d={map_hash}",
    f"/data/{version}/map/locations.bin.gz?d={map_hash}",
    f"/data/{version}/map/1337.4.1.json?d={map_hash}",
    f"/data/{version}/map/1337.4.1.pops.json?d={map_hash}",
    f"/data/{version}/map/names.json?d={map_hash}",
    f"/data/tr/{version}/map/names.json?d=4f9d5290228f",
    f"/data/{version}/map/rivers.json?d={map_hash}",
    f"/data/{version}/map/connections.json?d={map_hash}",
    f"/data/{version}/map/places.json?d={map_hash}",
    f"/data/{version}/map/mentions.json?d={map_hash}",
    f"/_astro/nameWorker-Di2fxXLz.js",
    f"/data/{version}/map/preview-1236.jpg?d={map_hash}",
    f"/data/{version}/map/preview-1236.avif?d={map_hash}",
]

errors = 0
for u in urls:
    try:
        req = urllib.request.Request(f"{base}{u}")
        with urllib.request.urlopen(req) as resp:
            print(f"[OK 200] {u} (size: {len(resp.read())})")
    except Exception as e:
        print(f"[ERROR] {u} -> {e}")
        errors += 1

print(f"\nCompleted check with {errors} errors.")
