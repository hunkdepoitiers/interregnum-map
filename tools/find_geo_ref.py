import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/bare-entry.CvDR_NEZ.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
all_js = set(re.findall(r'_astro/[a-zA-Z0-9_\-\.]+\.js', c))

print(f"Searching {len(all_js)} files for 'geography'...")
for js in sorted(all_js):
    req_file = urllib.request.Request(f"https://eu5db.com/{js}", headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req_file).read().decode('utf-8')
    if "geography" in data:
        print(f"Found in {js} (len={len(data)})")
        for m in re.finditer(r'(.{0,100}geography.{0,100})', data):
            print("  ", m.group(1))
