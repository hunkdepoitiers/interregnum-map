import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\LocText.DchzC0nD.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('topography`,group:`land')
idx_start = c.rfind('var _t=', 0, idx)
if idx_start == -1:
    idx_start = c.rfind('_t=[', 0, idx)
print(c[idx_start:idx+300])
