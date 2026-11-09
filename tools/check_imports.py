import urllib.request
import re

req = urllib.request.Request("https://eu5db.com/_astro/MapPage.CWs7aPan.js", headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Find imports
imports = re.findall(r'import\s*\{[^}]*\}\s*from\s*["\']([^"\']+)["\']', content)
print("Imports in MapPage:", imports)

all_imports = re.findall(r'from\s*["\']([^"\']+)["\']', content)
print("All imports in MapPage:", all_imports)
