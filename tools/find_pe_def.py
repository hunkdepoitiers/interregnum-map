import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\MapPage.CWs7aPan.js', 'r', encoding='utf-8') as f:
    c = f.read()

for m in re.finditer(r'(?:function\s+pe\b|var\s+pe\b|let\s+pe\b|const\s+pe\b)', c):
    p = m.start()
    print(c[p:p+300])
