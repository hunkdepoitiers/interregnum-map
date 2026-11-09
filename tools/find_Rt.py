import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\LocText.DchzC0nD.js', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'([a-zA-Z0-9_$]+)\s+as\s+Rt\b', c)
if m:
    orig = m.group(1)
    print("Rt is originally:", orig)
    for fm in re.finditer(rf'(?:function|var|let|const)\s+{orig}\b', c):
        print(c[fm.start():fm.start()+300])
