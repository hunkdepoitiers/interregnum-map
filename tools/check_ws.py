import subprocess
import time
import json
import urllib.request
import asyncio
import sys

# Let's inspect console logs using CDP
async def check_console():
    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    proc = subprocess.Popen([
        chrome,
        "--headless=new",
        "--remote-debugging-port=9223",
        "--user-data-dir=" + os.path.abspath("temp_chrome_profile"),
        "--no-sandbox",
        "http://localhost:3000/map"
    ])
    
    await asyncio.sleep(4)
    
    try:
        tabs = json.loads(urllib.request.urlopen("http://localhost:9223/json").read())
        page_tab = next(t for t in tabs if "map" in t.get("url", ""))
        ws_url = page_tab["webSocketDebuggerUrl"]
        print("Connecting to ws:", ws_url)
    finally:
        proc.terminate()

# Let's run a simple python script to check if websockets is available, or use basic urllib
