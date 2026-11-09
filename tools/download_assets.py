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

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

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

# Read site.html downloaded earlier
site_html_path = os.path.join(PUBLIC_DIR, "site.html")
with open(site_html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Clean up external tracker/ad scripts
cleaned_html = re.sub(r'<script defer src="https://analytics\.eu5db\.com[^>]*></script>', '', html_content)
cleaned_html = re.sub(r'<script data-cfasync="false" data-src="https://s\.nitropay\.com[^>]*>.*?</script>', '', cleaned_html, flags=re.DOTALL)
cleaned_html = re.sub(r'<script>\(function\(\)\{function c\(\)\{.*?</script>', '', cleaned_html, flags=re.DOTALL)
cleaned_html = re.sub(r'<script[^>]*cloudflareinsights[^>]*></script>', '', cleaned_html)

# Save as index.html and map/index.html
with open(os.path.join(PUBLIC_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(cleaned_html)
os.makedirs(os.path.join(PUBLIC_DIR, "map"), exist_ok=True)
with open(os.path.join(PUBLIC_DIR, "map", "index.html"), "w", encoding="utf-8") as f:
    f.write(cleaned_html)

# Download Favicon
curl_download(f"{BASE_URL}/favicon.svg", os.path.join(PUBLIC_DIR, "favicon.svg"))

# Download CSS and fonts
for css in re.findall(r'href="(/_astro/[^"]+\.css)"', html_content):
    curl_download(f"{BASE_URL}{css}", os.path.join(PUBLIC_DIR, css.lstrip("/")))
for font in re.findall(r'href="(/_astro/[^"]+\.woff2)"', html_content):
    curl_download(f"{BASE_URL}{font}", os.path.join(PUBLIC_DIR, font.lstrip("/")))

# Download initial JS
downloaded_js = set()
js_queue = set(re.findall(r'src="(/_astro/[^"]+\.js)"', html_content))

# Also add worker
js_queue.add("/_astro/nameWorker-Di2fxXLz.js")

while js_queue:
    js = js_queue.pop()
    if js in downloaded_js:
        continue
    rel = js.lstrip("/")
    target = os.path.join(PUBLIC_DIR, rel)
    if curl_download(f"{BASE_URL}{js}", target):
        downloaded_js.add(js)
        # Parse for more js references
        try:
            with open(target, "r", encoding="utf-8") as f:
                content = f.read()
            # find all _astro/*.js
            found = set(re.findall(r'[\'\"`](_astro/[a-zA-Z0-9_\-\.]+\.js)[\'\"`]', content))
            found.update(re.findall(r'\./([a-zA-Z0-9_\-\.]+\.js)', content))
            for fn in found:
                clean_fn = "/_astro/" + fn.replace("_astro/", "").replace("./", "")
                if clean_fn not in downloaded_js:
                    js_queue.add(clean_fn)
        except Exception as e:
            print(f"Error parsing {target}: {e}")

print(f"Total JS files downloaded: {len(downloaded_js)}")
