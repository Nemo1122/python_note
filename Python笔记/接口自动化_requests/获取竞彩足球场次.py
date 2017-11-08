import requests
import bs4, re


r = requests.get('http://m.xiaomicp.com/android_asset/www/shopmicai/shoppage/jcz/jczpage.html?chi=1#?page=hhtz')
# 解决中文乱码问题
r.encoding = 'utf-8'
print(r.text)
print(re.search(r'今天', r.text).group())
