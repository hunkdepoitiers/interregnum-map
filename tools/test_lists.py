import subprocess

concepts = [
    "country", "subject_type", "culture", "religion", "pop_type",
    "location_rank", "topography", "vegetation", "climate", "goods", "static_modifier"
]

version = "1.4.7-0df48df2740c"
base_url = f"https://eu5db.com/data/{version}/lists"

for c in concepts:
    url = f"{base_url}/{c}.json"
    res = subprocess.run(["curl.exe", "-sL", "-A", "Mozilla/5.0", "-w", "%{http_code}", "-o", "temp.json", url], capture_output=True, text=True)
    status = res.stdout.strip()
    with open("temp.json", "rb") as f:
        sz = len(f.read())
    print(f"List {c}.json -> status={status}, size={sz}")
