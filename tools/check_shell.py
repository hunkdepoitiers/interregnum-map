with open(r'C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\public\_astro\Shell.astro_astro_type_script_index_0_lang.BRBsIu4H.js', 'r', encoding='utf-8') as f:
    c = f.read()

print("Is sidebar-footer in Shell.js?", "sidebar-footer" in c)
print("Is discord in Shell.js?", "discord" in c.lower())
