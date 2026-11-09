import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\LocText.DchzC0nD.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function xt(')
print(c[max(0, idx-500):idx+50])
