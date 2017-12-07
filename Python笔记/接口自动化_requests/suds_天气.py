from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
# import logging, sys
#
#
# logger = logging.getLogger('suds')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler(sys.stdout))
#

url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl"

# 导入xsd
imp= Import('http://www.w3.org/2001/XMLSchema',
            location='http://www.w3.org/2001/XMLSchema.xsd')

# 缺少targetNamespace="http://WebXml.com.cn/", wsdl申明最后一句
imp.filter.add("http://WebXml.com.cn/")

d = ImportDoctor(imp)

client = Client(url, doctor=d)

# 查看服务接口
def get_all_methods(client):
    return [method for method in client.wsdl.services[0].ports[0].methods]
# print(get_all_methods(client))

# 查看某个具体接口的传输参数及类型
def get_method_args(client, method_name):
    method = client.wsdl.services[0].ports[0].methods[method_name]
    input_params = method.binding.input
    return input_params.param_defs(method)

# print(type(request))

# Methods (6):
#             getRegionCountry()
#             getRegionDataset()
#             getRegionProvince()
#             getSupportCityDataset(xs:string theRegionCode)
#             getSupportCityString(xs:string theRegionCode)
#             getWeather(xs:string theCityCode, xs:string theUserID)

# "四川,31123","成都,1117"

request = client.service.getSupportCityString("31123")
print(request.string)
for s in request.string:
    print(s)


