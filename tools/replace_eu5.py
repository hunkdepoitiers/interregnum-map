import os
import re

PUBLIC_DIR = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public"

def replace_in_file(fpath):
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    
    orig = c
    # 1. First replace "Europa Universalis V" and "Europa Universalis"
    c = c.replace("Europa Universalis V", "Interregnum")
    c = c.replace("Europa Universalis", "Interregnum")
    
    # 2. Replace "EU5DB" with "InterregnumDB" (or "Interregnum")
    # For brand text specifically in HTML:
    c = c.replace('<span class="brand-text">EU5<span>DB</span></span>', '<span class="brand-text">Interregnum</span>')
    c = c.replace("EU5DB", "InterregnumDB")
    
    # 3. Replace word boundary "EU5" with "Interregnum"
    # Using regex to replace EU5 where it is a distinct word or followed by spaces/punctuation
    c = re.sub(r'\bEU5\b', 'Interregnum', c)
    
    if c != orig:
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(c)
        return True
    return False

# Files to update
targets = [
    os.path.join(PUBLIC_DIR, "index.html"),
    os.path.join(PUBLIC_DIR, "map", "index.html"),
]

# Add all js files in _astro
for root, dirs, files in os.walk(os.path.join(PUBLIC_DIR, "_astro")):
    for f in files:
        if f.endswith('.js'):
            targets.append(os.path.join(root, f))

updated_count = 0
for t in targets:
    if os.path.exists(t):
        if replace_in_file(t):
            updated_count += 1
            print(f"Updated: {os.path.basename(t)}")

print(f"\nFinished updating {updated_count} files!")
