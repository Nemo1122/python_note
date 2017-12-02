from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor


url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl"

# 导入xsd
imp= Import('http://www.w3.org/2001/XMLSchema',
            location='http://www.w3.org/2001/XMLSchema.xsd')

# 缺少targetNamespace="http://WebXml.com.cn/", wsdl文件最后一句
imp.filter.add("http://WebXml.com.cn/")

d = ImportDoctor(imp)

client = Client(url, doctor=d)


request = client.service.getRegionCountry()

print(request)