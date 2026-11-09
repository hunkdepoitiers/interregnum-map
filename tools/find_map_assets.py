import urllib.request
import re

headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request("https://eu5db.com/_astro/Loading.6HvX-Ljv.js", headers=headers)
c = urllib.request.urlopen(req).read().decode('utf-8')

print("Loading.js matches:")
matches = set(re.findall(r'[\'\"`]([^\'\"`]*\.bin[^\'\"`]*)[\'\"`]', c))
for m in matches:
    print(".bin match:", m)

matches_json = set(re.findall(r'[\'\"`]([^\'\"`]*map[^\'\"`]*\.json[^\'\"`]*)[\'\"`]', c))
for m in matches_json:
    print("map json match:", m)

matches_png = set(re.findall(r'[\'\"`]([^\'\"`]*map[^\'\"`]*\.(?:png|webp|avif|jpg|bin|dat)[^\'\"`]*)[\'\"`]', c))
for m in matches_png:
    print("map asset match:", m)
