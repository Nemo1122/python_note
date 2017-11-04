import string
import random

print(string.ascii_letters)    # 大小写字母
print(string.ascii_lowercase)  # 小写字母
print(string.ascii_uppercase)  # 大写字母

print(string.digits)  # 十进制数字
print(string.hexdigits)  # 十六进制
print(string.printable)  # 全字符
print(string.octdigits)   # 八进制

s = string.digits + string.ascii_letters

print(random.choices(s, k=6))
print(''.join(random.sample(s, 6)))

# random.sample(s, 5) 与 random.choices(s,k=5)基本等价

print(random.shuffle([7, 8, 9, 5],random=0.5))