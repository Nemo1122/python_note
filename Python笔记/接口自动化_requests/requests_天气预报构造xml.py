import requests

# import logging, sys
#
#
# logger = logging.getLogger('requests')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler(sys.stdout))


url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather"

# url = "http://fy.webxml.com.cn/webservices/EnglishChinese.asmx?wsdl"

body = """
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://WebXml.com.cn/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:getWeather>
         <!--Optional:-->
         <web:theCityCode>1117</web:theCityCode>
         <!--Optional:-->
         <web:theUserID></web:theUserID>
      </web:getWeather>
   </soapenv:Body>
</soapenv:Envelope>"""
#'Content-Type': 'text/xml;charset=UTF-8',
headers = {
    'Content-Type':'application/soap+xml;charset=utf-8',
    'SOAPAction':'http://WebXml.com.cn/getWeather',
    'Host': 'ws.webxml.com.cn',
    'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
    'Accept-Encoding': 'gzip,deflate'}

response = requests.post(url, data=body, headers=headers)
print(response.text)
