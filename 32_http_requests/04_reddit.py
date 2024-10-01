import requests

base_url = "https://api.pushshift.io/reddit/comment/search/"
r = requests.get(base_url)
data = r.json()
print(data)
