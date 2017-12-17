#Content-Type text/xml; charset=utf-8

import requests
import bs4

url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather"

# payload = "theRegionCode=31123"
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "37f072f4-5ba0-2665-760a-9e2e84b1b4eb"
#     }

# response = requests.request("POST", url, data=payload)#, headers=headers)
# response = requests.post(url, data=payload, headers=headers)
# bs = bs4.BeautifulSoup(response.text, 'lxml')
# print(response.text)

# print(bs.find("string").child)


payload = {
    "theCityCode": "1117",
    "theUserID": ""
}
# requests.codes
r = requests.post(url, data=payload)
print(r.status_code)
print(r.text)