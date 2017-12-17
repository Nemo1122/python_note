import requests
import time

url = "https://api.douban.com/v2/book/search"

querystring = {"q":"python"}

start = time.time()
print(start)
response = requests.request("GET", url, params=querystring)
print((time.time() - start))

start2 = time.time()
print(response.json()['count'])
print((time.time() - start2))