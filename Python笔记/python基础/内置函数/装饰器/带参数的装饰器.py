def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("打印装饰器变量:", text)
            return func(*args, **kw)
        # 装饰器的返回值是一个函数对象，因此不会马上执行，如果返回的是函数调用的话，就会马上执行。
        # 函数对象加一个括号，就是函数调用了
        return wrapper
    return decorator


@log('abc')
def now():
    print(1)

# abc()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
now = log('execute')(now)

"""
    我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
    再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
"""