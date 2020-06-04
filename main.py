import requests

url = "https://www.reddit.com/r/wallpapers.json"

payload = {}
headers = {'User-agent': 'WallpaperChanger'}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
