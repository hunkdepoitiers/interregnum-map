import os
import re

PUBLIC_DIR = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public"

js_files = []
for root, dirs, files in os.walk(os.path.join(PUBLIC_DIR, "_astro")):
    for f in files:
        if f.endswith('.js'):
            js_files.append(os.path.join(root, f))

for jf in js_files:
    with open(jf, "r", encoding="utf-8") as f:
        c = f.read()
    # Find all occurrences of EU5 or Europa
    matches = re.findall(r'[^a-zA-Z0-9_$](?:EU5|Europa Universalis)[^a-zA-Z0-9_$]', c)
    if matches:
        print(f"{os.path.basename(jf)}: {len(matches)} matches")
        # Print sample
        for m in re.finditer(r'([^\'\"`\n]{0,30}(?:EU5|Europa Universalis)[^\'\"`\n]{0,30})', c):
            print("   Sample:", m.group(1))
            break
