import unittest
from 接口自动化_requests.getWeather import function as func
import time


class TestGetWeather(unittest.TestCase):
    """测试天气预报Web Service中的getWeather方法
    getWeather(xs:string theCityCode, xs:string theUserID)
    """


    def setUp(self):
        self.wsdl = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl"


    def test_get_weather_success(self):
        """参数正确"""
        client = func.client(self.wsdl)
        # 1117为成都, 免费用户不用输入theUserID
        request = client.service.getWeather("1117")
        # 判断是否成都的天气
        self.assertIn("成都", request.string, "城市不符合预期")
        # 判断日期是否当天
        today = time.strftime("%Y/%m/%d", time.localtime())
        self.assertIn(today, request.string[3], "日期不符合预期")

    def test_get_weather_no_city(self):
        """城市id不存在"""
        client = func.client(self.wsdl)
        # 12345为不存在的城市, 免费用户不用输入theUserID
        request = client.service.getWeather("12345")
        # 判断结果是否判断为空
        self.assertIn("查询结果为空", request.string[0], "查询结果不符合预期，预期为空")

    def test_get_weather_no_user_id(self):
        """user id不存在"""
        client = func.client(self.wsdl)
        # 1117为成都, theUserID 123为不存在用户
        request = client.service.getWeather("1117", "123")
        # 判断结果是否判断为空
        self.assertIn("用户验证失败", request.string[0], "查询结果不符合预期，预期为用户验证失败")

    @unittest.skip
    def test_get_weather_default(self):
        """城市为空字符串取上海市的天气"""
        client = func.client(self.wsdl)
        # 城市为空字符串取上海市的天气
        request = client.service.getWeather("")
        # 判断是否成都的天气
        self.assertIn("上海", request.string, "城市不符合预期")
        # 判断日期是否当天
        today = time.strftime("%Y/%m/%d", time.localtime())
        self.assertIn(today, request.string[3], "日期不符合预期")

