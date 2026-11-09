import subprocess
import re

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
res = subprocess.run([
    chrome, "--headless=new", "--dump-dom",
    "https://zippy-canyon-m5mkzfn.tmp.now/map"
], capture_output=True, text=True)

titles = re.findall(r'<title>(.*?)</title>', res.stdout)
print("Title:", titles)
headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', res.stdout)
print("Headings:", headings)
