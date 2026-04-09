import requests
res = requests.get("https://api.chucknorris.io/jokes/random").json()
print(res["value"])
