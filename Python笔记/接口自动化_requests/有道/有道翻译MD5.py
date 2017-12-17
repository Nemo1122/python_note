import hashlib
import requests
import random


url = 'https://openapi.youdao.com/api'

# appKey+q+salt+密钥
# salt为随机数，q为查询字符串，密钥为应用密钥， 应用ID为appkey
salt = random.randint(1, 65536)
appKey = '4aaf4f0434b6bd8e'
secretKey = 'vxt0kJPUzL4Hq6KtqkOKl0ZegjYtLsrP'
# 查询相关
q = 'good'
fromLang = 'EN'
toLang = 'zh-CHS'

# 按要求组合字符串
sign = appKey + q + str(salt) + secretKey
# 将字符串转为MD5码
sign = hashlib.md5(sign.encode('utf-8')).hexdigest()#.upper()
print(sign)

payload = {
    'appKey': appKey,
    'q': q,
    'from': fromLang,
    'to': toLang,
    'salt': str(salt),
    'sign': sign
}

r = requests.get(url, params=payload)
print(r.url)
print(r.json())

