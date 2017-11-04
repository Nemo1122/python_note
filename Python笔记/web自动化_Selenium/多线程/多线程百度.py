'''
在不同主机、不同浏览器同时执行测试用例，多线程；
利用Selenium Girl提供分布式执行测试用例；
先启动Selenium server，这里分别在本地主机启动一个hub和一个node，在其他主机（虚拟机）启动一个node。
'''
from selenium.webdriver import Remote
import threading
from time import *


# 测试用例
def baidu(host, browser):
    print("开始：%s" % ctime())
    print(host, browser)
    #dc = {'browserName': browser}
    dc = {
        'platform': 'ANY',
        'browserName': browser,
        'version': '',
        'javascriptEnabled': True
    }

    driver = Remote(
        command_executor=host,
        desired_capabilities=dc
    )
    try:
        driver.get(r'http://www.baidu.com')
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("新闻").click()
        sleep(2)
        driver.get_screenshot_as_file(r'.\baidu.jpg')
    finally:
        driver.quit()


if __name__ == '__main__':
    # 启动参数，指定运行主机和浏览器
    #lists = {'http://127.0.0.1:4444/wd/hub': 'chrome'#,
             #'http://127.0.0.1:5555/wd/hub': 'internet explorer'
             #'http://127.0.0.1:6666/wd/hub': 'firefox'  # 远程节点node
    #         }
    lists = {'http://169.254.55.201:4444/wd/hub': 'chrome'}
    for host, browser in lists.items():
        baidu(host, browser)
    # threads = []
    # files = range(len(lists))
    # # 创建线程，并append进线程组
    # for host, browser in lists.items():
    #     t = threading.Thread(target=baidu, args=(host, browser))
    #     threads.append(t)
    #     # 启动每一个线程
    # for i in files:
    #     threads[i].start()
    #     # 守护每一个线程
    # for i in files:
    #     threads[i].join()