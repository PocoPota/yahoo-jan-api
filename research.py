import requests

url = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={YourAppId}"
payload = {"jan_code": "{TargetJanCode}"}

r = requests.get(url, params=payload)
json = r.json()

for i in range(20):
    print(json['hits'][i]['name'])
