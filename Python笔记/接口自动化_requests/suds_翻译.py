from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import


url = "http://fy.webxml.com.cn/webservices/EnglishChinese.asmx?wsdl"

# 导入xsd
# imp= Import('http://www.w3.org/2001/XMLSchema',
#             location='http://www.w3.org/2001/XMLSchema.xsd')
#
# # 缺少targetNamespace="http://WebXml.com.cn/", wsdl文件最后一句
# imp.filter.add("http://WebXml.com.cn/")
#
# d = ImportDoctor(imp)

client = Client(url)

request = client.service.Translator(wordKey="is")

print(request)