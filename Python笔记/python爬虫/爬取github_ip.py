import requests
from bs4 import BeautifulSoup

github_ip = [
    'github.com',
    'assets-cdn.github.com',
    'avatars0.githubusercontent.com',
    'avatars1.githubusercontent.com',
    'documentcloud.github.com',
    'gist.github.com',
    'help.github.com',
    'nodeload.github.com',
    'raw.github.com',
    'status.github.com',
    'training.github.com',
    'github.io'
]

for i in github_ip:
    url = "http://ip.chinaz.com/" + i.strip()
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    x = soup.find(class_="IcpMain02")
    x = x.find_all("span", class_="Whwtdhalf")
    print(x[5].string.strip(), i.strip())
