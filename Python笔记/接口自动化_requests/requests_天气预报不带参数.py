"""
getRegionCountry 获得中国省份、直辖市、地区；国家名称（国外）和与之对应的ID None
getRegionDataset 获得中国省份、直辖市、地区和与之对应的ID 输入参数：无，返回数据：一维字符串数组。
getRegionProvince 获得支持的城市/地区名称和与之对应的ID
getSupportCityDataset 获得支持的城市/地区名称和与之对应的ID 输入参数：无，返回数据：DataSet。
getSupportCityString 获得天气预报数据
getWeather   获得天气预报数据  输入参数：城市/地区ID或名称，返回数据：一维字符串数组。
"""
import requests
import bs4


url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionCountry"
# url = "http://fy.webxml.com.cn/webservices/EnglishChinese.asmx?wsdl"

response = requests.get(url)
# bs = bs4.BeautifulSoup(response.text, 'lxml')
# 更改编码类型
# response.encoding = 'gbk'
# print(response.encoding)
print(response.text)