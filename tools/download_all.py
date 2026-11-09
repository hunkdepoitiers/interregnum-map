import os
import re
import subprocess
import json

BASE_URL = "https://eu5db.com"
PROJECT_DIR = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone"
PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")
DATA_DIR = os.path.join(PUBLIC_DIR, "data")
ASTRO_DIR = os.path.join(PUBLIC_DIR, "_astro")

os.makedirs(PUBLIC_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ASTRO_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0"

def curl_download(url, target_path):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
        return True
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    res = subprocess.run([
        "curl.exe", "-sL", "-A", USER_AGENT,
        url, "-o", target_path
    ])
    if res.returncode == 0 and os.path.exists(target_path) and os.path.getsize(target_path) > 0:
        print(f"Downloaded: {url} -> {os.path.basename(target_path)} ({os.path.getsize(target_path)} bytes)")
        return True
    else:
        print(f"Failed: {url}")
        return False

# Step 1: Clean and save HTML
site_test_path = os.path.join(PUBLIC_DIR, "site_test.html")
with open(site_test_path, "r", encoding="utf-8") as f:
    html_content = f.read()

cleaned_html = re.sub(r'<script defer src="https://analytics\.eu5db\.com[^>]*></script>', '', html_content)
cleaned_html = re.sub(r'<script data-cfasync="false" data-src="https://s\.nitropay\.com[^>]*>.*?</script>', '', cleaned_html, flags=re.DOTALL)
cleaned_html = re.sub(r'<script>\(function\(\)\{function c\(\)\{.*?</script>', '', cleaned_html, flags=re.DOTALL)
cleaned_html = re.sub(r'<script[^>]*cloudflareinsights[^>]*></script>', '', cleaned_html)

with open(os.path.join(PUBLIC_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(cleaned_html)
os.makedirs(os.path.join(PUBLIC_DIR, "map"), exist_ok=True)
with open(os.path.join(PUBLIC_DIR, "map", "index.html"), "w", encoding="utf-8") as f:
    f.write(cleaned_html)

# Step 2: Favicon & CSS & Fonts
curl_download(f"{BASE_URL}/favicon.svg", os.path.join(PUBLIC_DIR, "favicon.svg"))

for css in re.findall(r'href="(/_astro/[^"]+\.css)"', html_content):
    curl_download(f"{BASE_URL}{css}", os.path.join(PUBLIC_DIR, css.lstrip("/")))
for font in re.findall(r'href="(/_astro/[^"]+\.woff2)"', html_content):
    curl_download(f"{BASE_URL}{font}", os.path.join(PUBLIC_DIR, font.lstrip("/")))

# Step 3: Recursive JS downloading
downloaded_js = set()
js_queue = set(re.findall(r'src="(/_astro/[^"]+\.js)"', html_content))
js_queue.add("/_astro/nameWorker-Di2fxXLz.js")

while js_queue:
    js = js_queue.pop()
    if js in downloaded_js:
        continue
    rel = js.lstrip("/")
    target = os.path.join(PUBLIC_DIR, rel)
    if curl_download(f"{BASE_URL}{js}", target):
        downloaded_js.add(js)
        try:
            with open(target, "r", encoding="utf-8") as f:
                c = f.read()
            found = set(re.findall(r'["\'](_astro/[a-zA-Z0-9_\-\.]+\.js)["\']', c))
            found.update(re.findall(r'["\']\./([a-zA-Z0-9_\-\.]+\.js)["\']', c))
            for fn in found:
                clean_fn = "/_astro/" + fn.replace("_astro/", "").replace("./", "")
                if clean_fn not in downloaded_js:
                    js_queue.add(clean_fn)
        except Exception as e:
            print(f"Error reading {target}: {e}")

print(f"Total JS files downloaded: {len(downloaded_js)}")

# Step 4: Map Data Files for 1.4.7-0df48df2740c
version = "1.4.7-0df48df2740c"
map_hash = "e79d47c41710"

data_files = [
    ("versions.json", "versions.json"),
    (f"{version}/map/geography.json", f"data/{version}/map/geography.json"),
    (f"{version}/map/locations.bin.gz", f"data/{version}/map/locations.bin.gz"),
    (f"{version}/map/rivers.json", f"data/{version}/map/rivers.json"),
    (f"{version}/map/connections.json", f"data/{version}/map/connections.json"),
    (f"{version}/map/places.json", f"data/{version}/map/places.json"),
    (f"{version}/map/names.json", f"data/{version}/map/names.json"),
    (f"tr/{version}/map/names.json", f"data/tr/{version}/map/names.json"),
    (f"{version}/map/1337.4.1.json", f"data/{version}/map/1337.4.1.json"),
    (f"{version}/map/1337.4.1.pops.json", f"data/{version}/map/1337.4.1.pops.json"),
    (f"{version}/map/mentions.json", f"data/{version}/map/mentions.json"),
    (f"{version}/manifest.json", f"data/{version}/manifest.json"),
    # Preview images
    (f"{version}/map/preview-640.jpg", f"data/{version}/map/preview-640.jpg"),
    (f"{version}/map/preview-820.jpg", f"data/{version}/map/preview-820.jpg"),
    (f"{version}/map/preview-1236.jpg", f"data/{version}/map/preview-1236.jpg"),
    (f"{version}/map/preview-1648.jpg", f"data/{version}/map/preview-1648.jpg"),
    (f"{version}/map/preview-2472.jpg", f"data/{version}/map/preview-2472.jpg"),
    (f"{version}/map/preview-640.avif", f"data/{version}/map/preview-640.avif"),
    (f"{version}/map/preview-820.avif", f"data/{version}/map/preview-820.avif"),
    (f"{version}/map/preview-1236.avif", f"data/{version}/map/preview-1236.avif"),
    (f"{version}/map/preview-1648.avif", f"data/{version}/map/preview-1648.avif"),
    (f"{version}/map/preview-2472.avif", f"data/{version}/map/preview-2472.avif"),
]

for src_rel, dst_rel in data_files:
    url = f"{BASE_URL}/data/{src_rel}"
    target = os.path.join(PUBLIC_DIR, dst_rel)
    curl_download(url, target)

print("Asset downloading completed successfully!")
