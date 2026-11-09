import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<div class="sidebar-footer">')
idx_nav_close = c.find('</nav>', idx)
print("From sidebar-footer to </nav>:")
print(c[idx:idx_nav_close+6])
