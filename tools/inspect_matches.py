import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML Matches:")
for m in re.finditer(r'(.{0,40}(?:EU5|Europa Universalis).{0,40})', html, re.IGNORECASE):
    print("  ", m.group(1).strip().replace('\n', ' '))

with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\en.Dp-Oj5Nc.js', 'r', encoding='utf-8') as f:
    en = f.read()

print("\nEN JS Matches:")
for m in re.finditer(r'(.{0,40}(?:EU5|Europa Universalis).{0,40})', en, re.IGNORECASE):
    print("  ", m.group(1).strip().replace('\n', ' '))
