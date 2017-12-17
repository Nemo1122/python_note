import requests

url = "https://api.douban.com/v2/book/search"

# payload = "tag=%E8%AE%A1%E7%AE%97%E6%9C%BA&field=id%2Ctitle&count=30"
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "e650f860-3c64-31af-b201-002cc63e6de0"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

payload = {
    "tag": "计算机",
    "field": "id,title",
    "count": 5
}

response = requests.request("POST", url, data=payload)
print(response.json())