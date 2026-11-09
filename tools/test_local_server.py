import urllib.request
import json

base = "http://localhost:3000"

tests = [
    ("/", "text/html"),
    ("/map", "text/html"),
    ("/_astro/MapPage.CWs7aPan.js", "text/javascript"),
    ("/_astro/_..DaEYJm4o.css", "text/css"),
    ("/favicon.svg", "image/svg+xml"),
    ("/data/versions.json", "application/json"),
    ("/data/1.4.7-0df48df2740c/map/geography.json", "application/json"),
    ("/data/1.4.7-0df48df2740c/map/locations.bin.gz", "application/octet-stream"),
    ("/map-place.json?v=1.4.7-0df48df2740c&place=location:constantinople&lang=en", "application/json")
]

all_passed = True
for path, expected_content_type in tests:
    try:
        url = f"{base}{path}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            ct = resp.headers.get("content-type", "")
            data = resp.read()
            status = resp.status
            match = expected_content_type in ct
            print(f"[{'PASS' if match else 'WARN'}] {path} -> status={status}, size={len(data)}, type={ct}")
            if not match:
                all_passed = False
    except Exception as e:
        print(f"[FAIL] {path} -> {e}")
        all_passed = False

if all_passed:
    print("\nALL TEST ENDPOINTS PASSED SUCCESSFULLY!")
else:
    print("\nSome tests failed or had warnings.")
