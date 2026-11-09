import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\MapPage.CWs7aPan.js', 'r', encoding='utf-8') as f:
    c = f.read()

for m in re.finditer(r'import\s*\{([^}]+)\}\s*from\s*["\']([^"\']+)["\']', c):
    items = m.group(1).split(',')
    for it in items:
        if ' as pe' in it or it.strip() == 'pe':
            print(f"pe imported from {m.group(2)}: {it}")
