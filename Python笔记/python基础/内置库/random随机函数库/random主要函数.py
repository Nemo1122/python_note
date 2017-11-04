import random
import string


# random模块是Python自带的模块，除了生成最简单的随机数以外，还有很多功能。

# ----------------
# 1. random()方法, 用来生成一个0~1之间的随机浮点数,范围 0 <= n < 1.0
random.random()

# ----------------
# 2 . uniform(a, b)方法, 返回a, b之间的随机浮点数，范围[a, b]或[a, b), 取决于四舍五入,a不一定要比b小。

random.uniform(a, b)

# >>> random.uniform(50, 100)
# 76.81733455677832
# >>> random.uniform(100, 50)
# 52.98730193316595

# ----------------
# 3. randint(a, b)方法, 返回a, b之间的整数，范围[a, b]，注意：传入参数必须是整数，a一定要比b小
random.randint(a, b)


# >>> random.randint(50, 100)
# 54
# >>> random.randint(100, 50)
# 异常

# ----------------
# 4 . randrang([start], stop[, step]),返回有个区间内的整数，可以设置step。
# 只能传入整数，random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, … 96, 98]序列中获取一个随机数。

random.randrang([start], stop[, step])

# >>>random.randrange(100)
# 58
# >>>random.randrange(10, 100, 2)
# 54

# ----------------
# 5. choice(sequence),从序列中随机获取一个元素，list, tuple, 字符串都属于sequence。这里的sequence
# 需要是有序类型。random.randrange(10, 100, 2)在结果上与random.choice(range(10, 100, 2)等效。

random.choice(sequence)

# >>> random.choice(("stone", "scissors", "paper"))
#  'stone'
# >>> random.choice(["stone", "scissors", "paper"])
#  'scissors'
# >>> random.choice("Random")
#  'm'

# ----------------
# 6. shuffle(x[, random]),用于将列表中的元素打乱，俗称为洗牌。会修改原有序列。
random.shuffle(x[, random])

# >>> poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# >>> random.shuffle(poker)
# >>> poker
# ['4', '10', '8', '3', 'J', '6', '2', '7', '9', 'Q', '5', 'K', 'A']

# ----------------
# 7. sample(sequence, k),从指定序列中随机获取k个元素作为一个片段返回，sample函数不会修改原有序列。
random.sample(sequence, k)

# >>> poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# >>> random.sample(poker, 5)
# ['4', '3', '10', '2', 'Q']
