import subprocess
import time
import json
import urllib.request
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
proc = subprocess.Popen([
    chrome,
    "--headless=new",
    "--remote-debugging-port=9222",
    "--no-sandbox",
    "http://localhost:3000/map"
])

time.sleep(3)

try:
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    print("Open tabs:", len(tabs))
    for t in tabs:
        print("Tab:", t.get("title"), t.get("url"))
finally:
    proc.terminate()
