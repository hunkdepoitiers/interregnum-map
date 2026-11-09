import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\preload-helper.COQGF-qd.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
for m in re.finditer(r'(.{0,30}(?:EU5|Europa Universalis).{0,30})', c, re.IGNORECASE):
    print("Match in preload-helper:", m.group(1))
