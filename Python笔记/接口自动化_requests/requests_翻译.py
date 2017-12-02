import requests


url = "http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/Translator"

code = {"wordKey": "is"}

r = requests.post(url, data=code)

print(r.text)