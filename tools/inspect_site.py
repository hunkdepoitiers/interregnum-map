import urllib.request
import re
import json

base_url = "https://eu5db.com"

# Fetch /map
req = urllib.request.Request(f"{base_url}/map", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Find all script and link tags
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
styles = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
preload_fonts = re.findall(r'<link[^>]+as=["\']font["\'][^>]+href=["\']([^"\']+)["\']', html)

print("Styles:", styles)
print("Scripts:", scripts)
print("Preload fonts:", preload_fonts)

# Also check for catalog or manifest or version
versions = re.findall(r'data-shell-version=["\']([^"\']+)["\']', html)
print("Versions:", versions)
