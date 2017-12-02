from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

# 移动手机卡查询
url = "http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl"

client = Client(url)

# print(client)

result = client.service.getMobileCodeInfo("13408568554")

print(result)
