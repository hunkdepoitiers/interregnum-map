import urllib.request
import json

headers = {"User-Agent": "Mozilla/5.0"}

def fetch(path):
    req = urllib.request.Request(f"https://eu5db.com{path}", headers=headers)
    return urllib.request.urlopen(req).read()

versions = json.loads(fetch("/data/versions.json"))
print("Versions:", versions)

geo_data = fetch("/data/1.4.7-0df48df2740c/map/geography.json")
print("Geography length:", len(geo_data))
geo = json.loads(geo_data)
print("Geography keys:", list(geo.keys()))
if "bitmap" in geo:
    print("Bitmap:", geo["bitmap"])
if "rivers" in geo:
    print("Rivers:", geo["rivers"])

start_data = fetch("/data/1.4.7-0df48df2740c/map/1337.4.1.json")
print("Start data length:", len(start_data))
start = json.loads(start_data)
print("Start keys:", list(start.keys()))
