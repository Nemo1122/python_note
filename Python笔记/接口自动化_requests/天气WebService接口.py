import requests
from bs4 import BeautifulSoup



# r = requests.get("http://m.weather.com.cn/data/101010100.html")
# print(r.content)

r = requests.get("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx")
# print(r.text)

# bs = BeautifulSoup(r.text, "lxml")
# for i in range(len(bs.select("span h3"))-1):
#     print(bs.select("li a")[i].string, bs.select("span h3")[1:][i].string,\
#           bs.select("span p")[1:][i].string)
"""
getRegionCountry 获得中国省份、直辖市、地区；国家名称（国外）和与之对应的ID None
getRegionDataset 获得中国省份、直辖市、地区和与之对应的ID 输入参数：无，返回数据：一维字符串数组。
getRegionProvince 获得支持的城市/地区名称和与之对应的ID 
getSupportCityDataset 获得支持的城市/地区名称和与之对应的ID 输入参数：无，返回数据：DataSet。
getSupportCityString 获得天气预报数据 
getWeather   获得天气预报数据  输入参数：城市/地区ID或名称，返回数据：一维字符串数组。
"""

# 获取支持国家
# r = requests.get("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionCountry",)
# print(r.text)

the_region_code = {"theRegionCode":31123}

# 获取支持城市
# r = requests.post("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString", data=the_region_code)
# print(r.text)



# 以post方式获取天气预报
# the_city_code = {"theCityCode": "1117", "theUserID":""}
# the_city_code_post_url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather"
# r = requests.post(the_city_code_post_url, data=the_city_code)
# print(r.text)

# 以get方式获取天气预报
the_city_code_get_url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather " \
                        "?theCityCode=1117&theUserID="
r = requests.get(the_city_code_get_url)
bs = BeautifulSoup(r.text, 'lxml')
for t in bs.select("string"):
    print(t.text)