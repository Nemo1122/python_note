import requests
import json

# url = 'https://api.douban.com/v2/book/1220562'


url = 'https://api.douban.com/v2/movie/in_theaters'
# data = {"q": "后天"}
r = requests.post(url)
r.encoding = 'utf-8'

# ensure_ascii输出中文，需要设置为False
# indent美化级别，越大空格越多
print(json.dumps(r.json(), indent=4, ensure_ascii=False))