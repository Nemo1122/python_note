# 装饰器
# “装饰器”（Decorator）。本质上，decorator就是一个返回函数的高阶函数。
def log(func):
    """
    wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()
    函数可以接受任意参数的调用。在wrapper()
    函数内，首先打印日志，再紧接着调用原始函数。
    """
    # 装饰器内部申明一个函数，这个函数用于执行额外的语句
    # 并返回原来（以参数形式传入的函数）的函数的调用，相当于这个wrapper函数就包含了原来的函数的调用
    def wrapper(*args, **kw):
        print("打印函数名称: %s" % func.__name__)
        return func(*args, **kw)
    # 装饰器的返回值是一个函数对象，因此不会马上执行，如果返回的是函数调用的话，就会马上执行。
    # 函数对象加一个括号，就是函数调用了
    return wrapper


# 借助Python的@语法，把decorator置于函数的定义处
@log
def now(x):
    print("直接打印x: ", x)

# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
# now(5)
# 打印函数名称: test
# 直接打印x:  5

# 把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
now(1)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
"""
    上面这句话不是很好理解，那么要怎么理解呢？
        其实@log这种装饰器放在函数定义的地方，就相当于给这个函数重新赋值了
            now = log(now)
        now就等于log()函数的返回值，返回值也就是wrapper函数对象，也就是没有括号的情况（函数带括号的时候是函数调用，
        没有括号的时候就是函数对象，函数对象加括号也就是调用了）
        现在这个now就有点类似我们的函数调用，比如 a = str(a), 这时候a就是str的返回值
        那么这个wrapper函数对象呢，其实就是log函数内部的函数：            
        def wrapper(*args, **kw):
            print("打印函数名称: %s" % func.__name__)
            return func(*args, **kw)
        这个wrapper先执行打印语句，再返回以参数形式传入的函数的调用
        def log(func):
            def wrapper(*args, **kw):
                print("打印函数名称: %s" % func.__name__)
                return func(*args, **kw)
            return wrapper
        那么这个时候返回的wrapper只是一个函数的对象，而不是调用，因此不会马上执行，如果return wrapper()，那么这个
        装饰器在装饰函数的时候就会执行了。      
        
"""



