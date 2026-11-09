import urllib.request
import re

bundle_url = "https://eu5db.com/_astro/bare-entry.CvDR_NEZ.js"
c = urllib.request.urlopen(urllib.request.Request(bundle_url, headers={"User-Agent": "Mozilla/5.0"})).read().decode('utf-8')

# extract all _astro/*.js
all_js = set(re.findall(r'_astro/[a-zA-Z0-9_\-\.]+\.js', c))
print("Found js files in bare-entry:", len(all_js))

# Let's inspect each to see which one has fetch() or map data loading
for js in sorted(all_js):
    try:
        url = f"https://eu5db.com/{js}"
        data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})).read().decode('utf-8')
        fetches = re.findall(r'fetch\([^\)]+\)', data)
        if fetches or "/data/" in data or ".bin" in data or "indexedDB" in data or "IDB" in data:
            print(f"File {js}: length={len(data)}, fetches={len(fetches)}, has /data/={'/data/' in data}, has .bin={'.bin' in data}")
            if fetches:
                print("  Sample fetch:", fetches[:3])
    except Exception as e:
        print(f"Error {js}: {e}")
