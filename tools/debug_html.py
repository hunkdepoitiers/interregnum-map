import re

with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\site.html', 'r', encoding='utf-8') as f:
    c = f.read()

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', c)
print("Scripts found:", scripts)
css = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', c)
print("CSS found:", css)
fonts = re.findall(r'<link[^>]+href=["\']([^"\']+\.woff2[^"\']*)["\']', c)
print("Fonts found:", fonts)
