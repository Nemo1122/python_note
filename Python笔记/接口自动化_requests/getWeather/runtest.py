import unittest
from HTMLTestRunner import HTMLTestRunner
from 接口自动化_requests.getWeather.test_WeatherWS_getWeather import TestGetWeather

suite = unittest.TestSuite()
suite.addTest(TestGetWeather("test_get_weather_success"))
suite.addTest(TestGetWeather("test_get_weather_no_city"))
suite.addTest(TestGetWeather("test_get_weather_no_user_id"))
suite.addTest(TestGetWeather("test_get_weather_default"))

with open('./report.html', 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        title='天气预报Web Service测试报告',
        description='测试Web Service接口情况'
    )
    runner.run(suite)