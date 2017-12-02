import requests
import bs4, re

# 登录
login_url = "http://localhost/ecshop/user.php"
login_data = {"username": "nemo",
              "password": "nemo19851",
              "act": "act_login"
              }

login = requests.post(login_url, data=login_data)

# print(re.search(r"登录成功", login.text))
print(login.text)
bs = bs4.BeautifulSoup(login.text, 'lxml')
print(bs.find("p").string)
# print(bs.select("a"))