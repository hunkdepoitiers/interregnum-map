import os
import subprocess

PROJECT_DIR = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone"
PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")

concepts = [
    "country", "subject_type", "culture", "religion", "pop_type",
    "location_rank", "topography", "vegetation", "climate", "goods", "static_modifier"
]

version = "1.4.7-0df48df2740c"
list_hash = "ed43d1b61d8f"

# English lists
en_dir = os.path.join(PUBLIC_DIR, "data", version, "lists")
os.makedirs(en_dir, exist_ok=True)

for c in concepts:
    target = os.path.join(en_dir, f"{c}.json")
    if not os.path.exists(target) or os.path.getsize(target) == 0:
        url = f"https://eu5db.com/data/{version}/lists/{c}.json?d={list_hash}"
        subprocess.run(["curl.exe", "-sL", "-A", "Mozilla/5.0", url, "-o", target])
        print(f"Downloaded EN list: {c}.json ({os.path.getsize(target)} bytes)")

# Turkish lists
tr_dir = os.path.join(PUBLIC_DIR, "data", "tr", version, "lists")
os.makedirs(tr_dir, exist_ok=True)

tr_hash = "4f9d5290228f"
for c in concepts:
    target = os.path.join(tr_dir, f"{c}.json")
    if not os.path.exists(target) or os.path.getsize(target) == 0:
        url = f"https://eu5db.com/data/tr/{version}/lists/{c}.json?d={tr_hash}"
        subprocess.run(["curl.exe", "-sL", "-A", "Mozilla/5.0", url, "-o", target])
        print(f"Downloaded TR list: {c}.json ({os.path.getsize(target)} bytes)")

print("All lists downloaded successfully!")
