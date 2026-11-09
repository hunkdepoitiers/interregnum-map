import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\MapPage.CWs7aPan.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('loadFailed')
print("Around loadFailed:")
print(c[max(0, idx-400):min(len(c), idx+200)])
