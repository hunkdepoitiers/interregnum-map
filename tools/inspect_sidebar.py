with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<nav class="sidebar".*?</nav>', c, re.DOTALL)
if matches:
    print("Found sidebar! Length:", len(matches[0]))
    # print the last 1500 chars of sidebar
    print(matches[0][-1500:])
else:
    print("Sidebar tag not matched directly")
