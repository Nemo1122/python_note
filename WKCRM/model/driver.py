from selenium import webdriver


def browser(browser_name="ch"):
    """启动浏览器，根据输入不同的浏览器名启动不同的浏览器"""
    if browser_name.lower() == "ie":
        driver = webdriver.Ie()
        return driver
    elif browser_name.lower() == "ff" or browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
        return driver
    elif browser_name.lower() == "ch" or browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
        return driver
    elif browser_name.lower() == "phantomjs" or browser_name.lower() == "ph":
        driver = webdriver.PhantomJS()
        return driver
    else:
        raise NameError("浏览器名称错误！请输入正确的浏览器名称，类似：ch,ff,ph,ie等并且不用区分大小写!")