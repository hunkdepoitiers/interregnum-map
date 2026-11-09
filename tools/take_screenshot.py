import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\Furkan Yusuf\.gemini\antigravity\scratch\eu5db-clone\screenshot.png"
url = "http://localhost:3000/map"

args = [
    chrome,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={out_img}",
    "--window-size=1600,1000",
    "--virtual-time-budget=7000",
    url
]

res = subprocess.run(args, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
if os.path.exists(out_img):
    print("Screenshot exists! Size:", os.path.getsize(out_img))
else:
    print("Screenshot does not exist.")
