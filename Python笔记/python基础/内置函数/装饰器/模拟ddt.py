def log(*data):
    def decorator(func):
        def wrapper():
            print("这是一个装饰器")
            for i in data:
                func(i)
        # 装饰器的返回值是一个函数对象，因此不会马上执行，如果返回的是函数调用的话，就会马上执行。
        # 函数对象加一个括号，就是函数调用了
        return wrapper()
    return decorator


@log('a','b','c','d')
def p(x):
    print('打印出来的值：', x)
