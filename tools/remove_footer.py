import re

files = [
    r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\index.html",
    r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\map\index.html"
]

pattern = re.compile(r'<div class="sidebar-footer">.*?</div></div></nav>', re.DOTALL)

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content, count = pattern.subn('</nav>', content)
    print(f"File {fpath}: replaced {count} occurrence(s)")
    
    hide_css = '<style>.sidebar-footer, .site-footer { display: none !important; }</style></head>'
    new_content = new_content.replace('</head>', hide_css, 1)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Footer removal completed.")
