import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\i18n.BNHApIHh.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('list:(e,t,n=`en`)')
if idx == -1:
    idx = c.find('list:(e,t,')
print(c[idx:idx+400])
