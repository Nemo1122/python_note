from suds.client import Client
from suds.xsd.sxbasic import TypeNotFound
from suds.xsd.doctor import ImportDoctor,Import


def client(wsdl, imp_add="http://WebXml.com.cn/"):
    """处理client异常"""

    try:
        client = Client(wsdl)
    except TypeNotFound as tnf:
        print(tnf)
        # 导入xsd
        imp = Import('http://www.w3.org/2001/XMLSchema',
                     location='http://www.w3.org/2001/XMLSchema.xsd')
        # 缺少targetNamespace="http://WebXml.com.cn/", wsdl申明最后一句
        imp.filter.add(imp_add)

        doctor = ImportDoctor(imp)
        client = Client(wsdl, doctor=doctor)

    return client

def get_all_methods(client):
    """查看服务接口"""
    return [method for method in client.wsdl.services[0].ports[0].methods]

def get_method_args(client, method_name):
    """查看某个具体接口的传输参数及类型"""
    method = client.wsdl.services[0].ports[0].methods[method_name]
    input_params = method.binding.input
    return input_params.param_defs(method)