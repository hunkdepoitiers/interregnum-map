import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\MapPage.CWs7aPan.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('D.failed')
# Search backwards for D= or [D, or {failed:
matches = re.finditer(r'failed\b', c)
for m in matches:
    p = m.start()
    print("Match failed at", p)
    print(c[max(0, p-100):min(len(c), p+150)])
    print("="*40)
