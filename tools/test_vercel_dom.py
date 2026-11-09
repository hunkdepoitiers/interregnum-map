import subprocess

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
res = subprocess.run([
    chrome, "--headless=new", "--dump-dom",
    "https://zippy-canyon-m5mkzfn.tmp.now/map"
], capture_output=True, text=True)

print("Stdout:", res.stdout[:300])
print("Stderr:", res.stderr[:300])
