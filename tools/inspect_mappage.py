import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Look for fetch or data references
print("Data matches:")
for m in re.finditer(r'fetch\([^\)]+\)', content):
    print(m.group(0))

print("\nStrings with /data/ or .bin or .json:")
for m in set(re.findall(r'["\']([^"\']*(?:/data/|\.bin|\.json|\.png|\.webp)[^"\']*)["\']', content)):
    if len(m) < 150:
        print(m)
