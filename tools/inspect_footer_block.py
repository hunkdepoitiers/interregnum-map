import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('About EU5DB')
print(c[max(0, idx-200):idx+500])
