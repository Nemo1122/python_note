"""
 在类的继承中，如果重定义某个方法，该方法会覆盖父类的同名方法，
 但有时，我们希望能同时实现父类的功能，
 这时，我们就需要调用父类的方法了，可通过使用 super 来实现，比如：
"""


class Father():
    def __init__(self):
        self.f_a = "father"

    def fp(self):
        return self.f_a


class Son(Father):
    def __init__(self):
        super().__init__()
        self.s_b = "son"

    def sp(self):
        print("子类打印自身的属性：%s" % self.s_b)

    def fp(self):
        s_f_a = super().fp()
        print("子类打印父类的属性：%s" % self.f_a)
        print("子类打印父类fp方法的返回值:%s" % s_f_a)


"""
————————————————————————————————————————————
son = Son()
son.sp()
son.fp()

结果：
子类打印自身的属性：son
子类打印父类的属性：father
子类打印父类fp方法的返回值:father
————————————————————————————————————————————
其实就是通过super()调用父类的方法的概念
"""


""" 
看了上面的使用，你可能会觉得 super 的使用很简单，无非就是获取了父类，
并调用父类的方法。其实，在上面的情况下，super 获得的类刚好是父类，
但在其他情况就不一定了，super 其实和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类，下一个类可能是父类，也可能是并行的类，
主要是看MRO列表中的顺序。
"""

# 让我们看一个稍微复杂的例子，涉及到多重继承，代码如下：


class Base(object):

    def __init__(self):
        print("------")
        print("Base")
        print("Level 1")
        print("------")


class SonClass(Base):

    def __init__(self):
        print("SonClass")
        super().__init__()
        print("Level 2")


class DaughterinlawClass(Base):  #daughter-in-law 儿媳妇:）
    def __init__(self):
        print("DaughterClass")
        super().__init__()
        print("Level 2")


class GrandsonClass(SonClass, DaughterinlawClass):
    def __init__(self):
        print("GrandsonClass")
        super().__init__()
        print("Level 3")

"""
其中，Base 是父类，A, B 继承自 Base, C 继承自 A, B，它们的继承关系如下：
        Base
        /  \
SonClass    DaughterinlawClass
        \  /
    GrandsonClass
根据这个图，SonClass用super，应该调用Base中的方法。
——————————————————————————————————————————————
g = GrandsonClass()
结果：
GrandsonClass
SonClass
DaughterClass
------
Base
Level 1
------
Level 2
Level 2
Level 3
——————————————————————————————————————————————
但是实际结果SonClass用super的时候，调用的却是DaughterClass，然后才是Base。
事实上，对于你定义的每一个类，Python 会计算出一个方法解析顺序（Method Resolution Order, MRO）列表，
它代表了类继承的顺序，我们可以使用下面的方式获得某个类的 MRO 列表：
"""
"""
print(GrandsonClass.mro())
结果：
[<class '__main__.GrandsonClass'>, <class '__main__.SonClass'>, <class '__main__.DaughterinlawClass'>, <class '__main__.Base'>, <class 'object'>]
"""

"""
那这个 MRO 列表的顺序是怎么定的呢，它是通过一个 C3 线性化算法来实现的，
这里我们就不去深究这个算法了，感兴趣的读者可以自己去了解一下，
总的来说，一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：
1. 子类永远在父类前面
2. 如果有多个父类，会根据它们在列表中的顺序被检查
3. 如果对下一个类存在两个合法的选择，选择第一个父类
"""
# super 的工作原理如下：
r"""
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
其中，cls 代表类，inst 代表实例，上面的代码做了两件事：

获取 inst 的 MRO 列表
查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]
当你使用 super(cls, inst) 时，Python 会在 inst 的 MRO 列表上搜索 cls 的下一个类。

现在，让我们回到前面的例子。

首先看类 C 的 __init__ 方法：
    super(C, self).__init__()
这里的 self 是当前 C 的实例，self.__class__.mro() 结果是：
[__main__.C, __main__.A, __main__.B, __main__.Base, object]
可以看到，C 的下一个类是 A，于是，跳到了 A 的 __init__，这时会打印出 enter A，并执行下面一行代码：

super(A, self).__init__()

注意，这里的 self 也是当前 C 的实例，MRO 列表跟上面是一样的，搜索 A 在 MRO 中的下一个类，发现是 B，于是，跳到了 B 的 __init__，这时会打印出 enter B，而不是 enter Base。

整个过程还是比较清晰的，关键是要理解 super 的工作方式，而不是想当然地认为 super 调用了父类的方法。
"""

"""
小结

事实上，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。
"""