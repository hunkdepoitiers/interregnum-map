import os
import re
import urllib.request
import urllib.error
import gzip
import json

BASE_URL = "https://eu5db.com"
PROJECT_DIR = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone"
PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")
DATA_DIR = os.path.join(PUBLIC_DIR, "data")
ASTRO_DIR = os.path.join(PUBLIC_DIR, "_astro")

os.makedirs(PUBLIC_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ASTRO_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download_file(url, target_path):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
        return True
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            with open(target_path, "wb") as f:
                f.write(data)
        print(f"Downloaded: {url} -> {os.path.basename(target_path)} ({len(data)} bytes)")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Step 1: Download /map HTML
print("--- Fetching /map HTML ---")
req = urllib.request.Request(f"{BASE_URL}/map", headers=HEADERS)
html_content = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

# Clean up Cloudflare challenge & analytics & ads from HTML
cleaned_html = re.sub(r'<script defer src="https://analytics\.eu5db\.com[^>]*></script>', '', html_content)
cleaned_html = re.sub(r'<script data-cfasync="false" data-src="https://s\.nitropay\.com[^>]*>.*?</script>', '', cleaned_html, flags=re.DOTALL)
cleaned_html = re.sub(r'<script>\(function\(\)\{function c\(\)\{.*?</script>', '', cleaned_html, flags=re.DOTALL)
cleaned_html = re.sub(r'<script[^>]*cloudflareinsights[^>]*></script>', '', cleaned_html)

# Save as public/index.html and public/map/index.html
with open(os.path.join(PUBLIC_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(cleaned_html)
os.makedirs(os.path.join(PUBLIC_DIR, "map"), exist_ok=True)
with open(os.path.join(PUBLIC_DIR, "map", "index.html"), "w", encoding="utf-8") as f:
    f.write(cleaned_html)

# Step 2: Download favicon and fonts
download_file(f"{BASE_URL}/favicon.svg", os.path.join(PUBLIC_DIR, "favicon.svg"))

# Find all assets in HTML
css_links = re.findall(r'href="(/_astro/[^"]+\.css)"', html_content)
font_links = re.findall(r'href="(/_astro/[^"]+\.woff2)"', html_content)
js_scripts = re.findall(r'src="(/_astro/[^"]+\.js)"', html_content)

for css in css_links:
    download_file(f"{BASE_URL}{css}", os.path.join(PUBLIC_DIR, css.lstrip("/")))
for font in font_links:
    download_file(f"{BASE_URL}{font}", os.path.join(PUBLIC_DIR, font.lstrip("/")))
for js in js_scripts:
    download_file(f"{BASE_URL}{js}", os.path.join(PUBLIC_DIR, js.lstrip("/")))

print("HTML and primary assets saved.")
