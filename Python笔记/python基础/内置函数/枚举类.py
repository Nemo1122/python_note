# 首先，定义枚举要导入enum模块。
# 枚举定义用class关键字，继承Enum类。
# 用于定义枚举的class和定义类的class是有区别


from enum import Enum,unique

# 如果要限制定义枚举时，不能定义相同值的成员。
# 可以使用装饰器@unique【要导入unique模块】
@unique
class Stage(Enum):
    first = 'F'
    second = 'S'
    third = 'T'

class Type(Enum):
    choice = 'C'
    choices = 'C'
    filling = 'F'

#  默认情况下，不同的成员值允许相同。但是两个相同值的成员，
#  第二个成员的名称被视作第一个成员的别名　
#  如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员　

# 用值取枚举成员
print(Stage('F'))
# <Stage.first: 'F'>

# 用成员名称取
print(Stage.first)
print(Stage['first'])
# <Stage.first: 'F'>


# 通过成员，来获取它的名称和值
first = Stage.first
print(first.name)
# 'first'
print(first.value)
# 'F'

# 枚举支持迭代器，可以遍历枚举成员,
for s in Stage:
    print(s)
# Stage.first
# Stage.second
# Stage.third

# 如果枚举有值重复的成员，循环遍历枚举时只获取值重复成员的第一个成员
# 如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__
for t in Type:
    print(t)
# Type.choice
# Type.filling

for t in Type.__members__.items():
    print(t)
# ('choice', <Type.choice: 'C'>)
# ('choices', <Type.choice: 'C'>)
# ('filling', <Type.filling: 'F'>)

"""
枚举比较
枚举成员可进行同一性比较
Color.red is Color.red
　　输出结果是：True

Color.red is not Color.blue
　　输出结果是：True

枚举成员可进等值比较

Color.blue == Color.red
　　输出结果是：False

Color.blue != Color.red
　　输出结果是：True

枚举成员不能进行大小比较

Color.red < Color.blue
　　输出结果出错：TypeError: unorderable types: Color() < Color()
"""