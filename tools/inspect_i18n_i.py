import urllib.request

req = urllib.request.Request("https://eu5db.com/_astro/i18n.BNHApIHh.js", headers={"User-Agent": "Mozilla/5.0"})
c = urllib.request.urlopen(req).read().decode('utf-8')
idx = c.find('Br=(e,t)=>')
print(c[idx-500:idx])
