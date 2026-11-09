import os
import re

PUBLIC_DIR = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public"

matches = []
for root, dirs, files in os.walk(PUBLIC_DIR):
    for f in files:
        if f.endswith(('.html', '.js', '.json', '.svg', '.css')):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
                eu5_count = len(re.findall(r'\bEU5\b|EU5DB|Europa Universalis', content, re.IGNORECASE))
                if eu5_count > 0:
                    matches.append((os.path.relpath(fpath, PUBLIC_DIR), eu5_count))
            except Exception as e:
                pass

for rel, cnt in sorted(matches, key=lambda x: -x[1])[:30]:
    print(f"{rel}: {cnt} matches")
